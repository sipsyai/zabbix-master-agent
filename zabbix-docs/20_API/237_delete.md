---
title: proxygroup.delete
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/proxygroup/delete
downloaded: 2025-11-14 10:43:50
---

# proxygroup.delete

### Description

`object proxygroup.delete(array proxyGroupIds)`

This method allows to delete proxy groups.

This method is only available to _Super admin_ user type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(array)` IDs of proxy groups to delete.

### Return values

`(object)` Returns an object containing the IDs of the deleted proxy groups under the `proxy_groupids` property.

### Examples

#### Delete multiple proxy groups

Delete two proxy groups.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "proxygroup.delete",
               "params": [
                   "5",
                   "10"
               ],
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "proxy_groupids": [
                       "5",
                       "10"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CProxyGroup::delete() in _ui/include/classes/api/services/CProxyGroup.php_.