---
title: script.delete
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/script/delete
downloaded: 2025-11-14 10:44:14
---

# script.delete

### Description

`object script.delete(array scriptIds)`

This method allows to delete scripts.

This method is only available to _Super admin_ user type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(array)` IDs of the scripts to delete.

### Return values

`(object)` Returns an object containing the IDs of the deleted scripts under the `scriptids` property.

### Examples

#### Delete multiple scripts

Delete two scripts.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "script.delete",
               "params": [
                   "3",
                   "4"
               ],
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "scriptids": [
                       "3",
                       "4"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CScript::delete() in _ui/include/classes/api/services/CScript.php_.