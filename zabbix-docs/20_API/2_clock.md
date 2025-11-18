---
title: Clock
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/dashboard/widget_fields/clock
downloaded: 2025-11-14 10:40:41
---

# 2 Clock

### Description

These parameters and the possible property values for the respective dashboard widget field objects allow to configure the [_Clock_](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/clock) widget in `dashboard.create` and `dashboard.update` methods.

Widget `fields` properties are not validated during the creation or update of a dashboard. This allows users to modify [built-in widgets](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets) and create [custom widgets](/documentation/current/en/devel/modules/tutorials/widget), but also introduces the risk of creating or updating widgets incorrectly. To ensure the successful creation or update of the _Clock_ widget, please refer to the parameter behavior outlined in the tables below.

### Parameters

The following parameters are supported for the _Clock_ widget.

_Refresh interval_ | 0 | rf_rate | 0 - No refresh;  
10 - 10 seconds;  
30 - 30 seconds;  
60 - 1 minute;  
120 - 2 minutes;  
600 - 10 minutes;  
900 - _(default)_ 15 minutes.  
---|---|---|---  
_Time type_ | 0 | time_type | 0 - _(default)_ Local time;  
1 - Server time;  
2 - Host time.  
_Clock type_ | 0 | clock_type | 0 - _(default)_ Analog;  
1 - Digital.  
  
The following parameters are supported if _Time type_ is set to "Host time".

_Item_ | 4 | itemid.0 | [Item](/documentation/current/en/manual/api/reference/item/get) ID.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
---|---|---|---  
  
The following parameters are supported if _Clock type_ is set to "Digital".

_Show_ | 0 | show.0 | 1 - Date;  
2 - _(default)_ Time;  
3 - Time zone.  
  
Note: To configure multiple values, create a dashboard widget field object for each value with an incremented number in the property name.  
---|---|---|---  
  
#### Advanced configuration

The following advanced configuration parameters are supported if _Clock type_ is set to "Digital".

_Background color_ | 1 | bg_color | Hexadecimal color code (e.g. `FF0000`).  
  
Default: `""` (empty).  
---|---|---|---  
  
##### Date

The following advanced configuration parameters are supported if _Clock type_ is set to "Digital", and _Show_ is set to "Date".

_Bold_ | 0 | date_bold | 0 - _(default)_ Disabled;  
1 - Enabled.  
---|---|---|---  
_Color_ | 1 | date_color | Hexadecimal color code (e.g. `FF0000`).  
  
Default: `""` (empty).  
  
##### Time

The following advanced configuration parameters are supported if _Clock type_ is set to "Digital", and _Show_ is set to "Time".

_Bold_ | 0 | time_bold | 0 - _(default)_ Disabled;  
1 - Enabled.  
---|---|---|---  
_Color_ | 1 | time_color | Hexadecimal color code (e.g. `FF0000`).  
  
Default: `""` (empty).  
_Seconds_ | 0 | time_sec | 0 - Disabled;  
1 - _(default)_ Enabled.  
_Format_ | 0 | time_format | 0 - _(default)_ 24-hour;  
1 - 12-hour.  
  
##### Time zone

The following advanced configuration parameters are supported if _Clock type_ is set to "Digital", and _Show_ is set to "Time zone".

_Bold_ | 0 | tzone_bold | 0 - _(default)_ Disabled;  
1 - Enabled.  
---|---|---|---  
_Color_ | 1 | tzone_color | Hexadecimal color code (e.g. `FF0000`).  
  
Default: `""` (empty).  
_Time zone_ | 1 | tzone_timezone | Valid timezone string (e.g. `Europe/Riga`, `system`, `UTC`, etc.). For the full list of supported time zones please refer to [PHP documentation](https://www.php.net/manual/en/timezones.php).  
  
Default: `local`.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Time type_ is set to "Local time" or "Server time"  
_Format_ | 0 | tzone_format | 0 - _(default)_ Short;  
1 - Full.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Time type_ is set to "Local time" or "Server time"  
  
### Examples

The following examples aim to only describe the configuration of the dashboard widget field objects for the _Clock_ widget. For more information on configuring a dashboard, see [`dashboard.create`](/documentation/current/en/manual/api/reference/dashboard/create).

#### Configuring a _Clock_ widget

Configure a _Clock_ widget that displays local date, time and time zone in a customized digital clock.

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
                                   "type": "clock",
                                   "name": "Clock",
                                   "x": 0,
                                   "y": 0,
                                   "width": 12,
                                   "height": 3,
                                   "view_mode": 0,
                                   "fields": [
                                       {
                                           "type": 0,
                                           "name": "clock_type",
                                           "value": 1
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
                                           "name": "date_color",
                                           "value": "E1E1E1"
                                       },
                                       {
                                           "type": 0,
                                           "name": "time_bold",
                                           "value": 1
                                       },
                                       {
                                           "type": 1,
                                           "name": "tzone_color",
                                           "value": "E1E1E1"
                                       },
                                       {
                                           "type": 1,
                                           "name": "tzone_timezone",
                                           "value": "Europe/Riga"
                                       },
                                       {
                                           "type": 0,
                                           "name": "tzone_format",
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