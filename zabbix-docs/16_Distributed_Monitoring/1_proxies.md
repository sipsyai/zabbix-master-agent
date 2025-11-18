---
title: Proxies
source: https://www.zabbix.com/documentation/current/en/manual/distributed_monitoring/proxies
downloaded: 2025-11-14 10:37:42
---

# 1 Proxies

### Overview

A Zabbix proxy can collect performance and availability data on behalf of the Zabbix server. This way, a proxy can take on itself some of the load of collecting data and offload the Zabbix server.

Also, using a proxy is the easiest way of implementing centralized and distributed monitoring, when all agents and proxies report to one Zabbix server and all data is collected centrally.

A Zabbix proxy can be used to:

  * Monitor remote locations
  * Monitor locations having unreliable communications
  * Offload the Zabbix server when monitoring thousands of devices
  * Simplify the maintenance of distributed monitoring

![](/documentation/current/assets/en/manual/proxies/proxy.png)

The proxy requires only one TCP connection to the Zabbix server. This way it is easier to get around a firewall as you only need to configure one firewall rule.

Zabbix proxy must use a separate database. Pointing it to the Zabbix server database will break the configuration.

All data collected by the proxy is stored locally before transmitting it over to the server. This way no data is lost due to any temporary communication problems with the server. The _ProxyLocalBuffer_ and _ProxyOfflineBuffer_ parameters in the [proxy configuration file](/documentation/current/en/manual/appendix/config/zabbix_proxy) control for how long the data are kept locally.

It may happen that a proxy, which receives the latest configuration changes directly from Zabbix server database, has a more up-to-date configuration than Zabbix server whose configuration may not be updated as fast due to the value of [CacheUpdateFrequency](/documentation/current/en/manual/appendix/config/zabbix_server). As a result, proxy may start gathering data and send them to Zabbix server that ignores these data.

Zabbix proxy is a data collector. It does not calculate triggers, process events or send alerts. For an overview of what proxy functionality is, review the following table:

Items  
---  
| _Zabbix agent checks_ | **Yes**  
_Zabbix agent checks (active)_ | **Yes** 1  
_Simple checks_ | **Yes**  
_Trapper items_ | **Yes**  
_SNMP checks_ | **Yes**  
_SNMP traps_ | **Yes**  
_IPMI checks_ | **Yes**  
_JMX checks_ | **Yes**  
_Log file monitoring_ | **Yes**  
_Internal checks_ | **Yes**  
_SSH checks_ | **Yes**  
_Telnet checks_ | **Yes**  
_External checks_ | **Yes**  
_Dependent items_ | **Yes**  
_Script items_ | **Yes**  
_Browser items_ | **Yes**  
Built-in web monitoring | **Yes**  
Item value preprocessing | **Yes**  
Network discovery | **Yes**  
Active agent autoregistration | **Yes**  
Low-level discovery | **Yes** 2  
Remote commands | **Yes**  
Calculating triggers | _No_  
Processing events | _No_  
Event correlation | _No_  
Sending alerts | _No_  
  
[1] To make sure that an agent asks the proxy (and not the server) for active checks, the proxy must be listed in the **ServerActive** parameter in the agent configuration file.  
[2] For LLD, Zabbix proxy only collects and preprocesses the data and then sends it to Zabbix server for further processing.

##### Protection from overloading

If Zabbix server was down for some time, and proxies have collected a lot of data, and then the server starts, it may get overloaded (history cache usage stays at 95-100% for some time). This overload could result in a performance hit, where checks are processed slower than they should. Protection from this scenario was implemented to avoid problems that arise due to overloading history cache.

When Zabbix server history cache is full the history cache write access is being throttled, stalling server data gathering processes. The most common history cache overload case is after server downtime when proxies are uploading gathered data. To avoid this proxy throttling was added (currently it cannot be disabled).

Zabbix server will stop accepting data from proxies when history cache usage reaches 80%. Instead those proxies will be put on a throttling list. This will continue until the cache usage falls down to 60%. Now server will start accepting data from proxies one by one, defined by the throttling list. This means the first proxy that attempted to upload data during the throttling period will be served first and until it's done the server will not accept data from other proxies.

