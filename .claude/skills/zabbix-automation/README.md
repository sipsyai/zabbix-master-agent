# Zabbix Automation Skill

This Agent Skill provides comprehensive automation for Zabbix monitoring operations using the python-zabbix-utils library.

## Quick Start

1. Run the setup script:
```bash
python zabbix_runner.py
```

2. The script will automatically:
   - Create a virtual environment in ./venv
   - Install required dependencies
   - Prepare the environment for Zabbix operations

3. Set environment variables for your Zabbix instance:
```bash
export ZABBIX_URL="https://zabbix.example.com"
export ZABBIX_TOKEN="your-api-token"
```

## Features

- **Zabbix API**: Manage users, hosts, items, templates, triggers
- **Zabbix Sender**: Send metrics to Zabbix server/proxy
- **Zabbix Getter**: Retrieve values from Zabbix agents
- **Automatic venv management**: No manual setup required
- **Environment variable support**: Secure credential handling
- **TLS/PSK encryption**: Secure communications
- **Async support**: High-performance operations

## Documentation

- [SKILL.md](SKILL.md) - Main skill documentation
- [reference/api_methods.md](reference/api_methods.md) - API method reference
- [reference/sender_advanced.md](reference/sender_advanced.md) - Sender configurations
- [reference/getter_advanced.md](reference/getter_advanced.md) - Getter configurations
- [reference/security.md](reference/security.md) - Security best practices

## Requirements

- Python 3.8+
- Zabbix 6.0+
- Network access to Zabbix server/agents

## File Structure

```
zabbix-skill/
├── SKILL.md                    # Main skill documentation
├── README.md                   # This file
├── zabbix_runner.py            # Setup and runner script
├── requirements.txt            # Python dependencies
├── venv/                       # Virtual environment (auto-created)
└── reference/                  # Detailed documentation
    ├── api_methods.md          # API reference
    ├── sender_advanced.md      # Sender reference
    ├── getter_advanced.md      # Getter reference
    └── security.md             # Security guide
```

## Examples

### API Usage
```python
from zabbix_utils import ZabbixAPI

api = ZabbixAPI(url="https://zabbix.example.com")
api.login(token="your-token")

users = api.user.get(output=['userid', 'name'])
for user in users:
    print(user['name'])
```

### Sender Usage
```python
from zabbix_utils import Sender

sender = Sender(server='127.0.0.1', port=10051)
response = sender.send_value('myhost', 'cpu.usage', 75.5)
```

### Getter Usage
```python
from zabbix_utils import Getter

agent = Getter(host='127.0.0.1', port=10050)
resp = agent.get('system.uname')
print(resp.value)
```

## Environment Variables

- `ZABBIX_URL` - Zabbix server URL
- `ZABBIX_TOKEN` - API authentication token
- `ZABBIX_USER` - Username (alternative to token)
- `ZABBIX_PASSWORD` - Password (alternative to token)
- `ZABBIX_SERVER` - Zabbix server for Sender operations
- `ZABBIX_SERVER_PORT` - Zabbix server port (default: 10051)
- `ZABBIX_AGENT_HOST` - Zabbix agent host for Getter operations
- `ZABBIX_AGENT_PORT` - Zabbix agent port (default: 10050)

## Security

- Use API tokens instead of username/password
- Enable SSL/TLS certificate verification in production
- Use PSK or certificate encryption for Sender/Getter
- Store credentials in environment variables
- Never commit credentials to version control

## License

This skill uses the python-zabbix-utils library which is licensed under MIT License.

## Support

For issues related to:
- This skill: See SKILL.md documentation
- python-zabbix-utils library: https://github.com/zabbix/python-zabbix-utils
- Zabbix: https://www.zabbix.com/documentation
