---
title: Geomap
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/dashboard/widget_fields/geomap
downloaded: 2025-11-14 10:40:46
---

# 7 Geomap

### Description

These parameters and the possible property values for the respective dashboard widget field objects allow to configure the [_Geomap_](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/geomap) widget in `dashboard.create` and `dashboard.update` methods.

Widget `fields` properties are not validated during the creation or update of a dashboard. This allows users to modify [built-in widgets](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets) and create [custom widgets](/documentation/current/en/devel/modules/tutorials/widget), but also introduces the risk of creating or updating widgets incorrectly. To ensure the successful creation or update of the _Geomap_ widget, please refer to the parameter behavior outlined in the tables below.

### Parameters

The following parameters are supported for the _Geomap_ widget.

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
_Tags_  
| _Evaluation type_ | 0 | evaltype | 0 - _(default)_ And/Or;  
2 - Or.  
  
This parameter is not supported if configuring the widget on a [template dashboard](/documentation/current/en/manual/api/reference/templatedashboard/object).  
_Tag name_ | 1 | tags.0.tag | Any string value.  
  
Note: The number in the property name references tag order in the tag evaluation list.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_ if configuring _Tags_  
  
This parameter is not supported if configuring the widget on a [template dashboard](/documentation/current/en/manual/api/reference/templatedashboard/object).  
_Operator_ | 0 | tags.0.operator | 0 - Contains;  
1 - Equals;  
2 - Does not contain;  
3 - Does not equal;  
4 - Exists;  
5 - Does not exist.  
  
Note: The number in the property name references tag order in the tag evaluation list.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_ if configuring _Tags_  
  
This parameter is not supported if configuring the widget on a [template dashboard](/documentation/current/en/manual/api/reference/templatedashboard/object).  
_Tag value_ | 1 | tags.0.value | Any string value.  
  
Note: The number in the property name references tag order in the tag evaluation list.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_ if configuring _Tags_  
  
This parameter is not supported if configuring the widget on a [template dashboard](/documentation/current/en/manual/api/reference/templatedashboard/object).  
_Initial view_ | 1 | default_view | Comma separated _latitude_ , _longitude_ , _zoom level_ (_optional_ , possible values range from 0-30).  
Example: `40.6892494,-74.0466891,10`.  
_Reference_ | 1 | reference | Any string value consisting of 5 characters (e.g., `ABCDE` or `JBPNL`). This value must be unique within the dashboard to which the widget belongs.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
  
### Examples

The following examples aim to only describe the configuration of the dashboard widget field objects for the _Geomap_ widget. For more information on configuring a dashboard, see [`dashboard.create`](/documentation/current/en/manual/api/reference/dashboard/create).

#### Configuring a _Geomap_ widget

Configure a _Geomap_ widget that displays hosts from host groups "2" and "22" based on the following tag configuration: tag with the name "component" contains value "node", and tag with the name "location" equals value "New York". In addition, set the map initial view to coordinates "40.6892494" (latitude), "-74.0466891" (longitude) with the zoom level "10".

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
                                   "type": "geomap",
                                   "name": "Geomap",
                                   "x": 0,
                                   "y": 0,
                                   "width": 36,
                                   "height": 5,
                                   "view_mode": 0,
                                   "fields": [
                                       {
                                           "type": 2,
                                           "name": "groupids.0",
                                           "value": 22
                                       },
                                       {
                                           "type": 2,
                                           "name": "groupids.1",
                                           "value": 2
                                       },
                                       {
                                           "type": 1,
                                           "name": "default_view",
                                           "value": "40.6892494,-74.0466891,10"
                                       },
                                       {
                                           "type": 0,
                                           "name": "evaltype",
                                           "value": 2
                                       },
                                       {
                                           "type": 1,
                                           "name": "tags.0.tag",
                                           "value": "component"
                                       },
                                       {
                                           "type": 0,
                                           "name": "tags.0.operator",
                                           "value": 0
                                       },
                                       {
                                           "type": 1,
                                           "name": "tags.0.value",
                                           "value": "node"
                                       },
                                       {
                                           "type": 1,
                                           "name": "tags.1.tag",
                                           "value": "location"
                                       },
                                       {
                                           "type": 0,
                                           "name": "tags.1.operator",
                                           "value": 1
                                       },
                                       {
                                           "type": 1,
                                           "name": "tags.1.value",
                                           "value": "New York"
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