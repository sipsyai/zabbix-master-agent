---
title: Discovery check object
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/dcheck/object
downloaded: 2025-11-14 10:41:20
---

# Discovery check object

The following objects are directly related to the `dcheck` API.

### Discovery check

The discovery check object defines a specific check performed by a network discovery rule. It has the following properties.

dcheckid | ID | ID of the discovery check.  
---|---|---  
druleid | ID | ID of the discovery rule that the check belongs to.  
key_ | string | Item key (if `type` is set to "Zabbix agent") or SNMP OID (if `type` is set to "SNMPv1 agent", "SNMPv2 agent", or "SNMPv3 agent").  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `type` is set to "Zabbix agent", "SNMPv1 agent", "SNMPv2 agent", or "SNMPv3 agent"  
ports | string | One or several port ranges to check, separated by commas.  
  
Default: 0.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `type` is set to "SSH" (0), "LDAP" (1), "SMTP" (2), "FTP" (3), "HTTP" (4), "POP" (5), "NNTP" (6), "IMAP" (7), "TCP" (8), "Zabbix agent" (9), "SNMPv1 agent" (10), "SNMPv2 agent" (11), "SNMPv3 agent" (13), "HTTPS" (14), or "Telnet" (15)  
snmp_community | string | SNMP community.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `type` is set to "SNMPv1 agent" or "SNMPv2 agent"  
snmpv3_authpassphrase | string | Authentication passphrase.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `type` is set to "SNMPv3 agent" and `snmpv3_securitylevel` is set to "authNoPriv" or "authPriv"  
snmpv3_authprotocol | integer | Authentication protocol.  
  
Possible values:  
0 - _(default)_ MD5;  
1 - SHA1;  
2 - SHA224;  
3 - SHA256;  
4 - SHA384;  
5 - SHA512.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `type` is set to "SNMPv3 agent" and `snmpv3_securitylevel` is set to "authNoPriv" or "authPriv"  
snmpv3_contextname | string | SNMPv3 context name.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `type` is set to "SNMPv3 agent"  
snmpv3_privpassphrase | string | Privacy passphrase.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `type` is set to "SNMPv3 agent" and `snmpv3_securitylevel` is set to "authPriv"  
snmpv3_privprotocol | integer | Privacy protocol.  
  
Possible values:  
0 - _(default)_ DES;  
1 - AES128;  
2 - AES192;  
3 - AES256;  
4 - AES192C;  
5 - AES256C.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `type` is set to "SNMPv3 agent" and `snmpv3_securitylevel` is set to "authPriv"  
snmpv3_securitylevel | string | Security level.  
  
Possible values:  
0 - noAuthNoPriv;  
1 - authNoPriv;  
2 - authPriv.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `type` is set to "SNMPv3 agent"  
snmpv3_securityname | string | Security name.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `type` is set to "SNMPv3 agent"  
type | integer | Type of check.  
  
Possible values:  
0 - SSH;  
1 - LDAP;  
2 - SMTP;  
3 - FTP;  
4 - HTTP;  
5 - POP;  
6 - NNTP;  
7 - IMAP;  
8 - TCP;  
9 - Zabbix agent;  
10 - SNMPv1 agent;  
11 - SNMPv2 agent;  
12 - ICMP ping;  
13 - SNMPv3 agent;  
14 - HTTPS;  
15 - Telnet.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
uniq | integer | Whether to use this check as a device uniqueness criteria. Only a single unique check can be configured for a discovery rule.  
  
Possible values:  
0 - _(default)_ do not use this check as a uniqueness criteria;  
1 - use this check as a uniqueness criteria.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `type` is set to "Zabbix agent", "SNMPv1 agent", "SNMPv2 agent", or "SNMPv3 agent"  
host_source | integer | Source for host name.  
  
Possible values:  
1 - _(default)_ DNS;  
2 - IP;  
3 - discovery value of this check.  
name_source | integer | Source for visible name.  
  
Possible values:  
0 - _(default)_ not specified;  
1 - DNS;  
2 - IP;  
3 - discovery value of this check.  
allow_redirect | integer | Allow situation where the target being ICMP pinged responds from a different IP address.  
  
Possible values:  
0 - _(default)_ treat redirected responses as if the target host is down (fail);  
1 - treat redirected responses as if the target host is up (success).  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `type` is set to "ICMP ping"