---
title: template.create
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/template/create
downloaded: 2025-11-14 10:44:43
---

# template.create  
  
### Description

`object template.create(object/array templates)`

This method allows to create new templates.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` Templates to create.

Additionally to the [standard template properties](object#template), the method accepts the following parameters.

groups | object/array | [Template groups](/documentation/current/en/manual/api/reference/templategroup/object) to add the template to.  
  
The template groups must have only the `groupid` property defined.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
---|---|---  
tags | object/array | [Template tags](/documentation/current/en/manual/api/reference/template/object#template-tag).  
templates | object/array | [Templates](/documentation/current/en/manual/api/reference/template/object) to be linked to the template.  
  
The templates must have only the `templateid` property defined.  
macros | object/array | [User macros](/documentation/current/en/manual/api/reference/usermacro/object) to be created for the template.  
  
### Return values

`(object)` Returns an object containing the IDs of the created templates under the `templateids` property. The order of the returned IDs matches the order of the passed templates.

### Examples

#### Creating a template

Create a template with tags and link two templates to this template.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "template.create",
               "params": {
                   "host": "Linux template",
                   "groups": {
                       "groupid": 1
                   },
                   "templates": [
                       {
                           "templateid": "11115"
                       },
                       {
                           "templateid": "11116"
                       }
                   ],
                   "tags": [
                       {
                           "tag": "host-name",
                           "value": "{HOST.NAME}"
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
                       "11117"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CTemplate::create() in _ui/include/classes/api/services/CTemplate.php_.