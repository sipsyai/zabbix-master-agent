# Custom Plugins Examples

This directory contains custom plugins and integrations for extending Zabbix monitoring capabilities.

## Available Plugins

### ad-logon-plugin
Active Directory logon event monitoring and tracking.

**Features:**
- Monitor user logon events
- Track authentication failures
- Session duration monitoring
- Logon/logoff statistics

**Location:** `ad-logon-plugin/`

**Scripts:**
- `setup_items.py` - Initial setup
- `setup_items_v2.py` - Enhanced setup with additional metrics

**Use Cases:**
- Security monitoring
- User activity tracking
- Login pattern analysis
- Compliance reporting

### ad-event-collector
Active Directory event collection and analysis.

**Features:**
- Collect AD events
- Security event monitoring
- Account management tracking
- Group policy changes

**Location:** `ad-event-collector/`

**Scripts:**
- `create_zabbix_items.py` - Create monitoring items for AD events

**Use Cases:**
- Security auditing
- Change tracking
- Compliance monitoring
- Incident investigation

### example-plugin
Template for creating custom Zabbix plugins.

**Features:**
- Plugin structure template
- Sample item creation
- Basic monitoring setup
- Documentation examples

**Location:** `example-plugin/`

**Use Cases:**
- Plugin development reference
- Custom monitoring implementation
- Integration templates

## Creating Custom Plugins

### Plugin Structure
```
your-plugin/
├── README.md           # Plugin documentation
├── setup_items.py      # Item creation script
├── collector.py        # Data collection script
├── config.json         # Plugin configuration
└── tests/             # Plugin tests
```

### Basic Plugin Template
```python
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Zabbix API configuration
ZABBIX_URL = os.getenv('ZABBIX_API_URL')
ZABBIX_USER = os.getenv('ZABBIX_USERNAME')
ZABBIX_PASS = os.getenv('ZABBIX_PASSWORD')

# Your plugin code here
```

### Item Creation
```python
def create_items(zabbix_api, hostid):
    """Create monitoring items for the plugin"""
    items = [
        {
            'name': 'Plugin Metric 1',
            'key_': 'plugin.metric1',
            'type': 2,  # Zabbix trapper
            'value_type': 0,  # Numeric float
            'hostid': hostid
        }
    ]
    return zabbix_api.item.create(items)
```

### Data Collection
```python
def collect_data():
    """Collect data for monitoring"""
    # Your data collection logic
    return {
        'plugin.metric1': value1,
        'plugin.metric2': value2
    }

def send_to_zabbix(data):
    """Send collected data to Zabbix"""
    # Use zabbix_sender or trapper items
    pass
```

## Plugin Types

### Agent Plugins
- Extend Zabbix Agent 2 capabilities
- Written in Go
- Native performance
- Examples: MySQL, Redis, MongoDB plugins

### External Scripts
- Standalone data collectors
- Any programming language
- Flexible integration
- Examples: Custom API integrations

### Trapper Items
- Push-based monitoring
- Event-driven collection
- Real-time updates
- Examples: Application metrics, log parsing

### User Parameters
- Custom agent checks
- Shell commands
- Simple extensions
- Examples: Custom file checks, service status

## Integration Methods

### 1. Zabbix Sender
Send data programmatically:
```bash
zabbix_sender -z zabbix-server -s "Host name" -k plugin.metric1 -o 42
```

### 2. Trapper Items
Create items that accept pushed data:
- Type: Zabbix trapper
- No polling required
- Instant updates

### 3. External Checks
Execute scripts from Zabbix server:
- Type: External check
- Script on server
- Returns single value

### 4. User Parameters
Extend agent with custom commands:
```conf
# In zabbix_agent2.conf
UserParameter=plugin.metric1,/path/to/script.sh
```

## Best Practices

### Plugin Development
1. **Use environment variables**: Store configuration in `.env`
2. **Error handling**: Implement robust error handling
3. **Logging**: Add comprehensive logging
4. **Documentation**: Document configuration and usage
5. **Testing**: Test thoroughly before deployment

### Performance
1. **Efficient collection**: Minimize resource usage
2. **Caching**: Cache data when appropriate
3. **Batch operations**: Send multiple values together
4. **Async operations**: Use asynchronous processing

### Security
1. **Credentials**: Never hardcode credentials
2. **Input validation**: Validate all inputs
3. **Least privilege**: Use minimum required permissions
4. **Encryption**: Use TLS for API communication

## Plugin Configuration

### Zabbix API Authentication
All plugins use the zabbix-master agent skill for API operations:
- Automatic authentication
- Session management
- Error handling
- Configuration from `.env`

### Item Configuration
Common item parameters:
- **Type**: Agent, trapper, external, etc.
- **Key**: Unique item identifier
- **Interval**: Update frequency
- **Value type**: Numeric, character, log, text
- **Units**: Display units
- **Preprocessing**: Data transformation

## Testing Plugins

### Unit Testing
```python
import unittest

class TestPlugin(unittest.TestCase):
    def test_data_collection(self):
        data = collect_data()
        self.assertIsNotNone(data)
        self.assertIn('plugin.metric1', data)
```

### Integration Testing
1. Test with Zabbix test server
2. Verify item creation
3. Check data collection
4. Validate triggers
5. Test error handling

## Deployment

### Installation Steps
1. Copy plugin files to appropriate location
2. Configure `.env` with Zabbix credentials
3. Run setup script to create items
4. Configure data collection (cron, service, etc.)
5. Verify data is being collected
6. Create graphs and triggers as needed

### Maintenance
- Monitor plugin performance
- Update as needed
- Check logs regularly
- Keep dependencies updated

## Troubleshooting

### Plugin Not Collecting Data
- Check credentials in `.env`
- Verify network connectivity
- Review plugin logs
- Test data collection manually

### Items Not Created
- Check API permissions
- Verify host exists
- Review item keys for duplicates
- Check Zabbix server logs

### Data Not Updating
- Verify trapper item configuration
- Check zabbix_sender syntax
- Review firewall rules
- Check Zabbix server logs

## Resources

- [Zabbix Plugin Development](https://www.zabbix.com/documentation/current/manual/config/items/itemtypes/zabbix_agent)
- [Zabbix API Documentation](https://www.zabbix.com/documentation/current/manual/api)
- [Loadable Plugins](https://www.zabbix.com/documentation/current/manual/config/items/loadable_plugins)
