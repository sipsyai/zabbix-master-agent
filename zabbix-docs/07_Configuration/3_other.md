---
title: Additional operations
source: https://www.zabbix.com/documentation/current/en/manual/config/notifications/action/operation/other
downloaded: 2025-11-14 10:36:23
---

# 3 Additional operations  
  
#### Overview

In this section you may find some details of [additional operations](/documentation/current/en/manual/config/notifications/action/operation) for discovery/autoregistration events.

##### Adding host

Hosts are added during the discovery process, as soon as a host is discovered, rather than at the end of the discovery process.

As network discovery can take some time, due to many unavailable hosts/services, having patience and using reasonable IP ranges is recommended.

When adding a host, its name is decided by the standard **gethostbyname** function. If the host can be resolved, resolved name is used. If not, the IP address is used. Besides, if IPv6 address must be used for a host name, then all ":" (colons) are replaced by "_" (underscores), since colons are not allowed in host names.

If performing discovery by a proxy, currently hostname lookup still takes place on Zabbix server.

If a host already exists in Zabbix configuration with the same name as a newly discovered one, Zabbix will add **_N** to the hostname, where **N** is increasing number, starting with 2.