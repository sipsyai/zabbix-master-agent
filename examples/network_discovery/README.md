# Network Discovery Examples

This directory contains scripts for automating network discovery and topology management in Zabbix.

## Scripts

### configure_network_discovery.py
Configure network discovery rules in Zabbix.

**Features:**
- Create discovery rules
- Configure IP ranges
- Set discovery checks (ping, SNMP, agent)
- Configure discovery actions

**Usage:**
```bash
python configure_network_discovery.py
```

### execute_network_discovery.py
Execute network discovery operations.

**Features:**
- Trigger discovery scans
- Monitor discovery progress
- Process discovered hosts
- Automatic host creation

**Usage:**
```bash
python execute_network_discovery.py
```

### view_network_neighbors.py
View network topology and neighbor relationships.

**Features:**
- Display network topology
- Show LLDP/CDP neighbors
- Visualize network connections
- Export topology data

**Usage:**
```bash
python view_network_neighbors.py
```

See also: [NETWORK_NEIGHBORS_README.md](../../NETWORK_NEIGHBORS_README.md)

### delete_discovery_rules.py
Clean up and delete discovery rules.

**Features:**
- List existing discovery rules
- Delete specific rules
- Bulk deletion operations
- Cleanup orphaned discoveries

**Usage:**
```bash
python delete_discovery_rules.py
```

### update_host_ips.py
Update IP addresses for existing hosts.

**Features:**
- Bulk IP address updates
- Interface reconfiguration
- DNS name resolution
- Validation of new IPs

**Usage:**
```bash
python update_host_ips.py
```

## Discovery Checks

Zabbix network discovery supports multiple check types:

- **ICMP ping** - Basic connectivity check
- **SNMP** - SNMP device discovery
- **Zabbix agent** - Agent availability check
- **HTTP/HTTPS** - Web service check
- **FTP/SSH/Telnet** - Service checks

## Configuration

Discovery rules can be configured with:
- IP ranges (e.g., 192.168.1.1-254)
- Update intervals
- Concurrent checks
- Uniqueness criteria
- Device types

## Best Practices

1. **Start small**: Test with small IP ranges first
2. **Use appropriate intervals**: Avoid too frequent scans
3. **Set uniqueness criteria**: Prevent duplicate hosts
4. **Configure actions**: Automate host creation and template linking
5. **Monitor performance**: Large scans can impact Zabbix performance

## Troubleshooting

- **No devices discovered**: Check network connectivity and firewall rules
- **Duplicate hosts**: Review uniqueness criteria
- **Slow discovery**: Reduce IP range or increase check intervals
- **Missing devices**: Verify discovery checks match device capabilities
