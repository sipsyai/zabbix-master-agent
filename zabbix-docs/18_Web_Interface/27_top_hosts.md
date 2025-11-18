---
title: Top hosts
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/top_hosts
downloaded: 2025-11-14 10:38:25
---

# 27 Top hosts  
  
#### Overview

The Top hosts widget provides a way to create custom tables for displaying data for multiple hosts and can be utilized for creating _Top N_ -like reports and progress-bar reports useful for capacity planning. The type of data to display is customizable and can include CPU usage, memory availability, or any other collected values in the numeric, text, or binary format, as well as static text strings. Data can be presented in various formats such as bars, indicators, or sparkline charts.

The maximum number of hosts that can be displayed is 1000.

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/top_hosts.png)

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/top_hosts2.png)

#### Configuration

To configure, select _Top hosts_ as type:

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/top_hosts.1.png)

In addition to the parameters that are [common](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#common-parameters) for all widgets, you may set the following specific options:

_Host groups_ | Select host groups to display in the widget.  
Alternatively, select a compatible widget as the [data source](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/#dynamic-parameters) for host groups.  
This field is auto-complete, so starting to type the name of a group will offer a dropdown of matching groups.  
This parameter is not available when configuring the widget on a [template dashboard](/documentation/current/en/manual/config/templates/template#adding-dashboards).  
---|---  
_Hosts_ | Select hosts to display in the widget.  
Alternatively, select a compatible widget or the dashboard as the [data source](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/#dynamic-parameters) for hosts.  
This field is auto-complete, so starting to type the name of a host will offer a dropdown of matching hosts.  
This parameter is not available when configuring the widget on a [template dashboard](/documentation/current/en/manual/config/templates/template#adding-dashboards).  
_Host tags_ | Specify tags to limit the number of hosts displayed in the widget.  
It is possible to include as well as exclude specific tags and tag values. Several conditions can be set. Tag name matching is always case-sensitive.  
  
There are several operators available for each condition:  
**Exists** \- include the specified tag names;  
**Equals** \- include the specified tag names and values (case-sensitive);  
**Contains** \- include the specified tag names where the tag values contain the entered string (substring match, case-insensitive);  
**Does not exist** \- exclude the specified tag names;  
**Does not equal** \- exclude the specified tag names and values (case-sensitive);  
**Does not contain** \- exclude the specified tag names where the tag values contain the entered string (substring match, case-insensitive).  
  
There are two calculation types for conditions:  
**And/Or** \- all conditions must be met, conditions having the same tag name will be grouped by the Or condition;  
**Or** \- enough if one condition is met.  
  
This parameter is not available when configuring the widget on a [template dashboard](/documentation/current/en/manual/config/templates/template#adding-dashboards).  
_Show hosts in maintenance_ | Mark this checkbox for hosts in maintenance to be displayed as well (in this case, maintenance icon will be shown next to the host name). Unmarked by default.  
_Columns_ | Add data columns to display.  
The column order determines their display from left to right.  
Columns can be reordered by dragging up and down by the handle before the column name.  
_Order by_ | Specify the column from the defined _Columns_ list to use for _Top N_ or _Bottom N_ ordering.  
_Order_ | Specify the ordering of rows:  
**Top N** \- in descending order according to the _Order by_ aggregated value;  
**Bottom N** \- in ascending order according to the _Order by_ aggregated value.  
_Host limit_ | Number of host rows to be shown (1-1000).  
This parameter is not available when configuring the widget on a [template dashboard](/documentation/current/en/manual/config/templates/template#adding-dashboards).  
  
##### Column configuration

It is possible to add columns of three data types: host name, item value, or text. The list of available column parameters depends on the column data type and, for the item value type, on the value format.

###### Host name column

Host name column is used to display the name of the host.

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/thosts_hostname_column.png)

Supported parameters:

_Name_ | Name of the column.  
---|---  
_Data_ | Data type to display in the column, select **Host name**.  
_Base color_ | Background color of the column.  
  
###### Text column

Text column is used to display any specified text string.

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/thosts_text_column.png)

Supported parameters:

_Name_ | Name of the column.  
---|---  
_Data_ | Data type to display in the column, select **Text**.  
_Base color_ | Background color of the column.  
_Text_ | Enter the string to display.  
May contain host and inventory [macros](/documentation/current/en/manual/appendix/macros/supported_by_location).  
  
###### Item value column

Item value column is used to display value of the specified item; it supports multiple value display formats and options.

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/thosts_numeric_column.png)

Supported parameters:

_Name_ | Name of the column.  
---|---  
_Data_ | Data type to display in the column, select **Item value**.  
_Item name_ | Select an item; its name is used to match and display items with the same name on all selected hosts. If a host has multiple such items, the widget displays the item whose key is first alphabetically (e.g., _CPU utilization_ with key `proc.cpu.util` instead of `system.cpu.util`).  
When configuring the widget on a [template dashboard](/documentation/current/en/manual/config/templates/template#adding-dashboards), only [items configured on the template](/documentation/current/en/manual/config/templates/template#adding-items-triggers-graphs) can be selected.  
_Base color_ | Background color of the column; fill color if _Item value_ data is displayed as bar/indicators. The default color can be overridden by custom color, if the item value is over one of the specified thresholds.  
_Display item value as_ | Format for displaying the item value: **Numeric** , **Text** , or **Binary**.  
The selected option determines which additional parameters will be available. Refer to the parameter list for each format below.  
**_Advanced configuration_**  
_Aggregation function_ | Specify which aggregation function to use:  
**min** \- display the smallest value;  
**max** \- display the largest value;  
**avg** \- display the average value;  
**count** \- display the count of values;  
**sum** \- display the sum of values;  
**first** \- display the first value;  
**last** \- display the last value;  
**not used** \- display the most recent value (no aggregation).  
  
Aggregation allows to display an aggregated value for the chosen interval (5 minutes, an hour, a day), instead of the most recent value.  
Only numeric data can be displayed for _min_ , _max_ , _avg_ and _sum_. For _count_ , non-numeric data will be changed to numeric.  
_Time period_ | Specify the time period to use for aggregating values:  
**Dashboard** \- use time period of the dashboard;  
**Widget** \- use time period of the specified widget;  
**Custom** \- use a custom time period.  
This parameter will not be displayed if _Aggregation function_ is set to "not used".  
_Widget_ | Select the widget.  
This parameter will only be displayed if _Time period_ is set to "Widget".  
_From_ | Select the time period from (default value `now-1h`). See [relative time syntax](/documentation/current/en/manual/web_interface/time_period_selector).  
This parameter will only be displayed if _Time period_ is set to "Custom".  
_To_ | Select the time period to (default value `now`). See [relative time syntax](/documentation/current/en/manual/web_interface/time_period_selector).  
This parameter will only be displayed if _Time period_ is set to "Custom".  
_History data_ | Take data from history or trends:  
**Auto** \- automatic selection;  
**History** \- take history data;  
**Trends** \- take trend data.  
This parameter is available only for numeric item values. For text and binary values data will always be taken from history.  
  
**Numeric item value** parameters:

_Display_ | Define how the value should be displayed:  
**As is** \- as regular text;  
**Bar** \- as solid, color-filled bar;  
**Indicators** \- as segmented, color-filled bar;  
**Sparkline** \- mini line graph.  
---|---  
_Thresholds_ | Specify threshold values when the background/fill color should change.  
The list will be sorted in ascending order when saved.  
For sparklines, thresholds are applied only to the item last value.  
_Decimal places_ | Specify how many decimal places will be displayed with the value.  
**_Bar/Indicators_**  
_Min_ | Minimum value.  
_Max_ | Maximum value.  
**_Sparkline_**  
_Width_ | Set the graph line thickness by using the slider or manually entering a value in the range from 0 to 10.  
_Color_ | Select line and fill color.  
_Fill_ | Set fill color transparency level by using the slider or manually entering a value in the range from 0 to 10.  
_Time period_ | Specify the time period for values to be included into the sparkline chart:  
**Dashboard** \- use time period of the dashboard;  
**Widget** \- use time period of the specified widget;  
**Custom** \- use a custom time period.  
  
Note that the time period affects only the sparkline chart. The value displayed next to the sparkline represents the last value of the item, not the last value in the selected time period.  
_Widget_ | Select the widget.  
This parameter will only be displayed if _Time period_ is set to "Widget".  
_From_ | Select the time period from (default value `now-1h`). See [relative time syntax](/documentation/current/en/manual/web_interface/time_period_selector).  
This parameter will only be displayed if _Time period_ is set to "Custom".  
_To_ | Select the time period to (default value `now`). See [relative time syntax](/documentation/current/en/manual/web_interface/time_period_selector).  
This parameter will only be displayed if _Time period_ is set to "Custom".  
_History data_ | Take data from history or trends:  
**Auto** \- automatic selection;  
**History** \- take history data;  
**Trends** \- take trend data.  
  
**Text item value** parameters:

_Highlights_ | Specify the regular expressions upon matching which the background/fill color should change.  
---|---  
  
**Binary item value** parameters:

_Show thumbnail_ | Specify whether to create and display a thumbnail for the image containing binary data or to display a hyperlink _Show_ leading to the full-size image in the value column.  
---|---