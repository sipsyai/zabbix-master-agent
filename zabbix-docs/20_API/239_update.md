---
title: proxygroup.update
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/proxygroup/update
downloaded: 2025-11-14 10:43:52
---

# proxygroup.update

### Description

`object proxygroup.update(object/array proxyGroups)`

This method allows to update existing proxy groups.

This method is only available to _Super admin_ user type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` Proxy group properties to be updated.

The `proxy_groupid` property must be defined for each proxy group, all other properties are optional. Only the passed properties will be updated, all others will remain unchanged.

The method accepts proxy groups with the [standard proxy group properties](object#proxy-group).

### Return values

`(object)` Returns an object containing the IDs of the updated proxy groups under the `proxy_groupids` property.

### Examples

#### Change minimum number of online proxies

Change minimum number of online proxies required for the group to be online.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "proxygroup.update",
               "params": {
                   "proxy_groupid": "5",
                   "min_online": "3"
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

CProxyGroup::update() in _ui/include/classes/api/services/CProxyGroup.php_.