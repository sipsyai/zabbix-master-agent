---
title: Authentication object
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/authentication/object
downloaded: 2025-11-14 10:40:10
---

# Authentication object

The following objects are directly related to the `authentication` API.

### Authentication

The authentication object has the following properties.

authentication_type | integer | Default authentication.  
  
Possible values:  
0 - _(default)_ Internal;  
1 - LDAP.  
---|---|---  
http_auth_enabled | integer | HTTP authentication.  
  
Possible values:  
0 - _(default)_ Disabled;  
1 - Enabled.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `$ALLOW_HTTP_AUTH` is enabled in the [frontend configuration file](/documentation/current/en/manual/installation/frontend#install) (_zabbix.conf.php_).  
http_login_form | integer | Default login form.  
  
Possible values:  
0 - _(default)_ Zabbix login form;  
1 - HTTP login form.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `$ALLOW_HTTP_AUTH` is enabled in the [frontend configuration file](/documentation/current/en/manual/installation/frontend#install) (_zabbix.conf.php_).  
http_strip_domains | string | Domain name to remove.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `$ALLOW_HTTP_AUTH` is enabled in the [frontend configuration file](/documentation/current/en/manual/installation/frontend#install) (_zabbix.conf.php_).  
http_case_sensitive | integer | HTTP case-sensitive login.  
  
Possible values:  
0 - Off;  
1 - _(default)_ On.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `$ALLOW_HTTP_AUTH` is enabled in the [frontend configuration file](/documentation/current/en/manual/installation/frontend#install) (_zabbix.conf.php_).  
ldap_auth_enabled | integer | LDAP authentication.  
  
Possible values:  
0 - _(default)_ Disabled;  
1 - Enabled.  
ldap_case_sensitive | integer | LDAP case-sensitive login.  
  
Possible values:  
0 - Off;  
1 - _(default)_ On.  
ldap_userdirectoryid | ID | ID of the default user directory for LDAP authentication.  
Used for user groups with `gui_access` set to LDAP or System default.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `ldap_auth_enabled` is set to "Enabled"  
saml_auth_enabled | integer | SAML authentication.  
  
Possible values:  
0 - _(default)_ Disabled;  
1 - Enabled.  
saml_case_sensitive | integer | SAML case-sensitive login.  
  
Possible values:  
0 - Off;  
1 - _(default)_ On.  
passwd_min_length | integer | Password minimal length requirement.  
  
Possible values range from 1 to 70.  
  
Default: 8.  
passwd_check_rules | integer | Password checking rules.  
  
Possible bitmap values:  
0 - Check password length;  
1 - Check if password uses uppercase and lowercase Latin letters;  
2 - Check if password uses digits;  
4 - Check if password uses special characters;  
8 - _(default)_ Check if password is not in the list of commonly used passwords and does not contain derivations of word "Zabbix" or user's name, last name, or username.  
  
This is a bitmask field; any sum of possible bitmap values is acceptable (for example, 15 for checking all rules).  
ldap_jit_status | integer | Status of LDAP provisioning.  
  
Possible values:  
0 - Disabled for configured LDAP IdPs;  
1 - Enabled for configured LDAP IdPs.  
saml_jit_status | integer | Status of SAML provisioning.  
  
Possible values:  
0 - Disabled for configured SAML IdPs;  
1 - Enabled for configured SAML IdPs.  
jit_provision_interval | string | Time interval between JIT provision requests for logged-in user.  
Accepts seconds and time unit with suffix with month and year support (3600s,60m,1h,1d,1M,1y). Minimum value: 1h.  
  
Default: 1h.  
  
Available only for LDAP provisioning.  
disabled_usrgrpid | ID | ID of the user group to assign the deprovisioned user to.  
The user group must be disabled and cannot be enabled or deleted when configured.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `ldap_jit_status` is set to "Enabled for configured LDAP IdPs", or `saml_jit_status` is set to "Enabled for configured SAML IdPs"  
mfa_status | integer | [Multi-factor authentication](/documentation/current/en/manual/web_interface/frontend_sections/users/authentication/mfa).  
  
Possible values:  
0 - Disabled (for all configured MFA methods);  
1 - Enabled (for all configured MFA methods).  
mfaid | ID | Default [MFA method](/documentation/current/en/manual/api/reference/mfa/object) for [user groups](/documentation/current/en/manual/api/reference/usergroup/object#user-group) with MFA enabled.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `mfa_status` is set to "Enabled"