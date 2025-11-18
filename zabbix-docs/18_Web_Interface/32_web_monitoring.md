---
title: Web monitoring
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/web_monitoring
downloaded: 2025-11-14 10:38:30
---

# 32 Web monitoring

#### Overview

This widget displays a status summary of the active web monitoring scenarios. See the Web monitoring widget section for detailed information.

#### Configuration

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/web_monitoring.png)

In cases when a user does not have permission to access certain widget elements, that element's name will appear as _Inaccessible_ during the widget's configuration. This results in _Inaccessible Item, Inaccessible Host, Inaccessible Group, Inaccessible Map, and Inaccessible Graph_ appearing instead of the "real" name of the element.

In addition to the parameters that are [common](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#common-parameters) for all widgets, you may set the following specific options:

_Host groups_ | Select host groups to display in the widget.  
Alternatively, select a compatible widget as the [data source](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/#dynamic-parameters) for host groups.  
This field is auto-complete, so starting to type the name of a group will offer a dropdown of matching groups.  
Specifying a parent host group implicitly selects all nested host groups.  
Host data from these host groups will be displayed in the widget; if no host groups are entered, all host groups will be displayed.  
This parameter is not available when configuring the widget on a [template dashboard](/documentation/current/en/manual/config/templates/template#adding-dashboards).  
---|---  
_Exclude host groups_ | Select host groups to hide from the widget.  
This field is auto-complete, so starting to type the name of a group will offer a dropdown of matching groups.  
Specifying a parent host group implicitly selects all nested host groups.  
Host data from these host groups will not be displayed in the widget. For example, hosts 001, 002, 003 may be in Group A and hosts 002, 003 in Group B as well. If we select to _show_ Group A and _exclude_ Group B at the same time, only data from host 001 will be displayed in the dashboard.  
This parameter is not available when configuring the widget on a [template dashboard](/documentation/current/en/manual/config/templates/template#adding-dashboards).  
_Hosts_ | Select hosts to display in the widget.  
Alternatively, select a compatible widget or the dashboard as the [data source](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/#dynamic-parameters) for hosts.  
This field is auto-complete, so starting to type the name of a host will offer a dropdown of matching hosts.  
If no hosts are entered, all hosts will be displayed.  
This parameter is not available when configuring the widget on a [template dashboard](/documentation/current/en/manual/config/templates/template#adding-dashboards).  
_Scenario tags_ | Specify tags to limit the number of web scenarios displayed in the widget.  
It is possible to include as well as exclude specific tags and tag values. Several conditions can be set. Tag name matching is always case-sensitive.  
  
There are several operators available for each condition:  
**Exists** \- include the specified tag names;  
**Equals** \- include the specified tag names and values (case-sensitive);  
**Contains** \- include the specified tag names where the tag values contain the entered string (substring match, case-insensitive);  
**Does not exist** \- exclude the specified tag names;  
**Does not equal** \- exclude the specified tag names and values (case-sensitive);  
**Does not contain** \- exclude the specified tag names where the tag values contain the entered string (substring match, case-insensitive).  
  
There are two calculation types for conditions:  
**And/Or** \- all conditions must be met, conditions having the same tag name will be grouped by the _Or_ condition;  
**Or** \- enough if one condition is met.  
_Show hosts in maintenance_ | Include hosts that are in maintenance in the statistics.  
This parameter is labeled _Show data in maintenance_ when configuring the widget on a [template dashboard](/documentation/current/en/manual/config/templates/template#adding-dashboards).  
  
#### Web monitoring widget

Once you have completed the configuration, you might like to see the widget with the data it displays. To do it, go to _Dashboards_ , click on the name of a dashboard where you created the widget.

In this example, you can see the widget named "Zabbix frontend" displaying the status of the web monitoring for three host groups: "Internal network," "Linux servers," and "Web servers."

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/web_monitoring_2.png)

A web monitoring widget displays the following information:

  * a name of a widget; below it, there are four columns: 
    * _Host group_ \- displays a list of host groups that contain hosts having web scenarios configured;
    * _Ok_ \- displays a number of web scenarios (in green color) when two conditions are observed: 
      * Zabbix has collected the latest data for a web scenario(s);
      * all steps that were configured in a [web scenario](/documentation/current/en/manual/web_monitoring/example#scenario) are in "Ok" _[Status](/documentation/current/en/manual/web_monitoring/example#check-the-results)_.
    * _Failed_ \- displays a number of web scenarios (in red color), which have some failed steps: 
      * click on the host name, and it will open a new window; the _Status_ column provides detailed information (in red color) on the step where Zabbix failed to collect the data; and also,
      * gives a hint for the parameter that has to be corrected in the [configuration form](/documentation/current/en/manual/web_monitoring/example#scenario).

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/web_monitoring_3.png)

  * _Unknown_ \- displays a number of web scenarios (in grey color) for which Zabbix has neither collected data, nor has an information about the failed steps.

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/web_monitoring_4.png)

##### Viewing the status and data

Clickable links in the widget allow to easily navigate and quickly acquire a full information on each web scenario. Thus, to view:

  * the [Status](/documentation/current/en/manual/web_monitoring/example#check-the-results) of a web scenario, click on the name of a host group.
  * more detailed statistics, click on the scenario name. In this example it is "Zabbix frontend".
  * the details in the case of _Failed_ status, click on a host group name; in the window that opens, click on a web scenario name in the _Name_ column; it will open more detailed information on the configured steps for which Zabbix failed to collect the data.

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/web_monitoring_5.png)

Now, you can return to the [web scenario configuration form](/documentation/current/en/manual/web_monitoring/example#scenario) and correct your settings.

To view the details in the case of _Unknown_ status, you can repeat the same steps as explained for _Failed_.

At the first monitoring instance, a web scenario is always displayed in _Unknown_ state, which is switched to _Failed_ or _Ok_ state right after the first check. In the case when a host is monitored by the proxy, the status change occurs in accordance with the data collection frequency configured on the proxy.