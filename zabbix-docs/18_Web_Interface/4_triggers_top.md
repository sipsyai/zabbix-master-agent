---
title: Top 100 triggers
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/reports/triggers_top
downloaded: 2025-11-14 10:38:50
---

# 4 Top 100 triggers

#### Overview

In _Reports → Top 100 triggers_ , you can see the triggers with the highest number of problems detected during the selected period.

![](/documentation/current/assets/en/manual/web_interface/triggers_top.png)

Both host and trigger column entries are links that offer some useful options:

  * for host - clicking on the host name brings up the [host menu](/documentation/current/en/manual/web_interface/menu/host_menu)
  * for trigger - clicking on the trigger name brings up links to the latest events, simple graph for each trigger item, and the configuration forms of the trigger itself and each trigger item

**Using filter**

You may use the filter to display triggers by host group, host, problem name, tags, or trigger severity. Specifying a parent host group implicitly selects all nested host groups. For better search performance, data is searched with macros unresolved.

The filter is located below the _Top 100 triggers_ section name. It can be opened and collapsed by clicking on the _Filter_ tab on the right.

**Time period selector**

The [_Time period_ selector](/documentation/current/en/manual/web_interface/time_period_selector) allows to select often required periods with one mouse click. The _Time period_ selector can be expanded and collapsed by clicking the _Time period_ tab next to the filter.