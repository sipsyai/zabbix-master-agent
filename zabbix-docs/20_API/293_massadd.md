---
title: template.massadd
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/template/massadd
downloaded: 2025-11-14 10:44:46
---

# template.massadd

### Description

`object template.massadd(object parameters)`

This method allows to simultaneously add multiple related objects to the given templates.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object)` Parameters containing the IDs of the templates to update and the objects to add to the templates.

The method accepts the following parameters.

templates | object/array | [Templates](/documentation/current/en/manual/api/reference/template/object) to be updated.  
  
The templates must have only the `templateid` property defined.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
---|---|---  
groups | object/array | [Template groups](/documentation/current/en/manual/api/reference/templategroup/object) to add the given templates to.  
  
The template groups must have only the `groupid` property defined.  
macros | object/array | [User macros](/documentation/current/en/manual/api/reference/usermacro/object) to be created for the given templates.  
templates_link | object/array | [Templates](/documentation/current/en/manual/api/reference/template/object) to link to the given templates.  
  
The templates must have only the `templateid` property defined.  
  
### Return values

`(object)` Returns an object containing the IDs of the updated templates under the `templateids` property.

### Examples

#### Link a group to templates

Add template group "2" to two templates.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "template.massadd",
               "params": {
                   "templates": [
                       {
                           "templateid": "10085"
                       },
                       {
                           "templateid": "10086"
                       }
                   ],
                   "groups": [
                       {
                           "groupid": "2"
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
                   "templateids": [
                       "10085",
                       "10086"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Link two templates to a template

Link templates "10106" and "10104" to template "10073".

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "template.massadd",
               "params": {
                   "templates": [
                       {
                           "templateid": "10073"
                       }
                   ],
                   "templates_link": [
                       {
                           "templateid": "10106"
                       },
                       {
                           "templateid": "10104"
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
                   "templateids": [
                       "10073"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### See also

  * [template.update](update)
  * [Host](/documentation/current/en/manual/api/reference/host/object#host)
  * [Template group](/documentation/current/en/manual/api/reference/templategroup/object#template-group)
  * [User macro](/documentation/current/en/manual/api/reference/usermacro/object#hosttemplate-level-macro)

### Source

CTemplate::massAdd() in _ui/include/classes/api/services/CTemplate.php_.