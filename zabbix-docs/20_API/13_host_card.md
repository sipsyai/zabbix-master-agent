---
title: Host card
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/dashboard/widget_fields/host_card
downloaded: 2025-11-14 10:40:52
---

# 13 Host card

### Description

These parameters and the possible property values for the respective dashboard widget field objects allow to configure the [_Host card_](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/host_card) widget in `dashboard.create` and `dashboard.update` methods.

Widget `fields` properties are not validated during the creation or update of a dashboard. This allows users to modify [built-in widgets](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets) and create [custom widgets](/documentation/current/en/devel/modules/tutorials/widget), but also introduces the risk of creating or updating widgets incorrectly. To ensure the successful creation or update of the _Host card_ widget, please refer to the parameter behavior outlined in the tables below.

### Parameters

The following parameters are supported for the _Host card_ widget.

_Refresh interval_ | 0 | rf_rate | 0 - No refresh;  
10 - 10 seconds;  
30 - 30 seconds;  
60 - _(default)_ 1 minute;  
120 - 2 minutes;  
600 - 10 minutes;  
900 - 15 minutes.  
---|---|---|---  
_Host_ | 3 | hostid.0 | [Host](/documentation/current/en/manual/api/reference/host/get) ID.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_ if _Host (Widget/Dashboard)_ is not set  
  
This parameter is not supported if configuring the widget on a [template dashboard](/documentation/current/en/manual/api/reference/templatedashboard/object).  
| _Host (Widget/Dashboard)_ | 1 | hostid._reference | Instead of [Host](/documentation/current/en/manual/api/reference/host/get) ID:  
`DASHBOARD.hostid` \- set the [_Host_ selector](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#override-host) as the data source for host;  
`ABCDE._hostid` \- set a [compatible widget](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#widget-compatibility) (with its _Reference_ parameter set to "`ABCDE`") as the data source for host.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_ if _Host_ is not set  
  
This parameter is not supported if configuring the widget on a [template dashboard](/documentation/current/en/manual/api/reference/templatedashboard/object).  
_Show suppressed problems_ | 0 | show_suppressed | 0 - _(default)_ Disabled;  
1 - Enabled.  
_Show_ | 0 | sections.0 | 0 - Host groups;  
1 - Description;  
2 - Monitoring;  
3 - Availability;  
4 - Monitored by;  
5 - Templates;  
6 - Inventory;  
7 - Tags.  
  
Note: The number in the property name references section order in the section list. To configure multiple sections, create a dashboard widget field object for each section with an incremented number in the property name.  
  
The following parameters are supported if _Show_ is set to "Inventory".

_Inventory fields_ | 0 | inventory.0 | [Inventory](/documentation/current/en/manual/api/reference/host/object#host-inventory) ID.  
  
Note: To configure multiple inventory fields, create a dashboard widget field object for each inventory field with an incremented number in the property name.  
---|---|---|---  
  
### Examples

The following examples aim to only describe the configuration of the dashboard widget field objects for the _Host card_ widget. For more information on configuring a dashboard, see [`dashboard.create`](/documentation/current/en/manual/api/reference/dashboard/create).

#### Configuring a _Host card_ widget

Configure a _Host card_ widget that displays these sections: "Monitoring", "Availability", "Monitored by", "Inventory", and "Tags".

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
                                   "type": "hostcard",
                                   "name": "Host card",
                                   "x": 0,
                                   "y": 0,
                                   "width": 14,
                                   "height": 7,
                                   "view_mode": 0,
                                   "fields": [
                                       {
                                           "type": 3,
                                           "name": "hostid.0",
                                           "value": 10084
                                       },
                                       {
                                           "type": 0,
                                           "name": "show_suppressed",
                                           "value": 1
                                       },
                                       {
                                           "type": 0,
                                           "name": "sections.0",
                                           "value": 2
                                       },
                                       {
                                           "type": 0,
                                           "name": "sections.1",
                                           "value": 3
                                       },
                                       {
                                           "type": 0,
                                           "name": "sections.2",
                                           "value": 4
                                       },
                                       {
                                           "type": 0,
                                           "name": "sections.3",
                                           "value": 6
                                       },
                                       {
                                           "type": 0,
                                           "name": "sections.4",
                                           "value": 7
                                       },
                                       {
                                           "type": 0,
                                           "name": "inventory.0",
                                           "value": 25
                                       },
                                       {
                                           "type": 0,
                                           "name": "inventory.1",
                                           "value": 26
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