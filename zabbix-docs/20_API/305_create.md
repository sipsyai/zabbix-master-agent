---
title: templategroup.create
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/templategroup/create
downloaded: 2025-11-14 10:44:58
---

# templategroup.create  
  
### Description

`object templategroup.create(object/array templateGroups)`

This method allows to create new template groups.

This method is only available to _Super admin_ user type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` Template groups to create. The method accepts template groups with the [standard template group properties](object#template-group).

### Return values

`(object)` Returns an object containing the IDs of the created template groups under the `groupids` property. The order of the returned IDs matches the order of the passed template groups.

### Examples

#### Creating a template group

Create a template group called "Templates/Databases".

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "templategroup.create",
               "params": {
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
                       "107820"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CTemplateGroup::create() in _ui/include/classes/api/services/CTemplateGroup.php_.