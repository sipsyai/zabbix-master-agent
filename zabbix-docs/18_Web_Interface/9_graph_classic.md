---
title: Graph (classic)
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/graph_classic
downloaded: 2025-11-14 10:38:08
---

# 9 Graph (classic)

#### Overview

In the classic graph widget, you can display a single custom graph or simple graph.

#### Configuration

To configure, select _Graph (classic)_ as type:

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/dashboards/widgets/graph_classic.png)

In addition to the parameters that are [common](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#common-parameters) for all widgets, you may set the following specific options:

_Source_ | Select the graph type:  
**Graph** \- [custom graph](/documentation/current/en/manual/config/visualization/graphs/custom);  
**Simple graph** \- [simple graph](/documentation/current/en/manual/config/visualization/graphs/simple).  
---|---  
_Graph_ | Select the custom graph to display.  
Alternatively, select a compatible widget as the [data source](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/#dynamic-parameters) for graphs.  
This parameter is available if _Source_ is set to "Graph".  
_Item_ | Select the item to display in a simple graph.  
Alternatively, select a compatible widget as the [data source](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/#dynamic-parameters) for items.  
This parameter is available if _Source_ is set to "Simple graph".  
_Time period_ | Set a time period for which to display data in the graph. Select the [data source](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/#dynamic-parameters) for the time period:  
**Dashboard** \- set the _Time period_ selector as the data source;  
**Widget** \- set a compatible widget specified in the _Widget_ parameter as the data source;  
**Custom** \- set the time period specified in the _From_ and _To_ parameters as the data source; if set, a clock icon will be displayed in the upper-right corner of the widget, indicating the set time on mouseover.  
_Widget_ | Enter or select a compatible widget as the data source for the time period.  
This parameter is available if _Time period_ is set to "Widget".  
_From_ | Enter or select the start of the time period.  
[Relative time syntax](/documentation/current/en/manual/web_interface/time_period_selector) (`now`, `now/d`, `now/w-1w`, etc.) is supported.  
This parameter is available if _Time period_ is set to "Custom".  
_To_ | Enter or select the end of the time period.  
[Relative time syntax](/documentation/current/en/manual/web_interface/time_period_selector) (`now`, `now/d`, `now/w-1w`, etc.) is supported.  
This parameter is available if _Time period_ is set to "Custom".  
_Show legend_ | Unmark this checkbox to hide the legend on the graph (marked by default).  
_Override host_ | Select a compatible widget or the dashboard as the [data source](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/#dynamic-parameters) for hosts.  
This parameter is not available when configuring the widget on a [template dashboard](/documentation/current/en/manual/config/templates/template#adding-dashboards).  
  
The legend of the graph consists of three sections:

  * Items and their aggregated values
  * Percentiles (if configured)
  * Triggers (if any are associated with the displayed items)

If the height of the graph within the widget is insufficient, the legend may not be displayed or may be displayed only partially. Triggers and percentiles are hidden first, followed by the item legend. To display the full legend, increase the widget's vertical size.

No more than 3 trigger lines can be displayed. If there are more triggers then the triggers with lower severity are prioritized for display.

Information displayed by the classic graph widget can be downloaded as _.png_ image using the [widget menu](/documentation/current/en/manual/web_interface/frontend_sections/dashboards#widget-menu):

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/dashboards/graph_download.png)

A screenshot of the widget will be saved to the _Downloads_ folder.