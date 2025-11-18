---
title: User object
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/user/object
downloaded: 2025-11-14 10:45:29
---

# User object

The following objects are directly related to the `user` API.

### User

The user object has the following properties.

userid | ID | ID of the user.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
\- _required_ for update operations  
---|---|---  
username | string | User's name.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
\- _read-only_ for [provisioned users](/documentation/current/en/manual/web_interface/frontend_sections/users/authentication#default-authentication) if the user is linked to a [user directory](/documentation/current/en/manual/api/reference/userdirectory/object) (`userdirectoryid` is set to a valid value that is not "0"), and user directory provisioning status is enabled (`provision_status` of [User directory object](/documentation/current/en/manual/api/reference/userdirectory/object#userdirectory) is set to "1"), and authentication status of all LDAP or SAML provisioning is enabled (`ldap_jit_status` of [Authentication object](/documentation/current/en/manual/api/reference/authentication/object#authentication) is set to "Enabled for configured LDAP IdPs" or `saml_jit_status` of [Authentication object](/documentation/current/en/manual/api/reference/authentication/object#authentication) is set to "Enabled for configured SAML IdPs")  
passwd | string | User's password.  
  
The value of this parameter can be an empty string if the user is linked to a [user directory](/documentation/current/en/manual/api/reference/userdirectory/object).  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _write-only_  
roleid | ID | ID of the role of the user.  
  
Note that users without a role can log into Zabbix only using [LDAP](/documentation/current/en/manual/web_interface/frontend_sections/users/authentication/ldap) or [SAML](/documentation/current/en/manual/web_interface/frontend_sections/users/authentication/saml) authentication, provided their LDAP/SAML information matches the user group mappings configured in Zabbix.  
attempt_clock | timestamp | Time of the last unsuccessful login attempt.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
attempt_failed | integer | Recent failed login attempt count.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
attempt_ip | string | IP address from where the last unsuccessful login attempt came from.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
autologin | integer | Whether to enable auto-login.  
  
Possible values:  
0 - _(default)_ auto-login disabled;  
1 - auto-login enabled.  
autologout | string | User session life time. Accepts seconds and time unit with suffix. If set to 0s, the session will never expire.  
  
Default: 15m.  
lang | string | Language code of the user's language, for example, `en_US`.  
  
Default: `default` \- system default.  
name | string | Name of the user.  
provisioned | integer | Whether the user has been [provisioned](/documentation/current/en/manual/api/reference/user/provision).  
  
Possible values:  
0 - not provisioned;  
1 - provisioned.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
refresh | string | Automatic refresh period. Accepts seconds or time unit with suffix (e.g., 30s, 90s, 1m, 1h).  
  
Default: 30s.  
rows_per_page | integer | Amount of object rows to show per page.  
  
Default: 50.  
surname | string | Surname of the user.  
theme | string | User's theme.  
  
Possible values:  
`default` \- _(default)_ system default;  
`blue-theme` \- Blue;  
`dark-theme` \- Dark.  
ts_provisioned | timestamp | Time when the latest [provisioning](/documentation/current/en/manual/api/reference/user/provision) operation was made.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
\- _supported_ for _Super admin_ type users  
url | string | URL of the page to redirect the user to after logging in.  
userdirectoryid | ID | ID of the [user directory](/documentation/current/en/manual/api/reference/userdirectory/object) that the user in linked to.  
  
Used for provisioning (creating or updating), as well as to login a user that is linked to a user directory.  
  
For login operations the value of this property will have priority over the `userdirectoryid` property of [user groups](/documentation/current/en/manual/api/reference/usergroup/object#user-group) that the user belongs to.  
  
Default: 0.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
\- _supported_ for _Super admin_ type users  
timezone | string | User's time zone, for example, `Europe/London`, `UTC`.  
  
Default: `default` \- system default.  
  
For the full list of supported time zones please refer to [PHP documentation](https://www.php.net/manual/en/timezones.php).  
  
### Media

The media object has the following properties.

mediaid | ID | ID of the user's media.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
---|---|---  
mediatypeid | ID | ID of the media type used by the user's media.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
sendto | string/array | Address, user name or other identifier of the recipient.  
  
If `type` of [Media type](/documentation/current/en/manual/api/reference/mediatype/object#mediatype) is set to "Email", values are represented as array. For other types of [Media types](/documentation/current/en/manual/api/reference/mediatype/object#mediatype), value is represented as a string.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
active | integer | Whether the media is enabled.  
  
Possible values:  
0 - _(default)_ enabled;  
1 - disabled.  
severity | integer | Trigger severities to send notifications about.  
  
Possible bitmap values:  
1 - Not classified;  
2 - Information;  
4 - Warning;  
8 - Average;  
16 - High;  
32 - Disaster.  
  
This is a bitmask field; any sum of possible bitmap values is acceptable (for example, 48 for Average, High, and Disaster).  
  
Default: 63.  
period | string | Time when the notifications can be sent as a [time period](/documentation/current/en/manual/appendix/time_period) or user macros separated by a semicolon.  
  
Default: 1-7,00:00-24:00.  
provisioned | integer | Whether the user has been [provisioned](/documentation/current/en/manual/api/reference/user/provision).  
  
Possible values:  
0 - not provisioned;  
1 - provisioned.  
userdirectory_mediaid | ID | User directory media mapping ID for provisioned media.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
\- _supported_ for _Super admin_ type users