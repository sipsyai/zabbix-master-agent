---
title: hostgroup.massadd
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/hostgroup/massadd
downloaded: 2025-11-14 10:42:08
---

# hostgroup.massadd

### Description

`object hostgroup.massadd(object parameters)`

This method allows to simultaneously add multiple related objects to all the given host groups.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object)` Parameters containing the IDs of the host groups to update and the objects to add to all the host groups.

The method accepts the following parameters.

groups | object/array | [Host groups](/documentation/current/en/manual/api/reference/hostgroup/object) to be updated.  
  
The host groups must have only the `groupid` property defined.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
---|---|---  
hosts | object/array | [Hosts](/documentation/current/en/manual/api/reference/host/object) to add to all host groups.  
  
The hosts must have only the `hostid` property defined.  
  
### Return values

`(object)` Returns an object containing the IDs of the updated host groups under the `groupids` property.

### Examples

#### Adding hosts to host groups

Add two hosts to host groups with IDs 5 and 6.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "hostgroup.massadd",
               "params": {
                   "groups": [
                       {
                           "groupid": "5"
                       },
                       {
                           "groupid": "6"
                       }
                   ],
                   "hosts": [
                       {
                           "hostid": "30050"
                       },
                       {
                           "hostid": "30001"
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
                       "5",
                       "6"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### See also

  * [Host](/documentation/current/en/manual/api/reference/host/object#host)

### Source

CHostGroup::massAdd() in _ui/include/classes/api/services/CHostGroup.php_.