---
title: Host availability
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/host_availability
downloaded: 2025-11-14 10:38:11
---

# 12 Host availability

#### Overview

In the host availability widget, high-level statistics about host availability are displayed in colored columns/lines, depending on the chosen layout.

Horizontal display (columns):

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/dashboards/availability_h.png)

Vertical display (lines):

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/dashboards/availability_v.png)

Host availability in each column/line is counted as follows:

  * _Available_ \- hosts with all interfaces available
  * _Not available_ \- hosts with all interfaces not available
  * _Mixed_ \- hosts with at least one interface unavailable and at least one either available or unknown; others can have any value, including "unknown"
  * _Unknown_ \- hosts with at least one interface unknown (none unavailable)
  * _Total_ \- total of all hosts

For Zabbix agent (active checks), the _Mixed_ cell will always be empty since this type of items cannot have multiple interfaces.

#### Configuration

To configure, select _Host availability_ as type:

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/host_availability.png)

In addition to the parameters that are [common](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#common-parameters) for all widgets, you may set the following specific options:

_Host groups_ | Select host groups.  
Alternatively, select a compatible widget as the [data source](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/#dynamic-parameters) for host groups.  
This field is auto-complete, so starting to type the name of a group will offer a dropdown of matching groups.  
This parameter is not available when configuring the widget on a [template dashboard](/documentation/current/en/manual/config/templates/template#adding-dashboards).  
---|---  
_Interface type_ | Select which host interfaces you want to see availability data for.  
Availability of all interfaces is displayed by default if nothing is selected.  
_Layout_ | Select horizontal display (columns) or vertical display (lines).  
_Include hosts in maintenance_ | Include hosts that are in maintenance in the statistics.  
This parameter is labeled _Show data in maintenance_ when configuring the widget on a [template dashboard](/documentation/current/en/manual/config/templates/template#adding-dashboards).  
_Show only totals_ | If checked, the total of hosts, without breakdown by interfaces, is displayed. This option is disabled if only one interface is selected.