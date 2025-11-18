---
title: Value cache
source: https://www.zabbix.com/documentation/current/en/manual/config/items/value_cache
downloaded: 2025-11-14 10:35:28
---

# 10 Value cache

#### Overview

To make the calculation of trigger expressions, calculated items and some macros much faster, a value cache option is supported by the Zabbix server.

This in-memory cache can be used for accessing historical data, instead of making direct SQL calls to the database. If historical values are not present in the cache, the missing values are requested from the database and the cache updated accordingly.

Item values remain in value cache either until:

  * the item is deleted (cached values are deleted after the next configuration sync);
  * the item value is outside the time or count range specified in the trigger/calculated item expression (cached value is removed when a new value is received);
  * the time or count range specified in the trigger/calculated item expression is changed so that less data is required for calculation (unnecessary cached values are removed after 24 hours).

Value cache status can be observed by using the server [runtime control](/documentation/current/en/manual/concepts/server#runtime-control) option `diaginfo` (or `diaginfo=valuecache`) and inspecting the section for value cache diagnostic information. This can be useful for determining misconfigured triggers or calculated items.

To enable the value cache functionality, an optional **ValueCacheSize** parameter is supported by the Zabbix server [configuration](/documentation/current/en/manual/appendix/config/zabbix_server) file.

Two internal items are supported for monitoring the value cache: **zabbix[vcache,buffer, <mode>]** and **zabbix[vcache,cache, <parameter>]**. See more details with [internal items](/documentation/current/en/manual/config/items/itemtypes/internal).