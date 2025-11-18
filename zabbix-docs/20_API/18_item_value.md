---
title: Item value
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/dashboard/widget_fields/item_value
downloaded: 2025-11-14 10:40:58
---

# 18 Item value

### Description

These parameters and the possible property values for the respective dashboard widget field objects allow to configure the [_Item value_](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/item_value) widget in `dashboard.create` and `dashboard.update` methods.

Widget `fields` properties are not validated during the creation or update of a dashboard. This allows users to modify [built-in widgets](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets) and create [custom widgets](/documentation/current/en/devel/modules/tutorials/widget), but also introduces the risk of creating or updating widgets incorrectly. To ensure the successful creation or update of the _Item value_ widget, please refer to the parameter behavior outlined in the tables below.

### Parameters

The following parameters are supported for the _Item value_ widget.

_Refresh interval_ | 0 | rf_rate | 0 - No refresh;  
10 - 10 seconds;  
30 - 30 seconds;  
60 - _(default)_ 1 minute;  
120 - 2 minutes;  
600 - 10 minutes;  
900 - 15 minutes.  
---|---|---|---  
_Item_ | 4 | itemid.0 | [Item](/documentation/current/en/manual/api/reference/item/get) ID.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_ if _Item (Widget)_ is not set  
| _Item (Widget)_ | 1 | itemid._reference | Instead of [Item](/documentation/current/en/manual/api/reference/item/get) ID:  
`ABCDE._itemid` \- set a [compatible widget](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#widget-compatibility) (with its _Reference_ parameter set to "`ABCDE`") as the data source for items.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_ if _Item_ is not set  
_Show_ | 0 | show.0 | 1 - Description;  
2 - Value;  
3 - Time;  
4 - Change indicator;  
5 - Sparkline.  
  
Default: 1, 2, 3, 4.  
  
Note: To configure multiple values, create a dashboard widget field object for each value with an incremented number in the property name.  
_Override host_ | 1 | override_hostid._reference | `ABCDE._hostid` \- set a [compatible widget](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#widget-compatibility) (with its _Reference_ parameter set to "`ABCDE`") as the data source for hosts;  
`DASHBOARD._hostid` \- set the dashboard [_Host_ selector](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#override-host) as the data source for hosts.  
  
This parameter is not supported if configuring the widget on a [template dashboard](/documentation/current/en/manual/api/reference/templatedashboard/object).  
  
#### Advanced configuration

The following advanced configuration parameters are supported for the _Item value_ widget.

The number in the _Thresholds_ property name (e.g. thresholds.0.color) references the threshold place in a list, sorted in ascending order. However, if thresholds are configured in a different order, the values will be sorted in ascending order after updating widget configuration in Zabbix frontend (e.g. `"thresholds.0.threshold":"5"` → `"thresholds.0.threshold":"1"`; `"thresholds.1.threshold":"1"` → `"thresholds.1.threshold": "5"`).

_Background color_ | 1 | bg_color | Hexadecimal color code (e.g. `FF0000`).  
  
Default: `""` (empty).  
---|---|---|---  
_Thresholds_  
| _Color_ | 1 | thresholds.0.color | Hexadecimal color code (e.g. `FF0000`).  
_Threshold_ | 1 | thresholds.0.threshold | Any string value.  
_Aggregation function_ | 0 | aggregate_function | 0 - _(default)_ not used;  
1 - min;  
2 - max;  
3 - avg;  
4 - count;  
5 - sum;  
6 - first;  
7 - last.  
_Time period_ | 1 | time_period._reference | `DASHBOARD._timeperiod` \- set the [_Time period_ selector](/documentation/current/en/manual/web_interface/time_period_selector) as the data source;  
`ABCDE._timeperiod` \- set a [compatible widget](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#widget-compatibility) (with its `reference` parameter equal to `ABCDE`) as the data source.  
  
Default: `DASHBOARD._timeperiod`  
  
Alternatively, you can set the time period only in the _From_ and _To_ parameters.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Aggregation function_ is set to "min", "max", "avg", "count", "sum", "first", "last"  
| _From_ | 1 | time_period.from | Valid time string in absolute (`YYYY-MM-DD hh:mm:ss`) or [relative](/documentation/current/en/manual/web_interface/time_period_selector) time syntax (`now`, `now/d`, `now/w-1w`, etc.).  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Time period_ is not set and _Aggregation function_ is set to "min", "max", "avg", "count", "sum", "first", "last"  
_To_ | 1 | time_period.to | Valid time string in absolute (`YYYY-MM-DD hh:mm:ss`) or [relative](/documentation/current/en/manual/web_interface/time_period_selector) time syntax (`now`, `now/d`, `now/w-1w`, etc.).  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Time period_ is not set and _Aggregation function_ is set to "min", "max", "avg", "count", "sum", "first", "last"  
_History data_ | 0 | history | 0 - _(default)_ Auto;  
1 - History;  
2 - Trends.  
  
##### Description

The following advanced configuration parameters are supported if _Show_ is set to "Description".

_Description_ | 1 | description | Any string value, including macros.  
Supported macros: {HOST.*}, {ITEM.*}, {INVENTORY.*}, User macros.  
  
Default: {ITEM.NAME}.  
---|---|---|---  
_Horizontal position_ | 0 | desc_h_pos | 0 - Left;  
1 - _(default)_ Center;  
2 - Right.  
  
Two or more elements (Description, Value, Time) cannot share the same _Horizontal position_ and _Vertical position_.  
_Vertical position_ | 0 | desc_v_pos | 0 - Top;  
1 - Middle;  
2 - _(default)_ Bottom.  
  
Two or more elements (Description, Value, Time) cannot share the same _Horizontal position_ and _Vertical position_.  
_Size_ | 0 | desc_size | Possible values range from 1-100.  
  
Default: 15.  
_Bold_ | 0 | desc_bold | 0 - _(default)_ Disabled;  
1 - Enabled.  
_Color_ | 1 | desc_color | Hexadecimal color code (e.g. `FF0000`).  
  
Default: `""` (empty).  
  
##### Value

The following advanced configuration parameters are supported if _Show_ is set to "Value".

_Decimal places_  
---  
| _Decimal places_ | 0 | decimal_places | Possible values range from 1-10.  
  
Default: 2.  
_Size_ | 0 | decimal_size | Possible values range from 1-100.  
  
Default: 35.  
_Position_  
| _Horizontal position_ | 0 | value_h_pos | 0 - Left;  
1 - _(default)_ Center;  
2 - Right.  
  
Two or more elements (Description, Value, Time) cannot share the same _Horizontal position_ and _Vertical position_.  
_Vertical position_ | 0 | value_v_pos | 0 - Top;  
1 - _(default)_ Middle;  
2 - Bottom.  
  
Two or more elements (Description, Value, Time) cannot share the same _Horizontal position_ and _Vertical position_.  
_Size_ | 0 | value_size | Possible values range from 1-100.  
  
Default: 45.  
_Bold_ | 0 | value_bold | 0 - Disabled;  
1 - _(default)_ Enabled.  
_Color_ | 1 | value_color | Hexadecimal color code (e.g. `FF0000`).  
  
Default: `""` (empty).  
_Units_  
| _Units_ (checkbox) | 0 | units_show | 0 - Disabled;  
1 - _(default)_ Enabled.  
_Units_ (value) | 1 | units | Any string value.  
_Position_ | 0 | units_pos | 0 - Before value;  
1 - Above value;  
2 - _(default)_ After value;  
3 - Below value.  
_Size_ | 0 | units_size | Possible values range from 1-100.  
  
Default: 35.  
_Bold_ | 0 | units_bold | 0 - Disabled;  
1 - _(default)_ Enabled.  
_Color_ | 1 | units_color | Hexadecimal color code (e.g. `FF0000`).  
  
Default: `""` (empty).  
  
##### Time

The following advanced configuration parameters are supported if _Show_ is set to "Time".

_Horizontal position_ | 0 | time_h_pos | 0 - Left;  
1 - _(default)_ Center;  
2 - Right.  
  
Two or more elements (Description, Value, Time) cannot share the same _Horizontal position_ and _Vertical position_.  
---|---|---|---  
_Vertical position_ | 0 | time_v_pos | 0 - _(default)_ Top;  
1 - Middle;  
2 - Bottom.  
  
Two or more elements (Description, Value, Time) cannot share the same _Horizontal position_ and _Vertical position_.  
_Size_ | 0 | time_size | Possible values range from 1-100.  
  
Default: 15.  
_Bold_ | 0 | time_bold | 0 - _(default)_ Disabled;  
1 - Enabled.  
_Color_ | 1 | time_color | Hexadecimal color code (e.g. `FF0000`).  
  
Default: `""` (empty).  
  
##### Change indicator

The following advanced configuration parameters are supported if _Show_ is set to "Change indicator".

_Change indicator ↑ color_ | 1 | up_color | Hexadecimal color code (e.g. `FF0000`).  
  
Default: `""` (empty).  
---|---|---|---  
_Change indicator ↓ color_ | 1 | down_color | Hexadecimal color code (e.g. `FF0000`).  
  
Default: `""` (empty).  
_Change indicator ↕ color_ | 1 | updown_color | Hexadecimal color code (e.g. `FF0000`).  
  
Default: `""` (empty).  
  
##### Sparkline

The following advanced configuration parameters are supported if _Show_ is set to "Sparkline".

_Width_ | 0 | sparkline.width | Possible values range from 0-10.  
  
Default: 1.  
---|---|---|---  
_Fill_ | 0 | sparkline.fill | Possible values range from 0-10.  
  
Default: 3.  
_Color_ | 1 | sparkline.color | Hexadecimal color code (e.g. `FF0000`).  
  
Default: `42A5F5`.  
_Time period_ | 1 | sparkline.time_period._reference | `DASHBOARD._timeperiod` \- set the [_Time period_ selector](/documentation/current/en/manual/web_interface/time_period_selector) as the data source;  
`ABCDE._timeperiod` \- set a [compatible widget](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#widget-compatibility) (with its `reference` parameter equal to `ABCDE`) as the data source.  
  
Default: `DASHBOARD._timeperiod`  
  
Alternatively, you can set the time period only in the _From_ and _To_ parameters.  
| _From_ | 1 | sparkline.time_period.from | Valid time string in absolute (`YYYY-MM-DD hh:mm:ss`) or [relative](/documentation/current/en/manual/web_interface/time_period_selector) time syntax (`now`, `now/d`, `now/w-1w`, etc.).  
_To_ | 1 | sparkline.time_period.to | Valid time string in absolute (`YYYY-MM-DD hh:mm:ss`) or [relative](/documentation/current/en/manual/web_interface/time_period_selector) time syntax (`now`, `now/d`, `now/w-1w`, etc.).  
_History data_ | 0 | sparkline.history | 0 - _(default)_ Auto;  
1 - History;  
2 - Trends.  
  
### Examples

The following examples aim to only describe the configuration of the dashboard widget field objects for the _Item value_ widget. For more information on configuring a dashboard, see [`dashboard.create`](/documentation/current/en/manual/api/reference/dashboard/create).

#### Configuring an _Item value_ widget

Configure an _Item value_ widget that displays the item value for the item "42266" (Zabbix agent availability). In addition, visually fine-tune the widget with multiple advanced options, including a dynamic background color that changes based on the availability status of Zabbix agent.

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
                                   "type": "item",
                                   "name": "Item value",
                                   "x": 0,
                                   "y": 0,
                                   "width": 12,
                                   "height": 3,
                                   "view_mode": 0,
                                   "fields": [
                                       {
                                           "type": 4,
                                           "name": "itemid.0",
                                           "value": 42266
                                       },
                                       {
                                           "type": 0,
                                           "name": "show.0",
                                           "value": 1
                                       },
                                       {
                                           "type": 0,
                                           "name": "show.1",
                                           "value": 2
                                       },
                                       {
                                           "type": 0,
                                           "name": "show.2",
                                           "value": 3
                                       },
                                       {
                                           "type": 1,
                                           "name": "description",
                                           "value": "Agent status"
                                       },
                                       {
                                           "type": 0,
                                           "name": "desc_h_pos",
                                           "value": 0
                                       },
                                       {
                                           "type": 0,
                                           "name": "desc_v_pos",
                                           "value": 0
                                       },
                                       {
                                           "type": 0,
                                           "name": "desc_bold",
                                           "value": 1
                                       },
                                       {
                                           "type": 1,
                                           "name": "desc_color",
                                           "value": "F06291"
                                       },
                                       {
                                           "type": 0,
                                           "name": "value_h_pos",
                                           "value": 0
                                       },
                                       {
                                           "type": 0,
                                           "name": "value_size",
                                           "value": 25
                                       },
                                       {
                                           "type": 1,
                                           "name": "value_color",
                                           "value": "FFFF00"
                                       },
                                       {
                                           "type": 0,
                                           "name": "units_show",
                                           "value": 0
                                       },
                                       {
                                           "type": 0,
                                           "name": "time_h_pos",
                                           "value": 2
                                       },
                                       {
                                           "type": 0,
                                           "name": "time_v_pos",
                                           "value": 2
                                       },
                                       {
                                           "type": 0,
                                           "name": "time_size",
                                           "value": 10
                                       },
                                       {
                                           "type": 0,
                                           "name": "time_bold",
                                           "value": 1
                                       },
                                       {
                                           "type": 1,
                                           "name": "time_color",
                                           "value": "9FA8DA"
                                       },
                                       {
                                           "type": 1,
                                           "name": "thresholds.0.color",
                                           "value": "E1E1E1"
                                       },
                                       {
                                           "type": 1,
                                           "name": "thresholds.0.threshold",
                                           "value": "0"
                                       },
                                       {
                                           "type": 1,
                                           "name": "thresholds.1.color",
                                           "value": "D1C4E9"
                                       },
                                       {
                                           "type": 1,
                                           "name": "thresholds.1.threshold",
                                           "value": "1"
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