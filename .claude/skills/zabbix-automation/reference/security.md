# Security Configuration

Security best practices and encryption setup for Zabbix operations.

## API Token Security

### Generate API Token
1. Login to Zabbix UI
2. Navigate to Administration > Users
3. Select user > API tokens tab
4. Create new token
5. Set expiration date
6. Copy token immediately (shown once)

### Use API Token
```python
from zabbix_utils import ZabbixAPI

api = ZabbixAPI(url="https://zabbix.example.com")
api.login(token="your-api-token-here")
# No need to logout with token auth
```

### Store Tokens Securely
```bash
# Environment variable (recommended)
export ZABBIX_TOKEN="your-token"

# Or use secrets management
# - HashiCorp Vault
# - AWS Secrets Manager
# - Azure Key Vault
```

## SSL/TLS Configuration

### Enable Certificate Verification
```python
api = ZabbixAPI(
    url="https://zabbix.example.com",
    validate_certs=True  # Verify SSL certificate
)
```

### Custom CA Certificate
```python
import ssl

context = ssl.create_default_context(cafile="/path/to/ca.crt")

api = ZabbixAPI(
    url="https://zabbix.example.com",
    ssl_context=context
)
```

## PSK Encryption for Sender

### Generate PSK Key
```bash
# Generate 32-byte (256-bit) PSK
openssl rand -hex 32 > zabbix.psk
```

### Configure Zabbix Server
In zabbix_server.conf:
```ini
TLSPSKIdentity=PSK 001
TLSPSKFile=/etc/zabbix/zabbix.psk
```

### Use PSK in Python
```python
from zabbix_utils import Sender, PSKContext

# Read PSK from file
with open('zabbix.psk', 'r') as f:
    psk_hex = f.read().strip()

psk = PSKContext(
    psk_identity="PSK 001",
    psk_hex=psk_hex
)

sender = Sender(
    server='zabbix.example.com',
    port=10051,
    psk_context=psk
)

response = sender.send_value('host', 'secret.metric', 'sensitive-data')
```

## PSK Encryption for Getter

### Configure Agent
In zabbix_agentd.conf:
```ini
TLSConnect=psk
TLSAccept=psk
TLSPSKIdentity=PSK 001
TLSPSKFile=/etc/zabbix/zabbix_agentd.psk
```

### Use PSK in Python
```python
from zabbix_utils import Getter, PSKContext

with open('zabbix.psk', 'r') as f:
    psk_hex = f.read().strip()

psk = PSKContext(
    psk_identity="PSK 001",
    psk_hex=psk_hex
)

agent = Getter(
    host='agent.example.com',
    port=10050,
    psk_context=psk
)

resp = agent.get('system.uname')
```

## Certificate-Based TLS

### For Sender
```python
from zabbix_utils import Sender, CertContext

cert = CertContext(
    cert_file='/path/to/client.crt',
    key_file='/path/to/client.key',
    ca_file='/path/to/ca.crt'
)

sender = Sender(
    server='zabbix.example.com',
    port=10051,
    cert_context=cert
)
```

### For Getter
```python
from zabbix_utils import Getter, CertContext

cert = CertContext(
    cert_file='/path/to/client.crt',
    key_file='/path/to/client.key',
    ca_file='/path/to/ca.crt'
)

agent = Getter(
    host='agent.example.com',
    port=10050,
    cert_context=cert
)
```

## Credential Management

### Environment Variables
```bash
export ZABBIX_URL="https://zabbix.example.com"
export ZABBIX_TOKEN="your-token"
export ZABBIX_SERVER="zabbix.example.com"
export ZABBIX_AGENT_HOST="agent.example.com"
```

### Configuration File
```python
import json

with open('zabbix_config.json', 'r') as f:
    config = json.load(f)

api = ZabbixAPI(url=config['url'])
api.login(token=config['token'])
```

zabbix_config.json:
```json
{
  "url": "https://zabbix.example.com",
  "token": "your-token"
}
```

## Access Control

### Least Privilege API Tokens
Create tokens with minimal required permissions:
- Read-only for monitoring
- Specific object permissions
- Short expiration times

### IP Restrictions
Configure Zabbix to allow API access only from specific IPs.

### Audit Logging
Enable audit logging in Zabbix to track API usage.

## Best Practices

1. Use API tokens instead of username/password
2. Enable SSL/TLS certificate verification
3. Use PSK or certificates for Sender/Getter
4. Store credentials in environment variables or secrets management
5. Rotate API tokens regularly
6. Use short-lived tokens when possible
7. Never commit credentials to version control
8. Use .gitignore for config files with secrets
9. Implement proper error handling (don't expose credentials in errors)
10. Use read-only tokens for monitoring operations

## Example .gitignore
```
# Credentials and secrets
.env
*.psk
zabbix_config.json
*.key
*.crt

# Virtual environment
venv/
```

## Secret Scanning
Use tools to prevent credential leaks:
- git-secrets
- truffleHog
- GitGuardian
