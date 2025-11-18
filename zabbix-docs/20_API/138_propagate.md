---
title: hostgroup.propagate
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/hostgroup/propagate
downloaded: 2025-11-14 10:42:11
---

# hostgroup.propagate

### Description

`object hostgroup.propagate(object parameters)`

This method allows to apply permissions and tag filters to all subgroups of a host group.

This method is only available to _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object)` Parameters defining the desired output.

The method supports the following parameters.

groups | object/array | [Host groups](/documentation/current/en/manual/api/reference/hostgroup/object) to propagate.  
  
The host groups must have the `groupid` property defined.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
---|---|---  
permissions | boolean | Set to "true" to propagate permissions.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_ if `tag_filters` is not set  
tag_filters | boolean | Set to "true" to propagate tag filters.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_ if `permissions` is not set  
  
### Return values

`(object)` Returns an object containing the IDs of the propagated host groups under the `groupids` property.

### Examples

#### Propagating host group permissions and tag filters to its subgroups.

Propagate host group permissions and tag filters to its subgroups.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "hostgroup.propagate",
               "params": {
                   "groups": [
                       {
                           "groupid": "6"
                       }
                   ],
                   "permissions": true,
                   "tag_filters": true
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

CHostGroup::propagate() in _ui/include/classes/api/services/CHostGroup.php_.