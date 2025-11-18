---
title: user.delete
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/user/delete
downloaded: 2025-11-14 10:45:32
---

# user.delete

### Description

`object user.delete(array users)`

This method allows to delete users.

This method is only available to _Super admin_ user type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(array)` IDs of users to delete.

### Return values

`(object)` Returns an object containing the IDs of the deleted users under the `userids` property.

### Examples

#### Deleting multiple users

Delete two users.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "user.delete",
               "params": [
                   "1",
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
                   "userids": [
                       "1",
                       "5"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CUser::delete() in _ui/include/classes/api/services/CUser.php_.