---
title: regexp.create
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/regexp/create
downloaded: 2025-11-14 10:43:55
---

# regexp.create  
  
### Description

`object regexp.create(object/array regularExpressions)`

This method allows to create new global regular expressions.

This method is only available to _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` Regular expressions to create.

Additionally to the [standard properties](object), the method accepts the following parameters.

expressions | array | [Expressions](/documentation/current/en/manual/api/reference/regexp/object#expressions) options.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
---|---|---  
  
### Return values

`(object)` Returns an object containing the IDs of the created regular expressions under the `regexpids` property.

### Examples

#### Creating a new global regular expression.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "regexp.create",
               "params": {
                 "name": "Storage devices for SNMP discovery",
                 "test_string": "/boot",
                 "expressions": [
                   {
                     "expression": "^(Physical memory|Virtual memory|Memory buffers|Cached memory|Swap space)$",
                     "expression_type": "4",
                     "case_sensitive": "1"
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
                   "regexpids": [
                       "16"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CRegexp::create() in _ui/include/classes/api/services/CRegexp.php_.