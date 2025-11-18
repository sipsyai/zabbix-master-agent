---
title: hostprototype.update
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/hostprototype/update
downloaded: 2025-11-14 10:42:27
---

# hostprototype.update

### Description

`object hostprototype.update(object/array hostPrototypes)`

This method allows to update existing host prototypes.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` Host prototype properties to be updated.

The `hostid` property must be defined for each host prototype, all other properties are optional. Only the passed properties will be updated, all others will remain unchanged.

Additionally to the [standard host prototype properties](object#host-prototype), the method accepts the following parameters.

groupLinks | array | [Group links](/documentation/current/en/manual/api/reference/hostprototype/object#group-link) to replace the current group links on the host prototype.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _read-only_ for inherited objects  
---|---|---  
groupPrototypes | array | [Group prototypes](/documentation/current/en/manual/api/reference/hostprototype/object#group-prototype) to replace the existing group prototypes on the host prototype.  
  
All group prototypes that are not listed in the request will be removed.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _read-only_ for inherited objects  
macros | object/array | [User macros](/documentation/current/en/manual/api/reference/usermacro/object) to replace the current user macros.  
All macros that are not listed in the request will be removed.  
tags | object/array | [Host prototype tags](/documentation/current/en/manual/api/reference/hostprototype/object#host-prototype-tag) to replace the current tags.  
All tags that are not listed in the request will be removed.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _read-only_ for inherited objects  
interfaces | object/array | Host prototype [custom interfaces](/documentation/current/en/manual/api/reference/hostprototype/object#custom-interface) to replace the current interfaces.  
Custom interface object should contain all its parameters.  
All interfaces that are not listed in the request will be removed.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if `custom_interfaces` of [Host prototype object](/documentation/current/en/manual/api/reference/usermacro/object#host-prototype) is set to "use host prototypes custom interfaces"  
\- _read-only_ for inherited objects  
templates | object/array | [Templates](/documentation/current/en/manual/api/reference/template/object) to replace the currently linked templates.  
  
The templates must have only the `templateid` property defined.  
  
### Return values

`(object)` Returns an object containing the IDs of the updated host prototypes under the `hostids` property.

### Examples

#### Disabling a host prototype

Disable a host prototype, that is, set its status to "1".

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "hostprototype.update",
               "params": {
                   "hostid": "10092",
                   "status": 1
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
                       "10092"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Updating host prototype tags

Replace host prototype tags with new ones.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "hostprototype.update",
               "params": {
                   "hostid": "10092",
                   "tags": [
                       {
                           "tag": "datacenter",
                           "value": "{#DATACENTER.NAME}"
                       },
                       {
                           "tag": "instance-type",
                           "value": "{#INSTANCE_TYPE}"
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
                       "10092"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Updating host prototype custom interfaces

Replace inherited interfaces with host prototype custom interfaces.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "hostprototype.update",
               "params": {
                   "hostid": "10092",
                   "custom_interfaces": "1",
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
                       "10092"
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

CHostPrototype::update() in _ui/include/classes/api/services/CHostPrototype.php_.