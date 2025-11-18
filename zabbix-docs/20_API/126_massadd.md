---
title: host.massadd
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/host/massadd
downloaded: 2025-11-14 10:42:00
---

# host.massadd

### Description

`object host.massadd(object parameters)`

This method allows to simultaneously add multiple related objects to all the given hosts.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object)` Parameters containing the IDs of the hosts to update and the objects to add to all the hosts.

The method accepts the following parameters.

hosts | object/array | [Hosts](/documentation/current/en/manual/api/reference/host/object) to be updated.  
  
The hosts must have only the `hostid` property defined.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
---|---|---  
groups | object/array | [Host groups](/documentation/current/en/manual/api/reference/hostgroup/object) to add to the given hosts.  
  
The host groups must have only the `groupid` property defined.  
interfaces | object/array | [Host interfaces](/documentation/current/en/manual/api/reference/hostinterface/object) to be created for the given hosts.  
macros | object/array | [User macros](/documentation/current/en/manual/api/reference/usermacro/object) to be created for the given hosts.  
templates | object/array | [Templates](/documentation/current/en/manual/api/reference/template/object) to link to the given hosts.  
  
The templates must have only the `templateid` property defined.  
  
### Return values

`(object)` Returns an object containing the IDs of the updated hosts under the `hostids` property.

### Examples

#### Adding macros

Add two new macros to two hosts.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "host.massadd",
               "params": {
                   "hosts": [
                       {
                           "hostid": "10160"
                       },
                       {
                           "hostid": "10167"
                       }
                   ],
                   "macros": [
                       {
                           "macro": "{$TEST1}",
                           "value": "MACROTEST1"
                       },
                       {
                           "macro": "{$TEST2}",
                           "value": "MACROTEST2",
                           "description": "Test description"
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
                       "10160",
                       "10167"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### See also

  * [host.update](update)
  * [Host group](/documentation/current/en/manual/api/reference/hostgroup/object#host-group)
  * [Template](/documentation/current/en/manual/api/reference/template/object#template)
  * [User macro](/documentation/current/en/manual/api/reference/usermacro/object#hosttemplate-level-macro)
  * [Host interface](/documentation/current/en/manual/api/reference/hostinterface/object#host-interface)

### Source

CHost::massAdd() in _ui/include/classes/api/services/CHost.php_.