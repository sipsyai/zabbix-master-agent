---
title: Gauge
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/dashboard/widget_fields/gauge
downloaded: 2025-11-14 10:40:45
---

# 6 Gauge

### Description

These parameters and the possible property values for the respective dashboard widget field objects allow to configure the [_Gauge_](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/gauge) widget in `dashboard.create` and `dashboard.update` methods.

Widget `fields` properties are not validated during the creation or update of a dashboard. This allows users to modify [built-in widgets](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets) and create [custom widgets](/documentation/current/en/devel/modules/tutorials/widget), but also introduces the risk of creating or updating widgets incorrectly. To ensure the successful creation or update of the _Gauge_ widget, please refer to the parameter behavior outlined in the tables below.

### Parameters

The following parameters are supported for the _Gauge_ widget.

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
_Min_ | 1 | min | Any numeric value. [Suffixes](/documentation/current/en/manual/appendix/suffixes) (e.g. "1d", "2w", "4K", "8G") are supported.  
  
Default: "0".  
_Max_ | 1 | max | Any numeric value. [Suffixes](/documentation/current/en/manual/appendix/suffixes) (e.g. "1d", "2w", "4K", "8G") are supported.  
  
Default: "100".  
_Value arc_ | 1 | value_arc_color | Hexadecimal color code (e.g. `FF0000`).  
  
Default: `""` (empty).  
_Arc background_ | 1 | empty_color | Hexadecimal color code (e.g. `FF0000`).  
  
Default: `""` (empty).  
_Background_ | 1 | bg_color | Hexadecimal color code (e.g. `FF0000`).  
  
Default: `""` (empty).  
_Show_ | 0 | show.0 | 1 - Description;  
2 - Value;  
3 - Needle;  
4 - Scale;  
5 - Value arc.  
  
Note: To configure multiple values, create a dashboard widget field object for each value with an incremented number in the property name.  
  
Default: 1, 2, 4, 5.  
  
Values "Needle" and "Scale" are not supported if both:  
\- no dashboard widget field object for _Show_ with the value "Value arc" is set;  
\- _Show arc_ advanced configuration parameter is set to "Disabled".  
  
