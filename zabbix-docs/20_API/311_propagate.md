---
title: templategroup.propagate
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/templategroup/propagate
downloaded: 2025-11-14 10:45:04
---

# templategroup.propagate

### Description

`object templategroup.propagate(object parameters)`

This method allows to apply permissions to all template groups' subgroups.

This method is only available to _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object)` Parameters defining the desired output.

The method supports the following parameters.

groups | object/array | [Template groups](/documentation/current/en/manual/api/reference/templategroup/object#template-group) to propagate.  
  
The template groups must have only the `groupid` property defined.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
---|---|---  
permissions | boolean | Set `true` if need to propagate permissions.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
  
### Return values

`(object)` Returns an object containing the IDs of the propagated template groups under the `groupids` property.

### Examples

#### Propagating template group permissions to its subgroups.

Propagate template group permissions to its subgroups.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "templategroup.propagate",
               "params": {
                   "groups": [
                       {
                           "groupid": "15"
                       }
                   ],
                   "permissions": true
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
                       "15",
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

CTemplateGroup::propagate() in _ui/include/classes/api/services/CTemplateGroup.php_.