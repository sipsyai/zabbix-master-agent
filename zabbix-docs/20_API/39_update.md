---
title: correlation.update
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/correlation/update
downloaded: 2025-11-14 10:40:32
---

# correlation.update

### Description

`object correlation.update(object/array correlations)`

This method allows to update existing correlations.

This method is only available to _Super admin_ user type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` Correlation properties to be updated.

The `correlationid` property must be defined for each correlation, all other properties are optional. Only the passed properties will be updated, all others will remain unchanged.

Additionally to the [standard correlation properties](object#correlation), the method accepts the following parameters.

filter | object | [Correlation filter](/documentation/current/en/manual/api/reference/correlation/object#correlation-filter) object to replace the current filter.  
---|---|---  
operations | array | [Correlation operations](/documentation/current/en/manual/api/reference/correlation/object#correlation-operation) to replace existing operations.  
  
### Return values

`(object)` Returns an object containing the IDs of the updated correlations under the `correlationids` property.

### Examples

#### Disable correlation

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "correlation.update",
               "params": {
                   "correlationid": "1",
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
                   "correlationids": [
                       "1"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Replace conditions, but keep the evaluation method

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "correlation.update",
               "params": {
                   "correlationid": "1",
                   "filter": {
                       "conditions": [
                           {
                               "type": 3,
                               "oldtag": "error",
                               "newtag": "ok"
                           }
                       ]
                   }
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

### See also

  * [Correlation filter](object#correlation-filter)
  * [Correlation operation](object#correlation-operation)

### Source

CCorrelation::update() in _ui/include/classes/api/services/CCorrelation.php_.