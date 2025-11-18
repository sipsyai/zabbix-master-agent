# Zabbix Sender Advanced Configuration

Advanced configurations and use cases for Zabbix Sender protocol.

## Basic Setup

```python
from zabbix_utils import Sender, ItemValue

sender = Sender(
    server='127.0.0.1',
    port=10051,
    source_ip='10.0.0.1',  # Optional: bind to specific IP
    timeout=5,  # Connection timeout in seconds
    chunk_size=250  # Items per packet (default: 250)
)
```

## Single Value Sending

### With Current Timestamp
```python
response = sender.send_value('myhost', 'cpu.usage', 75.5)
```

### With Custom Timestamp
```python
import time

timestamp = int(time.time())
response = sender.send_value('myhost', 'cpu.usage', 75.5, timestamp)
```

### With Nanoseconds Precision
```python
response = sender.send_value('myhost', 'cpu.usage', 75.5, timestamp, ns=500000000)
```

## Bulk Value Sending

### Multiple Metrics
```python
from zabbix_utils import ItemValue

items = [
    ItemValue('host1', 'cpu.usage', 80.0),
    ItemValue('host1', 'memory.used', 4096),
    ItemValue('host1', 'disk.free', 50.5),
    ItemValue('host2', 'cpu.usage', 45.2),
    ItemValue('host2', 'network.in', 1024000)
]

response = sender.send(items)

print(f"Processed: {response.processed}")
print(f"Failed: {response.failed}")
print(f"Total: {response.total}")
print(f"Time: {response.time}")
```

### With Timestamps
```python
import time

timestamp = int(time.time())
items = [
    ItemValue('host1', 'cpu.usage', 80.0, timestamp),
    ItemValue('host1', 'memory.used', 4096, timestamp),
    ItemValue('host2', 'cpu.usage', 45.2, timestamp - 60)  # 1 minute ago
]

response = sender.send(items)
```

## Multiple Cluster Support

Send to multiple Zabbix clusters simultaneously:

```python
clusters = [
    ['zabbix1.dc1.com', 'zabbix2.dc1.com:10051'],
    ['zabbix1.dc2.com:10051', 'zabbix2.dc2.com:20051'],
    ['zabbix.dc3.com']
]

sender = Sender(clusters=clusters)
response = sender.send_value('myhost', 'cpu.usage', 75.5)

# Check detailed response per cluster
for server, responses in response.details.items():
    print(f"{server}: {responses}")
```

## Using Zabbix Agent Configuration

Load sender configuration from zabbix_agentd.conf:

```python
sender = Sender(config='/etc/zabbix/zabbix_agentd.conf')
response = sender.send_value('myhost', 'cpu.usage', 75.5)
```

Configuration file format:
```ini
Server=zabbix.example.com:10051
Hostname=myhost
```

## TLS/PSK Encryption

### PSK (Pre-Shared Key) Encryption

```python
from zabbix_utils import Sender, PSKContext

# Create PSK context
psk = PSKContext(
    psk_identity="PSK 001",
    psk_hex="1234567890abcdef1234567890abcdef"  # 32-char hex string
)

sender = Sender(
    server='zabbix.example.com',
    port=10051,
    psk_context=psk
)

response = sender.send_value('myhost', 'secret.metric', 'sensitive-data')
```

### PSK from Configuration File

```python
sender = Sender(
    config='/etc/zabbix/zabbix_agentd.conf',
    use_config_psk=True  # Use PSK settings from config
)
```

Configuration file with PSK:
```ini
Server=zabbix.example.com:10051
Hostname=myhost
TLSConnect=psk
TLSAccept=psk
TLSPSKIdentity=PSK 001
TLSPSKFile=/etc/zabbix/zabbix_agentd.psk
```

### Certificate-Based TLS

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

## Response Handling

### Check Response Status
```python
response = sender.send_value('myhost', 'cpu.usage', 75.5)

if response.failed == 0:
    print("All values sent successfully")
else:
    print(f"Failed to send {response.failed} out of {response.total} values")
```

### Response Attributes
```python
print(f"Processed: {response.processed}")  # Successfully processed items
print(f"Failed: {response.failed}")        # Failed items
print(f"Total: {response.total}")          # Total items sent
print(f"Time: {response.time}")            # Processing time (seconds)
print(f"Chunk: {response.chunk}")          # Number of chunks sent
```

## Async Operations

For high-performance scenarios:

```python
import asyncio
from zabbix_utils import AsyncSender, ItemValue

async def send_metrics():
    sender = AsyncSender(server='127.0.0.1', port=10051)
    
    items = [
        ItemValue('host1', 'cpu.usage', 80.0),
        ItemValue('host1', 'memory.used', 4096)
    ]
    
    response = await sender.send(items)
    print(f"Processed: {response.processed}")

asyncio.run(send_metrics())
```

## Data Type Examples

### Numeric Values
```python
items = [
    ItemValue('host1', 'cpu.usage', 75.5),      # Float
    ItemValue('host1', 'process.count', 42),    # Integer
    ItemValue('host1', 'memory.bytes', 4294967296)  # Large integer
]
```

### String Values
```python
items = [
    ItemValue('host1', 'status.message', 'OK'),
    ItemValue('host1', 'version.info', '1.2.3')
]
```

### JSON Values
```python
import json

data = {
    "cpu": 75.5,
    "memory": 4096,
    "disk": {"free": 100, "used": 50}
}

items = [
    ItemValue('host1', 'system.metrics', json.dumps(data))
]
```

## Error Handling

```python
from zabbix_utils import Sender
from zabbix_utils.exceptions import ProcessingError

try:
    sender = Sender(server='invalid-server', port=10051, timeout=5)
    response = sender.send_value('myhost', 'cpu.usage', 75.5)
except ProcessingError as e:
    print(f"Failed to send: {e}")
except ConnectionError as e:
    print(f"Connection failed: {e}")
```

## Chunking Large Batches

For sending thousands of metrics:

```python
sender = Sender(
    server='127.0.0.1',
    port=10051,
    chunk_size=100  # Send 100 items per packet
)

# Generate large dataset
items = [
    ItemValue(f'host{i}', 'cpu.usage', i % 100)
    for i in range(10000)
]

response = sender.send(items)
print(f"Sent {response.total} items in {response.chunk} chunks")
```

## Best Practices

1. **Batch Operations**: Send multiple items in one call when possible
2. **Error Handling**: Always check `response.failed` count
3. **Timeouts**: Set appropriate timeouts for your network
4. **Chunk Size**: Adjust chunk_size for large batches (default 250 is optimal)
5. **TLS/PSK**: Use encryption for sensitive data
6. **Item Types**: Ensure items are type "Zabbix trapper" in Zabbix
7. **Timestamps**: Use current time or recent past (not future)
8. **Async**: Use AsyncSender for high-volume scenarios

## Common Issues

**"Failed to send value"**
- Ensure host exists in Zabbix
- Verify item exists and is type "Zabbix trapper"
- Check item key matches exactly
- Verify firewall allows port 10051

**"Connection timeout"**
- Check Zabbix server/proxy is running
- Verify network connectivity
- Check firewall rules
- Increase timeout parameter

**"Invalid timestamp"**
- Don't use future timestamps
- Ensure timestamp is Unix epoch (seconds)
- Check Zabbix item history settings
