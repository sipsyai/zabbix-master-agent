---
title: Map
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/dashboard/widget_fields/map
downloaded: 2025-11-14 10:40:59
---

# 19 Map

### Description

These parameters and the possible property values for the respective dashboard widget field objects allow to configure the [_Map_](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/map) widget in `dashboard.create` and `dashboard.update` methods.

Widget `fields` properties are not validated during the creation or update of a dashboard. This allows users to modify [built-in widgets](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets) and create [custom widgets](/documentation/current/en/devel/modules/tutorials/widget), but also introduces the risk of creating or updating widgets incorrectly. To ensure the successful creation or update of the _Map_ widget, please refer to the parameter behavior outlined in the tables below.

### Parameters

The following parameters are supported for the _Map_ widget.

_Refresh interval_ | 0 | rf_rate | 0 - No refresh;  
10 - 10 seconds;  
30 - 30 seconds;  
60 - 1 minute;  
120 - 2 minutes;  
600 - 10 minutes;  
900 - _(default)_ 15 minutes.  
---|---|---|---  
_Map_ | 8 | sysmapid.0 | [Map](/documentation/current/en/manual/api/reference/map/get) ID.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_ if _Map (Widget)_ is not set  
| _Map (Widget)_ | 1 | sysmapid._reference | `ABCDE._mapid` \- set a [_Map navigation tree_](/documentation/current/en/manual/api/reference/dashboard/widget_fields/map_tree) widget (with its _Reference_ parameter set to "`ABCDE`") as the data source for maps.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_ if _Map_ is not set  
_Reference_ | 1 | reference | Any string value consisting of 5 characters (e.g., `ABCDE` or `JBPNL`). This value must be unique within the dashboard to which the widget belongs.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
  
### Examples

The following examples aim to only describe the configuration of the dashboard widget field objects for the _Map_ widget. For more information on configuring a dashboard, see [`dashboard.create`](/documentation/current/en/manual/api/reference/dashboard/create).

#### Configuring a _Map_ widget

Configure a _Map_ widget that displays the map "1".

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
                                   "type": "map",
                                   "name": "Map",
                                   "x": 0,
                                   "y": 0,
                                   "width": 54,
                                   "height": 5,
                                   "view_mode": 0,
                                   "fields": [
                                       {
                                           "type": 8,
                                           "name": "sysmapid.0",
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

#### Configuring a linked _Map_ widget

Configure a _Map_ widget that is linked to a [_Map navigation tree_](/documentation/current/en/manual/api/reference/dashboard/widget_fields/map_tree#configuring-a-map-navigation-tree-widget) widget.

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
                                   "type": "map",
                                   "name": "Map",
                                   "x": 0,
                                   "y": 5,
                                   "width": 54,
                                   "height": 5,
                                   "view_mode": 0,
                                   "fields": [
                                       {
                                           "type": 1,
                                           "name": "sysmapid._reference",
                                           "value": "ABCDE._mapid"
                                       }
                                   ]
                               },
                               {
                                   "type": "navtree",
                                   "name": "Map navigation tree",
                                   "x": 0,
                                   "y": 0,
                                   "width": 18,
                                   "height": 5,
                                   "view_mode": 0,
                                   "fields": [
                                       {
                                           "type": 1,
                                           "name": "navtree.1.name",
                                           "value": "Element A"
                                       },
                                       {
                                           "type": 1,
                                           "name": "navtree.2.name",
                                           "value": "Element B"
                                       },
                                       {
                                           "type": 1,
                                           "name": "navtree.3.name",
                                           "value": "Element C"
                                       },
                                       {
                                           "type": 1,
                                           "name": "navtree.4.name",
                                           "value": "Element A1"
                                       },
                                       {
                                           "type": 1,
                                           "name": "navtree.5.name",
                                           "value": "Element A2"
                                       },
                                       {
                                           "type": 1,
                                           "name": "navtree.6.name",
                                           "value": "Element B1"
                                       },
                                       {
                                           "type": 1,
                                           "name": "navtree.7.name",
                                           "value": "Element B2"
                                       },
                                       {
                                           "type": 0,
                                           "name": "navtree.4.parent",
                                           "value": 1
                                       },
                                       {
                                           "type": 0,
                                           "name": "navtree.5.parent",
                                           "value": 1
                                       },
                                       {
                                           "type": 0,
                                           "name": "navtree.6.parent",
                                           "value": 2
                                       },
                                       {
                                           "type": 0,
                                           "name": "navtree.7.parent",
                                           "value": 2
                                       },
                                       {
                                           "type": 0,
                                           "name": "navtree.1.order",
                                           "value": 1
                                       },
                                       {
                                           "type": 0,
                                           "name": "navtree.2.order",
                                           "value": 2
                                       },
                                       {
                                           "type": 0,
                                           "name": "navtree.3.order",
                                           "value": 3
                                       },
                                       {
                                           "type": 0,
                                           "name": "navtree.4.order",
                                           "value": 1
                                       },
                                       {
                                           "type": 0,
                                           "name": "navtree.5.order",
                                           "value": 2
                                       },
                                       {
                                           "type": 0,
                                           "name": "navtree.6.order",
                                           "value": 1
                                       },
                                       {
                                           "type": 0,
                                           "name": "navtree.7.order",
                                           "value": 2
                                       },
                                       {
                                           "type": 8,
                                           "name": "navtree.6.sysmapid",
                                           "value": 1
                                       },
                                       {
                                           "type": 1,
                                           "name": "reference",
                                           "value": "ABCDE"
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
  * [Map navigation tree](/documentation/current/en/manual/api/reference/dashboard/widget_fields/map_tree)