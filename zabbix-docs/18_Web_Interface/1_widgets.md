---
title: Dashboard widgets
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets
downloaded: 2025-11-14 10:37:59
---

# 1 Dashboard widgets

#### Overview

This section provides the details of parameters that are common for [dashboard](/documentation/current/en/manual/web_interface/frontend_sections/dashboards) widgets.

#### Common parameters

The following parameters are common for every single widget:

_Name_ | Enter a widget name.  
---|---  
_Refresh interval_ | Configure the default refresh interval.  
  
Default refresh intervals for widgets range from _No refresh_ to _15 minutes_ depending on the type of the widget. For example:  
\- _No refresh_ for _URL_ widget;  
\- _1 minute_ for _Action log_ widget;  
\- _15 minutes_ for _Clock_ widget.  
  
Refresh intervals can be set to a default value for all users. Switch the dashboard to [editing mode](/documentation/current/en/manual/web_interface/frontend_sections/dashboards#viewing-a-dashboard), click the [edit a widget](/documentation/current/en/manual/web_interface/frontend_sections/dashboards#editing-widgets) button and select the desired refresh interval from the dropdown list.  
  
Each user can also set their own widget refresh interval. In dashboard [viewing mode](/documentation/current/en/manual/web_interface/frontend_sections/dashboards#viewing-a-dashboard), click the three dots ![](/documentation/current/assets/en/manual/web_interface/frontend_sections/dashboards/edit_button_widget_view.png) button on a widget and select the desired refresh interval from the dropdown list. Note that a user's unique refresh interval takes priority over the widget setting and is preserved even when the widget's setting is modified.  
_Show header_ | Mark the checkbox to permanently display the widget header.  
When unmarked, the header is hidden to save space and becomes visible only on widget mouseover (both in view and edit modes). The header is also semi-visible when dragging a widget to a new place.  
  
#### Specific parameters

To see specific parameters for each widget, go to individual widget pages:

  * [Action log](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/action_log)
  * [Clock](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/clock)
  * [Discovery status](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/discovery_status)
  * [Favorite graphs](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/favorite_graphs)
  * [Favorite maps](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/favorite_maps)
  * [Gauge](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/gauge)
  * [Geomap](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/geomap)
  * [Graph](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/graph)
  * [Graph (classic)](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/graph_classic)
  * [Graph prototype](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/graph_prototype)
  * [Honeycomb](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/honeycomb)
  * [Host availability](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/host_availability)
  * [Host card](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/host_card)
  * [Host navigator](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/host_navigator)
  * [Item card](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/item_card)
  * [Item history](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/item_history)
  * [Item navigator](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/item_navigator)
  * [Item value](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/item_value)
  * [Map](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/map)
  * [Map navigation tree](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/map_tree)
  * [Pie chart](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/pie_chart)
  * [Problem hosts](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/problem_hosts)
  * [Problems](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/problems)
  * [Problems by severity](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/problems_severity)
  * [SLA report](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/sla_report)
  * [System information](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/system)
  * [Top hosts](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/top_hosts)
  * [Top items](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/top_items)
  * [Top triggers](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/top_triggers)
  * [Trigger overview](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/trigger_overview)
  * [URL](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/url)
  * [Web monitoring](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/web_monitoring)

#### Dynamic parameters

Multiple widgets have parameters that enable them to share configuration data between other widgets or the dashboard.

##### Host groups, Hosts, Item, Item list

The _Host groups_ , _Hosts_ , _Item_ , and _Item list_ parameters allow selecting either the respective entities or a data source containing either host groups, hosts or items for which the widget can display data.

For _Host groups_ , _Item_ , and _Item list_ parameters, the data source can be a compatible widget from the same dashboard.

For _Hosts_ parameter, the data source can be a compatible widget from the same dashboard or the dashboard itself.

The _Map_ widget can also broadcast host group and host data to compatible widgets. For more information, see Widget behavior.

##### Override host

The _Override host_ parameter allows selecting a data source containing a host for which the widget can display data. The data source can be a compatible widget from the same dashboard or the dashboard itself.

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/dashboards/override_host.png)

  * To specify a compatible widget, enter its name and select it. Alternatively, click the _Select_ button (or the dropdown button, then "Widget") to open a pop-up of available widgets.

  * To specify a dashboard, click the dropdown button, then "Dashboard". After [saving](/documentation/current/en/manual/web_interface/frontend_sections/dashboards#editing-a-dashboard) the dashboard, the _Host_ field (for selecting hosts) will appear at the top of the dashboard.

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/dynamic_selection.png)

##### Time period

The _Time period_ parameter allows selecting a data source containing a time period for which the widget can display data. The data source can be a compatible widget from the same dashboard, the dashboard itself, or the time period configured on the widget itself.

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/dashboards/time_period.png)

  * To specify a compatible widget, set _Time period_ to "Widget", enter its name and select it. Alternatively, click the _Select_ button to open a pop-up of available widgets.

  * To specify a dashboard, set _Time period_ to "Dashboard". After [saving](/documentation/current/en/manual/web_interface/frontend_sections/dashboards#editing-a-dashboard) the dashboard, the [_Time period_ selector](/documentation/current/en/manual/web_interface/time_period_selector) will appear at the top of the dashboard.

  * To configure the time period on the widget itself, set _Time period_ to "Custom" and enter or select the start and end of the time period.

Regardless of the widget's _Time period_ configuration, compatible widgets can use it as a data source for the time period.

##### Widget behavior

Widgets differ in how they **broadcast** data to other widgets.

All widgets capable of broadcasting data begin doing so automatically upon creation. For example, the _Graph_ widget immediately broadcasts time period data to listening widgets.

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/dashboards/widget_behavior_constant.png)

