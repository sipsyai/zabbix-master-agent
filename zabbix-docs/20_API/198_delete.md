---
title: maintenance.delete
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/maintenance/delete
downloaded: 2025-11-14 10:43:11
---

# maintenance.delete

### Description

`object maintenance.delete(array maintenanceIds)`

This method allows to delete maintenance periods.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(array)` IDs of the maintenance periods to delete.

### Return values

`(object)` Returns an object containing the IDs of the deleted maintenance periods under the `maintenanceids` property.

### Examples

#### Deleting multiple maintenance periods

Delete two maintenance periods.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "maintenance.delete",
               "params": [
                   "3",
                   "1"
               ],
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "maintenanceids": [
                       "3",
                       "1"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CMaintenance::delete() in _ui/include/classes/api/services/CMaintenance.php_.