---
title: host.create
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/host/create
downloaded: 2025-11-14 10:41:57
---

# host.create  
  
### Description

`object host.create(object/array hosts)`

This method allows to create new hosts.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` Hosts to create.

Additionally to the [standard host properties](object#host), the method accepts the following parameters.

groups | object/array | [Host groups](/documentation/current/en/manual/api/reference/hostgroup/object) to add the host to.  
  
The host groups must have only the `groupid` property defined.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
---|---|---  
interfaces | object/array | [Interfaces](/documentation/current/en/manual/api/reference/hostinterface/object) to be created for the host.  
tags | object/array | [Host tags](/documentation/current/en/manual/api/reference/host/object#host-tag).  
templates | object/array | [Templates](/documentation/current/en/manual/api/reference/template/object) to be linked to the host.  
  
The templates must have only the `templateid` property defined.  
macros | object/array | [User macros](/documentation/current/en/manual/api/reference/usermacro/object) to be created for the host.  
inventory | object | [Host inventory](/documentation/current/en/manual/api/reference/host/object#host-inventory) properties.  
  
### Return values

`(object)` Returns an object containing the IDs of the created hosts under the `hostids` property. The order of the returned IDs matches the order of the passed hosts.

### Examples

#### Creating a host

Create a host called "Linux server" with an IP interface and tags, add it to a group, link a template to it and set the MAC addresses in the host inventory.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "host.create",
               "params": {
                   "host": "Linux server",
                   "interfaces": [
                       {
                           "type": 1,
                           "main": 1,
                           "useip": 1,
                           "ip": "192.168.3.1",
                           "dns": "",
                           "port": "10050"
                       }
                   ],
                   "groups": [
                       {
                           "groupid": "50"
                       }
                   ],
                   "tags": [
                       {
                           "tag": "host-name",
                           "value": "linux-server"
                       }
                   ],
                   "templates": [
                       {
                           "templateid": "20045"
                       }
                   ],
                   "macros": [
                       {
                           "macro": "{$USER_ID}",
                           "value": "123321"
                       },
                       {
                           "macro": "{$USER_LOCATION}",
                           "value": "0:0:0",
                           "description": "latitude, longitude and altitude coordinates"
                       }
                   ],
                   "inventory_mode": 0,
                   "inventory": {
                       "macaddress_a": "01234",
                       "macaddress_b": "56768"
                   }
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "hostids": [
                       "107819"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Creating a host with SNMP interface

Create a host called "SNMP host" with an SNMPv3 interface with details.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "host.create",
               "params": {
                   "host": "SNMP host",
                   "interfaces": [
                       {
                           "type": 2,
                           "main": 1,
                           "useip": 1,
                           "ip": "127.0.0.1",
                           "dns": "",
                           "port": "161",
                           "details": {
                               "version": 3,
                               "bulk": 0,
                               "securityname": "mysecurityname",
                               "contextname": "",
                               "securitylevel": 1
                           }
                       }
                   ],
                   "groups": [
                       {
                           "groupid": "4"
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
                   "hostids": [
                       "10658"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Creating a host with PSK encryption

Create a host called "PSK host" with PSK encryption configured. Note that the host has to be [pre-configured to use PSK](/documentation/current/en/manual/encryption/using_pre_shared_keys#configuring-psk-for-server-agent-communication-example).

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "host.create",
               "params": {
                   "host": "PSK host",
                   "interfaces": [
                       {
                           "type": 1,
                           "ip": "192.168.3.1",
                           "dns": "",
                           "port": "10050",
                           "useip": 1,
                           "main": 1
                       }
                   ],
                   "groups": [
                       {
                           "groupid": "2"
                       }
                   ],
                   "tls_accept": 2,
                   "tls_connect": 2,
                   "tls_psk_identity": "PSK 001",
                   "tls_psk": "1f87b595725ac58dd977beef14b97461a7c1045b9a1c963065002c5473194952"
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "hostids": [
                       "10590"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Creating a host monitored by a proxy

Create a host that will be monitored by proxy with ID "1".

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "host.create",
               "params": {
                   "host": "Host monitored by proxy",
                   "groups": [
                       {
                           "groupid": "2"
                       }
                   ],
                   "monitored_by": 1,
                   "proxyid": 1
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "hostids": [
                       "10591"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Creating a host monitored by a proxy group

Create a host that will be monitored by proxy group with ID "1".

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "host.create",
               "params": {
                   "host": "Host monitored by proxy group",
                   "groups": [
                       {
                           "groupid": "2"
                       }
                   ],
                   "monitored_by": 2,
                   "proxy_groupid": 1
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "hostids": [
                       "10592"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### See also

  * [Host group](/documentation/current/en/manual/api/reference/hostgroup/object#host-group)
  * [Template](/documentation/current/en/manual/api/reference/template/object#template)
  * [User macro](/documentation/current/en/manual/api/reference/usermacro/object#hosttemplate-level-macro)
  * [Host interface](/documentation/current/en/manual/api/reference/hostinterface/object#host-interface)
  * [Host inventory](object#host-inventory)
  * [Host tag](object#host-tag)
  * [Proxy](/documentation/current/en/manual/api/reference/proxy/object#proxy)
  * [Proxy group](/documentation/current/en/manual/api/reference/proxygroup/object#proxy-group)

### Source

CHost::create() in _ui/include/classes/api/services/CHost.php_.