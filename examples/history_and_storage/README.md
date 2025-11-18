# History & Storage Examples

This directory contains scripts for managing historical data and storage in Zabbix.

## Scripts

### check_history_storage.py
Check history storage status and configuration.

**Features:**
- Database size monitoring
- History table statistics
- Trends table analysis
- Storage usage reports
- Housekeeper status

**Usage:**
```bash
python check_history_storage.py
```

### test_history_api.py
Test history API functionality and data retrieval.

**Features:**
- History API testing
- Data retrieval validation
- Time range queries
- Item history verification
- Performance testing

**Usage:**
```bash
python test_history_api.py
```

## History Storage

Zabbix stores two types of historical data:

### History
- **Detailed data**: Original collected values
- **Short-term storage**: Typically 7-90 days
- **High granularity**: Individual data points
- **Larger storage**: More space required

### Trends
- **Aggregated data**: Hourly averages
- **Long-term storage**: Typically 365+ days
- **Lower granularity**: Hourly min/avg/max
- **Smaller storage**: Compressed data

## Value Types

Zabbix uses different tables for different data types:

- **history_uint** - Unsigned integers (0 and positive)
- **history** - Floating point numbers
- **history_str** - Short strings
- **history_text** - Long text
- **history_log** - Log entries

## Storage Configuration

### Database Settings
```sql
-- Check table sizes
SELECT
    table_name,
    round(((data_length + index_length) / 1024 / 1024), 2) AS "Size (MB)"
FROM information_schema.TABLES
WHERE table_schema = "zabbix"
    AND table_name LIKE "history%"
ORDER BY (data_length + index_length) DESC;
```

### Housekeeper Configuration
- **HousekeepingFrequency**: How often cleanup runs
- **MaxHousekeeperDelete**: Max records per cycle
- **Override item history**: Per-item retention
- **Override trend history**: Per-item trend retention

## Best Practices

### Storage Optimization
1. **Adjust retention periods**: Balance between historical visibility and storage
2. **Use trends for long-term**: Archive detailed data, keep trends
3. **Disable unnecessary items**: Don't collect data you don't need
4. **Optimize intervals**: Collect less frequently when possible
5. **Partition tables**: For large installations

### Performance Tuning
1. **Database optimization**: Regular maintenance and indexing
2. **Housekeeper tuning**: Balance cleanup vs. performance
3. **Value cache**: Increase for better performance
4. **History syncer**: Multiple processes for high load

## Data Retention Strategies

### Short-term Monitoring (Days)
- Use history for detailed analysis
- High update frequency
- Keep 7-14 days

### Long-term Monitoring (Months/Years)
- Use trends for overview
- Lower update frequency
- Keep 365+ days

### Compliance/Audit (Years)
- Export to external storage
- Archive historical data
- Use external databases

## History API

### Get History
```python
result = zabbix_api.history.get({
    'itemids': [12345],
    'time_from': 1234567890,
    'time_till': 1234567899,
    'history': 0,  # float
    'sortfield': 'clock',
    'sortorder': 'DESC',
    'limit': 100
})
```

### History Types
- 0 - numeric (float)
- 1 - character
- 2 - log
- 3 - numeric (unsigned)
- 4 - text

## Database Maintenance

### MySQL/MariaDB
```sql
-- Optimize tables
OPTIMIZE TABLE history;
OPTIMIZE TABLE history_uint;
OPTIMIZE TABLE trends;
OPTIMIZE TABLE trends_uint;

-- Check fragmentation
SELECT table_name, data_free, data_free/(data_length+index_length) AS fragmentation
FROM information_schema.tables
WHERE table_schema = 'zabbix' AND data_free > 0;
```

### PostgreSQL
```sql
-- Vacuum tables
VACUUM ANALYZE history;
VACUUM ANALYZE history_uint;
VACUUM ANALYZE trends;
VACUUM ANALYZE trends_uint;

-- Reindex
REINDEX TABLE history;
```

## Troubleshooting

### Database Growing Too Fast
- Reduce history retention
- Increase update intervals
- Disable unused items
- Check for item spam

### Slow Queries
- Add database indexes
- Optimize housekeeper
- Partition large tables
- Upgrade hardware

### Missing Historical Data
- Check housekeeper settings
- Verify retention periods
- Check database space
- Review item configuration

## Monitoring Storage

Key metrics to monitor:
- Database size growth rate
- Housekeeper performance
- Query execution time
- Disk space available
- Items per second rate
