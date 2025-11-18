---
title: Problems
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/dashboard/widget_fields/problems
downloaded: 2025-11-14 10:41:03
---

# 23 Problems

### Description

These parameters and the possible property values for the respective dashboard widget field objects allow to configure the [_Problems_](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/problems) widget in `dashboard.create` and `dashboard.update` methods.

Widget `fields` properties are not validated during the creation or update of a dashboard. This allows users to modify [built-in widgets](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets) and create [custom widgets](/documentation/current/en/devel/modules/tutorials/widget), but also introduces the risk of creating or updating widgets incorrectly. To ensure the successful creation or update of the _Problems_ widget, please refer to the parameter behavior outlined in the tables below.

### Parameters

The following parameters are supported for the _Problems_ widget.

_Refresh interval_ | 0 | rf_rate | 0 - No refresh;  
10 - 10 seconds;  
30 - 30 seconds;  
60 - _(default)_ 1 minute;  
120 - 2 minutes;  
600 - 10 minutes;  
900 - 15 minutes.  
---|---|---|---  
_Show_ | 0 | show | 1 - _(default)_ Recent problems;  
2 - History;  
3 - Problems.  
_Host groups_ | 2 | groupids.0 | [Host group](/documentation/current/en/manual/api/reference/hostgroup/get) ID.  
  
Note: To configure multiple host groups, create a dashboard widget field object for each host group with an incremented number in the property name.  
  
This parameter is not supported if configuring the widget on a [template dashboard](/documentation/current/en/manual/api/reference/templatedashboard/object).  
| _Host groups (Widget)_ | 1 | groupids._reference | Instead of [Host group](/documentation/current/en/manual/api/reference/hostgroup/get) ID:  
`ABCDE._hostgroupids` \- set a [compatible widget](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#widget-compatibility) (with its _Reference_ parameter set to "`ABCDE`") as the data source for host groups.  
  
This parameter is not supported if configuring the widget on a [template dashboard](/documentation/current/en/manual/api/reference/templatedashboard/object).  
_Exclude host groups_ | 2 | exclude_groupids.0 | [Host group](/documentation/current/en/manual/api/reference/hostgroup/get) ID.  
  
Note: To exclude multiple host groups, create a dashboard widget field object for each host group with an incremented number in the property name.  
  
This parameter is not supported if configuring the widget on a [template dashboard](/documentation/current/en/manual/api/reference/templatedashboard/object).  
_Hosts_ | 3 | hostids.0 | [Host](/documentation/current/en/manual/api/reference/host/get) ID.  
  
Note: To configure multiple hosts, create a dashboard widget field object for each host with an incremented number in the property name. For multiple hosts, the parameter _Host groups_ must either be not configured at all or configured with at least one host group that the configured hosts belong to.  
  
This parameter is not supported if configuring the widget on a [template dashboard](/documentation/current/en/manual/api/reference/templatedashboard/object).  
| _Hosts (Widget/Dashboard)_ | 1 | hostids._reference | Instead of [Host](/documentation/current/en/manual/api/reference/host/get) ID:  
`DASHBOARD.hostids` \- set the [_Host_ selector](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#override-host) as the data source for hosts;  
`ABCDE._hostids` \- set a [compatible widget](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#widget-compatibility) (with its _Reference_ parameter set to "`ABCDE`") as the data source for hosts.  
  
This parameter is not supported if configuring the widget on a [template dashboard](/documentation/current/en/manual/api/reference/templatedashboard/object).  
_Problem_ | 1 | problem | Problem [event name](/documentation/current/en/manual/config/triggers/trigger#configuration) (case insensitive, full name or part of it).  
_Severity_ | 0 | severities.0 | 0 - Not classified;  
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
_Show tags_ | 0 | show_tags | 0 - _(default)_ None;  
1 - 1;  
2 - 2;  
3 - 3.  
_Tag name_ (format) | 0 | tag_name_format | 0 - _(default)_ Full;  
1 - Shortened;  
2 - None.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Show tags_ is set to "1", "2", or "3"  
_Tag display priority_ | 1 | tag_priority | Comma-separated list of tags.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Show tags_ is set to "1", "2", or "3"  
_Show operational data_ | 0 | show_opdata | 0 - _(default)_ None;  
1 - Separately;  
2 - With problem name.  
_Show suppressed problems_ | 0 | show_suppressed | 0 - _(default)_ Disabled;  
1 - Enabled.  
_Acknowledgement status_ | 0 | acknowledgement_status | 0 - _(default)_ all;  
1 - Unacknowledged;   
2 - Acknowledged.  
_By me_ | 0 | acknowledged_by_me | 0 - _(default)_ Disabled;  
1 - Enabled.  
_Sort entries by_ | 0 | sort_triggers | 1 - Severity (descending);  
2 - Host (ascending);  
3 - Time (ascending);  
4 - _(default)_ Time (descending);  
13 - Severity (ascending);  
14 - Host (descending);  
15 - Problem (ascending);  
16 - Problem (descending).  
  
For all values, except "Time (descending)" and "Time (ascending)", the _Show timeline_ parameter must be set to "Disabled".  
  
Values "Host (ascending)" and "Host (descending)" are not supported if configuring the widget on a [template dashboard](/documentation/current/en/manual/api/reference/templatedashboard/object).  
_Show timeline_ | 0 | show_timeline | 0 - Disabled;  
1 - _(default)_ Enabled.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Sort entries by_ is set to "Time (descending)" or "Time (ascending)"  
_Highlight whole row_ | 0 | highlight_row | 0 - _(default)_ Disabled;  
1 - Enabled.  
  
This parameter is not supported in the high-contrast themes.  
  
This option is supported since Zabbix 7.4.3.  
_Show lines_ | 0 | show_lines | Possible values range from 1-100.  
  
Default: 25.  
_Reference_ | 1 | reference | Any string value consisting of 5 characters (e.g., `ABCDE` or `JBPNL`). This value must be unique within the dashboard to which the widget belongs.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
  
### Examples

The following examples aim to only describe the configuration of the dashboard widget field objects for the _Problems_ widget. For more information on configuring a dashboard, see [`dashboard.create`](/documentation/current/en/manual/api/reference/dashboard/create).

#### Configuring a _Problems_ widget

Configure a _Problems_ widget that displays problems for host group "4" that satisfy the following conditions:

  * Problems that have a tag with the name "scope" that contains values "performance" or "availability", or "capacity".
  * Problems that have the following severities: "Warning", "Average", "High", "Disaster".

In addition, configure the widget to show tags and operational data.

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
                                   "type": "problems",
                                   "name": "Problems",
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
                                           "type": 0,
                                           "name": "show_tags",
                                           "value": 1
                                       },
                                       {
                                           "type": 0,
                                           "name": "show_opdata",
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