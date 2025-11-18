---
title: templategroup.massupdate
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/templategroup/massupdate
downloaded: 2025-11-14 10:45:03
---

# templategroup.massupdate

### Description

`object templategroup.massupdate(object parameters)`

This method allows to replace templates with the specified ones in multiple template groups.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object)` Parameters containing the IDs of the template groups to update and the objects that should be updated.

groups | object/array | [Template groups](/documentation/current/en/manual/api/reference/templategroup/object#template-group) to be updated.  
  
The template groups must have only the `groupid` property defined.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
---|---|---  
templates | object/array | [Templates](/documentation/current/en/manual/api/reference/template/object#template) to replace the current template on the given template groups.  
All other template, except the ones mentioned, will be excluded from template groups.  
  
The templates must have only the `templateid` property defined.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
  
### Return values

`(object)` Returns an object containing the IDs of the updated template groups under the `groupids` property.

### Examples

#### Replacing templates in a template group

Replace all templates in a template group to ones mentioned templates.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "templategroup.massupdate",
               "params": {
                   "groups": [
                       {
                           "groupid": "8"
                       }
                   ],
                   "templates": [
                       {
                           "templateid": "40050"
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
                       "8",
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### See also

  * [templategroup.update](update)
  * [templategroup.massadd](massadd)
  * [Template](/documentation/current/en/manual/api/reference/template/object#template)

### Source

CTemplateGroup::massUpdate() in _ui/include/classes/api/services/CTemplateGroup.php_.