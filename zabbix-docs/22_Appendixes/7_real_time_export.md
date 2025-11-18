---
title: Newline-delimited JSON export protocol
source: https://www.zabbix.com/documentation/current/en/manual/appendix/protocols/real_time_export
downloaded: 2025-11-14 10:47:17
---

# 7 Newline-delimited JSON export protocol

This section presents details of the export protocol in a newline-delimited JSON format, used in:

  * [data export to files](/documentation/current/en/manual/config/export/files)
  * [streaming to external systems](/documentation/current/en/manual/config/export/streaming)

The following can be exported:

  * trigger events
  * item values
  * trends (export to files only)

All files have a .ndjson extension. Each line of the export file is a JSON object.

#### Trigger events

The following information is exported for a problem event:

_clock_ | number | Number of seconds since Epoch to the moment when problem was detected (integer part).  
---|---|---  
_ns_ | number | Number of nanoseconds to be added to `clock` to get a precise problem detection time.  
_value_ | number | 1 (always).  
_eventid_ | number | Problem event ID.  
_name_ | string | Problem event name.  
_severity_ | number | Problem event severity (0 - Not classified, 1 - Information, 2 - Warning, 3 - Average, 4 - High, 5 - Disaster).  
_hosts_ | array | List of hosts involved in the trigger expression; there should be at least one element in array.  
| - | object  
| _host_ | string | Host name.  
_name_ | string | Visible host name.  
_groups_ | array | List of host groups of all hosts involved in the trigger expression; there should be at least one element in array.  
| - | string | Host group name.  
_tags_ | array | List of problem tags (can be empty).  
| - | object  
| _tag_ | string | Tag name.  
_value_ | string | Tag value (can be empty).  
  
The following information is exported for a recovery event:

_clock_ | number | Number of seconds since Epoch to the moment when problem was resolved (integer part).  
---|---|---  
_ns_ | number | Number of nanoseconds to be added to `clock` to get a precise problem resolution time.  
_value_ | number | 0 (always).  
_eventid_ | number | Recovery event ID.  
_p_eventid_ | number | Problem event ID.  
  
##### Examples

Problem:
    
    
    {"clock":1519304285,"ns":123456789,"value":1,"name":"Either Zabbix agent is unreachable on Host B or pollers are too busy on Zabbix Server","severity":3,"eventid":42, "hosts":[{"host":"Host B", "name":"Host B visible"},{"host":"Zabbix Server","name":"Zabbix Server visible"}],"groups":["Group X","Group Y","Group Z","Zabbix servers"],"tags":[{"tag":"availability","value":""},{"tag":"data center","value":"Riga"}]}

Copy

✔ Copied

Recovery:
    
    
    {"clock":1519304345,"ns":987654321,"value":0,"eventid":43,"p_eventid":42}

Copy

✔ Copied

Problem (multiple problem event generation):
    
    
    {"clock":1519304286,"ns":123456789,"value":1,"eventid":43,"name":"Either Zabbix agent is unreachable on Host B or pollers are too busy on Zabbix Server","severity":3,"hosts":[{"host":"Host B", "name":"Host B visible"},{"host":"Zabbix Server","name":"Zabbix Server visible"}],"groups":["Group X","Group Y","Group Z","Zabbix servers"],"tags":[{"tag":"availability","value":""},{"tag":"data center","value":"Riga"}]}
           
           {"clock":1519304286,"ns":123456789,"value":1,"eventid":43,"name":"Either Zabbix agent is unreachable on Host B or pollers are too busy on Zabbix Server","severity":3,"hosts":[{"host":"Host B", "name":"Host B visible"},{"host":"Zabbix Server","name":"Zabbix Server visible"}],"groups":["Group X","Group Y","Group Z","Zabbix servers"],"tags":[{"tag":"availability","value":""},{"tag":"data center","value":"Riga"}]}

Copy

✔ Copied

Recovery:
    
    
    {"clock":1519304346,"ns":987654321,"value":0,"eventid":44,"p_eventid":43}
           
           {"clock":1519304346,"ns":987654321,"value":0,"eventid":44,"p_eventid":42}

Copy

✔ Copied

#### Item values

The following information is exported for a collected item value:

