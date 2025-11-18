---
title: HTTP
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/users/authentication/http
downloaded: 2025-11-14 10:39:21
---

# 1 HTTP

#### Overview

HTTP or web server-based [authentication](/documentation/current/en/manual/web_interface/frontend_sections/users/authentication) (for example: BasicAuthentication, NTLM/Kerberos) can be used to check user names and passwords. Note that a user must exist in Zabbix as well, however its Zabbix password will not be used.

Be careful! Make sure that web server authentication is configured and works properly before switching it on.

HTTP authentication can be disabled in the frontend by configuring the corresponding option on the _HTTP settings_ tab in the [_Users > Authentication_](/documentation/current/en/manual/web_interface/frontend_sections/users/authentication) section. When HTTP authentication is disabled, the tab with HTTP authentication options will not be displayed in the frontend. Note that reinstalling the frontend (running setup.php) will reset authentication settings, including HTTP authentication configuration.

#### Configuration

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/administration/auth_http.png)

Configuration parameters:

_Enable HTTP authentication_ | Mark the checkbox to enable HTTP authentication. Hovering the mouse over ![](/documentation/current/assets/en/manual/web_interface/frontend_sections/administration/auth_http_2.png) will bring up a hint box warning that in the case of web server authentication, all users (even with [frontend access](/documentation/current/en/manual/config/users_and_usergroups/usergroup#configuration) set to LDAP/Internal) will be authenticated by the web server, not by Zabbix.  
---|---  
_Default login form_ | Specify whether to direct non-authenticated users to:  
**Zabbix login form** \- standard Zabbix login page.  
**HTTP login form** \- HTTP login page.  
It is recommended to enable web-server based authentication for the `index_http.php` page only. If _Default login form_ is set to 'HTTP login page' the user will be logged in automatically if web server authentication module will set valid user login in the `$_SERVER` variable.  
Supported `$_SERVER` keys are `PHP_AUTH_USER`, `REMOTE_USER`, `AUTH_USER`.  
_Remove domain name_ | A comma-delimited list of domain names that should be removed from the username.  
E.g. `comp,any` \- if username is 'Admin@any', 'comp\Admin', user will be logged in as 'Admin'; if username is 'notacompany\Admin', login will be denied.  
_Case-sensitive login_ | Unmark the checkbox to disable case-sensitive login for usernames (enabled by default).  
Disabling case-sensitive login allows, for example, to log in as "admin" even if the Zabbix user is "Admin" or "ADMIN".  
Please note that if case-sensitive login is disabled and there are multiple Zabbix users with similar usernames (e.g., Admin and admin), the login for those users will always be denied with the following error message: "Authentication failed: supplied credentials are not unique."  
  
For internal users who are unable to log in using HTTP credentials (with HTTP login form set as default) leading to the 401 error, you may want to add a `ErrorDocument 401 /index.php?form=default` line to basic authentication directives, which will redirect to the regular Zabbix login form.