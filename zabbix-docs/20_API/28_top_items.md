---
title: Top items
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/dashboard/widget_fields/top_items
downloaded: 2025-11-14 10:41:08
---

# 28 Top items

### Description

These parameters and the possible property values for the respective dashboard widget field objects allow to configure the [_Top items_](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/top_items) widget in `dashboard.create` and `dashboard.update` methods.

Widget `fields` properties are not validated during the creation or update of a dashboard. This allows users to modify [built-in widgets](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets) and create [custom widgets](/documentation/current/en/devel/modules/tutorials/widget), but also introduces the risk of creating or updating widgets incorrectly. To ensure the successful creation or update of the _Top items_ widget, please refer to the parameter behavior outlined in the tables below.

### Parameters

The following parameters are supported for the _Top items_ widget.

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
| _Evaluation type_ | 0 | host_tags_evaltype | 0 - _(default)_ And/Or;  
2 - Or.  
  
This parameter is not supported if configuring the widget on a [template dashboard](/documentation/current/en/manual/api/reference/templatedashboard/object).  
_Tag name_ | 1 | host_tags.0.tag | Any string value.  
  
Note: The number in the property name references tag order in the tag evaluation list.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_ if configuring _Host tags_  
  
This parameter is not supported if configuring the widget on a [template dashboard](/documentation/current/en/manual/api/reference/templatedashboard/object).  
_Operator_ | 0 | host_tags.0.operator | 0 - Contains;  
1 - Equals;  
2 - Does not contain;  
3 - Does not equal;  
4 - Exists;  
5 - Does not exist.  
  
Note: The number in the property name references tag order in the tag evaluation list.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_ if configuring _Host tags_  
  
This parameter is not supported if configuring the widget on a [template dashboard](/documentation/current/en/manual/api/reference/templatedashboard/object).  
_Tag value_ | 1 | host_tags.0.value | Any string value.  
  
Note: The number in the property name references tag order in the tag evaluation list.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_ if configuring _Host tags_  
  
This parameter is not supported if configuring the widget on a [template dashboard](/documentation/current/en/manual/api/reference/templatedashboard/object).  
_Layout_ | 0 | layout | 0 - _(default)_ Horizontal;  
1 - Vertical.  
_Show problems_ | 0 | show_problems | 0 - All;  
1 - _(default)_ Unsuppressed;  
2 - None.  
_Items_ (see below)  
  
#### Advanced configuration

The following advanced configuration parameters are supported for the _Top items_ widget.

**_Host ordering_**  
---  
_Order by_ | 0 | host_ordering_order_by | 0 - _(default)_ Host name;  
3 - Item value.  
| _Item patterns_ | 1 | host_ordering_item.0 | [Item](/documentation/current/en/manual/api/reference/item/get) name or pattern (e.g., "*: Number of processed *values per second").  
  
Note: To configure multiple item patterns, create a dashboard widget field object for each item pattern with an incremented number in the property name.  
  
When configuring the widget on a [template dashboard](/documentation/current/en/manual/api/reference/templatedashboard/object), only the patterns for items configured on the template should be set.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_ if _Order by_ is set to "Item value"  
_Order_ | 0 | host_ordering_order | 2 - _(default)_ Top N;  
3 - Bottom N.  
_Limit_ | 0 | host_ordering_limit | Possible values range from 1-100.  
  
Default: 10.  
**_Item ordering_**  
_Order by_ | 0 | item_ordering_order_by | 1 - Host;  
2 - Item name;  
3 - _(default)_ Item value.  
| _Host patterns_ | 1 | item_ordering_host.0 | [Host](/documentation/current/en/manual/api/reference/host/get) name or pattern.  
  
Note: To configure multiple host patterns, create a dashboard widget field object for each host pattern with an incremented number in the property name.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_ if _Order by_ is set to "Host"  
_Order_ | 0 | item_ordering_order | 2 - _(default)_ Top N;  
3 - Bottom N.  
_Limit_ | 0 | item_ordering_limit | Possible values range from 1-100.  
  
Default: 10.  
  
### Columns

The first number in the property name (e.g. columns.0.items.0, columns.0.item_tags_evaltype) represents the particular column, while the second number, if present, represents the configured entity (e.g. item pattern, tag).

_Item patterns_ | 1 | columns.0.items.0 | [Item](/documentation/current/en/manual/api/reference/item/get) name or pattern (e.g., "*: Number of processed *values per second").  
  
Note: To configure multiple item patterns, create a dashboard widget field object for each item pattern with an incremented second number in the property name.  
  
When configuring the widget on a [template dashboard](/documentation/current/en/manual/api/reference/templatedashboard/object), only the patterns for items configured on the template should be set.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
---|---|---|---  
_Item tags_  
| _Evaluation type_ | 0 | columns.0.item_tags_evaltype | 0 - _(default)_ And/Or;  
2 - Or.  
_Tag name_ | 1 | columns.0.item_tags.0.tag | Any string value.  
  
Note: The second number in the property name references tag order in the tag evaluation list.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_ if configuring _Item tags_  
_Operator_ | 0 | columns.0.item_tags.0.operator | 0 - Contains;  
1 - Equals;  
2 - Does not contain;  
3 - Does not equal;  
4 - Exists;  
5 - Does not exist.  
  
Note: The second number in the property name references tag order in the tag evaluation list.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_ if configuring _Item tags_  
_Tag value_ | 1 | columns.0.item_tags.0.value | Any string value.  
  
