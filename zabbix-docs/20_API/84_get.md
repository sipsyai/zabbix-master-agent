---
title: dservice.get
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/dservice/get
downloaded: 2025-11-14 10:41:18
---

# dservice.get  
  
### Description

`integer/array dservice.get(object parameters)`

The method allows to retrieve discovered services according to the given parameters.

This method is available to users of any type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object)` Parameters defining the desired output.

The method supports the following parameters.

dserviceids | ID/array | Return only discovered services with the given IDs.  
---|---|---  
dhostids | ID/array | Return only discovered services that belong to the given discovered hosts.  
dcheckids | ID/array | Return only discovered services that have been detected by the given discovery checks.  
druleids | ID/array | Return only discovered services that have been detected by the given discovery rules.  
selectDRules | query | Return a [`drules`](/documentation/current/en/manual/api/reference/drule/object) property with an array of the discovery rules that detected the service.  
selectDHosts | query | Return a [`dhosts`](/documentation/current/en/manual/api/reference/dhost/object) property with an array the discovered hosts that the service belongs to.  
selectHosts | query | Return a [`hosts`](/documentation/current/en/manual/api/reference/host/object) property with the hosts with the same IP address and proxy as the service.  
  
Supports `count`.  
limitSelects | integer | Limits the number of records returned by subselects.  
  
Applies to the following subselects:  
`selectHosts` \- result will be sorted by `hostid`.  
sortfield | string/array | Sort the result by the given properties.  
  
Possible values: `dserviceid`, `dhostid`, `ip`.  
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

#### Retrieve services discovered on a host

Retrieve all discovered services detected on discovered host "11".

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "dservice.get",
               "params": {
                   "output": "extend",
                   "dhostids": "11"
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
                       "dserviceid": "12",
                       "dhostid": "11",
                       "value": "",
                       "port": "80",
                       "status": "1",
                       "lastup": "0",
                       "lastdown": "1348650607",
                       "dcheckid": "5",
                       "ip": "192.168.1.134",
                       "dns": "john.local"
                   },
                   {
                       "dserviceid": "13",
                       "dhostid": "11",
                       "value": "",
                       "port": "21",
                       "status": "1",
                       "lastup": "0",
                       "lastdown": "1348650610",
                       "dcheckid": "6",
                       "ip": "192.168.1.134",
                       "dns": "john.local"
                   }
               ],
               "id": 1
           }

Copy

✔ Copied

### See also

  * [Discovered host](/documentation/current/en/manual/api/reference/dhost/object#discovered-host)
  * [Discovery check](/documentation/current/en/manual/api/reference/dcheck/object#discovery-check)
  * [Host](/documentation/current/en/manual/api/reference/host/object#host)

### Source

CDService::get() in _ui/include/classes/api/services/CDService.php_.