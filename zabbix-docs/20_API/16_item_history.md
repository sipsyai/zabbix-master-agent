---
title: Item history
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/dashboard/widget_fields/item_history
downloaded: 2025-11-14 10:40:56
---

# 16 Item history

### Description

These parameters and the possible property values for the respective dashboard widget field objects allow to configure the [_Item history_](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/item_history) widget in `dashboard.create` and `dashboard.update` methods.

Widget `fields` properties are not validated during the creation or update of a dashboard. This allows users to modify [built-in widgets](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets) and create [custom widgets](/documentation/current/en/devel/modules/tutorials/widget), but also introduces the risk of creating or updating widgets incorrectly. To ensure the successful creation or update of the _Item history_ widget, please refer to the parameter behavior outlined in the tables below.

### Parameters

The following parameters are supported for the _Item history_ widget.

_Refresh interval_ | 0 | rf_rate | 0 - No refresh;  
10 - 10 seconds;  
30 - 30 seconds;  
60 - _(default)_ 1 minute;  
120 - 2 minutes;  
600 - 10 minutes;  
900 - 15 minutes.  
---|---|---|---  
_Layout_ | 0 | layout | 0 - _(default)_ Horizontal;  
1 - Vertical.  
_Columns_ (see below)  
_Show lines_ | 0 | show_lines | Possible values range from 1-100.  
  
