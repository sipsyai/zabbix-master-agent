---
title: service.delete
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/service/delete
downloaded: 2025-11-14 10:44:23
---

# service.delete

### Description

`object service.delete(array serviceIds)`

This method allows to delete services.

This method is available to users of any type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(array)` IDs of the services to delete.

### Return values

`(object)` Returns an object containing the IDs of the deleted services under the `serviceids` property.

### Examples

#### Deleting multiple services

Delete two services.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "service.delete",
               "params": [
                   "4",
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
                   "serviceids": [
                       "4",
                       "5"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CService::delete() in _ui/include/classes/api/services/CService.php_.