Widgets supporting entity selection (e.g., _Item navigator_) automatically broadcast data for the first available entity. For example, the _Item navigator_ widget broadcasts data for the first item in its item list. When a different item is selected, it broadcasts data for that item. On mouseover, the item is highlighted in light blue color; on selection, it is highlighted in yellow color.

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/dashboards/widget_behavior_selected_item.png)

The _Map_ widget also automatically broadcasts data for the first available element (e.g., host), which is closest to the upper-left corner of the widget's viewport (for _Geomap_ widget, closest to the center of the widget's viewport). When a different element is selected, it broadcasts data for that element. On mouseover, the element is highlighted in light blue color; on selection, it is highlighted in dark blue color.

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/dashboards/widget_behavior_selected_map.png)

Widgets also have specific behaviors when **listening** for data from other widgets:

  * If the data source widget is not broadcasting data, the listening widget enters the _Awaiting data_ state.
  * If the data source widget has been deleted, replaced with an incompatible widget, or moved to another dashboard page, the listening widget enters the _Referred widget is unavailable_ state.
  * If the specified host in the data source (widget or dashboard) lacks the entity configured in the listening widget (item, graph, map, etc.) or if the user lacks permissions to access the host, the listening widget displays the following message: _"No permissions to referred object or it does not exist!"_

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/dashboards/widget_behavior_nodata.png)

For the broadcasting and listening capabilities of each widget, see Widget compatibility.

##### Widget compatibility

Some widgets can broadcast configuration data to other widgets, some can listen for data, and some can do both. For example:

  * The _Action log_ widget can only retrieve time period data from _Graph_ , _Graph (classic)_ , and _Graph prototype_ widgets.
  * The _Geomap_ widget can broadcast host data to widgets that listen for it (_Honeycomb_ , _Top items_ , etc.) and can also listen for host group and host data from widgets that broadcast it (_Honeycomb_ , _Problem hosts_ , etc.).
  * The _Clock_ widget cannot broadcast or listen for any data.

The following table outlines the broadcasting and listening capabilities of each widget.

_Action log_ | - | Time period  
---|---|---  
_Clock_ | - | -  
_Discovery status_ | - | -  
_Favorite graphs_ | - | -  
_Favorite maps_ | - | -  
_Gauge_ | - | Hosts, Items  
_Geomap_ | Hosts | Host groups, Hosts  
_Graph_ | Time period | Time period, Items, Hosts  
_Graph (classic)_ | Time period | Hosts, Items, Graphs, Time period  
_Graph prototype_ | Time period | Hosts, Time period  
_Honeycomb_ | Hosts, Items | Host groups, Hosts  
_Host availability_ | - | Host groups  
_Host card_ | - | Hosts  
_Host navigator_ | Hosts | Host groups  
_Item card_ | - | Hosts, Items, Time period  
_Item history_ | Items | Hosts, Time period  
_Item navigator_ | Items | Host groups, Hosts  
_Item value_ | - | Hosts, Items, Time period  
_Map_ | Host groups, Hosts | Maps  
_Map navigation tree_ | Maps | -  
_Pie chart_ | - | Time period, Items  
_Problem hosts_ | Host groups | Host groups, Hosts  
_Problems_ | Events | Host groups, Hosts  
_Problems by severity_ | Host groups | Host groups, Hosts  
_SLA report_ | - | -  
_System information_ | - | -  
_Top hosts_ | Hosts | Host groups, Hosts  
_Top items_ | - | Host groups, Hosts  
_Top triggers_ | - | Time period  
_Trigger overview_ | - | Host groups, Hosts  
_URL_ | - | Hosts  
_Web monitoring_ | Host groups | Host groups, Hosts