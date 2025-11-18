---
title: template.massupdate
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/template/massupdate
downloaded: 2025-11-14 10:44:48
---

# template.massupdate

### Description

`object template.massupdate(object parameters)`

This method allows to simultaneously replace or remove related objects and update properties on multiple templates.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object)` Parameters containing the IDs of the templates to update and the objects to replace for the templates.

The method accepts the following parameters.

templates | object/array | [Templates](/documentation/current/en/manual/api/reference/template/object) to be updated.  
  
The templates must have only the `templateid` property defined.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
---|---|---  
groups | object/array | [Template groups](/documentation/current/en/manual/api/reference/templategroup/object) to replace the current template groups the templates belong to.  
  
The template groups must have only the `groupid` property defined.  
macros | object/array | [User macros](/documentation/current/en/manual/api/reference/usermacro/object) to replace all of the current user macros on the given templates.  
templates_clear | object/array | [Templates](/documentation/current/en/manual/api/reference/template/object) to unlink and clear from the given templates.  
  
The templates must have only the `templateid` property defined.  
templates_link | object/array | [Templates](/documentation/current/en/manual/api/reference/template/object) to replace the currently linked templates.  
  
The templates must have only the `templateid` property defined.  
  
### Return values

`(object)` Returns an object containing the IDs of the updated templates under the `templateids` property.

### Examples

#### Unlinking a template

Unlink and clear template "10091" from the given templates.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "template.massupdate",
               "params": {
                   "templates": [
                       {
                           "templateid": "10085"
                       },
                       {
                           "templateid": "10086"
                       }
                   ],
                   "templates_clear": [
                       {
                           "templateid": "10091"
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

#### Replacing user macros

Replace all user macros with the given user macro on multiple templates.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "template.massupdate",
               "params": {
                   "templates": [
                       {
                           "templateid": "10074"
                       },
                       {
                           "templateid": "10075"
                       },
                       {
                           "templateid": "10076"
                       },
                       {
                           "templateid": "10077"
                       }
                   ],
                   "macros": [
                       {
                           "macro": "{$AGENT.TIMEOUT}",
                           "value": "5m",
                           "description": "Timeout after which agent is considered unavailable. Works only for agents reachable from Zabbix server/proxy (passive mode)."
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
                       "10074",
                       "10075",
                       "10076",
                       "10077"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### See also

  * [template.update](update)
  * [template.massadd](massadd)
  * [Template group](/documentation/current/en/manual/api/reference/templategroup/object#template-group)
  * [User macro](/documentation/current/en/manual/api/reference/usermacro/object#hosttemplate-level-macro)

### Source

CTemplate::massUpdate() in _ui/include/classes/api/services/CTemplate.php_.