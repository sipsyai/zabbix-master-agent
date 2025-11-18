---
title: iconmap.delete
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/iconmap/delete
downloaded: 2025-11-14 10:42:35
---

# iconmap.delete

### Description

`object iconmap.delete(array iconMapIds)`

This method allows to delete icon maps.

This method is only available to _Super admin_ user type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(array)` IDs of the icon maps to delete.

### Return values

`(object)` Returns an object containing the IDs of the deleted icon maps under the `iconmapids` property.

### Examples

#### Delete multiple icon maps

Delete two icon maps.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "iconmap.delete",
               "params": [
                   "2",
                   "5"
               ],
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "iconmapids": [
                       "2",
                       "5"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CIconMap::delete() in _ui/include/classes/api/services/CIconMap.php_.