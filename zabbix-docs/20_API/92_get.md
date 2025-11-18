---
title: drule.get
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/drule/get
downloaded: 2025-11-14 10:41:26
---

# drule.get

### Description

`integer/array drule.get(object parameters)`

The method allows to retrieve discovery rules according to the given parameters.

This method is available to users of any type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object)` Parameters defining the desired output.

The method supports the following parameters.

dhostids | ID/array | Return only discovery rules that created the given discovered hosts.  
---|---|---  
druleids | ID/array | Return only discovery rules with the given IDs.  
dserviceids | ID/array | Return only discovery rules that created the given discovered services.  
selectDChecks | query | Return a [`dchecks`](/documentation/current/en/manual/api/reference/dcheck/object) property with the discovery checks used by the discovery rule.  
  
Supports `count`.  
selectDHosts | query | Return a [`dhosts`](/documentation/current/en/manual/api/reference/dhost/object) property with the discovered hosts created by the discovery rule.  
  
Supports `count`.  
limitSelects | integer | Limits the number of records returned by subselects.  
  
Applies to the following subselects:  
`selectDChecks` \- results will be sorted by `dcheckid`;  
`selectDHosts` \- results will be sorted by `dhostsid`.  
sortfield | string/array | Sort the result by the given properties.  
  
Possible values: `druleid`, `name`.  
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

#### Retrieve all discovery rules

Retrieve all configured discovery rules and the discovery checks they use.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "drule.get",
               "params": {
                   "output": "extend",
                   "selectDChecks": "extend"
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
                       "druleid": "2",
                       "proxyid": "0",
                       "name": "Local network",
                       "iprange": "192.168.3.1-255",
                       "delay": "5s",
                       "status": "0",
                       "concurrency_max": "0",
                       "error": "",
                       "dchecks": [
                           {
                               "dcheckid": "7",
                               "druleid": "2",
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
                           },
                           {
                               "dcheckid": "8",
                               "druleid": "2",
                               "type": "4",
                               "key_": "",
                               "snmp_community": "",
                               "ports": "80",
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
                       ]
                   },
                   {
                       "druleid": "6",
                       "proxyid": "0",
                       "name": "Zabbix agent discovery",
                       "iprange": "192.168.1.1-255",
                       "delay": "1h",
                       "status": "0",
                       "concurrency_max": "10",
                       "error": "",
                       "dchecks": [
                           {
                               "dcheckid": "10",
                               "druleid": "6",
                               "type": "9",
                               "key_": "system.uname",
                               "snmp_community": "",
                               "ports": "10050",
                               "snmpv3_securityname": "",
                               "snmpv3_securitylevel": "0",
                               "snmpv3_authpassphrase": "",
                               "snmpv3_privpassphrase": "",
                               "uniq": "0",
                               "snmpv3_authprotocol": "0",
                               "snmpv3_privprotocol": "0",
                               "snmpv3_contextname": "",
                               "host_source": "2",
                               "name_source": "3",
                               "allow_redirect": "0"
                           }
                       ]
                   }
               ],
               "id": 1
           }

Copy

✔ Copied

### See also

  * [Discovered host](/documentation/current/en/manual/api/reference/dhost/object#discovered-host)
  * [Discovery check](/documentation/current/en/manual/api/reference/dcheck/object#discovery-check)

### Source

CDRule::get() in _ui/include/classes/api/services/CDRule.php_.