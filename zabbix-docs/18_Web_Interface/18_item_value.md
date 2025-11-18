---
title: Item value
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/item_value
downloaded: 2025-11-14 10:38:16
---

# 18 Item value  
  
#### Overview

This widget is useful for displaying the value of a single item prominently. This can be the latest value as well as an aggregated value for some period in the past.

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/item_value_single.png)

Besides the value itself, additional elements can be displayed, if desired:

  * Time of the metric
  * Item description
  * Change indicator for the value
  * Background color for the value
  * Item unit
  * Sparkline chart for values from the specified time period

The widget can display numeric and string values. Displaying binary values is not supported. String values are displayed on a single line and truncated, if needed. "No data" is displayed, if there is no value for the item.

The change indicator always compares with the same period in the past. So, for example, the latest value will be compared with the previous value, while the latest month will be compared with the month before. Note that the previous period for aggregations is calculated as time period of the same length as the original one with ending time directly before the starting time of the original period.

Clicking on the value leads to an [ad-hoc graph](/documentation/current/en/manual/config/visualization/graphs/adhoc) for numeric items or latest data for string items.

The widget and all elements in it can be visually fine-tuned using advanced configuration options, allowing to create a wide variety of visual styles:

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/item_value_overview.png)

#### Configuration

To configure, select _Item value_ as the widget type:

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/dashboards/widgets/item_value.png)

In addition to the parameters that are [common](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#common-parameters) for all widgets, you may set the following specific options:

_Item_ | Select the item.  
Alternatively, select a compatible widget as the [data source](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/#dynamic-parameters) for items.  
---|---  
_Show_ | Mark the checkbox to display the respective element: description, value, time, change indicator, sparkline. Unmark to hide. At least one element must be selected.  
_Override host_ | Select a compatible widget or the dashboard as the [data source](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/#dynamic-parameters) for hosts.  
This parameter is not available when configuring the widget on a [template dashboard](/documentation/current/en/manual/config/templates/template#adding-dashboards).  
_Advanced configuration_ | Click the _Advanced configuration_ label to display advanced configuration options.  
  
#### Advanced configuration

Advanced configuration options are available in the collapsible _Advanced configuration_ section, and only for those elements that are selected in the _Show_ field (see above).

Note that multiple elements cannot occupy the same space; if they are placed in the same space, an error message will be displayed.

##### Generic widget parameters

These parameters determine the background color (static or dynamic) for the whole widget and an aggregation function for displaying values.

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/item_value_conf_generic.png)

_Background color_ | Select the background color for the whole widget from the color picker.  
`D` stands for default color (depends on the frontend theme). To return to the default value, click the _Use default_ button in the color picker.  
---|---  
_Thresholds_ | Configure the dynamic background color for the whole widget. Click _Add_ to add a threshold, select the background color from the color picker, and specify a numeric value. Once the item value equals or is greater than the threshold value, the background color will change.  
The list will be sorted in ascending order when saved.  
Note that the dynamic background color will be displayed correctly only for numeric items.  
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
<This parameter will not be displayed if _Aggregation function_ is set to "not used".  
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
  
This setting applies only to numeric data. Non-numeric data will always be taken from history.  
  
##### Description

These parameters determine how the item description should be displayed.

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/item_value_conf_description.png)

_Description_ | Enter the item description. This description may override the default item name. Multiline descriptions are supported. A combination of text and supported macros is possible.  
{HOST.*}, {ITEM.*}, {INVENTORY.*} and user macros are supported.  
---|---  
_Horizontal position_ | Select horizontal position of the item description - left, right or center.  
_Vertical position_ | Select vertical position of the item description - top, bottom or middle.  
_Size_ | Enter font size height for the item description (in percent relative to total widget height).  
_Bold_ | Mark the checkbox to display item description in bold type.  
_Color_ | Select the item description color from the color picker.  
`D` stands for default color (depends on the frontend theme). To return to the default value, click the _Use default_ button in the color picker.  
  
##### Value

These parameters determine how the item value should be displayed.

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/item_value_conf_value.png)

_Decimal places_ | Select how many decimal places will be displayed with the value. This value will affect only float items. For items with units set to "s", if this value is greater than 0 (the default is 2), the widget rounds the most significant time unit and displays a numeric value (e.g. "10.43m") instead of converting the value into a full time string. When set to 0, the seconds are converted to a human-readable time string (for example, "4h 56m 30s").  
---|---  
_Size_ | Enter font size height for the decimal places (in percent relative to total widget height).  
_Horizontal position_ | Select horizontal position of the item value - left, right or center.  
_Vertical position_ | Select vertical position of the item value - top, bottom or middle.  
_Size_ | Enter font size height for the item value (in percent relative to total widget height).  
Note that the size of item value is prioritized; other elements have to concede space for the value. With the change indicator though, if the value is too large, it will be truncated to show the change indicator.  
_Bold_ | Mark the checkbox to display item value in bold type.  
_Color_ | Select the item value color from the color picker.  
`D` stands for default color (depends on the frontend theme). To return to the default value, click the _Use default_ button in the color picker.  
**_Units_**  
_Units_ | Mark the checkbox to display units with the item value. If you enter a unit name, it will override the unit from item configuration.  
_Position_ | Select the item unit position - above, below, before or after the value.  
_Size_ | Enter font size height for the item unit (in percent relative to total widget height).  
_Bold_ | Mark the checkbox to display item unit in bold type.  
_Color_ | Select the item unit color from the color picker.  
`D` stands for default color (depends on the frontend theme). To return to the default value, click the _Use default_ button in the color picker.  
  
##### Time

These parameters determine how the time (clock value from the item history) should be displayed.

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/item_value_conf_time.png)

_Horizontal position_ | Select horizontal position of the time - left, right or center.  
---|---  
_Vertical position_ | Select vertical position of the time - top, bottom or middle.  
_Size_ | Enter font size height for the time (in percent relative to total widget height).  
_Bold_ | Mark the checkbox to display time in bold type.  
_Color_ | Select the time color from the color picker.  
`D` stands for default color (depends on the frontend theme). To return to the default value, click the _Use default_ button in the color picker.  
  
##### Change indicator

This section allows to select the color of change indicators from the color picker.

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/item_value_conf_change.png)

The change indicators are as follows:

  * **↑** \- item value is up (for numeric items)
  * **↓** \- item value is down (for numeric items)
  * **↕** \- item value has changed (for string items and items with value mapping)

`D` stands for default color (depends on the frontend theme). To return to the default value, click the _Use default_ button in the color picker.

Vertical size of the change indicator is equal to the size of the value (integer part of the value for numeric items).

Note that up and down indicators are not shown with just one value.

##### Sparkline

These parameters determine how the sparkline chart should be displayed.

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/item_value_conf_sparkline.png)

_Width_ | Set the graph line thickness by using the slider or manually entering a value in the range from 0 to 10.  
---|---  
_Color_ | Select line and fill color.  
_Fill_ | Set fill color transparency level by using the slider or manually entering a value in the range from 0 to 10.  
_Time period_ | Specify the time period for values to be included into the sparkline chart:  
**Dashboard** \- use time period of the dashboard;  
**Widget** \- use time period of the specified widget;  
**Custom** \- use a custom time period.  
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