---
title: Hosts
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/data_collection/hosts
downloaded: 2025-11-14 10:39:08
---

# 4 Hosts

#### Overview

In the _Data collection → Hosts_ section users can configure and maintain hosts.

A listing of existing hosts with their details is displayed.

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/configuration/hosts.png)

Displayed data:

_Host menu_ | Click on the three dots icon to open the [host menu](/documentation/current/en/manual/web_interface/menu/host_menu).  
---|---  
_Name_ | Name of the host.  
Clicking on the host name opens the host [configuration form](/documentation/current/en/manual/config/hosts/host#configuration).  
An orange wrench icon ![](/documentation/current/assets/en/manual/web_interface/frontend_sections/configuration/maintenance_wrench_icon.png) after the host name indicates that this host is in maintenance. Maintenance details are displayed when the mouse pointer is positioned on the icon.  
_Entities (Items, Triggers, Graphs, Discovery, Web)_ | Clicking on the entity name will display items, triggers, etc., of the host.  
The number of the respective entities is displayed in gray.  
_Interface_ | The main interface of the host is displayed.  
_Proxy_ | Assigned proxies are displayed in this column:  
<Proxy name> \- host is monitored by standalone proxy (even if the proxy is part of proxy group);  
<Proxy group name: proxy name> \- host is monitored by proxy group, and Zabbix server has assigned a proxy to monitor the host;  
<Proxy group name> \- host is monitored by proxy group without any proxies, or if Zabbix server has not assigned a proxy to monitor the host;  
Nothing - host is not monitored by either proxy or proxy group.  
This column is only displayed if the _Monitored by_ filter option is set to 'Any', 'Proxy', or 'Proxy group'.  
_Templates_ | The templates linked to the host are displayed.  
If other templates are contained in the linked template, those are displayed in parentheses, separated by a comma.  
Clicking on a template name will open its configuration form.  
_Status_ | Host status is displayed - _Enabled_ or _Disabled_.  
By clicking on the status you can change it manually.  
Discovered hosts that have been lost are marked with an info icon. The tooltip text provides details on their status.  
_Availability_ | Host availability per configured interface is displayed.  
  
Availability icons represent host interface current status on Zabbix server. Therefore, if you disable a host in the frontend, its availability will update after Zabbix server has synchronized the configuration changes. Similarly, if you enable a host, its availability will update after Zabbix server has synchronized the configuration changes and polled the host.  
  
Availability icons represent only those interface types (Agent, SNMP, IPMI, JMX) that are configured.  
Hovering over the icon displays a pop-up with a list of all interfaces of the same type with details, status, and errors. For Agent interface, the pop-up displays interfaces (passive) and active checks. If a host has active checks only, the Agent interface icon is displayed even if the host does not have an Agent interface configured.  
The column is empty for hosts with no interfaces.  
  
The status of a single host interface is determined by the connection between an enabled item using the interface and the host. The status can be:  
**Available** \- the connection to the host was successful;  
**Not available** \- the connection to the host was unsuccessful (timeout, firewall issues, etc.);  
**Unknown** \- the connection to the host has not been attempted or the result is unknown.  
For additional details on how Zabbix server determines interface status, see [Unknown interface status](/documentation/current/en/manual/web_interface/frontend_sections/data_collection/hosts#unknown-interface-status) and [Unreachable/unavailable host interface settings](/documentation/current/en/manual/appendix/items/unreachability).  
  
The status of all host interfaces of a single type (Agent, SNMP, IPMI, JMX) is determined by those interfaces that are used by at least one enabled item. The status is indicated by the icon color:  
**Green** \- all interfaces are available;  
**Yellow** \- at least one interface is not available, and at least one is available or unknown;  
**Red** \- all interfaces are not available;  
**Gray** \- at least one interface is unknown, but none are not available.  
  
**Active check availability.** If at least one active check is enabled on the host, active checks also affect the total Agent interface availability as described above. To determine active check availability, heartbeat messages are sent in the agent active check thread. The frequency of heartbeat messages is controlled by the `HeartbeatFrequency` parameter in Zabbix [agent](/documentation/current/en/manual/appendix/config/zabbix_agentd) or [agent 2](/documentation/current/en/manual/appendix/config/zabbix_agent2) configuration (default 60 seconds, range 0-3600). Active checks are considered not available when the active check heartbeat is older than 2 x HeartbeatFrequency seconds.  
**Note:** Zabbix agents older than version 6.2.x do not send active check heartbeats, so the availability of their hosts remains unknown.  
_Agent encryption_ | Encryption status for connections to the host and from the host is displayed:  
**None** \- no encryption;  
**PSK** \- using pre-shared key;  
**Cert** \- using certificate.  
_Info_ | Error information (if any) regarding the host is displayed.  
_Tags_ | [Tags](/documentation/current/en/manual/config/tagging) of the host with macros unresolved.  
  
To configure a new host, click on the _Host Wizard_ or _Create host_ button in the upper-right corner. To import a host from a YAML, XML, or JSON file, click on the _Import_ button in the upper-right corner.

##### Mass editing options

Buttons below the list offer some mass editing options:

  * _Enable_ \- change host status to _Monitored_ ;
  * _Disable_ \- change host status to _Not monitored_ ;
  * _Export_ \- export the hosts to a YAML, XML or JSON file;
  * _Mass update_ \- [update several properties](/documentation/current/en/manual/config/hosts/hostupdate) for a number of hosts at once;
  * _Delete_ \- delete the hosts.

To use these options, mark the checkboxes before the respective hosts, then click on the required button.

#### Using filter

You can use the filter to display only the hosts you are interested in. For better search performance, data is searched with macros unresolved.

The _Filter_ icon is available at the upper-right corner. Clicking on it will open a filter where you can specify the desired filtering criteria.

![](/documentation/current/assets/en/manual/web_interface/host_filter.png)

_Host groups_ | Filter by one or more host groups.  
Specifying a parent host group implicitly selects all nested host groups.  
---|---  
_Templates_ | Filter by linked templates.  
_Name_ | Filter by visible host name.  
_DNS_ | Filter by DNS name.  
_IP_ | Filter by IP address.  
_Port_ | Filter by port number.  
_Status_ | Filter by host status.  
_Monitored by_ | Filter hosts that are monitored by Zabbix server, proxy, or proxy group.  
_Proxies_ | Filter hosts that are monitored by the proxies specified here. This field is only available if "Proxy" is selected in the _Monitored by_ field.  
_Proxy groups_ | Filter hosts that are monitored by the proxy groups specified here. This field is only available if "Proxy group" is selected in the _Monitored by_ field.  
_Tags_ | Filter by host tag name and value.  
It is possible to include as well as exclude specific tags and tag values. Several conditions can be set. Tag name matching is always case-sensitive.  
  
There are several operators available for each condition:  
**Exists** \- include the specified tag names;  
**Equals** \- include the specified tag names and values (case-sensitive);  
**Contains** \- include the specified tag names where the tag values contain the entered string (substring match, case-insensitive);  
**Does not exist** \- exclude the specified tag names;  
**Does not equal** \- exclude the specified tag names and values (case-sensitive);  
**Does not contain** \- exclude the specified tag names where the tag values contain the entered string (substring match, case-insensitive).  
  
There are two calculation types for conditions:  
**And/Or** \- all conditions must be met, conditions having the same tag name will be grouped by the Or condition;  
**Or** \- enough if one condition is met.  
  
#### Unknown interface status

Zabbix server displays the "Unknown" status for a host interface (Agent, SNMP, IPMI, JMX) in the following cases:

  * Host is disabled.
  * Host is set to be monitored by proxy, different proxy, or server if it was previously monitored by proxy.
  * Host is monitored by a proxy that appears to be offline (no updates received from the proxy during the maximum heartbeat interval - 1 hour).
  * All host items with that interface type are disabled.
  * No pollers for that interface type have been configured (for example, the [`StartAgentPollers`](/documentation/current/en/manual/appendix/config/zabbix_server#startagentpollers) or [`StartSNMPPollers`](/documentation/current/en/manual/appendix/config/zabbix_server#startsnmppollers) server configuration parameter is set to `0`).

Interface availability is set to "Unknown" after Zabbix server configuration cache synchronization.

Interface availability (Available/Not available) on hosts monitored by proxies is restored after proxy configuration cache synchronization.