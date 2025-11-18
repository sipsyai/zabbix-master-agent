---
title: usermacro.update
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/usermacro/update
downloaded: 2025-11-14 10:46:00
---

# usermacro.update

### Description

`object usermacro.update(object/array hostMacros)`

This method allows to update existing host macros.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` [Host macro properties](object#host-macro) to be updated.

The `hostmacroid` property must be defined for each host macro, all other properties are optional. Only the passed properties will be updated, all others will remain unchanged.

### Return values

`(object)` Returns an object containing the IDs of the updated host macros under the `hostmacroids` property.

### Examples

#### Changing the value of a host macro

Change the value of a host macro to "public".

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "usermacro.update",
               "params": {
                   "hostmacroid": "1",
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
                       "1"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Change macro value that was created by discovery rule

Convert discovery rule created "automatic" macro to "manual" and change its value to "new-value".

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "usermacro.update",
               "params": {
                   "hostmacroid": "1",
                   "value": "new-value",
                   "automatic": "0"
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
                       "1"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CUserMacro::update() in _ui/include/classes/api/services/CUserMacro.php_.