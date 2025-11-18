---
title: service.create
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/service/create
downloaded: 2025-11-14 10:44:22
---

# service.create  
  
### Description

`object service.create(object/array services)`

This method allows to create new services.

This method is available to users of any type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` services to create.

Additionally to the [standard service properties](object#service), the method accepts the following parameters.

children | array | Child [services](/documentation/current/en/manual/api/reference/service/object#service) to be linked to the service.  
  
The child services must have only the `serviceid` property defined.  
---|---|---  
parents | array | Parent [services](/documentation/current/en/manual/api/reference/service/object#service) to be linked to the service.  
  
The parent services must have only the `serviceid` property defined.  
tags | array | [Service tags](/documentation/current/en/manual/api/reference/service/object#service-tag) to be created for the service.  
problem_tags | array | [Problem tags](/documentation/current/en/manual/api/reference/service/object#problem-tag) to be created for the service.  
status_rules | array | [Status rules](/documentation/current/en/manual/api/reference/service/object#status-rule) to be created for the service.  
  
### Return values

`(object)` Returns an object containing the IDs of the created services under the `serviceids` property. The order of the returned IDs matches the order of the passed services.

### Examples

#### Creating a service

Create a service that will be switched to problem state, if at least one child has a problem.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "service.create",
               "params": {
                   "name": "Server 1",
                   "algorithm": 1,
                   "sortorder": 1
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

### Source

CService::create() in _ui/include/classes/api/services/CService.php_.