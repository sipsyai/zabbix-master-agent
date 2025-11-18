---
title: hostgroup.massremove
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/hostgroup/massremove
downloaded: 2025-11-14 10:42:09
---

# hostgroup.massremove

### Description

`object hostgroup.massremove(object parameters)`

This method allows to remove related objects from multiple host groups.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object)` Parameters containing the IDs of the host groups to update and the objects that should be removed.

groupids | ID/array | IDs of the host groups to be updated.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
---|---|---  
hostids | ID/array | IDs of the [hosts](/documentation/current/en/manual/api/reference/host/object) to remove from all host groups.  
  
### Return values

`(object)` Returns an object containing the IDs of the updated host groups under the `groupids` property.

### Examples

#### Removing hosts from host groups

Remove two hosts from the given host groups.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "hostgroup.massremove",
               "params": {
                   "groupids": [
                       "5",
                       "6"
                   ],
                   "hostids": [
                       "30050",
                       "30001"
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
                       "5",
                       "6"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CHostGroup::massRemove() in _ui/include/classes/api/services/CHostGroup.php_.