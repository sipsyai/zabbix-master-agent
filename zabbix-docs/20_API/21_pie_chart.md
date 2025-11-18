---
title: Pie chart
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/dashboard/widget_fields/pie_chart
downloaded: 2025-11-14 10:41:01
---

# 21 Pie chart

### Description

These parameters and the possible property values for the respective dashboard widget field objects allow to configure the [_Pie chart_](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/pie_chart) widget in `dashboard.create` and `dashboard.update` methods.

Widget `fields` properties are not validated during the creation or update of a dashboard. This allows users to modify [built-in widgets](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets) and create [custom widgets](/documentation/current/en/devel/modules/tutorials/widget), but also introduces the risk of creating or updating widgets incorrectly. To ensure the successful creation or update of the _Pie chart_ widget, please refer to the parameter behavior outlined in the tables below.

### Parameters

The following parameters are supported for the _Pie chart_ widget.

_Refresh interval_ | 0 | rf_rate | 0 - No refresh;  
10 - 10 seconds;  
30 - 30 seconds;  
60 - _(default)_ 1 minute;  
120 - 2 minutes;  
600 - 10 minutes;  
900 - 15 minutes.  
---|---|---|---  
  
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
\- _supported_ if _Data set type_ is set to "Item list"  
_Item type_ | 0 | ds.0.type.0 | 0 - _(default)_ Normal;  
1 - Total.  
  
The value "Total" can be set only for one item in the whole chart.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Data set type_ is set to "Item list"  
_Host patterns_ | 1 | ds.0.hosts.0 | [Host](/documentation/current/en/manual/api/reference/host/get) name or pattern (e.g., "Zabbix*").  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_ if _Data set type_ is set to "Item patterns"  
  
This parameter is not supported if configuring the widget on a [template dashboard](/documentation/current/en/manual/api/reference/templatedashboard/object).  
_Item patterns_ | 1 | ds.0.items.0 | [Item](/documentation/current/en/manual/api/reference/item/get) name or pattern (e.g., "*: Number of processed *values per second").  
  
When configuring the widget on a [template dashboard](/documentation/current/en/manual/api/reference/templatedashboard/object), only the patterns for items configured on the template should be set.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_ if _Data set type_ is set to "Item patterns"  
_Color_ | 1 | ds.0.color | Hexadecimal color code (e.g. `FF0000`).  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Data set type_ is set to "Item patterns"  
_Aggregation function_ | 0 | ds.0.aggregate_function | 1 - min;  
2 - max;  
3 - avg;  
4 - count;  
5 - sum;  
6 - first;  
7 - _(default)_ last.  
_Data set aggregation_ | 0 | ds.0.dataset_aggregation | 0 - _(default)_ none;  
1 - min;  
2 - max;  
3 - avg;  
4 - count;  
5 - sum.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Item type_ is set to "Total"  
_Data set label_ | 1 | ds.0.data_set_label | Any string value.  
  
Default: `""` (empty).  
  
#### Displaying options

The following parameters are supported for configuring _Displaying options_.

_History data selection_ | 0 | source | 0 - _(default)_ Auto;  
1 - History;  
2 - Trends.  
---|---|---|---  
_Draw_ | 0 | draw_type | 0 - _(default)_ Pie;  
1 - Doughnut.  
| _Width_ | 0 | width | 20 - 20% of the radius;  
30 - 30% of the radius;  
40 - 40% of the radius;  
50 - _(default)_ 50% of the radius.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Draw_ is set to "Doughnut"  
_Stroke width_ | 0 | stroke | Possible values range from 0-10.  
  
Default: 0.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Draw_ is set to "Doughnut"  
_Show total value_ | 0 | total_show | 0 - _(default)_ Disabled;  
1 - Enabled.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Draw_ is set to "Doughnut"  
_Size_ | 0 | value_size_type | 0 - _(default)_ Auto;  
1 - Custom.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Show total value_ is set to "Enabled"  
_Size_ (value for custom size) | 0 | value_size | Possible values range from 1-100.  
  
