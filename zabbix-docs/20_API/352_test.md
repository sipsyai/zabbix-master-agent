---
title: userdirectory.test
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/userdirectory/test
downloaded: 2025-11-14 10:45:45
---

# userdirectory.test

### Description

`object userdirectory.test(array userDirectory)`

This method allows to test user directory connection settings.

This method also allows to test what configured data matches the user directory settings for user provisioning (e.g., what user role, user groups, user medias will be assigned to the user). For this type of test the API request should be made for a [user directory](/documentation/current/en/manual/api/reference/userdirectory/object#userdirectory) that has `provision_status` set to enabled.

This method is only available to _Super admin_ user type.

### Parameters

`(object)` User directory properties.

Since `userdirectory.get` API does not return `bind_password` field, `userdirectoryid` and/or `bind_password` should be supplied.  
Additionally to the [standard user directory properties](object#userdirectory), the method accepts the following parameters.

test_username | string | Username to test in user directory.  
---|---|---  
test_password | string | Username associated password to test in user directory.  
  
### Return values

`(bool)` Returns true on success.

### Examples

##### Test user directory for existing user

Test user directory "3" for "user1".

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "userdirectory.test",
               "params": {
                   "userdirectoryid": "3",
                   "host": "127.0.0.1",
                   "port": "389",
                   "base_dn": "ou=Users,dc=example,dc=org",
                   "search_attribute": "uid",
                   "bind_dn": "cn=ldap_search,dc=example,dc=org",
                   "bind_password": "password",
                   "test_username": "user1",
                   "test_password": "password"
               },
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

##### Test user directory for non-existing user

Test user directory "3" for non-existing "user2".

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "userdirectory.test",
               "params": {
                   "userdirectoryid": "3",
                   "host": "127.0.0.1",
                   "port": "389",
                   "base_dn": "ou=Users,dc=example,dc=org",
                   "search_attribute": "uid",
                   "bind_dn": "cn=ldap_search,dc=example,dc=org",
                   "test_username": "user2",
                   "test_password": "password"
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "error": {
                   "code": -32500,
                   "message": "Application error.",
                   "data": "Incorrect user name or password or account is temporarily blocked."
               },
               "id": 1
           }

Copy

✔ Copied

##### Test user directory for user provisioning

Test userdirectory "3" for what configured data matches the user directory settings for "user3" provisioning (e.g., what user role, user groups, user medias will be assigned to the user).

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "userdirectory.test",
               "params": {
                   "userdirectoryid": "2",
                   "host": "host.example.com",
                   "port": "389",
                   "base_dn": "DC=zbx,DC=local",
                   "search_attribute": "sAMAccountName",
                   "bind_dn": "CN=Admin,OU=Users,OU=Zabbix,DC=zbx,DC=local",
                   "test_username": "user3",
                   "test_password": "password"
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "username": "user3",
                   "name": "John",
                   "surname": "Doe",
                   "medias": [],
                   "usrgrps": [
                       {
                           "usrgrpid": "8"
                       },
                       {
                           "usrgrpid": "7"
                       }
                   ],
                   "roleid": "2",
                   "userdirectoryid": "2"
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CUserDirectory::test() in _ui/include/classes/api/services/CUserDirectory.php_.