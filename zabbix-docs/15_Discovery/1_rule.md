---
title: Configuring a network discovery rule
source: https://www.zabbix.com/documentation/current/en/manual/discovery/network_discovery/rule
downloaded: 2025-11-14 10:37:16
---

# 1 Configuring a network discovery rule

#### Overview

To configure a network discovery rule used by Zabbix to discover hosts and services:

  * Go to _Data collection → Discovery_
  * Click on _Create discovery rule_ (or on the rule name to edit an existing one)
  * Edit the discovery rule attributes

#### Rule attributes

![](/documentation/current/assets/en/manual/discovery/network_discovery/d_rule.png)

All mandatory input fields are marked with a red asterisk.

_Name_ | Unique name of the rule. For example, "Local network".  
---|---  
_Discovery by_ | Discovery is performed by:  
**Server** \- by Zabbix server  
**Proxy** \- by Zabbix proxy (selected in the proxy name field)  
_IP range_ | The range of IP addresses for discovery. It may have the following formats:  
Single IP: 192.168.1.33  
Range of IP addresses: 192.168.1-10.1-255. The range is limited by the total number of covered addresses (less than 64K).  
IP mask: 192.168.4.0/24  
supported IP masks:  
/16 - /30 for IPv4 addresses  
/112 - /128 for IPv6 addresses  
List: 192.168.1.1-255, 192.168.2.1-100, 192.168.2.200, 192.168.4.0/24  
This field supports spaces, tabulation and multiple lines.  
_Update interval_ | This parameter defines how often Zabbix will execute the rule.  
The interval is measured after the execution of previous discovery instance ends so there is no overlap.  
[Time suffixes](/documentation/current/en/manual/appendix/suffixes) are supported, e.g. 30s, 1m, 2h, 1d.  
[User macros](/documentation/current/en/manual/config/macros/user_macros) are supported.  
_Note_ that if a user macro is used and its value is changed (e.g. 1w → 1h), the next check will be executed according to the previous value (far in the future with the example values).  
_Maximum concurrent checks per type_ | Set the maximum number of discovery threads (workers) per service check for parallel processing of discovery checks:  
**One** \- one thread  
**Unlimited** \- unlimited number of threads (but no more than in the [StartDiscoverers](/documentation/current/en/manual/appendix/config/zabbix_server#startdiscoverers) parameter)  
**Custom** \- set a custom number of threads (0-999)  
Note that all discovery rules with SNMPv3 asynchronous service checks are processed by one worker due to the peculiarities of libsnmp implementation, i.e. increasing the number of workers will not increase the discovery speed.  
_Checks_ | Zabbix will use this list of checks for discovery. Click on ![](/documentation/current/assets/en/manual/discovery/network_discovery/add_link.png) to configure a new check in a popup window.  
Supported checks: SSH, LDAP, SMTP, FTP, HTTP, HTTPS, POP, NNTP, IMAP, TCP, Telnet, Zabbix agent, SNMPv1 agent, SNMPv2 agent, SNMPv3 agent, ICMP ping.  
A protocol-based discovery uses the **net.tcp.service[]** functionality to test each host, except for SNMP which queries an SNMP OID. Zabbix agent is tested by querying an item in unencrypted mode. Please see [agent items](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent) for more details.  
The 'Ports' parameter may be one of following:  
Single port: 22  
Range of ports: 22-45  
List: 22-45,55,60-70  
Since Zabbix 7.0. all service checks are performed asynchronously, except for LDAP checks.  
Since Zabbix 7.0 HTTP/HTTPs checking is done via libcurl. If Zabbix server/proxy is compiled without libcurl, then HTTP checks will work like in previous versions (i.e. as TCP checks), but HTTPS checks will not work.  
_Device uniqueness criteria_ | Uniqueness criteria may be:  
**IP address** \- do not process multiple single-IP devices. If a device with the same IP already exists it will be considered already discovered and a new host will not be added.  
**< discovery check>** \- either Zabbix agent or SNMP agent check.  
Note that uniqueness criteria used during discovery is not the same as host identification in the system when performing actions. Uniqueness criteria during discovery define whether two or more discovered devices are the same (or different), whereas only the IP address is the criterion for host identification in Zabbix (see [Host creation](/documentation/current/en/manual/discovery/network_discovery#host-creation)).  
_Host name_ | Set the technical host name of a created host using:  
**DNS name** \- DNS name (default)  
**IP address** \- IP address  
**< discovery check>** \- received string value of the discovery check (e.g. Zabbix agent, SNMP agent check)  
See also: [Host naming](/documentation/current/en/manual/discovery/network_discovery#host-naming).  
_Visible name_ | Set the visible host name of a created host using:  
**Host name** \- technical host name (default)  
**DNS name** \- DNS name  
**IP address** \- IP address  
**< discovery check>** \- received string value of the discovery check (e.g. Zabbix agent, SNMP agent check)  
See also: [Host naming](/documentation/current/en/manual/discovery/network_discovery#host-naming).  
_Enabled_ | With the check-box marked the rule is active and will be executed by Zabbix server.  
If unmarked, the rule is not active. It won't be executed.  
  
##### Exceeding file descriptor limit

In case of large number of concurrent checks, it is possible to exhaust the file descriptor limit for the [discovery manager](/documentation/current/en/manual/concepts/server#server-process-types-and-threads).

The number of file descriptors required for detection equates to the number of discovery workers * 1000. By default, there are 5 [discovery workers](/documentation/current/en/manual/appendix/config/zabbix_server#startdiscoverers), while the soft limit of the system is approximately 1024.

If this limit is approached, Zabbix will reduce the default number of concurrent checks per type for each worker and write a warning to the log file. But, if the user has set a higher value for _Maximum concurrent checks per type_ than the value calculated by Zabbix, Zabbix will use the user-defined value for one worker.

#### A real life scenario

In this example, we would like to set up network discovery for the local network having an IP range of 192.168.1.1-192.168.1.254.

In our scenario we want to:

  * discover those hosts that have Zabbix agent running
  * run discovery every 10 minutes
  * add a host to monitoring if the host uptime is more than 1 hour
  * remove hosts if the host downtime is more than 24 hours
  * add Linux hosts to the "Linux servers" group
  * add Windows hosts to the "Windows servers" group
  * use the template _Linux_ for Linux hosts
  * use the template _Windows_ for Windows hosts

##### Step 1

Defining a network discovery rule for our IP range.

![](/documentation/current/assets/en/manual/discovery/network_discovery/discovery.png)

Zabbix will try to discover hosts in the IP range of 192.168.1.1-192.168.1.254 by connecting to Zabbix agents and getting the value from the **system.uname** key. The value received from the agent can be used to name the hosts and also to apply different actions for different operating systems. For example, link Windows servers to the template _Windows_ , Linux servers to the template _Linux_.

The rule will be executed every 10 minutes.

When this rule is added, Zabbix will automatically start the discovery and generation of the discovery-based events for further processing.

##### Step 2

Defining a discovery [action](/documentation/current/en/manual/config/notifications/action) for adding the discovered Linux servers to the respective group/template.

![](/documentation/current/assets/en/manual/discovery/network_discovery/discov_action.png)

The action will be activated if:

  * the "Zabbix agent" service is "up"
  * the value of system.uname (the Zabbix agent key we used in rule definition) contains "Linux"
  * Uptime is 1 hour (3600 seconds) or more

![](/documentation/current/assets/en/manual/discovery/network_discovery/discov_action_b.png)

The action will execute the following operations:

  * add the discovered host to the "Linux servers" group (and also add host if it wasn't added previously)
  * link host to the _Linux_ template. Zabbix will automatically start monitoring the host using items and triggers from the "Linux" template.

##### Step 3

Defining a discovery action for adding the discovered Windows servers to the respective group/template.

![](/documentation/current/assets/en/manual/discovery/network_discovery/discov_action_win.png)

![](/documentation/current/assets/en/manual/discovery/network_discovery/discov_action_win_b.png)

##### Step 4

Defining a discovery action for removing lost servers.

![](/documentation/current/assets/en/manual/discovery/network_discovery/discov_action_remove.png)

![](/documentation/current/assets/en/manual/discovery/network_discovery/discov_action_remove_b.png)

A server will be removed if "Zabbix agent" service is 'down' for more than 24 hours (86400 seconds).