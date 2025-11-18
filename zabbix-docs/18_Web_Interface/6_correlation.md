---
title: Event correlation
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/data_collection/correlation
downloaded: 2025-11-14 10:39:10
---

# 6 Event correlation

#### Overview

In the _Data collection → Event correlation_ section users can configure and maintain [global correlation](/documentation/current/en/manual/config/event_correlation/global) rules for Zabbix events.

![](/documentation/current/assets/en/manual/web_interface/correlation_rules.png)

Displayed data:

_Name_ | Name of the correlation rule. Clicking on the correlation rule name opens the rule [configuration form](/documentation/current/en/manual/config/event_correlation/global#configuration).  
---|---  
_Conditions_ | Correlation rule conditions are displayed.  
_Operations_ | Correlation rule operations are displayed.  
_Status_ | Correlation rule status is displayed - _Enabled_ or _Disabled_.  
By clicking on the status you can change it.  
  
To configure a new correlation rule, click on the _Create event correlation_ button in the upper-right corner.

##### Mass editing options

Buttons below the list offer some mass-editing options:

  * _Enable_ \- change the correlation rule status to _Enabled_
  * _Disable_ \- change the correlation rule status to _Disabled_
  * _Delete_ \- delete the correlation rules

To use these options, mark the checkboxes before the respective correlation rules, then click on the required button.

##### Using filter

You can use the filter to display only the correlation rules you are interested in. For better search performance, data is searched with macros unresolved.

The _Filter_ link is available above the list of correlation rules. If you click on it, a filter becomes available where you can filter correlation rules by name and status.

![](/documentation/current/assets/en/manual/web_interface/correlation_rules_filter1.png)