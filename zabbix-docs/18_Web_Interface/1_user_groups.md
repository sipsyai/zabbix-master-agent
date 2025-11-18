---
title: User groups
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/users/user_groups
downloaded: 2025-11-14 10:39:16
---

# 1 User groups

#### Overview

In the _Users → User groups_ section user groups of the system are maintained.

#### User groups

A listing of existing user groups with their details is displayed.

![](/documentation/current/assets/en/manual/web_interface/user_groups0.png)

Displayed data:

_Name_ | Name of the user group. Clicking on the user group name opens the user group [configuration form](/documentation/current/en/manual/config/users_and_usergroups/usergroup#configuration).  
---|---  
_#_ | The number of users in the group. Clicking on _Users_ will display the respective users filtered out in the user list.  
_Members_ | Usernames of individual users in the user group (with name and surname in parentheses). Clicking on the username will open the user configuration form. Users from disabled groups are displayed in red.  
_Frontend access_ | Frontend access level is displayed:  
**System default** \- users are authenticated by Zabbix, LDAP or HTTP (depending on the [authentication](authentication) method set globally);  
**Internal** \- users are authenticated by Zabbix; ignored if HTTP authentication is the global default;  
**LDAP** \- users are authenticated by LDAP; ignored if HTTP authentication is the global default;  
**Disabled** \- access to Zabbix frontend is forbidden for this group.  
By clicking on the current level, you can change it.  
_Debug mode_ | [Debug mode](/documentation/current/en/manual/web_interface/debug_mode) status is displayed - _Enabled_ or _Disabled_. By clicking on the status you can change it.  
_Status_ | User group status is displayed - _Enabled_ or _Disabled_. By clicking on the status you can change it.  
  
To configure a new user group, click on the _Create user group_ button in the upper-right corner.

##### Mass editing options

Buttons below the list offer some mass-editing options:

  * _Enable_ \- change the user group status to _Enabled_
  * _Disable_ \- change the user group status to _Disabled_
  * _Enable debug mode_ \- enable debug mode for the user groups
  * _Disable debug mode_ \- disable debug mode for the user groups
  * _Delete_ \- delete the user groups

To use these options, mark the checkboxes before the respective user groups, then click on the required button.

##### Using filter

You can use the filter to display only the user groups you are interested in. For better search performance, data is searched with macros unresolved.

The _Filter_ link is available above the list of user groups. If you click on it, a filter becomes available where you can filter user groups by name and status.

![](/documentation/current/assets/en/manual/web_interface/user_groups_filter1.png)