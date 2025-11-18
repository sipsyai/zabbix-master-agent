---
title: Network discovery
source: https://www.zabbix.com/documentation/current/en/manual/discovery/network_discovery
downloaded: 2025-11-14 10:37:15
---

# 1 Network discovery

#### Overview

Zabbix offers automatic network discovery functionality that is effective and very flexible.

With network discovery properly set up you can:

  * speed up Zabbix deployment
  * simplify administration
  * use Zabbix in rapidly changing environments without excessive administration

Zabbix network discovery is based on the following information:

  * IP ranges
  * Availability of external services (FTP, SSH, WEB, POP3, IMAP, TCP, etc)
  * Information received from Zabbix agent (only unencrypted mode is supported)
  * Information received from SNMP agent

It does NOT provide:

  * Discovery of network topology

Network discovery basically consists of two phases: discovery and actions.

#### Discovery

Zabbix periodically scans the IP ranges defined in [network discovery rules](/documentation/current/en/manual/discovery/network_discovery/rule). The frequency of the check is configurable for each rule individually.

Each rule has a set of service checks defined to be performed for the IP range.

Discovery rules are processed by the discovery manager. The discovery manager creates a job per each rule with a list of tasks (network checks). Network checks are performed in parallel by the available discovery workers (the number is configurable in the frontend per each rule). Only checks with the same IP and port are scheduled sequentially because some devices will not accept parallel connections on the same port.

The queue size of network checks is limited to 2000000 or 4 GB of memory approximately. If the queue becomes full then the discovery rule will be skipped and a warning message will be printed in the log. You may use the `zabbix[discovery_queue]` internal item to monitor the number of discovery checks in the queue.

Discovery checks are processed independently from the other checks. If any checks do not find a service (or fail), other checks will still be processed.

If a discovery rule is changed during execution, then the current discovery execution will be aborted.

Every check of a service and a host (IP) performed by the network discovery module generates a discovery event.

_Service Discovered_ | The service is 'up' after it was 'down' or when discovered for the first time.  
---|---  
_Service Up_ | The service is 'up', after it was already 'up'.  
_Service Lost_ | The service is 'down' after it was 'up'.  
_Service Down_ | The service is 'down', after it was already 'down'.  
_Host Discovered_ | At least one service of a host is 'up' after all services of that host were 'down' or a service is discovered which belongs to a not registered host.  
_Host Up_ | At least one service of a host is 'up', after at least one service was already 'up'.  
_Host Lost_ | All services of a host are 'down' after at least one was 'up'.  
_Host Down_ | All services of a host are 'down', after they were already 'down'.  
  
#### Actions

Discovery events can be the basis of relevant [actions](/documentation/current/en/manual/config/notifications/action), such as:

  * Sending notifications
  * Adding/removing hosts
  * Enabling/disabling hosts
  * Adding hosts to a group
  * Removing hosts from a group
  * Adding tags to a host
  * Removing tags from a host
  * Linking a template to hosts/unlinking a template from hosts
  * Executing remote scripts

These actions can be configured with respect to the device type, IP, status, uptime/downtime, etc. For full details on configuring actions for network-discovery based events, see action [operation](/documentation/current/en/manual/config/notifications/action/operation) and [conditions](/documentation/current/en/manual/config/notifications/action/conditions) pages.

Since network discovery actions are event-based, they will be triggered both when a discovered host is online and when it is offline. It is highly recommended to add an action [condition](/documentation/current/en/manual/config/notifications/action/conditions) _Discovery status: up_ to avoid such actions as _Add host_ being triggered upon _Service Lost_ /_Service Down_ events. Otherwise, if a discovered host is manually removed, it will still generate _Service Lost_ /_Service Down_ events and will be recreated during the next discovery cycle.

Linking templates to a discovered host will fail collectively if any of the linkable templates has a unique entity (e.g. item key) that is the same as a unique entity (e.g. item key) already existing on the host or on another of the linkable templates.

##### Host creation

A host is added if the _Add host_ operation is selected. A host is also added, even if the _Add host_ operation is missing, if you select operations resulting in actions on a host. Such operations are:

  * enable host
  * disable host
  * add host to a host group
  * link template to a host

Created hosts are added to the _Discovered hosts_ group (by default, configurable in _Administration_ → _General_ → _[Other](/documentation/current/en/manual/web_interface/frontend_sections/administration/general#other-parameters)_). If you wish hosts to be added to another group, add a _Remove from host groups_ operation (specifying "Discovered hosts") and also add an _Add to host groups_ operation (specifying another host group), because a host must belong to a host group.

The IP address of the discovered device is the criterion for finding a host in the system. If a host with that IP address and interface type already exists, that host will be the target for performing operations.

If the IP address of the discovered host is changed or the interface is deleted, a new host will be created upon the next discovery.

##### Host naming

When adding hosts, a host name is the result of reverse DNS lookup or IP address if reverse lookup fails. Lookup is performed from the Zabbix server or Zabbix proxy, depending on which is doing the discovery. If lookup fails on the proxy, it is not retried on the server. If the host with such a name already exists, the next host would get **_2** appended to the name, then **_3** and so on.

It is also possible to override DNS/IP lookup and instead use an item value for host name, for example:

  * You may discover multiple servers with Zabbix agent running using a Zabbix agent item for discovery and assign proper names to them automatically, based on the string value returned by this item
  * You may discover multiple SNMP network devices using an SNMP agent item for discovery and assign proper names to them automatically, based on the string value returned by this item

If the host name has been set using an item value, it is not updated during the following discovery checks. If it is not possible to set host name using an item value, default value (DNS name) is used.

If a host already exists with the discovered IP address, a new host is not created. However, if the discovery action contains operations (link template, add to host group, etc), they are performed on the existing host.

##### Host removal

Hosts discovered by a network discovery rule are removed automatically from _Monitoring_ → _Discovery_ if a discovered entity is not in the rule's IP range any more. Hosts are removed immediately.

##### Interface creation when adding hosts

When hosts are added as a result of network discovery, they get interfaces created according to these rules:

  * the services detected - for example, if an SNMP check succeeded, an SNMP interface will be created
  * if a host responded both to Zabbix agent and SNMP requests, both types of interfaces will be created
  * if uniqueness criteria are Zabbix agent or SNMP-returned data, the first interface found for a host will be created as the default one. Other IP addresses will be added as additional interfaces. Action's conditions (such as Host IP) do not impact adding interfaces. _Note_ that this will work if all interfaces are discovered by the same discovery rule. If a different discovery rule discovers a different interface of the same host, an additional host will be added.
  * if a host responded to agent checks only, it will be created with an agent interface only. If it would start responding to SNMP later, additional SNMP interfaces would be added.
  * if 3 separate hosts were initially created, having been discovered by the "IP" uniqueness criteria, and then the discovery rule is modified so that hosts A, B and C have identical uniqueness criteria result, B and C are created as additional interfaces for A, the first host. The individual hosts B and C remain. In _Monitoring → Discovery_ the added interfaces will be displayed in the "Discovered device" column, in black font and indented, but the "Monitored host" column will only display A, the first created host. "Uptime/Downtime" is not measured for IPs that are considered to be additional interfaces.

#### Changing proxy setting

The hosts discovered by different proxies are always treated as different hosts. While this allows to perform discovery on matching IP ranges used by different subnets, changing proxy for an already monitored subnet is complicated because the proxy changes must be also applied to all discovered hosts.

For example the steps to replace proxy in a discovery rule:

  1. disable discovery rule
  2. sync proxy configuration
  3. replace the proxy in the discovery rule
  4. replace the proxy for all hosts discovered by this rule
  5. enable discovery rule