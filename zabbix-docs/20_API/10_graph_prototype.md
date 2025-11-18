---
title: Graph prototype
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/dashboard/widget_fields/graph_prototype
downloaded: 2025-11-14 10:40:49
---

# 10 Graph prototype

### Description

These parameters and the possible property values for the respective dashboard widget field objects allow to configure the [_Graph prototype_](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/graph_prototype) widget in `dashboard.create` and `dashboard.update` methods.

Widget `fields` properties are not validated during the creation or update of a dashboard. This allows users to modify [built-in widgets](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets) and create [custom widgets](/documentation/current/en/devel/modules/tutorials/widget), but also introduces the risk of creating or updating widgets incorrectly. To ensure the successful creation or update of the _Graph prototype_ widget, please refer to the parameter behavior outlined in the tables below.

### Parameters

The following parameters are supported for the _Graph prototype_ widget.

_Refresh interval_ | 0 | rf_rate | 0 - No refresh;  
10 - 10 seconds;  
30 - 30 seconds;  
60 - _(default)_ 1 minute;  
120 - 2 minutes;  
600 - 10 minutes;  
900 - 15 minutes.  
---|---|---|---  
_Source_ | 0 | source_type | 2 - _(default)_ Graph prototype;  
3 - Simple graph prototype.  
_Graph prototype_ | 7 | graphid.0 | [Graph prototype](/documentation/current/en/manual/api/reference/graphprototype/get) ID.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_ if _Source_ is set to "Graph prototype"  
_Item prototype_ | 5 | itemid.0 | [Item prototype](/documentation/current/en/manual/api/reference/itemprototype/get) ID.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_ if _Source_ is set to "Simple graph prototype"  
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
_Show legend_ | 0 | show_legend | 0 - Disabled;  
1 - _(default)_ Enabled.  
_Override host_ | 1 | override_hostid._reference | `ABCDE._hostid` \- set a [compatible widget](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#widget-compatibility) (with its _Reference_ parameter set to "`ABCDE`") as the data source for hosts;  
`DASHBOARD._hostid` \- set the dashboard [_Host_ selector](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#override-host) as the data source for hosts.  
  
This parameter is not supported if configuring the widget on a [template dashboard](/documentation/current/en/manual/api/reference/templatedashboard/object).  
_Columns_ | 0 | columns | Possible values range from 1-24.  
  
Default: 2.  
_Rows_ | 0 | rows | Possible values range from 1-16.  
  
Default: 1.  
_Reference_ | 1 | reference | Any string value consisting of 5 characters (e.g., `ABCDE` or `JBPNL`). This value must be unique within the dashboard to which the widget belongs.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
  
### Examples

The following examples aim to only describe the configuration of the dashboard widget field objects for the _Graph prototype_ widget. For more information on configuring a dashboard, see [`dashboard.create`](/documentation/current/en/manual/api/reference/dashboard/create).

#### Configuring a _Graph prototype_ widget

Configure a _Graph prototype_ widget that displays a grid of 3 graphs (3 columns, 1 row) created from an item prototype (ID: "42316") by low-level discovery.

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
                                   "type": "graphprototype",
                                   "name": "Graph prototype",
                                   "x": 0,
                                   "y": 0,
                                   "width": 48,
                                   "height": 5,
                                   "view_mode": 0,
                                   "fields": [
                                       {
                                           "type": 0,
                                           "name": "source_type",
                                           "value": 3
                                       },
                                       {
                                           "type": 5,
                                           "name": "itemid.0",
                                           "value": 42316
                                       },
                                       {
                                           "type": 0,
                                           "name": "columns",
                                           "value": 3
                                       },
                                       {
                                           "type": 1,
                                           "name": "reference",
                                           "value": "OPQWX"
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