---
title: Templates
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/data_collection/templates
downloaded: 2025-11-14 10:38:57
---

# 3 Templates

#### Overview

In the _Data collection_ → _Templates_ section users can configure and maintain templates.

A listing of existing templates with their details is displayed.

![](/documentation/current/assets/en/manual/web_interface/templates.png)

Displayed data:

_Name_ | Name of the template.  
Clicking on the template name opens the template [configuration form](/documentation/current/en/manual/config/templates/template#creating-a-template).  
---|---  
_Hosts_ | Number of editable hosts to which the template is linked; read-only hosts are not included.  
Clicking on _Hosts_ will open the host list with only those hosts filtered that are linked to the template.  
_Entities (Items, Triggers, Graphs, Dashboards, Discovery, Web)_ | Number of the respective entities in the template (displayed in gray).  
Clicking on the entity name will, in the whole listing of that entity, filter out those that belong to the template.  
_Linked templates_ | Templates that are [linked](/documentation/current/en/manual/config/templates/nesting) to the template.  
_Linked to templates_ | Templates that the template is [linked](/documentation/current/en/manual/config/templates/nesting) to.  
_Vendor_ , _Version_ | Template vendor and version; displayed if the template configuration contains such information, and only for [out-of-the-box templates](/documentation/current/en/manual/config/templates_out_of_the_box), [imported templates](/documentation/current/en/manual/xml_export_import/templates#importing), or templates modified through the [Template API](/documentation/current/en/manual/api/reference/template).  
For out-of-the-box templates, version is displayed as follows: major version of Zabbix, delimiter ("-"), revision number (increased with each new version of the template, and reset with each major version of Zabbix). For example, 7.0-0, 7.0-3, 7.4-0, 7.4-3.  
_Tags_ | [Tags](/documentation/current/en/manual/config/tagging) of the template, with macros unresolved.  
  
To [configure a new template](/documentation/current/en/manual/config/templates/template), click on the _Create template_ button in the upper-right corner.

To [import a template](/documentation/current/en/manual/xml_export_import/templates#importing) from a YAML, XML, or JSON file, click on the _Import_ button in the upper-right corner.

##### Using filter

You can use the filter to display only the templates you are interested in. For better search performance, data is searched with macros unresolved.

The _Filter_ link is available below _Create template_ and _Import_ buttons. If you click on it, a filter becomes available where you can filter templates by template group, linked templates, name and tags.

![](/documentation/current/assets/en/manual/web_interface/template_filter.png)

_Template groups_ | Filter by one or more template groups.  
Specifying a parent template group implicitly selects all nested groups.  
---|---  
_Linked templates_ | Filter by directly linked templates.  
_Name_ | Filter by template name.  
_Vendor_ | Filter by template vendor.  
_Version_ | Filter by template version.  
_Tags_ | Filter by template tag name and value.  
Filtering is possible only by template-level tags (not inherited ones). It is possible to include as well as exclude specific tags and tag values. Several conditions can be set. Tag name matching is always case-sensitive.  
  
There are several operators available for each condition:  
**Exists** \- include the specified tag names;  
**Equals** \- include the specified tag names and values (case-sensitive);  
**Contains** \- include the specified tag names where the tag values contain the entered string (substring match, case-insensitive);  
**Does not exist** \- exclude the specified tag names;  
**Does not equal** \- exclude the specified tag names and values (case-sensitive);  
**Does not contain** \- exclude the specified tag names where the tag values contain the entered string (substring match, case-insensitive).  
  
There are two calculation types for conditions:  
**And/Or** \- all conditions must be met, conditions having the same tag name will be grouped by the Or condition;  
**Or** \- enough if one condition is met.  
  
##### Mass editing options

Buttons below the list offer some mass-editing options:

  * _Export_ \- export the template to a YAML, XML or JSON file;
  * _Mass update_ \- [update several properties](/documentation/current/en/manual/config/templates/mass) for a number of templates at once;
  * _Delete_ \- delete the template while leaving its linked entities (items, triggers etc.) with the hosts;
  * _Delete and clear_ \- delete the template and its linked entities from the hosts.

To use these options, mark the checkboxes before the respective templates, then click on the required button.