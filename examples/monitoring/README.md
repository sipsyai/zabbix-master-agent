# Monitoring & Graphs Examples

This directory contains scripts for analyzing graphs and diagnosing monitoring issues in Zabbix.

## Scripts

### analyze_all_graphs.py
Comprehensive analysis of all graphs in Zabbix.

**Features:**
- Scan all graphs for issues
- Identify graphs with no data
- Check graph configurations
- Generate analysis reports

**Usage:**
```bash
python analyze_all_graphs.py
```

### check_graph_issue.py
Check specific graph problems and configurations.

**Features:**
- Detailed graph inspection
- Item availability checks
- Data collection verification
- Graph configuration validation

**Usage:**
```bash
python check_graph_issue.py
```

### check_cpu_graph.py
CPU graph diagnostics and troubleshooting.

**Features:**
- CPU metric verification
- Graph data validation
- Item configuration check
- Performance analysis

**Usage:**
```bash
python check_cpu_graph.py
```

### check_specific_cpu_graph.py
Detailed analysis of specific CPU graphs.

**Features:**
- Per-core CPU analysis
- Load average checking
- Historical data review
- Threshold validation

**Usage:**
```bash
python check_specific_cpu_graph.py
```

### diagnose_graph_no_data.py
Diagnose why graphs are not showing data.

**Features:**
- Item state verification
- Data collection checks
- Agent connectivity tests
- Trigger and problem analysis

**Usage:**
```bash
python diagnose_graph_no_data.py
```

## Common Graph Issues

### No Data in Graph
Possible causes:
- Item is disabled
- Agent is not responding
- Item key is incorrect
- Data type mismatch
- History storage issues

### Incorrect Data
Possible causes:
- Wrong item type
- Incorrect preprocessing
- Formula errors
- Unit conversion issues

### Performance Issues
Possible causes:
- Too many items on one graph
- High-frequency data collection
- Long time periods
- Insufficient server resources

## Graph Types

Zabbix supports several graph types:
- **Normal** - Standard line graph
- **Stacked** - Cumulative values
- **Pie** - Percentage distribution
- **Exploded** - Separated pie chart

## Best Practices

1. **Use appropriate update intervals**: Balance between data granularity and performance
2. **Set reasonable history retention**: Avoid excessive storage usage
3. **Group related items**: Create logical graph groupings
4. **Use templates**: Standardize graphs across similar hosts
5. **Monitor graph performance**: Track graph generation time

## Troubleshooting

- **"No permissions"**: Check user role and permissions
- **"Item not supported"**: Verify agent version and item key
- **"Graph is empty"**: Check data collection and history settings
- **"Slow graph loading"**: Reduce time range or number of items
