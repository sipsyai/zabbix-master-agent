---
title: hostprototype.create
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/hostprototype/create
downloaded: 2025-11-14 10:42:24
---

# hostprototype.create  
  
### Description

`object hostprototype.create(object/array hostPrototypes)`

This method allows to create new host prototypes.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` Host prototypes to create.

Additionally to the [standard host prototype properties](object#host-prototype), the method accepts the following parameters.

groupLinks | array | [Group links](/documentation/current/en/manual/api/reference/hostprototype/object#group-link) to be created for the host prototype.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
---|---|---  
ruleid | ID | ID of the LLD rule that the host prototype belongs to.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
groupPrototypes | array | [Group prototypes](/documentation/current/en/manual/api/reference/hostprototype/object#group-prototype) to be created for the host prototype.  
macros | object/array | [User macros](/documentation/current/en/manual/api/reference/usermacro/object) to be created for the host prototype.  
tags | object/array | [Host prototype tags](/documentation/current/en/manual/api/reference/hostprototype/object#host-prototype-tag).  
interfaces | object/array | Host prototype [custom interfaces](/documentation/current/en/manual/api/reference/hostprototype/object#custom-interface).  
templates | object/array | [Templates](/documentation/current/en/manual/api/reference/template/object) to be linked to the host prototype.  
  
The templates must have only the `templateid` property defined.  
  
### Return values

`(object)` Returns an object containing the IDs of the created host prototypes under the `hostids` property. The order of the returned IDs matches the order of the passed host prototypes.

### Examples

#### Creating a host prototype

Create a host prototype "{#VM.NAME}" on LLD rule "23542" with a group prototype "{#HV.NAME}", tag pair "datacenter": "{#DATACENTER.NAME}" and custom SNMPv2 interface 127.0.0.1:161 with community {$SNMP_COMMUNITY}. Link it to host group "2".

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "hostprototype.create",
               "params": {
                   "host": "{#VM.NAME}",
                   "ruleid": "23542",
                   "custom_interfaces": "1",
                   "groupLinks": [
                       {
                           "groupid": "2"
                       }
                   ],
                   "groupPrototypes": [
                       {
                           "name": "{#HV.NAME}"
                       }
                   ],
                   "tags": [
                       {
                           "tag": "datacenter",
                           "value": "{#DATACENTER.NAME}"
                       }
                   ],
                   "interfaces": [
                       {
                           "main": "1",
                           "type": "2",
                           "useip": "1",
                           "ip": "127.0.0.1",
                           "dns": "",
                           "port": "161",
                           "details": {
                               "version": "2",
                               "bulk": "1",
                               "community": "{$SNMP_COMMUNITY}"
                           }
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
                   "hostids": [
                       "10103"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### See also

  * [Group link](object#group-link)
  * [Group prototype](object#group-prototype)
  * [Host prototype tag](object#host-prototype-tag)
  * [Custom interface](object#custom-interface)
  * [User macro](/documentation/current/en/manual/api/reference/usermacro/object#hosttemplate-level-macro)

### Source

CHostPrototype::create() in _ui/include/classes/api/services/CHostPrototype.php_.