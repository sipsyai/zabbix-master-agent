---
title: proxy.delete
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/proxy/delete
downloaded: 2025-11-14 10:43:44
---

# proxy.delete

### Description

`object proxy.delete(array proxies)`

This method allows to delete proxies.

This method is only available to _Super admin_ user type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(array)` IDs of proxies to delete.

### Return values

`(object)` Returns an object containing the IDs of the deleted proxies under the `proxyids` property.

### Examples

#### Delete multiple proxies

Delete two proxies.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "proxy.delete",
               "params": [
                   "10286",
                   "10285"
               ],
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "proxyids": [
                       "10286",
                       "10285"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CProxy::delete() in _ui/include/classes/api/services/CProxy.php_.