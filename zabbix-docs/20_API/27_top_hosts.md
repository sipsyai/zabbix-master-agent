---
title: Top hosts
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/dashboard/widget_fields/top_hosts
downloaded: 2025-11-14 10:41:07
---

# 27 Top hosts

### Description

These parameters and the possible property values for the respective dashboard widget field objects allow to configure the [_Top hosts_](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/top_hosts) widget in `dashboard.create` and `dashboard.update` methods.

Widget `fields` properties are not validated during the creation or update of a dashboard. This allows users to modify [built-in widgets](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets) and create [custom widgets](/documentation/current/en/devel/modules/tutorials/widget), but also introduces the risk of creating or updating widgets incorrectly. To ensure the successful creation or update of the _Top hosts_ widget, please refer to the parameter behavior outlined in the tables below.

### Parameters

The following parameters are supported for the _Top hosts_ widget.

_Refresh interval_ | 0 | rf_rate | 0 - No refresh;  
10 - 10 seconds;  
30 - 30 seconds;  
60 - _(default)_ 1 minute;  
120 - 2 minutes;  
600 - 10 minutes;  
900 - 15 minutes.  
---|---|---|---  
_Host groups_ | 2 | groupids.0 | [Host group](/documentation/current/en/manual/api/reference/hostgroup/get) ID.  
  
Note: To configure multiple host groups, create a dashboard widget field object for each host group with an incremented number in the property name.  
  
