---
title: autoregistration.update
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/autoregistration/update
downloaded: 2025-11-14 10:40:16
---

# autoregistration.update

### Description

`object autoregistration.update(object autoregistration)`

This method allows to update existing autoregistration.

This method is only available to _Super admin_ user type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object)` [Autoregistration properties](object#autoregistration) to be updated.

### Return values

`(boolean )` Returns boolean true as result on successful update.

### Examples

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "autoregistration.update",
               "params": {
                   "tls_accept": "3",
                   "tls_psk_identity": "PSK 001",
                   "tls_psk": "11111595725ac58dd977beef14b97461a7c1045b9a1c923453302c5473193478"
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

### Source

CAutoregistration::update() in _ui/include/classes/api/services/CAutoregistration.php_.