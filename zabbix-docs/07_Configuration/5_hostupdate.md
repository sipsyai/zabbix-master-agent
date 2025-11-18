---
title: Mass update
source: https://www.zabbix.com/documentation/current/en/manual/config/hosts/hostupdate
downloaded: 2025-11-14 10:34:39
---

# 5 Mass update

#### Overview

Sometimes you may want to change some attribute for a number of hosts at once. Instead of opening each individual host for editing, you may use the mass update function for that.

#### Using mass update

To mass-update some hosts, do the following:

  * Mark the checkboxes before the hosts you want to update in the [host list](/documentation/current/en/manual/web_interface/frontend_sections/data_collection/hosts)
  * Click on _Mass update_ below the list
  * Navigate to the tab with required attributes (_Host_ , _IPMI_ , _Tags_ , _Macros_ , _Inventory_ , _Encryption_ or _Value mapping_)
  * Mark the checkboxes of any attribute to update and enter a new value for them

![](/documentation/current/assets/en/manual/config/hosts/host_mass.png)

The following options are available when selecting the respective button for **template** linkage update:

  * _Link_ \- specify which additional templates to link
  * _Replace_ \- specify which templates to link while unlinking any template that was linked to the hosts before
  * _Unlink_ \- specify which templates to unlink

To specify the templates to link/unlink start typing the template name in the auto-complete field until a dropdown appears offering the matching templates. Just scroll down to select the required template.

The _Clear when unlinking_ option will allow to not only unlink any previously linked templates, but also remove all elements inherited from them (items, triggers, etc.).

The following options are available when selecting the respective button for **host group** update:

  * _Add_ \- allows to specify additional host groups from the existing ones or enter completely new host groups for the hosts
  * _Replace_ \- will remove the host from any existing host groups and replace them with the one(s) specified in this field (existing or new host groups)
  * _Remove_ \- will remove specific host groups from hosts

These fields are auto-complete - starting to type in them offers a dropdown of matching host groups. If the host group is new, it also appears in the dropdown and it is indicated by _(new)_ after the string. Just scroll down to select.

![](/documentation/current/assets/en/manual/config/hosts/host_mass_c.png)

![](/documentation/current/assets/en/manual/config/hosts/host_mass_d.png)

User macros, {INVENTORY.*} macros, {HOST.HOST}, {HOST.NAME}, {HOST.CONN}, {HOST.DNS}, {HOST.IP}, {HOST.PORT} and {HOST.ID} macros are supported in tags. Note that tags with the same name but different values are not considered 'duplicates' and can be added to the same host.

![](/documentation/current/assets/en/manual/config/hosts/host_mass_e.png)

The following options are available when selecting the respective button for macros update:

  * _Add_ \- allows to specify additional user macros for the hosts. If _Update existing_ checkbox is checked, value, type and description for the specified macro name will be updated. If unchecked, if a macro with that name already exist on the host(s), it will not be updated.
  * _Update_ \- will replace values, types and descriptions of macros specified in this list. If _Add missing_ checkbox is checked, macro that didn't previously exist on a host will be added as new macro. If unchecked, only macros that already exist on a host will be updated.
  * _Remove_ \- will remove specified macros from hosts. If _Except selected_ box is checked, all macros except specified in the list will be removed. If unchecked, only macros specified in the list will be removed.
  * _Remove all_ \- will remove all user macros from hosts. If _I confirm to remove all macros_ checkbox is not checked, a new popup window will open asking to confirm removal of all macros.

![](/documentation/current/assets/en/manual/config/hosts/host_mass_f.png)

To be able to mass update inventory fields, the _Inventory mode_ should be set to 'Manual' or 'Automatic'.

![](/documentation/current/assets/en/manual/config/hosts/host_mass_g.png)

![](/documentation/current/assets/en/manual/config/hosts/host_mass_h.png)

Buttons with the following options are available for value map update:

  * _Add_ \- add value maps to the hosts. If you mark _Update existing_ , all properties of the value map with this name will be updated. Otherwise, if a value map with that name already exists, it will not be updated.
  * _Update_ \- update existing value maps. If you mark _Add missing_ , a value map that didn't previously exist on a host will be added as a new value map. Otherwise only the value maps that already exist on a host will be updated.
  * _Rename_ \- give new name to an existing value map
  * _Remove_ \- remove the specified value maps from the hosts. If you mark _Except selected_ , all value maps will be removed **except** the ones that are specified.
  * _Remove all_ \- remove all value maps from the hosts. If the _I confirm to remove all value maps_ checkbox is not marked, a new popup window will open asking to confirm the removal.

When done with all required changes, click on _Update_. The attributes will be updated accordingly for all the selected hosts.