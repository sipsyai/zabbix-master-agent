---
title: hostprototype.delete
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/hostprototype/delete
downloaded: 2025-11-14 10:42:25
---

# hostprototype.delete

### Description

`object hostprototype.delete(array hostPrototypeIds)`

This method allows to delete host prototypes.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(array)` IDs of the host prototypes to delete.

### Return values

`(object)` Returns an object containing the IDs of the deleted host prototypes under the `hostids` property.

### Examples

#### Deleting multiple host prototypes

Delete two host prototypes.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "hostprototype.delete",
               "params": [
                   "10103",
                   "10105"
               ],
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "hostids": [
                       "10103",
                       "10105"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CHostPrototype::delete() in _ui/include/classes/api/services/CHostPrototype.php_.