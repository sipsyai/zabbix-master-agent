---
title: Linking/unlinking
source: https://www.zabbix.com/documentation/current/en/manual/config/templates/linking
downloaded: 2025-11-14 10:36:00
---

# 3 Linking/unlinking

### Overview

Linking is a process whereby templates are applied to hosts, whereas unlinking removes the association with the template from a host.

### Linking a template

To link a template to the host, do the following:

  1. Go to _Data collection → Hosts_.
  2. Click on the required host.
  3. Start typing the template name in the _Templates_ field. A list of matching templates will appear; scroll down to select. Alternatively, you may click on _Select_ next to the field and select one or several templates from the list in a popup window.
  4. Click on _Add/Update_ in the host attributes form.

The host will now have all the entities of the template. This includes items, triggers, graphs, low-level discovery rules, web scenarios, as well as dashboards.

Linking multiple templates to the same host will fail if those templates contain items with the same item key. And, as triggers and graphs use items, they cannot be linked to a single host from multiple templates either, if using identical item keys.

When entities (items, triggers, etc.) are added from the template:

  * previously existing identical entities on the host are updated as entities of the template, and **any existing host-level customizations to the entity are lost** ;
  * entities from the template are added;
  * any directly linked entities that, prior to template linkage, existed only on the host remain untouched.

In the lists, all entities from the template now are prefixed by the template name, indicating that these belong to the particular template. The template name itself (in gray text) is a link allowing to access the list of those entities on the template level.

For some items, such as [external checks](/documentation/current/en/manual/config/items/itemtypes/external), [HTTP agent checks](/documentation/current/en/manual/config/items/itemtypes/http), [simple checks](/documentation/current/en/manual/config/items/itemtypes/simple_checks), [SSH checks](/documentation/current/en/manual/config/items/itemtypes/ssh_checks) and [Telnet checks](/documentation/current/en/manual/config/items/itemtypes/telnet_checks), a host interface is optional. If, at the time of linking a template, the host does not have an interface defined these items will be added without an interface. If you add a host interface later it will not be assigned automatically to already existing items. To assign the newly added host interface to all template items at once, unlink the template from the host and then link it back again. To preserve item history use the option _Unlink_ , do not use _Unlink and clear_.

If some entity is not prefixed by the template name, it means that it existed on the host before and was not added by the template.

##### Entity uniqueness criteria

When adding entities (items, triggers, etc.) from a template it is important to know what of those entities already exist on the host and need to be updated and what entities differ. The uniqueness criteria for deciding upon the sameness/difference are:

  * for items - the item key;
  * for triggers - trigger name and expression;
  * for custom graphs - graph name and its items.

##### Linking templates to several hosts

To update template linkage of many hosts, in _Data collection → Hosts_ select some hosts by marking their checkboxes, then click on **[Mass update](/documentation/current/en/manual/config/hosts/hostupdate)** below the list and then select _Link templates_ :

![](/documentation/current/assets/en/manual/config/mass_link.png)

To link additional templates, start typing the template name in the auto-complete field until a dropdown appears offering the matching templates. Just scroll down to select the template to link.

The _Replace_ option will allow to link a new template while unlinking any template that was linked to the hosts before. The _Unlink_ option will allow to specify which templates to unlink. The _Clear when unlinking_ option will allow to not only unlink any previously linked templates, but also remove all entities inherited from them (items, triggers, etc.).

Zabbix offers a sizable set of predefined templates. You can use these for reference, but beware of using them unchanged in production as they may contain too many items and poll for data too often. If you feel like using them, finetune them to fit you real needs.

##### Editing linked entities

If you try to edit an item or a trigger that was linked from the template, you may realize that many key options are disabled for editing. This makes sense as the idea of templates is that things are edited in a one-touch manner on the template level. However, you still can, for example, enable/disable an item on individual hosts and set the update interval, history length and some other parameters.

If you want to edit the entity fully, you have to edit it on the template level (template level shortcut is displayed in the form name), keeping in mind that these changes will affect all hosts that have this template linked to them.

Any customizations to the entities implemented on a template-level will override the previous customizations of the entities on a host-level.

#### Unlinking a template

To unlink a template from a host, do the following:

  1. Go to _Data collection → Hosts_.
  2. Click on the required host and find the _Templates_ field.
  3. Click on _Unlink_ or _Unlink and clear_ next to the template to unlink the template.
  4. Click on _Update_ in the host attributes form.

Choosing the _Unlink_ option will simply remove association with the template, while leaving all its entities with the host. This includes items, triggers, graphs, low-level discovery rules, and web scenarios, but excludes dashboards. Note that value maps and tags inherited from linked templates will also be removed.

Choosing the _Unlink and clear_ option will remove both the association with the template and all its entities (items, triggers, etc.).