---
title: user.logout
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/user/logout
downloaded: 2025-11-14 10:45:35
---

# user.logout

### Description

`string/object user.logout(array)`

This method allows to log out of the API and invalidates the current authentication token.

This method is available to users of any type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(array)` The method accepts an empty array.

### Return values

`(boolean)` Returns `true` if the user has been logged out successfully.

### Examples

#### Logging out

Log out from the API.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "user.logout",
               "params": [],
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": true,
               "id": 1
           }

Copy

✔ Copied

### See also

  * [user.login](login)

### Source

CUser::login() in _ui/include/classes/api/services/CUser.php_.