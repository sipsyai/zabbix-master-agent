---
title: Configuring a template group
source: https://www.zabbix.com/documentation/current/en/manual/config/templates/template_groups
downloaded: 2025-11-14 10:35:59
---

# 2 Configuring a template group

#### Overview

Template groups are used for the logical grouping of templates and assigning user permissions to them.

Each template must have at least one template group assigned. A template may belong to multiple template groups, and each template group may contain multiple templates.

Note that in Zabbix, all permissions are based on groups: [user groups](/documentation/current/en/manual/config/users_and_usergroups), [host groups](/documentation/current/en/manual/config/hosts/host_groups), and template groups. So, even if a single user needs access to a single template, it is granted by adding the user to a user group that has permission to access the template group containing that template.

#### Configuration

Only Super admin users can create template groups.

There are two options of creating a template group in Zabbix frontend.

**Option one** :

  * Go to: _Data collection → Template groups_
  * Click on _Create template group_ in the upper-right corner of the screen
  * Enter the group name in the form

![](/documentation/current/assets/en/manual/config/template_group.png)

**Option two** : when [configuring a template](/documentation/current/en/manual/config/templates/template#creating-a-template), enter a non-existing group name in the _Template groups_ input field.

Once the template group is created, you can click on the template name in the list under _Data collection_ → _Template groups_ to edit the group name, clone the group, or delete the group.

Deleting a template group only deletes the logical group, not the templates in the group. It is not possible to delete a template group that is the only group for any existing template.

#### Creating template subgroups

A template subgroup (or nested template group) is a child of the parent template group that contains it.

A subgroup is created by using the forward slash '/' in the group name input field to denote its relation to the parent group(s). For example:

  * inputting `Linux servers/Databases` creates the `Linux servers/Databases` subgroup of the parent group `Linux servers`.
  * inputting `Linux servers/Databases/MySQL/Tokyo` creates the respective subgroup within the nested parent groups `Linux servers`, `Linux servers/Databases`, `Linux servers/Databases/MySQL`.

When creating a subgroup, using leading or trailing slashes, or several slashes in a row is not allowed. Escaping of '/' is not supported.

It is not required to create any parent template group(s) before creating a subgroup. You can choose whether to start by creating a subgroup (for example, `Linux servers/Databases`) or any parent template group(s) (in our example, `Linux servers`). If you start by creating a subgroup, parent template group(s) will **not** be created automatically.

##### Permissions to template groups

  * When creating a subgroup to an existing parent template group (for example, creating `Linux servers/Databases` when `Linux servers` already exists), [user group](/documentation/current/en/manual/config/users_and_usergroups/usergroup) permissions to the subgroup are inherited from the parent.
  * When creating a parent template group to an existing subgroup (for example, creating `Linux servers` when `Linux servers/Databases` already exists), no permissions to the parent are set.

When editing any template group, you can also set an additional option, _Apply permissions to all subgroups_.

![](/documentation/current/assets/en/manual/config/template_group2.png)

Marking this checkbox and clicking on _Update_ will apply the same level of permissions to all current and future subgroups of the template group being edited.

So, if any user groups have been given varying [permissions](/documentation/current/en/manual/config/users_and_usergroups/usergroup#configuration) to the subgroups of the template group being edited, marking the checkbox will grant all current and future subgroups the same user permissions as the group being edited.

Note that this option is not saved in the database and will override existing permissions. Any changes made through this option can be reverted only manually.