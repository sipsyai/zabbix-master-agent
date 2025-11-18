---
title: usermacro.create
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/usermacro/create
downloaded: 2025-11-14 10:45:55
---

# usermacro.create  
  
### Description

`object usermacro.create(object/array hostMacros)`

This method allows to create new host macros.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` Host macros to create.

The method accepts host macros with the [standard host macro properties](object#host-macro).

### Return values

`(object)` Returns an object containing the IDs of the created host macros under the `hostmacroids` property. The order of the returned IDs matches the order of the passed host macros.

### Examples

#### Creating a host macro

Create a host macro "{$SNMP_COMMUNITY}" with the value "public" on host "10198".

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "usermacro.create",
               "params": {
                   "hostid": "10198",
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
                   "hostmacroids": [
                       "11"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CUserMacro::create() in _ui/include/classes/api/services/CUserMacro.php_.