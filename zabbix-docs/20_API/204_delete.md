---
title: map.delete
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/map/delete
downloaded: 2025-11-14 10:43:17
---

# map.delete

### Description

`object map.delete(array mapIds)`

This method allows to delete maps.

This method is available to users of any type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(array)` IDs of the maps to delete.

### Return values

`(object)` Returns an object containing the IDs of the deleted maps under the `sysmapids` property.

### Examples

#### Delete multiple maps

Delete two maps.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "map.delete",
               "params": [
                   "12",
                   "34"
               ],
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "sysmapids": [
                       "12",
                       "34"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CMap::delete() in _ui/include/classes/api/services/CMap.php_.