# SNMP Management Examples

This directory contains scripts for managing SNMP devices and templates in Zabbix.

## Scripts

### add_snmp_devices.py
Bulk add SNMP devices to Zabbix monitoring.

**Features:**
- Add multiple SNMP devices from a configuration
- Automatic template assignment
- SNMP version configuration (v1, v2c, v3)
- Interface configuration

**Usage:**
```bash
python add_snmp_devices.py
```

### check_and_configure_snmp.py
Verify and configure SNMP settings for existing hosts.

**Features:**
- Verify SNMP connectivity
- Configure SNMP interfaces
- Update SNMP credentials
- Test SNMP responses

**Usage:**
```bash
python check_and_configure_snmp.py
```

### link_snmp_templates.py
Link SNMP templates to hosts based on device type.

**Features:**
- Automatic device type detection
- Template linking based on OID
- Bulk template operations
- Template verification

**Usage:**
```bash
python link_snmp_templates.py
```

### test_snmp_direct.py
Test direct SNMP connectivity to devices.

**Features:**
- Direct SNMP query testing
- OID walk operations
- SNMP version testing
- Connectivity diagnostics

**Usage:**
```bash
python test_snmp_direct.py
```

### list_all_templates.py
List all available templates in Zabbix, including SNMP templates.

**Features:**
- List all templates
- Filter SNMP templates
- Show template details
- Export template information

**Usage:**
```bash
python list_all_templates.py
```

## Common SNMP Templates

- **Template Net Cisco IOS SNMPv2** - Cisco network devices
- **Template Net Generic Device SNMPv2** - Generic SNMP devices
- **Template Net HP Enterprise Switch SNMPv2** - HP switches
- **Template Net Juniper SNMPv2** - Juniper devices

## Configuration

All scripts use the `.env` file for Zabbix API credentials. Make sure your `.env` file is properly configured:

```
ZABBIX_API_URL=http://your-zabbix-server/api_jsonrpc.php
ZABBIX_USERNAME=your-username
ZABBIX_PASSWORD=your-password
```

## SNMP Requirements

For SNMP monitoring to work:
1. SNMP must be enabled on target devices
2. Zabbix server must have network access to SNMP ports (usually 161/UDP)
3. SNMP community strings or v3 credentials must be configured
4. Proper firewall rules must be in place

## Troubleshooting

- **"SNMP connection failed"**: Check firewall rules and SNMP service status
- **"Authentication failed"**: Verify SNMP community string or v3 credentials
- **"Timeout"**: Check network connectivity and SNMP service response time
- **"Template not found"**: Ensure the correct template is installed in Zabbix
