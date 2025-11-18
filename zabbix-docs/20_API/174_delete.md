---
title: item.delete
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/item/delete
downloaded: 2025-11-14 10:42:47
---

# item.delete

### Description

`object item.delete(array itemIds)`

This method allows to delete items.

Web items cannot be deleted via the Zabbix API.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(array)` IDs of the items to delete.

### Return values

`(object)` Returns an object containing the IDs of the deleted items under the `itemids` property.

### Examples

#### Deleting multiple items

Delete two items.  
Dependent items and item prototypes are removed automatically if master item is deleted.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "item.delete",
               "params": [
                   "22982",
                   "22986"
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
                       "22982",
                       "22986"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CItem::delete() in _ui/include/classes/api/services/CItem.php_.