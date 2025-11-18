---
title: Top triggers
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/dashboard/widget_fields/top_triggers
downloaded: 2025-11-14 10:41:09
---

# 29 Top triggers

### Description

These parameters and the possible property values for the respective dashboard widget field objects allow to configure the [_Top triggers_](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/top_triggers) widget in `dashboard.create` and `dashboard.update` methods.

Widget `fields` properties are not validated during the creation or update of a dashboard. This allows users to modify [built-in widgets](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets) and create [custom widgets](/documentation/current/en/devel/modules/tutorials/widget), but also introduces the risk of creating or updating widgets incorrectly. To ensure the successful creation or update of the _Top triggers_ widget, please refer to the parameter behavior outlined in the tables below.

### Parameters

The following parameters are supported for the _Top triggers_ widget.

_Refresh interval_ | 0 | rf_rate | 0 - _(default)_ No refresh;  
10 - 10 seconds;  
30 - 30 seconds;  
60 - 1 minute;  
120 - 2 minutes;  
600 - 10 minutes;  
900 - 15 minutes.  
---|---|---|---  
_Host groups_ | 2 | groupids.0 | [Host group](/documentation/current/en/manual/api/reference/hostgroup/get) ID.  
  
Note: To configure multiple host groups, create a dashboard widget field object for each host group with an incremented number in the property name.  
  
This parameter is not supported if configuring the widget on a [template dashboard](/documentation/current/en/manual/api/reference/templatedashboard/object).  
_Hosts_ | 3 | hostids.0 | [Host](/documentation/current/en/manual/api/reference/host/get) ID.  
  
Note: To configure multiple hosts, create a dashboard widget field object for each host with an incremented number in the property name. For multiple hosts, the parameter _Host groups_ must either be not configured at all or configured with at least one host group that the configured hosts belong to.  
  
This parameter is not supported if configuring the widget on a [template dashboard](/documentation/current/en/manual/api/reference/templatedashboard/object).  
_Problem_ | 1 | problem | Problem [event name](/documentation/current/en/manual/config/triggers/trigger#configuration) (case insensitive, full name or part of it).  
_Severity_ | 0 | severities.0 | Trigger severities.  
  
0 - Not classified;  
1 - Information;  
2 - Warning;  
3 - Average;  
4 - High;  
5 - Disaster.  
  
Default: empty (all enabled).  
  
Note: To configure multiple values, create a dashboard widget field object for each value with an incremented number in the property name.  
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
_Trigger limit_ | 0 | show_lines | Possible values range from 1-100.  
  
Default: 10.  
  
### Examples

The following examples aim to only describe the configuration of the dashboard widget field objects for the _Top triggers_ widget. For more information on configuring a dashboard, see [`dashboard.create`](/documentation/current/en/manual/api/reference/dashboard/create).

#### Configuring a _Top triggers_ widget

Configure a _Top triggers_ widget that displays the top 5 triggers for host group "4" with the count of all problems for each trigger. The widget displays only triggers that have severities "Warning", "Average", "High", or "Disaster", and problems that have a tag with the name "scope" that contains values "performance" or "availability", or "capacity".

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
                                   "type": "toptriggers",
                                   "name": "Top triggers",
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
                                           "type": 0,
                                           "name": "severities.0",
                                           "value": 2
                                       },
                                       {
                                           "type": 0,
                                           "name": "severities.1",
                                           "value": 3
                                       },
                                       {
                                           "type": 0,
                                           "name": "severities.2",
                                           "value": 4
                                       },
                                       {
                                           "type": 0,
                                           "name": "severities.3",
                                           "value": 5
                                       },
                                       {
                                           "type": 1,
                                           "name": "tags.0.tag",
                                           "value": "scope"
                                       },
                                       {
                                           "type": 0,
                                           "name": "tags.0.operator",
                                           "value": 0
                                       },
                                       {
                                           "type": 1,
                                           "name": "tags.0.value",
                                           "value": "performance"
                                       },
                                       {
                                           "type": 1,
                                           "name": "tags.1.tag",
                                           "value": "scope"
                                       },
                                       {
                                           "type": 0,
                                           "name": "tags.1.operator",
                                           "value": 0
                                       },
                                       {
                                           "type": 1,
                                           "name": "tags.1.value",
                                           "value": "availability"
                                       },
                                       {
                                           "type": 1,
                                           "name": "tags.2.tag",
                                           "value": "scope"
                                       },
                                       {
                                           "type": 0,
                                           "name": "tags.2.operator",
                                           "value": 0
                                       },
                                       {
                                           "type": 1,
                                           "name": "tags.2.value",
                                           "value": "capacity"
                                       },
                                       {
                                           "type": 0,
                                           "name": "show_lines",
                                           "value": 5
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