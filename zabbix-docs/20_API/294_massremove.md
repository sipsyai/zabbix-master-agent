---
title: template.massremove
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/template/massremove
downloaded: 2025-11-14 10:44:47
---

# template.massremove

### Description

`object template.massremove(object parameters)`

This method allows to remove related objects from multiple templates.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object)` Parameters containing the IDs of the templates to update and the objects that should be removed.

templateids | ID/array | IDs of the [templates](/documentation/current/en/manual/api/reference/template/object#template) to be updated.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
---|---|---  
groupids | ID/array | IDs of the [template groups](/documentation/current/en/manual/api/reference/templategroup/object) from which to remove the given templates.  
macros | string/array | IDs of the [user macros](/documentation/current/en/manual/api/reference/usermacro/object) to delete from the given templates.  
templateids_clear | ID/array | IDs of the [templates](/documentation/current/en/manual/api/reference/template/object) to unlink and clear from the given templates (upstream).  
templateids_link | ID/array | IDs of the [templates](/documentation/current/en/manual/api/reference/template/object) to unlink from the given templates (upstream).  
  
### Return values

`(object)` Returns an object containing the IDs of the updated templates under the `templateids` property.

### Examples

#### Removing templates from a group

Remove two templates from group "2".

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "template.massremove",
               "params": {
                   "templateids": [
                       "10085",
                       "10086"
                   ],
                   "groupids": "2"
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

#### Unlinking templates from a host

Unlink templates "10106" and "10104" from template "10085".

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "template.massremove",
               "params": {
                   "templateids": "10085",
                   "templateids_link": [
                       "10106",
                       "10104"
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
                       "10085"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### See also

  * [template.update](update)
  * [User macro](/documentation/current/en/manual/api/reference/usermacro/object#hosttemplate-level-macro)

### Source

CTemplate::massRemove() in _ui/include/classes/api/services/CTemplate.php_.