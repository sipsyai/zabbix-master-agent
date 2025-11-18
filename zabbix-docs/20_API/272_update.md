---
title: service.update
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/service/update
downloaded: 2025-11-14 10:44:25
---

# service.update

### Description

`object service.update(object/array services)`

This method allows to update existing services.

This method is available to users of any type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` service properties to be updated.

The `serviceid` property must be defined for each service, all other properties are optional. Only the passed properties will be updated, all others will remain unchanged.

Additionally to the [standard service properties](object#service), the method accepts the following parameters.

children | array | Child [services](/documentation/current/en/manual/api/reference/service/object#service) to replace the current child services.  
  
The child services must have only the `serviceid` property defined.  
---|---|---  
parents | array | Parent [services](/documentation/current/en/manual/api/reference/service/object#service) to replace the current parent services.  
  
The parent services must have only the `serviceid` property defined.  
tags | array | [Service tags](/documentation/current/en/manual/api/reference/service/object#service-tag) to replace the current service tags.  
problem_tags | array | [Problem tags](/documentation/current/en/manual/api/reference/service/object#problem-tag) to replace the current problem tags.  
status_rules | array | [Status rules](/documentation/current/en/manual/api/reference/service/object#status-rule) to replace the current status rules.  
  
### Return values

`(object)` Returns an object containing the IDs of the updated services under the `serviceids` property.

### Examples

#### Setting the parent for a service

Make service with ID "3" to be the parent for service with ID "5".

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "service.update",
               "params": {
                   "serviceid": "5",
                   "parents": [
                       {
                           "serviceid": "3"
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
                   "serviceids": [
                       "5"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Adding a scheduled downtime

Add a downtime for service with ID "4" scheduled weekly from Monday 22:00 till Tuesday 10:00.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "service.update",
               "params": {
                   "serviceid": "4",
                   "times": [
                       {
                           "type": "1",
                           "ts_from": "165600",
                           "ts_to": "201600"
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
                   "serviceids": [
                       "4"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CService::update() in _ui/include/classes/api/services/CService.php_.