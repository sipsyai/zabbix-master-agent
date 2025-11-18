---
title: Definitions
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/definitions
downloaded: 2025-11-14 10:39:39
---

# 7 Definitions

#### Overview

While many things in the frontend can be configured using the frontend itself, some customizations are currently only possible by editing a definitions file.

This file is `defines.inc.php` located in /include of the Zabbix HTML document directory.

#### Parameters

Parameters in this file that could be of interest to users:

  * ZBX_MIN_PERIOD

Minimum graph period, in seconds. One minute by default.

  * GRAPH_YAXIS_SIDE_DEFAULT

Default location of Y axis in simple graphs and default value for drop down box when adding items to custom graphs. Possible values: 0 - left, 1 - right.

Default: 0

  * ZBX_SESSION_NAME

String used as the name of the Zabbix frontend session cookie.

Default: zbx_sessionid

  * ZBX_DATA_CACHE_TTL

TTL timeout in seconds used to invalidate data cache of [Vault response](/documentation/current/en/manual/config/secrets). Set 0 to disable Vault response caching.

Default: 60

  * SUBFILTER_VALUES_PER_GROUP

Number of subfilter values per group (For example, in the [latest data](/documentation/current/en/manual/web_interface/frontend_sections/monitoring/latest_data) subfilter).

Default: 1000

  * ZBX_MAX_WIDGET_LINES

Maximum number of widget lines to display.

Default: 1000