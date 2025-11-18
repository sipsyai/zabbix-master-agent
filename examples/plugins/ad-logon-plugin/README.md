# Zabbix Agent 2 - Active Directory Logon Monitoring Plugin

A comprehensive Zabbix Agent 2 plugin for monitoring Active Directory logon activities on Windows Domain Controllers, Member Servers, and Workstations.

## Features

- **Multiple Logon Event Types**: Monitor 9 different types of logon activities
- **Windows Event Log Integration**: Direct access to Security and System event logs
- **Flexible Time Filtering**: Query events from the last 1 to 720 hours
- **Performance Optimized**: Built-in caching and configurable event limits
- **JSON Output**: Structured data for easy processing in Zabbix
- **Detailed Logging**: Comprehensive debug logging for troubleshooting
- **Error Handling**: Graceful error management and meaningful error messages

## Supported Logon Types

1. **Logon Failures** - Failed authentication attempts
2. **DC Activity** - Logon activity on Domain Controllers
3. **Server Activity** - Logon activity on Member Servers
4. **Workstation Activity** - Logon activity on Workstations
5. **User Activity** - User-specific logon patterns
6. **Recent Users** - Recently logged-in users
7. **Last Logon** - Last logon timestamp per workstation
8. **Multiple Computers** - Users logged into multiple computers
9. **RADIUS Logons** - RADIUS/NPS authentication events

## Requirements

- **Operating System**: Windows Server 2012 R2 or later
- **Zabbix Agent**: Zabbix Agent 2 (6.0 or later)
- **Permissions**: Administrator privileges (for reading Security event logs)
- **Go Version**: Go 1.23.0 or later (for building)

## Installation

### Step 1: Build the Plugin

```bash
# Clone or download the plugin source
cd ad-logon-plugin

# Install dependencies
go mod download

# Build the plugin
make build

# Or build explicitly for Windows
make build-windows
```

The compiled binary will be in `build/zabbix-agent2-plugin-adlogon.exe`

### Step 2: Install the Plugin

```bash
# Copy the binary to Zabbix plugins directory
copy build\zabbix-agent2-plugin-adlogon.exe "C:\Program Files\Zabbix Agent 2\plugins\"

# Copy the configuration file
copy adlogon.conf "C:\Program Files\Zabbix Agent 2\zabbix_agent2.d\plugins.d\"
```

### Step 3: Configure the Plugin

Edit `C:\Program Files\Zabbix Agent 2\zabbix_agent2.d\plugins.d\adlogon.conf`:

```conf
# Required: Path to the plugin executable
Plugins.ADLogon.System.Path=C:\Program Files\Zabbix Agent 2\plugins\zabbix-agent2-plugin-adlogon.exe

# Optional: Adjust these based on your needs
Plugins.ADLogon.Timeout=30
Plugins.ADLogon.MaxEvents=1000
Plugins.ADLogon.CacheExpiry=300
Plugins.ADLogon.DefaultHours=24
```

### Step 4: Restart Zabbix Agent 2

```powershell
Restart-Service "Zabbix Agent 2"
```

## Usage

### Item Key Format

```
ad.logon[<type>, <hours>, <computer>]
```

**Parameters:**

- `type` (required): Type of logon data to retrieve
  - `failure` - Logon failures
  - `dc_activity` - Domain Controller activity
  - `server_activity` - Member Server activity
  - `workstation_activity` - Workstation activity
  - `user_activity` - User logon activity
  - `recent_users` - Recent user logons
  - `last_logon` - Last logon per workstation
  - `multiple_computers` - Users on multiple computers
  - `radius` - RADIUS/NPS logons

- `hours` (optional): Number of hours to look back (default: 24, max: 720)

- `computer` (optional): Filter by specific computer name

### Example Item Keys

```
# Get logon failures from the last 24 hours
ad.logon[failure]

# Get logon failures from the last 12 hours
ad.logon[failure, 12]

# Get DC activity from the last 48 hours
ad.logon[dc_activity, 48]

# Get logon failures for specific computer
ad.logon[failure, 24, DC01]

# Get users logged into multiple computers
ad.logon[multiple_computers, 24]

# Get RADIUS authentication events
ad.logon[radius, 6]
```

### Testing

Test the plugin from the command line:

```powershell
# Test logon failures
& "C:\Program Files\Zabbix Agent 2\zabbix_agent2.exe" -t ad.logon[failure,24]

# Test DC activity
& "C:\Program Files\Zabbix Agent 2\zabbix_agent2.exe" -t ad.logon[dc_activity,12]
```

## Output Format

The plugin returns data in JSON format:

```json
{
  "count": 5,
  "start_time": "2025-11-16T10:00:00Z",
  "end_time": "2025-11-17T10:00:00Z",
  "events": [
    {
      "timestamp": "2025-11-17T09:45:23Z",
      "event_id": 4625,
      "computer": "DC01",
      "user": "jdoe",
      "domain": "CONTOSO",
      "logon_type": 3,
      "logon_type_name": "Network",
      "source_ip": "192.168.1.100",
      "workstation_name": "WS001",
      "status": "failure",
      "failure_reason": "Unknown user name or bad password",
      "auth_package": "NTLM"
    }
  ],
  "unique_users": 3,
  "unique_hosts": 2
}
```

## Event IDs Monitored

