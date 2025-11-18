---
title: Housekeeping
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/administration/housekeeping
downloaded: 2025-11-14 10:39:28
---

# 3 Housekeeping

#### Overview

The _Administration > Housekeeping_ section lets you set when outdated or user-deleted data is removed for:

  * Events and alerts
  * Services
  * User sessions
  * History
  * Trends

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/administration/general_housekeeper1.png)

Audit housekeeping is configured [separately](/documentation/current/en/manual/web_interface/frontend_sections/administration/audit_log).

#### Configuration

The table below describes housekeeping configuration parameters.

_Enable internal housekeeping_ | Enable (default) or disable internal housekeeping performed by the Zabbix server [housekeeper process](/documentation/current/en/manual/concepts/server#server-process-types-and-threads).  
---|---  
_Data storage period_ | Specify how long records should be kept before being removed by the housekeeper.  
Mandatory if internal housekeeping is enabled.  
Range: 1 day (1 hour for history) - 25 years; or "0". [Time suffixes](/documentation/current/en/manual/appendix/suffixes) (e.g., 1d, 1w) are supported.  
  
For _Events and alerts_ , the data storage period is set separately for triggers, services, internal data, network discovery, and autoregistration.  
The housekeeper removes only those events that are not associated with problems; for example, problem/recovery events are removed only after the associated problem is removed.  
Note that when an item/trigger is deleted, its problems are also deleted; however, the related problem/recovery events remain in the database until the housekeeper removes them.  
  
For _History_ and _Trends_ , the data storage periods also determine how long data remains visible in _Monitoring > Latest data_, even if internal housekeeping is disabled.  
_Override item history period_ | If enabled, the history/trend storage period specified in the [item configuration](/documentation/current/en/manual/config/items/item) is overridden by the _Data storage period_ setting (except for items with the _Do not store_ option enabled).  
  
This option can be used even when internal housekeeping is disabled and an external housekeeper is used.  
_Override item trend period_  
  
If using **TimescaleDB** , the _History, trends and audit log compression_ section becomes available.

For [TimescaleDB](/documentation/current/en/manual/appendix/install/timescaledb), enable _Override item history period_ , _Override item trend period_ , and _Enable internal housekeeping_ for history and trends to fully benefit from automatic partitioning. If these options are disabled, data kept in history and trends tables will still be partitioned, but the housekeeper will not drop outdated partitions, and configuration warnings will appear. When dropping of outdated partitions is enabled, Zabbix server and frontend will no longer track deleted items, and history for those items will be cleared when an outdated partition is deleted.

The _Reset defaults_ button lets you revert any changes made.