---
title: hostgroup.create
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/hostgroup/create
downloaded: 2025-11-14 10:42:06
---

# hostgroup.create  
  
### Description

`object hostgroup.create(object/array hostGroups)`

This method allows to create new host groups.

This method is only available to _Super admin_ user type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` Host groups to create.

The method accepts host groups with the [standard host group properties](object#host-group).

### Return values

`(object)` Returns an object containing the IDs of the created host groups under the `groupids` property. The order of the returned IDs matches the order of the passed host groups.

### Examples

#### Creating a host group

Create a host group called "Linux servers".

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "hostgroup.create",
               "params": {
                   "name": "Linux servers"
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
                       "107819"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CHostGroup::create() in _ui/include/classes/api/services/CHostGroup.php_.