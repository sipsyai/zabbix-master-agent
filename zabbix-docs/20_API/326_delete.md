---
title: trigger.delete
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/trigger/delete
downloaded: 2025-11-14 10:45:19
---

# trigger.delete

### Description

`object trigger.delete(array triggerIds)`

This method allows to delete triggers.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(array)` IDs of the triggers to delete.

### Return values

`(object)` Returns an object containing the IDs of the deleted triggers under the `triggerids` property.

### Examples

#### Delete multiple triggers

Delete two triggers.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "trigger.delete",
               "params": [
                   "12002",
                   "12003"
               ],
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "triggerids": [
                       "12002",
                       "12003"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CTrigger::delete() in _ui/include/classes/api/services/CTrigger.php_.