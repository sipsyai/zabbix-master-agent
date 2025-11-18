---
title: Authentication
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/users/authentication
downloaded: 2025-11-14 10:39:20
---

# 5 Authentication

### Overview

The _Users → Authentication_ section allows to specify the user authentication method for Zabbix and internal password requirements.

The available authentication methods are internal, HTTP, LDAP, SAML, and MFA authentication.

#### Default authentication

By default, Zabbix uses **internal** Zabbix authentication for all users.

It is possible to change the default authentication method to [LDAP](/documentation/current/en/manual/web_interface/frontend_sections/users/authentication/ldap) system-wide. To do so, navigate to the _LDAP_ tab and configure LDAP parameters, then return to the _Authentication_ tab and switch the _Default authentication_ selector to LDAP.

Note that the authentication method can be fine-tuned on the [user group](/documentation/current/en/manual/config/users_and_usergroups/usergroup) level. Even if LDAP authentication is set globally, some user groups can still be authenticated by Zabbix. These groups must have [frontend access](/documentation/current/en/manual/config/users_and_usergroups/usergroup#configuration) set to Internal.

It is also possible to enable LDAP authentication only for specific user groups, if internal authentication is used globally. In this case LDAP authentication details can be specified and used for specific user groups whose [frontend access](/documentation/current/en/manual/config/users_and_usergroups/usergroup#configuration) must then be set to LDAP. If a user is included into at least one user group with LDAP authentication, this user will not be able to use the internal authentication method.

HTTP, SAML 2.0, and MFA authentication methods can be used in addition to the default authentication method.

Zabbix supports just-in-time (JIT) provisioning that allows to create user accounts in Zabbix the first time an external user authenticates and provision these user accounts. JIT provisioning is supported for LDAP and SAML.

See also:

  * [HTTP authentication](/documentation/current/en/manual/web_interface/frontend_sections/users/authentication/http)
  * [LDAP authentication](/documentation/current/en/manual/web_interface/frontend_sections/users/authentication/ldap)
  * [SAML authentication](/documentation/current/en/manual/web_interface/frontend_sections/users/authentication/saml)
  * [MFA authentication](/documentation/current/en/manual/web_interface/frontend_sections/users/authentication/mfa)

#### Configuration

The _Authentication_ tab allows to set the default authentication method, specify a group for deprovisioned users and set password complexity requirements for Zabbix users.

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/users/auth.png)

Configuration parameters:

_Default authentication_ | Select the default authentication method for Zabbix - _Internal_ or _LDAP_.  
---|---  
_Deprovisioned users group_ | Specify a user group for deprovisioned users. This setting is required only for JIT provisioning, regarding users that were created in Zabbix from LDAP or SAML systems, but no longer need to be provisioned.  
A disabled user group must be specified.  
_Minimum password length_ | By default, the minimum password length is set to 8. Supported range: 1-70. Note that passwords longer than 72 characters will be truncated.  
_Password must contain_ | Mark one or several checkboxes to require usage of specified characters in a password:  
\- an uppercase and a lowercase Latin letter  
\- a digit  
\- a special character  
  
Hover over the question mark to see a hint with the list of characters for each option.  
_Avoid easy-to-guess passwords_ | If marked, a password will be checked against the following requirements:  
\- must not contain user's name, surname, or username  
\- must not be one of the common or context-specific passwords.  
  
The list of common and context-specific passwords is generated automatically from the list of NCSC "Top 100k passwords", the list of SecLists "Top 1M passwords" and the list of Zabbix context-specific passwords. Internal users will not be allowed to set passwords included in this list as such passwords are considered weak due to their common use.  
  
Changes in password complexity requirements will not affect existing user passwords, but if an existing user chooses to change a password, the new password will have to meet current requirements. A hint with the list of requirements will be displayed next to the _Password_ field in the [user profile](/documentation/current/en/manual/web_interface/user_profile) and in the [user configuration form](/documentation/current/en/manual/config/users_and_usergroups/user) accessible from the _Users → Users_ menu.