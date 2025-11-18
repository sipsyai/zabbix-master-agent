---
title: Host navigator
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/dashboard/widget_fields/host_navigator
downloaded: 2025-11-14 10:40:53
---

# 14 Host navigator

### Description

These parameters and the possible property values for the respective dashboard widget field objects allow to configure the [_Host navigator_](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/host_navigator) widget in `dashboard.create` and `dashboard.update` methods.

Widget `fields` properties are not validated during the creation or update of a dashboard. This allows users to modify [built-in widgets](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets) and create [custom widgets](/documentation/current/en/devel/modules/tutorials/widget), but also introduces the risk of creating or updating widgets incorrectly. To ensure the successful creation or update of the _Host navigator_ widget, please refer to the parameter behavior outlined in the tables below.

### Parameters

The following parameters are supported for the _Host navigator_ widget.

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
_Host patterns_ | 1 | hosts.0 | [Host](/documentation/current/en/manual/api/reference/host/get) name or pattern.  
  
Note: To configure multiple host patterns, create a dashboard widget field object for each host pattern with an incremented number in the property name. For multiple host patterns, the parameter _Host groups_ must either be not configured at all or configured with at least one host group that the hosts matching the configured host patterns belong to.  
  
This parameter is not supported if configuring the widget on a [template dashboard](/documentation/current/en/manual/api/reference/templatedashboard/object).  
_Host status_ | 0 | status | -1 - _(default)_ Any;  
0 - Enabled;  
1 - Disabled.  
  
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
_Severity_ | 0 | severities.0 | 0 - Not classified;  
1 - Information;  
2 - Warning;  
3 - Average;  
4 - High;  
5 - Disaster.  
  
Default: empty (all enabled).  
  
Note: To configure multiple values, create a dashboard widget field object for each value with an incremented number in the property name.  
_Show hosts in maintenance_ | 0 | maintenance | 0 - _(default)_ Disabled;  
1 - Enabled.  
_Show problems_ | 0 | show_problems | 0 - All;  
1 - _(default)_ Unsuppressed;  
2 - None.  
_Group by_  
| _Attribute_ | 0 | group_by.0.attribute | 0 - Host group;  
1 - Tag value;  
2 - Severity.  
  
Note: The number in the property name references attribute order in the grouping attribute list.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_ if configuring _Group by_  
_Value_ | 1 | group_by.0.tag_name | Any string value.  
  
Note: The number in the property name references the grouping attribute set in the _Attribute_ parameter.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_ if configuring _Group by_ and _Attribute_ is set to "Tag value"  
_Host limit_ | 0 | show_lines | Possible values range from 1-9999.  
  
Default: 100.  
  
This parameter is not supported if configuring the widget on a [template dashboard](/documentation/current/en/manual/api/reference/templatedashboard/object).  
_Reference_ | 1 | reference | Any string value consisting of 5 characters (e.g., `ABCDE` or `JBPNL`). This value must be unique within the dashboard to which the widget belongs.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
  
### Examples

The following examples aim to only describe the configuration of the dashboard widget field objects for the _Host navigator_ widget. For more information on configuring a dashboard, see [`dashboard.create`](/documentation/current/en/manual/api/reference/dashboard/create).

#### Configuring a _Host navigator_ widget

Configure a _Host navigator_ widget that displays hosts grouped by their host group and, then, by the "city" tag value.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "dashboard.create",
               "params": {
                   "name": "My dashboard",
                   "display_period": "30",
                   "auto_start": "1",
                   "pages": [
                       {
                           "widgets": [
                               {
                                   "type": "hostnavigator",
                                   "name": "Host navigator",
                                   "x": "0",
                                   "y": "0",
                                   "width": "12",
                                   "height": "5",
                                   "view_mode": "0",
                                   "fields": [
                                       {
                                           "type": 2,
                                           "name": "groupids.0",
                                           "value": 2
                                       },
                                       {
                                           "type": 2,
                                           "name": "groupids.1",
                                           "value": 4
                                       },
                                       {
                                           "type": 0,
                                           "name": "group_by.0.attribute",
                                           "value": 0
                                       },
                                       {
                                           "type": 0,
                                           "name": "group_by.1.attribute",
                                           "value": 1
                                       },
                                       {
                                           "type": 1,
                                           "name": "group_by.1.tag_name",
                                           "value": "city"
                                       },
                                       {
                                           "type": 1,
                                           "name": "reference",
                                           "value": "SWKLB"
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