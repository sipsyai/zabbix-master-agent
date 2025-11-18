---
title: user.checkAuthentication
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/user/checkauthentication
downloaded: 2025-11-14 10:45:30
---

# user.checkAuthentication  
  
### Description

`object user.checkAuthentication`

This method checks and prolongs the user session.

Calling the `user.checkAuthentication` method using the parameter `sessionid` prolongs the user session by default.

### Parameters

The method accepts the following parameters.

extend | boolean | Whether to prolong the user session.  
  
Default value: "true".  
Setting the value to "false" allows to check the user session without prolonging it.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if `sessionid` is set  
---|---|---  
sessionid | string | User [authentication token](/documentation/current/en/manual/api#authentication).  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_ if `token` is not set  
secret | string | Random 32 characters string. Is generated on user login.  
token | string | User [API token](/documentation/current/en/manual/api#authentication).  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_ if `sessionid` is not set  
  
### Return values

`(object)` Returns an object containing information about the user.

Additionally to the [standard user properties](object#user), the following information is returned.

auth_type | integer | Default authentication for the user.  
  
Refer to the `authentication_type` property of the [Authentication object](/documentation/current/en/manual/api/reference/authentication/object#authentication-object) for a list of possible values.  
---|---|---  
debug_mode | integer | Whether debug mode is enabled or disabled for the user.  
  
Refer to the `debug_mode` property of the [User group object](/documentation/current/en/manual/api/reference/usergroup/object#user-group) for a list of possible values.  
deprovisioned | boolean | Whether the user belongs to a [deprovisioned users group](/documentation/current/en/manual/web_interface/frontend_sections/users/authentication#configuration).  
gui_access | string | User's authentication method to the frontend.  
  
Refer to the `gui_access` property of the [User group object](/documentation/current/en/manual/api/reference/usergroup/object#user-group) for a list of possible values.  
secret | string | Random 32 characters string. Is generated on user login.  
  
Property `secret` is not returned if the user session is checked using an API token.  
sessionid | string | Authentication token, which must be used in the following API requests.  
  
Property `sessionid` is not returned if the user session is checked using an API token.  
type | integer | User type.  
  
Refer to the `type` property of the [Role object](/documentation/current/en/manual/api/reference/role/object#role) for a list of possible values.  
userip | string | IP address of the user.  
  
### Examples

##### Check authentication using authentication token

Check and prolong a user session using the user authentication token, and return additional information about the user.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "user.checkAuthentication",
               "params": {
                   "sessionid": "673b8ba11562a35da902c66cf5c23fa2"
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
                   "ts_provisioned": "0",
                   "type": 3,
                   "userip": "127.0.0.1",
                   "debug_mode": 0,
                   "gui_access": "0",
                   "deprovisioned": false,
                   "auth_type": 0,
                   "sessionid": "673b8ba11562a35da902c66cf5c23fa2",
                   "secret": "0e329b933e46984e49a5c1051ecd0751"
               },
               "id": 1
           }

Copy

✔ Copied

##### Check authentication using API token

Check a user session using the user API token, and return additional information about the user.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "user.checkAuthentication",
               "params": {
                   "token": "00aff470e07c12d707e50d98cfe39edef9e6ec349c14728dbdfbc8ddc5ea3eae"
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
                   "attempt_clock": "1355919338",
                   "rows_per_page": "50",
                   "timezone": "Europe/Riga",
                   "roleid": "3",
                   "userdirectoryid": "0",
                   "ts_provisioned": "0",
                   "type": 3,
                   "userip": "127.0.0.1",
                   "debug_mode": 0,
                   "gui_access": "1",
                   "deprovisioned": false,
                   "auth_type": 0
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CUser::checkAuthentication() in _ui/include/classes/api/services/CUser.php_.