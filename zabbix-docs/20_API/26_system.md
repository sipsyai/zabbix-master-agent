---
title: System information
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/dashboard/widget_fields/system
downloaded: 2025-11-14 10:41:06
---

# 26 System information

### Description

These parameters and the possible property values for the respective dashboard widget field objects allow to configure the [_System Information_](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/system) widget in `dashboard.create` and `dashboard.update` methods.

Widget `fields` properties are not validated during the creation or update of a dashboard. This allows users to modify [built-in widgets](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets) and create [custom widgets](/documentation/current/en/devel/modules/tutorials/widget), but also introduces the risk of creating or updating widgets incorrectly. To ensure the successful creation or update of the _System information_ widget, please refer to the parameter behavior outlined in the tables below.

### Parameters

The following parameters are supported for the _System Information_ widget.

_Refresh interval_ | 0 | rf_rate | 0 - No refresh;  
10 - 10 seconds;  
30 - 30 seconds;  
60 - 1 minute;  
120 - 2 minutes;  
600 - 10 minutes;  
900 - _(default)_ 15 minutes.  
---|---|---|---  
_Show_ | 0 | info_type | 0 - _(default)_ System stats;  
1 - High availability nodes.  
_Show software update check details_ | 0 | show_software_update_check_details | 0 - _(default)_ Disabled;  
1 - Enabled.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if [`AllowSoftwareUpdateCheck`](/documentation/current/en/manual/appendix/config/zabbix_server#allowsoftwareupdatecheck) in Zabbix server configuration is enabled and _Show_ is set to "System stats"  
  
### Examples

The following examples aim to only describe the configuration of the dashboard widget field objects for the _System information_ widget. For more information on configuring a dashboard, see [`dashboard.create`](/documentation/current/en/manual/api/reference/dashboard/create).

#### Configuring a _System information_ widget

Configure a _System information_ widget that displays system stats with a refresh interval of 10 minutes and software update check enabled.

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
                                   "type": "systeminfo",
                                   "name": "System information",
                                   "x": 0,
                                   "y": 0,
                                   "width": 36,
                                   "height": 5,
                                   "view_mode": 0,
                                   "fields": [
                                       {
                                           "type": 0,
                                           "name": "rf_rate",
                                           "value": 600
                                       },
                                       {
                                           "type": 0,
                                           "name": "show_software_update_check_details",
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