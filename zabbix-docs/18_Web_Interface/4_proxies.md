---
title: Proxies
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/administration/proxies
downloaded: 2025-11-14 10:39:29
---

# 4 Proxies

#### Overview

In the _Administration → Proxies_ section proxies for [distributed monitoring](/documentation/current/en/manual/distributed_monitoring) can be configured in the Zabbix frontend.

#### Proxies

A listing of existing proxies with their details is displayed.

![](/documentation/current/assets/en/manual/web_interface/proxies.png)

Displayed data:

_Name_ | Name of the proxy.  
Clicking on the proxy name opens the proxy [configuration form](/documentation/current/en/manual/distributed_monitoring/proxies#configuration).  
If the proxy belongs to a proxy group, the group name is displayed before the proxy name as a gray link. Clicking on the group name opens the proxy group [configuration form](/documentation/current/en/manual/distributed_monitoring/proxies/ha#configuring-a-proxy-group).  
---|---  
_Mode_ | Proxy mode - _Active_ or _Passive_.  
_Encryption_ | Encryption status for connections from the proxy:  
**None** \- no encryption;  
**PSK** \- using pre-shared key;  
**Cert** \- using certificate.  
_State_ | State of the proxy:  
**Unknown** \- proxy was created while Zabbix server was down, or server has not yet updated the state;  
**Online** \- proxy has communicated with Zabbix server (passive proxy responded to server request; active proxy sent request) within the failover period;  
**Offline** \- proxy has not communicated with Zabbix server within the failover period.  
_Version_ | Proxy version (three digit version number). If proxy is outdated or unsupported, version number is highlighted (red) and info status icon (yellow or red) is displayed. Hover over the icon for details.  
_Last seen (age)_ | The time when the proxy was last seen by the server.  
_Item count_ | The number of enabled items on enabled hosts assigned to the proxy.  
_Required vps_ | Required proxy performance (the number of values that need to be collected per second).  
_Hosts_ | Count of enabled hosts assigned to the proxy and a list of hosts monitored by the proxy.  
Clicking on the host name opens the host configuration form.  
  
To configure a new proxy, click on the _Create proxy_ button in the upper-right corner.

##### Mass editing options

Buttons below the list offer some mass-editing options:

  * _Refresh configuration_ \- refresh configuration of the proxies;
  * _Enable hosts_ \- change the status of hosts monitored by the proxy to _Monitored_ ;
  * _Disable hosts_ \- change the status of hosts monitored by the proxy to _Not monitored_ ;
  * _Delete_ \- delete the proxies.

To use these options, mark the checkboxes before the respective proxies, then click on the required button.

##### Using filter

You can use the filter to display only the proxies you are interested in. For better search performance, data is searched with macros unresolved.

The _Filter_ link is available above the list of proxies. If you click on it, a filter becomes available where you can filter proxies by name, mode and version. Note that the filter option _Outdated_ displays both outdated (partially supported) and unsupported proxies.

![](/documentation/current/assets/en/manual/web_interface/proxies_filter1.png)