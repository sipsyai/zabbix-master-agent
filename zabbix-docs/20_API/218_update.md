---
title: mfa.update
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/mfa/update
downloaded: 2025-11-14 10:43:31
---

# mfa.update

### Description

`object mfa.update(object/array MFA methods)`

This method allows to update existing MFA methods.

This method is only available to _Super admin_ user type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` MFA method properties to be updated.

The `mfaid` property must be defined for each item, all other properties are optional. Only the passed properties will be updated, all others will remain unchanged.

The method accepts MFA methods with the [standard MFA method properties](/documentation/current/en/manual/api/reference/mfa/object#mfa).

### Return values

`(object)` Returns an object containing the IDs of the updated MFA methods under the `mfaids` property.

### Examples

#### Updating method properties

Update the hash function for generating TOTP codes and the verification code length for the "Zabbix TOTP" MFA method utilizing time-based one-time passwords (TOTP).

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "mfa.update",
               "params": {
                   "mfaid": "1",
                   "hash_function": 3,
                   "code_length": 8
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "mfaids": [
                       "1"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CMfa::update() in _ui/include/classes/api/services/CMfa.php_.