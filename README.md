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

## Usage with Claude Code and Zabbix Master Agent Skill

This repository includes a powerful **Claude Code skill** that automates Zabbix operations through natural language commands. The `zabbix-master` agent skill provides intelligent automation for all Zabbix-related tasks.

### How It Works

The zabbix-master skill is a Claude Code agent that:
- **Automatically detects** Zabbix-related keywords in your requests
- **Reads configuration** from your `.env` file automatically
- **Handles API authentication** and session management
- **Executes operations** with built-in error handling and retries
- **Provides intelligent responses** with context-aware suggestions

### Using the Skill in Claude Code

Simply open this project in Claude Code and ask questions or request operations in natural language:

**Examples:**

```
You: "Check the status of all hosts in Zabbix"
Claude: [Activates zabbix-master skill, connects to your Zabbix server,
         and provides detailed host status report]

You: "Add SNMP monitoring for device 192.168.1.100"
Claude: [Uses the skill to configure SNMP monitoring, link templates,
         and verify connectivity]

You: "Show me all triggers that are in problem state"
Claude: [Queries Zabbix API through the skill and displays active problems
         with details]

You: "Create a graph for CPU utilization on server DC01"
Claude: [Creates the graph items, configures visualization, and confirms creation]
```

### Skill Capabilities

The zabbix-master skill can handle:

- **Host Management**: Add, update, delete, and monitor hosts
- **Item Configuration**: Create items, check values, troubleshoot collection issues
- **Template Operations**: Link templates, export/import configurations
- **Monitoring Setup**: Configure SNMP, agents, network discovery
- **Graph Creation**: Build custom graphs and dashboards
- **Problem Analysis**: Diagnose issues, check triggers, analyze events
- **Security Audits**: Review permissions, check configurations
- **Performance Optimization**: Analyze database, optimize settings

### Manual Script Execution

You can also run the example scripts directly with Python:

```bash
# Navigate to examples directory
cd examples/snmp

# Run a script
python add_snmp_devices.py
```

All scripts automatically use the credentials from your `.env` file.

### Skill vs Manual Scripts

| Method | Best For | Advantages |
|--------|----------|------------|
| **Claude Code Skill** | Interactive exploration, complex tasks, troubleshooting | Natural language, intelligent automation, context-aware |
| **Manual Scripts** | Scheduled tasks, automation pipelines, batch operations | Direct control, scriptable, integration-ready |

### Getting Started with the Skill

1. **Clone the repository**
   ```bash
   git clone https://github.com/sipsyai/zabbix-master-agent.git
   ```

2. **Navigate to the project directory**
   ```bash
   cd zabbix-master-agent
   ```

3. **Configure your environment**
   ```bash
   cp .env.example .env
   # Edit .env with your Zabbix credentials
   ```

4. **Open Claude Code**
   - Open Claude Code application
   - Navigate to this project folder
   - Or use the terminal command: `claude`

5. **Start using the skill** - Simply type your questions or requests in natural language:
   - "List all templates in my Zabbix server"
   - "Check which hosts are unreachable"
   - "Create a dashboard for network monitoring"
   - "Help me troubleshoot why host X has no data"
   - "Configure SNMP monitoring for my network devices"
   - "Add SNMP monitoring for device 192.168.1.100"
   - "Show me all triggers in problem state"

The zabbix-master skill activates automatically when you mention Zabbix-related operations. It reads your `.env` configuration and handles all API operations intelligently.

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
