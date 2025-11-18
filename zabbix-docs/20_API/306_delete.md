---
title: templategroup.delete
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/templategroup/delete
downloaded: 2025-11-14 10:44:59
---

# templategroup.delete

### Description

`object templategroup.delete(array templateGroupIds)`

This method allows to delete template groups.

A template group can not be deleted if it contains templates that belong to this group only.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(array)` IDs of the template groups to delete.

### Return values

`(object)` Returns an object containing the IDs of the deleted template groups under the `groupids` property.

### Examples

#### Deleting multiple template groups

Delete two template groups.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "templategroup.delete",
               "params": [
                   "107814",
                   "107815"
               ],
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "groupids": [
                       "107814",
                       "107815"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CTemplateGroup::delete() in _ui/include/classes/api/services/CTemplateGroup.php_.