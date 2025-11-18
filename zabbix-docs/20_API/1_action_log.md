---
title: Action log
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/dashboard/widget_fields/action_log
downloaded: 2025-11-14 10:40:40
---

# 1 Action log

### Description

These parameters and the possible property values for the respective dashboard widget field objects allow to configure the [_Action log_](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/action_log) widget in `dashboard.create` and `dashboard.update` methods.

Widget `fields` properties are not validated during the creation or update of a dashboard. This allows users to modify [built-in widgets](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets) and create [custom widgets](/documentation/current/en/devel/modules/tutorials/widget), but also introduces the risk of creating or updating widgets incorrectly. To ensure the successful creation or update of the _Action log_ widget, please refer to the parameter behavior outlined in the tables below.

### Parameters

The following parameters are supported for the _Action log_ widget.

_Refresh interval_ | 0 | rf_rate | 0 - No refresh;  
10 - 10 seconds;  
30 - 30 seconds;  
60 - _(default)_ 1 minute;  
120 - 2 minutes;  
600 - 10 minutes;  
900 - 15 minutes.  
---|---|---|---  
_Recipients_ | 11 | userids.0 | [User](/documentation/current/en/manual/api/reference/user/get) ID.  
  
Note: To configure multiple users, create a dashboard widget field object for each user with an incremented number in the property name.  
_Actions_ | 12 | actionids.0 | [Action](/documentation/current/en/manual/api/reference/action/get) ID.  
  
Note: To configure multiple actions, create a dashboard widget field object for each action with an incremented number in the property name.  
_Media types_ | 13 | mediatypeids.0 | [Media type](/documentation/current/en/manual/api/reference/mediatype/get) ID.  
  
Note: To configure multiple media types, create a dashboard widget field object for each media type with an incremented number in the property name.  
_Status_ | 0 | statuses.0 | 0 - In progress;  
1 - Sent/Executed;  
2 - Failed.  
  
Note: To configure multiple values, create a dashboard widget field object for each value with an incremented number in the property name.  
_Search string_ | 1 | message | Any string value.  
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
_Sort entries by_ | 0 | sort_triggers | 3 - Time (ascending);  
4 - _(default)_ Time (descending);  
5 - Type (ascending);  
6 - Type (descending);  
7 - Status (ascending);  
8 - Status (descending);  
11 - Recipient (ascending);  
12 - Recipient (descending).  
_Show lines_ | 0 | show_lines | Possible values range from 1-100.  
  
Default: 25.  
  
### Examples

The following examples aim to only describe the configuration of the dashboard widget field objects for the _Action log_ widget. For more information on configuring a dashboard, see [`dashboard.create`](/documentation/current/en/manual/api/reference/dashboard/create).

#### Configuring an _Action log_ widget

Configure an _Action log_ widget that displays 10 entries of action operation details, sorted by time (in ascending order). In addition, display details only for those action operations that attempted to send an email to user "1", but were unsuccessful.

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
                                   "type": "actionlog",
                                   "name": "Action log",
                                   "x": 0,
                                   "y": 0,
                                   "width": 36,
                                   "height": 5,
                                   "view_mode": 0,
                                   "fields": [
                                       {
                                           "type": 0,
                                           "name": "show_lines",
                                           "value": 10
                                       },
                                       {
                                           "type": 0,
                                           "name": "sort_triggers",
                                           "value": 3
                                       },
                                       {
                                           "type": 11,
                                           "name": "userids.0",
                                           "value": 1
                                       },
                                       {
                                           "type": 13,
                                           "name": "mediatypeids.0",
                                           "value": 1
                                       },
                                       {
                                           "type": 0,
                                           "name": "statuses.0",
                                           "value": 2
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