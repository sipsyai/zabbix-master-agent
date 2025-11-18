---
title: System information
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/system
downloaded: 2025-11-14 10:38:24
---

# 26 System information  
  
#### Overview

This widget displays the same information as in _Reports_ → _[System information](/documentation/current/en/manual/web_interface/frontend_sections/reports/status_of_zabbix)_ , however, a single dashboard widget can only display either the system stats or the high availability nodes at a time (not both).

#### Configuration

To configure, select _System information_ as type:

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/system_information.png)

In addition to the parameters that are [common](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#common-parameters) for all widgets, you may set the following specific options:

_Show_ | Select what to display:  
**System stats** \- display a summary of key Zabbix server and system data;  
**High availability nodes** \- display the status of high availability nodes (if [high availability cluster](/documentation/current/en/manual/concepts/server/ha) is enabled).  
---|---  
_Show software update check details_ | Mark the checkbox to display Zabbix software update check details.  
This option is only available if software update check is enabled in Zabbix server [configuration](/documentation/current/en/manual/appendix/config/zabbix_server#allowsoftwareupdatecheck) and "System stats" is selected in the _Show_ field.