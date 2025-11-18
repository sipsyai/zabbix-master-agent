---
title: role.update
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/role/update
downloaded: 2025-11-14 10:44:10
---

# role.update

### Description

`object role.update(object/array roles)`

This method allows to update existing roles.

This method is only available to _Super admin_ user type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` Role properties to be updated.

The `roleid` property must be defined for each role, all other properties are optional. Only the passed properties will be updated, all others will remain unchanged.

Additionally to the [standard role properties](object#role) the method accepts the following parameters.

rules | array | Access [rules](object#role-rules) to update for the role.  
---|---|---  
  
### Return values

`(object)` Returns an object containing the IDs of the updated roles under the `roleids` property.

### Examples

#### Disabling ability to execute scripts

Update role with ID "5", disable ability to execute scripts.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "role.update",
               "params": [
                   {
                       "roleid": "5",
                       "rules": {
                           "actions": [
                               {
                                   "name": "execute_scripts",
                                   "status": "0"
                               }
                           ]
                       }
                   }
               ],
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

#### Limiting access to API

Update role with ID "5", deny to call any "create", "update" or "delete" methods.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "role.update",
               "params": [
                   {
                       "roleid": "5",
                       "rules": {
                           "api.access": "1",
                           "api.mode": "0",
                           "api": ["*.create", "*.update", "*.delete"]
                       }
                   }
               ],
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

### Source

CRole::update() in _ui/include/classes/api/services/CRole.php_.