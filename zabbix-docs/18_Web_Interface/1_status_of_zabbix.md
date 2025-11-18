---
title: System information
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/reports/status_of_zabbix
downloaded: 2025-11-14 10:38:47
---

# 1 System information

#### Overview

In _Reports → System information_ , a summary of key Zabbix server and system data is displayed. System data is collected using [internal items](/documentation/current/en/manual/config/items/itemtypes/internal).

Note that in a high availability setup, it is possible to redirect the system information source (server instance). To do this, edit the _zabbix.conf.php_ file - uncomment and set `$ZBX_SERVER` or both `$ZBX_SERVER` and `$ZBX_SERVER_PORT` to a server other than the one shown active. Note that when setting `$ZBX_SERVER` only, a default value (10051) for `$ZBX_SERVER_PORT` will be used.

With the high availability setup enabled, a separate block is displayed below the system stats with details of high availability nodes. This block is visible to Zabbix _Super Admin_ users only.

_System information_ is also available as a dashboard [widget](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets).

#### System stats

![](/documentation/current/assets/en/manual/web_interface/system_information.png)

Displayed data:

_Zabbix server is running_ | Status of Zabbix server:  
**Yes** \- server is running  
**No** \- server is not running  
 _Note:_ To display the rest of the information the web, frontend needs the server to be running and there must be at least one trapper process started on the server (StartTrappers parameter in [zabbix_server.conf](/documentation/current/en/manual/appendix/config/zabbix_server) file > 0). | Location and port of Zabbix server.  
---|---|---  
_Zabbix server version_ | Current server version number is displayed.  
_Note:_ It is only displayed when Zabbix server is running. | Server version status is displayed:  
**Up to date** \- using the latest version;  
**New update available** \- a more up-to-date version is available;  
**Outdated** \- the full support period for this version has expired.  
This information is only available if software update check is enabled in Zabbix server [configuration](/documentation/current/en/manual/appendix/config/zabbix_server#allowsoftwareupdatecheck). Nothing is displayed if the last software update check was performed more than a week ago or no data exist about the current version.  
_Zabbix frontend version_ | Zabbix frontend version number is displayed. | Zabbix frontend version status is displayed:  
**Up to date** \- using the latest version;  
**New update available** \- a more up-to-date version is available;  
**Outdated** \- the full support period for this version has expired.  
This information is only available if software update check is enabled in Zabbix server [configuration](/documentation/current/en/manual/appendix/config/zabbix_server#allowsoftwareupdatecheck). Nothing is displayed if the last software update check was performed more than a week ago or no data exist about the current version.  
_Software update last checked_ | The date of the last Zabbix software update check is displayed.  
This information is only available if software update check is enabled in Zabbix server [configuration](/documentation/current/en/manual/appendix/config/zabbix_server#allowsoftwareupdatecheck). |   
_Latest release_ | The number of a newer release (if available) for the current Zabbix version is displayed.  
This information is only available if software update check is enabled in Zabbix server [configuration](/documentation/current/en/manual/appendix/config/zabbix_server#allowsoftwareupdatecheck). Nothing is displayed if the last software update check was performed more than a week ago or no data exist about the current version. | A link to the release notes of the latest available Zabbix release is displayed.  
_Number of hosts_ | Total number of hosts configured is displayed. | Number of monitored hosts/not monitored hosts.  
_Number of templates_ | Total number of templates is displayed. |   
_Number of items_ | Total number of items is displayed. | Number of monitored/disabled/unsupported host-level items.  
Items on disabled hosts are counted as disabled.  
_Number of triggers_ | Total number of triggers is displayed. | Number of enabled/disabled host-level triggers; split of the enabled triggers according to "Problem"/"OK" states.  
  
Triggers listed under the "OK" state include triggers with the status "Unknown".  
Triggers dependent on disabled items or assigned to disabled hosts are counted as disabled.  
_Number of users_ | Total number of users configured is displayed. | Number of users online.  
_Required server performance, new values per second_ | The expected number of new values processed by Zabbix server per second is displayed. | _Required server performance_ is an estimate and can be useful as a guideline. For precise numbers of values processed, use the `zabbix[wcache,values,all]` [internal item](/documentation/current/en/manual/config/items/itemtypes/internal).  
  
Enabled items from monitored hosts are included in the calculation. Log items are counted as one value per item update interval. Regular interval values are counted; flexible and scheduling interval values are not. The calculation is not adjusted during a "nodata" maintenance period. Trapper items are not counted.  
_Global scripts on Zabbix server_ | **Disabled** will be displayed in this field if global scripts are disabled on Zabbix server by setting EnableGlobalScripts=0 in server configuration. |   
_High availability cluster_ | Status of [high availability cluster](/documentation/current/en/manual/concepts/server/ha) for Zabbix server:  
**Disabled** \- standalone server  
**Enabled** \- at least one high availability node exists | If enabled, the failover delay is displayed.  
  
_System information_ will also display an error message in the following conditions:

  * The database used does not have the required character set or collation (UTF-8).
  * The version of the database is below or above the [supported range](/documentation/current/en/manual/installation/requirements#required-software) (available only to users with the _Super admin role_ type).
  * [Housekeeping](/documentation/current/en/manual/web_interface/frontend_sections/administration/housekeeping) for [TimescaleDB](/documentation/current/en/manual/appendix/install/timescaledb) is incorrectly configured (history or trend tables contain compressed chunks, but _Override item history period_ or _Override item trend period_ options are disabled).

#### High availability nodes

If [high availability cluster](/documentation/current/en/manual/concepts/server/ha) is enabled, then another block of data is displayed with the status of each high availability node.

![](/documentation/current/assets/en/manual/web_interface/ha_nodes.png)

Displayed data:

_Name_ | Node name, as defined in server configuration.  
---|---  
_Address_ | Node IP address and port.  
_Last access_ | Time of node last access.  
Hovering over the cell shows the timestamp of last access in long format.  
_Status_ | Node status. Table rows are sorted by these statuses in this priority order:  
**Active** \- node is up and working  
**Unavailable** \- node hasn't been seen for more than failover delay (you may want to find out why)  
**Stopped** \- node has been stopped or couldn't start (you may want to start it or delete it)  
**Standby** \- node is up and waiting