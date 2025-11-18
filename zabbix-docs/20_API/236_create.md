---
title: proxygroup.create
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/proxygroup/create
downloaded: 2025-11-14 10:43:49
---

# proxygroup.create  
  
### Description

`object proxygroup.create(object/array proxyGroups)`

This method allows to create new proxy groups.

This method is only available to _Super admin_ user type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` Proxy groups to create.

The method accepts proxy groups with the [standard proxy group properties](object#proxy-group).

### Return values

`(object)` Returns an object containing the IDs of the created proxy groups under the `proxy_groupids` property. The order of the returned IDs matches the order of the passed proxy groups.

### Examples

#### Create a proxy group

Create a proxy group with custom settings.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "proxygroup.create",
               "params": {
                   "name": "Proxy group",
                   "failover_delay": "5m",
                   "min_online": "10"
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "proxy_groupids": [
                       "5"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CProxyGroup::create() in _ui/include/classes/api/services/CProxyGroup.php_.