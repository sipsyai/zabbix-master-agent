---
title: SLA report
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/dashboard/widget_fields/sla_report
downloaded: 2025-11-14 10:41:05
---

# 25 SLA report

### Description

These parameters and the possible property values for the respective dashboard widget field objects allow to configure the [_SLA report_](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/sla_report) widget in `dashboard.create` and `dashboard.update` methods.

Widget `fields` properties are not validated during the creation or update of a dashboard. This allows users to modify [built-in widgets](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets) and create [custom widgets](/documentation/current/en/devel/modules/tutorials/widget), but also introduces the risk of creating or updating widgets incorrectly. To ensure the successful creation or update of the _SLA report_ widget, please refer to the parameter behavior outlined in the tables below.

### Parameters

The following parameters are supported for the _SLA report_ widget.

_Refresh interval_ | 0 | rf_rate | 0 - _(default)_ No refresh;  
10 - 10 seconds;  
30 - 30 seconds;  
60 - 1 minute;  
120 - 2 minutes;  
600 - 10 minutes;  
900 - 15 minutes.  
---|---|---|---  
_SLA_ | 10 | slaid.0 | [SLA](/documentation/current/en/manual/api/reference/sla/get) ID.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
_Service_ | 9 | serviceid.0 | [Service](/documentation/current/en/manual/api/reference/service/get) ID.  
_Show periods_ | 0 | show_periods | Possible values range from 1-100.  
  
Default: 20.  
_From_ | 1 | date_from | Valid date string in format `YYYY-MM-DD`.  
[Relative dates](/documentation/current/en/manual/web_interface/time_period_selector) with modifiers `d`, `w`, `M`, `y` (e.g. `now`, `now/d`, `now/w-1w`, etc.) are supported.  
_To_ | 1 | date_to | Valid date string in format `YYYY-MM-DD`.  
[Relative dates](/documentation/current/en/manual/web_interface/time_period_selector) with modifiers `d`, `w`, `M`, `y` (e.g. `now`, `now/d`, `now/w-1w`, etc.) are supported.  
  
### Examples

The following examples aim to only describe the configuration of the dashboard widget field objects for the _SLA report_ widget. For more information on configuring a dashboard, see [`dashboard.create`](/documentation/current/en/manual/api/reference/dashboard/create).

#### Configuring an _SLA report_ widget

Configure an _SLA report_ widget that displays the SLA report for SLA "4" service "2" for the period of last 30 days.

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
                                   "type": "slareport",
                                   "name": "SLA report",
                                   "x": 0,
                                   "y": 0,
                                   "width": 36,
                                   "height": 5,
                                   "view_mode": 0,
                                   "fields": [
                                       {
                                           "type": 10,
                                           "name": "slaid.0",
                                           "value": 4
                                       },
                                       {
                                           "type": 9,
                                           "name": "serviceid.0",
                                           "value": 2
                                       },
                                       {
                                           "type": 1,
                                           "name": "date_from",
                                           "value": "now-30d"
                                       },
                                       {
                                           "type": 1,
                                           "name": "date_to",
                                           "value": "now"
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