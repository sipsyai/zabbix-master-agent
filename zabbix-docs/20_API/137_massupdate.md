---
title: hostgroup.massupdate
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/hostgroup/massupdate
downloaded: 2025-11-14 10:42:10
---

# hostgroup.massupdate

### Description

`object hostgroup.massupdate(object parameters)`

This method allows to replace hosts and templates with the specified ones in multiple host groups.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object)` Parameters containing the IDs of the host groups to update and the objects that should be updated.

groups | object/array | [Host groups](/documentation/current/en/manual/api/reference/hostgroup/object) to be updated.  
  
The host groups must have only the `groupid` property defined.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
---|---|---  
hosts | object/array | [Hosts](/documentation/current/en/manual/api/reference/host/object) to replace the current hosts on the given host groups.  
All other hosts, except the ones mentioned, will be excluded from host groups.  
Discovered hosts will not be affected.  
  
The hosts must have only the `hostid` property defined.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
  
### Return values

`(object)` Returns an object containing the IDs of the updated host groups under the `groupids` property.

### Examples

#### Replacing hosts in a host group

Replace all hosts in a host group to ones mentioned host.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "hostgroup.massupdate",
               "params": {
                   "groups": [
                       {
                           "groupid": "6"
                       }
                   ],
                   "hosts": [
                       {
                           "hostid": "30050"
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
                   "groupids": [
                       "6",
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### See also

  * [hostgroup.update](update)
  * [hostgroup.massadd](massadd)
  * [Host](/documentation/current/en/manual/api/reference/host/object#host)

### Source

CHostGroup::massUpdate() in _ui/include/classes/api/services/CHostGroup.php_.