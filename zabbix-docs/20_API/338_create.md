---
title: user.create
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/user/create
downloaded: 2025-11-14 10:45:31
---

# user.create

### Description

`object user.create(object/array users)`

This method allows to create new users.

This method is only available to _Super admin_ user type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

The strength of user password is validated according the password policy rules defined by Authentication API. See [Authentication API](/documentation/current/en/manual/api/reference/authentication) for more information.

### Parameters

`(object/array)` Users to create.

Additionally to the [standard user properties](object#user), the method accepts the following parameters.

usrgrps | array | [User groups](/documentation/current/en/manual/api/reference/usergroup/object#user-group) to add the user to.  
  
The user groups must have only the `usrgrpid` property defined.  
---|---|---  
medias | array | [User media](/documentation/current/en/manual/api/reference/user/object#media) to be created.  
  
### Return values

`(object)` Returns an object containing the IDs of the created users under the `userids` property. The order of the returned IDs matches the order of the passed users.

### Examples

#### Creating a user

Create a new user, add him to a user group and create a new media for him.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "user.create",
               "params": {
                   "username": "John",
                   "passwd": "Doe123",
                   "roleid": "5",
                   "usrgrps": [
                       {
                           "usrgrpid": "7"
                       }
                   ],
                   "medias": [
                       {
                           "mediatypeid": "1",
                           "sendto": [
                               "support@company.com"
                           ],
                           "active": 0,
                           "severity": 63,
                           "period": "1-7,00:00-24:00"
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
  * [Media](/documentation/current/en/manual/api/reference/user/object#media)
  * [User group](/documentation/current/en/manual/api/reference/usergroup/object#user-group)
  * [Role](/documentation/current/en/manual/api/reference/role/object#role)

### Source

CUser::create() in _ui/include/classes/api/services/CUser.php_.