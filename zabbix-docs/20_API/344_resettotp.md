---
title: user.resettotp
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/user/resettotp
downloaded: 2025-11-14 10:45:37
---

# user.resettotp

### Description

`object user.resettotp(object/array users)`

This method allows to reset user TOTP secrets.

This method is only available to _Super admin_ user type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(array)` IDs of users for which to reset TOTP secrets.

User sessions for the specified users will also be deleted (except for the user sending the request).

### Return values

`(object)` Returns an object containing the IDs of the users for which TOTP secrets have been reset, under the `userids` property.

### Examples

#### Resetting TOTP secrets for multiple users

Reset TOTP secrets for two users.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "user.resettotp",
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

### See also

  * [MFA object](/documentation/current/en/manual/api/reference/mfa/object)

### Source

CUser::resettotp() in _ui/include/classes/api/services/CUser.php_.