Default: 20.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Show total value_ is set to "Enabled"  
_Decimal places_ | 0 | decimal_places | Possible values range from 0-6.  
  
Default: 2.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Show total value_ is set to "Enabled"  
_Units_ (checkbox) | 0 | units_show | 0 - _(default)_ Disabled;  
1 - Enabled.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Show total value_ is set to "Enabled"  
_Units_ (value) | 1 | units | Any string value.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Units_ (checkbox) is set to "Enabled"  
_Bold_ | 0 | value_bold | 0 - _(default)_ Disabled;  
1 - Enabled.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Show total value_ is set to "Enabled"  
_Color_ | 1 | value_color | Hexadecimal color code (e.g. `FF0000`).  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Show total value_ is set to "Enabled"  
_Space between sectors_ | 0 | space | Possible values range from 0-10.  
  
Default: 1.  
_Merge sectors smaller than N%_ (checkbox) | 0 | merge | 0 - _(default)_ Disabled;  
1 - Enabled.  
_Merge sectors smaller than N%_ (value) | 0 | merge_percent | Possible values range from 1-10.  
  
Default: 1.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Merge sectors smaller than N%_ (checkbox) is set to "Enabled"  
_Merge sectors smaller than N%_ (color) | 1 | merge_color | Hexadecimal color code (e.g. `FF0000`).  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Merge sectors smaller than N%_ (checkbox) is set to "Enabled"  
  
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
  
#### Legend

The following parameters are supported for configuring _Legend_.

_Show legend_ | 0 | legend | 0 - Disabled;  
1 - _(default)_ Enabled.  
---|---|---|---  
_Show value_ | 0 | legend_value | 0 - _(default)_ Disabled;  
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
\- _supported_ if _Show legend_ is set to "Enabled", and _Show value_ is set to "Disabled"  
  
### Examples

The following examples aim to only describe the configuration of the dashboard widget field objects for the _Pie chart_ widget. For more information on configuring a dashboard, see [`dashboard.create`](/documentation/current/en/manual/api/reference/dashboard/create).

#### Configuring a _Pie chart_ widget

Configure a _Pie chart_ widget in the following way:

  * 2 data sets for a total of 9 items on 1 host.
  * The first data set is of type "Item list" and consists of 3 items that are all with type "Normal" and represented by a different color.
  * The second data set is of type "Item patterns", consists of 6 items, has a configured aggregation for each item, and is represented by a custom color.
  * The second data set also has a custom data set label.
  * Data in the pie chart are displayed as a doughnut chart with a custom width and total value with units in the center.
  * Data in the pie chart are displayed and aggregated for a custom time period of the last 3 hours.
  * Pie chart legend displays configured items in 4 rows.

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
                                   "type": "piechart",
                                   "name": "Pie chart",
                                   "x": 0,
                                   "y": 0,
                                   "width": 24,
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
                                           "type": 0,
                                           "name": "ds.0.type.1",
                                           "value": 0
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
                                         "type": 0,
                                         "name": "ds.0.type.2",
                                         "value": 0
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
                                         "name": "ds.0.type.3",
                                         "value": 0
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
                                           "name": "ds.1.aggregate_function",
                                           "value": 3
                                       },
                                       {
                                           "type": 1,
                                           "name": "ds.1.data_set_label",
                                           "value": "Number of processed values per second"
                                       },
                                       {
                                           "type": 0,
                                           "name": "draw_type",
                                           "value": 1
                                       },
                                       {
                                           "type": 0,
                                           "name": "width",
                                           "value": 30
                                       },
                                       {
                                           "type": 0,
                                           "name": "total_show",
                                           "value": 1
                                       },
                                       {
                                           "type": 0,
                                           "name": "units_show",
                                           "value": 1
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
                                           "name": "legend_lines",
                                           "value": 4
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