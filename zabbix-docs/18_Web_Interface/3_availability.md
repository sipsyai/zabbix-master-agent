---
title: Availability report
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/reports/availability
downloaded: 2025-11-14 10:38:49
---

# 3 Availability report

#### Overview

In _Reports > Availability report_, you can see what proportion of time each trigger has been in the problem/OK state.

For each state, a percentage of time is displayed, making it easy to determine the availability of various elements on your system.

![](/documentation/current/assets/en/manual/web_interface/availability_host.png)

In the dropdown in the upper-right corner, you can choose the selection mode - whether to display triggers by hosts or by triggers belonging to a template.

![](/documentation/current/assets/en/manual/web_interface/availability_trigger.png)

The name of the trigger is a link to the latest events of that trigger.

#### Using filter

The filter can help narrow down the number of hosts and/or triggers displayed. For better search performance, data is searched with macros unresolved.

The filter is located below the _Availability report_ section name. It can be opened and collapsed by clicking on the _Filter_ tab on the right.

##### Filtering by trigger template

In _By trigger template_ mode, results can be filtered by one or several of the parameters listed below.

_Template group_ | Filter hosts by triggers that are inherited from templates belonging to the selected template group.  
Specifying a parent template group implicitly selects all nested template groups.  
---|---  
_Template_ | Filter hosts by triggers that are inherited from the selected template, including nested templates.  
If a nested template has its own triggers, those triggers will not be displayed.  
_Template trigger_ | Filter hosts by the selected trigger. Other triggers of the filtered hosts will not be displayed.  
_Host group_ | Filter hosts belonging to the selected host group.  
  
##### Filtering by host

In _By host_ mode, results can be filtered by host or host group. Specifying a parent host group implicitly selects all nested host groups.

#### Time period selector

The [time period selector](/documentation/current/en/manual/web_interface/time_period_selector) allows to select commonly used time periods with one click. The selector can be expanded and collapsed by clicking the _Time period_ tab next to the filter.

Clicking _Show_ in the _Graph_ column displays availability information in a bar graph where each bar represents a passed week of the current year.

![](/documentation/current/assets/en/manual/web_interface/availability_bar.png)

The green of a bar stands for OK time and red - for problem time.

#### Effect of maintenance periods

[Maintenance](/documentation/current/en/manual/maintenance) does not automatically exclude time from the availability report. Only maintenance [configured](/documentation/current/en/manual/maintenance#configuration) as _No data collection_ stops polling (so no problems are generated) and therefore leaves the availability percentage unchanged for affected triggers.