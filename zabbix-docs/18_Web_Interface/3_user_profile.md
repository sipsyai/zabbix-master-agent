---
title: User settings
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/user_profile
downloaded: 2025-11-14 10:39:33
---

# 3 User settings

#### Overview

Depending on user role permissions, the _User settings_ section may contain the following pages:

  * _Profile_ or _User profile_ \- for customizing certain Zabbix frontend features;
  * _Notifications_ \- for customizing current user notifications;
  * _API tokens_ \- for managing API tokens assigned to the current user.

The list of available pages appears upon clicking the ![](/documentation/current/assets/en/manual/web_interface/user_profile.png) user icon near the bottom of the Zabbix menu (not available for the _guest_ user). It is also possible to switch between pages by using the title dropdown in the upper-left corner.

![](/documentation/current/assets/en/manual/web_interface/user_settings_menu.png) | ![](/documentation/current/assets/en/manual/web_interface/user_settings_selector.png)  
---|---  
Third-level menu. | Title dropdown.  
  
#### User profile

The _User profile_ section provides options to set a custom interface language, color theme, number of rows displayed in the lists, etc. The changes made here will be applied to the current user only.

![profile.png](/documentation/current/assets/en/manual/web_interface/profile.png)

_Name_ | User name and surname are displayed.  
In the absence of name and surname, the username is displayed.  
---|---  
_Password_ | Click on the _Change password_ button to open three fields: _Old password_ , _New password_ , _New password (once again)_.  
On a successful password change, the user will be logged out of all active sessions.  
Note that the password can only be changed for users using Zabbix [internal authentication](/documentation/current/en/manual/web_interface/frontend_sections/users/authentication#default-authentication).  
_Language_ | Select the interface language of your choice or select **System default** to use default system settings.  
Selecting _English (en_US)_ will also enable the US time/date format in the frontend.  
For more information, see [Installation of additional frontend languages](/documentation/current/en/manual/appendix/install/locales).  
_Time zone_ | Select the time zone to override the global [time zone](/documentation/current/en/manual/web_interface/time_zone#overview) on the user level or select **System default** to use global time zone settings.  
_Theme_ | Select a color theme specifically for your profile:  
**System default** \- use default system settings;  
**Blue** \- standard blue theme;  
**Dark** \- alternative dark theme;  
**High-contrast light** \- light theme with high contrast;  
**High-contrast dark** \- dark theme with high contrast.  
_Auto-login_ | Mark this checkbox to make Zabbix remember you and log you in automatically for 30 days.   
When logging in with [_Remember for 30 days_](/documentation/current/en/manual/quickstart/login#persistent-login) enabled:  
\- Auto-logout timer is reset (session persists until the 30-day period ends).  
\- Auto-login is enabled on subsequent visits within 30 days.   
When logging in without _Remember for 30 days_ :  
\- Auto-login parameter is cleared.  
\- Auto-logout follows the configured timeout as usual.  
Browser cookies are used for this.  
_Auto-logout_ | With this checkbox marked, you will be logged out automatically after the set amount of seconds (minimum 90 seconds, maximum 1 day).  
Note, that if logging in with [_Remember for 30 days_](/documentation/current/en/manual/quickstart/login#persistent-login) enabled, the auto-logout timer is overridden, keeping your session active for the full period.  
[Time suffixes](/documentation/current/en/manual/appendix/suffixes) are supported, for example: 90s, 5m, 2h, 1d.  
Note that this option will not work in the following cases:  
* When the [_Monitoring_](/documentation/current/en/manual/web_interface/frontend_sections/monitoring) menu pages perform background information refreshes. In case pages that are refreshing data in a specific time interval (dashboards, graphs, latest data, etc.) are left open, the session lifetime is extended, respectively disabling the auto-logout feature.  
* If logging in with the [_Remember me for 30 days_](/documentation/current/en/manual/installation/frontend#log-in) option checked.  
* When authentication is performed via an SSO Identity Provider (IdP), auto-logout ends only the Zabbix session. The SSO session with the IdP remains active, so the user may be able to log back in without entering a password.  
_Auto-logout_ can also accept "0", meaning that the auto-logout feature becomes disabled after profile settings update.  
_Refresh_ | Set how often the information on the [_Monitoring_](/documentation/current/en/manual/web_interface/frontend_sections/monitoring) menu pages will be refreshed (minimum 0 seconds, maximum 1 hour).  
[Time suffixes](/documentation/current/en/manual/appendix/suffixes) are supported, for example: 30s, 90s, 1m, 1h.  
_Rows per page_ | Set how many rows will be displayed per page in the lists. Fewer rows (and fewer records to display) result in faster loading times.  
_URL (after login)_ | Set a specific URL to be displayed after login. Instead of the default _Dashboards_ , it can be, for example, the URL of _Monitoring_ > _Triggers_.  
  
#### Notifications

The _Notifications_ section provides options for customizing current user notifications.

The _Media_ tab allows you to specify [media details](/documentation/current/en/manual/config/notifications/media#user-media) for the user, such as media types and addresses to use and when to use them to deliver notifications.

![profile_b.png](/documentation/current/assets/en/manual/web_interface/profile_b.png)

If the media type has been disabled:

  * a yellow info icon is displayed after the name;
  * "Disabled" is displayed in the _Status_ column.

User permissions to change media details for themselves can be granted/revoked based on their [user role](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) (see _Create and edit own media_ option). Super admin user permissions to change media details for others can also be granted/revoked based on their [user role](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) (see _Create and edit user media_ option)

Note that for provisioned users:

  * provisioned user media cannot be deleted;
  * provisioned user media can be disabled/enabled;
  * such provisioned user media fields as _When active_ , _Use if severity_ and _Enabled_ can be manually edited;
  * additional user media can be added (for example, additional email addresses) for provisioned users manually;
  * manually added user media can be deleted.

The _Frontend notifications_ tab allows you to set [global notifications](/documentation/current/en/manual/web_interface/user_profile/global_notifications).

#### API tokens

The _API tokens_ section allows you to view tokens assigned to the user, edit token details and [create new tokens](/documentation/current/en/manual/web_interface/frontend_sections/users/api_tokens). This section is available to a user only if the _Manage API tokens_ action is allowed in the [user role](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) settings.

![](/documentation/current/assets/en/manual/web_interface/user_tokens.png)

You can filter API tokens by name, expiry date, or status (_Enabled/Disabled_). Click on the token status in the list to quickly enable/disable a token. You can also enable/disable multiple tokens at once by selecting them in the list and then clicking on the _Enable/Disable_ buttons below the list.

Users cannot view the _Auth token_ value of the tokens assigned to them in Zabbix. The _Auth token_ value is displayed only once - immediately after creating a token. If the token has been lost, it has to be regenerated.