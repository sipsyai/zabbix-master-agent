---
title: Proxy groups
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/administration/proxy_groups
downloaded: 2025-11-14 10:39:30
---

# 5 Proxy groups

#### Overview

In _Administration → Proxy groups_ it is possible to configure proxy groups.

Proxy groups are used in [proxy load balancing](/documentation/current/en/manual/distributed_monitoring/proxies/ha) with automated distribution of hosts between proxies and high availability between proxies.

#### Proxy groups

A listing of existing proxy groups with their details is displayed.

![](/documentation/current/assets/en/manual/web_interface/proxy_groups.png)

Displayed data:

_Name_ | Name of the proxy group. Clicking on the proxy group name opens the proxy group [configuration form](/documentation/current/en/manual/distributed_monitoring/proxies/ha#configuring-a-proxy-group).  
---|---  
_State_ | State of the proxy group (displayed if group contains at least one proxy):  
**Unknown** \- group was created while Zabbix server was down, or server has not yet updated the state;  
**Online** \- minimum number of proxies have communicated with Zabbix server within the failover period;  
**Degrading** \- group is going offline shortly due to online proxies falling below the _Minimum proxies_ threshold;  
**Offline** \- fewer than minimum number of proxies have communicated with Zabbix server within the failover period;  
**Recovering** \- group is coming back online shortly due to online proxies reaching the _Minimum proxies_ threshold.  
Proxy group state can be monitored with [zabbix[proxy group,<name>,state]](/documentation/current/en/manual/config/items/itemtypes/internal#proxy.group.d) and [zabbix[proxy group,discovery]](/documentation/current/en/manual/config/items/itemtypes/internal#proxy.group.e) items.  
_Failover period_ | Period during which a proxy in the proxy group must communicate with Zabbix server to be considered online.  
_Online proxies_ | Number of online proxies (displayed in red if below the group minimum).  
_Minimum proxies_ | Minimum number of [online proxies](/documentation/current/en/manual/web_interface/frontend_sections/administration/proxies) required to keep the proxy group online.  
_Proxies_ | Count of proxies in the group and a list of proxies in the group, with links to the proxy configuration form.  
The maximum number of listed proxies is limited by the _[Max count of elements to show inside table cell](/documentation/current/en/manual/web_interface/frontend_sections/administration/general#gui)_ value.  
  
To configure a new proxy group, click on the _Create proxy groups_ button in the upper-right corner.

##### Mass editing options

Buttons below the list offer some mass-editing options:

  * _Delete_ \- delete the proxy groups.

To use these options, mark the checkboxes before the respective proxy groups, then click on the required button.

##### Using filter

You can use the filter to display only the proxy groups you are interested in. For better search performance, data is searched with macros unresolved.

The _Filter_ link is available above the list of proxy groups. If you click on it, a filter becomes available where you can filter proxy groups by name and status.

![](/documentation/current/assets/en/manual/web_interface/proxy_group_filter.png)