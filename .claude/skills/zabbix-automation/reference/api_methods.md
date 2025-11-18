# Zabbix API Methods Reference

Complete reference for Zabbix API methods available through zabbix_utils.

## Connection and Authentication

### Create API Instance
```python
from zabbix_utils import ZabbixAPI

api = ZabbixAPI(
    url="https://zabbix.example.com",
    validate_certs=True,  # Enable SSL verification
    timeout=30  # Request timeout in seconds
)
```

### Login Methods

**Token Authentication (Recommended)**:
```python
api.login(token="your-api-token")
```

**Username/Password**:
```python
api.login(user="Admin", password="zabbix")
# Remember to logout when done
api.logout()
```

## User Operations

### Get Users
```python
users = api.user.get(
    output=['userid', 'username', 'name', 'surname', 'roleid'],
    selectMedias='extend',
    selectUsrgrps='extend'
)
```

### Create User
```python
user = api.user.create(
    username="newuser",
    passwd="SecurePassword123",
    roleid="1",  # User role ID
    usrgrps=[{"usrgrpid": "7"}]  # User group ID
)
```

### Update User
```python
api.user.update(
    userid="123",
    name="Updated Name",
    surname="Updated Surname"
)
```

### Delete User
```python
api.user.delete("123", "124", "125")  # Can delete multiple
```

## Host Operations

### Get Hosts
```python
hosts = api.host.get(
    output=['hostid', 'host', 'name', 'status'],
    selectInterfaces=['interfaceid', 'ip', 'port'],
    selectGroups=['groupid', 'name'],
    selectTags='extend',
    filter={'status': '0'}  # 0=monitored, 1=unmonitored
)
```

### Create Host
```python
host = api.host.create(
    host="NewServer",
    name="New Server Visible Name",
    interfaces=[{
        "type": 1,  # 1=Agent, 2=SNMP, 3=IPMI, 4=JMX
        "main": 1,
        "useip": 1,
        "ip": "192.168.1.100",
        "dns": "",
        "port": "10050"
    }],
    groups=[{"groupid": "2"}],  # Linux servers group
    templates=[{"templateid": "10001"}],  # Link templates
    tags=[
        {"tag": "Environment", "value": "Production"},
        {"tag": "Location", "value": "DC1"}
    ]
)
```

### Update Host
```python
api.host.update(
    hostid="10001",
    name="Updated Host Name",
    status="1"  # Disable monitoring
)
```

### Delete Host
```python
api.host.delete("10001", "10002")
```

## Host Group Operations

### Get Host Groups
```python
groups = api.hostgroup.get(
    output=['groupid', 'name'],
    selectHosts=['hostid', 'name']
)
```

### Create Host Group
```python
group = api.hostgroup.create(
    name="Web Servers"
)
```

## Item Operations

### Get Items
```python
items = api.item.get(
    hostids="10001",
    output=['itemid', 'name', 'key_', 'lastvalue', 'lastclock'],
    filter={'status': '0'},  # Enabled items
    search={'key_': 'cpu'},  # Search in key
    searchWildcardsEnabled=True
)
```

### Create Item
```python
item = api.item.create(
    name="Custom CPU Usage",
    key_="system.cpu.util[,user]",
    hostid="10001",
    type=0,  # 0=Zabbix agent, 2=Zabbix trapper
    value_type=0,  # 0=float, 1=character, 2=log, 3=unsigned, 4=text
    delay="30s",
    history="7d",
    trends="365d"
)
```

### Create Trapper Item (for Sender)
```python
item = api.item.create(
    name="Custom Metric",
    key_="custom.metric",
    hostid="10001",
    type=2,  # Zabbix trapper
    value_type=0,  # Float
    delay=0  # No delay for trapper
)
```

## Template Operations

### Get Templates
```python
templates = api.template.get(
    output=['templateid', 'name'],
    selectHosts=['hostid', 'name'],
    selectItems=['itemid', 'name']
)
```

### Import Template
```python
with open('template.xml', 'r', encoding='utf-8') as f:
    template_source = f.read()

result = api.configuration.import_(
    source=template_source,
    format="xml",
    rules={
        "templates": {"createMissing": True, "updateExisting": True},
        "items": {"createMissing": True, "updateExisting": True},
        "triggers": {"createMissing": True, "updateExisting": True}
    }
)
```

### Export Template
```python
result = api.configuration.export(
    format="xml",
    options={
        "templates": ["10001", "10002"]
    }
)

with open('exported_template.xml', 'w', encoding='utf-8') as f:
    f.write(result)
```

## Trigger Operations

### Get Triggers
```python
triggers = api.trigger.get(
    hostids="10001",
    output=['triggerid', 'description', 'priority', 'status'],
    selectFunctions='extend',
    selectItems=['itemid', 'name']
)
```

### Create Trigger
```python
trigger = api.trigger.create(
    description="High CPU usage on {HOST.NAME}",
    expression="{MyHost:system.cpu.util.avg(5m)}>80",
    priority=3  # 0-5, where 5 is disaster
)
```

## Problem/Event Operations

### Get Current Problems
```python
problems = api.problem.get(
    output=['eventid', 'objectid', 'name', 'severity'],
    selectAcknowledges='extend',
    recent=True,
    sortfield=['eventid'],
    sortorder='DESC'
)
```

## History Operations

### Get Item History
```python
history = api.history.get(
    itemids="10001",
    history=0,  # 0=float, 1=string, 2=log, 3=int, 4=text
    time_from="1634000000",
    time_till="1634086400",
    output='extend',
    sortfield='clock',
    sortorder='DESC',
    limit=100
)
```

## Version Information

### Get API Version
```python
version = api.api_version()
print(f"Version: {version}")
print(f"Major: {version.major}")
print(f"Minor: {version.minor}")
print(f"Is LTS: {version.is_lts()}")

# Version comparison
if version >= 7.0:
    # Use v7+ features
    pass
```

### Get Zabbix Server Info
```python
info = api.apiinfo.version()
print(f"Server version: {info}")
```

## Error Handling

```python
from zabbix_utils import ZabbixAPI
from zabbix_utils.exceptions import APIRequestError, ProcessingError

try:
    api = ZabbixAPI(url="https://zabbix.example.com")
    api.login(token="invalid-token")
except APIRequestError as e:
    print(f"API request failed: {e}")
except ProcessingError as e:
    print(f"Processing error: {e}")
```

## Best Practices

1. **Use API Tokens**: More secure than username/password
2. **Filter Results**: Use `output`, `filter`, `search` to minimize data transfer
3. **Batch Operations**: Delete/update multiple entities in one call
4. **Check Version**: Use version checks for compatibility
5. **Handle Errors**: Always wrap API calls in try/except
6. **Logout**: Call `api.logout()` when using password auth
