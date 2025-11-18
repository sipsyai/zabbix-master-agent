---
title: Users
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/users/user_list
downloaded: 2025-11-14 10:39:18
---

# 3 Users

#### Overview

In the _Users → Users_ section users of the system are maintained.

#### Users

A listing of existing users with their details is displayed.

![](/documentation/current/assets/en/manual/web_interface/users.png)

Displayed data:

_Username_ | Username for logging into Zabbix. Clicking on the username opens the user [configuration form](/documentation/current/en/manual/config/users_and_usergroups/user).  
---|---  
_Name_ | First name of the user.  
_Last name_ | Second name of the user.  
_User role_ | [User role](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) is displayed.  
_Groups_ | Groups that the user is a member of are listed. Clicking on the user group name opens the user group configuration form. Disabled groups are displayed in red.  
_Is online?_ | The on-line status of the user is displayed - _Yes_ or _No_. The time of last user activity is displayed in parentheses.  
_Login_ | The login status of the user is displayed - _Ok_ or _Blocked_. A user can become temporarily blocked upon exceeding the number of unsuccessful login attempts set in the _[Administration → General → Other](/documentation/current/en/manual/web_interface/frontend_sections/administration/general#other-parameters)_ section (five by default). By clicking on _Blocked_ you can unblock the user.  
_Frontend access_ | Frontend access level is displayed - _System default_ , _Internal_ , _LDAP_ , or _Disabled_ , depending on the one set for the whole user group.  
_API access_ | API access status is displayed - _Enabled_ or _Disabled_ , depending on the one set for the user role.  
_Debug mode_ | Debug mode status is displayed - _Enabled_ or _Disabled_ , depending on the one set for the whole user group.  
_Status_ | User status is displayed - _Enabled_ or _Disabled_ , depending on the one set for the whole user group.  
_Provisioned_ | The date when the user was last provisioned is displayed.  
Used for users created by JIT provisioning from LDAP/SAML.  
_Info_ | Information about errors is displayed.  
A yellow warning is displayed for users without user groups.  
A red warning is displayed for users without roles, and for users without roles and user groups.  
  
To configure a new user, click on the _Create user_ button in the upper-right corner.

##### Mass editing options

Buttons below the list offer some mass-editing options:

  * _Provision now_ \- update user information from LDAP (this option is only enabled if an [LDAP](/documentation/current/en/manual/web_interface/frontend_sections/users/authentication/ldap) user is selected)
  * _Reset TOTP secret_ \- reset user TOTP secrets for all TOTP methods and delete the user session (this option is only enabled if [MFA](/documentation/current/en/manual/web_interface/frontend_sections/users/authentication/mfa) is enabled; for users without TOTP secrets, their session will not be deleted)
  * _Unblock_ \- re-enable system access to blocked users
  * _Delete_ \- delete the users

To use these options, mark the check-boxes before the respective users, then click on the required button.

##### Using filter

You can use the filter to display only the users you are interested in. For better search performance, data is searched with macros unresolved.

The _Filter_ link is available above the list of users. If you click on it, a filter becomes available where you can filter users by username, name, last name, user role and user group.

![](/documentation/current/assets/en/manual/web_interface/user_filter.png)