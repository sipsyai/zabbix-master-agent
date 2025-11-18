# Installation and Setup Guide

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Network access to Zabbix server/agents
- Zabbix 6.0 or higher

## Quick Installation

1. Navigate to the skill directory:
```bash
cd python-zabbix-utils-main/zabbix-skill
```

2. Run the setup script:
```bash
python zabbix_runner.py
```

The script will automatically:
- Check Python version (requires 3.8+)
- Create virtual environment in ./venv
- Install dependencies from requirements.txt

## Manual Installation

If you prefer manual setup:

1. Create virtual environment:
```bash
python -m venv venv
```

2. Activate virtual environment:

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

### Environment Variables

Set these environment variables for seamless operation:

```bash
# API Operations
export ZABBIX_URL="https://zabbix.example.com"
export ZABBIX_TOKEN="your-api-token-here"

# Alternative: Username/Password
export ZABBIX_USER="Admin"
export ZABBIX_PASSWORD="zabbix"

# Sender Operations
export ZABBIX_SERVER="127.0.0.1"
export ZABBIX_SERVER_PORT="10051"

# Getter Operations
export ZABBIX_AGENT_HOST="127.0.0.1"
export ZABBIX_AGENT_PORT="10050"
```

### Windows (PowerShell)
```powershell
$env:ZABBIX_URL="https://zabbix.example.com"
$env:ZABBIX_TOKEN="your-api-token-here"
```

### Permanent Configuration

**Linux/Mac** - Add to ~/.bashrc or ~/.zshrc:
```bash
export ZABBIX_URL="https://zabbix.example.com"
export ZABBIX_TOKEN="your-api-token-here"
```

**Windows** - Set system environment variables via Control Panel or:
```powershell
[System.Environment]::SetEnvironmentVariable('ZABBIX_URL', 'https://zabbix.example.com', 'User')
```

## Verify Installation

Test the installation:

```python
from zabbix_utils import ZabbixAPI

api = ZabbixAPI(url="https://zabbix.example.com")
api.login(token="your-token")
print(f"Connected to Zabbix {api.version}")
```

## Troubleshooting

### Virtual Environment Not Created

**Error**: "Failed to create virtual environment"

**Solution**:
```bash
# Ensure Python 3.8+ is installed
python --version

# Try creating manually
python -m venv venv
```

### Dependency Installation Failed

**Error**: "Failed to install dependencies"

**Solutions**:
1. Update pip:
```bash
python -m pip install --upgrade pip
```

2. Install manually:
```bash
pip install zabbix-utils aiohttp
```

3. Check internet connectivity

### Import Error

**Error**: "ModuleNotFoundError: No module named 'zabbix_utils'"

**Solution**: Ensure virtual environment is activated
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate

# Verify
which python  # Should point to venv/bin/python
```

### Connection Refused

**Error**: "Connection refused to Zabbix server"

**Solutions**:
1. Verify Zabbix server is running
2. Check firewall rules (ports 80/443 for API, 10051 for Sender, 10050 for Getter)
3. Verify URL/IP is correct
4. Test network connectivity: `ping zabbix.example.com`

### Authentication Failed

**Error**: "Login failed" or "Invalid API token"

**Solutions**:
1. Verify API token is correct and not expired
2. Generate new token in Zabbix UI
3. Check user permissions
4. Try username/password authentication

## Uninstallation

To remove the skill:

1. Deactivate virtual environment (if active):
```bash
deactivate
```

2. Remove the skill directory:
```bash
rm -rf python-zabbix-utils-main/zabbix-skill
```

## Updating

To update to the latest version:

1. Activate virtual environment:
```bash
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

2. Update dependencies:
```bash
pip install --upgrade zabbix-utils aiohttp
```

## Next Steps

After installation:

1. Read [SKILL.md](SKILL.md) for usage examples
2. Review [reference/api_methods.md](reference/api_methods.md) for API operations
3. Check [reference/security.md](reference/security.md) for security best practices
4. Start automating your Zabbix operations!
