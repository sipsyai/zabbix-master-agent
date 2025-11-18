---
title: Host availability
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/dashboard/widget_fields/host_availability
downloaded: 2025-11-14 10:40:51
---

# 12 Host availability

### Description

These parameters and the possible property values for the respective dashboard widget field objects allow to configure the [_Host availability_](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/host_availability) widget in `dashboard.create` and `dashboard.update` methods.

### Parameters

The following parameters are supported for the _Host availability_ widget.

_Refresh interval_ | 0 | rf_rate | 0 - No refresh;  
10 - 10 seconds;  
30 - 30 seconds;  
60 - 1 minute;  
120 - 2 minutes;  
600 - 10 minutes;  
900 - _(default)_ 15 minutes.  
---|---|---|---  
_Host groups_ | 2 | groupids.0 | [Host group](/documentation/current/en/manual/api/reference/hostgroup/get) ID.  
  
Note: To configure multiple host groups, create a dashboard widget field object for each host group with an incremented number in the property name.  
  
This parameter is not supported if configuring the widget on a [template dashboard](/documentation/current/en/manual/api/reference/templatedashboard/object).  
| _Host groups (Widget)_ | 1 | groupids._reference | Instead of [Host group](/documentation/current/en/manual/api/reference/hostgroup/get) ID:  
`ABCDE._hostgroupids` \- set a [compatible widget](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#widget-compatibility) (with its _Reference_ parameter set to "`ABCDE`") as the data source for host groups.  
  
This parameter is not supported if configuring the widget on a [template dashboard](/documentation/current/en/manual/api/reference/templatedashboard/object).  
_Interface type_ | 0 | interface_type.0 | 0 - None;  
1 - Zabbix agent (passive checks);  
2 - SNMP;  
3 - IPMI;  
4 - JMX;  
5 - Zabbix agent (active checks).  
  
Default: 1, 2, 3, 4, 5 (all enabled).  
  
Note: To configure multiple values, create a dashboard widget field object for each value with an incremented number in the property name.  
_Layout_ | 0 | layout | 0 - _(default)_ Horizontal;  
1 - Vertical.  
_Show hosts in maintenance_ | 0 | maintenance | 0 - _(default)_ Disabled;  
1 - Enabled.  
_Show only totals_ | 0 | only_totals | 0 - _(default)_ Disabled;  
1 - Enabled.  
  
### Examples

The following examples aim to only describe the configuration of the dashboard widget field objects for the _Host availability_ widget. For more information on configuring a dashboard, see [`dashboard.create`](/documentation/current/en/manual/api/reference/dashboard/create).

#### Configuring a _Host availability_ widget

Configure a _Host availability_ widget that displays availability information (in a vertical layout) for hosts in host group "4" with "Zabbix agent" and "SNMP" interfaces configured.

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
                                   "type": "hostavail",
                                   "name": "Host availability",
                                   "x": 0,
                                   "y": 0,
                                   "width": 18,
                                   "height": 3,
                                   "view_mode": 0,
                                   "fields": [
                                       {
                                           "type": 2,
                                           "name": "groupids.0",
                                           "value": 4
                                       },
                                       {
                                           "type": 0,
                                           "name": "interface_type",
                                           "value": 1
                                       },
                                       {
                                           "type": 0,
                                           "name": "interface_type",
                                           "value": 2
                                       },
                                       {
                                           "type": 0,
                                           "name": "layout",
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