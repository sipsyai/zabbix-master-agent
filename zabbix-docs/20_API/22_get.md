---
title: autoregistration.get
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/autoregistration/get
downloaded: 2025-11-14 10:40:15
---

# autoregistration.get  
  
### Description

`object autoregistration.get(object parameters)`

The method allows to retrieve autoregistration object according to the given parameters.

This method is only available to _Super admin_ user type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object)` Parameters defining the desired output.

The method supports only one parameter.

output | query | This parameter is described in the [reference commentary](/documentation/current/en/manual/api/reference_commentary#common-get-method-parameters).  
---|---|---  
  
### Return values

`(object)` Returns autoregistration object.

### Examples

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
              "jsonrpc": "2.0",
               "method": "autoregistration.get",
               "params": {
                   "output": "extend"
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "tls_accept": "3"
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CAutoregistration::get() in _ui/include/classes/api/services/CAutoregistration.php_.