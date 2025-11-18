---
title: host.massremove
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/host/massremove
downloaded: 2025-11-14 10:42:01
---

# host.massremove

### Description

`object host.massremove(object parameters)`

This method allows to remove related objects from multiple hosts.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object)` Parameters containing the IDs of the hosts to update and the objects that should be removed.

hostids | ID/array | IDs of the hosts to be updated.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
---|---|---  
groupids | ID/array | IDs of the [host groups](/documentation/current/en/manual/api/reference/hostgroup/object) to remove the given hosts from.  
interfaces | object/array | [Host interfaces](/documentation/current/en/manual/api/reference/hostinterface/object) to remove from the given hosts.  
  
The host interface object must have only the `ip`, `dns` and `port` properties defined.  
macros | string/array | [User macros](/documentation/current/en/manual/api/reference/usermacro/object) to delete from the given hosts.  
templateids | ID/array | IDs of the [templates](/documentation/current/en/manual/api/reference/template/object) to unlink from the given hosts.  
templateids_clear | ID/array | IDs of the [templates](/documentation/current/en/manual/api/reference/template/object) to unlink and clear from the given hosts.  
  
### Return values

`(object)` Returns an object containing the IDs of the updated hosts under the `hostids` property.

### Examples

#### Unlinking templates

Unlink a template from two hosts and delete all of the templated entities.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "host.massremove",
               "params": {
                   "hostids": ["69665", "69666"],
                   "templateids_clear": "325"
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
  * [User macro](/documentation/current/en/manual/api/reference/usermacro/object#hosttemplate-level-macro)
  * [Host interface](/documentation/current/en/manual/api/reference/hostinterface/object#host-interface)

### Source

CHost::massRemove() in _ui/include/classes/api/services/CHost.php_.