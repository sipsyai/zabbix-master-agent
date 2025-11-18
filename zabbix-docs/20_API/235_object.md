---
title: Proxy group object
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/proxygroup/object
downloaded: 2025-11-14 10:43:48
---

# Proxy group object

The following objects are directly related to the `proxygroup` API.

### Proxy group

The proxy group object has the following properties.

proxy_groupid | ID | ID of the proxy group.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
\- _required_ for update operations  
---|---|---  
name | string | Name of the proxy group.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
description | text | Description of the proxy group.  
failover_delay | string | Period during which a proxy in the proxy group must communicate with Zabbix server to be considered online.  
  
Time suffixes are supported, e.g. 30s, 1m.  
User macros are supported.  
  
Possible values: 10s-15m.  
  
Default: 1m.  
min_online | string | Minimum number of online proxies required to keep the proxy group online.  
  
User macros are supported.  
  
Possible values range: 1-1000.  
  
Default: 1.  
state | integer | State of the proxy group.  
  
Possible values:  
0 - Unknown;  
1 - Offline;  
2 - Recovering;  
3 - Online;  
4 - Degrading.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_