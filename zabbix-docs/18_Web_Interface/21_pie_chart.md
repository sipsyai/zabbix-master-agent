---
title: Pie chart
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/pie_chart
downloaded: 2025-11-14 10:38:19
---

# 21 Pie chart  
  
#### Overview

The pie chart widget allows to display values of selected items as a **pie** or **doughnut** chart.

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/pie_chart.png)  
Pie chart.  
---  
![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/doughnut_chart.png)  
Doughnut chart.  
  
On mouseover, the focused sector enlarges outwards and the legend for this sector is displayed. Clicking on the focused sector makes the pop-out effect permanent, until closed with "x".

The charts are drawn using a vector image drawing technique.

#### Configuration

To configure, select _Pie chart_ as type:

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/pie_dataset.png)

#### Data set

The **Data set** tab allows selecting data for the pie chart by adding data sets. Two types of data sets can be added:

  * _Item patterns_ \- data from matching items is displayed. You can pick a single base color or select a palette row to assign distinct colors to each matched item.
  * _Item list_ \- data from selected items is displayed. You can choose each item's color individually from the picker.

By default, an _Item patterns_ data set is added.

_Data set_ | For **Item patterns** data set:  
Select or enter host and item patterns; data of items that match the entered patterns will be displayed on the pie chart; up to 50 items may be displayed.  
Wildcard patterns may be used for selection (for example, `*` will return results that match zero or more characters).  
To specify a wildcard pattern, enter the string manually and press _Enter_.  
The wildcard symbol is always interpreted, so it is not possible to add, for example, an item named _item*_ individually if there are other matching items (for example, _item2_ , _item3_).  
Specifying host and item patterns is mandatory for "Item patterns" data sets.  
See also: Data set configuration details.  
  
