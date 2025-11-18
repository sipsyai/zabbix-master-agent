---
title: usermacro.createglobal
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/usermacro/createglobal
downloaded: 2025-11-14 10:45:56
---

# usermacro.createglobal

### Description

`object usermacro.createglobal(object/array globalMacros)`

This method allows to create new global macros.

This method is only available to _Super admin_ user type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` Global macros to create.

The method accepts global macros with the [standard global macro properties](object#global-macro).

### Return values

`(object)` Returns an object containing the IDs of the created global macros under the `globalmacroids` property. The order of the returned IDs matches the order of the passed global macros.

### Examples

#### Creating a global macro

Create a global macro "{$SNMP_COMMUNITY}" with value "public".

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "usermacro.createglobal",
               "params":  {
                   "macro": "{$SNMP_COMMUNITY}",
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
                       "6"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CUserMacro::createGlobal() in _ui/include/classes/api/services/CUserMacro.php_.