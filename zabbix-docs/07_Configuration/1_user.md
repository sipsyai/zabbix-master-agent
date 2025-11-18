---
title: Configuring a user
source: https://www.zabbix.com/documentation/current/en/manual/config/users_and_usergroups/user
downloaded: 2025-11-14 10:36:36
---

# 1 Configuring a user

#### Overview

The initial Zabbix installation has two predefined users:

  * _Admin_ \- a Zabbix [superuser](/documentation/current/en/manual/config/users_and_usergroups/permissions#user-types) with full permissions.
  * _guest_ \- a special Zabbix [user](/documentation/current/en/manual/config/users_and_usergroups/permissions#user-types). The 'guest' user is disabled by default. If you add it to the Guests user group, you may log in with this user and access monitoring pages in Zabbix. Note that by default, 'guest' has no permissions on Zabbix objects.

To configure a user:

  * Go to _Users → Users_.
  * Click on _Create user_ (or on a user name to edit an existing user).
  * Edit user attributes in the form.

#### General attributes

The _User_ tab contains general user attributes:

![](/documentation/current/assets/en/manual/config/user.png)

All mandatory input fields are marked with a red asterisk.

_Username_ | Unique username, used as the login name.  
---|---  
_Name_ | User first name (optional).  
If not empty, visible in acknowledgment information and notification recipient information.  
_Last name_ | User last name (optional).  
If not empty, visible in acknowledgment information and notification recipient information.  
_Groups_ | Select [user groups](usergroup) the user belongs to. This field is auto-complete so starting to type the name of a user group will offer a dropdown of matching groups. Scroll down to select. Alternatively, click on _Select_ to add groups. Click on 'x' to remove the selected.  
Adherence to user groups determines what host groups and hosts the user will have [access to](permissions).  
_Password_ | Two fields for entering the user password, or a _Change password_ button if the user already exists.  
Clicking on the _Change password_ button opens two fields for entering a new password.  
For the user with the _Super admin role_ changing own password, clicking on the _Change password_ button opens an additional field for entering the current (old) password.  
On a successful password change, the user for which the password was changed will be logged out of all active sessions.  
Note that the password can only be changed for users using Zabbix [internal authentication](/documentation/current/en/manual/web_interface/frontend_sections/users/authentication#default-authentication).  
_Language_ | Language of the Zabbix frontend.  
The php gettext extension is required for the translations to work.  
_Time zone_ | Select the time zone to override global [time zone](/documentation/current/en/manual/web_interface/time_zone#overview) on user level or select **System default** to use global time zone settings.  
_Theme_ | Defines how the frontend looks like:  
**System default** \- use default system settings  
**Blue** \- standard blue theme  
**Dark** \- alternative dark theme  
**High-contrast light** \- light theme with high contrast  
**High-contrast dark** \- dark theme with high contrast  
_Auto-login_ | Mark this checkbox to make Zabbix remember the user and log the user in automatically for 30 days.   
When logging in with [_Remember for 30 days_](/documentation/current/en/manual/quickstart/login#persistent-login):  
\- Auto-logout is reset (session persists for 30 days).  
\- Auto-login is enabled for seamless re-authentication.  
When logging in without _Remember for 30 days_ :  
\- Auto-login is enabled for seamless re-authentication.  
\- Auto-logout remains governed by the standard timeout setting.   
Browser cookies are used for this.  
_Auto-logout_ | With this checkbox marked the user will be logged out automatically, after the set amount of seconds (minimum 90 seconds, maximum 1 day).  
Note, that this setting is overridden if [_Remember for 30 days_](/documentation/current/en/manual/quickstart/login#persistent-login) is enabled, as the session is extended for the full period.  
[Time suffixes](/documentation/current/en/manual/appendix/suffixes) are supported, e.g. 90s, 5m, 2h, 1d.  
Note that this option will not work:  
* If the "Show warning if Zabbix server is down" global configuration option is enabled and Zabbix frontend is kept open.  
* When Monitoring menu pages perform background information refreshes.  
* If logging in with the _Remember me for 30 days_ option checked.  
_Refresh_ | Set the refresh rate used for graphs, plain text data, etc. Can be set to 0 to disable.  
[Time suffixes](/documentation/current/en/manual/appendix/suffixes) are supported, e.g. 90s, 5m, 1h.  
_Rows per page_ | You can determine how many rows per page will be displayed in lists.  
_URL (after login)_ | You can make Zabbix transfer the user to a specific URL after successful login, for example, to _Problems_ page.  
  
#### User media

The _Media_ tab contains a listing of all media defined for the user. Media are used for sending notifications.

![](/documentation/current/assets/en/manual/config/user_media.png)

Click on _Add_ to assign media to the user.

If the media type has been disabled:

  * A yellow info icon is displayed after the name.
  * _Disabled_ is displayed in the Status column.

User permissions to change media details for themselves can be granted/revoked based on their [user role](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) (see _Create and edit own media_ option). Super admin user permissions to change media details for others can also be granted/revoked based on their [user role](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) (see _Create and edit user media_ option)

See the [Media types](/documentation/current/en/manual/config/notifications/media#user-media) section for details on configuring user media.

#### Permissions

The _Permissions_ tab contains information on the following elements:

  * User role (mandatory for any newly created user) that can only be changed by a _Super admin_ user.

Users cannot be created without a [user role](/documentation/current/en/manual/config/users_and_usergroups/permissions#user-roles) (except with Zabbix [User API](/documentation/current/en/manual/api/reference/user/object)). Previously created users which do not have a role may still be edited without assigning a role to them. However, once a role is assigned, it can only be changed, not removed.   
  
Note that users without a role can log into Zabbix only using [LDAP](/documentation/current/en/manual/web_interface/frontend_sections/users/authentication/ldap) or [SAML](/documentation/current/en/manual/web_interface/frontend_sections/users/authentication/saml) authentication, provided their LDAP/SAML information matches the user group mappings configured in Zabbix.

  * User type (_User_ , _Admin_ , _Super admin_) that is defined in the user role configuration.
  * Host and template groups that the user has access to. 
    * _User_ and _Admin_ type users, by default, do not have access to any groups, templates, and hosts. To grant such access, users must be included in user groups configured with permissions to the relevant entities.
  * Access rights to sections and elements of Zabbix frontend, modules, and API methods. 
    * Elements with allowed access are displayed in green color, while those with denied access - in light gray color.
  * Rights to perform specific actions. 
    * Actions that the user is allowed to perform are displayed in green color, while those that are denied - in light gray color.

See the [Permissions](permissions) page for details.