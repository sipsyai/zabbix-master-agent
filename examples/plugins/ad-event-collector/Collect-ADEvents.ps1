#Requires -Version 5.1
#Requires -RunAsAdministrator

<#
.SYNOPSIS
    Active Directory Event Collector for Zabbix
.DESCRIPTION
    Collects AD events from Windows Event Logs and sends to Zabbix Server
.PARAMETER TimeWindow
    Minutes to look back for events (default: 5)
.PARAMETER ZabbixServer
    Zabbix server IP/hostname
.PARAMETER ZabbixPort
    Zabbix server port (default: 10051)
.PARAMETER HostName
    Zabbix host name (default: DC01)
.PARAMETER ConfigPath
    Path to event-mapping.json configuration file
.EXAMPLE
    .\Collect-ADEvents.ps1 -TimeWindow 5 -ZabbixServer 192.168.213.141
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $false)]
    [int]$TimeWindow = 5,

    [Parameter(Mandatory = $false)]
    [string]$ZabbixServer = "192.168.213.141",

    [Parameter(Mandatory = $false)]
    [int]$ZabbixPort = 10051,

    [Parameter(Mandatory = $false)]
    [string]$HostName = "DC01",

    [Parameter(Mandatory = $false)]
    [string]$ConfigPath = "$PSScriptRoot\event-mapping.json",

    [Parameter(Mandatory = $false)]
    [string]$ZabbixSenderPath = "C:\Program Files\Zabbix Agent 2\zabbix_sender.exe"
)

#region Helper Functions

function Write-Log {
    param(
        [string]$Message,
        [ValidateSet('Info', 'Warning', 'Error')]
        [string]$Level = 'Info'
    )

    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $logMessage = "[$timestamp] [$Level] $Message"

    switch ($Level) {
        'Error'   { Write-Host $logMessage -ForegroundColor Red }
        'Warning' { Write-Host $logMessage -ForegroundColor Yellow }
        'Info'    { Write-Host $logMessage -ForegroundColor Cyan }
    }

    # Also log to file
    $logFile = "$PSScriptRoot\ad-event-collector.log"
    Add-Content -Path $logFile -Value $logMessage
}

function Get-EventConfig {
    param([string]$Path)

    if (-not (Test-Path $Path)) {
        Write-Log "Configuration file not found: $Path" -Level Error
        throw "Configuration file not found"
    }

    try {
        $config = Get-Content $Path -Raw | ConvertFrom-Json
        Write-Log "Loaded configuration from: $Path"
        return $config
    }
    catch {
        Write-Log "Failed to parse configuration: $_" -Level Error
        throw
    }
}

function Get-ADEvents {
    param(
        [string[]]$EventIDs,
        [datetime]$StartTime,
        [string]$LogName = 'Security'
    )

    $filterXml = @"
<QueryList>
  <Query Id="0" Path="$LogName">
    <Select Path="$LogName">
      *[System[(EventID=$($EventIDs -join ' or EventID=')) and TimeCreated[@SystemTime&gt;='$($StartTime.ToUniversalTime().ToString('o'))']]]
    </Select>
  </Query>
</QueryList>
"@

    try {
        $events = Get-WinEvent -FilterXml $filterXml -ErrorAction SilentlyContinue
        return $events
    }
    catch {
        if ($_.Exception.Message -notlike "*No events were found*") {
            Write-Log "Error reading events from $LogName : $_" -Level Warning
        }
        return @()
    }
}

function Parse-EventData {
    param(
        [System.Diagnostics.Eventing.Reader.EventLogRecord]$Event
    )

    $eventData = @{
        TimeCreated = $Event.TimeCreated.ToString('o')
        EventID = $Event.Id
        Level = $Event.LevelDisplayName
        Computer = $Event.MachineName
        Message = $Event.Message
        EventRecordID = $Event.RecordId
    }

    # Parse event properties
    if ($Event.Properties) {
        $properties = @{}
        for ($i = 0; $i -lt $Event.Properties.Count; $i++) {
            $properties["Property$i"] = $Event.Properties[$i].Value
        }
        $eventData['Properties'] = $properties
    }

    # Extract common fields based on Event ID
    switch ($Event.Id) {
        4624 { # Successful Logon
            if ($Event.Properties.Count -ge 9) {
                $eventData['TargetUserName'] = $Event.Properties[5].Value
                $eventData['TargetDomainName'] = $Event.Properties[6].Value
                $eventData['LogonType'] = $Event.Properties[8].Value
                $eventData['IpAddress'] = $Event.Properties[18].Value
                $eventData['WorkstationName'] = $Event.Properties[11].Value
            }
        }
        4625 { # Failed Logon
            if ($Event.Properties.Count -ge 13) {
                $eventData['TargetUserName'] = $Event.Properties[5].Value
                $eventData['TargetDomainName'] = $Event.Properties[6].Value
                $eventData['LogonType'] = $Event.Properties[10].Value
                $eventData['FailureReason'] = $Event.Properties[8].Value
                $eventData['IpAddress'] = $Event.Properties[19].Value
                $eventData['WorkstationName'] = $Event.Properties[13].Value
            }
        }
        { $_ -in 4720, 4726, 4738, 4722, 4725 } { # User Account Changes
            if ($Event.Properties.Count -ge 1) {
                $eventData['TargetUserName'] = $Event.Properties[0].Value
                $eventData['TargetDomainName'] = $Event.Properties[1].Value
                $eventData['SubjectUserName'] = $Event.Properties[4].Value
                $eventData['SubjectDomainName'] = $Event.Properties[5].Value
            }
        }
        { $_ -in 4728, 4729, 4732, 4733 } { # Group Membership Changes
            if ($Event.Properties.Count -ge 2) {
                $eventData['MemberName'] = $Event.Properties[0].Value
                $eventData['GroupName'] = $Event.Properties[2].Value
                $eventData['SubjectUserName'] = $Event.Properties[4].Value
                $eventData['SubjectDomainName'] = $Event.Properties[5].Value
            }
        }
        { $_ -in 4741, 4742, 4743 } { # Computer Account Changes
            if ($Event.Properties.Count -ge 1) {
                $eventData['TargetComputerName'] = $Event.Properties[0].Value
                $eventData['SubjectUserName'] = $Event.Properties[4].Value
                $eventData['SubjectDomainName'] = $Event.Properties[5].Value
            }
        }
    }

    return $eventData
}

