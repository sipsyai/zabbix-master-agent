---
title: Configuring a template
source: https://www.zabbix.com/documentation/current/en/manual/config/templates/template
downloaded: 2025-11-14 10:35:58
---

# 1 Configuring a template

#### Overview

Configuring a template requires that you first create a template by defining its general parameters and then you add entities (items, triggers, graphs, etc.) to it.

#### Creating a template

To create a template, do the following:

  1. Go to _Data collection_ → _Templates_.
  2. Click on _Create template_.
  3. Edit template attributes.

The **Template** tab contains general template attributes.

![](/documentation/current/assets/en/manual/config/template_a.png)

All mandatory input fields are marked with a red asterisk.

Template attributes:

_Template name_ | Unique template name.  
Alphanumerics, spaces, dots, dashes, and underscores are allowed.  
Leading and trailing spaces are not allowed.  
---|---  
_Visible name_ | If you set this name, it will be the one visible in lists, maps, etc.  
_Templates_ | Link one or more templates to this template. All entities (items, triggers, etc.) will be inherited from the linked templates.  
To link a new template, type its name in the _Templates_ field—this will display a drop-down list of matching templates. Alternatively, click _Select_ to open the _Templates_ pop-up, which initially shows no templates. To populate the list, either type a template group name in the _Template group_ field (and select one from the suggested list) or press the _Select_ button next to the _Template group_ field to open a _Template groups_ pop-up. Once you choose a template group, the _Templates_ pop-up is updated to show the templates belonging to that group. The selected templates will be linked when the configuration is saved or updated.  
To unlink a template, use one of the two options in the _Templates_ block:  
_Unlink_ \- unlink the template, but preserve its entities (items, triggers, etc.);  
_Unlink and clear_ \- unlink the template and remove all of its entities (items, triggers, etc.).  
_Template groups_ | [Template groups](/documentation/current/en/manual/config/templates/template_groups) the template belongs to.  
_Description_ | Template description.  
_Vendor and version_ | Template vendor and version; displayed only when updating existing templates ([out-of-the-box templates](/documentation/current/en/manual/config/templates_out_of_the_box) provided by Zabbix, [imported templates](/documentation/current/en/manual/xml_export_import/templates#importing), or templates modified through the [Template API](/documentation/current/en/manual/api/reference/template)) if the template configuration contains such information.  
Cannot be modified in Zabbix frontend.  
For out-of-the-box templates, version is displayed as follows: major version of Zabbix, delimiter ("-"), revision number (increased with each new version of the template, and reset with each major version of Zabbix). For example, 7.0-0, 7.0-5, 7.4-0, 7.4-3.  
  
The **Tags** tab allows you to define template-level [tags](/documentation/current/en/manual/config/tagging). All problems of hosts linked to this template will be tagged with the values entered here.

![](/documentation/current/assets/en/manual/config/template_c.png)

User macros, {INVENTORY.*} macros, {HOST.HOST}, {HOST.NAME}, {HOST.CONN}, {HOST.DNS}, {HOST.IP}, {HOST.PORT} and {HOST.ID} macros are supported in tags.

The **Macros** tab allows you to define template-level [user macros](/documentation/current/en/manual/config/macros/user_macros) as a name-value pairs. Note that macro values can be kept as plain text, secret text, or Vault secret. Adding a description is also supported.

![](/documentation/current/assets/en/manual/config/template_d1.png)

If you select the _Inherited and template macros_ option, you may also view macros from linked templates and global macros that the template will inherit, as well as the values that the macros will resolve to.

![](/documentation/current/assets/en/manual/config/template_d2.png)

For convenience, links to the respective templates, as well as a link to global macro configuration is provided. It is also possible to edit a linked template macro or global macro on the template level, effectively creating a copy of the macro on the template.

The **Value mapping** tab allows to configure human-friendly representation of item data in [value mappings](/documentation/current/en/manual/config/items/mapping).

Buttons:

![](/documentation/current/assets/en/manual/config/button_add.png) | Add the template. The added template should appear in the list.  
---|---  
![](/documentation/current/assets/en/manual/config/button_update.png) | Update the properties of an existing template.  
![](/documentation/current/assets/en/manual/config/button_clone.png) | Create another template based on the properties of the current template. This **includes** the entities (items, triggers, etc.) both inherited from linked templates and directly attached to the current template, but **excludes** the current template's vendor and version for the cloned template to be distinguishable from the original.  
![](/documentation/current/assets/en/manual/config/button_delete.png) | Delete the template; entities of the template (items, triggers, etc.) remain with the linked hosts.  
![](/documentation/current/assets/en/manual/config/button_clear.png) | Delete the template and all its entities from linked hosts.  
![](/documentation/current/assets/en/manual/config/button_cancel.png) | Cancel the editing of template properties.  
  
#### Adding items, triggers, graphs

Items have to be added to a template first. Triggers and graphs cannot be added without the corresponding item.

There are two ways to add items to the template:  

  1. To create new items, follow the guidelines for [Creating an item](/documentation/current/en/manual/config/items/item).  

  2. To add existing items to the template:

  * Go to _Data collection → Hosts_ (or _Templates_).
  * Click on _Items_ in the row of the required host/template.
  * Mark the checkboxes of items you want to add to the template.
  * Click on _Copy_ below the item list.
  * Select the template (or group of templates) the items should be copied to and click on _Copy_.  
All the selected items should be copied to the template.

Adding triggers and graphs is done in a similar fashion (from the list of triggers and graphs respectively), again, keeping in mind that they can only be added if the required items are added first.

#### Adding dashboards

To add dashboards to a template in _Data collection_ → _Templates_ , do the following:

  1. Click on _Dashboards_ in the row of the template.
  2. Configure a dashboard following the guidelines of [configuring dashboards](/documentation/current/en/manual/web_interface/frontend_sections/dashboards).

When configuring widgets on a template dashboard (instead of a global dashboard), the host-related parameters are not available, and some parameters have a different label. This is because template dashboards display data only from the host that the template is linked to. For example, the parameters _Host groups_ , _Exclude host groups_ and _Hosts_ in the [_Problems_](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/problems) widget are not available, the parameter _Host groups_ in the [_Host availability_](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/host_availability) widget is not available, and the parameter _Show hosts in maintenance_ is renamed to _Show data in maintenance_ , etc. For more information on the availability of parameters in template dashboard widgets, see specific parameters for each [dashboard widget](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets).

For details on accessing host dashboards that are created from template dashboards, see the [host dashboards](/documentation/current/en/manual/web_interface/frontend_sections/monitoring/hosts/dashboards#access) section.

#### Configuring low-level discovery rules

See the [low-level discovery](/documentation/current/en/manual/discovery/low_level_discovery) section of the manual.

#### Adding web scenarios

To add web scenarios to a template in _Data collection_ → _Templates_ , do the following:

  1. Click on _Web_ in the row of the template.
  2. Configure a web scenario following the usual method of [configuring web scenarios](/documentation/current/en/manual/web_monitoring#configuring-a-web-scenario).