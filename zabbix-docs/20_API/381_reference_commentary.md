---
title: Appendix 1. Reference commentary
source: https://www.zabbix.com/documentation/current/en/manual/api/reference_commentary
downloaded: 2025-11-14 10:46:14
---

# Appendix 1. Reference commentary

### Notation

#### Data types

The Zabbix API supports the following data types as input:

ID | A unique identifier used to reference an entity.  
---|---  
boolean | A boolean value (either `true` or `false`).  
flag | A value that is considered to be `true` if passed and not equal to `null`; otherwise, the value is considered to be `false`.  
integer | A whole number.  
float | A floating point number.  
string | A text string.  
text | A longer text string.  
timestamp | A Unix timestamp.  
array | An ordered sequence of values (a plain array).  
object | An associative array.  
query | A value that defines the data to be returned. The value can be defined as an array of property names (to return only specific properties), or as one of the predefined values:  
`extend` \- returns all object properties;  
`count` \- returns the number of retrieved records, supported only by certain subselects.  
  
Zabbix API always returns values as strings or arrays only.

#### Property behavior

Some of the object properties are marked with short labels to describe their behavior. The following labels are used:

  * **_read-only_** \- the value of the property is set automatically and cannot be defined or changed by the user, even in some specific conditions (e.g., _read-only_ for inherited objects or discovered objects);
  * **_write-only_** \- the value of the property can be set, but cannot be accessed after;
  * **_constant_** \- the value of the property can be set when creating an object, but cannot be changed after;
  * **_supported_** \- the value of the property is not required to be set, but is allowed to be set in some specific conditions (e.g., _supported_ if `type` is set to "Simple check", "External check", "SSH agent", "TELNET agent", or "HTTP agent"); note, however, that _supported_ properties may still be set to their default values regardless of conditions;
  * **_required_** \- the value of the property is required to be set for all operations (except get operations) or in some specific conditions (e.g., _required_ for create operations; _required_ if `operationtype` is set to "global script" and `opcommand_hst` is not set).

For update operations, a property is considered as "set" when setting it during the update operation.

Properties that are not marked with labels are optional.

#### Parameter behavior

Some of the operation parameters are marked with short labels to describe their behavior for the operation. The following labels are used:

  * **_read-only_** \- the value of the parameter is set automatically and cannot be defined or changed by the user, even in some specific conditions (e.g., _read-only_ for inherited objects or discovered objects);
  * **_write-only_** \- the value of the parameter can be set, but cannot be accessed after;
  * **_supported_** \- the value of the parameter is not required to be set, but is allowed to be set in some specific conditions (e.g., _supported_ if `operating_mode` of Proxy object is set to "passive proxy"); note, however, that _supported_ parameters may still be set to their default values regardless of conditions;
  * **_required_** \- the value of the parameter is required to be set.

Parameters that are not marked with labels are optional.

### Reserved ID value "0"

Reserved ID value "0" can be used to filter elements and to remove referenced objects. For example, to remove a referenced proxy from a host, proxyid should be set to 0 ("proxyid": "0") or to filter hosts monitored by server option proxyids should be set to 0 ("proxyids": "0").

### Common "get" method parameters

The following parameters are supported by all `get` methods:

countOutput | boolean | Return the number of records in the result instead of the actual data.  
---|---|---  
editable | boolean | If set to `true`, return only objects that the user has write permissions to.  
  
Default: `false`.  
excludeSearch | boolean | Return results that do not match the criteria given in the `search` parameter.  
filter | object | Return only those results that exactly match the given filter.  
  
Accepts an object, where the keys are property names (e.g., Host object properties in `host.get`, Item object properties in `item.get`, etc.), and the values are either a single value or an array of values to match against.  
  
Does not support properties of `text` data type.  
  
Note that some methods have specific functionality for this parameter, which is described on the method page (e.g., the `filter` parameter in [host.get](/documentation/current/en/manual/api/reference/host/get) also supports Host interface properties).  
limit | integer | Limit the number of records returned.  
output | query | Object properties to be returned.  
  
Default: `extend`.  
preservekeys | boolean | Use IDs as keys in the resulting array.  
search | object | Return results that match the given pattern (case-insensitive).  
  
Accepts an object, where the keys are property names (e.g., Host object properties in `host.get`, Item object properties in `item.get`, etc.), and the values are strings to search for. If no additional options are given, this will perform a `LIKE "%…%"` search.  
  
Supports only properties of `string` and `text` data type.  
  
Note that some methods have specific functionality for this parameter, which is described on the method page (e.g., the `search` parameter in [host.get](/documentation/current/en/manual/api/reference/host/get) also supports Host interface properties).  
searchByAny | boolean | If set to `true`, return results that match any of the criteria given in the `filter` or `search` parameter instead of all of them.  
  
Default: `false`.  
searchWildcardsEnabled | boolean | If set to `true`, enables the use of "*" as a wildcard character in the `search` parameter.  
  
Default: `false`.  
sortfield | string/array | Sort the result by the given properties. Refer to a specific API get method description for a list of properties that can be used for sorting. Macros are not expanded before sorting.  
  
If no value is specified, data will be returned unsorted.  
sortorder | string/array | Order of sorting. If an array is passed, each value will be matched to the corresponding property given in the `sortfield` parameter.  
  
