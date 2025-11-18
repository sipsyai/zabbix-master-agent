---
title: Configuring a host group
source: https://www.zabbix.com/documentation/current/en/manual/config/hosts/host_groups
downloaded: 2025-11-14 10:34:37
---

# 3 Configuring a host group

#### Overview

Host groups are used for the logical grouping of hosts and assigning user permissions to them.

Each host must have at least one host group assigned. A host may belong to multiple host groups, and each host group may contain multiple hosts.

Note that in Zabbix, all permissions are based on groups: [user groups](/documentation/current/en/manual/config/users_and_usergroups), host groups, and [template groups](/documentation/current/en/manual/config/hosts/template_groups). So, even if a single user needs access to a single host, it is granted by adding the user to a user group that has permission to access the host group containing that host.

#### Configuration

Only Super admin users can create host groups.

There are two options of creating a host group in Zabbix frontend.

**Option one** :

  * Go to: _Data collection_ → _Host groups_
  * Click on _Create host group_ in the upper-right corner of the screen
  * Enter the group name in the form

![](/documentation/current/assets/en/manual/config/host_group.png)

**Option two** : when [configuring a host](/documentation/current/en/manual/config/hosts/host#configuration), enter a non-existing group name in the _Host groups_ input field.

Once the host group is created, you can click on the group name in the list under _Data collection_ → _Host groups_ to edit the group name, clone the group, or delete the group.

Deleting a host group only deletes the logical group, not the hosts in the group. It is not possible to delete a host group that is the only group for any existing host.

#### Creating host subgroups

A host subgroup (or nested host group) is a child of the parent host group that contains it.

A subgroup is created by using the forward slash '/' in the group name input field to denote its relation to the parent group(s). For example:

  * inputting `Europe/Latvia` creates the `Europe/Latvia` subgroup of the parent group `Europe`.
  * inputting `Europe/Latvia/Riga/Zabbix servers` creates the respective subgroup within the nested parent groups `Europe`, `Europe/Latvia`, `Europe/Latvia/Riga`.

When creating a subgroup, using leading or trailing slashes, or several slashes in a row is not allowed. Escaping of '/' is not supported.

It is not required to create any parent host group(s) before creating a subgroup. You can choose whether to start by creating a subgroup (for example, `Europe/Latvia`) or any parent host group(s) (in our example, `Europe`). If you start by creating a subgroup, parent host group(s) will **not** be created automatically.

##### Permissions to host groups

  * When creating a subgroup to an existing parent host group (for example, creating `Europe/Latvia` when `Europe` already exists), [user group](/documentation/current/en/manual/config/users_and_usergroups/usergroup) permissions to the subgroup are inherited from the parent.
  * When creating a parent host group to an existing subgroup (for example, creating `Europe` when `Europe/Latvia` already exists), no permissions to the parent are set.

When editing any host group, you can also set an additional option, _Apply permissions and tag filters to all subgroups_.

![](/documentation/current/assets/en/manual/config/host_group2.png)

Marking this checkbox and clicking on _Update_ will apply the same level of permissions and tag filters to all current and future subgroups of the host group being edited.

So, if any user groups have been given varying [permissions](/documentation/current/en/manual/config/users_and_usergroups/usergroup#configuration) to the subgroups of the host group being edited, marking the checkbox will grant all current and future subgroups the same user permissions and tag-based permissions as the group being edited.

Note that this option is not saved in the database and will override existing permissions. Any changes made through this option can be reverted only manually.