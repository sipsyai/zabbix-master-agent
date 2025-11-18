---
title: Graph
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/dashboard/widget_fields/graph
downloaded: 2025-11-14 10:40:47
---

# 8 Graph

### Description

These parameters and the possible property values for the respective dashboard widget field objects allow to configure the [_Graph_](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/graph) widget in `dashboard.create` and `dashboard.update` methods.

Widget `fields` properties are not validated during the creation or update of a dashboard. This allows users to modify [built-in widgets](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets) and create [custom widgets](/documentation/current/en/devel/modules/tutorials/widget), but also introduces the risk of creating or updating widgets incorrectly. To ensure the successful creation or update of the _Graph_ widget, please refer to the parameter behavior outlined in the tables below.

### Parameters

The following parameters are supported for the _Graph_ widget.

_Refresh interval_ | 0 | rf_rate | 0 - No refresh;  
10 - 10 seconds;  
30 - 30 seconds;  
60 - _(default)_ 1 minute;  
120 - 2 minutes;  
600 - 10 minutes;  
900 - 15 minutes.  
---|---|---|---  
_Reference_ | 1 | reference | Any string value consisting of 5 characters (e.g., `ABCDE` or `JBPNL`). This value must be unique within the dashboard to which the widget belongs.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
  
#### Data set

The following parameters are supported for configuring a _Data set_.

The first number in the property name (e.g. ds.0.hosts.0, ds.0.items.0) represents the particular data set, while the second number, if present, represents the configured host or item.

_Data set type_ | 0 | ds.0.dataset_type | 0 - Item list;  
1 - _(default)_ Item patterns.  
---|---|---|---  
| _Items_ | 4 | ds.0.itemids.0 | [Item](/documentation/current/en/manual/api/reference/item/get) ID.  
  
When configuring the widget on a [template dashboard](/documentation/current/en/manual/api/reference/templatedashboard/object), only items configured on the template should be set.  
  
