---
title: itemprototype.delete
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/itemprototype/delete
downloaded: 2025-11-14 10:42:53
---

# itemprototype.delete

### Description

`object itemprototype.delete(array itemPrototypeIds)`

This method allows to delete item prototypes.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(array)` IDs of the item prototypes to delete.

### Return values

`(object)` Returns an object containing the IDs of the deleted item prototypes under the `prototypeids` property.

### Examples

#### Deleting multiple item prototypes

Delete two item prototypes.  
Dependent item prototypes are removed automatically if master item or item prototype is deleted.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "itemprototype.delete",
               "params": [
                   "27352",
                   "27356"
               ],
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "prototypeids": [
                       "27352",
                       "27356"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CItemPrototype::delete() in _ui/include/classes/api/services/CItemPrototype.php_.