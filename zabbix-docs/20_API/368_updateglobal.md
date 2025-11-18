---
title: usermacro.updateglobal
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/usermacro/updateglobal
downloaded: 2025-11-14 10:46:01
---

# usermacro.updateglobal

### Description

`object usermacro.updateglobal(object/array globalMacros)`

This method allows to update existing global macros.

This method is only available to _Super admin_ user type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` [Global macro properties](object#global-macro) to be updated.

The `globalmacroid` property must be defined for each global macro, all other properties are optional. Only the passed properties will be updated, all others will remain unchanged.

### Return values

`(object)` Returns an object containing the IDs of the updated global macros under the `globalmacroids` property.

### Examples

#### Changing the value of a global macro

Change the value of a global macro to "public".

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "usermacro.updateglobal",
               "params": {
                   "globalmacroid": "1",
                   "value": "public"
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "globalmacroids": [
                       "1"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CUserMacro::updateGlobal() in _ui/include/classes/api/services/CUserMacro.php_.