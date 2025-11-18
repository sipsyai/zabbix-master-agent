---
title: Discovery prototypes
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/data_collection/templates/discovery/discovery_prototypes
downloaded: 2025-11-14 10:39:06
---

# 5 Discovery prototypes

#### Overview

In this section the configured discovery prototypes of a low-level discovery rule on the template are displayed.

If the template is linked to the host, discovery prototypes will become the basis of creating real [discovery prototypes](/documentation/current/en/manual/discovery/low_level_discovery/discovery_prototypes) of the parent discovery rule.

![](/documentation/current/assets/en/manual/web_interface/template_discovery_prototypes.png)

Displayed data:

_Name_ | Name of the discovery prototype, displayed as a blue link.  
Clicking on the name opens the discovery prototype configuration form.  
If the discovery prototype belongs to a linked template, the template name is displayed before the discovery prototype name as a gray link. Clicking on the template link opens the discovery prototype list on the linked template level.  
---|---  
_Items_ | A link to the list of item prototypes is displayed.  
The number of existing item prototypes is displayed in gray.  
_Triggers_ | A link to the list of trigger prototypes is displayed.  
The number of existing trigger prototypes is displayed in gray.  
_Graphs_ | A link to the list of graph prototypes displayed.  
The number of existing graph prototypes is displayed in gray.  
_Hosts_ | A link to the list of host prototypes displayed.  
The number of existing host prototypes is displayed in gray.  
_Discovery rules_ | A link to the list of discovery prototypes displayed.  
The number of existing discovery prototypes is displayed in gray.  
_Key_ | The item key used for discovery is displayed.  
_Interval_ | The frequency of performing discovery is displayed.  
_Type_ | The item type used for discovery is displayed (Zabbix agent, SNMP agent, etc).  
_Create enabled_ | Discovery prototype creation status is displayed - create enabled (_Yes_) or create disabled (_No_). By clicking on the status you can change it - from Yes to No (and back).  
_Discover_ | Discovery prototype discovery status is displayed - discover (_Yes_) or do not discover (_No_). By clicking on the status you can change it - from Yes to No (and back).  
  
To configure a new discovery prototype, click on the _Create discovery prototype_ button at the upper-right corner.

##### Mass editing options

Buttons below the list offer some mass-editing options:

  * _Create enabled_ \- create these discovery prototypes as _Enabled_
  * _Create disabled_ \- create these discovery prototypes as _Disabled_
  * _Delete_ \- delete these discovery prototypes

To use these options, mark the checkboxes before the respective discovery prototypes, then click on the required button.