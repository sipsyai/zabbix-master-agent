---
title: Triggers
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/data_collection/templates/triggers
downloaded: 2025-11-14 10:38:59
---

# 2 Triggers

#### Overview

The trigger list for a template can be accessed from _Data collection → Templates_ by clicking on _Triggers_ for the respective template.

![](/documentation/current/assets/en/manual/web_interface/template_triggers.png)

Displayed data:

_Severity_ | Severity of the trigger is displayed by both name and cell background color.  
---|---  
_Template_ | Template the trigger belongs to.  
Clicking on the template name opens the template [configuration form](/documentation/current/en/manual/config/templates/template#creating-a-template).  
This column is displayed only if multiple templates or no templates are selected in the filter.  
_Name_ | Name of the trigger displayed as a blue link to trigger details.  
Clicking on the trigger name link opens the trigger [configuration form](/documentation/current/en/manual/config/triggers/trigger#configuration).  
If the trigger is inherited from another template, the template name is displayed before the trigger name as a gray link. Clicking on the template link opens the trigger list on that template level.  
_Operational data_ | Operational data definition of the trigger, containing arbitrary strings and macros that will resolve dynamically in _Monitoring_ → _Problems_.  
_Expression_ | Trigger expression is displayed. The template-item part of the expression is displayed as a link, leading to the item configuration form.  
_Status_ | Trigger status is displayed - _Enabled_ or _Disabled_. By clicking on the status you can change it - from Enabled to Disabled (and back).  
_Tags_ | If a trigger contains tags, tag name and value are displayed in this column.  
  
To configure a new trigger, click on the _Create trigger_ button at the upper-right corner.

##### Mass editing options

Buttons below the list offer some mass-editing options:

  * _Enable_ \- change trigger status to _Enabled_
  * _Disable_ \- change trigger status to _Disabled_
  * _Copy_ \- copy the triggers to other hosts or templates
  * _Mass update_ \- update several properties for a number of triggers at once
  * _Delete_ \- delete the triggers

To use these options, mark the checkboxes before the respective triggers, then click on the required button.

##### Using filter

You can use the filter to display only the triggers you are interested in. For better search performance, data is searched with macros unresolved.

The _Filter_ icon is available at the upper-right corner. Clicking on it will open a filter where you can specify the desired filtering criteria.

![](/documentation/current/assets/en/manual/web_interface/template_trigger_filter.png)

_Template groups_ | Filter by one or more template groups.  
Specifying a parent template group implicitly selects all nested groups.  
---|---  
_Templates_ | Filter by one or more templates.  
If template groups are already selected above, template selection is limited to those groups.  
_Name_ | Filter by trigger name.  
_Severity_ | Select to filter by one or several trigger severities.  
_Status_ | Filter by trigger status.  
_Tags_ | Filter by trigger tag name and value. It is possible to include as well as exclude specific tags and tag values. Several conditions can be set. Tag name matching is always case-sensitive.  
There are several operators available for each condition:  
**Exists** \- include the specified tag names  
**Equals** \- include the specified tag names and values (case-sensitive)  
**Contains** \- include the specified tag names where the tag values contain the entered string (substring match, case-insensitive)  
**Does not exist** \- exclude the specified tag names  
**Does not equal** \- exclude the specified tag names and values (case-sensitive)  
**Does not contain** \- exclude the specified tag names where the tag values contain the entered string (substring match, case-insensitive)  
There are two calculation types for conditions:  
**And/Or** \- all conditions must be met, conditions having the same tag name will be grouped by the Or condition  
**Or** \- enough if one condition is met  
Macros and [macro functions](/documentation/current/en/manual/config/macros/macro_functions) are supported in tag name and tag value fields.  
_Inherited_ | Filter triggers inherited (or not inherited) from linked templates.  
_With dependencies_ | Filter triggers with (or without) dependencies.