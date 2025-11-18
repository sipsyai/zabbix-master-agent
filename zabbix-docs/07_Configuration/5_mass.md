---
title: Mass update
source: https://www.zabbix.com/documentation/current/en/manual/config/templates/mass
downloaded: 2025-11-14 10:36:01
---

# 5 Mass update

#### Overview

Sometimes you may want to change some attribute for a number of templates at once. Instead of opening each individual template for editing, you may use the mass update function for that.

#### Using mass update

To mass-update some templates, do the following:

  1. Mark the checkboxes before the templates you want to update in the [template list](/documentation/current/en/manual/web_interface/frontend_sections/data_collection/templates).
  2. Click on _Mass update_ below the list.
  3. Navigate to the tab with required attributes (_Template_ , _Tags_ , _Macros_ or _Value mapping_).
  4. Mark the checkboxes of any attribute to update and enter a new value for them.

The **Template** tab contains general template mass update options.

![](/documentation/current/assets/en/manual/config/templates/templ_mass.png)

The following options are available when selecting the respective button for the _Link templates_ update:

  * _Link_ \- specify which additional templates to link;
  * _Replace_ \- specify which templates to link while at the same time unlinking any previously linked templates;
  * _Unlink_ \- specify which templates to unlink.

To specify the templates to link/unlink, start typing the template name in the auto-complete field until a dropdown appears offering the matching templates. Just scroll down to select the required templates.

The _Clear when unlinking_ option will allow to unlink any previously linked templates, as well as to remove all elements inherited from them (items, triggers, graphs, etc.).

The following options are available when selecting the respective button for the _Template groups_ update:

  * _Add_ \- allows to specify additional template groups from the existing ones or enter completely new template groups for the templates;
  * _Replace_ \- will remove the template from any existing template groups and replace them with the one(s) specified in this field (existing or new template groups);
  * _Remove_ \- will remove specific template groups from templates.

These fields are auto-complete - starting to type in them offers a dropdown of matching template groups. If the template group is new, it also appears in the dropdown and it is indicated by _(new)_ after the string. Just scroll down to select.

The **Tags** tab allows you to mass update template-level tags.

![](/documentation/current/assets/en/manual/config/templates/templ_mass_c.png)

User macros, {INVENTORY.*} macros, {HOST.HOST}, {HOST.NAME}, {HOST.CONN}, {HOST.DNS}, {HOST.IP}, {HOST.PORT} and {HOST.ID} macros are supported in tags. Note that tags with the same name, but different values are not considered 'duplicates' and can be added to the same template.

The **Macros** tab allows you to mass update template-level macros.

![](/documentation/current/assets/en/manual/config/templates/templ_mass_d.png)

The following options are available when selecting the respective button for macros update:

  * _Add_ \- allows to specify additional user macros for the templates. If _Update existing_ checkbox is checked, value, type and description for the specified macro name will be updated. If unchecked, if a macro with that name already exist on the template(s), it will not be updated.
  * _Update_ \- will replace values, types and descriptions of macros specified in this list. If _Add missing_ checkbox is checked, macro that didn't previously exist on a template will be added as new macro. If unchecked, only macros that already exist on a template will be updated.
  * _Remove_ \- will remove specified macros from templates. If _Except selected_ box is checked, all macros except specified in the list will be removed. If unchecked, only macros specified in the list will be removed.
  * _Remove all_ \- will remove all user macros from templates. If _I confirm to remove all macros_ checkbox is not checked, a new popup window will open asking to confirm removal of all macros.

The **Value mapping** tab allows you to mass update [value mappings](/documentation/current/en/manual/config/items/mapping).

![](/documentation/current/assets/en/manual/config/templates/templ_mass_e.png)

Buttons with the following options are available for value map update:

  * _Add_ \- add value maps to the templates. If you mark _Update existing_ , all properties of the value map with this name will be updated. Otherwise, if a value map with that name already exists, it will not be updated.
  * _Update_ \- update existing value maps. If you mark _Add missing_ , a value map that didn't previously exist on a template will be added as a new value map. Otherwise only the value maps that already exist on a template will be updated.
  * _Rename_ \- give new name to an existing value map.
  * _Remove_ \- remove the specified value maps from the templates. If you mark _Except selected_ , all value maps will be removed **except** the ones that are specified.
  * _Remove all_ \- remove all value maps from the templates. If the _I confirm to remove all value maps_ checkbox is not marked, a new popup window will open asking to confirm the removal.

_Add from template_ and _Add from host_ options are available for value mapping add/update operations. They allow to select value mappings from a template or a host respectively.

When done with all required changes, click on _Update_. The attributes will be updated accordingly for all the selected templates.