---
title: role.delete
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/role/delete
downloaded: 2025-11-14 10:44:08
---

# role.delete

### Description

`object role.delete(array roleids)`

This method allows to delete roles.

This method is only available to _Super admin_ user type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(array)` IDs of the roles to delete.

### Return values

`(object)` Returns an object containing the IDs of the deleted roles under the `roleids` property.

### Examples

#### Deleting multiple user roles

Delete two user roles.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "role.delete",
               "params": [
                   "4",
                   "5"
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
                       "4",
                       "5"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CRole::delete() in _ui/include/classes/api/services/CRole.php_.