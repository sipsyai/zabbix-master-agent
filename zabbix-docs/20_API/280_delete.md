---
title: sla.delete
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/sla/delete
downloaded: 2025-11-14 10:44:33
---

# sla.delete

### Description

`object sla.delete(array slaids)`

This method allows to delete SLA entries.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(array)` IDs of the SLAs to delete.

### Return values

`(object)` Returns an object containing the IDs of the deleted SLAs under the `slaids` property.

### Examples

#### Deleting multiple SLAs

Delete two SLA entries.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "sla.delete",
               "params": [
                   "4",
                   "5"
               ],
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "slaids": [
                       "4",
                       "5"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CSla::delete() in _ui/include/classes/api/services/CSla.php_.