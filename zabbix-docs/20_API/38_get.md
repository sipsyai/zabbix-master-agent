---
title: correlation.get
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/correlation/get
downloaded: 2025-11-14 10:40:31
---

# correlation.get

### Description

`integer/array correlation.get(object parameters)`

The method allows to retrieve correlations according to the given parameters.

This method is available to users of any type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object)` Parameters defining the desired output.

The method supports the following parameters.

correlationids | ID/array | Return only correlations with the given IDs.  
---|---|---  
selectFilter | query | Return a [`filter`](/documentation/current/en/manual/api/reference/correlation/object#correlation-filter) property with the correlation conditions.  
selectOperations | query | Return an [`operations`](/documentation/current/en/manual/api/reference/correlation/object#correlation-operation) property with the correlation operations.  
sortfield | string/array | Sort the result by the given properties.  
  
Possible values: `correlationid`, `name`, `status`.  
countOutput | boolean | These parameters are described in the [reference commentary](/documentation/current/en/manual/api/reference_commentary#common-get-method-parameters).  
editable | boolean  
excludeSearch | boolean  
filter | object  
limit | integer  
output | query  
preservekeys | boolean  
search | object  
searchByAny | boolean  
searchWildcardsEnabled | boolean  
sortorder | string/array  
startSearch | boolean  
  
### Return values

`(integer/array)` Returns either:

  * an array of objects;
  * the count of retrieved objects, if the `countOutput` parameter has been used.

### Examples

#### Retrieve correlations

Retrieve all configured correlations together with correlation conditions and operations. The filter uses the "and/or" evaluation type, so the `formula` property is empty and `eval_formula` is generated automatically.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "correlation.get",
               "params": {
                   "output": "extend",
                   "selectOperations": "extend",
                   "selectFilter": "extend"
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": [
                   {
                       "correlationid": "1",
                       "name": "Correlation 1",
                       "description": "",
                       "status": "0",
                       "filter": {
                           "evaltype": "0",
                           "formula": "",
                           "conditions": [
                               {
                                   "type": "3",
                                   "oldtag": "error",
                                   "newtag": "ok",
                                   "formulaid": "A"
                               }
                           ],
                           "eval_formula": "A"
                       },
                       "operations": [
                           {
                               "type": "0"
                           }
                       ]
                   }
               ],
               "id": 1
           }

Copy

✔ Copied

### See also

  * [Correlation filter](object#correlation-filter)
  * [Correlation operation](object#correlation-operation)

### Source

CCorrelation::get() in _ui/include/classes/api/services/CCorrelation.php_.