---
title: user.update
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/user/update
downloaded: 2025-11-14 10:45:39
---

# user.update

### Description

`object user.update(object/array users)`

This method allows to update existing users.

This method is available to users of any type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

The strength of user password is validated according the password policy rules defined by Authentication API. See [Authentication API](/documentation/current/en/manual/api/reference/authentication) for more information.

### Parameters

`(object/array)` User properties to be updated.

The `userid` property must be defined for each user, all other properties are optional. Only the passed properties will be updated, all others will remain unchanged.

Additionally to the [standard user properties](object#user), the method accepts the following parameters.

current_passwd | string | User's current password.  
  
The value of this parameter can be an empty string if the user is linked to a [user directory](/documentation/current/en/manual/api/reference/userdirectory/object).  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _write-only_  
\- _required_ if `passwd` of [User object](object#user) is set and user changes own user password  
---|---|---  
usrgrps | array | [User groups](/documentation/current/en/manual/api/reference/usergroup/object#user-group) to replace existing user groups.  
  
The user groups must have only the `usrgrpid` property defined.  
medias | array | [User media](/documentation/current/en/manual/api/reference/user/object#media) to replace existing, non-provisioned media. Provisioned media can be omitted when updating media.  
  
### Return values

`(object)` Returns an object containing the IDs of the updated users under the `userids` property.

### Examples

#### Renaming a user

Rename a user to John Doe.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "user.update",
               "params": {
                   "userid": "1",
                   "name": "John",
                   "surname": "Doe"
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "userids": [
                       "1"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Changing user role

Change a role of a user.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "user.update",
               "params": {
                   "userid": "12",
                   "roleid": "6"
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "userids": [
                       "12"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### See also

  * [Authentication](/documentation/current/en/manual/api/reference/authentication)

### Source

CUser::update() in _ui/include/classes/api/services/CUser.php_.