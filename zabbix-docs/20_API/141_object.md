---
title: Host interface object
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/hostinterface/object
downloaded: 2025-11-14 10:42:14
---

# Host interface object

The following objects are directly related to the `hostinterface` API.

### Host interface

The host interface object has the following properties.

Note that both `ip` and `dns` properties are _required_ for create operations. If you do not want to use DNS, set it to an empty string.

interfaceid | ID | ID of the interface.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
\- _required_ for update operations  
---|---|---  
available | integer | Availability of host interface.  
  
Possible values:  
0 - _(default)_ unknown;  
1 - available;  
2 - unavailable.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
hostid | ID | ID of the host that the interface belongs to.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _constant_  
\- _required_ for create operations  
type | integer | Interface type.  
  
Possible values:  
1 - Agent;  
2 - SNMP;  
3 - IPMI;  
4 - JMX.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
ip | string | IP address used by the interface.  
  
Can be empty if the connection is made via DNS.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
dns | string | DNS name used by the interface.  
  
Can be empty if the connection is made via IP.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
port | string | Port number used by the interface.  
Can contain user macros.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
useip | integer | Whether the connection should be made via IP.  
  
Possible values:  
0 - connect using host DNS name;  
1 - connect using host IP address.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
main | integer | Whether the interface is used as default on the host. Only one interface of some type can be set as default on a host.  
  
Possible values:  
0 - not default;  
1 - default.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
details | object | Additional details object for interface.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `type` is set to "SNMP"  
disable_until | timestamp | The next polling time of an unavailable host interface.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
error | string | Error text if host interface is unavailable.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
errors_from | timestamp | Time when host interface became unavailable.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
  
#### Details

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
1 - (default) - use bulk requests.  
community | string | SNMP community. Used only by SNMPv1 and SNMPv2 interfaces.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `version` is set to "SNMPv1" or "SNMPv2c"  
max_repetitions | integer | Max repetition value for native SNMP bulk requests (GetBulkRequest-PDUs).  
Used only for `discovery[]` and `walk[]` items in SNMPv2 and v3.  
  
Default: 10.  
securityname | string | SNMPv3 security name. Used only by SNMPv3 interfaces.  
securitylevel | integer | SNMPv3 security level. Used only by SNMPv3 interfaces.  
  
Possible values:  
0 - (default) - noAuthNoPriv;  
1 - authNoPriv;  
2 - authPriv.  
authpassphrase | string | SNMPv3 authentication passphrase. Used only by SNMPv3 interfaces.  
privpassphrase | string | SNMPv3 privacy passphrase. Used only by SNMPv3 interfaces.  
authprotocol | integer | SNMPv3 authentication protocol. Used only by SNMPv3 interfaces.  
  
Possible values:  
0 - (default) - MD5;  
1 - SHA1;  
2 - SHA224;  
3 - SHA256;  
4 - SHA384;  
5 - SHA512.  
privprotocol | integer | SNMPv3 privacy protocol. Used only by SNMPv3 interfaces.  
  
Possible values:  
0 - (default) - DES;  
1 - AES128;  
2 - AES192;  
3 - AES256;  
4 - AES192C;  
5 - AES256C.  
contextname | string | SNMPv3 context name. Used only by SNMPv3 interfaces.