Note: To configure multiple items, create a dashboard widget field object for each item with an incremented number in the property name.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_ if _Data set type_ is set to "Item list" and _Items (Widget)_ is not set  
_Items (Widget)_ | 1 | ds.0.itemids.0._reference | Instead of [Item](/documentation/current/en/manual/api/reference/item/get) ID:  
`ABCDE._itemid` \- set a [compatible widget](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#widget-compatibility) (with its _Reference_ parameter set to "`ABCDE`") as the data source for items.  
  
Note: To configure multiple widgets, create a dashboard widget field object for each widget with an incremented number in the property name.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_ if _Data set type_ is set to "Item list" and _Items_ is not set  
_Color_ | 1 | ds.0.color.0 | Hexadecimal color code (e.g. `FF0000`).  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_ if _Data set type_ is set to "Item list"  
_Host patterns_ | 1 | ds.0.hosts.0 | [Host](/documentation/current/en/manual/api/reference/host/get) name or pattern (e.g., "Zabbix*").  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_ if _Data set type_ is set to "Item patterns"  
  
This parameter is not supported if configuring the widget on a [template dashboard](/documentation/current/en/manual/api/reference/templatedashboard/object).  
_Item patterns_ | 1 | ds.0.items.0 | [Item](/documentation/current/en/manual/api/reference/item/get) name or pattern (e.g., "*: Number of processed *values per second").  
  
When configuring the widget on a [template dashboard](/documentation/current/en/manual/api/reference/templatedashboard/object), only the patterns for items configured on the template should be set.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_ if _Data set type_ is set to "Item patterns"  
_Color_ | 1 | ds.0.color | Hexadecimal color code (e.g. `FF0000`).  
  
Default: `FF465C`.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Data set type_ is set to "Item patterns"  
_Draw_ | 0 | ds.0.type | 0 - _(default)_ Line;  
1 - Points;  
2 - Staircase;  
3 - Bar.  
_Stacked_ | 0 | ds.0.stacked | 0 - _(default)_ Disabled;  
1 - Enabled.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Draw_ is set to "Line", "Staircase", or "Bar"  
_Width_ | 0 | ds.0.width | Possible values range from 1-10.  
  
Default: 1.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Draw_ is set to "Line" or "Staircase"  
_Point size_ | 0 | ds.0.pointsize | Possible values range from 1-10.  
  
Default: 3.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Draw_ is set to "Points"  
_Transparency_ | 0 | ds.0.transparency | Possible values range from 1-10.  
  
Default: 5.  
_Fill_ | 0 | ds.0.fill | Possible values range from 1-10.  
  
Default: 3.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Draw_ is set to "Line" or "Staircase"  
_Missing data_ | 0 | ds.0.missingdatafunc | 0 - _(default)_ None;  
1 - Connected;  
2 - Treat as 0;  
3 - Last known.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Draw_ is set to "Line" or "Staircase"  
_Override host_ | 1 | ds.0.override_hostid._reference | `ABCDE._hostid`\- set a compatible widget (with its "Reference" parameter set to "`ABCDE`") as the data source for hosts;  
`DASHBOARD._hostid` \- set the dashboard Host selector as the data source for hosts.  
  
This parameter is not supported if configuring the widget on a [template dashboard](/documentation/current/en/manual/api/reference/templatedashboard/object).  
_Y-axis_ | 0 | ds.0.axisy | 0 - _(default)_ Left;  
1 - Right.  
_Time shift_ | 1 | ds.0.timeshift | Valid time string (e.g. `3600`, `1h`, etc.).  
You may use [time suffixes](/documentation/current/en/manual/appendix/suffixes#time-suffixes). Negative values are also allowed.  
  
Default: `""` (empty).  
_Aggregation function_ | 0 | ds.0.aggregate_function | 0 - _(default)_ not used;  
1 - min;  
2 - max;  
3 - avg;  
4 - count;  
5 - sum;  
6 - first;  
7 - last.  
_Aggregation interval_ | 1 | ds.0.aggregate_interval | Valid time string (e.g. `3600`, `1h`, etc.).  
You may use [time suffixes](/documentation/current/en/manual/appendix/suffixes#time-suffixes).  
  
Default: `1h`.  
_Aggregate_ | 0 | ds.0.aggregate_grouping | 0 - _(default)_ Each item;  
1 - Data set.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Aggregation function_ is set to "min", "max", "avg", "count", "sum", "first", or "last"  
_Approximation_ | 0 | ds.0.approximation | 1 - min;  
2 - _(default)_ avg;  
4 - max;  
7 - all.  
_Data set label_ | 1 | ds.0.data_set_label | Any string value.  
  
Default: `""` (empty).  
  
#### Display options

The following parameters are supported for configuring _Display options_.

_History data selection_ | 0 | source | 0 - _(default)_ Auto;  
1 - History;  
2 - Trends.  
---|---|---|---  
_Simple triggers_ | 0 | simple_triggers | 0 - _(default)_ Disabled;  
1 - Enabled.  
_Working time_ | 0 | working_time | 0 - _(default)_ Disabled;  
1 - Enabled.  
_Percentile line (left)_  
| _Status_ | 0 | percentile_left | 0 - _(default)_ Disabled;  
1 - Enabled.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Y-axis_ (in _Data set_ configuration) is set to "Left"  
_Value_ | 0 | percentile_left_value | Possible values range from 1-100.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Y-axis_ (in _Data set_ configuration) is set to "Left"  
_Percentile line (right)_  
| _Status_ | 0 | percentile_right | 0 - _(default)_ Disabled;  
1 - Enabled.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Y-axis_ (in _Data set_ configuration) is set to "Right"  
_Value_ | 0 | percentile_right_value | Possible values range from 1-100.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Y-axis_ (in _Data set_ configuration) is set to "Right"  
  
#### Time period

The following parameters are supported for configuring _Time period_.

_Time period_ | 1 | time_period._reference | `DASHBOARD._timeperiod` \- set the [_Time period_ selector](/documentation/current/en/manual/web_interface/time_period_selector) as the data source;  
`ABCDE._timeperiod` \- set a [compatible widget](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#widget-compatibility) (with its _Reference_ parameter set to "`ABCDE`") as the data source.  
  
Default: `DASHBOARD._timeperiod`  
  
Alternatively, you can set the time period only in the _From_ and _To_ parameters.  
---|---|---|---  
| _From_ | 1 | time_period.from | Valid time string in absolute (`YYYY-MM-DD hh:mm:ss`) or [relative](/documentation/current/en/manual/web_interface/time_period_selector) time syntax (`now`, `now/d`, `now/w-1w`, etc.).  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Time period_ is not set  
_To_ | 1 | time_period.to | Valid time string in absolute (`YYYY-MM-DD hh:mm:ss`) or [relative](/documentation/current/en/manual/web_interface/time_period_selector) time syntax (`now`, `now/d`, `now/w-1w`, etc.).  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Time period_ is not set  
  
#### Axes

The following parameters are supported for configuring _Axes_.

_Left Y_ | 0 | lefty | 0 - Disabled;  
1 - _(default)_ Enabled.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Y-axis_ (in _Data set_ configuration) is set to "Left"  
---|---|---|---  
_Right Y_ | 0 | righty | 0 - _(default)_ Disabled;  
1 - Enabled.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Y-axis_ (in _Data set_ configuration) is set to "Right"  
_Scale_ | 0 | lefty_scale | 0 - _(default)_ Linear;  
1 - Logarithmic.  
righty_scale  
_Min_ | 1 | lefty_min | Any numeric value.  
  
Default: `""` (empty).  
righty_min  
_Max_ | 1 | lefty_max | Any numeric value.  
  
Default: `""` (empty).  
righty_max  
_Units_ (type) | 0 | lefty_units | 0 - _(default)_ Auto;  
1 - Static.  
righty_units  
_Units_ (value) | 1 | lefty_static_units | Any string value.  
  
Default: `""` (empty).  
righty_static_units  
_X-Axis_ | 0 | xaxis | 0 - Disabled;  
1 - _(default)_ Enabled.  
  
#### Legend

The following parameters are supported for configuring _Legend_.

_Show legend_ | 0 | legend | 0 - Disabled;  
1 - _(default)_ Enabled.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Show legend_ is set to "Enabled"  
---|---|---|---  
_Display min/avg/max_ | 0 | legend_statistic | 0 - _(default)_ Disabled;  
1 - Enabled.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Show legend_ is set to "Enabled"  
_Show aggregation function_ | 0 | legend_aggregation | 0 - _(default)_ Disabled;  
1 - Enabled.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Show legend_ is set to "Enabled"  
_Rows_ | 0 | legend_lines_mode | 0 - _(default)_ Fixed;  
1 - Variable.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Show legend_ is set to "Enabled"  
_Number of rows/_  
_Maximum number of rows_ | 0 | legend_lines | Possible values range from 1-10.  
  
Default: 1.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Show legend_ is set to "Enabled"  
_Number of columns_ | 0 | legend_columns | Possible values range from 1-4.  
  
Default: 4.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Show legend_ is set to "Enabled", and _Display min/avg/max_ is set to "Disabled"  
  
#### Problems

The following parameters are supported for configuring _Problems_.

_Show problems_ | 0 | show_problems | 0 - _(default)_ Disabled;  
1 - Enabled.  
---|---|---|---  
_Selected items only_ | 0 | graph_item_problems | 0 - Disabled;  
1 - _(default)_ Enabled.  
_Problem hosts_ | 1 | problemhosts.0 | [Host](/documentation/current/en/manual/api/reference/host/get) name.  
  
Note: The number in the property name references the configured host.  
To configure multiple hosts, create a dashboard widget field object for each host with an incremented number in the property name.  
  
This parameter is not supported if configuring the widget on a [template dashboard](/documentation/current/en/manual/api/reference/templatedashboard/object).  
_Severity_ | 0 | severities.0 | 0 - Not classified;  
1 - Information;  
2 - Warning;  
3 - Average;  
4 - High;  
5 - Disaster.  
  
Default: empty (all enabled).  
  
Note: To configure multiple values, create a dashboard widget field object for each value with an incremented number in the property name.  
_Problem_ | 1 | problem_name | Problem [event name](/documentation/current/en/manual/config/triggers/trigger#configuration) (case insensitive, full name or part of it).  
_Problem tags_  
| _Evaluation type_ | 0 | evaltype | 0 - _(default)_ And/Or;  
2 - Or.  
_Tag name_ | 1 | tags.0.tag | Any string value.  
  
Note: The number in the property name references tag order in the tag evaluation list.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_ if configuring _Problem tags_  
_Operator_ | 0 | tags.0.operator | 0 - Contains;  
1 - Equals;  
2 - Does not contain;  
3 - Does not equal;  
4 - Exists;  
5 - Does not exist.  
  
Note: The number in the property name references tag order in the tag evaluation list.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_ if configuring _Problem tags_  
_Tag value_ | 1 | tags.0.value | Any string value.  
  
Note: The number in the property name references tag order in the tag evaluation list.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_ if configuring _Problem tags_  
  
#### Overrides

The following parameters are supported for configuring _Overrides_.

The first number in the property name (e.g. or.0.hosts.0, or.0.items.0) represents the particular data set, while the second number, if present, represents the configured host or item.

_Host patterns_ | 1 | or.0.hosts.0 | [Host](/documentation/current/en/manual/api/reference/host/get) name or pattern (e.g. `Zabbix*`).  
  
This parameter is not supported if configuring the widget on a [template dashboard](/documentation/current/en/manual/api/reference/templatedashboard/object).  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_ if configuring _Overrides_  
---|---|---|---  
_Item patterns_ | 1 | or.0.items.0 | [Item](/documentation/current/en/manual/api/reference/item/get) name or pattern (e.g. `*: Number of processed *values per second`).  
When configuring the widget on a [template dashboard](/documentation/current/en/manual/api/reference/templatedashboard/object), only the patterns for items configured on the template should be set.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_ if configuring _Overrides_  
_Base color_ | 1 | or.0.color | Hexadecimal color code (e.g. `FF0000`).  
_Width_ | 0 | or.0.width | Possible values range from 1-10.  
_Draw_ | 0 | or.0.type | 0 - Line;  
1 - Points;  
2 - Staircase;  
3 - Bar.  
_Transparency_ | 0 | or.0.transparency | Possible values range from 1-10.  
_Fill_ | 0 | or.0.fill | Possible values range from 1-10.  
_Point size_ | 0 | or.0.pointsize | Possible values range from 1-10.  
_Missing data_ | 0 | or.0.missingdatafunc | 0 - None;  
1 - Connected;  
2 - Treat as 0;  
3 - Last known.  
_Y-axis_ | 0 | or.0.axisy | 0 - Left;  
1 - Right.  
_Time shift_ | 1 | or.0.timeshift | Valid time string (e.g. `3600`, `1h`, etc.).  
You may use [time suffixes](/documentation/current/en/manual/appendix/suffixes#time-suffixes). Negative values are allowed.  
  
### Examples

The following examples aim to only describe the configuration of the dashboard widget field objects for the _Graph_ widget. For more information on configuring a dashboard, see [`dashboard.create`](/documentation/current/en/manual/api/reference/dashboard/create).

#### Configuring a _Graph_ widget

Configure a _Graph_ widget in the following way:

  * 2 data sets for a total of 9 items on 1 host.
  * The first data set is of type "Item list" and consists of 3 items that are represented by lines with a different color, but the same width, transparency, and fill.
  * The second data set is of type "Item patterns", consists of 6 items, has a configured aggregation, and is represented by a line with a custom color, width, transparency, and fill.
  * The second data set also has a custom data set label.
  * Data in the graph are displayed for a time period of the last 3 hours.
  * Problems in the graph are displayed only for the configured items.
  * Graph has two Y axes of which the right Y axis displays values only for the second data set.
  * Graph legend displays configured items in 4 rows, as well as minimum, maximum and average values of the data sets.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "dashboard.create",
               "params": {
                   "name": "My dashboard",
                   "display_period": 30,
                   "auto_start": 1,
                   "pages": [
                       {
                           "widgets": [
                               {
                                   "type": "svggraph",
                                   "name": "Graph",
                                   "x": 0,
                                   "y": 0,
                                   "width": 36,
                                   "height": 5,
                                   "view_mode": 0,
                                   "fields": [
                                       {
                                           "type": 0,
                                           "name": "ds.0.dataset_type",
                                           "value": 0
                                       },
                                       {
                                           "type": 4,
                                           "name": "ds.0.itemids.1",
                                           "value": 23264
                                       },
                                       {
                                           "type": 1,
                                           "name": "ds.0.color.1",
                                           "value": "FF0000"
                                       },
                                       {
                                           "type": 4,
                                           "name": "ds.0.itemids.2",
                                           "value": 23269
                                       },
                                       {
                                           "type": 1,
                                           "name": "ds.0.color.2",
                                           "value": "BF00FF"
                                       },
                                       {
                                           "type": 4,
                                           "name": "ds.0.itemids.3",
                                           "value": 23257
                                       },
                                       {
                                           "type": 1,
                                           "name": "ds.0.color.3",
                                           "value": "0040FF"
                                       },
                                       {
                                           "type": 0,
                                           "name": "ds.0.width",
                                           "value": 3
                                       },
                                       {
                                           "type": 0,
                                           "name": "ds.0.transparency",
                                           "value": 3
                                       },
                                       {
                                           "type": 0,
                                           "name": "ds.0.fill",
                                           "value": 1
                                       },
                                       {
                                           "type": 1,
                                           "name": "ds.1.hosts.0",
                                           "value": "Zabbix server"
                                       },
                                       {
                                           "type": 1,
                                           "name": "ds.1.items.0",
                                           "value": "*: Number of processed *values per second"
                                       },
                                       {
                                           "type": 1,
                                           "name": "ds.1.color",
                                           "value": "000000"
                                       },
                                       {
                                           "type": 0,
                                           "name": "ds.1.transparency",
                                           "value": 0
                                       },
                                       {
                                           "type": 0,
                                           "name": "ds.1.fill",
                                           "value": 0
                                       },
                                       {
                                           "type": 0,
                                           "name": "ds.1.axisy",
                                           "value": 1
                                       },
                                       {
                                           "type": 0,
                                           "name": "ds.1.aggregate_function",
                                           "value": 3
                                       },
                                       {
                                           "type": 1,
                                           "name": "ds.1.aggregate_interval",
                                           "value": "1m"
                                       },
                                       {
                                           "type": 0,
                                           "name": "ds.1.aggregate_grouping",
                                           "value": 1
                                       },
                                       {
                                           "type": 1,
                                           "name": "ds.1.data_set_label",
                                           "value": "Number of processed values per second"
                                       },
                                       {
                                           "type": 0,
                                           "name": "graph_time",
                                           "value": 1
                                       },
                                       {
                                           "type": 1,
                                           "name": "time_period.from",
                                           "value": "now-3h"
                                       },
                                       {
                                           "type": 0,
                                           "name": "legend_statistic",
                                           "value": 1
                                       },
                                       {
                                           "type": 0,
                                           "name": "legend_lines",
                                           "value": 4
                                       },
                                       {
                                           "type": 0,
                                           "name": "show_problems",
                                           "value": 1
                                       },
                                       {
                                           "type": 1,
                                           "name": "reference",
                                           "value": "YZABC"
                                       }
                                   ]
                               }
                           ]
                       }
                   ],
                   "userGroups": [
                       {
                           "usrgrpid": 7,
                           "permission": 2
                       }
                   ],
                   "users": [
                       {
                           "userid": 1,
                           "permission": 3
                       }
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "dashboardids": [
                       "3"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### See also

  * [Dashboard widget field](/documentation/current/en/manual/api/reference/dashboard/object#dashboard-widget-field)
  * [`dashboard.create`](/documentation/current/en/manual/api/reference/dashboard/create)
  * [`dashboard.update`](/documentation/current/en/manual/api/reference/dashboard/update)