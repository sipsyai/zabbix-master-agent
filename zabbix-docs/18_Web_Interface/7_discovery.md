---
title: Discovery
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/data_collection/discovery
downloaded: 2025-11-14 10:39:11
---

# 7 Discovery

#### Overview

In the _Data collection → Discovery_ section users can configure and maintain discovery rules.

A listing of existing discovery rules with their details is displayed.

![](/documentation/current/assets/en/manual/web_interface/discovery_rules0.png)

Displayed data:

_Name_ | Name of the discovery rule. Clicking on the discovery rule name opens the discovery rule [configuration form](/documentation/current/en/manual/discovery/network_discovery/rule).  
---|---  
_IP range_ | The range of IP addresses to use for network scanning is displayed.  
_Proxy_ | The proxy name is displayed, if discovery is performed by the proxy.  
_Interval_ | The frequency of performing discovery displayed.  
_Checks_ | The types of checks used for discovery are displayed.  
_Status_ | The discovery rule status is displayed - _Enabled_ or _Disabled_.  
By clicking on the status you can change it.  
_Info_ | If everything is working correctly, nothing is displayed in this column. In case of errors, a red info icon with the letter "i" is displayed. Hover over the icon to see a tooltip with the error description.  
  
To configure a new discovery rule, click on the _Create discovery rule_ button in the upper-right corner.

##### Mass editing options

Buttons below the list offer some mass-editing options:

  * _Enable_ \- change the discovery rule status to _Enabled_
  * _Disable_ \- change the discovery rule status to _Disabled_
  * _Delete_ \- delete the discovery rules

To use these options, mark the checkboxes before the respective discovery rules, then click on the required button.

##### Using filter

You can use the filter to display only the discovery rules you are interested in. For better search performance, data is searched with macros unresolved.

The _Filter_ link is available above the list of discovery rules. If you click on it, a filter becomes available where you can filter discovery rules by name and status.

![](/documentation/current/assets/en/manual/web_interface/discovery_rules_filter1.png)