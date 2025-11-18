---
title: host.massupdate
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/host/massupdate
downloaded: 2025-11-14 10:42:02
---

# host.massupdate

### Description

`object host.massupdate(object parameters)`

This method allows to simultaneously replace or remove related objects and update properties on multiple hosts.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object)` Parameters containing the IDs of the hosts to update and the properties that should be updated.

Additionally to the [standard host properties](object#host), the method accepts the following parameters.

hosts | object/array | [Hosts](/documentation/current/en/manual/api/reference/host/object) to be updated.  
  
The hosts must have only the `hostid` property defined.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
---|---|---  
groups | object/array | [Host groups](/documentation/current/en/manual/api/reference/hostgroup/object) to replace the current host groups the hosts belong to.  
  
The host groups must have only the `groupid` property defined.  
interfaces | object/array | [Host interfaces](/documentation/current/en/manual/api/reference/hostinterface/object) to replace the current host interfaces on the given hosts.  
inventory | object | [Host inventory](/documentation/current/en/manual/api/reference/host/object#host-inventory) properties.  
  
Host inventory mode cannot be updated using the `inventory` parameter, use `inventory_mode` instead.  
macros | object/array | [User macros](/documentation/current/en/manual/api/reference/usermacro/object) to replace the current user macros on the given hosts.  
templates | object/array | [Templates](/documentation/current/en/manual/api/reference/template/object) to replace the currently linked templates on the given hosts.  
  
The templates must have only the `templateid` property defined.  
templates_clear | object/array | [Templates](/documentation/current/en/manual/api/reference/template/object) to unlink and clear from the given hosts.  
  
The templates must have only the `templateid` property defined.  
  
### Return values

`(object)` Returns an object containing the IDs of the updated hosts under the `hostids` property.

### Examples

#### Enabling multiple hosts

Enable monitoring of two hosts, that is, set their status to "0".

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "host.massupdate",
               "params": {
                   "hosts": [
                       {
                           "hostid": "69665"
                       },
                       {
                           "hostid": "69666"
                       }
                   ],
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
                       "69665",
                       "69666"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### See also

  * [host.update](update)
  * [host.massadd](massadd)
  * [host.massremove](massremove)
  * [Host group](/documentation/current/en/manual/api/reference/hostgroup/object#host-group)
  * [Template](/documentation/current/en/manual/api/reference/template/object#host-group)
  * [User macro](/documentation/current/en/manual/api/reference/usermacro/object#hosttemplate-level-macro)
  * [Host interface](/documentation/current/en/manual/api/reference/hostinterface/object#host-interface)

### Source

CHost::massUpdate() in _ui/include/classes/api/services/CHost.php_.