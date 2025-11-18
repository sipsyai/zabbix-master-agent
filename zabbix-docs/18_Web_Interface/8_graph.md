---
title: Graph
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/graph
downloaded: 2025-11-14 10:38:07
---

# 8 Graph

#### Overview

The graph widget provides a modern and versatile way of visualizing data collected by Zabbix using a vector image drawing technique. This graph widget is supported since Zabbix 4.0. Note that the graph widget supported before Zabbix 4.0 can still be used as [Graph (classic)](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/graph_classic). See also [_Adding widgets_](/documentation/current/en/manual/web_interface/frontend_sections/dashboards#adding-widgets) section on _Dashboards_ page for more details.

#### Configuration

To configure, select _Graph_ as type:

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/graph_dataset.png)

#### Data set

The **Data set** tab allows selecting data for the graph by adding data sets. Two types of data sets can be added:

  * _Item patterns_ \- data from matching items is displayed. You can pick a single base color or select a palette row to assign distinct colors to each matched item.
  * _Item list_ \- data from selected items is displayed. You can choose each item's color individually from the picker.

By default, an _Item patterns_ data set is added.

_Data set_ | For **Item patterns** data set:  
Select or enter host and item patterns; data of items that match these patterns will be displayed on the graph; up to 50 items may be displayed.  
Wildcard patterns may be used for selection (for example, `*` will return results that match zero or more characters).  
To specify a wildcard pattern, enter the string manually and press _Enter_.  
The wildcard symbol is always interpreted, so it is not possible to add, for example, an item named _item*_ individually if there are other matching items (for example, _item2_ , _item3_).  
Specifying host and item patterns is mandatory for "Item patterns" data sets.  
See also: Data set configuration details.  
  
