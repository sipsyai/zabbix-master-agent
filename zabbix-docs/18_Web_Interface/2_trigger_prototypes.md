---
title: Trigger prototypes
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/data_collection/templates/discovery/trigger_prototypes
downloaded: 2025-11-14 10:39:03
---

# 2 Trigger prototypes

#### Overview

In this section the configured trigger prototypes of a low-level discovery rule on the template are displayed.

If the template is linked to the host, trigger prototypes will become the basis of creating real host [triggers](/documentation/current/en/manual/web_interface/frontend_sections/data_collection/hosts/triggers) during low-level discovery.

![](/documentation/current/assets/en/manual/web_interface/template_trigger_prototypes.png)

Displayed data:

_Severity_ | Severity of the trigger is displayed by both name and cell background color.  
---|---  
_Name_ | Name of the trigger prototype, displayed as a blue link.  
Clicking on the name opens the trigger prototype [configuration form](/documentation/current/en/manual/discovery/low_level_discovery/trigger_prototypes).  
If the trigger prototype belongs to a linked template, the template name is displayed before the trigger name as a gray link. Clicking on the template link opens the trigger prototype list on the linked template level.  
_Expression_ | Trigger expression is displayed. The template-item part of the expression is displayed as a link, leading to the item configuration form.  
_Operational data_ | Format of the operational data of the trigger is displayed, containing arbitrary strings and macros that will resolve dynamically in _Monitoring_ → _Problems_.  
_Create enabled_ | Create the trigger based on this prototype as:  
**Yes** \- enabled  
**No** \- disabled. You can switch between 'Yes' and 'No' by clicking on them.  
_Discover_ | Discover the trigger based on this prototype:  
**Yes** \- discover  
**No** \- do not discover. You can switch between 'Yes' and 'No' by clicking on them.  
_Tags_ | Tags of the trigger prototype are displayed.  
  
To configure a new trigger prototype, click on the _Create trigger prototype_ button at the upper-right corner.

##### Mass editing options

Buttons below the list offer some mass-editing options:

  * _Create enabled_ \- create these triggers as _Enabled_
  * _Create disabled_ \- create these triggers as _Disabled_
  * _Mass update_ \- mass update these trigger prototypes
  * _Delete_ \- delete these trigger prototypes

To use these options, mark the checkboxes before the respective trigger prototypes, then click on the required button.