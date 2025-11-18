---
title: proxy.update
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/proxy/update
downloaded: 2025-11-14 10:43:46
---

# proxy.update

### Description

`object proxy.update(object/array proxies)`

This method allows to update existing proxies.

This method is only available to _Super admin_ user type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` Proxy properties to be updated.

The `proxyid` property must be defined for each proxy, all other properties are optional. Only the passed properties will be updated, all others will remain unchanged.

Additionally to the [standard proxy properties](object#proxy), the method accepts the following parameters.

hosts | array | [Hosts](/documentation/current/en/manual/api/reference/host/object) to be monitored by the proxy.  
If a host is already monitored by a different proxy, it will be reassigned to the current proxy.  
  
The hosts must have only the `hostid` property defined.  
---|---|---  
  
### Return values

`(object)` Returns an object containing the IDs of the updated proxies under the `proxyids` property.

### Examples

#### Change hosts monitored by a proxy

Update the proxy to monitor the two given hosts.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "proxy.update",
               "params": {
                   "proxyid": "10293",
                   "hosts": [
                       {
                           "hostid": "10294"
                       },
                       {
                           "hostid": "10295"
                       }
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "proxyids": [
                       "10293"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Change proxy status

Change the proxy to an active proxy and rename it to "Active proxy".

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "proxy.update",
               "params": {
                   "proxyid": "10293",
                   "name": "Active proxy",
                   "operating_mode": "0"
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "proxyids": [
                       "10293"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Add a proxy to a proxy group

Update proxy with ID "5" and add it to proxy group with ID "1".

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "proxy.create",
               "params": {
                   "proxyid": "5",
                   "proxy_groupid": "1",
                   "local_address": "127.0.0.1"
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "proxyids": [
                       "5"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### See also

  * [Host](/documentation/current/en/manual/api/reference/host/object#host)
  * [Proxy group](/documentation/current/en/manual/api/reference/proxygroup/object#proxy-group)

### Source

CProxy::update() in _ui/include/classes/api/services/CProxy.php_.