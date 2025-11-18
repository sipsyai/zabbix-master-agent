---
title: User groups
source: https://www.zabbix.com/documentation/current/en/manual/config/users_and_usergroups/usergroup
downloaded: 2025-11-14 10:36:38
---

# 3 User groups

#### Overview

User groups allow to group users both for organizational purposes and for assigning permissions to data. Permissions to viewing and configuring data of host groups and template groups are assigned to user groups, not individual users.

It may often make sense to separate what information is available for one group of users and what - for another. This can be accomplished by grouping users and then assigning varied permissions to host and template groups.

A user can belong to any number of groups.

#### Configuration

To configure a user group:

  * Go to _Users → User groups_
  * Click on _Create user group_ (or on the group name to edit an existing group)
  * Edit group attributes in the form

The **User group** tab contains general group attributes:

![](/documentation/current/assets/en/manual/config/user_group.png)

All mandatory input fields are marked with a red asterisk.

_Group name_ | Unique group name.  
---|---  
_Users_ | To add users to the group start typing the name of an existing user. When the dropdown with matching user names appears, scroll down to select.  
Alternatively you may click the _Select_ button to select users in a popup.  
_Frontend access_ | How the users of the group are authenticated.  
**System default** \- use default authentication method (set [globally](/documentation/current/en/manual/web_interface/frontend_sections/users/authentication))  
**Internal** \- use Zabbix internal authentication (even if LDAP authentication is used globally).  
Ignored if HTTP authentication is the global default.  
**LDAP** \- use LDAP authentication (even if internal authentication is used globally).  
Ignored if HTTP authentication is the global default.  
**Disabled** \- access to Zabbix frontend is forbidden for this group  
_LDAP server_ | Select which [LDAP server](/documentation/current/en/manual/web_interface/frontend_sections/users/authentication/ldap#configuration) to use to authenticate the user.  
This field is enabled only if _Frontend access_ is set to LDAP or System default.  
_Multi-factor authentication_ | Select which multi-factor authentication [method](/documentation/current/en/manual/web_interface/frontend_sections/users/authentication/mfa#method-configuration) to use to authenticate the user:  
**Default** \- use the method set as default in MFA configuration; this option is selected by default for new user groups if MFA is enabled;  
**< Method name>** \- use selected method (for example, "Zabbix TOTP");  
**Disabled** \- MFA is disabled for this group; this option is selected by default for new user groups if MFA is disabled.  
Note that if a user belongs to multiple user groups with MFA enabled (or at least one group has MFA enabled), the following authentication rules apply: if any group uses the "Default" MFA method, it will authenticate the user; otherwise, the first method (ordered alphabetically) will be used for authentication.  
_Enabled_ | Status of user group and group members.  
_Checked_ \- user group and users are enabled  
 _Unchecked_ \- user group and users are disabled  
_Debug mode_ | Mark this checkbox to activate [debug mode](/documentation/current/en/manual/web_interface/debug_mode) for the users.  
  
The **Template permissions** tab allows specifying user group access to template group (and thereby template) data:

![](/documentation/current/assets/en/manual/config/user_group_templates.png)

The **Host permissions** tab allows specifying user group access to host group (and thereby host) data:

![](/documentation/current/assets/en/manual/config/user_group_hosts.png)

Click on ![](/documentation/current/assets/en/manual/config/add_link.png) to choose the template/host groups (be it a parent or a nested group) and assign permissions to those. Start typing the group name (a dropdown of matching groups will appear) or click on _Select_ for a popup window listing all groups to be opened.

Then use the option buttons to assign permissions to the chosen groups. Possible permissions are the following:

  * **Read-write** \- read-write access to a group;
  * **Read** \- read-only access to a group;
  * **Deny** \- access to a group denied.

If the same template/host group is added in several rows with different permissions set, the strictest permission will be applied.

Note that a _Super admin_ user can enforce nested groups to have the same level of permissions as the parent group; this can be done in the [host](/documentation/current/en/manual/config/hosts/host_groups)/[template](/documentation/current/en/manual/config/templates/template_groups) group configuration form.

**Template permissions** and **Host permissions** tabs support the same set of parameters.

Current permissions to groups are displayed in the _Permissions_ block, and those can be modified or removed.

If a user group has **Read-write** permissions to a host and **Deny** or no permissions to a template linked to this host, the users of such group will not be able to edit templated items on the host, and template name will be displayed as _Inaccessible template_.

The **Problem tag filter** tab allows setting tag-based permissions for user groups to see problems filtered by tag name and value:

![](/documentation/current/assets/en/manual/config/user_group_tags.png)

Click on ![](/documentation/current/assets/en/manual/config/add_link.png) to choose the host groups. To select a host group to apply a tag filter for, click _Select_ to get the complete list of existing host groups or start typing the name of a host group to get a dropdown of matching groups. Only host groups will be displayed, because problem tag filter cannot be applied to template groups.

Then it is possible to switch from _All tags_ to _Tag list_ in order to set particular tags and their values for filtering. Tag names without values can be added, but values without names cannot. Only the first three tags (with values, if any) are displayed in the _Permissions_ block; if there are more, those can be seen by clicking or hovering over the ![](/documentation/current/assets/en/manual/config/items/itemtypes/dependent_item_button.png) icon.

Tag filter allows separating the access to host group from the possibility to see problems.

For example, if a database administrator needs to see only "MySQL" database problems, it is required to create a user group for database administrators first, then specify "target" tag name and "mysql" value.

![](/documentation/current/assets/en/manual/config/user_group_tag_filter_2.png)

If "target" tag name is specified and value field is left blank, the user group will see all problems with tag name "target" for the selected host group. If _All tags_ is selected, the user group will see all problems for the specified host group.

Make sure tag name and tag value are correctly specified, otherwise, the user group will not see any problems.

Let's review an example when a user is a member of several user groups selected. Filtering in this case will use OR condition for tags.

**User group A** | **User group B** | **Visible result for a user (member) of both groups**  
---|---|---  
_Tag filter_  
_Host group_ | _Tag name_ | _Tag value_ | _Host group_ | _Tag name_ | _Tag value_  
Databases | target | mysql | Databases | target | oracle | target:mysql or target:oracle problems visible  
Databases | set to: _All tags_ | Databases | target | oracle | All problems visible  
Not configured in the **Problem tag filter** | Databases | target | oracle | target:oracle problems visible  
  
Adding a filter (for example, all tags in a certain host group "Databases") results in not being able to see the problems of other host groups.

#### Access from several user groups

A user may belong to any number of user groups. These groups may have different access permissions to hosts or templates.

Therefore, it is important to know what entities an unprivileged user will be able to access as a result. For example, let us consider how access to host **X** (in Hostgroup 1) will be affected in various situations for a user who is in user groups A and B.

  * If Group A has only _Read_ access to Hostgroup 1, but Group B _Read-write_ access to Hostgroup 1, the user will get **Read-write** access to 'X'.

“Read-write” permissions have precedence over “Read” permissions.

  * In the same scenario as above, if 'X' is simultaneously also in Hostgroup 2 that is **denied** to Group A or B, access to 'X' will be **unavailable** , despite a _Read-write_ access to Hostgroup 1.
  * If Group A has no permissions defined and Group B has a _Read-write_ access to Hostgroup 1, the user will get **Read-write** access to 'X'.
  * If Group A has _Deny_ access to Hostgroup 1 and Group B has a _Read-write_ access to Hostgroup 1, the user will get access to 'X' **denied**.

#### Other details

  * An Admin level user with _Read-write_ access to a host will not be able to link/unlink templates, if he has no access to the template group they belong to. With _Read_ access to the template group he will be able to link/unlink templates to the host, however, will not see any templates in the template list and will not be able to operate with templates in other places.
  * An Admin level user with _Read_ access to a host will not see the host in the configuration section host list; however, the host triggers will be accessible in IT service configuration.
  * Any non-Super Admin user (including 'guest') can see network maps as long as the map is empty or has only images. When hosts, host groups or triggers are added to the map, permissions are respected.
  * Zabbix server will not send notifications to users defined as action operation recipients if access to the concerned host is explicitly "denied".