| Event ID | Description |
|----------|-------------|
| 4624 | Successful logon |
| 4625 | Failed logon |
| 4634 | Logoff |
| 4740 | Account locked out |
| 4768 | Kerberos ticket granted (TGT) |
| 4769 | Kerberos service ticket requested |
| 4776 | NTLM authentication |
| 6272 | NPS granted access (RADIUS) |
| 6273 | NPS denied access (RADIUS) |

## Logon Types

| Type | Name | Description |
|------|------|-------------|
| 2 | Interactive | Console logon |
| 3 | Network | Network logon (file shares, etc.) |
| 4 | Batch | Scheduled task |
| 5 | Service | Service startup |
| 7 | Unlock | Workstation unlock |
| 8 | NetworkCleartext | Network logon with cleartext password |
| 9 | NewCredentials | RunAs with different credentials |
| 10 | RemoteInteractive | Remote Desktop/Terminal Services |
| 11 | CachedInteractive | Cached domain credentials |

## Configuration Options

### Timeout
- **Range**: 1-300 seconds
- **Default**: 30 seconds
- **Purpose**: Maximum time for event log operations

### MaxEvents
- **Range**: 1-10000 events
- **Default**: 1000 events
- **Purpose**: Maximum events to retrieve per query

### CacheExpiry
- **Range**: 0-3600 seconds
- **Default**: 300 seconds (5 minutes)
- **Purpose**: Cache TTL (set to 0 to disable)

### DefaultHours
- **Range**: 1-720 hours
- **Default**: 24 hours
- **Purpose**: Default time range when not specified

### DebugMode
- **Values**: true/false
- **Default**: false
- **Purpose**: Enable detailed debug logging

## Zabbix Template Example

```xml
<item>
  <name>AD: Logon Failures (24h)</name>
  <key>ad.logon[failure,24]</key>
  <delay>5m</delay>
  <value_type>TEXT</value_type>
  <preprocessing>
    <step>
      <type>JSONPATH</type>
      <params>$.count</params>
    </step>
  </preprocessing>
</item>

<trigger>
  <expression>{Windows AD:ad.logon[failure,1].last()}&gt;10</expression>
  <name>High number of failed logons in the last hour</name>
  <priority>WARNING</priority>
</trigger>
```

## Performance Considerations

1. **Event Log Size**: Large event logs may take time to query
   - Use shorter time ranges (hours parameter)
   - Increase Timeout if needed

2. **Caching**: Enable caching for frequently queried metrics
   - Reduces load on event log system
   - Improves response time

3. **MaxEvents Limit**: Balance between completeness and performance
   - Higher values = more complete data but slower
   - Monitor query times and adjust

4. **Computer Filtering**: Use computer filter to reduce data volume
   - More efficient than post-processing

## Troubleshooting

### Plugin Not Loading

Check Zabbix Agent 2 log:
```
C:\Program Files\Zabbix Agent 2\zabbix_agent2.log
```

Verify configuration:
```powershell
& "C:\Program Files\Zabbix Agent 2\zabbix_agent2.exe" -T
```

### Permission Denied

Ensure Zabbix Agent 2 service runs as Administrator or Local System:
```powershell
Get-Service "Zabbix Agent 2" | Select-Object Name, StartType, Status
```

### No Events Returned

1. Verify event log is enabled and has events
2. Check time range (hours parameter)
3. Enable DebugMode to see detailed logging
4. Verify computer name filter (if used)

### Timeout Errors

1. Increase Timeout in configuration
2. Reduce MaxEvents
3. Use shorter time ranges
4. Check disk I/O performance

## Development

### Building from Source

```bash
# Install dependencies
make deps

# Build
make build

# Run tests
make test

# Create distribution package
make dist
```

### Running Tests

```bash
# Unit tests
make test

# With coverage
make test-coverage
```

### Code Formatting

```bash
make format
```

### Linting

```bash
make lint
```

## Security Considerations

1. **Privilege Requirements**: Plugin requires Administrator privileges to read Security logs
2. **Sensitive Data**: Event logs may contain sensitive information
3. **Network Security**: Ensure Zabbix communication is encrypted
4. **Access Control**: Limit who can view logon data in Zabbix

## Limitations

1. **Windows Only**: Plugin only works on Windows systems
2. **Event Log Retention**: Limited by Windows Event Log retention policy
3. **Performance**: Large event logs may impact performance
4. **Computer Role Detection**: Uses naming conventions (DC*, SRV*, WS*)

## Future Enhancements

- [ ] Support for custom event IDs
- [ ] Advanced filtering (user groups, IP ranges)
- [ ] Event correlation and anomaly detection
- [ ] Support for remote event log reading
- [ ] Performance metrics and statistics
- [ ] Automatic computer role detection via AD query

## License

MIT License - See LICENSE file for details

## Support

For issues, questions, or contributions:
- Report issues on GitHub
- Check Zabbix Agent 2 logs for errors
- Enable DebugMode for detailed troubleshooting

## Version History

### 1.0.0-beta1 (2025-11-17)
- Initial release
- Support for 9 logon event types
- Windows Event Log integration
- Caching and performance optimization
- Comprehensive error handling

## Authors

Developed for Zabbix Agent 2 monitoring of Active Directory environments.

## Acknowledgments

- Zabbix team for the excellent Agent 2 SDK
- Microsoft for Windows Event Log API documentation
