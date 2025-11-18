---
title: Hosts
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/monitoring/hosts
downloaded: 2025-11-14 10:38:34
---

# 2 Hosts

#### Overview

The _Monitoring → Hosts_ section displays a full list of monitored hosts with detailed information about host interface, availability, tags, current problems, status (enabled/disabled), and links to easily navigate to the host's latest data, problem history, graphs, dashboards and web scenarios.

![](/documentation/current/assets/en/manual/web_interface/monitoring_hosts.png)

_Name_ | The visible host name. Clicking on the name brings up the [host menu](/documentation/current/en/manual/web_interface/menu/host_menu).  
An orange wrench icon ![](/documentation/current/assets/en/manual/web_interface/frontend_sections/configuration/maintenance_wrench_icon.png) after the name indicates that this host is in maintenance.  
Click on the column header to sort hosts by name in ascending or descending order.  
---|---  
_Interface_ | The main interface of the host is displayed.  
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
_Tags_ | [Tags](/documentation/current/en/manual/config/tagging) of the host and all linked templates, with macros unresolved.  
_Status_ | Host status - _Enabled_ or _Disabled_.  
Click on the column header to sort hosts by status in ascending or descending order.  
_Latest data_ | Clicking on the link will open the _Monitoring - Latest data_ page with all the latest data collected from the host.  
The number of items with latest data is displayed in gray.  
_Problems_ | The number of open host problems sorted by severity. The color of the square indicates problem severity. The number on the square means the number of problems for the given severity.  
Clicking on the icon will open _Monitoring - Problems_ page for the current host.   
If a host has no problems, a link to the _Problems_ section for this host is displayed as text.   
Use the filter to select whether suppressed problems should be included (not included by default).  
_Graphs_ | Clicking on the link will display graphs configured for the host. The number of graphs is displayed in gray.  
If a host has no graphs, the link is disabled (gray text) and no number is displayed.  
_Dashboards_ | Clicking on the link will display dashboards configured for the host. The number of dashboards is displayed in gray.  
If a host has no dashboards, the link is disabled (gray text) and no number is displayed.  
_Web_ | Clicking on the link will display web scenarios configured for the host. The number of web scenarios is displayed in gray.  
If a host has no web scenarios, the link is disabled (gray text) and no number is displayed.  
  
##### Buttons

_Create host_ allows to create a [new host](/documentation/current/en/manual/config/hosts/host). This button is available for Admin and Super Admin users only.

View mode buttons being common for all sections are described on the [Monitoring](/documentation/current/en/manual/web_interface/frontend_sections/monitoring#view-mode-buttons) page.

#### Using filter

You can use the filter to display only the hosts you are interested in. For better search performance, data is searched with macros unresolved.

The filter is located above the table. It is possible to filter hosts by name, host group, IP or DNS, interface port, tags, problem severity, status (enabled/disabled/any); you can also select whether to display suppressed problems and hosts that are currently in maintenance.

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/monitoring_hosts_filter.png)

_Name_ | Filter by visible host name.  
---|---  
_Host groups_ | Filter by one or more host groups.  
Specifying a parent host group implicitly selects all nested host groups.  
_IP_ | Filter by IP address.  
_DNS_ | Filter by DNS name.  
_Port_ | Filter by port number.  
_Severity_ | Filter by problem severity. By default problems of all severities are displayed. Problems are displayed if not suppressed.  
_Status_ | Filter by host status.  
_Tags_ | Filter by host tag name and value. Hosts can be filtered by host-level tags as well as tags from all linked templates, including nested templates.  
It is possible to include as well as exclude specific tags and tag values. Several conditions can be set. Tag name matching is always case-sensitive.  
There are several operators available for each condition:  
**Exists** \- include the specified tag names  
**Equals** \- include the specified tag names and values (case-sensitive)  
**Contains** \- include the specified tag names where the tag values contain the entered string (substring match, case-insensitive)  
**Does not exist** \- exclude the specified tag names  
**Does not equal** \- exclude the specified tag names and values (case-sensitive)  
**Does not contain** \- exclude the specified tag names where the tag values contain the entered string (substring match, case-insensitive)  
There are two calculation types for conditions:  
**And/Or** \- all conditions must be met, conditions having the same tag name will be grouped by the Or condition  
**Or** \- enough if one condition is met  
_Show hosts in maintenance_ | Mark the checkbox to display hosts that are in maintenance (displayed by default).  
_Show suppressed problems_ | Mark the checkbox to display problems that would otherwise be suppressed (not shown) because of host maintenance or single [problem suppression](/documentation/current/en/manual/acknowledgment/suppression).  
  
##### Saving filter

Favorite filter settings can be saved as tabs and then quickly accessed by clicking on the respective tab above the filter.

See more details about [saving filters](/documentation/current/en/manual/web_interface/frontend_sections/monitoring/problems#tabs-for-favorite-filters).