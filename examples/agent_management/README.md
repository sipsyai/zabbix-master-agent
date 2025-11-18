# Agent Management Examples

This directory contains scripts for managing Zabbix agents and host configurations.

## Scripts

### agent_migration_helper.py
Migrate agents between versions or configurations.

**Features:**
- Migrate from Zabbix Agent 1 to Agent 2
- Configuration migration
- Item key compatibility check
- Bulk agent migration

**Usage:**
```bash
python agent_migration_helper.py
```

See also: [FIX_AGENT_ACTIVE.md](../../FIX_AGENT_ACTIVE.md)

### check_dc01_agent.py
Check domain controller agent status and configuration.

**Features:**
- Agent connectivity verification
- Configuration validation
- Active/passive mode checks
- Performance metrics review

**Usage:**
```bash
python check_dc01_agent.py
```

### check_host_interface.py
Verify and manage host interface configurations.

**Features:**
- Interface connectivity tests
- IP/DNS configuration check
- Port verification
- Interface type validation

**Usage:**
```bash
python check_host_interface.py
```

### collect_zabbix_info.py
Collect comprehensive Zabbix system information.

**Features:**
- Server configuration details
- Agent status across all hosts
- Template assignments
- Item statistics
- Trigger information

**Usage:**
```bash
python collect_zabbix_info.py
```

## Agent Types

### Zabbix Agent 1 (Legacy)
- Simple monitoring agent
- Support for passive and active checks
- Limited preprocessing capabilities
- Being phased out

### Zabbix Agent 2
- Modern Go-based agent
- Plugin architecture
- Better performance
- Extended capabilities
- Native support for:
  - MongoDB
  - Redis
  - PostgreSQL
  - MySQL
  - Docker
  - And more...

## Agent Modes

### Passive Mode
- Server connects to agent
- Requires agent port (10050) accessible
- Good for:
  - Stable network environments
  - When server can reach agents
  - Firewall rules allow inbound connections

### Active Mode
- Agent connects to server
- Agent initiates connections
- Good for:
  - NAT environments
  - Remote locations
  - Dynamic IP addresses
  - Restricted firewall policies

## Host Interface Types

1. **Agent** - Zabbix agent connection (port 10050)
2. **SNMP** - SNMP monitoring (port 161)
3. **JMX** - Java JMX monitoring (port 12345)
4. **IPMI** - Hardware monitoring via IPMI

## Configuration Files

### Zabbix Agent 2 (Windows)
```
C:\Program Files\Zabbix Agent 2\zabbix_agent2.conf
```

### Zabbix Agent 2 (Linux)
```
/etc/zabbix/zabbix_agent2.conf
```

## Common Agent Items

- `agent.ping` - Agent availability
- `agent.version` - Agent version
- `system.cpu.load` - CPU load
- `vm.memory.size` - Memory metrics
- `vfs.fs.size` - Filesystem metrics
- `net.if.in/out` - Network traffic

## Migration Considerations

When migrating from Agent 1 to Agent 2:
1. Review item keys for compatibility
2. Update configuration files
3. Install Agent 2 package
4. Test monitoring before full migration
5. Update firewall rules if needed
6. Configure plugins as needed

## Troubleshooting

### Agent Not Reachable
- Check firewall rules
- Verify agent is running
- Check `Server` or `ServerActive` configuration
- Test network connectivity

### Item Not Supported
- Verify agent version supports the key
- Check agent configuration
- Review user parameters
- Ensure plugins are loaded (Agent 2)

### Encryption Issues
- Verify PSK or certificate configuration
- Check encryption settings match server
- Validate TLS configuration
- Review log files for errors

## PowerShell Installation

For Windows agent installation, see:
- [Install-ZabbixAgent2.ps1](../../Install-ZabbixAgent2.ps1)

This script automates:
- Agent download
- Installation
- Configuration
- Service setup
- Firewall rules
