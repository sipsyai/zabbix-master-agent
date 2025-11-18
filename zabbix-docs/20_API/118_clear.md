---
title: history.clear
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/history/clear
downloaded: 2025-11-14 10:41:52
---

# history.clear  
  
### Description

`object history.clear(array itemids)`

This method allows to clear item history.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(array)` IDs of items to clear.

### Return values

`(object)` Returns an object containing the IDs of the cleared items under the `itemids` property.

### Examples

#### Clear history

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "history.clear",
               "params": [
                   "10325",
                   "13205"
               ],
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "itemids": [
                       "10325",
                       "13205"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CHistory::clear() in _ui/include/classes/api/services/CHistory.php_.