Possible values:  
`ASC` \- _(default)_ ascending;  
`DESC` \- descending.  
startSearch | boolean | The `search` parameter will compare the beginning of fields, that is, perform a `LIKE "…%"` search instead.  
  
Ignored if `searchWildcardsEnabled` is set to `true`.  
  
### Entity origin flags

Get methods return a `flags` property for entities related to low-level discovery (LLD rule/LLD rule prototype, item/item prototype, etc). This property is useful to denote if the entity has been discovered or not, since editing for discovered entities is limited.

The `flags` property returns a result based on a combination ("+" operation) of these values:

0 | Base entity (item, trigger, graph, host)  
---|---  
1 | Low-level discovery rule  
2 | Any prototype (item prototype, trigger prototype, LLD rule prototype, etc)  
4 | Discovered entity (discovered item, trigger, graph, host, LLD rule)  
  
The **combined** value returned by the `flags` property may be:

**0** | 0 | Plain entity (item, trigger, graph, host).  
---|---|---  
**2** | 2 | Entity prototype (item prototype, trigger prototype, etc).  
**6** | 2+4 | Discovered item, trigger, graph, host (converted from prototype).  
**1** | 1 | Low-level discovery rule.  
**3** | 1+2 | Low-level discovery rule prototype.  
**5** | 1+4 | Discovered low-level discovery rule (converted from prototype).  
**7** | 1+2+4 | Discovered low-level discovery rule prototype.  
  
### Examples

#### User permission check

Does the user have permission to write to hosts whose names begin with "MySQL" or "Linux" ?

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "host.get",
               "params": {
                   "countOutput": true,
                   "search": {
                       "host": ["MySQL", "Linux"]
                   },
                   "editable": true,
                   "startSearch": true,
                   "searchByAny": true
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": "0",
               "id": 1
           }

Copy

✔ Copied

Zero result means no hosts with read/write permissions.

#### Mismatch counting

Count the number of hosts whose names do not contain the substring "ubuntu"

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "host.get",
               "params": {
                   "countOutput": true,
                   "search": {
                       "host": "ubuntu"
                   },
                   "excludeSearch": true
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": "44",
               "id": 1
           }

Copy

✔ Copied

#### Searching for hosts using wildcards

Find hosts whose name contains word "server" and have interface ports "10050" or "10071". Sort the result by host name in descending order and limit it to 5 hosts.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "host.get",
               "params": {
                   "output": ["hostid", "host"],
                   "selectInterfaces": ["port"],
                   "filter": {
                       "port": ["10050", "10071"]
                   },
                   "search": {
                       "host": "*server*"
                   },
                   "searchWildcardsEnabled": true,
                   "searchByAny": true,
                   "sortfield": "host",
                   "sortorder": "DESC",
                   "limit": 5
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
                       "hostid": "50003",
                       "host": "WebServer-Tomcat02",
                       "interfaces": [
                           {
                               "port": "10071"
                           }
                       ]
                   },
                   {
                       "hostid": "50005",
                       "host": "WebServer-Tomcat01",
                       "interfaces": [
                           {
                               "port": "10071"
                           }
                       ]
                   },
                   {
                       "hostid": "50004",
                       "host": "WebServer-Nginx",
                       "interfaces": [
                           {
                               "port": "10071"
                           }
                       ]
                   },
                   {
                       "hostid": "99032",
                       "host": "MySQL server 01",
                       "interfaces": [
                           {
                               "port": "10050"
                           }
                       ]
                   },
                   {
                       "hostid": "99061",
                       "host": "Linux server 01",
                       "interfaces": [
                           {
                               "port": "10050"
                           }
                       ]
                   }
               ],
               "id": 1
           }

Copy

✔ Copied

#### Searching for hosts using wildcards with "preservekeys"

If you add the parameter "preservekeys" to the previous request, the result is returned as an associative array, where the keys are the id of the objects.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "host.get",
               "params": {
                   "output": ["hostid", "host"],
                   "selectInterfaces": ["port"],
                   "filter": {
                       "port": ["10050", "10071"]
                   },
                   "search": {
                       "host": "*server*"
                   },
                   "searchWildcardsEnabled": true,
                   "searchByAny": true,
                   "sortfield": "host",
                   "sortorder": "DESC",
                   "limit": 5,
                   "preservekeys": true
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "50003": {
                       "hostid": "50003",
                       "host": "WebServer-Tomcat02",
                       "interfaces": [
                           {
                               "port": "10071"
                           }
                       ]
                   },
                   "50005": {
                       "hostid": "50005",
                       "host": "WebServer-Tomcat01",
                       "interfaces": [
                           {
                               "port": "10071"
                           }
                       ]
                   },
                   "50004": {
                       "hostid": "50004",
                       "host": "WebServer-Nginx",
                       "interfaces": [
                           {
                               "port": "10071"
                           }
                       ]
                   },
                   "99032": {
                       "hostid": "99032",
                       "host": "MySQL server 01",
                       "interfaces": [
                           {
                               "port": "10050"
                           }
                       ]
                   },
                   "99061": {
                       "hostid": "99061",
                       "host": "Linux server 01",
                       "interfaces": [
                           {
                               "port": "10050"
                           }
                       ]
                   }
               },
               "id": 1
           }

Copy

✔ Copied