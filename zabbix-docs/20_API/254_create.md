---
title: role.create
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/role/create
downloaded: 2025-11-14 10:44:07
---

# role.create  
  
### Description

`object role.create(object/array roles)`

This method allows to create new roles.

This method is only available to _Super admin_ user type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` Roles to create.

Additionally to the [standard role properties](object#role), the method accepts the following parameters.

rules | array | [Role rules](object#role-rules) to be created for the role.  
---|---|---  
  
### Return values

`(object)` Returns an object containing the IDs of the created roles under the `roleids` property. The order of the returned IDs matches the order of the passed roles.

### Examples

#### Creating a role

Create a role with type "User" and denied access to two UI elements.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "role.create",
               "params": {
                   "name": "Operator",
                   "type": "1",
                   "rules": {
                       "ui": [
                           {
                               "name": "monitoring.hosts",
                               "status": "0"
                           },
                           {
                               "name": "monitoring.maps",
                               "status": "0"
                           }
                       ]
                   }
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "roleids": [
                       "5"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### See also

  * [Role rules](object#role-rules)
  * [UI element](object#ui-element)
  * [Module](object#module)
  * [Action](object#action)

### Source

CRole::create() in _ui/include/classes/api/services/CRole.php_.