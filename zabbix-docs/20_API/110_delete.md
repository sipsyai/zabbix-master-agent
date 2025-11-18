---
title: graphprototype.delete
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/graphprototype/delete
downloaded: 2025-11-14 10:41:44
---

# graphprototype.delete

### Description

`object graphprototype.delete(array graphPrototypeIds)`

This method allows to delete graph prototypes.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(array)` IDs of the graph prototypes to delete.

### Return values

`(object)` Returns an object containing the IDs of the deleted graph prototypes under the `graphids` property.

### Examples

#### Deleting multiple graph prototypes

Delete two graph prototypes.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "graphprototype.delete",
               "params": [
                   "652",
                   "653"
               ],
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "graphids": [
                       "652",
                       "653"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CGraphPrototype::delete() in _ui/include/classes/api/services/CGraphPrototype.php_.