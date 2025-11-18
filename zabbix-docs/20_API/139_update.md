---
title: hostgroup.update
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/hostgroup/update
downloaded: 2025-11-14 10:42:12
---

# hostgroup.update

### Description

`object hostgroup.update(object/array hostGroups)`

This method allows to update existing hosts groups.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` [Host group properties](object#host-group) to be updated.

The `groupid` property must be defined for each host group, all other properties are optional. Only the given properties will be updated, all others will remain unchanged.

### Return values

`(object)` Returns an object containing the IDs of the updated host groups under the `groupids` property.

### Examples

#### Renaming a host group

Rename a host group to "Linux hosts."

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "hostgroup.update",
               "params": {
                   "groupid": "7",
                   "name": "Linux hosts"
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
                       "7"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CHostGroup::update() in _ui/include/classes/api/services/CHostGroup.php_.