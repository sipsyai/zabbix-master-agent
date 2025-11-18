---
title: dcheck.get
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/dcheck/get
downloaded: 2025-11-14 10:41:21
---

# dcheck.get  
  
### Description

`integer/array dcheck.get(object parameters)`

The method allows to retrieve discovery checks according to the given parameters.

This method is available to users of any type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object)` Parameters defining the desired output.

The method supports the following parameters.

dcheckids | ID/array | Return only discovery checks with the given IDs.  
---|---|---  
druleids | ID/array | Return only discovery checks that belong to the given discovery rules.  
dserviceids | ID/array | Return only discovery checks that have detected the given discovered services.  
selectDRules | query | Return discovery rules related to the discovery checks.  
sortfield | string/array | Sort the result by the given properties.  
  
Possible values: `dcheckid`, `druleid`.  
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

#### Retrieve discovery checks for a discovery rule

Retrieve all discovery checks used by discovery rule "6".

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "dcheck.get",
               "params": {
                   "output": "extend",
                   "dcheckids": "6"
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
                       "dcheckid": "6",
                       "druleid": "4",
                       "type": "3",
                       "key_": "",
                       "snmp_community": "",
                       "ports": "21",
                       "snmpv3_securityname": "",
                       "snmpv3_securitylevel": "0",
                       "snmpv3_authpassphrase": "",
                       "snmpv3_privpassphrase": "",
                       "uniq": "0",
                       "snmpv3_authprotocol": "0",
                       "snmpv3_privprotocol": "0",
                       "snmpv3_contextname": "",
                       "host_source": "1",
                       "name_source": "0",
                       "allow_redirect": "0"
                   }
               ],
               "id": 1
           }

Copy

✔ Copied

### Source

CDCheck::get() in _ui/include/classes/api/services/CDCheck.php_.