---
title: Item prototypes
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/data_collection/templates/discovery/item_prototypes
downloaded: 2025-11-14 10:39:02
---

# 1 Item prototypes  
  
#### Overview

In this section the configured item prototypes of a low-level discovery rule on the template are displayed.

If the template is linked to the host, item prototypes will become the basis of creating real host [items](/documentation/current/en/manual/web_interface/frontend_sections/data_collection/hosts/items) during low-level discovery.

![](/documentation/current/assets/en/manual/web_interface/template_item_prototypes.png)

Displayed data:

_Name_ | Name of the item prototype, displayed as a blue link.  
Clicking on the name opens the item prototype [configuration form](/documentation/current/en/manual/discovery/low_level_discovery/item_prototypes).  
If the item prototype belongs to a linked template, the template name is displayed before the item prototype name as a gray link. Clicking on the template link opens the item prototype list on the linked template level.  
If the item prototype is of the "Dependent item" type, the master item name is displayed before the item prototype name in green (as in the case of item prototypes on the [host level](/documentation/current/en/manual/web_interface/frontend_sections/data_collection/hosts/discovery/item_prototypes)).  
---|---  
_Key_ | Key of the item prototype is displayed.  
_Interval_ | Frequency of the check is displayed.  
_History_ | How many days to keep item data history is displayed.  
_Trends_ | How many days to keep item trends history is displayed.  
_Type_ | Type of the item prototype is displayed (Zabbix agent, SNMP agent, simple check, etc).  
_Create enabled_ | Create the item based on this prototype as:  
**Yes** \- enabled  
**No** \- disabled. You can switch between 'Yes' and 'No' by clicking on them.  
_Discover_ | Discover the item based on this prototype:  
**Yes** \- discover  
**No** \- do not discover. You can switch between 'Yes' and 'No' by clicking on them.  
_Tags_ | Tags of the item prototype is displayed.  
  
To configure a new item prototype, click on the _Create item prototype_ button at the upper-right corner.

##### Mass editing options

Buttons below the list offer some mass-editing options:

  * _Create enabled_ \- create these items as _Enabled_
  * _Create disabled_ \- create these items as _Disabled_
  * _Mass update_ \- mass update these item prototypes
  * _Delete_ \- delete these item prototypes

To use these options, mark the checkboxes before the respective item prototypes, then click on the required button.