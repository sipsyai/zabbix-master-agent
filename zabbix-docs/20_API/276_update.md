---
title: settings.update
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/settings/update
downloaded: 2025-11-14 10:44:29
---

# settings.update

### Description

`object settings.update(object settings)`

This method allows to update existing common settings.

This method is only available to _Super admin_ user type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object)` [Settings properties](object#settings) to be updated.

### Return values

`(array)` Returns an array with the names of updated parameters.

### Examples

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "settings.update",
               "params": {
                   "login_attempts": "1",
                   "login_block": "1m"
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": [
                   "login_attempts",
                   "login_block"
               ],
               "id": 1
           }

Copy

✔ Copied

### Source

CSettings::update() in _ui/include/classes/api/services/CSettings.php_.