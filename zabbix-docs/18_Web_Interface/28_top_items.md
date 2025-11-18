---
title: Top items
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/top_items
downloaded: 2025-11-14 10:38:26
---

# 28 Top items  
  
#### Overview

In the _Top items_ widget, you can display top (or bottom) values for a group of items.

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/top_items.png)

It is possible to select items directly or by pattern, customize column ordering and highlighting.

The color of problem items is based on the problem severity color, which can be adjusted in the [problem update](/documentation/current/en/manual/acknowledgment#updating-problems) screen.

By default, only values that fall within the last 24 hours are displayed. This limit has been introduced with the aim of improving initial loading times for large pages of latest data. This limit is configurable in _Administration_ → _General_ → _[GUI](/documentation/current/en/manual/web_interface/frontend_sections/administration/general#gui)_ , using the _Max history display period_ option.

Clicking on item value opens the [item menu](/documentation/current/en/manual/web_interface/menu/item_menu).

#### Configuration

To configure, select _Top items_ as type:

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/top_items_conf.png)

In addition to the parameters that are [common](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#common-parameters) for all widgets, you may set the following specific options:

_Host groups_ | Select host groups.  
Alternatively, select a compatible widget as the [data source](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/#dynamic-parameters) for host groups.  
This field is auto-complete so starting to type the name of a group will offer a dropdown of matching groups.  
This parameter is not available when configuring the widget on a [template dashboard](/documentation/current/en/manual/config/templates/template#adding-dashboards).  
---|---  
_Hosts_ | Select hosts.  
Alternatively, select a compatible widget or the dashboard as the [data source](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/#dynamic-parameters) for hosts.  
This field is auto-complete so starting to type the name of a host will offer a dropdown of matching hosts.  
This parameter is not available when configuring the widget on a [template dashboard](/documentation/current/en/manual/config/templates/template#adding-dashboards).  
_Host tags_ | Specify tags to limit the number of host data displayed in the widget.  
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
_Layout_ | Select the layout option:  
**Horizontal** \- host names will be displayed on the left;  
**Vertical** \- host names will be displayed at the top.  
_Show problems_ | Select how to display problems:  
**All** \- display all problems;  
**Unsuppressed** \- only display problems that are not suppressed due to host mainteneance;  
**None** \- do not display problems at all.  
_Note_ that when a problem state is represented, it overrides the display style settings from item column configuration.  
_Items_ | Add item patterns or specific items for display (see Column configuration).  
**_Advanced configuration_**  
_Host ordering_ | Select ordering options for the host column/row.  
| _Order by_ | Order hosts by:  
**Host name** \- hosts will be ordered by host name;  
**Item value** \- hosts will be ordered by the value of selected items.  
_Order_ | Select whether to display the highest or lowest values:  
**TopN** \- top N values;  
**BottomN** \- bottom N values.  
The value of N is selected in the _Limit_ field.  
_Limit_ | Enter limit for displayable hosts (range 1-1000; default 10).  
This value will become the value of N in the _Order_ field.  
_Item ordering_ | Select ordering options for the item column/row.  
| _Order by_ | Order items by:  
**Item value** \- items will be ordered by item value;  
**Item name** \- items will be ordered by item name;  
**Host** \- items will be ordered by the selected host pattern.  
_Order_ | Select whether to display the highest or lowest values:  
**TopN** \- top N values;  
**BottomN** \- bottom N values.  
The value of N is selected in the _Limit_ field.  
_Limit_ | Enter limit for displayable items (range 1-1000; default 10).  
This value will become the value of N in the _Order_ field.  
_Show column header_ | Select column header display options:  
**Off** \- do not display column header;  
**Horizontal** \- display text horizontally in the header;  
**Vertical** \- display text vertically in the header.  
  
#### Column configuration

To configure item columns, click _Add_ in the _Items_ parameter:

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/top_items_column.png)

Common column parameters:

_Item patterns_ | Specify one or several item patterns, using the wildcard character.  
Alternatively, select the items.  
When configuring the widget on a [template dashboard](/documentation/current/en/manual/config/templates/template#adding-dashboards), only [items configured on the template](/documentation/current/en/manual/config/templates/template#adding-items-triggers-graphs) can be selected.  
---|---  
_Item tags_ | Specify tags to limit the number of item data displayed in the widget.  
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
_Base color_ | Select the column's background color or fill color if _Display_ is set to "Bar" or "Indicators".  
Note that the base color can be overridden by threshold or highlight colors.  
_Display value as_ | Format for displaying the item value: **Numeric** or **Text**.  
  
The selected option determines which additional parameters will be available. Refer to the parameter list for each format below.  
  
Column parameters for numeric values:

_Display_ | Define how the value should be displayed:  
**As is** \- as regular text;  
**Bar** \- as solid, color-filled bar;  
**Indicators** \- as segmented, color-filled bar;  
**Sparkline** \- mini line graph.  
---|---  
_Min_ | Minimum value for bar/indicators display.  
_Max_ | Maximum value for bar/indicators display.  
_Width_ | Set the graph line thickness by using the slider or manually entering a value in the range from 0 to 10.  
This parameter is for sparkline display only.  
_Fill_ | Set fill color transparency level by using the slider or manually entering a value in the range from 0 to 10.  
This parameter is for sparkline display only.  
_Color_ | Select line and fill color.  
This parameter is for sparkline display only.  
See _Advanced configuration_ for description of fields related to time period and history data selection.  
_Thresholds_ | Specify threshold values when the background/fill color should change.  
The list will be sorted in ascending order when saved.  
For sparklines, thresholds are applied only to the item last value.  
_Decimal places_ | Specify how many decimal places will be displayed with the value.  
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
This parameter is available only for numeric item values. For text values data will always be taken from history.  
  
Column parameters for text values:

_Highlights_ | Specify the regular expressions upon matching which the background/fill color should change.  
---|---