# Items & Graphs Creation Examples

This directory contains scripts for creating and managing Zabbix items and graphs.

## Scripts

### create_graph.py
Create custom graphs in Zabbix.

**Features:**
- Create graphs from templates
- Configure graph items
- Set graph properties (colors, styles)
- Bulk graph creation

**Usage:**
```bash
python create_graph.py
```

### create_working_memory_item.py
Create memory monitoring items.

**Features:**
- Create memory utilization items
- Configure memory thresholds
- Set up memory triggers
- Memory metric collection

**Usage:**
```bash
python create_working_memory_item.py
```

### create_memory_util_graph.py
Create memory utilization graphs.

**Features:**
- Visual memory monitoring
- Multiple memory metrics
- Threshold visualization
- Historical memory trends

**Usage:**
```bash
python create_memory_util_graph.py
```

### fix_memory_utilization.py
Fix memory monitoring configuration issues.

**Features:**
- Repair broken memory items
- Update memory calculations
- Fix trigger expressions
- Reconfigure memory graphs

**Usage:**
```bash
python fix_memory_utilization.py
```

### check_dependent_items.py
Verify and manage dependent items.

**Features:**
- Check dependent item chains
- Validate master items
- Verify preprocessing rules
- Dependent item troubleshooting

**Usage:**
```bash
python check_dependent_items.py
```

## Item Types

### Zabbix Agent Items
- Direct data collection from agents
- High performance
- Wide range of metrics

### Dependent Items
- Process data from master items
- Reduce agent overhead
- JSON/XML parsing
- Data transformation

### Calculated Items
- Mathematical operations
- Cross-item calculations
- Custom formulas

## Item Configuration

Key parameters:
- **Type**: Agent, SNMP, dependent, calculated, etc.
- **Key**: Unique identifier for the item
- **Update interval**: How often data is collected
- **History**: How long to keep detailed data
- **Trends**: How long to keep aggregated data

## Graph Configuration

Graph parameters:
- **Width/Height**: Display dimensions
- **Graph type**: Normal, stacked, pie, exploded
- **Show legend**: Display item names
- **Show triggers**: Display trigger lines
- **Y-axis**: Min/max values, scale

## Best Practices

1. **Use dependent items**: Reduce agent load with single data collection
2. **Set appropriate intervals**: Balance granularity vs. performance
3. **Configure trends properly**: Long-term storage with aggregation
4. **Use preprocessing**: Transform data at collection time
5. **Create graph templates**: Reuse graph configurations

## Item Preprocessing

Common preprocessing steps:
- **Regular expression**: Extract specific values
- **JSONPath**: Parse JSON responses
- **XML XPath**: Parse XML data
- **Multiplier**: Unit conversion
- **Delta**: Calculate change between values
- **JavaScript**: Custom data transformation

## Troubleshooting

- **"Item not supported"**: Check agent version and item key syntax
- **"No data"**: Verify collection interval and agent connectivity
- **"Invalid key"**: Check item key format and parameters
- **"Dependent item failed"**: Verify master item is collecting data