Note: The second number in the property name references tag order in the tag evaluation list.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_ if configuring _Item tags_  
_Base color_ | 1 | columns.0.base_color | Hexadecimal color code (e.g. `FF0000`).  
_Display value as_ | 0 | columns.0.display_value_as | 1 - _(default)_ Numeric;  
2 - Text.  
_Display_ | 0 | columns.0.display | 1 - _(default)_ As is;  
2 - Bar;  
3 - Indicators;  
6 - Sparkline.  
_Min_ | 1 | columns.0.min | Any numeric value. [Suffixes](/documentation/current/en/manual/appendix/suffixes) (e.g. "1d", "2w", "4K", "8G") are supported.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Display value as_ is set to "Numeric" and _Display_ is set to "Bar" or "Indicators"  
_Max_ | 1 | columns.0.max | Any numeric value. [Suffixes](/documentation/current/en/manual/appendix/suffixes) (e.g. "1d", "2w", "4K", "8G") are supported.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Display value as_ is set to "Numeric" and _Display_ is set to "Bar" or "Indicators"  
_Sparkline_  
| _Width_ | 0 | columns.0.sparkline.width | Possible values range from 0-10.  
  
Default: 1.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Display_ is set to "Sparkline"  
_Fill_ | 0 | columns.0.sparkline.fill | Possible values range from 0-10.  
  
Default: 3.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Display_ is set to "Sparkline"  
_Color_ | 1 | columns.0.sparkline.color | Hexadecimal color code (e.g. `FF0000`).  
  
Default: `42A5F5`.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Display_ is set to "Sparkline"  
_Time period_ | 1 | columns.0.sparkline.time_period._reference | `DASHBOARD._timeperiod` \- set the [_Time period_ selector](/documentation/current/en/manual/web_interface/time_period_selector) as the data source;  
`ABCDE._timeperiod` \- set a [compatible widget](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#widget-compatibility) (with its `reference` parameter equal to `ABCDE`) as the data source.  
  
Default: `DASHBOARD._timeperiod`  
  
Alternatively, you can set the time period only in the _From_ and _To_ parameters.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Display_ is set to "Sparkline"  
_From_ | 1 | columns.0.sparkline.time_period.from | Valid time string in absolute (`YYYY-MM-DD hh:mm:ss`) or [relative](/documentation/current/en/manual/web_interface/time_period_selector) time syntax (`now`, `now/d`, `now/w-1w`, etc.).  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Display_ is set to "Sparkline"  
_To_ | 1 | columns.0.sparkline.time_period.to | Valid time string in absolute (`YYYY-MM-DD hh:mm:ss`) or [relative](/documentation/current/en/manual/web_interface/time_period_selector) time syntax (`now`, `now/d`, `now/w-1w`, etc.).  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Display_ is set to "Sparkline"  
_History data_ | 0 | columns.0.sparkline.history | 0 - _(default)_ Auto;  
1 - History;  
2 - Trends.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Display_ is set to "Sparkline"  
_Thresholds_  
| _Color_ | 1 | columns.0.thresholds.0.color | Hexadecimal color code (e.g. `FF0000`).  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Display value as_ is set to "Numeric"  
_Threshold_ | 1 | columns.0.thresholds.0.threshold | Any numeric value. [Suffixes](/documentation/current/en/manual/appendix/suffixes) (e.g. "1d", "2w", "4K", "8G") are supported.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Display value as_ is set to "Numeric"  
_Highlights_  
| _Highlight_ | 1 | columns.0.highlights.0.color | Hexadecimal color code (e.g. `FF0000`).  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Display value as_ is set to "Text"  
_Threshold_ | 1 | columns.0.highlights.0.pattern | Any regular expression.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Display value as_ is set to "Text"  
_Decimal places_ | 0 | columns.0.decimal_places | Possible values range from 0-10.  
  
Default: 2.  
**_Advanced configuration_**  
_Aggregation function_ | 0 | columns.0.aggregate_function | If _Display value as_ is set to "Numeric":  
0 - _(default)_ not used;  
1 - min;  
2 - max;  
3 - avg;  
4 - count;  
5 - sum;  
6 - first;  
7 - last.  
  
If _Display value as_ is set to "Text":  
0 - _(default)_ not used;  
4 - count;  
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
\- _supported_ if _Display value as_ is set to "Numeric"  
  
### Examples

The following examples aim to only describe the configuration of the dashboard widget field objects for the _Top items_ widget. For more information on configuring a dashboard, see [`dashboard.create`](/documentation/current/en/manual/api/reference/dashboard/create).

#### Configuring a _Top items_ widget

Configure a _Top items_ widget that displays data for host "10084" and only for items for which the tag with the name "component" contains the value "cpu". In addition, display the data with hosts located at the top and use a colored gauge bar for cell representation.

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
                                   "type": "topitems",
                                   "name": "Top items",
                                   "x": 0,
                                   "y": 0,
                                   "width": 36,
                                   "height": 5,
                                   "view_mode": 0,
                                   "fields": [
                                       {
                                           "type": 3,
                                           "name": "hostids.0",
                                           "value": 10084
                                       },
                                       {
                                           "type": 1,
                                           "name": "columns.0.items.0",
                                           "value": "*"
                                       },
                                       {
                                           "type": 1,
                                           "name": "columns.0.item_tags.0.tag",
                                           "value": "component"
                                       },
                                       {
                                           "type": 0,
                                           "name": "columns.0.item_tags.0.operator",
                                           "value": 0
                                       },
                                       {
                                           "type": 1,
                                           "name": "columns.0.item_tags.0.value",
                                           "value": "cpu"
                                       },
                                       {
                                           "type": 0,
                                           "name": "columns.0.display",
                                           "value": 2
                                       },
                                       {
                                           "type": 0,
                                           "name": "layout",
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