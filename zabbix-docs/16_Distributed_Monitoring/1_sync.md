---
title: Synchronization of monitoring configuration
source: https://www.zabbix.com/documentation/current/en/manual/distributed_monitoring/proxies/sync
downloaded: 2025-11-14 10:37:43
---

# 1 Synchronization of monitoring configuration

### Overview

This page provides details on the monitoring configuration update for the proxy, i.e. how changes made to the monitoring configuration on the server are synchronized to the proxy.

### Incremental update

The proxy configuration update is incremental. During a configuration sync only the modified entities are updated (thus, if no entities have been modified, nothing will be sent). This approach allows to save resources and set a smaller interval (almost instant) for the proxy configuration update.

Proxy configuration changes are tracked using revision numbers. Only entities with revisions larger than the proxy configuration revision are included in configuration data sent to the proxy.

The entities for a configuration sync are as follows:

_autoregistration tls data_ | All autoregistration TLS data.  
---|---  
_expressions_ | All expressions (regular expressions, expression tables).  
_global configuration_ | Global configuration defined in the 'config' table  
_host_ | All properties, interfaces, inventory, items, item preprocessing, item parameters, web scenarios of a host.  
_host macros_ | All macros defined on a host and all template IDs linked to it.  
_proxy discovery rule_ | Discovery rules and checks assigned to a proxy.  
  
That means:

  * If an item is changed on a **host** , all configuration of that host will be synced.
  * If a **regular expression** is changed, all regular expressions will be synced.

An exception are the host macros which are sent also if anything on the host has been changed.

The `-R config_cache_reload` command on the proxy will also initiate an incremental update.

Note that a full configuration sync will take place on a proxy start/restart, HA failover, if the session token has changed, or if the configuration update failed on the proxy, for example, if the connection was broken while receiving configuration data.

### Configuration parameters

The **ProxyConfigFrequency** parameter determines how often the proxy configuration is synced with the server (10 seconds by default).

Note that ProxyConfigFrequency is:

  * server parameter for passive proxies
  * proxy parameter for active proxies

On active proxies ProxyConfigFrequency is a new parameter since Zabbix 6.4 and must be used instead of the now-deprecated ConfigFrequency.

If both ProxyConfigFrequency and ConfigFrequency are used, the proxy will log an error and terminate.

#### Calculation of queues during maintenance

The Zabbix proxy is not aware of maintenance periods; see [Calculation of queues during maintenance](/documentation/current/en/manual/maintenance#calculation-of-queues-during-maintenance) for details.