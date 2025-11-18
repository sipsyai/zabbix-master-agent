---
title: host.update
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/host/update
downloaded: 2025-11-14 10:42:03
---

# host.update

### Description

`object host.update(object/array hosts)`

This method allows to update existing hosts.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` Host properties to be updated.

The `hostid` property must be defined for each host, all other properties are optional. Only the given properties will be updated, all others will remain unchanged.

Note, however, that updating the host technical name will also update the host's visible name (if not given or empty) by the host's technical name value.

Additionally to the [standard host properties](object#host), the method accepts the following parameters.

groups | object/array | [Host groups](/documentation/current/en/manual/api/reference/hostgroup/object#host-group) to replace the current host groups the host belongs to.  
All host groups that are not listed in the request will be unlinked.  
  
The host groups must have only the `groupid` property defined.  
---|---|---  
interfaces | object/array | [Host interfaces](/documentation/current/en/manual/api/reference/hostinterface/object) to replace the current host interfaces.  
All interfaces that are not listed in the request will be removed.  
tags | object/array | [Host tags](/documentation/current/en/manual/api/reference/host/object#host-tag) to replace the current host tags.  
All tags that are not listed in the request will be removed.  
inventory | object | [Host inventory](/documentation/current/en/manual/api/reference/host/object#host-inventory) properties.  
macros | object/array | [User macros](/documentation/current/en/manual/api/reference/usermacro/object) to replace the current user macros.  
All macros that are not listed in the request will be removed.  
templates | object/array | [Templates](/documentation/current/en/manual/api/reference/template/object) to replace the currently linked templates.  
All templates that are not listed in the request will be only unlinked.  
  
The templates must have only the `templateid` property defined.  
templates_clear | object/array | [Templates](/documentation/current/en/manual/api/reference/template/object) to unlink and clear from the host.  
  
The templates must have only the `templateid` property defined.  
  
As opposed to the Zabbix frontend, when `name` (visible host name) is the same as `host` (technical host name), updating `host` via API will not automatically update `name`. Both properties need to be updated explicitly.

### Return values

`(object)` Returns an object containing the IDs of the updated hosts under the `hostids` property.

### Examples

#### Enabling a host

Enable host monitoring, that is, set its status to "0".

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "host.update",
               "params": {
                   "hostid": "10126",
                   "status": 0
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
                       "10126"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Unlinking templates

Unlink and clear two templates from host.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "host.update",
               "params": {
                   "hostid": "10126",
                   "templates_clear": [
                       {
                           "templateid": "10124"
                       },
                       {
                           "templateid": "10125"
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
                       "10126"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Updating host macros

Replace all host macros with two new ones.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "host.update",
               "params": {
                   "hostid": "10126",
                   "macros": [
                       {
                           "macro": "{$PASS}",
                           "value": "password"
                       },
                       {
                           "macro": "{$DISC}",
                           "value": "sda",
                           "description": "Updated description"
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
                       "10126"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Updating host inventory

Change inventory mode and add location

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "host.update",
               "params": {
                   "hostid": "10387",
                   "inventory_mode": 0,
                   "inventory": {
                       "location": "Latvia, Riga"
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
                       "10387"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Updating host tags

Replace all host tags with a new one.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "host.update",
               "params": {
                   "hostid": "10387",
                   "tags": {
                       "tag": "os",
                       "value": "rhel-7"
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
                       "10387"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Updating discovered host macros

Convert discovery rule created "automatic" macro to "manual" and change its value to "new-value".

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "host.update",
               "params": {
                   "hostid": "10387",
                   "macros": {
                       "hostmacroid": "5541",
                       "value": "new-value",
                       "automatic": "0"
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
                       "10387"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Updating host encryption

Update the host "10590" to use PSK encryption only for connections from host to Zabbix server, and change the PSK identity and PSK key. Note that the host has to be [pre-configured to use PSK](/documentation/current/en/manual/encryption/using_pre_shared_keys#configuring-psk-for-server-agent-communication-example).

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "host.update",
               "params": {
                   "hostid": "10590",
                   "tls_connect": 1,
                   "tls_accept": 2,
                   "tls_psk_identity": "PSK 002",
                   "tls_psk": "e560cb0d918d26d31b4f642181f5f570ad89a390931102e5391d08327ba434e9"
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

### See also

  * [host.massadd](massadd)
  * [host.massupdate](massupdate)
  * [host.massremove](massremove)
  * [Host group](/documentation/current/en/manual/api/reference/hostgroup/object#host-group)
  * [Template](/documentation/current/en/manual/api/reference/template/object#template)
  * [User macro](/documentation/current/en/manual/api/reference/usermacro/object#hosttemplate-level-macro)
  * [Host interface](/documentation/current/en/manual/api/reference/hostinterface/object#host-interface)
  * [Host inventory](object#host-inventory)
  * [Host tag](object#host-tag)
  * [Proxy](/documentation/current/en/manual/api/reference/proxy/object#proxy)
  * [Proxy group](/documentation/current/en/manual/api/reference/proxygroup/object#proxy-group)

### Source

CHost::update() in _ui/include/classes/api/services/CHost.php_.