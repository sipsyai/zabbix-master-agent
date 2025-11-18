---
title: Discovery rule object
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/drule/object
downloaded: 2025-11-14 10:41:23
---

# Discovery rule object

The following objects are directly related to the `drule` API.

### Discovery rule

The discovery rule object defines a network discovery rule. It has the following properties.

druleid | ID | ID of the discovery rule.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
\- _required_ for update operations  
---|---|---  
iprange | string | One or several IP ranges to check, separated by commas.  
  
Refer to the [network discovery configuration](/documentation/current/en/manual/discovery/network_discovery/rule) section for more information on supported formats of IP ranges.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
name | string | Name of the discovery rule.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
delay | string | Execution interval of the discovery rule.  
  
Accepts seconds or time unit with suffix (e.g., 30s, 1m, 2h, 1d), or a user macro.  
  
Default: 1h.  
proxyid | ID | ID of the proxy used for discovery.  
status | integer | Whether the discovery rule is enabled.  
  
Possible values:  
0 - _(default)_ enabled;  
1 - disabled.  
concurrency_max | integer | Maximum number of concurrent checks per discovery rule.  
  
Possible values:  
0 - _(default)_ unlimited number of checks;  
1 - one check;  
2-999 - custom number of checks.  
error | string | Error text if there have been any problems when executing the discovery rule.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_