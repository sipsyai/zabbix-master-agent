---
title: usermacro.delete
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/usermacro/delete
downloaded: 2025-11-14 10:45:57
---

# usermacro.delete

### Description

`object usermacro.delete(array hostMacroIds)`

This method allows to delete host macros.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(array)` IDs of the host macros to delete.

### Return values

`(object)` Returns an object containing the IDs of the deleted host macros under the `hostmacroids` property.

### Examples

#### Deleting multiple host macros

Delete two host macros.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "usermacro.delete",
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
                   "hostmacroids": [
                       "32",
                       "11"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CUserMacro::delete() in _ui/include/classes/api/services/CUserMacro.php_.