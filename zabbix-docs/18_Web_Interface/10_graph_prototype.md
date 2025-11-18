---
title: Graph prototype
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/graph_prototype
downloaded: 2025-11-14 10:38:09
---

# 10 Graph prototype

#### Overview

In the graph prototype widget, you can display a grid of graphs created from either a graph prototype or an item prototype by low-level discovery.

#### Configuration

To configure, select _Graph prototype_ as widget type:

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/dashboards/widgets/graph_prototype.png)

In addition to the parameters that are [common](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#common-parameters) for all widgets, you may set the following specific options:

_Source_ | Select the source of the graphs: **Graph prototype** or **Simple graph prototype**.  
---|---  
_Graph prototype_ | Select a graph prototype to display graphs discovered by the graph prototype.  
This parameter is available if _Source_ is set to "Graph prototype".  
_Item prototype_ | Select an item prototype to display simple graphs for items discovered by the item prototype.  
This parameter is available if _Source_ is set to "Simple graph prototype".  
_Time period_ | Set a time period for which to display data in the graphs. Select the [data source](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#dynamic-parameters) for the time period:  
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
_Show legend_ | Unmark this checkbox to hide the legend on the graphs (marked by default).  
_Override host_ | Select a compatible widget or the dashboard as the [data source](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/#dynamic-parameters) for hosts.  
This parameter is not available when configuring the widget on a [template dashboard](/documentation/current/en/manual/config/templates/template#adding-dashboards).  
_Columns_ | Enter the number of columns of graphs to display within a graph prototype widget.  
_Rows_ | Enter the number of rows of graphs to display within a graph prototype widget.  
  
The legend of the graph consists of three sections:

  * Items and their aggregated values
  * Percentiles (if configured)
  * Triggers (if any are associated with the displayed items)

If the height of the graph within the widget is insufficient, the legend may not be displayed or may be displayed only partially. Triggers and percentiles are hidden first, followed by the item legend. To display the full legend, increase the widget's vertical size.

No more than 3 trigger lines can be displayed. If there are more triggers then the triggers with lower severity are prioritized for display.

While the _Columns_ and _Rows_ parameters allow fitting more than one graph in the widget, there still may be more discovered graphs than there are columns/rows in the widget. In this case, paging becomes available in the widget, and a slide-up header allows to switch between pages using the left and right arrows:

![](/documentation/current/assets/en/manual/config/visualization/host_dashboards_discovered.png)