For **Item list** data set:  
Select items for the graph by clicking on the _Add item_ button.  
You may also select compatible widgets as the [data source](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#dynamic-parameters) for items by clicking on the _Add widget_ button.  
Specifying items or widgets is mandatory for "Item list" data sets.  
See also: Data set configuration details.  
  
Note that only numeric item types are allowed.  
  
When configuring the widget on a [template dashboard](/documentation/current/en/manual/config/templates/template#adding-dashboards), the parameter for specifying host patterns is not available, and the parameter for specifying an item list allows to select only the [items configured on the template](/documentation/current/en/manual/config/templates/template#adding-items-triggers-graphs).  
---|---  
| _Draw_ | Choose the draw type of the metric.  
Possible draw types: _Line_ (set by default), _Points_ , _Staircase_ , and _Bar_.  
Note that if there is only one data point in the line/staircase graph, it is drawn as a point regardless of the draw type. The point size is calculated from the line width, but it cannot be smaller than 3 pixels, even if the line width is less.  
_Stacked_ | Mark the checkbox to display data as stacked (filled areas displayed).  
This option is disabled when _Points_ draw type is selected.  
_Width_ | Set the line width.  
This option is available when _Line_ or _Staircase_ draw type is selected.  
_Point size_ | Set the point size.  
This option is available when _Points_ draw type is selected.  
_Transparency_ | Set the transparency level.  
_Fill_ | Set the fill level.  
This option is available when _Line_ or _Staircase_ draw type is selected.  
_Missing data_ | Select the option for displaying missing data:  
**None** \- the gap is left empty;  
**Connected** \- two border values are connected;  
**Treat as 0** \- the missing data is displayed as 0 values;  
**Last known** \- the missing data is displayed with the same value as the last known value; not applicable for the _Points_ and _Bar_ draw type.  
_Override host_ | Select a compatible widget or the dashboard as the data source for hosts.  
This parameter is not available when configuring the widget on a [template dashboard](/documentation/current/en/manual/config/templates/template#adding-dashboards).  
_Y-axis_ | Select the side of the graph where the Y-axis will be displayed.  
_Time shift_ | Specify time shift if required.  
You may use [time suffixes](/documentation/current/en/manual/appendix/suffixes#time-suffixes) in this field. Negative values are allowed.  
_Aggregation function_ | Specify which aggregation function to use:  
**min** \- display the smallest value;  
**max** \- display the largest value;  
**avg** \- display the average value;  
**sum** \- display the sum of values;  
**count** \- display the count of values;  
**first** \- display the first value;  
**last** \- display the last value;  
**none** \- display all values (no aggregation).  
  
Aggregation allows to display an aggregated value for the chosen interval (5 minutes, an hour, a day), instead of all values. See also: [Aggregation in graphs](/documentation/current/en/manual/config/visualization/graphs/aggregate).  
_Aggregation interval_ | Specify the interval for aggregating values.  
You may use [time suffixes](/documentation/current/en/manual/appendix/suffixes#time-suffixes) in this field. A numeric value without a suffix will be regarded as seconds.  
  
Note that if the widget is configured to display historical data based on [trends](/documentation/current/en/manual/config/items/history_and_trends#keeping-trends) (_History data selection_ is set to _Trends_ or _Auto_), it is recommended to use an aggregation interval that is a multiple of 1 hour (e.g., 3600, 60m, 1h, 3h, etc.). Trends store hourly aggregated values, so using an aggregation interval that is not a multiple of 1 hour (e.g., 100s, 7min, 15min, 90min, etc.) may lead to results that are hard to interpret.  
_Aggregate_ | Specify whether to aggregate:  
**Each item** \- each item in the dataset will be aggregated and displayed separately;  
**Data set** \- all dataset items will be aggregated and displayed as one value.  
_Approximation_ | Specify what value to display when more than one value exists per vertical graph pixel:  
**all** \- display the smallest, the largest and the average values;  
**min** \- display the smallest value;  
**max** \- display the largest value;  
**avg** \- display the average value.  
  
This setting is useful when displaying a graph for a large time period with frequent update interval (such as one year of values collected every 10 minutes).  
_Data set label_ | Specify the data set label that is displayed in graph _Data set_ configuration and in graph _Legend_ (for aggregated data sets).  
All data sets are numbered including those with a specified _Data set label_. If no label is specified, the data set will be labeled automatically according to its number (e.g. "Data set #2", "Data set #3", etc.). Data set numbering is recalculated after reordering/dragging data sets.  
Data set labels that are too long will be shortened to fit where displayed (e.g. "Number of proc...").  
  
##### Data set configuration details

Existing data sets are displayed in a list. You may:

  * Click on the ![](/documentation/current/assets/en/manual/web_interface/frontend_sections/dashboards/move_icon.png) move icon and drag a data set to a new place in the list.
  * Click on the ![](/documentation/current/assets/en/manual/web_interface/frontend_sections/dashboards/expand_icon.png) expand icon to expand data set details. When expanded, this icon turns into a ![](/documentation/current/assets/en/manual/web_interface/frontend_sections/dashboards/collapse_icon.png) collapse icon.
  * Click on the ![](/documentation/current/assets/en/manual/web_interface/frontend_sections/dashboards/color_icon.png) color icon to open the picker. You can enter a hex code, choose a solid swatch, or switch to the _Palette_ tab and select a row of predefined colors. The chosen color applies directly for _Item list_ data sets or as the base for generated shades in _Item patterns_. Use Tab to move between dialog controls, arrow keys to navigate swatches or palette rows, Enter to select, and Esc to cancel.
  * Click on the _Add new data set_ button to add an empty data set allowing to select host and item patterns. If you click on the downward pointing icon next to the _Add new data set_ button, a drop-down menu appears, allowing you to add a new _Item patterns_ or _Item list_ data set or allowing you to _Clone_ the currently open data set. If all data sets are collapsed, the _Clone_ option is not available.

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/dashboards/graph_dataset_add.png)

The **Item patterns** data set contains _Host patterns_ and _Item patterns_ fields that both recognize full names or patterns containing a wildcard symbol (*). This functionality allows you to select all the host names and item names containing the selected pattern. While typing the item name or item pattern in the _Item patterns_ field, only items belonging to the selected host name(s) are displayed in the dropdown list.

For example, having typed a pattern **z*** in the _Host patterns_ field, the dropdown list displays all host names containing this pattern: **z*, Zabbix server, Zabbix proxy**. After pressing _Enter_ , this pattern is accepted and is displayed as **z***. Similarly, having typed the pattern **a*** in the _Item patterns_ field, the dropdown list displays all item names containing this pattern: **a*, Available memory, Available memory in %**.

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/dashboards/widgets/graph_widget_it_host_pattern_1.png)

After pressing Enter, the pattern is accepted and shown as a*.

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/dashboards/widgets/graph_widget_it_host_pattern_2.png)

The graph then displays all items belonging to the selected host name(s).

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/dashboards/widgets/graph_widget_it_host_pattern_3.png)

The **Item list** data set contains the _Add item_ button that allows you to add items to be displayed on the graph. You can also add compatible widgets as the [data source](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#dynamic-parameters) for items by clicking the _Add widget_ button.

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/dashboards/widgets/graph_widget_it_item_list_1.png)

For example, clicking the _Add item_ button opens a pop-up window containing a _Host_ parameter. Having selected a host, all its items that are available for selection are displayed in a list.

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/dashboards/widgets/graph_widget_it_item_list_2.png)

After selecting one or more items, they will be displayed in the data set item list and in the graph.

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/dashboards/widgets/graph_widget_it_item_list_3.png)

