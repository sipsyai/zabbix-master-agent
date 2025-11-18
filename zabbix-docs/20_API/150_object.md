---
title: Host prototype object
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/hostprototype/object
downloaded: 2025-11-14 10:42:23
---

# Host prototype object

The following objects are directly related to the `hostprototype` API.

### Host prototype

The host prototype object has the following properties.

hostid | ID | ID of the host prototype.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
\- _required_ for update operations  
---|---|---  
host | string | Technical name of the host prototype.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
\- _read-only_ for inherited objects  
name | string | Visible name of the host prototype.  
  
Default: `host` property value.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_ for inherited objects  
status | integer | Status of the host prototype.  
  
Possible values:  
0 - _(default)_ monitored host;  
1 - unmonitored host.  
flags | integer | [Origin](/documentation/current/en/manual/api/reference_commentary#entity-origin-flags) of the host prototype.  
  
Possible values:  
2 - a host prototype;  
6 - a discovered host prototype  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
inventory_mode | integer | Host inventory population mode.  
  
Possible values:  
-1 - _(default)_ disabled;  
0 - manual;  
1 - automatic.  
templateid | ID | ID of the parent template host prototype.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
discover | integer | Host prototype discovery status.  
  
Possible values:  
0 - _(default)_ new hosts will be discovered;  
1 - new hosts will not be discovered and existing hosts will be marked as lost.  
custom_interfaces | integer | Source of custom interfaces for hosts created by the host prototype.  
  
Possible values:  
0 - _(default)_ inherit interfaces from parent host;  
1 - use host prototypes custom interfaces.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_ for inherited objects  
uuid | string | Universal unique identifier, used for linking imported host prototypes to already existing ones. Auto-generated, if not given.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if the host prototype belongs to a template  
  
### Group link

The group link object links a host prototype with a host group. It has the following properties.

groupid | ID | ID of the host group.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
  
### Group prototype

The group prototype object defines a group that will be created for a discovered host. It has the following properties.

group_prototypeid | ID | ID of the group prototype.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
---|---|---  
name | string | Name of the group prototype.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
  
### Host prototype tag

The host prototype tag object has the following properties.

tag | string | Host prototype tag name.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
value | string | Host prototype tag value.  
  
### Custom interface

Custom interfaces are supported if `custom_interfaces` of Host prototype object is set to "use host prototypes custom interfaces". The custom interface object has the following properties.

type | integer | Interface type.  
  
Possible values:  
1 - Agent;  
2 - SNMP;  
3 - IPMI;  
4 - JMX.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
useip | integer | Whether the connection should be made via IP.  
  
Possible values:  
0 - connect using host DNS name;  
1 - connect using host IP address.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
ip | string | IP address used by the interface.  
Can contain macros.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `useip` is set to "connect using host IP address"  
dns | string | DNS name used by the interface.  
Can contain macros.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `useip` is set to "connect using host DNS name"  
port | string | Port number used by the interface.  
Can contain user and LLD macros.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
main | integer | Whether the interface is used as default on the host.  
Only one interface of some type can be set as default on a host.  
  
Possible values:  
0 - not default;  
1 - default.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
details | object | Additional object for custom interface details.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `type` is set to "SNMP"  
  
#### Custom interface details

The details object has the following properties.

version | integer | SNMP interface version.  
  
Possible values:  
1 - SNMPv1;  
2 - SNMPv2c;  
3 - SNMPv3.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
bulk | integer | Whether to use bulk SNMP requests.  
  
Possible values:  
0 - don't use bulk requests;  
1 - _(default)_ \- use bulk requests.  
community | string | SNMP community.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `version` is set to "SNMPv1" or "SNMPv2c"  
max_repetitions | integer | Max repetition value for native SNMP bulk requests (GetBulkRequest-PDUs).  
Used only for `discovery[]` and `walk[]` items in SNMPv2 and v3.  
  
Default: 10.  
securityname | string | SNMPv3 security name.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `version` is set to "SNMPv3"  
securitylevel | integer | SNMPv3 security level.  
  
Possible values:  
0 - _(default)_ \- noAuthNoPriv;  
1 - authNoPriv;  
2 - authPriv.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `version` is set to "SNMPv3"  
authpassphrase | string | SNMPv3 authentication passphrase.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `version` is set to "SNMPv3" and `securitylevel` is set to "authNoPriv" or "authPriv"  
privpassphrase | string | SNMPv3 privacy passphrase.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `version` is set to "SNMPv3" and `securitylevel` is set to "authPriv"  
authprotocol | integer | SNMPv3 authentication protocol.  
  
Possible values:  
0 - _(default)_ \- MD5;  
1 - SHA1;  
2 - SHA224;  
3 - SHA256;  
4 - SHA384;  
5 - SHA512.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `version` is set to "SNMPv3" and `securitylevel` is set to "authNoPriv" or "authPriv"  
privprotocol | integer | SNMPv3 privacy protocol. Used only by SNMPv3 interfaces.  
  
Possible values:  
0 - _(default)_ \- DES;  
1 - AES128;  
2 - AES192;  
3 - AES256;  
4 - AES192C;  
5 - AES256C.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `version` is set to "SNMPv3" and `securitylevel` is set to "authPriv"  
contextname | string | SNMPv3 context name.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `version` is set to "SNMPv3"