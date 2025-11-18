---
title: templategroup.massremove
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/templategroup/massremove
downloaded: 2025-11-14 10:45:02
---

# templategroup.massremove

### Description

`object templategroup.massremove(object parameters)`

This method allows to remove related objects from multiple template groups.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object)` Parameters containing the IDs of the template groups to update and the objects that should be removed.

groupids | ID/array | IDs of the [template groups](/documentation/current/en/manual/api/reference/templategroup/object#template-group) to be updated.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
---|---|---  
templateids | ID/array | IDs of the [templates](/documentation/current/en/manual/api/reference/template/object#template) to remove from all template groups.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
  
### Return values

`(object)` Returns an object containing the IDs of the updated template groups under the `groupids` property.

### Examples

#### Removing templates from template groups

Remove two templates from the given template groups.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "templategroup.massremove",
               "params": {
                   "groupids": [
                       "5",
                       "6"
                   ],
                   "templateids": [
                       "30050",
                       "30001"
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
                       "5",
                       "6"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CTemplateGroup::massRemove() in _ui/include/classes/api/services/CTemplateGroup.php_.