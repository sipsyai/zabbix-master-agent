---
title: dhost.get
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/dhost/get
downloaded: 2025-11-14 10:41:15
---

# dhost.get  
  
### Description

`integer/array dhost.get(object parameters)`

The method allows to retrieve discovered hosts according to the given parameters.

This method is available to users of any type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object)` Parameters defining the desired output.

The method supports the following parameters.

dhostids | ID/array | Return only discovered hosts with the given IDs.  
---|---|---  
druleids | ID/array | Return only discovered hosts that have been created by the given discovery rules.  
dserviceids | ID/array | Return only discovered hosts that are running the given services.  
selectDRules | query | Return a [`drules`](/documentation/current/en/manual/api/reference/drule/object) property with an array of the discovery rules that detected the host.  
selectDServices | query | Return a [`dservices`](/documentation/current/en/manual/api/reference/dservice/object) property with the discovered services running on the host.  
  
Supports `count`.  
limitSelects | integer | Limits the number of records returned by subselects.  
  
Applies to the following subselects:  
`selectDServices` \- results will be sorted by `dserviceid`.  
sortfield | string/array | Sort the result by the given properties.  
  
Possible values: `dhostid`, `druleid`.  
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

#### Retrieve discovered hosts by discovery rule

Retrieve all hosts and the discovered services they are running that have been detected by discovery rule "4".

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "dhost.get",
               "params": {
                   "output": "extend",
                   "selectDServices": "extend",
                   "druleids": "4"
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
                       "dservices": [
                           {
                               "dserviceid": "1",
                               "dhostid": "1",
                               "type": "4",
                               "key_": "",
                               "value": "",
                               "port": "80",
                               "status": "0",
                               "lastup": "1337697227",
                               "lastdown": "0",
                               "dcheckid": "5",
                               "ip": "192.168.1.1",
                               "dns": "station.company.lan"
                           }
                       ],
                       "dhostid": "1",
                       "druleid": "4",
                       "status": "0",
                       "lastup": "1337697227",
                       "lastdown": "0"
                   },
                   {
                       "dservices": [
                           {
                               "dserviceid": "2",
                               "dhostid": "2",
                               "type": "4",
                               "key_": "",
                               "value": "",
                               "port": "80",
                               "status": "0",
                               "lastup": "1337697234",
                               "lastdown": "0",
                               "dcheckid": "5",
                               "ip": "192.168.1.4",
                               "dns": "john.company.lan"
                           }
                       ],
                       "dhostid": "2",
                       "druleid": "4",
                       "status": "0",
                       "lastup": "1337697234",
                       "lastdown": "0"
                   },
                   {
                       "dservices": [
                           {
                               "dserviceid": "3",
                               "dhostid": "3",
                               "type": "4",
                               "key_": "",
                               "value": "",
                               "port": "80",
                               "status": "0",
                               "lastup": "1337697234",
                               "lastdown": "0",
                               "dcheckid": "5",
                               "ip": "192.168.1.26",
                               "dns": "printer.company.lan"
                           }
                       ],
                       "dhostid": "3",
                       "druleid": "4",
                       "status": "0",
                       "lastup": "1337697234",
                       "lastdown": "0"
                   },
                   {
                       "dservices": [
                           {
                               "dserviceid": "4",
                               "dhostid": "4",
                               "type": "4",
                               "key_": "",
                               "value": "",
                               "port": "80",
                               "status": "0",
                               "lastup": "1337697234",
                               "lastdown": "0",
                               "dcheckid": "5",
                               "ip": "192.168.1.7",
                               "dns": "mail.company.lan"
                           }
                       ],
                       "dhostid": "4",
                       "druleid": "4",
                       "status": "0",
                       "lastup": "1337697234",
                       "lastdown": "0"
                   }
               ],
               "id": 1
           }

Copy

✔ Copied

### See also

  * [Discovered service](/documentation/current/en/manual/api/reference/dservice/object#discovered-service)
  * [Discovery rule](/documentation/current/en/manual/api/reference/drule/object#discovery-rule)

### Source

CDHost::get() in _ui/include/classes/api/services/CDHost.php_.