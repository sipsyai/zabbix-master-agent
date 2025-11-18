---
title: module.delete
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/module/delete
downloaded: 2025-11-14 10:43:35
---

# module.delete

### Description

`object module.delete(array moduleids)`

This method allows to uninstall modules.

This method is only available to _Super admin_ user type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

Module files must be removed manually.

### Parameters

`(array)` IDs of the modules to uninstall.

### Return values

`(object)` Returns an object containing the IDs of the uninstalled modules under the `moduleids` property.

### Examples

#### Uninstalling multiple modules

Uninstall modules "27" and "28".

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "module.delete",
               "params": [
                   "27",
                   "28"
               ],
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "moduleids": [
                       "27",
                       "28"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CModule::delete() in _ui/include/classes/api/services/CModule.php_.