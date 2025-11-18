---
title: triggerprototype.delete
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/triggerprototype/delete
downloaded: 2025-11-14 10:45:25
---

# triggerprototype.delete

### Description

`object triggerprototype.delete(array triggerPrototypeIds)`

This method allows to delete trigger prototypes.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(array)` IDs of the trigger prototypes to delete.

### Return values

`(object)` Returns an object containing the IDs of the deleted trigger prototypes under the `triggerids` property.

### Examples

#### Deleting multiple trigger prototypes

Delete two trigger prototypes.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "triggerprototype.delete",
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

CTriggerPrototype::delete() in _ui/include/classes/api/services/CTriggerPrototype.php_.