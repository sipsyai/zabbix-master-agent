---
title: usergroup.create
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/usergroup/create
downloaded: 2025-11-14 10:45:49
---

# usergroup.create  
  
### Description

`object usergroup.create(object/array userGroups)`

This method allows to create new user groups.

This method is only available to _Super admin_ user type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` User groups to create.

Additionally to the [standard user group properties](object#user-group), the method accepts the following parameters.

hostgroup_rights | object/array | Host group [permissions](/documentation/current/en/manual/api/reference/usergroup/object#permission) to assign to the user group.  
---|---|---  
templategroup_rights | object/array | Template group [permissions](/documentation/current/en/manual/api/reference/usergroup/object#permission) to assign to the user group.  
tag_filters | array | [Tag-based permissions](/documentation/current/en/manual/api/reference/usergroup/object#tag-based-permission) to assign to the user group.  
users | object/array | [Users](/documentation/current/en/manual/api/reference/user/create) to add to the user group.  
  
The user must have only the `userid` property defined.  
  
### Return values

`(object)` Returns an object containing the IDs of the created user groups under the `usrgrpids` property. The order of the returned IDs matches the order of the passed user groups.

### Examples

#### Creating a user group

Create a user group _Operation managers_ with denied access to host group "2", and add a user to it.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "usergroup.create",
               "params": {
                   "name": "Operation managers",
                   "hostgroup_rights": {
                       "id": "2",
                       "permission": 0
                   },
                   "users": [
                       {
                           "userid": "12"
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
                       "20"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### See also

  * [Permission](object#permission)

### Source

CUserGroup::create() in _ui/include/classes/api/services/CUserGroup.php_.