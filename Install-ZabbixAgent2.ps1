<#
.SYNOPSIS
    Zabbix Agent'tan Agent2'ye geçiş scripti

.DESCRIPTION
    Bu script, Windows sunucusunda Zabbix Agent'tan Agent2'ye geçişi otomatikleştirir.
    Hem lokal hem de remote sunucularda çalışabilir.

.PARAMETER ComputerName
    Hedef sunucu adı (opsiyonel, varsayılan: localhost)

.PARAMETER ZabbixServer
    Zabbix Server IP adresi

.PARAMETER Hostname
    Zabbix'te görünecek host adı

.PARAMETER Agent2MSIPath
    Agent2 MSI dosyasının yolu

.EXAMPLE
    .\Install-ZabbixAgent2.ps1 -ZabbixServer "192.168.213.141" -Hostname "WinServer01"

.EXAMPLE
    .\Install-ZabbixAgent2.ps1 -ComputerName "SERVER01" -ZabbixServer "192.168.213.141" -Hostname "WinServer01" -Agent2MSIPath "C:\temp\zabbix_agent2.msi"
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory=$false)]
    [string]$ComputerName = "localhost",

    [Parameter(Mandatory=$true)]
    [string]$ZabbixServer,

    [Parameter(Mandatory=$true)]
    [string]$Hostname,

    [Parameter(Mandatory=$false)]
    [string]$Agent2MSIPath = ".\zabbix_agent2-7.0.0-windows-amd64-openssl.msi",

    [Parameter(Mandatory=$false)]
    [string]$ServerActive = "",

    [Parameter(Mandatory=$false)]
    [int]$ListenPort = 10050,

    [Parameter(Mandatory=$false)]
    [switch]$RemoveOldAgent = $false,

    [Parameter(Mandatory=$false)]
    [switch]$BackupConfig = $true
)

# Renkli output için fonksiyonlar
function Write-ColorOutput {
    param(
        [Parameter(Mandatory=$true)]
        [string]$Message,
        [Parameter(Mandatory=$false)]
        [string]$Color = "White"
    )
    Write-Host $Message -ForegroundColor $Color
}

function Write-Success {
    param([string]$Message)
    Write-ColorOutput "✓ $Message" -Color Green
}

function Write-Error {
    param([string]$Message)
    Write-ColorOutput "❌ $Message" -Color Red
}

function Write-Warning {
    param([string]$Message)
    Write-ColorOutput "⚠ $Message" -Color Yellow
}

function Write-Info {
    param([string]$Message)
    Write-ColorOutput "ℹ $Message" -Color Cyan
}

# ServerActive varsayılan değeri
if ([string]::IsNullOrEmpty($ServerActive)) {
    $ServerActive = "${ZabbixServer}:10051"
}

Write-ColorOutput "`n========================================" -Color Magenta
Write-ColorOutput "ZABBIX AGENT → AGENT2 MIGRATION" -Color Magenta
Write-ColorOutput "========================================`n" -Color Magenta

Write-Info "Hedef Sunucu: $ComputerName"
Write-Info "Zabbix Server: $ZabbixServer"
Write-Info "Hostname: $Hostname"
Write-Info "MSI Path: $Agent2MSIPath"

# MSI dosyası kontrolü
if (-not (Test-Path $Agent2MSIPath)) {
    Write-Error "Agent2 MSI dosyası bulunamadı: $Agent2MSIPath"
    Write-Info "MSI dosyasını https://www.zabbix.com/download_agents adresinden indirin"
    exit 1
}

Write-Success "Agent2 MSI dosyası bulundu"