This parameter is not supported if configuring the widget on a [template dashboard](/documentation/current/en/manual/api/reference/templatedashboard/object).  
| _Host groups (Widget)_ | 1 | groupids._reference | Instead of [Host group](/documentation/current/en/manual/api/reference/hostgroup/get) ID:  
`ABCDE._hostgroupids` \- set a [compatible widget](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#widget-compatibility) (with its _Reference_ parameter set to "`ABCDE`") as the data source for host groups.  
  
This parameter is not supported if configuring the widget on a [template dashboard](/documentation/current/en/manual/api/reference/templatedashboard/object).  
_Hosts_ | 3 | hostids.0 | [Host](/documentation/current/en/manual/api/reference/host/get) ID.  
  
Note: To configure multiple hosts, create a dashboard widget field object for each host with an incremented number in the property name. For multiple hosts, the parameter _Host groups_ must either be not configured at all or configured with at least one host group that the configured hosts belong to.  
  
This parameter is not supported if configuring the widget on a [template dashboard](/documentation/current/en/manual/api/reference/templatedashboard/object).  
| _Hosts (Widget/Dashboard)_ | 1 | hostids._reference | Instead of [Host](/documentation/current/en/manual/api/reference/host/get) ID:  
`DASHBOARD.hostids` \- set the [_Host_ selector](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#override-host) as the data source for hosts;  
`ABCDE._hostids` \- set a [compatible widget](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#widget-compatibility) (with its _Reference_ parameter set to "`ABCDE`") as the data source for hosts.  
  
This parameter is not supported if configuring the widget on a [template dashboard](/documentation/current/en/manual/api/reference/templatedashboard/object).  
_Host tags_  
| _Evaluation type_ | 0 | evaltype | 0 - _(default)_ And/Or;  
2 - Or.  
  
This parameter is not supported if configuring the widget on a [template dashboard](/documentation/current/en/manual/api/reference/templatedashboard/object).  
_Tag name_ | 1 | tags.0.tag | Any string value.  
  
Note: The number in the property name references tag order in the tag evaluation list.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_ if configuring _Host tags_  
  
This parameter is not supported if configuring the widget on a [template dashboard](/documentation/current/en/manual/api/reference/templatedashboard/object).  
_Operator_ | 0 | tags.0.operator | 0 - Contains;  
1 - Equals;  
2 - Does not contain;  
3 - Does not equal;  
4 - Exists;  
5 - Does not exist.  
  
Note: The number in the property name references tag order in the tag evaluation list.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_ if configuring _Host tags_  
  
This parameter is not supported if configuring the widget on a [template dashboard](/documentation/current/en/manual/api/reference/templatedashboard/object).  
_Tag value_ | 1 | tags.0.value | Any string value.  
  
Note: The number in the property name references tag order in the tag evaluation list.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_ if configuring _Host tags_  
  
This parameter is not supported if configuring the widget on a [template dashboard](/documentation/current/en/manual/api/reference/templatedashboard/object).  
_Show hosts in maintenance_ | 0 | maintenance | 0 - _(default)_ Disabled;  
1 - Enabled.  
_Columns_ (see below)  
_Order by_ | 0 | column | Column numeric value from the configured columns.  
_Order_ | 0 | order | 2 - _(default)_ Top N;  
3 - Bottom N.  
_Host limit_ | 0 | show_lines | Possible values range from 1-1000.  
  
Default: 10.  
  
This parameter is not supported if configuring the widget on a [template dashboard](/documentation/current/en/manual/api/reference/templatedashboard/object).  
  
#### Columns

Columns have common parameters and additional parameters depending on the configuration of the parameter _Data_.

For all parameters related to columns the number in the property name (e.g. columns.0.name) references a column for which the parameter is configured.

The following parameters are supported for all columns.

_Name_ | 1 | columns.0.name | Any string value.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
---|---|---|---  
_Data_ | 0 | columns.0.data | 1 - Item value;  
2 - Host name;  
3 - Text.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
_Base color_ | 1 | columns.0.base_color | Hexadecimal color code (e.g. `FF0000`).  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
  
##### Item value

The following parameters are supported if _Data_ is set to "Item value".

The first number in the _Thresholds_ property name (e.g. columnsthresholds.0.color.0) references the column for which thresholds are configured, while the second number references threshold place in a list, sorted in ascending order. However, if thresholds are configured in a different order, the values will be sorted in ascending order after updating widget configuration in Zabbix frontend (e.g. `"threshold.0.threshold":"5"` → `"threshold.0.threshold":"1"`; `"threshold.1.threshold":"1"` → `"threshold.1.threshold": "5"`).

_Item_ | 1 | columns.0.item | Valid item name.  
  
When configuring the widget on a [template dashboard](/documentation/current/en/manual/api/reference/templatedashboard/object), only items configured on the template should be set.  
---|---|---|---  
_Display item value as_ | 0 | columns.0.display_value_as | 0 - _(default)_ Numeric;  
1 - Text;  
2 - Binary.  
_Display_ | 0 | columns.0.display | 1 - _(default)_ As is;  
2 - Bar;  
3 - Indicators;  
6 - Sparkline.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Display item value as_ is set to "Numeric"  
_Min_ | 1 | columns.0.min | Any numeric value.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Display item value as_ is set to "Numeric" and _Display_ is set to "Bar" or "Indicators"  
_Max_ | 1 | columns.0.max | Any numeric value.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Display item value as_ is set to "Numeric" and _Display_ is set to "Bar" or "Indicators"  
_Decimal places_ | 0 | columns.0.decimal_places | Possible values range from 0-10.  
  
Default: 2.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Display item value as_ is set to "Numeric"  
_Sparkline_  
| _Width_ | 0 | columns.0.sparkline.width | Possible values range from 0-10.  
  
Default: 1.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Display item value as_ is set to "Numeric" and _Display_ is set to "Sparkline"  
_Fill_ | 0 | columns.0.sparkline.fill | Possible values range from 0-10.  
  
Default: 3.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Display item value as_ is set to "Numeric" and _Display_ is set to "Sparkline"  
_Color_ | 1 | columns.0.sparkline.color | Hexadecimal color code (e.g. `FF0000`).  
  
Default: `42A5F5`.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Display item value as_ is set to "Numeric" and _Display_ is set to "Sparkline"  
_Time period_ | 1 | columns.0.sparkline.time_period._reference | `DASHBOARD._timeperiod` \- set the [_Time period_ selector](/documentation/current/en/manual/web_interface/time_period_selector) as the data source;  
`ABCDE._timeperiod` \- set a [compatible widget](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#widget-compatibility) (with its `reference` parameter equal to `ABCDE`) as the data source.  
  
Default: `DASHBOARD._timeperiod`  
  
Alternatively, you can set the time period only in the _From_ and _To_ parameters.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Display item value as_ is set to "Numeric" and _Display_ is set to "Sparkline"  
_From_ | 1 | columns.0.sparkline.time_period.from | Valid time string in absolute (`YYYY-MM-DD hh:mm:ss`) or [relative](/documentation/current/en/manual/web_interface/time_period_selector) time syntax (`now`, `now/d`, `now/w-1w`, etc.).  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Display item value as_ is set to "Numeric" and _Display_ is set to "Sparkline"  
_To_ | 1 | columns.0.sparkline.time_period.to | Valid time string in absolute (`YYYY-MM-DD hh:mm:ss`) or [relative](/documentation/current/en/manual/web_interface/time_period_selector) time syntax (`now`, `now/d`, `now/w-1w`, etc.).  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Display item value as_ is set to "Numeric" and _Display_ is set to "Sparkline"  
_History data_ | 0 | columns.0.sparkline.history | 0 - _(default)_ Auto;  
1 - History;  
2 - Trends.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Display item value as_ is set to "Numeric" and _Display_ is set to "Sparkline"  
_Thresholds_  
| _Color_ | 1 | columnsthresholds.0.color.0 | Hexadecimal color code (e.g. `FF0000`).  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Display item value as_ is set to "Numeric"  
_Threshold_ | 1 | columnsthresholds.0.threshold.0 | Any string value.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Display item value as_ is set to "Numeric"  
_Highlights_  
| _Color_ | 1 | columns.0.highlights.0.color | Hexadecimal color code (e.g. `FF0000`).  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Display item value as_ is set to "Text"  
_Pattern_ | 1 | columns.0.highlights.0.pattern | Any string value.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Display item value as_ is set to "Text"  
_Show thumbnail_ | 0 | columns.0.show_thumbnail | 0 - _(default)_ Disabled;  
1 - Enabled.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Display item value as_ is set to "Binary"  
_Aggregation function_ | 0 | columns.0.aggregate_function | 0 - _(default)_ not used;  
1 - min;  
2 - max;  
3 - avg;  
4 - count;  
5 - sum;  
6 - first;  
7 - last.  
_Time period_ | 1 | columns.0.time_period._reference | `DASHBOARD._timeperiod` \- set the [_Time period_ selector](/documentation/current/en/manual/web_interface/time_period_selector) as the data source;  
`ABCDE._timeperiod` \- set a [compatible widget](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#widget-compatibility) (with its `reference` parameter equal to `ABCDE`) as the data source.  
  
Default: `DASHBOARD._timeperiod`  
  
Alternatively, you can set the time period only in the _From_ and _To_ parameters.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Aggregation function_ is set to "min", "max", "avg", "count", "sum", "first", "last"  
| _From_ | 1 | columns.0.time_period.from | Valid time string in absolute (`YYYY-MM-DD hh:mm:ss`) or [relative](/documentation/current/en/manual/web_interface/time_period_selector) time syntax (`now`, `now/d`, `now/w-1w`, etc.).  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Time period_ is not set and _Aggregation function_ is set to "min", "max", "avg", "count", "sum", "first", "last"  
_To_ | 1 | columns.0.time_period.to | Valid time string in absolute (`YYYY-MM-DD hh:mm:ss`) or [relative](/documentation/current/en/manual/web_interface/time_period_selector) time syntax (`now`, `now/d`, `now/w-1w`, etc.).  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Time period_ is not set and _Aggregation function_ is set to "min", "max", "avg", "count", "sum", "first", "last"  
_History data_ | 0 | columns.0.history | 0 - _(default)_ Auto;  
1 - History;  
2 - Trends.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Display item value as_ is set to "Numeric"  
_Reference_ | 1 | reference | Any string value consisting of 5 characters (e.g., `ABCDE` or `JBPNL`). This value must be unique within the dashboard to which the widget belongs.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
  
##### Text

The following parameters are supported if _Data_ is set to "Text".

_Text_ | 1 | columns.0.text | Any string value, including macros.  
Supported macros: {HOST.*}, {INVENTORY.*}.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_ if _Data_ is set to "Text"  
---|---|---|---  
  
### Examples

The following examples aim to only describe the configuration of the dashboard widget field objects for the _Top hosts_ widget. For more information on configuring a dashboard, see [`dashboard.create`](/documentation/current/en/manual/api/reference/dashboard/create).

#### Configuring a _Top hosts_ widget

Configure a _Top hosts_ widget that displays top hosts by CPU utilization in host group "4". In addition, configure the following custom columns: "Host name", "CPU utilization in %", "1m avg", "5m avg", "15m avg", "Processes".

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
                                   "type": "tophosts",
                                   "name": "Top hosts",
                                   "x": 0,
                                   "y": 0,
                                   "width": 36,
                                   "height": 5,
                                   "view_mode": 0,
                                   "fields": [
                                       {
                                           "type": 2,
                                           "name": "groupids.0",
                                           "value": 4
                                       },
                                       {
                                           "type": 1,
                                           "name": "columns.0.name",
                                           "value": "Host"
                                       },
                                       {
                                           "type": 0,
                                           "name": "columns.0.data",
                                           "value": 2
                                       },
                                       {
                                           "type": 1,
                                           "name": "columns.0.base_color",
                                           "value": "FFFFFF"
                                       },
                                       {
                                           "type": 1,
                                           "name": "columns.1.name",
                                           "value": "CPU utilization in %"
                                       },
                                       {
                                           "type": 0,
                                           "name": "columns.1.data",
                                           "value": 1
                                       },
                                       {
                                           "type": 1,
                                           "name": "columns.1.base_color",
                                           "value": "4CAF50"
                                       },
                                       {
                                           "type": 1,
                                           "name": "columns.1.item",
                                           "value": "CPU utilization"
                                       },
                                       {
                                           "type": 0,
                                           "name": "columns.1.display",
                                           "value": 3
                                       },
                                       {
                                           "type": 1,
                                           "name": "columns.1.min",
                                           "value": "0"
                                       },
                                       {
                                           "type": 1,
                                           "name": "columns.1.max",
                                           "value": "100"
                                       },
                                       {
                                           "type": 1,
                                           "name": "columnsthresholds.1.color.0",
                                           "value": "FFFF00"
                                       },
                                       {
                                           "type": 1,
                                           "name": "columnsthresholds.1.threshold.0",
                                           "value": "50"
                                       },
                                       {
                                           "type": 1,
                                           "name": "columnsthresholds.1.color.1",
                                           "value": "FF8000"
                                       },
                                       {
                                           "type": 1,
                                           "name": "columnsthresholds.1.threshold.1",
                                           "value": "80"
                                       },
                                       {
                                           "type": 1,
                                           "name": "columnsthresholds.1.color.2",
                                           "value": "FF4000"
                                       },
                                       {
                                           "type": 1,
                                           "name": "columnsthresholds.1.threshold.2",
                                           "value": "90"
                                       },
                                       {
                                           "type": 1,
                                           "name": "columns.2.name",
                                           "value": "1m avg"
                                       },
                                       {
                                           "type": 0,
                                           "name": "columns.2.data",
                                           "value": 1
                                       },
                                       {
                                           "type": 1,
                                           "name": "columns.2.base_color",
                                           "value": "FFFFFF"
                                       },
                                       {
                                           "type": 1,
                                           "name": "columns.2.item",
                                           "value": "Load average (1m avg)"
                                       },
                                       {
                                           "type": 1,
                                           "name": "columns.3.name",
                                           "value": "5m avg"
                                       },
                                       {
                                           "type": 0,
                                           "name": "columns.3.data",
                                           "value": 1
                                       },
                                       {
                                           "type": 1,
                                           "name": "columns.3.base_color",
                                           "value": "FFFFFF"
                                       },
                                       {
                                           "type": 1,
                                           "name": "columns.3.item",
                                           "value": "Load average (5m avg)"
                                       },
                                       {
                                           "type": 1,
                                           "name": "columns.4.name",
                                           "value": "15m avg"
                                       },
                                       {
                                           "type": 0,
                                           "name": "columns.4.data",
                                           "value": 1
                                       },
                                       {
                                           "type": 1,
                                           "name": "columns.4.base_color",
                                           "value": "FFFFFF"
                                       },
                                       {
                                           "type": 1,
                                           "name": "columns.4.item",
                                           "value": "Load average (15m avg)"
                                       },
                                       {
                                           "type": 1,
                                           "name": "columns.5.name",
                                           "value": "Processes"
                                       },
                                       {
                                           "type": 0,
                                           "name": "columns.5.data",
                                           "value": 1
                                       },
                                       {
                                           "type": 1,
                                           "name": "columns.5.base_color",
                                           "value": "FFFFFF"
                                       },
                                       {
                                           "type": 1,
                                           "name": "columns.5.item",
                                           "value": "Number of processes"
                                       },
                                       {
                                           "type": 0,
                                           "name": "columns.5.decimal_places",
                                           "value": 0
                                       },
                                       {
                                           "type": 0,
                                           "name": "column",
                                           "value": 1
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