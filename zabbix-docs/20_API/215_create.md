---
title: mfa.create
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/mfa/create
downloaded: 2025-11-14 10:43:29
---

# mfa.create  
  
### Description

`object mfa.create(object/array MFA methods)`

This method allows to create new MFA methods.

This method is only available to _Super admin_ user type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` MFA methods to create.

The method accepts MFA methods with the [standard MFA method properties](/documentation/current/en/manual/api/reference/mfa/object#mfa).

### Return values

`(object)` Returns an object containing the IDs of the created MFA methods under the `mfaids` property. The order of the returned IDs matches the order of the passed items.

### Examples

#### Creating MFA methods

Create a "Zabbix TOTP" MFA method utilizing time-based one-time passwords (TOTP), with the hash function for generating TOTP codes set to SHA-1 and the verification code length set to 6 digits.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "mfa.create",
               "params": {
                   "type": 1,
                   "name": "Zabbix TOTP",
                   "hash_function": 1,
                   "code_length": 6
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

CMfa::create() in _ui/include/classes/api/services/CMfa.php_.