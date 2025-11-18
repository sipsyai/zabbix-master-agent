# Zabbix Getter Advanced Configuration

Advanced configurations for Zabbix Getter protocol (retrieving values from Zabbix agents).

## Basic Setup

```python
from zabbix_utils import Getter

agent = Getter(
    host='127.0.0.1',
    port=10050,
    source_ip='10.0.0.1',  # Optional
    timeout=5
)
```

## Value Retrieval Examples

### System Information
```python
# System name
resp = agent.get('system.uname')
if not resp.error:
    print(f"System: {resp.value}")

# Uptime
resp = agent.get('system.uptime')
if not resp.error:
    print(f"Uptime: {resp.value} seconds")
```

### CPU Metrics
```python
resp = agent.get('system.cpu.util[,user]')
if not resp.error:
    print(f"CPU user: {resp.value}%")
```

### Memory Metrics
```python
resp = agent.get('vm.memory.size[total]')
if not resp.error:
    print(f"Total memory: {resp.value} bytes")
```

## Discovery Rules

```python
import json

resp = agent.get('net.if.discovery')
if not resp.error:
    interfaces = json.loads(resp.value)
    for iface in interfaces:
        print(f"Interface: {iface['{#IFNAME}']}")
```

## TLS/PSK Encryption

```python
from zabbix_utils import Getter, PSKContext

psk = PSKContext(
    psk_identity="PSK 001",
    psk_hex="1234567890abcdef1234567890abcdef"
)

agent = Getter(
    host='agent.example.com',
    port=10050,
    psk_context=psk
)

resp = agent.get('system.uname')
```

## Async Operations

```python
import asyncio
from zabbix_utils import AsyncGetter

async def get_metrics():
    agent = AsyncGetter(host='127.0.0.1', port=10050)
    resp = await agent.get('system.cpu.util')
    print(f"CPU: {resp.value}")

asyncio.run(get_metrics())
```

## Common Item Keys

- system.uname - System information
- system.uptime - Uptime in seconds
- system.cpu.util - CPU utilization
- vm.memory.size - Memory metrics
- vfs.fs.size - Filesystem size
- net.if.in/out - Network traffic
- proc.num - Process count
- agent.ping - Agent availability

## Error Handling

```python
resp = agent.get('system.uname')

if resp.error:
    print(f"Error: {resp.error}")
else:
    print(f"Value: {resp.value}")
```

## Best Practices

1. Always check resp.error before using resp.value
2. Set appropriate timeouts
3. Use exact item key syntax
4. Parse JSON for discovery rules
5. Use PSK for sensitive data
6. Use AsyncGetter for concurrent queries
