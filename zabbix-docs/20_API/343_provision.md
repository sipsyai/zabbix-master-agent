---
title: user.provision
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/user/provision
downloaded: 2025-11-14 10:45:36
---

# user.provision

### Description

`object user.provision(object/array users)`

This method allows to provision LDAP users.

This method is only available to _Super admin_ user type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(array)` IDs of users to provision.

### Return values

`(object)` Returns an object containing the IDs of the provisioned users under the `userids` property.

### Examples

#### Provisioning multiple users

Provision two users.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "user.provision",
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

CUser::provision() in _ui/include/classes/api/services/CUser.php_.