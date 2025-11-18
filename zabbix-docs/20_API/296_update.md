---
title: template.update
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/template/update
downloaded: 2025-11-14 10:44:49
---

# template.update

### Description

`object template.update(object/array templates)`

This method allows to update existing templates.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` Template properties to be updated.

The `templateid` property must be defined for each template, all other properties are optional. Only the given properties will be updated, all others will remain unchanged.

Additionally to the [standard template properties](object#template), the method accepts the following parameters.

groups | object/array | [Template groups](/documentation/current/en/manual/api/reference/templategroup/object) to replace the current template groups the templates belong to.  
  
The template groups must have only the `groupid` property defined.  
---|---|---  
tags | object/array | [Template tags](/documentation/current/en/manual/api/reference/template/object#template-tag) to replace the current template tags.  
macros | object/array | [User macros](/documentation/current/en/manual/api/reference/usermacro/object) to replace the current user macros on the given templates.  
templates | object/array | [Templates](/documentation/current/en/manual/api/reference/template/object) to replace the currently linked templates. Templates that are not passed are only unlinked.  
  
The templates must have only the `templateid` property defined.  
templates_clear | object/array | [Templates](/documentation/current/en/manual/api/reference/template/object) to unlink and clear from the given templates.  
  
The templates must have only the `templateid` property defined.  
  
### Return values

`(object)` Returns an object containing the IDs of the updated templates under the `templateids` property.

### Examples

#### Changing the standard template properties

Change the technical name of the template to "Linux by Zabbix agent Custom", the visible name to "My template", and update the template description.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "template.update",
               "params": {
                   "templateid": "10086",
                   "host": "Linux by Zabbix agent Custom",
                   "name": "My template",
                   "description": "This is a custom Linux template."
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
                       "10086"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Updating template groups

Replace all template groups for the given template with a different one.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "template.update",
               "params": {
                   "templateid": "10086",
                   "groups": [
                       {
                           "groupid": "24"
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
                       "10086"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Updating template tags

Replace all template tags with a different one.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "template.update",
               "params": {
                   "templateid": "10086",
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
                       "10086"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Updating template macros

Replace all template macros with a different one.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "template.update",
               "params": {
                   "templateid": "10086",
                   "macros": [
                       {
                           "macro": "{$MY_MACRO}",
                           "value": "new_value"
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
                       "10086"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Updating template linked templates

Unlink (without clearing) all templates from the given template and link a different one to it.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "template.update",
               "params": {
                   "templateid": "10086",
                   "templates": [
                       {
                           "templateid": "10087"
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
                       "10086"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Clearing template linked templates

Unlink and clear the given template from a specific linked template.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "template.update",
               "params": {
                   "templateid": "10086",
                   "templates_clear": [
                       {
                           "templateid": "10087"
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
                       "10086"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CTemplate::update() in _ui/include/classes/api/services/CTemplate.php_.