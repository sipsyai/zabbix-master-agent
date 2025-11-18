---
title: Discovery status
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/dashboard/widget_fields/discovery_status
downloaded: 2025-11-14 10:40:42
---

# 3 Discovery status

### Description

These parameters and the possible property values for the respective dashboard widget field objects allow to configure the [_Discovery status_](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/discovery_status) widget in `dashboard.create` and `dashboard.update` methods.

### Parameters

The following parameters are supported for the _Discovery status_ widget.

_Refresh interval_ | 0 | rf_rate | 0 - No refresh;  
10 - 10 seconds;  
30 - 30 seconds;  
60 - _(default)_ 1 minute;  
120 - 2 minutes;  
600 - 10 minutes;  
900 - 15 minutes.  
---|---|---|---  
  
### Examples

The following examples aim to only describe the configuration of the dashboard widget field objects for the _Discovery status_ widget. For more information on configuring a dashboard, see [`dashboard.create`](/documentation/current/en/manual/api/reference/dashboard/create).

#### Configuring _Discovery status_ widget

Configure a _Discovery status_ widget with the refresh interval set to 15 minutes.

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
                                   "type": "discovery",
                                   "name": "Discovery status",
                                   "x": 0,
                                   "y": 0,
                                   "width": 18,
                                   "height": 3,
                                   "view_mode": 0,
                                   "fields": [
                                       {
                                           "type": 0,
                                           "name": "rf_rate",
                                           "value": 900
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