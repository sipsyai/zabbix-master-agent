---
title: action.update
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/action/update
downloaded: 2025-11-14 10:40:01
---

# action.update

### Description

`object action.update(object/array actions)`

This method allows to update existing actions.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` Action properties to be updated.

The `actionid` property must be defined for each action, all other properties are optional. Only the passed properties will be updated, all others will remain unchanged.

Additionally to the [standard action properties](object#action), the method accepts the following parameters.

filter | object | [Action filter](/documentation/current/en/manual/api/reference/action/object#action-filter) object to replace the current filter.  
---|---|---  
operations | array | [Action operations](/documentation/current/en/manual/api/reference/action/object#action-operation) to replace existing operations.  
recovery_operations | array | [Action recovery operations](/documentation/current/en/manual/api/reference/action/object#action-recovery-operation) to replace existing recovery operations.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if `eventsource` of [Action object](/documentation/current/en/manual/api/reference/action/object#action) is set to "event created by a trigger", "internal event", or "event created on service status update"  
update_operations | array | [Action update operations](/documentation/current/en/manual/api/reference/action/object#action-update-operation) to replace existing update operations.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if `eventsource` of [Action object](/documentation/current/en/manual/api/reference/action/object#action) is set to "event created by a trigger" or "event created on service status update"  
  
### Return values

`(object)` Returns an object containing the IDs of the updated actions under the `actionids` property.

### Examples

#### Disable action

Disable an action, that is, set its status to "1".

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "action.update",
               "params": {
                   "actionid": "2",
                   "status": "1"
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "actionids": [
                       "2"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### See also

  * [Action filter](object#action-filter)
  * [Action operation](object#action-operation)

### Source

CAction::update() in _ui/include/classes/api/services/CAction.php_.