# Script block - Remote veya local çalıştırılacak
$ScriptBlock = {
    param($ZabbixServer, $ServerActive, $Hostname, $ListenPort, $RemoveOldAgent, $BackupConfig, $Agent2TempPath)

    # Eski Agent servis kontrolü
    Write-Host "`n[1/7] Mevcut Zabbix Agent kontrolü..."
    $oldAgentService = Get-Service -Name "Zabbix Agent" -ErrorAction SilentlyContinue

    if ($oldAgentService) {
        Write-Host "  → Mevcut Agent bulundu: $($oldAgentService.Status)"

        # Eski konfig yedekleme
        if ($BackupConfig) {
            Write-Host "`n[2/7] Mevcut konfigürasyon yedekleniyor..."
            $configPath = "C:\Program Files\Zabbix Agent\zabbix_agentd.conf"
            if (Test-Path $configPath) {
                $backupPath = "${configPath}.backup_$(Get-Date -Format 'yyyyMMdd_HHmmss')"
                Copy-Item $configPath $backupPath -Force
                Write-Host "  → Yedek oluşturuldu: $backupPath" -ForegroundColor Green
            }
        }

        # Servisi durdur
        Write-Host "`n[3/7] Eski Agent servisi durduruluyor..."
        if ($oldAgentService.Status -eq 'Running') {
            Stop-Service "Zabbix Agent" -Force
            Start-Sleep -Seconds 2
            Write-Host "  → Servis durduruldu" -ForegroundColor Green
        }

        # Eski agent'ı kaldır
        if ($RemoveOldAgent) {
            Write-Host "`n[4/7] Eski Agent kaldırılıyor..."
            sc.exe delete "Zabbix Agent" | Out-Null
            Write-Host "  → Eski Agent servisi kaldırıldı" -ForegroundColor Green
        } else {
            Write-Host "`n[4/7] Eski Agent saklanıyor (RemoveOldAgent=false)" -ForegroundColor Yellow
        }
    } else {
        Write-Host "  → Mevcut Agent bulunamadı" -ForegroundColor Yellow
        Write-Host "`n[2/7] Konfig yedekleme - Atlandı"
        Write-Host "`n[3/7] Servis durdurma - Atlandı"
        Write-Host "`n[4/7] Eski Agent kaldırma - Atlandı"
    }

    # Agent2 kurulumu
    Write-Host "`n[5/7] Zabbix Agent2 kuruluyor..."
    $installArgs = @(
        "/i", $Agent2TempPath,
        "/qn",
        "SERVER=$ZabbixServer",
        "SERVERACTIVE=$ServerActive",
        "HOSTNAME=$Hostname",
        "LISTENPORT=$ListenPort",
        "ENABLEPATH=1",
        "TLSCONNECT=unencrypted",
        "TLSACCEPT=unencrypted"
    )

    $process = Start-Process "msiexec.exe" -ArgumentList $installArgs -Wait -PassThru -NoNewWindow

    if ($process.ExitCode -eq 0) {
        Write-Host "  → Agent2 başarıyla kuruldu" -ForegroundColor Green
    } else {
        Write-Host "  → Kurulum hatası! Exit code: $($process.ExitCode)" -ForegroundColor Red
        return $false
    }

    # Servis kontrolü
    Write-Host "`n[6/7] Agent2 servisi kontrol ediliyor..."
    Start-Sleep -Seconds 3
    $agent2Service = Get-Service -Name "Zabbix Agent 2" -ErrorAction SilentlyContinue

    if ($agent2Service) {
        Write-Host "  → Servis durumu: $($agent2Service.Status)" -ForegroundColor Cyan

        if ($agent2Service.Status -ne 'Running') {
            Write-Host "  → Servis başlatılıyor..."
            Start-Service "Zabbix Agent 2"
            Start-Sleep -Seconds 2
            $agent2Service.Refresh()
            Write-Host "  → Servis durumu: $($agent2Service.Status)" -ForegroundColor Green
        }
    } else {
        Write-Host "  → Agent2 servisi bulunamadı!" -ForegroundColor Red
        return $false
    }

    # Firewall kuralı
    Write-Host "`n[7/7] Firewall kuralı ekleniyor..."
    $fwRule = Get-NetFirewallRule -DisplayName "Zabbix Agent2" -ErrorAction SilentlyContinue

    if (-not $fwRule) {
        New-NetFirewallRule -DisplayName "Zabbix Agent2" `
                            -Direction Inbound `
                            -Protocol TCP `
                            -LocalPort $ListenPort `
                            -Action Allow `
                            -Profile Any `
                            -ErrorAction SilentlyContinue | Out-Null
        Write-Host "  → Firewall kuralı eklendi" -ForegroundColor Green
    } else {
        Write-Host "  → Firewall kuralı zaten mevcut" -ForegroundColor Yellow
    }

    Write-Host "`n========================================" -ForegroundColor Magenta
    Write-Host "MİGRASYON TAMAMLANDI!" -ForegroundColor Green
    Write-Host "========================================`n" -ForegroundColor Magenta

    # Son durum raporu
    Write-Host "SON DURUM:"
    Write-Host "  Agent2 Servisi: $($agent2Service.Status)" -ForegroundColor Cyan
    Write-Host "  Hostname: $Hostname"
    Write-Host "  Server: $ZabbixServer"
    Write-Host "  Listen Port: $ListenPort"

    # Konfig dosyası yolu göster
    $configPath = "C:\Program Files\Zabbix Agent 2\zabbix_agent2.conf"
    Write-Host "`nKonfig dosyası: $configPath" -ForegroundColor Yellow

    return $true
}

# Remote veya local çalıştır
try {
    if ($ComputerName -eq "localhost" -or $ComputerName -eq $env:COMPUTERNAME) {
        Write-Info "`nLokal kurulum başlatılıyor...`n"
        $result = & $ScriptBlock -ZabbixServer $ZabbixServer `
                                  -ServerActive $ServerActive `
                                  -Hostname $Hostname `
                                  -ListenPort $ListenPort `
                                  -RemoveOldAgent $RemoveOldAgent `
                                  -BackupConfig $BackupConfig `
                                  -Agent2TempPath $Agent2MSIPath
    } else {
        Write-Info "`nRemote kurulum başlatılıyor: $ComputerName`n"

        # MSI dosyasını remote sunucuya kopyala
        $remotePath = "\\$ComputerName\C$\Temp\zabbix_agent2_temp.msi"
        Write-Info "MSI dosyası kopyalanıyor..."
        Copy-Item $Agent2MSIPath $remotePath -Force

        $result = Invoke-Command -ComputerName $ComputerName -ScriptBlock $ScriptBlock -ArgumentList `
            $ZabbixServer, $ServerActive, $Hostname, $ListenPort, $RemoveOldAgent, $BackupConfig, "C:\Temp\zabbix_agent2_temp.msi"

        # Geçici dosyayı temizle
        Remove-Item $remotePath -Force -ErrorAction SilentlyContinue
    }

    if ($result) {
        Write-Success "`n✓ İşlem başarıyla tamamlandı!"
        Write-Info "`nSONRAKİ ADIMLAR:"
        Write-Host "  1. Zabbix sunucusunda host'un erişilebilir olduğunu kontrol edin"
        Write-Host "  2. agent.version item'ının Agent2 versiyon bilgisini gösterdiğini doğrulayın"
        Write-Host "  3. Python helper script ile doğrulama yapın:"
        Write-Host "     python agent_migration_helper.py" -ForegroundColor Cyan
    } else {
        Write-Error "`n❌ İşlem sırasında hata oluştu!"
    }

} catch {
    Write-Error "`n❌ Hata: $($_.Exception.Message)"
    Write-Host $_.Exception.StackTrace -ForegroundColor DarkGray
    exit 1
}
