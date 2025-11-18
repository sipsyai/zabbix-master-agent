---
title: action.delete
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/action/delete
downloaded: 2025-11-14 10:39:59
---

# action.delete

### Description

`object action.delete(array actionIds)`

This method allows to delete actions.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(array)` IDs of the actions to delete.

### Return values

`(object)` Returns an object containing the IDs of the deleted actions under the `actionids` property.

### Examples

#### Delete multiple actions

Delete two actions.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "action.delete",
               "params": [
                   "17",
                   "18"
               ],
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "actionids": [
                       "17",
                       "18"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CAction::delete() in _ui/include/classes/api/services/CAction.php_.