---
title: mfa.delete
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/mfa/delete
downloaded: 2025-11-14 10:43:30
---

# mfa.delete

### Description

`object mfa.delete(array mfaids)`

This method allows to delete MFA methods.

This method is only available to _Super admin_ user type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(array)` IDs of the MFA methods to delete.

### Return values

`(object)` Returns an object containing the IDs of the deleted MFA methods under the `mfaids` property.

### Examples

#### Deleting MFA methods

Delete an MFA method.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "mfa.delete",
               "params": [
                   "2"
               ],
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "mfaids": [
                       "2"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CMfa::delete() in _ui/include/classes/api/services/CMfa.php_.