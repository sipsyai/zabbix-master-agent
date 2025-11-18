---
title: usermacro.deleteglobal
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/usermacro/deleteglobal
downloaded: 2025-11-14 10:45:58
---

# usermacro.deleteglobal

### Description

`object usermacro.deleteglobal(array globalMacroIds)`

This method allows to delete global macros.

This method is only available to _Super admin_ user type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(array)` IDs of the global macros to delete.

### Return values

`(object)` Returns an object containing the IDs of the deleted global macros under the `globalmacroids` property.

### Examples

#### Deleting multiple global macros

Delete two global macros.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "usermacro.deleteglobal",
               "params": [
                   "32",
                   "11"
               ],
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "globalmacroids": [
                       "32",
                       "11"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CUserMacro::deleteGlobal() in _ui/include/classes/api/services/CUserMacro.php_.