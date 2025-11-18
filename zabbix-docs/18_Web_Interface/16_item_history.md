---
title: Item history
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/item_history
downloaded: 2025-11-14 10:38:14
---

# 16 Item history  
  
#### Overview

The item history widget displays the latest data for various item types (numeric, character, log, text, and binary) in a table format. It can also show progress bars, images for binary data types (useful for [browser items](/documentation/current/en/manual/config/items/itemtypes/browser)), and highlight values (useful for [log file monitoring](/documentation/current/en/manual/config/items/itemtypes/log_items)).

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/dashboards/widgets/item_history.png)

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/dashboards/widgets/item_history_binary.png)

Up to 1000 records can be displayed.

#### Configuration

To configure, select _Item history_ as type:

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/dashboards/widgets/item_history_configuration.png)

In addition to the parameters that are [common](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#common-parameters) for all widgets, you may set the following specific options:

_Layout_ | Select the layout option for item columns:  
**Horizontal** \- items will be displayed horizontally, values vertically;  
**Vertical** \- items will be displayed vertically, values horizontally.  
---|---  
_Items_ | Add item columns to display.  
The order of items determines their display order.  
Items can be reordered by dragging them up or down by the handle before the item name.  
_Show lines_ | Specify the number of item value lines to display.  
_Override host_ | Select a compatible widget or the dashboard as the [data source](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/#dynamic-parameters) for hosts.  
This parameter is not available when configuring the widget on a [template dashboard](/documentation/current/en/manual/config/templates/template#adding-dashboards).  
_Advanced configuration_ | Click the _Advanced configuration_ label to display advanced configuration options.  
  
#### Column configuration

To configure item columns, click _Add_ in the _Items_ parameter:

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/dashboards/widgets/item_history_column_configuration.png)

Common column parameters:

_Name_ | Enter the name of the column.  
If left empty, the item name from the _Item_ parameter is used.  
---|---  
_Item_ | Select the item.  
Note that column configuration parameters vary based on the information type of the selected item; for more information, see individual parameters below.  
When configuring the widget on a [template dashboard](/documentation/current/en/manual/config/templates/template#adding-dashboards), only [items configured on the template](/documentation/current/en/manual/config/templates/template#adding-items-triggers-graphs) can be selected.  
_Base color_ | Select the column's background color or fill color if _Display_ is set to "Bar" or "Indicators".  
Note that the base color can be overridden by threshold or highlight colors.  
  
Column parameters specific to numeric type items:

_Display_ | Select how the item value should be displayed:  
**As is** \- as regular text;  
**Bar** \- as solid, color-filled bar;  
**Indicators** \- as segmented, color-filled bar.  
---|---  
_Min_ | Enter the minimum value for bar/indicators.  
If left empty, the widget will use the minimum value of the item.  
This parameter is available only when _Display_ is set to "Bar" or "Indicators".  
_Max_ | Enter the maximum value for bar/indicators.  
If left empty, the widget will use the maximum value of the item.  
This parameter is available only when _Display_ is set to "Bar" or "Indicators".  
_Thresholds_ | Click _Add_ to add a threshold, select a threshold color from the color picker, and specify a numeric value.  
The thresholds list will be sorted in ascending order when saved.  
[Suffixes](/documentation/current/en/manual/appendix/suffixes) (for example, "1d", "2w", "4K", "8G") are supported. [Value mappings](/documentation/current/en/manual/config/items/mapping) are supported.  
_History data_ | Select whether to take data from history or trends:  
**Auto** \- automatic selection;  
**History** \- take history data;  
**Trends** \- take trend data.  
  
Column parameters specific to character, text, and log type items:

_Highlights_ | Click _Add_ to add a highlight, select a highlight color from the color picker, and specify a regular expression.  
The selected color will be used as the background color for item values where the specified regular expression matches the text.  
---|---  
_Display_ | Select how the item value should be displayed:  
**As is** \- displayed as is:  
\- linebreaks are observed if the incoming value has line returns;  
\- no word wrapping with horizontal layout or vertical layout with one column; word wrapping with vertical layout and more than one column.  
Hovering or clicking on the value opens a pop-up with the value.  
**HTML** \- as HTML text;  
**Single line** \- as a single line, truncated to a specified length (1-500 characters).  
Hovering or clicking on the truncated value opens a pop-up with the full value.  
_Use monospace font_ | Mark this checkbox to display the item value in monospace font (unmarked by default).  
_Display local time_ | Mark this checkbox to display local time instead of timestamp in the timestamp column.  
Note that the _Show timestamp_ checkbox in advanced configuration must also be marked.  
This parameter is available only for log type items.  
  
Column parameters specific to binary type items:

_Show thumbnail_ | Mark this checkbox to display a thumbnail for image binaries or a "Show" option for non-image binaries.  
Unmark this checkbox to display a "Show" option for all binary item values.  
Hovering or clicking the "Show" option opens a pop-up window with the item value (image or Base64 string).  
If the item value is an empty string, the "Show" option is displayed; hovering or clicking it opens a pop-up containing "Empty string".  
---|---  
  
#### Advanced configuration

Advanced configuration options are available in the collapsible _Advanced configuration_ section:

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/dashboards/widgets/item_history_advanced_configuration.png)

_New values_ | Select where new item values should be added:  
**Top** \- at the top of columns;  
**Bottom** \- at the bottom of columns.  
---|---  
_Show timestamp_ | Mark this checkbox to display the timestamp column (unmarked by default).  
_Show column header_ | Select the column header orientation:  
**Off** \- hide the header;  
**Horizontal** \- display the header horizontally;  
**Vertical** \- display the header vertically.  
[_Time period_](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#dynamic-parameters) | Select the data source for the time period:  
**Dashboard** \- set the [_Time period_ selector](/documentation/current/en/manual/web_interface/time_period_selector) as the data source;  
**Widget** \- set a compatible widget specified in the _Widget_ parameter as the data source;  
**Custom** \- set the time period specified in the _From_ and _To_ parameters as the data source; if set, a clock icon will be displayed in the upper-right corner of the widget, indicating the set time on mouseover.  
_Widget_ | Enter or select a compatible widget (_Graph_ , _Graph (classic)_ , _Graph prototype_) as the data source for the time period.  
This parameter is available if _Time period_ is set to "Widget".  
_From_ | Enter or select the start of the time period.  
[Relative time syntax](/documentation/current/en/manual/web_interface/time_period_selector) (`now`, `now/d`, `now/w-1w`, etc.) is supported.  
This parameter is available if _Time period_ is set to "Custom".  
_To_ | Enter or select the end of the time period.  
[Relative time syntax](/documentation/current/en/manual/web_interface/time_period_selector) (`now`, `now/d`, `now/w-1w`, etc.) is supported.  
This parameter is available if _Time period_ is set to "Custom".