_host_ | object | Host name of the item host.  
---|---|---  
| host | string | Host name.  
name | string | Visible host name.  
_groups_ | array | List of host groups of the item host; there should be at least one element in array.  
| - | string | Host group name.  
_item_tags_ | array | List of item tags (can be empty).  
| - | object  
| _tag_ | string | Tag name.  
_value_ | string | Tag value (can be empty).  
_itemid_ | number | Item ID.  
_name_ | string | Visible item name.  
_clock_ | number | Number of seconds since Epoch to the moment when value was collected (integer part).  
_ns_ | number | Number of nanoseconds to be added to `clock` to get a precise value collection time.  
_timestamp_  
(_Log_ only) | number | 0 if not available.  
_source_  
(_Log_ only) | string | Empty string if not available.  
_severity_  
(_Log_ only) | number | 0 if not available.  
_eventid_  
(_Log_ only) | number | 0 if not available.  
_value_ | number (for numeric items) or  
string (for text items) | Collected item value.  
_type_ | number | Collected value type:  
0 - numeric float, 1 - character, 2 - log, 3 - numeric unsigned, 4 - text, 5 - binary  
  
##### Examples

Numeric (unsigned) value:
    
    
    {"host":{"host":"Host B","name":"Host B visible"},"groups":["Group X","Group Y","Group Z"],"item_tags":[{"tag":"foo","value":"test"}],"itemid":3,"name":"Agent availability","clock":1519304285,"ns":123456789,"value":1,"type":3}

Copy

✔ Copied

Numeric (float) value:
    
    
    {"host":{"host":"Host B","name":"Host B visible"},"groups":["Group X","Group Y","Group Z"],"item_tags":[{"tag":"foo","value":"test"}],"itemid":4,"name":"CPU Load","clock":1519304285,"ns":123456789,"value":0.1,"type":0}

Copy

✔ Copied

Character, text value:
    
    
    {"host":{"host":"Host B","name":"Host B visible"},"groups":["Group X","Group Y","Group Z"],"item_tags":[{"tag":"foo","value":"test"}],"itemid":2,"name":"Agent version","clock":1519304285,"ns":123456789,"value":"3.4.4","type":4}

Copy

✔ Copied

Log value:
    
    
    {"host":{"host":"Host A","name":"Host A visible"},"groups":["Group X","Group Y","Group Z"],"item_tags":[{"tag":"foo","value":"test"}],"itemid":1,"name":"Messages in log file","clock":1519304285,"ns":123456789,"timestamp":1519304285,"source":"","severity":0,"eventid":0,"value":"log file message","type":2}

Copy

✔ Copied

#### Trends

The following information is exported for a calculated trend value:

_host_ | object | Host name of the item host.  
---|---|---  
| host | string | Host name.  
name | string | Visible host name.  
_groups_ | array | List of host groups of the item host; there should be at least one element in array.  
| - | string | Host group name.  
_item_tags_ | array | List of item tags (can be empty).  
| - | object  
| _tag_ | string | Tag name.  
_value_ | string | Tag value (can be empty).  
_itemid_ | number | Item ID.  
_name_ | string | Visible item name.  
_clock_ | number | Number of seconds since Epoch to the moment when value was collected (integer part).  
_count_ | number | Number of values collected for a given hour.  
_min_ | number | Minimum item value for a given hour.  
_avg_ | number | Average item value for a given hour.  
_max_ | number | Maximum item value for a given hour.  
_type_ | number | Value type:  
0 - numeric float, 3 - numeric unsigned  
  
##### Examples

Numeric (unsigned) value:
    
    
    {"host":{"host":"Host B","name":"Host B visible"},"groups":["Group X","Group Y","Group Z"],"item_tags":[{"tag":"foo","value":"test"}],"itemid":3,"name":"Agent availability","clock":1519311600,"count":60,"min":1,"avg":1,"max":1,"type":3}

Copy

✔ Copied

Numeric (float) value:
    
    
    {"host":{"host":"Host B","name":"Host B visible"},"groups":["Group X","Group Y","Group Z"],"item_tags":[{"tag":"foo","value":"test"}],"itemid":4,"name":"CPU Load","clock":1519311600,"count":60,"min":0.01,"avg":0.15,"max":1.5,"type":0}

Copy

✔ Copied