This throttling mode will continue until either cache usage hits 80% again or falls down to 20% or the throttling list is empty. In the first case the server will stop accepting proxy data again. In the other two cases the server will start working normally, accepting data from all proxies.

The above information can be illustrated in the following table:

Reaches 80% | Wait | Stops accepting proxy data, but maintains a _throttling list_ (prioritized list of proxies to be contacted later).  
---|---|---  
Drops to 60% | Throttled | Starts processing the throttling list, but still not accepting proxy data.  
Drops to 20% | Normal | Drops the throttling list and starts accepting proxy data normally.  
  
You may use the [zabbix[wcache,history,pused]](/documentation/current/en/manual/config/items/itemtypes/internal#wcache) internal item to correlate this behavior of Zabbix server with a metric.

### Configuration

Once you have [installed](/documentation/current/en/manual/installation/install) and [configured](/documentation/current/en/manual/appendix/config/zabbix_proxy) a proxy, it is time to configure it in the Zabbix frontend.

##### Adding proxies

To configure a proxy in Zabbix frontend:

  * Go to: _Administration → Proxies_
  * Click on _Create proxy_

![](/documentation/current/assets/en/manual/distributed_monitoring/proxy.png)

_Proxy name_ | Enter the proxy name. It must be the same name as in the _Hostname_ parameter in the proxy configuration file.  
---|---  
_Proxy group_ | Select one proxy group for proxy [load balancing/high availability](/documentation/current/en/manual/distributed_monitoring/proxies/ha).  
_Address for active agents_ | Enter address the monitored active agents or senders must connect to. Supported **only** for Zabbix 7.0 agents or later.  
This address is used to connect to both active and passive proxies. This field is only available if a proxy group is selected in the _Proxy group_ field.  
| _Address_ | IP address/DNS name to connect to.  
_Port_ | TCP port number (10051 by default) to connect to. User macros are supported.  
_Proxy mode_ | Select the proxy mode.  
**Active** \- the proxy will connect to the Zabbix server and request configuration data  
**Passive** \- Zabbix server connects to the proxy  
 _Note_ that without encrypted communications (sensitive) proxy configuration data may become available to parties having access to the Zabbix server trapper port when using an active proxy. This is possible because anyone may pretend to be an active proxy and request configuration data if authentication does not take place or proxy addresses are not limited in the _Proxy address_ field.  
_Proxy address_ | If specified then active proxy requests are only accepted from this list of comma-delimited IP addresses, optionally in CIDR notation, or DNS names of active Zabbix proxy.  
This field is only available if an active proxy is selected in the _Proxy mode_ field. Macros are not supported.  
_Interface_ | Enter interface details for a passive proxy.  
This field is only available if a passive proxy is selected in the Proxy mode field.  
| _Address_ | IP address/DNS name of the passive proxy.  
_Port_ | TCP port number of the passive proxy (10051 by default). User macros are supported.  
_Description_ | Enter the proxy description.  
  
The **Encryption** tab allows you to require encrypted connections with the proxy.

_Connections to proxy_ | How the server connects to the passive proxy: no encryption (default), using PSK (pre-shared key) or certificate.  
---|---  
_Connections from proxy_ | Select what type of connections are allowed from the active proxy. Several connection types can be selected at the same time (useful for testing and switching to other connection type). Default is "No encryption".  
_Issuer_ | Allowed issuer of certificate. Certificate is first validated with CA (certificate authority). If it is valid, signed by the CA, then the _Issuer_ field can be used to further restrict allowed CA. This field is optional, intended to use if your Zabbix installation uses certificates from multiple CAs.  
_Subject_ | Allowed subject of certificate. Certificate is first validated with CA. If it is valid, signed by the CA, then the _Subject_ field can be used to allow only one value of _Subject_ string. If this field is empty then any valid certificate signed by the configured CA is accepted.  
_PSK identity_ | Pre-shared key identity string.  
Do not put sensitive information in the PSK identity, it is transmitted unencrypted over the network to inform a receiver which PSK to use.  
_PSK_ | Pre-shared key (hex-string). Maximum length: 512 hex-digits (256-byte PSK) if Zabbix uses GnuTLS or OpenSSL library, 64 hex-digits (32-byte PSK) if Zabbix uses mbed TLS (PolarSSL) library. Example: 1f87b595725ac58dd977beef14b97461a7c1045b9a1c963065002c5473194952  
  
The **Timeouts** tab allows you to override [global](/documentation/current/en/manual/web_interface/frontend_sections/administration/general#timeouts) timeouts for item types that support it.

![](/documentation/current/assets/en/manual/distributed_monitoring/proxy_timeout.png)

_Timeouts for item types_ | Select the timeout option:  
**Global** \- global timeout is used (displayed in the grayed out _Timeout_ field for each item type);  
**Override** \- custom timeout is used (set in the _Timeout_ field for each item type). Allowed range: 1 - 600s (default: inherited from [global](/documentation/current/en/manual/web_interface/frontend_sections/administration/general#timeouts) timeouts). [Time suffixes](/documentation/current/en/manual/appendix/suffixes#time-suffixes), e.g. 30s, 1m, and [user macros](/documentation/current/en/manual/config/macros/user_macros) are supported.  
  
Clicking the _Global timeouts_ link allows you to configure [global](/documentation/current/en/manual/web_interface/frontend_sections/administration/general#timeouts) timeouts. Note that the _Global timeouts_ link is visible only to users of _Super admin_ type with permissions to the _Administration_ → [_General_](/documentation/current/en/manual/web_interface/frontend_sections/administration/general) frontend section.  
  
Supported item types:  
\- [Zabbix agent](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent) (both passive and active checks)  
\- [Simple check](/documentation/current/en/manual/config/items/itemtypes/simple_checks) (except `icmpping*`, `vmware.*` items)  
\- [SNMP agent](/documentation/current/en/manual/config/items/itemtypes/snmp) (only for SNMP `walk[OID]` and `get[OID]` items)  
\- [External check](/documentation/current/en/manual/config/items/itemtypes/external)  
\- [Database monitor](/documentation/current/en/manual/config/items/itemtypes/odbc_checks)  
\- [HTTP agent](/documentation/current/en/manual/config/items/itemtypes/http)  
\- [SSH agent](/documentation/current/en/manual/config/items/itemtypes/ssh_checks)  
\- [TELNET agent](/documentation/current/en/manual/config/items/itemtypes/telnet_checks)  
\- [Script](/documentation/current/en/manual/config/items/itemtypes/script)  
\- [Browser](/documentation/current/en/manual/config/items/itemtypes/browser)  
  
Note that the timeouts set under **Override** will prevail over the global ones but will be overridden by individual item timeouts if those are set under [item configuration](/documentation/current/en/manual/config/items/item#configuration).  
---|---  
  
If proxy major version does not match server major version, ![](/documentation/current/assets/en/manual/distributed_monitoring/info_yellow.png) icon will be displayed next to _Timeouts for item types_ , with the hover message "Timeouts disabled because the proxy and server versions do not match". In such cases, the proxy will use the [`Timeout`](/documentation/current/en/manual/appendix/config/zabbix_proxy#timeout) parameter from the proxy configuration file.

The editing form of an existing proxy has the following additional buttons:

  * _Refresh configuration_ \- refresh configuration of the proxy
  * _Clone_ \- create a new proxy based on the properties of the existing proxy
  * _Delete_ \- delete the proxy

##### Host configuration

You can specify that an individual host should be monitored by a proxy or proxy group in the [host configuration](/documentation/current/en/manual/config/hosts/host) form, using the _Monitored by_ field.

![](/documentation/current/assets/en/manual/proxies/proxy_set.png)

Host [mass update](/documentation/current/en/manual/config/hosts/hostupdate) is another way of specifying that hosts should be monitored by a proxy or proxy group.