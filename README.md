# Zabbix Master Agent

A comprehensive collection of tools and utilities for managing and automating Zabbix monitoring operations.

## Overview

This repository contains automated scripts and tools for Zabbix monitoring system management, including:
- SNMP device management
- Network discovery automation
- Monitoring and graph management
- Agent deployment and migration
- History and storage management
- Custom plugins

## Prerequisites

- Python 3.7+
- Zabbix Server 5.0+ (tested with Zabbix 6.0+)
- Network access to Zabbix API
- Required Python packages (install via pip):
  ```bash
  pip install requests python-dotenv
  ```

## Configuration

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` with your Zabbix server details:
   ```
   ZABBIX_API_URL=http://your-zabbix-server/api_jsonrpc.php
   ZABBIX_SERVER=your-zabbix-server-ip
   ZABBIX_USERNAME=your-username
   ZABBIX_PASSWORD=your-password
   ZABBIX_PORT=10051
   ZABBIX_USE_SSL=false
   ZABBIX_TIMEOUT=30
   ```

## Usage with Zabbix Master Agent Skill

All scripts in this repository are designed to work seamlessly with the `zabbix-master` agent skill. The agent automatically handles:
- Authentication and session management
- API connection management
- Error handling and retries
- Configuration from `.env` file

Simply invoke the zabbix-master skill and it will automatically use the credentials from your `.env` file.

## Examples

The `examples/` directory contains organized scripts by category:

### 📡 SNMP Management (`examples/snmp/`)
Scripts for managing SNMP devices and templates:
- `add_snmp_devices.py` - Bulk add SNMP devices to Zabbix
- `check_and_configure_snmp.py` - Verify and configure SNMP settings
- `link_snmp_templates.py` - Link SNMP templates to hosts
- `test_snmp_direct.py` - Test direct SNMP connectivity
- `list_all_templates.py` - List available templates

### 🔍 Network Discovery (`examples/network_discovery/`)
Network discovery and topology management:
- `configure_network_discovery.py` - Configure discovery rules
- `execute_network_discovery.py` - Execute discovery actions
- `view_network_neighbors.py` - View network topology
- `delete_discovery_rules.py` - Clean up discovery rules
- `update_host_ips.py` - Update host IP addresses

### 📊 Monitoring & Graphs (`examples/monitoring/`)
Graph analysis and monitoring diagnostics:
- `analyze_all_graphs.py` - Analyze all graphs for issues
- `check_graph_issue.py` - Check specific graph problems
- `check_cpu_graph.py` - CPU graph diagnostics
- `check_specific_cpu_graph.py` - Detailed CPU graph analysis
- `diagnose_graph_no_data.py` - Diagnose missing graph data

### 📈 Items & Graphs Creation (`examples/items_and_graphs/`)
Create and manage items and graphs:
- `create_graph.py` - Create custom graphs
- `create_working_memory_item.py` - Create memory monitoring items
- `create_memory_util_graph.py` - Create memory utilization graphs
- `fix_memory_utilization.py` - Fix memory monitoring issues
- `check_dependent_items.py` - Verify dependent items

### 🖥️ Agent Management (`examples/agent_management/`)
Zabbix agent deployment and management:
- `agent_migration_helper.py` - Migrate agents between versions
- `check_dc01_agent.py` - Check domain controller agent status
- `check_host_interface.py` - Verify host interfaces
- `collect_zabbix_info.py` - Collect comprehensive Zabbix information

### 💾 History & Storage (`examples/history_and_storage/`)
Historical data and storage management:
- `check_history_storage.py` - Check history storage status
- `test_history_api.py` - Test history API functionality

### 🔌 Plugins (`examples/plugins/`)
Custom plugins and integrations:
- `ad-logon-plugin/` - Active Directory logon monitoring
- `ad-event-collector/` - Active Directory event collection
- `example-plugin/` - Template for creating custom plugins

## PowerShell Scripts

### Zabbix Agent 2 Installation
- `Install-ZabbixAgent2.ps1` - Automated installation script for Zabbix Agent 2 on Windows

## Documentation

- [CLAUDE.md](CLAUDE.md) - Project instructions and guidelines
- [deployment_plan_phase1.md](deployment_plan_phase1.md) - Deployment planning documentation
- [FIX_AGENT_ACTIVE.md](FIX_AGENT_ACTIVE.md) - Agent active mode troubleshooting
- [NETWORK_NEIGHBORS_README.md](NETWORK_NEIGHBORS_README.md) - Network neighbor discovery guide

## Security

⚠️ **IMPORTANT**: Never commit the `.env` file to version control. It contains sensitive credentials.

The `.env` file is included in `.gitignore` to prevent accidental commits.

## Contributing

When adding new scripts:
1. Place them in the appropriate category under `examples/`
2. Update the relevant README
3. Ensure they use `.env` for configuration
4. Follow the existing code style
5. Add proper error handling

## License

This project is provided as-is for Zabbix monitoring automation.

## Support

For issues and questions:
- Check the documentation in the `docs/` directory
- Review example scripts for reference implementations
- Consult Zabbix official documentation for API details

## Project Structure

```
zabbix-master-agent/
├── .claude/              # Claude AI configuration
├── examples/             # Organized example scripts
│   ├── snmp/            # SNMP management
│   ├── network_discovery/  # Network discovery
│   ├── monitoring/      # Monitoring and graphs
│   ├── items_and_graphs/   # Items and graphs creation
│   ├── agent_management/   # Agent management
│   ├── history_and_storage/ # History and storage
│   └── plugins/         # Custom plugins
├── zabbix-docs/         # Additional documentation
├── .env.example         # Environment configuration template
├── .gitignore          # Git ignore rules
└── README.md           # This file
```
