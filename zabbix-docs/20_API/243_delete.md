---
title: regexp.delete
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/regexp/delete
downloaded: 2025-11-14 10:43:56
---

# regexp.delete

### Description

`object regexp.delete(array regexpids)`

This method allows to delete global regular expressions.

This method is only available to _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(array)` IDs of the regular expressions to delete.

### Return values

`(object)` Returns an object containing the IDs of the deleted regular expressions under the `regexpids` property.

### Examples

#### Deleting multiple global regular expressions.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "regexp.delete",
               "params": [
                   "16",
                   "17"
               ],
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "regexpids": [
                       "16",
                       "17"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CRegexp::delete() in _ui/include/classes/api/services/CRegexp.php_.