For **Item list** data set:  
Select items for the pie chart by clicking on the _Add item_ button.  
The _Type_ dropdown after the item name allows to select the display type for each item:  
**Normal** \- item value is represented proportionally on the pie chart (default);  
**Total** \- item value takes up the whole pie chart. Note that only one "Total" item can exist per pie chart, and it will be placed first on the pie chart legend. If an item is set to "Total", the _Data set aggregation_ parameter (see below) will be disabled and set to "not used".  
You may also select compatible widgets as the [data source](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#dynamic-parameters) for items by clicking on the _Add widget_ button. The same options apply to widgets as to individual items.  
Specifying items or widgets is mandatory for "Item list" data sets.  
See also: Data set configuration details.  
  
Note that only numeric item types are allowed.  
  
When configuring the widget on a [template dashboard](/documentation/current/en/manual/config/templates/template#adding-dashboards), the parameter for specifying host patterns is not available, and the parameter for specifying an item list allows to select only the [items configured on the template](/documentation/current/en/manual/config/templates/template#adding-items-triggers-graphs).  
---|---  
| _Aggregation function_ | Specify which aggregation function to use for each item in the data set:  
**min** \- display the smallest value;  
**max** \- display the largest value;  
**avg** \- display the average value;  
**sum** \- display the sum of values;  
**count** \- display the count of values;  
**first** \- display the first value;  
**last** \- display the last value (default).  
  
Aggregation allows to display an aggregated value for the interval (5 minutes, an hour, a day) selected in the _Time period_ tab or used for the whole dashboard.  
_Data set aggregation_ | Specify which aggregation function to use for the whole data set:  
**not used** \- no aggregation, items are displayed separately (default);  
**min** \- display the smallest value;  
**max** \- display the largest value;  
**avg** \- display the average value;  
**sum** \- display the sum of values;  
**count** \- display the count of values.  
  
Aggregation allows to display an aggregated value for the interval (5 minutes, an hour, a day) selected in the _Time period_ tab or used for the whole dashboard.  
_Data set label_ | Specify a custom label for the data set.  
The label is displayed in the data set configuration and the pie chart legend (for aggregated data sets).  
All data sets are numbered including those with a specified _Data set label_. If no label is specified, the data set will be labeled automatically according to its number (e.g. "Data set #2", "Data set #3", etc.). Data set numbering ir recalculated after reordering/dragging data sets.  
Data set labels that are too long will be shortened to fit where displayed (e.g. "Number of proc...").  
  
##### Data set configuration details

Existing data sets are displayed in a list. You can rearrange, expand/collapse, change colors, and clone these data sets.

For more information, see data set configuration details in the [_Graph_](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/graph#data-set-configuration-details) widget. These details also apply to the _Pie chart_ widget.

#### Displaying options

The **Displaying options** tab allows to define history data selection and visualization options for the pie chart:

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/pie_displaying_options.png)

_History data selection_ | Select the data source:  
**Auto** \- data are sourced according to the classic [algorithm](/documentation/current/en/manual/config/visualization/graphs/simple#generating-from-historytrends) (default);  
**History** \- data from history;  
**Trends** \- data from trends.  
---|---  
_Draw_ | Select the visualization style of the pie chart:  
**Pie** \- a full pie (sectors take up 100% of the radius);  
**Doughnut** \- a pie with empty circle in the middle (sectors use up to 50% of radius).  
_Space between sectors_ | Select the space size (in units of 0-10) between sectors (default is "1").  
_Merge sectors smaller than N%_ | Mark the checkbox to merge sectors smaller than the N%.  
If enabled, select the color for the merged sectors and the percentage threshold (N) for merging small sectors.  
_Draw style:**Doughnut**_  
| _Width_ | Select the doughnut width: 20, 30, 40 or 50% (default) of the radius.  
_Stroke width_ | Select the width of the doughnut sector border (0-10).  
_Show total value_ | Mark the checkbox to show the total value in the middle of the doughnut chart.  
| _Size_ | Select the size option for the total value:  
**Auto** \- the text is sized automatically to fit the doughnut middle readably;  
**Custom** \- specify the text size as height percentage from the total widget height.  
_Decimal places_ | Specify the number of decimal places for the total value (0-6).  
_Units_ | Specify the units for the total value.  
_Bold_ | Mark the checkbox to display the total value in bold.  
_Color_ | Select the color for the total value.  
  
#### Time period

The **Time period** tab allows to set a custom time period for the aggregation settings of the pie chart:

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/pie_time_period.png)

_Time period_ | Select the [data source](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#dynamic-parameters) for the time period:  
**Dashboard** \- set the _Time period_ selector as the data source;  
**Widget** \- set a compatible widget specified in the _Widget_ parameter as the data source;  
**Custom** \- set the time period specified in the _From_ and _To_ parameters as the data source; if set, a clock icon will be displayed in the upper-right corner of the widget, indicating the set time on mouseover.  
---|---  
_Widget_ | Enter or select a compatible widget (_Graph_ , _Graph (classic)_ , _Graph prototype_) as the data source for the time period.  
This parameter is available if _Time period_ is set to "Widget".  
_From_ | Enter or select the start of the time period.  
[Relative time syntax](/documentation/current/en/manual/web_interface/time_period_selector) (`now`, `now/d`, `now/w-1w`, etc.) is supported.  
This parameter is available if _Time period_ is set to "Custom".  
_To_ | Enter or select the end of the time period.  
[Relative time syntax](/documentation/current/en/manual/web_interface/time_period_selector) (`now`, `now/d`, `now/w-1w`, etc.) is supported.  
This parameter is available if _Time period_ is set to "Custom".  
  
#### Legend

The **Legend** tab allows to customize the pie chart legend:

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/pie_legend.png)

_Show legend_ | Unmark this checkbox to hide the legend on the pie chart (marked by default).  
---|---  
_Show value_ | Mark this checkbox to show the value of the item in the legend.  
_Show aggregation function_ | Mark this checkbox to show the aggregation function in the legend.  
_Rows_ | Select the display mode for legend rows:  
**Fixed** \- the number of rows displayed is determined by the _Number of rows_ parameter value;  
**Variable** \- the number of rows displayed is determined by the amount of configured items while not exceeding the _Maximum number of rows_ parameter value.  
_Number of rows/_  
_Maximum number of rows_ | If _Rows_ is set to "Fixed", set the number of legend rows to be displayed (1-10).  
If _Rows_ is set to "Variable", set the maximum number of legend rows to be displayed (1-10).  
_Number of columns_ | Set the number of legend columns to be displayed (1-4).  
This parameter is available if _Show value_ is unmarked.  
  
The information displayed by the pie chart widget can be downloaded as a _.png_ image using the [widget menu](/documentation/current/en/manual/web_interface/frontend_sections/dashboards#widget-menu).

A screenshot of the widget will be saved to the _Downloads_ folder.