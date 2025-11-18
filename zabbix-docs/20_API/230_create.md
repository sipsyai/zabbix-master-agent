---
title: proxy.create
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/proxy/create
downloaded: 2025-11-14 10:43:43
---

# proxy.create  
  
### Description

`object proxy.create(object/array proxies)`

This method allows to create new proxies.

This method is only available to _Super admin_ user type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` Proxies to create.

Additionally to the [standard proxy properties](object#proxy), the method accepts the following parameters.

hosts | array | [Hosts](/documentation/current/en/manual/api/reference/host/object) to be monitored by the proxy.  
If a host is already monitored by a different proxy, it will be reassigned to the current proxy.  
  
The hosts must have only the `hostid` property defined.  
---|---|---  
  
### Return values

`(object)` Returns an object containing the IDs of the created proxies under the `proxyids` property. The order of the returned IDs matches the order of the passed proxies.

### Examples

#### Create an active proxy

Create an action proxy "Active proxy" and assign a host to be monitored by it.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "proxy.create",
               "params": {
                   "name": "Active proxy",
                   "operating_mode": "0",
                   "hosts": [
                       {
                           "hostid": "10279"
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
                       "10280"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Create a passive proxy

Create a passive proxy "Passive proxy" and assign two hosts to be monitored by it.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "proxy.create",
               "params": {
                   "name": "Passive proxy",
                   "operating_mode": "1",
                   "address": "127.0.0.1",
                   "port": "10051",
                   "hosts": [
                       {
                           "hostid": "10192"
                       },
                       {
                           "hostid": "10139"
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
                       "10284"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Creating a proxy and adding it to a proxy group

Create an active proxy "Active proxy" and add it to proxy group with ID "1".

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "proxy.create",
               "params": {
                   "name": "Active proxy",
                   "proxy_groupid": "1",
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

CProxy::create() in _ui/include/classes/api/services/CProxy.php_.