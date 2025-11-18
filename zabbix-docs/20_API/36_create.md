---
title: correlation.create
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/correlation/create
downloaded: 2025-11-14 10:40:29
---

# correlation.create  
  
### Description

`object correlation.create(object/array correlations)`

This method allows to create new correlations.

This method is only available to _Super admin_ user type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` Correlations to create.

Additionally to the [standard correlation properties](object#correlation), the method accepts the following parameters.

operations | array | [Correlation operations](/documentation/current/en/manual/api/reference/correlation/object#correlation-operation) to create for the correlation.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
---|---|---  
filter | object | [Correlation filter](/documentation/current/en/manual/api/reference/correlation/object#correlation-filter) object for the correlation.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
  
### Return values

`(object)` Returns an object containing the IDs of the created correlations under the `correlationids` property. The order of the returned IDs matches the order of the passed correlations.

### Examples

#### Create a new event tag correlation

Create a correlation using evaluation method `AND/OR` with one condition and one operation. By default the correlation will be enabled.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "correlation.create",
               "params": {
                   "name": "new event tag correlation",
                   "filter": {
                       "evaltype": 0,
                       "conditions": [
                           {
                               "type": 1,
                               "tag": "ok"
                           }
                       ]
                   },
                   "operations": [
                       {
                           "type": 0
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
                   "correlationids": [
                       "1"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Using a custom expression filter

Create a correlation that will use a custom filter condition. The formula IDs "A" or "B" have been chosen arbitrarily. Condition type will be "Host group" with operator "<>".

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "correlation.create",
               "params": {
                   "name": "new host group correlation",
                   "description": "a custom description",
                   "status": 0,
                   "filter": {
                       "evaltype": 3,
                       "formula": "A or B",
                       "conditions": [
                           {
                               "type": 2,
                               "operator": 1,
                               "formulaid": "A"
                           },
                           {
                               "type": 2,
                               "operator": 1,
                               "formulaid": "B"
                           }
                       ]
                   },
                   "operations": [
                       {
                           "type": 1
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
                   "correlationids": [
                       "2"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### See also

  * [Correlation filter](object#correlation-filter)
  * [Correlation operation](object#correlation-operation)

### Source

CCorrelation::create() in _ui/include/classes/api/services/CCorrelation.php_.