---
title: templategroup.update
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/templategroup/update
downloaded: 2025-11-14 10:45:05
---

# templategroup.update

### Description

`object templategroup.update(object/array templateGroups)`

This method allows to update existing template groups.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` [Template group properties](object#template-group) to be updated.

The `groupid` property must be defined for each template group, all other properties are optional. Only the given properties will be updated, all others will remain unchanged.

### Return values

`(object)` Returns an object containing the IDs of the updated template groups under the `groupids` property.

### Examples

#### Renaming a template group

Rename a template group to "Templates/Databases"

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "templategroup.update",
               "params": {
                   "groupid": "7",
                   "name": "Templates/Databases"
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "groupids": [
                       "7"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CTemplateGroup::update() in _ui/include/classes/api/services/CTemplateGroup.php_.