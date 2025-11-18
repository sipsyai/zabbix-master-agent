---
title: valuemap.delete
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/valuemap/delete
downloaded: 2025-11-14 10:46:05
---

# valuemap.delete

### Description

`object valuemap.delete(array valuemapids)`

This method allows to delete value maps.

This method is only available to _Super admin_ user type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(array)` IDs of the value maps to delete.

### Return values

`(object)` Returns an object containing the IDs of the deleted value maps under the `valuemapids` property.

### Examples

#### Deleting multiple value maps

Delete two value maps.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "valuemap.delete",
               "params": [
                   "1",
                   "2"
               ],
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "valuemapids": [
                       "1",
                       "2"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CValueMap::delete() in _ui/include/classes/api/services/CValueMap.php_.