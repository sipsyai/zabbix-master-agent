---
title: Proxy object
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/proxy/object
downloaded: 2025-11-14 10:43:42
---

# Proxy object

The following objects are directly related to the `proxy` API.

### Proxy

The proxy object has the following properties.

proxyid | ID | ID of the proxy.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
\- _required_ for update operations  
---|---|---  
name | string | Name of the proxy.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
proxy_groupid | ID | ID of the proxy group.  
  
0 - proxy is not assigned to any proxy group.  
local_address | string | Address for active agents. IP address or DNS name to connect to.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `proxy_groupid` is not `0`  
local_port | string | Local proxy port number to connect to.  
  
User macros are supported.  
  
Default: 10051.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `proxy_groupid` is not `0`  
operating_mode | integer | Type of proxy.  
  
Possible values:  
0 - active proxy;  
1 - passive proxy.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
description | text | Description of the proxy.  
lastaccess | timestamp | Time when the proxy last connected to the server.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
address | string | IP address or DNS name to connect to.  
  
User macros are supported.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if the Zabbix proxy operating mode is passive  
port | string | Port number to connect to.  
  
User macros are supported.  
  
Default: 10051.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if the Zabbix proxy operating mode is passive  
allowed_addresses | string | Comma-delimited IP addresses or DNS names of active Zabbix proxy.  
tls_connect | integer | Connections to host.  
  
Possible values:  
1 - _(default)_ No encryption;  
2 - PSK;  
4 - certificate.  
tls_accept | integer | Connections from host.  
  
Possible bitmap values:  
1 - _(default)_ No encryption;  
2 - PSK;  
4 - certificate.  
  
This is a bitmask field; any sum of possible bitmap values is acceptable (for example, 6 for PSK and certificate).  
tls_issuer | string | Certificate issuer.  
tls_subject | string | Certificate subject.  
tls_psk_identity | string | PSK identity; must be paired with only one PSK (across [autoregistration](/documentation/current/en/manual/api/reference/autoregistration/object), [hosts](/documentation/current/en/manual/api/reference/host/object), and [proxies](/documentation/current/en/manual/api/reference/proxy/object)).  
  
Do not include sensitive information in the PSK identity, as it is sent unencrypted over the network to inform the receiver which PSK to use.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _write-only_  
\- _required_ if `tls_connect` is set to "PSK", or `tls_accept` contains the "PSK" bit  
tls_psk | string | Pre-shared key (PSK); must be at least 32 hex digits.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _write-only_  
\- _required_ if `tls_connect` is set to "PSK", or `tls_accept` contains the "PSK" bit  
custom_timeouts | integer | Whether to override global item timeouts on the proxy level.  
  
Possible values:  
0 - _(default)_ use global settings;  
1 - override timeouts.  
timeout_zabbix_agent | string | Spend no more than `timeout_*` seconds on processing.  
Accepts seconds or time unit with suffix (e.g., 30s, 1m). Also accepts user macros.  
  
Possible values range: 1-600s.  
  
Default: "".  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `custom_timeouts` is set to `1`.  
timeout_simple_check  
timeout_snmp_agent  
timeout_external_check  
timeout_db_monitor  
timeout_http_agent  
timeout_ssh_agent  
timeout_telnet_agent  
timeout_script  
timeout_browser  
version | integer | Version of proxy.  
  
Three-part Zabbix version number, where two decimal digits are used for each part, e.g., 60401 for version 6.4.1, 70002 for version 7.0.2, etc.  
0 - Unknown proxy version.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
compatibility | integer | Version of proxy compared to Zabbix server version.  
  
Possible values:  
0 - Undefined;  
1 - Current version (proxy and server have the same major version);  
2 - Outdated version (proxy version is older than server version, but is partially supported);  
3 - Unsupported version (proxy version is older than server previous LTS release version or server major version is older than proxy major version).  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
state | integer | State of the proxy.  
  
Possible values:  
0 - Unknown;  
1 - Offline;  
2 - Online.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_