#### Displaying options

The **Displaying options** tab allows to define history data selection:

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/graph_displaying_options.png)

_History data selection_ | Set the source of graph data:  
**Auto** \- data are sourced according to the classic graph [algorithm](/documentation/current/en/manual/config/visualization/graphs/simple#generating-from-historytrends) (default);  
**History** \- data from history;  
**Trends** \- data from trends.  
---|---  
_Simple triggers_ | Mark the checkbox to show the trigger thresholds for simple triggers. The thresholds will be drawn as dashed lines using the trigger severity color.  
A simple trigger is a trigger with one function (only `last`, `max`, `min`, `avg`) for one item in the expression.  
A maximum of three triggers can be drawn. Note that the trigger has to be within the drawn range to be visible.  
_Working time_ | Mark the checkbox to show working time on the graph. Working time (working days) is displayed in graphs as a white background, while non-working time is displayed in gray (with the _Original blue_ default frontend theme).  
_Percentile line (left)_ | Mark the checkbox and enter the percentile value to show the specified percentile as a line on the left Y-axis of the graph.  
If, for example, a 95% percentile is set, then the percentile line will be at the level where 95 percent of the values fall under.  
_Percentile line (right)_ | Mark the checkbox and enter the percentile value to show the specified percentile as a line on the right Y-axis of the graph.  
If, for example, a 95% percentile is set, then the percentile line will be at the level where 95 percent of the values fall under.  
  
#### Time period

The **Time period** tab allows to set a time period for which to display data in the graph:

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/graph_time_period.png)

_Time period_ | Select the [data source](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#dynamic-parameters) for the time period:  
**Dashboard** \- set the _Time period_ selector as the data source;  
**Widget** \- set a compatible widget specified in the _Widget_ parameter as the data source;  
**Custom** \- set the time period specified in the _From_ and _To_ parameters as the data source; if set, a clock icon will be displayed in the upper-right corner of the widget, indicating the set time on mouseover.  
---|---  
_Widget_ | Enter or select a compatible widget as the data source for the time period.  
This parameter is available if _Time period_ is set to "Widget".  
_From_ | Enter or select the start of the time period.  
[Relative time syntax](/documentation/current/en/manual/web_interface/time_period_selector) (`now`, `now/d`, `now/w-1w`, etc.) is supported.  
This parameter is available if _Time period_ is set to "Custom".  
_To_ | Enter or select the end of the time period.  
[Relative time syntax](/documentation/current/en/manual/web_interface/time_period_selector) (`now`, `now/d`, `now/w-1w`, etc.) is supported.  
This parameter is available if _Time period_ is set to "Custom".  
  
#### Axes

The **Axes** tab allows to customize how axes are displayed:

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/graph_axes.png)

_Left Y_ | Mark this checkbox to make left Y-axis visible.  
The checkbox may be disabled if unselected either in _Data set_ or in _Overrides_ tab.  
---|---  
_Right Y_ | Mark this checkbox to make right Y-axis visible.  
The checkbox may be disabled if unselected either in _Data set_ or in _Overrides_ tab.  
_X-Axis_ | Unmark this checkbox to hide X-axis (marked by default).  
_Scale_ | Choose the scale for the graph axis values from the dropdown:  
**Linear** \- axis values increase by a fixed amount (e.g., 10, 20, 30), suitable for data that changes steadily or covers a small to moderate range;  
**Logarithmic** \- axis values increase exponentially (e.g., 10, 100, 1000), suitable for data that changes rapidly or covers a large range.  
_Min_ | Set the minimum value of the corresponding axis.  
Visible range minimum value of Y-axis is specified.  
_Max_ | Set the maximum value of the corresponding axis.  
Visible range maximum value of Y-axis is specified.  
_Units_ | Choose the unit for the graph axis values from the dropdown:  
**Auto** \- axis values are displayed using the unit of the first item in the data set;  
**Static** \- axis values are displayed using the unit specified in the _value_ input field; if the field is left blank, only numeric values are displayed.  
  