function Send-ToZabbix {
    param(
        [string]$Server,
        [int]$Port,
        [string]$Host,
        [string]$Key,
        [string]$Value,
        [string]$SenderPath
    )

    if (-not (Test-Path $SenderPath)) {
        Write-Log "Zabbix sender not found at: $SenderPath" -Level Error
        return $false
    }

    # Create temp file for zabbix_sender input
    $tempFile = [System.IO.Path]::GetTempFileName()

    try {
        # Escape special characters in JSON
        $escapedValue = $Value -replace '"', '\"' -replace '\\', '\\'

        # Write data in zabbix_sender format
        $data = "$Host $Key $escapedValue"
        Set-Content -Path $tempFile -Value $data -Encoding UTF8

        # Send to Zabbix
        $arguments = @(
            "-z", $Server,
            "-p", $Port,
            "-i", $tempFile,
            "-vv"
        )

        $result = & $SenderPath $arguments 2>&1

        if ($LASTEXITCODE -eq 0) {
            Write-Log "Successfully sent data for key: $Key"
            return $true
        }
        else {
            Write-Log "Failed to send data for key ${Key}: $result" -Level Warning
            return $false
        }
    }
    catch {
        Write-Log "Error sending to Zabbix: $_" -Level Error
        return $false
    }
    finally {
        if (Test-Path $tempFile) {
            Remove-Item $tempFile -Force
        }
    }
}

#endregion

#region Main Script

try {
    Write-Log "=========================================="
    Write-Log "AD Event Collector - Starting"
    Write-Log "=========================================="
    Write-Log "Time Window: $TimeWindow minutes"
    Write-Log "Zabbix Server: ${ZabbixServer}:${ZabbixPort}"
    Write-Log "Zabbix Host: $HostName"

    # Load configuration
    $config = Get-EventConfig -Path $ConfigPath

    # Calculate time range
    $startTime = (Get-Date).AddMinutes(-$TimeWindow)
    Write-Log "Collecting events since: $($startTime.ToString('yyyy-MM-dd HH:mm:ss'))"

    # Process each category
    $totalEvents = 0
    $categorySummary = @{}

    foreach ($categoryName in $config.categories.PSObject.Properties.Name) {
        $category = $config.categories.$categoryName

        Write-Log "Processing category: $($category.name)"

        # Get all event IDs for this category
        $eventIDs = $category.events.PSObject.Properties.Name

        if ($eventIDs.Count -eq 0) {
            Write-Log "  No event IDs defined for category: $categoryName" -Level Warning
            continue
        }

        # Collect events
        $events = Get-ADEvents -EventIDs $eventIDs -StartTime $startTime

        Write-Log "  Found $($events.Count) events"
        $totalEvents += $events.Count

        # Parse events
        $parsedEvents = @()
        foreach ($event in $events) {
            $parsedEvent = Parse-EventData -Event $event
            $parsedEvents += $parsedEvent
        }

        # Create summary
        $summary = @{
            category = $categoryName
            category_name = $category.name
            description = $category.description
            time_window_minutes = $TimeWindow
            start_time = $startTime.ToString('o')
            end_time = (Get-Date).ToString('o')
            event_count = $events.Count
            events = $parsedEvents
        }

        # Group by Event ID
        $eventGroups = $parsedEvents | Group-Object -Property EventID
        $eventBreakdown = @{}
        foreach ($group in $eventGroups) {
            $eventID = $group.Name
            $eventName = $category.events.$eventID
            $eventBreakdown[$eventID] = @{
                event_id = $eventID
                event_name = $eventName
                count = $group.Count
            }
        }
        $summary['event_breakdown'] = $eventBreakdown

        $categorySummary[$categoryName] = $summary

        # Send to Zabbix
        $jsonData = $summary | ConvertTo-Json -Depth 10 -Compress
        $zabbixKey = "ad.events[$categoryName]"

        $sent = Send-ToZabbix -Server $ZabbixServer -Port $ZabbixPort `
                              -Host $HostName -Key $zabbixKey `
                              -Value $jsonData -SenderPath $ZabbixSenderPath

        if (-not $sent) {
            Write-Log "  Failed to send data for category: $categoryName" -Level Warning
        }
    }

    # Send overall summary
    $overallSummary = @{
        collection_time = (Get-Date).ToString('o')
        time_window_minutes = $TimeWindow
        total_events = $totalEvents
        categories_processed = $categorySummary.Count
        categories = $categorySummary
    }

    $overallJson = $overallSummary | ConvertTo-Json -Depth 10 -Compress
    Send-ToZabbix -Server $ZabbixServer -Port $ZabbixPort `
                  -Host $HostName -Key "ad.events[summary]" `
                  -Value $overallJson -SenderPath $ZabbixSenderPath

    Write-Log "=========================================="
    Write-Log "Collection Complete"
    Write-Log "Total Events Collected: $totalEvents"
    Write-Log "Categories Processed: $($categorySummary.Count)"
    Write-Log "=========================================="
}
catch {
    Write-Log "Fatal error: $_" -Level Error
    Write-Log $_.ScriptStackTrace -Level Error
    exit 1
}

#endregion
