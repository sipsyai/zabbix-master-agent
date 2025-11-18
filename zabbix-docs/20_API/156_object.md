---
title: Housekeeping object
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/housekeeping/object
downloaded: 2025-11-14 10:42:29
---

# Housekeeping object

The following objects are directly related to the `housekeeping` API.

### Housekeeping

The settings object has the following properties.

hk_events_mode | integer | Enable internal housekeeping for events and alerts.  
  
Possible values:  
0 - Disable;  
1 - _(default)_ Enable.  
---|---|---  
hk_events_trigger | string | Trigger data storage period. Accepts seconds and time unit with suffix.  
  
Default: 365d.  
hk_events_service | string | Service data storage period. Accepts seconds and time unit with suffix.  
  
Default: 1d.  
hk_events_internal | string | Internal data storage period. Accepts seconds and time unit with suffix.  
  
Default: 1d.  
hk_events_discovery | string | Network discovery data storage period. Accepts seconds and time unit with suffix.  
  
Default: 1d.  
hk_events_autoreg | string | Autoregistration data storage period. Accepts seconds and time unit with suffix.  
  
Default: 1d.  
hk_services_mode | integer | Enable internal housekeeping for services.  
  
Possible values:  
0 - Disable;  
1 - _(default)_ Enable.  
hk_services | string | Services data storage period. Accepts seconds and time unit with suffix.  
  
Default: 365d.  
hk_audit_mode | integer | Enable internal housekeeping for audit.  
  
Possible values:  
0 - Disable;  
1 - _(default)_ Enable.  
hk_audit | string | Audit data storage period. Accepts seconds and time unit with suffix.  
  
Default: 31d.  
hk_sessions_mode | integer | Enable internal housekeeping for sessions.  
  
Possible values:  
0 - Disable;  
1 - _(default)_ Enable.  
hk_sessions | string | Sessions data storage period. Accepts seconds and time unit with suffix.  
  
Default: 31d.  
hk_history_mode | integer | Enable internal housekeeping for history.  
  
Possible values:  
0 - Disable;  
1 - _(default)_ Enable.  
hk_history_global | integer | Override item history period.  
  
Possible values:  
0 - Do not override;  
1 - _(default)_ Override.  
hk_history | string | History data storage period. Accepts seconds and time unit with suffix.  
  
Default: 31d.  
hk_trends_mode | integer | Enable internal housekeeping for trends.  
  
Possible values:  
0 - Disable;  
1 - _(default)_ Enable.  
hk_trends_global | integer | Override item trend period.  
  
Possible values:  
0 - Do not override;  
1 - _(default)_ Override.  
hk_trends | string | Trends data storage period. Accepts seconds and time unit with suffix.  
  
Default: 365d.  
db_extension | string | Configuration flag DB extension. If this flag is set to "timescaledb" then the server changes its behavior for housekeeping and item deletion.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
compression_availability | integer | Whether data compression is supported by the database (or its extension).  
  
Possible values:  
0 - Unavailable;  
1 - Available.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
compression_status | integer | Enable TimescaleDB compression for history and trends.  
  
Possible values:  
0 - _(default)_ Off;  
1 - On.  
compress_older | string | Compress history and trends records older than specified period. Accepts seconds and time unit with suffix.  
  
Default: 7d.