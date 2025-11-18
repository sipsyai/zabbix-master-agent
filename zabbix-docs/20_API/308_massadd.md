---
title: templategroup.massadd
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/templategroup/massadd
downloaded: 2025-11-14 10:45:01
---

# templategroup.massadd

### Description

`object templategroup.massadd(object parameters)`

This method allows to simultaneously add multiple related objects to all the given template groups.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object)` Parameters containing the IDs of the template groups to update and the objects to add to all the template groups.

The method accepts the following parameters.

groups | object/array | [Template groups](/documentation/current/en/manual/api/reference/templategroup/object#template-group) to be updated.  
  
The template groups must have only the `groupid` property defined.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
---|---|---  
templates | object/array | [Templates](/documentation/current/en/manual/api/reference/template/object#template) to add to all template groups.  
  
The templates must have only the `templateid` property defined.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
  
### Return values

`(object)` Returns an object containing the IDs of the updated template groups under the `groupids` property.

### Examples

#### Adding templates to template groups

Add two templates to template groups with IDs 12 and 13.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "templategroup.massadd",
               "params": {
                   "groups": [
                       {
                           "groupid": "12"
                       },
                       {
                           "groupid": "13"
                       }
                   ],
                   "templates": [
                       {
                           "templateid": "10486"
                       },
                       {
                           "templateid": "10487"
                       }
                   ]
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
                       "12",
                       "13"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### See also

  * [Template](/documentation/current/en/manual/api/reference/template/object#template)

### Source

CTemplateGroup::massAdd() in _ui/include/classes/api/services/CTemplateGroup.php_.