Default: 25.  
_Override host_ | 1 | override_hostid._reference | `ABCDE._hostid` \- set a [compatible widget](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#widget-compatibility) (with its _Reference_ parameter set to "`ABCDE`") as the data source for hosts;  
`DASHBOARD._hostid` \- set the dashboard [_Host_ selector](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#override-host) as the data source for hosts.  
  
This parameter is not supported if configuring the widget on a [template dashboard](/documentation/current/en/manual/api/reference/templatedashboard/object).  
_Advanced configuration_ (see below)  
_Reference_ | 1 | reference | Any string value consisting of 5 characters (e.g., `ABCDE` or `JBPNL`). This value must be unique within the dashboard to which the widget belongs.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
  
#### Columns

Columns have common parameters and additional parameters depending on the configuration of the _Item_ parameter.

For all parameters related to columns, the number in the property name (e.g. columns.0.name) references a column for which the parameter is configured.

The following parameters are supported for all columns.

_Name_ | 1 | columns.0.name | Any string value.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
---|---|---|---  
_Item_ | 4 | columns.0.itemid | [Item](/documentation/current/en/manual/api/reference/item/get) ID.  
  
When configuring the widget on a [template dashboard](/documentation/current/en/manual/api/reference/templatedashboard/object), only items configured on the template should be set.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
_Base color_ | 1 | columns.0.base_color | Hexadecimal color code (e.g. `FF0000`).  
  
Default: `""` (empty).  
  
The following column parameters are supported if the configured _Item_ is a numeric type item.

_Display_ | 0 | columns.0.display | 1 - _(default)_ As is;  
2 - Bar;  
3 - Indicators.  
---|---|---|---  
_Min_ | 1 | columns.0.min | Any numeric value.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Display_ is set to "Bar" or "Indicators"  
_Max_ | 1 | columns.0.max | Any numeric value.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Display_ is set to "Bar" or "Indicators"  
_Thresholds_  
| _Color_ | 1 | columns.0.thresholds.0.color | Hexadecimal color code (e.g. `FF0000`).  
_Threshold_ | 1 | columns.0.thresholds.0.threshold | Any numeric value. [Suffixes](/documentation/current/en/manual/appendix/suffixes) (e.g. "1d", "2w", "4K", "8G") are supported.  
_History data_ | 0 | columns.0.history | 0 - _(default)_ Auto;  
1 - History;  
2 - Trends.  
  
The following column parameters are supported if the configured _Item_ is a character, text, or log type item.

_Highlights_  
---  
| _Highlight_ | 1 | columns.0.highlights.0.color | Hexadecimal color code (e.g. `FF0000`).  
_Threshold_ | 1 | columns.0.highlights.0.pattern | Any regular expression.  
_Display_ | 0 | columns.0.display | 1 - _(default)_ As is;  
4 - HTML;  
5 - Single line.  
| _Single line_ | 0 | columns.0.max_length | Possible values range from 1-500.  
  
Default: 100.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Display_ is set to "Single line"  
_Use monospace font_ | 0 | columns.0.monospace_font | 0 - _(default)_ Use default font;  
1 - Use monospace font.  
_Display local time_ | 0 | columns.0.local_time | 0 - _(default)_ Display timestamp;  
1 - Display local time.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Item_ is set to log type item, and _Show timestamp_ is set to "Enabled"  
  
The following column parameters are supported if the configured _Item_ is a binary type item.

_Show thumbnail_ | 1 | columns.0.show_thumbnail | 0 - _(default)_ Disabled;  
1 - Enabled.  
---|---|---|---  
  
#### Advanced configuration

The following advanced configuration parameters are supported for the _Item history_ widget.

_New values_ | 0 | sortorder | 0 - _(default)_ Top;  
1 - Bottom.  
---|---|---|---  
_Show timestamp_ | 0 | show_timestamp | 0 - _(default)_ Disabled;  
1 - Enabled.  
_Show column header_ | 0 | show_column_header | 0 - Off;  
1 - Horizontal;  
2 - _(default)_ Vertical.  
_Time period_ | 1 | time_period._reference | `DASHBOARD._timeperiod` \- set the [_Time period_ selector](/documentation/current/en/manual/web_interface/time_period_selector) as the data source;  
`ABCDE._timeperiod` \- set a [compatible widget](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#widget-compatibility) (with its _Reference_ parameter set to "`ABCDE`") as the data source.  
  
Default: `DASHBOARD._timeperiod`  
  
Alternatively, you can set the time period only in the _From_ and _To_ parameters.  
| _From_ | 1 | time_period.from | Valid time string in absolute (`YYYY-MM-DD hh:mm:ss`) or [relative](/documentation/current/en/manual/web_interface/time_period_selector) time syntax (`now`, `now/d`, `now/w-1w`, etc.).  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Time period_ is not set  
_To_ | 1 | time_period.to | Valid time string in absolute (`YYYY-MM-DD hh:mm:ss`) or [relative](/documentation/current/en/manual/web_interface/time_period_selector) time syntax (`now`, `now/d`, `now/w-1w`, etc.).  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Time period_ is not set  
  
### Examples

The following examples aim to only describe the configuration of the dashboard widget field objects for the _Item history_ widget. For more information on configuring a dashboard, see [`dashboard.create`](/documentation/current/en/manual/api/reference/dashboard/create).

#### Configuring an _Item history_ widget

Configure an _Item history_ widget that displays latest data for two numeric items "42269" and "42270". In addition, configure the item columns to be displayed vertically, with column names displayed horizontally; limit the display to 15 lines of data and include a separate timestamp column.

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
                                   "type": "itemhistory",
                                   "name": "Item history",
                                   "x": "0",
                                   "y": "0",
                                   "width": "18",
                                   "height": "6",
                                   "view_mode": "0",
                                   "fields": [
                                       {
                                           "type": "0",
                                           "name": "layout",
                                           "value": "1"
                                       },
                                       {
                                           "type": "1",
                                           "name": "columns.0.name",
                                           "value": "CPU utilization"
                                       },
                                       {
                                           "type": "4",
                                           "name": "columns.0.itemid",
                                           "value": "42269"
                                       },
                                       {
                                           "type": "1",
                                           "name": "columns.1.name",
                                           "value": "Memory utilization"
                                       },
                                       {
                                           "type": "4",
                                           "name": "columns.1.itemid",
                                           "value": "42270"
                                       },
                                       {
                                           "type": "0",
                                           "name": "show_lines",
                                           "value": "15"
                                       },
                                       {
                                           "type": "0",
                                           "name": "show_timestamp",
                                           "value": "1"
                                       },
                                       {
                                           "type": "0",
                                           "name": "show_column_header",
                                           "value": "1"
                                       },
                                       {
                                           "type": "1",
                                           "name": "reference",
                                           "value": "KIVKD"
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