---
title: authentication.update
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/authentication/update
downloaded: 2025-11-14 10:40:12
---

# authentication.update

### Description

`object authentication.update(object authentication)`

This method allows to update existing authentication settings.

This method is only available to _Super admin_ user type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object)` [Authentication properties](object#authentication) to be updated.

### Return values

`(array)` Returns an array with the names of updated parameters.

### Examples

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "authentication.update",
               "params": {
                   "http_auth_enabled": 1,
                   "http_case_sensitive": 0,
                   "http_login_form": 1
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": [
                   "http_auth_enabled",
                   "http_case_sensitive",
                   "http_login_form"
               ],
               "id": 1
           }

Copy

✔ Copied

### Source

CAuthentication::update() in _ui/include/classes/api/services/CAuthentication.php_.