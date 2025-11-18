---
title: Discovery rules
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/data_collection/templates/discovery
downloaded: 2025-11-14 10:39:01
---

# 4 Discovery rules

#### Overview

The list of low-level discovery rules for a template can be accessed from _Data collection_ → _Templates_ by clicking on _Discovery_ for the respective template.

A list of existing low-level discovery rules is displayed. It is also possible to see all discovery rules independently of the template, or all discovery rules of a specific template group by changing the filter settings.

![](/documentation/current/assets/en/manual/web_interface/template_lld_rules.png)

Displayed data:

_Template_ | The template discovery rule belongs to.  
Clicking on the template name opens the template [configuration form](/documentation/current/en/manual/config/templates/template#creating-a-template).  
---|---  
_Name_ | Name of the rule, displayed as a blue link.  
Clicking on the rule name opens the low-level discovery rule [configuration form](/documentation/current/en/manual/discovery/low_level_discovery#discovery-rule).  
If the discovery rule is inherited from another template, the template name is displayed before the rule name as a gray link. Clicking on the template link opens the discovery rule list on that template level.  
_Items_ | A link to the list of item prototypes is displayed.  
The number of existing item prototypes is displayed in gray.  
_Triggers_ | A link to the list of trigger prototypes is displayed.  
The number of existing trigger prototypes is displayed in gray.  
_Graphs_ | A link to the list of graph prototypes displayed.  
The number of existing graph prototypes is displayed in gray.  
_Hosts_ | A link to the list of host prototypes displayed.  
The number of existing host prototypes is displayed in gray.  
_Key_ | The item key used for discovery is displayed.  
_Interval_ | The frequency of performing discovery is displayed.  
_Type_ | The item type used for discovery is displayed (Zabbix agent, SNMP agent, etc).  
_Status_ | Discovery rule status is displayed - _Enabled_ or _Disabled_. By clicking on the status you can change it - from Enabled to Disabled (and back).  
  
To configure a new low-level discovery rule, click on the _Create discovery rule_ button at the upper-right corner.

##### Mass editing options

Buttons below the list offer some mass-editing options:

  * _Enable_ \- change the low-level discovery rule status to _Enabled_
  * _Disable_ \- change the low-level discovery rule status to _Disabled_
  * _Delete_ \- delete the low-level discovery rules

To use these options, mark the checkboxes before the respective discovery rules, then click on the required button.

##### Using filter

You can use the filter to display only the discovery rules you are interested in. For better search performance, data is searched with macros unresolved.

The _Filter_ icon is available at the upper-right corner. Clicking on it will open a filter where you can specify the desired filtering criteria such as template, discovery rule name, item key, item type, etc.

![](/documentation/current/assets/en/manual/web_interface/template_drule_filter.png)

_Template groups_ | Filter by one or more template groups.  
Specifying a parent template group implicitly selects all nested groups.  
---|---  
_Templates_ | Filter by one or more templates.  
_Name_ | Filter by discovery rule name.  
_Key_ | Filter by discovery item key.  
_Type_ | Filter by discovery item type.  
_Update interval_ | Filter by update interval.  
Not available for Zabbix trapper and dependent items.  
_Delete lost resources_ | Filter by _Delete lost resources_ period.  
_Disable lost resources_ | Filter by _Disable lost resources_ period.  
_Status_ | Filter by discovery rule status (All/Enabled/Disabled).