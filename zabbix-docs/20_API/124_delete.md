---
title: host.delete
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/host/delete
downloaded: 2025-11-14 10:41:57
---

# host.delete

### Description

`object host.delete(array hosts)`

This method allows to delete hosts.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(array)` IDs of hosts to delete.

### Return values

`(object)` Returns an object containing the IDs of the deleted hosts under the `hostids` property.

### Examples

#### Deleting multiple hosts

Delete two hosts.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "host.delete",
               "params": [
                   "13",
                   "32"
               ],
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "hostids": [
                       "13",
                       "32"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CHost::delete() in _ui/include/classes/api/services/CHost.php_.