#### Legend

The **Legend** tab allows to customize the graph legend:

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/graph_legend.png)

_Show legend_ | Unmark this checkbox to hide the legend on the graph (marked by default).  
---|---  
_Display min/avg/max_ | Mark this checkbox to display the minimum, average, and maximum values of the item in the legend.  
_Show aggregation function_ | Mark this checkbox to show the aggregation function in the legend.  
_Rows_ | Select the display mode for legend rows:  
**Fixed** \- the number of rows displayed is determined by the _Number of rows_ parameter value;  
**Variable** \- the number of rows displayed is determined by the amount of configured items while not exceeding the _Maximum number of rows_ parameter value.  
_Number of rows/_  
_Maximum number of rows_ | If _Rows_ is set to "Fixed", set the number of legend rows to be displayed (1-10).  
If _Rows_ is set to "Variable", set the maximum number of legend rows to be displayed (1-10).  
_Number of columns_ | Set the number of legend columns to be displayed (1-4).  
This parameter is available if _Display min/avg/max_ is unmarked.  
  
#### Problems

The **Problems** tab allows to customize the problem display:

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/graph_problems.png)

_Show problems_ | Mark this checkbox to enable problem displaying on the graph (unmarked, i.e., disabled by default).  
---|---  
_Selected items only_ | Mark this checkbox to include problems for the selected items only to be displayed on the graph.  
_Problem hosts_ | Select the problem hosts to be displayed on the graph.  
  
Wildcard patterns may be used (for example, `*` will return results that match zero or more characters).  
To specify a wildcard pattern, just enter the string manually and press _Enter_.  
While you are typing, note how all matching hosts are displayed in the dropdown.  
  
This parameter is not available when configuring the widget on a [template dashboard](/documentation/current/en/manual/config/templates/template#adding-dashboards).  
_Severity_ | Mark problem severities to filter problems to be displayed on the graph.  
If no severities are marked, all problems will be displayed.  
_Problem_ | Specify the problem's name to be displayed on the graph.  
_Problem tags_ | Specify problem tags to limit the number of problems displayed in the widget.  
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
  
#### Overrides

The **Overrides** tab allows to add custom overrides for data sets:

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/graph_overrides.png)

Overrides are useful when several items are selected for a data set using the `*` wildcard and you want to change how the items are displayed by default (e.g. default base color or any other property).

Existing overrides (if any) are displayed in a list. To add a new override:

  * Click on the ![](/documentation/current/assets/en/manual/web_interface/frontend_sections/dashboards/add_override.png) button
  * Select hosts and items for the override. Alternatively, you may enter host and item patterns. Wildcard patterns may be used (for example, `*` will return results that match zero or more characters). To specify a wildcard pattern, just enter the string manually and press _Enter_. While you are typing, note how all matching hosts are displayed in the dropdown. The wildcard symbol is always interpreted, therefore it is not possible to add, for example, an item named "item*" individually if there are other matching items (e.g. item2, item3). Host pattern and item pattern parameters are mandatory. The parameter for specifying host patterns is not available when configuring the widget on a [template dashboard](/documentation/current/en/manual/config/templates/template#adding-dashboards). The parameter for specifying an item list allows to select only [items configured on the template](/documentation/current/en/manual/config/templates/template#adding-items-triggers-graphs) when configuring the widget on a [template dashboard](/documentation/current/en/manual/config/templates/template#adding-dashboards).
  * Click on ![](/documentation/current/assets/en/manual/web_interface/frontend_sections/dashboards/add_override2.png), to select override parameters. At least one override parameter should be selected. For parameter descriptions, see the _Data set_ tab above.

Information displayed by the graph widget can be downloaded as a .png image using the [widget menu](/documentation/current/en/manual/web_interface/frontend_sections/dashboards#widget-menu):

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/dashboards/graph_widget_as_png.png)

A screenshot of the widget will be saved to the Downloads folder.