---
title: User group object
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/usergroup/object
downloaded: 2025-11-14 10:45:48
---

# User group object

The following objects are directly related to the `usergroup` API.

### User group

The user group object has the following properties.

usrgrpid | ID | ID of the user group.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
\- _required_ for update operations  
---|---|---  
name | string | Name of the user group.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
debug_mode | integer | Whether debug mode is enabled or disabled.  
  
Possible values:  
0 - _(default)_ disabled;  
1 - enabled.  
gui_access | integer | Frontend authentication method of the users in the group.  
  
Possible values:  
0 - _(default)_ use the system default authentication method;  
1 - use internal authentication;  
2 - use LDAP authentication;  
3 - disable access to the frontend.  
mfa_status | integer | Whether MFA is enabled or disabled for the users in the group.  
  
Possible values:  
0 - disabled (for all configured MFA methods);  
1 - enabled (for all configured MFA methods).  
mfaid | ID | [MFA method](/documentation/current/en/manual/api/reference/mfa/object) used for the users in the group.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ for _Super admin_ type users  
\- _supported_ if `mfa_status` of [Authentication object](/documentation/current/en/manual/api/reference/authentication/object#authentication) is set to "Enabled"  
users_status | integer | Whether the user group is enabled or disabled.  
For [deprovisioned](/documentation/current/en/manual/web_interface/frontend_sections/users/authentication#configuration) users, the user group cannot be enabled.  
  
Possible values:  
0 - _(default)_ enabled;  
1 - disabled.  
userdirectoryid | ID | ID of the user directory used for authentication.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ for _Super admin_ type users  
\- _supported_ if `gui_access` is set to "use the system default authentication method" or "use LDAP authentication"  
  
### Permission

The permission object has the following properties.

id | ID | ID of the host group or template group to add permission to.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
permission | integer | Access level to the host group or template group.  
  
Possible values:  
0 - access denied;  
2 - read-only access;  
3 - read-write access.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
  
### Tag-based permission

The tag-based permission object has the following properties.

groupid | ID | ID of the host group to add permission to.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
tag | string | Tag name.  
value | string | Tag value.