---
title: Host card
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/host_card
downloaded: 2025-11-14 10:38:12
---

# 13 Host card  
  
#### Overview

The Host card widget provides comprehensive and customizable information about a single host. The host can be specified through the widget configuration, selected from another compatible widget, or located using the host selector at the dashboard level.

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/host_card.png)

Top part of the widget contains the name of a host and the number of host problems grouped by severity. If a host is disabled, the text _Disabled_ will be written next to the host name. If a host is in maintenance, the maintenance icon will be displayed next to the host name. Other sections of the widget can be customized as required.

This widget automatically adjusts the layout based on the width. To rearrange widget sections into multiple columns, expand the widget horizontally.

#### Configuration

To configure, select _Host card_ as type:

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/host_card_conf.png)

In addition to the parameters that are [common](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#common-parameters) for all widgets, you may set the following specific parameters:

_Host_ | Select the host.  
Alternatively, select a compatible widget or the dashboard as the [data source](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/#dynamic-parameters).  
This field provides matching suggestions as you start typing a name. You can also press the Select button to choose manually.  
  
This parameter is not available when configuring the widget on a [template dashboard](/documentation/current/en/manual/config/templates/template#adding-dashboards).  
---|---  
_Show suppressed problems_ | Mark this checkbox to include suppressed problems into problem calculation.  
_Show_ | Configure up to eight sections to be displayed by the widget. The sections can be rearranged by dragging and dropping.  
| _Host groups_ | Host groups the host belongs to.  
_Description_ | Host description.  
_Monitoring_ | Quick links for navigating to dashboards, latest data, graphs, and web scenarios of the host. The number next to each link indicates the number of entities.  
_Availability_ | Host availability by interface.  
_Monitored by_ | Zabbix server, proxy, or proxy group the host is monitored by.  
_Templates_ | Templates linked to the host.  
_Inventory_ | Display host inventory fields. If selected, an _Inventory fields_ parameter will appear, allowing to specify which fields should be displayed.  
_Tags_ | Host tags.  
_Inventory fields_ | Specify the inventory fields to be displayed.  
This field provides matching suggestions as you start typing a name. Alternatively, you can press the Select button to choose manually.  
If no inventory fields are specified, all populated inventory fields will be displayed.   
  
This parameter becomes available only when _Inventory_ is selected in the _Show_ section.