Advanced configuration parameters for _Show_ options are not supported if no dashboard widget field objects with the respective values are set.  
_Override host_ | 1 | override_hostid._reference | `ABCDE._hostid` \- set a [compatible widget](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#widget-compatibility) (with its _Reference_ parameter set to "`ABCDE`") as the data source for hosts;  
`DASHBOARD._hostid` \- set the dashboard [_Host_ selector](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#override-host) as the data source for hosts.  
  
This parameter is not supported if configuring the widget on a [template dashboard](/documentation/current/en/manual/api/reference/templatedashboard/object).  
  
#### Advanced configuration

The following advanced configuration parameters are supported for the _Gauge_ widget.

The number in the _Thresholds_ property name (e.g. thresholds.0.color) references the threshold place in a list, sorted in ascending order. However, if thresholds are configured in a different order, the values will be sorted in ascending order after updating widget configuration in Zabbix frontend (e.g. `"thresholds.0.threshold":"5"` → `"thresholds.0.threshold":"1"`; `"thresholds.1.threshold":"1"` → `"thresholds.1.threshold": "5"`).

_Angle_ | 0 | angle | Possible values: 180 _(default)_ or 270.  
---|---|---|---  
**_Description_**  
_Description_ | 1 | description | Any string value, including macros.  
Supported macros: {HOST.*}, {ITEM.*}, {INVENTORY.*}, user macros.  
  
Default: {ITEM.NAME}.  
_Size_ | 0 | desc_size | Possible values range from 1-100.  
  
Default: 15.  
_Vertical position_ | 0 | desc_v_pos | 0 - Top;  
1 - _(default)_ Bottom.  
_Bold_ | 0 | desc_bold | 0 - _(default)_ Disabled;  
1 - Enabled.  
_Color_ | 1 | desc_color | Hexadecimal color code (e.g. `FF0000`).  
  
Default: `""` (empty).  
**_Value_**  
_Decimal places_ | 0 | decimal_places | Possible values range from 1-10.  
  
Default: 2.  
_Size_ | 0 | value_size | Possible values range from 1-100.  
  
Default: 25.  
_Bold_ | 0 | value_bold | 0 - _(default)_ Disabled;  
1 - Enabled.  
_Color_ | 1 | value_color | Hexadecimal color code (e.g. `FF0000`).  
  
Default: `""` (empty).  
**_Units_**  
_Units_ (checkbox) | 0 | units_show | 0 - Disabled;  
1 - _(default)_ Enabled.  
_Units_ (value) | 1 | units | Any string value.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Units_ (checkbox) is set to "Enabled"  
_Size_ | 0 | units_size | Possible values range from 1-100.  
  
Default: 25.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Units_ (checkbox) is set to "Enabled"  
_Bold_ | 0 | units_bold | 0 - _(default)_ Disabled;  
1 - Enabled.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Units_ (checkbox) is set to "Enabled"  
_Position_ | 0 | units_pos | 0 - Before value;  
1 - Above value;  
2 - _(default)_ After value;  
3 - Below value.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Units_ (checkbox) is set to "Enabled"  
  
This parameter is ignored if set to one of the following [time-related units](/documentation/current/en/manual/config/items/item#configuration): unixtime, uptime, s.  
_Color_ | 1 | units_color | Hexadecimal color code (e.g. `FF0000`).  
  
Default: `""` (empty).  
**_Value arc_**  
_Arc size_ | 0 | value_arc_size | Possible values range from 1-100.  
  
Default: 20.  
**_Needle_**  
_Color_ | 1 | needle_color | Hexadecimal color code (e.g. `FF0000`).  
  
Default: `""` (empty).  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if a dashboard widget field object for _Show_ with the value "Value arc" is set, or _Show arc_ is set to "Enabled"  
**_Scale_**  
_Show units_ | 0 | scale_show_units | 0 - Disabled;  
1 - _(default)_ Enabled.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Units_ (checkbox) is set to "Enabled" and either a dashboard widget field object for _Show_ with the value "Value arc" is set, or _Show arc_ is set to "Enabled"  
_Size_ | 0 | scale_size | Possible values range from 1-100.  
  
Default: 15.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if a dashboard widget field object for _Show_ with the value "Value arc" is set, or _Show arc_ is set to "Enabled"  
_Decimal places_ | 0 | scale_decimal_places | Possible values range from 1-10.  
  
Default: 0.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if a dashboard widget field object for _Show_ with the value "Value arc" is set, or _Show arc_ is set to "Enabled"  
**_Thresholds_**  
_Color_ | 1 | thresholds.0.color | Hexadecimal color code (e.g. `FF0000`).  
_Threshold_ | 1 | thresholds.0.threshold | Any numeric value. [Suffixes](/documentation/current/en/manual/appendix/suffixes) (e.g. "1d", "2w", "4K", "8G") are supported.  
_Show labels_ | 0 | th_show_labels | 0 - _(default)_ Disabled;  
1 - Enabled.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Thresholds_ are set and either a dashboard widget field object for _Show_ with the value "Value arc" is set or _Show arc_ is set to "Enabled"  
_Show arc_ | 0 | th_show_arc | 0 - _(default)_ Disabled;  
1 - Enabled.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Thresholds_ are set  
_Arc size_ | 0 | th_arc_size | Possible values range from 1-100.  
  
Default: 5.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Show arc_ is set to "Enabled"  
  
### Examples

The following examples aim to only describe the configuration of the dashboard widget field objects for the _Gauge_ widget. For more information on configuring a dashboard, see [`dashboard.create`](/documentation/current/en/manual/api/reference/dashboard/create).

#### Configuring a _Gauge_ widget

Configure a _Gauge_ widget that displays the item value for the item "44474" (Interface enp0s3: Bits sent). In addition, visually fine-tune the widget with multiple advanced options, including thresholds.

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
                                   "type": "gauge",
                                   "name": "Gauge",
                                   "x": 0,
                                   "y": 0,
                                   "width": 18,
                                   "height": 5,
                                   "view_mode": 0,
                                   "fields": [
                                       {
                                           "type": 4,
                                           "name": "itemid.0",
                                           "value": 44474
                                       },
                                       {
                                           "type": 1,
                                           "name": "min",
                                           "value": "100000"
                                       },
                                       {
                                           "type": 1,
                                           "name": "max",
                                           "value": "1000000"
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
                                           "type": 0,
                                           "name": "show.4",
                                           "value": 4
                                       },
                                       {
                                           "type": 0,
                                           "name": "show.5",
                                           "value": 5
                                       },
                                       {
                                           "type": 0,
                                           "name": "angle",
                                           "value": 270
                                       },
                                       {
                                           "type": 0,
                                           "name": "desc_size",
                                           "value": 10
                                       },
                                       {
                                           "type": 0,
                                           "name": "desc_bold",
                                           "value": 1
                                       },
                                       {
                                           "type": 0,
                                           "name": "decimal_places",
                                           "value": 0
                                       },
                                       {
                                           "type": 0,
                                           "name": "value_bold",
                                           "value": 1
                                       },
                                       {
                                           "type": 0,
                                           "name": "units_size",
                                           "value": 15
                                       },
                                       {
                                           "type": 0,
                                           "name": "units_pos",
                                           "value": 3
                                       },
                                       {
                                           "type": 1,
                                           "name": "needle_color",
                                           "value": "3C3C3C"
                                       },
                                       {
                                           "type": 1,
                                           "name": "thresholds.0.color",
                                           "value": "FF465C"
                                       },
                                       {
                                           "type": 1,
                                           "name": "thresholds.0.threshold",
                                           "value": "700000"
                                       },
                                       {
                                           "type": 1,
                                           "name": "thresholds.1.color",
                                           "value": "FFD54F"
                                       },
                                       {
                                           "type": 1,
                                           "name": "thresholds.1.threshold",
                                           "value": "500000"
                                       },
                                       {
                                           "type": 1,
                                           "name": "thresholds.2.color",
                                           "value": "0EC9AC"
                                       },
                                       {
                                           "type": 1,
                                           "name": "thresholds.2.threshold",
                                           "value": "100000"
                                       },
                                       {
                                           "type": 0,
                                           "name": "th_show_labels",
                                           "value": 1
                                       },
                                       {
                                           "type": 0,
                                           "name": "th_show_arc",
                                           "value": 1
                                       },
                                       {
                                           "type": 0,
                                           "name": "th_arc_size",
                                           "value": 15
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