---
title: user.login
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/user/login
downloaded: 2025-11-14 10:45:34
---

# user.login

### Description

`string/object user.login(object parameters)`

This method allows to log in to the API and generate an authentication token.

When using this method, you also need to do [user.logout](/documentation/current/en/manual/api/reference/user/logout) to prevent the generation of a large number of open session records.

This method is only available to unauthenticated users who do not belong to any [user group](/documentation/current/en/manual/api/reference/usergroup/object#user-group) with enabled multi-factor authentication.

### Parameters

`(object)` Parameters containing the user name and password.

The method accepts the following parameters.

password | string | User password.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
---|---|---  
username | string | User name.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
userData | flag | Return information about the authenticated user.  
  
### Return values

`(string/object)` If the `userData` parameter is used, returns an object containing information about the authenticated user.

Additionally to the [standard user properties](object#user), the following information is returned:

auth_type | integer | Default authentication for the user.  
  
Refer to the `authentication_type` property of the [Authentication object](/documentation/current/en/manual/api/reference/authentication/object#authentication-object) for a list of possible values.  
---|---|---  
debug_mode | integer | Whether debug mode is enabled or disabled for the user.  
  
Refer to the `debug_mode` property of the [User group object](/documentation/current/en/manual/api/reference/usergroup/object#user-group) for a list of possible values.  
deprovisioned | boolean | Whether the user belongs to a [deprovisioned users group](/documentation/current/en/manual/web_interface/frontend_sections/users/authentication#configuration).  
gui_access | string | User's authentication method to the frontend.  
  
Refer to the `gui_access` property of the [User group object](/documentation/current/en/manual/api/reference/usergroup/object#user-group) for a list of possible values.  
mfaid | integer | ID of the [MFA method](/documentation/current/en/manual/api/reference/mfa/object) to use for the user during login.  
  
Returns "0" if MFA is disabled globally or for all user groups that the user belongs to.  
secret | string | Random 32 characters string. Is generated on user login.  
sessionid | string | Authentication token, which must be used in the following API requests.  
type | integer | User type.  
  
Refer to the `type` property of the [Role object](/documentation/current/en/manual/api/reference/role/object#role) for a list of possible values.  
userip | string | IP address of the user.  
  
If a user has been successfully authenticated after one or more failed attempts, the method will return the current values for the `attempt_clock`, `attempt_failed` and `attempt_ip` properties and then reset them.

If the `userData` parameter is not used, the method returns an authentication token that is required for [authentication](/documentation/current/en/manual/api#authentication).

### Examples

#### Authenticating a user

Authenticate a user.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "user.login",
               "params": {
                   "username": "Admin",
                   "password": "zabbix"
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": "0424bd59b807674191e7d77572075f33",
               "id": 1
           }

Copy

✔ Copied

#### Requesting authenticated user's information

Authenticate and return additional information about the user.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "user.login",
               "params": {
                   "username": "Admin",
                   "password": "zabbix",
                   "userData": true
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "userid": "1",
                   "username": "Admin",
                   "name": "Zabbix",
                   "surname": "Administrator",
                   "url": "",
                   "autologin": "1",
                   "autologout": "0",
                   "lang": "ru_RU",
                   "refresh": "0",
                   "theme": "default",
                   "attempt_failed": "0",
                   "attempt_ip": "127.0.0.1",
                   "attempt_clock": "1355919038",
                   "rows_per_page": "50",
                   "timezone": "Europe/Riga",
                   "roleid": "3",
                   "userdirectoryid": "0",
                   "type": 3,
                   "userip": "127.0.0.1",
                   "debug_mode": 0,
                   "gui_access": "0",
                   "mfaid": "1",
                   "deprovisioned": false,
                   "auth_type": 0,
                   "sessionid": "5b56eee8be445e98f0bd42b435736e42",
                   "secret": "cd0ba923319741c6586f3d866423a8f4"
               },
               "id": 1
           }

Copy

✔ Copied

### See also

  * [user.logout](logout)

### Source

CUser::login() in _ui/include/classes/api/services/CUser.php_.