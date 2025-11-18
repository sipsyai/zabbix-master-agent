---
title: usergroup.update
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/usergroup/update
downloaded: 2025-11-14 10:45:52
---

# usergroup.update

### Description

`object usergroup.update(object/array userGroups)`

This method allows to update existing user groups.

This method is only available to _Super admin_ user type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` User group properties to be updated.

The `usrgrpid` property must be defined for each user group, all other properties are optional. Only the passed properties will be updated, all others will remain unchanged.

Additionally to the [standard user group properties](object#user-group), the method accepts the following parameters.

hostgroup_rights | object/array | Host group [permissions](/documentation/current/en/manual/api/reference/usergroup/object#permission) to replace the current permissions assigned to the user group.  
---|---|---  
templategroup_rights | object/array | Template group [permissions](/documentation/current/en/manual/api/reference/usergroup/object#permission) to replace the current permissions assigned to the user group.  
tag_filters | array | [Tag-based permissions](/documentation/current/en/manual/api/reference/usergroup/object#tag-based-permission) to replace the current permissions assigned to the user group.  
users | object/array | [Users](/documentation/current/en/manual/api/reference/user/create) to replace the current users assigned to the user group.  
  
The user must have only the `userid` property defined.  
  
### Return values

`(object)` Returns an object containing the IDs of the updated user groups under the `usrgrpids` property.

### Examples

#### Enabling a user group and updating permissions

Enable a user group and provide read-write access for it to host groups "2" and "4".

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "usergroup.update",
               "params": {
                   "usrgrpid": "17",
                   "users_status": "0",
                   "hostgroup_rights": [
                       {
                           "id": "2",
                           "permission": 3
                       },
                       {
                           "id": "4",
                           "permission": 3
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
                   "usrgrpids": [
                       "17"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### See also

  * [Permission](object#permission)

### Source

CUserGroup::update() in _ui/include/classes/api/services/CUserGroup.php_.