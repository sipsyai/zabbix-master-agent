---
title: Autoregistration object
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/autoregistration/object
downloaded: 2025-11-14 10:40:14
---

# Autoregistration object

The following objects are directly related to the `autoregistration` API.

### Autoregistration

The autoregistration object has the following properties.

tls_accept | integer | Type of allowed incoming connections for autoregistration.  
  
Possible values:  
1 - allow unencrypted connections;  
2 - allow TLS with PSK;  
3 - allow both unencrypted and TLS with PSK connections.  
---|---|---  
tls_psk_identity | string | PSK identity; must be paired with only one PSK (across [autoregistration](/documentation/current/en/manual/api/reference/autoregistration/object), [hosts](/documentation/current/en/manual/api/reference/host/object), and [proxies](/documentation/current/en/manual/api/reference/proxy/object)).  
  
Do not include sensitive information in the PSK identity, as it is sent unencrypted over the network to inform the receiver which PSK to use.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _write-only_  
tls_psk | string | Pre-shared key (PSK); must be at least 32 hex digits.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _write-only_