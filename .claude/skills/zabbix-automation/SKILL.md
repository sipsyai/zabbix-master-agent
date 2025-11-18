---
name: zabbix-automation
description: Automating Zabbix monitoring operations including API interactions, metric sending, and agent data retrieval. Use when managing Zabbix hosts, users, items, templates, sending metrics to Zabbix servers, or querying Zabbix agents for monitoring data.
version: 1.0.0
technologies: [python, zabbix, monitoring]
degree_of_freedom: medium
---

# Zabbix Automation Skill

Automates Zabbix monitoring operations using the python-zabbix-utils library. Supports API operations (user/host/item management), Sender protocol (metric transmission), and Getter protocol (agent queries).

## Quick Start

Run the interactive script:

```bash
python zabbix_runner.py
```

The script automatically:
- Creates virtual environment in ./venv if needed
- Installs dependencies from requirements.txt
- Provides interactive menu for operations
- Reads credentials from environment variables or prompts

## Core Operations

### Zabbix API
Manage Zabbix entities via REST API:
- Users: list, create, update, delete
- Hosts: create, configure, remove
- Items: create monitoring items
- Templates: import/export XML
- Authentication: token (recommended) or username/password

### Zabbix Sender
Send metrics to Zabbix server/proxy:
- Single values with custom timestamps
- Bulk metric submission
- Multiple cluster support
- TLS/PSK encryption

### Zabbix Getter
Retrieve values from Zabbix agents:
- Query specific item keys
- System information (uname, uptime)
- Network interface discovery
- TLS/PSK encryption

## Configuration

Set environment variables to avoid prompts:

```bash
# API operations
export ZABBIX_URL="https://zabbix.example.com"
export ZABBIX_TOKEN="your-api-token-here"

# Sender operations
export ZABBIX_SERVER="127.0.0.1"
export ZABBIX_SERVER_PORT="10051"

# Getter operations
export ZABBIX_AGENT_HOST="127.0.0.1"
export ZABBIX_AGENT_PORT="10050"
```

Alternative: username/password authentication:
```bash
export ZABBIX_USER="Admin"
export ZABBIX_PASSWORD="zabbix"
```

## Usage Examples

### List All Users
```python
from zabbix_utils import ZabbixAPI

api = ZabbixAPI(url="https://zabbix.example.com")
api.login(token="your-api-token")

users = api.user.get(output=['userid', 'name'])
for user in users:
    print(user['name'])
```

### Send Single Metric
```python
from zabbix_utils import Sender

sender = Sender(server='127.0.0.1', port=10051)
response = sender.send_value('myhost', 'cpu.usage', 75.5)

if response.failed == 0:
    print(f"Sent successfully in {response.time}")
```

### Send Bulk Metrics
```python
from zabbix_utils import ItemValue, Sender

items = [
    ItemValue('host1', 'cpu.usage', 80),
    ItemValue('host1', 'memory.used', 4096),
    ItemValue('host2', 'disk.free', 50.5)
]

sender = Sender(server='127.0.0.1', port=10051)
response = sender.send(items)
print(f"Processed: {response.processed}, Failed: {response.failed}")
```

### Query Zabbix Agent
```python
from zabbix_utils import Getter

agent = Getter(host='127.0.0.1', port=10050)
resp = agent.get('system.uname')

if not resp.error:
    print(f"System: {resp.value}")
```

### Create Zabbix Host
```python
api = ZabbixAPI(url="https://zabbix.example.com")
api.login(user="Admin", password="zabbix")

host = api.host.create(
    host="NewServer",
    interfaces=[{
        "type": 1,
        "main": 1,
        "useip": 1,
        "ip": "192.168.1.100",
        "dns": "",
        "port": "10050"
    }],
    groups=[{"groupid": "2"}]
)

print(f"Created host: {host['hostids'][0]}")
api.logout()
```

## Common Workflows

### Setup New Host Monitoring
1. Connect to Zabbix API
2. Create host with interface details
3. Link appropriate template
4. Create custom items if needed
5. Verify host appears in monitoring

### Bulk Metric Collection
1. Gather metrics from multiple sources
2. Build ItemValue list with timestamps
3. Send to Zabbix using Sender
4. Check response for failures
5. Retry failed items

### Agent Health Check
1. Connect to agent with Getter
2. Query system.uname and agent.ping
3. Parse responses
4. Report status

## Error Handling

Always verify responses:

```python
# API operations
if response:
    print("Success")

# Sender operations
if response.failed > 0:
    print(f"Failed: {response.failed} items")

# Getter operations
if resp.error:
    print(f"Error: {resp.error}")
```

Common issues:
- Connection refused: Check Zabbix server/agent is running
- Authentication failed: Verify credentials and token validity
- Failed to send value: Ensure host exists and item is type "Zabbix trapper"
- Venv creation failed: Check Python 3.8+ installed and write permissions

## Security

1. Use environment variables for credentials (never hardcode)
2. Prefer API tokens over username/password
3. Enable SSL/TLS verification in production:
   ```python
   api = ZabbixAPI(url="https://...", validate_certs=True)
   ```
4. Use PSK encryption for sensitive data:
   ```python
   from zabbix_utils import PSKContext
   psk = PSKContext(psk_identity="PSK 001", psk_hex="1234...")
   sender = Sender(server='...', psk_context=psk)
   ```
5. Grant minimal API token permissions

## Compatibility

- Zabbix: 6.0, 7.0, 7.2, 7.4+
- Python: 3.8, 3.9, 3.10, 3.11, 3.12, 3.13

Check API version:
```python
ver = api.version
print(f"Zabbix {ver}, LTS: {ver.is_lts()}")
```

## Advanced Features

See reference files for detailed information:
- [reference/api_methods.md](reference/api_methods.md) - Complete API method reference
- [reference/sender_advanced.md](reference/sender_advanced.md) - Advanced Sender configurations
- [reference/getter_advanced.md](reference/getter_advanced.md) - Advanced Getter configurations
- [reference/security.md](reference/security.md) - TLS/PSK encryption setup
