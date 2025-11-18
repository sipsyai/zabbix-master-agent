---
title: Map navigation tree
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/dashboard/widget_fields/map_tree
downloaded: 2025-11-14 10:41:00
---

# 20 Map navigation tree

### Description

These parameters and the possible property values for the respective dashboard widget field objects allow to configure the [_Map navigation tree_](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/map_tree) widget in `dashboard.create` and `dashboard.update` methods.

Widget `fields` properties are not validated during the creation or update of a dashboard. This allows users to modify [built-in widgets](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets) and create [custom widgets](/documentation/current/en/devel/modules/tutorials/widget), but also introduces the risk of creating or updating widgets incorrectly. To ensure the successful creation or update of the _Map navigation tree_ widget, please refer to the parameter behavior outlined in the tables below.

### Parameters

The following parameters are supported for the _Map navigation tree_ widget.

_Refresh interval_ | 0 | rf_rate | 0 - No refresh;  
10 - 10 seconds;  
30 - 30 seconds;  
60 - 1 minute;  
120 - 2 minutes;  
600 - 10 minutes;  
900 - _(default)_ 15 minutes.  
---|---|---|---  
_Show unavailable maps_ | 1 | show_unavailable | 0 - _(default)_ Disabled;  
1 - Enabled.  
_Reference_ | 1 | reference | Any string value consisting of 5 characters (e.g., `ABCDE` or `JBPNL`). This value must be unique within the dashboard to which the widget belongs.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
  
The following parameters are supported for configuring map navigation tree elements.

_Name_ | 1 | navtree.1.name | Any string value.  
  
Note: The number in the property name sets the element number.  
---|---|---|---  
_Linked map_ | 8 | navtree.1.sysmapid | [Map](/documentation/current/en/manual/api/reference/map/get) ID.  
  
Note: The number in the property name references the element to which the map is linked.  
_Parameters for creating element hierarchy_ | 0 | navtree.1.parent | Parent element number.  
  
Note: The number in the property name references the child element. The property value references the parent element.  
0 | navtree.1.order | Element position in the map navigation tree.  
  
Note: The number in the property name references the element number. The property value references the element position in the map navigation tree. Parent element position is determined within the whole map navigation tree. Child element position is determined within the parent element.  
  
### Examples

The following examples aim to only describe the configuration of the dashboard widget field objects for the _Map navigation tree_ widget. For more information on configuring a dashboard, see [`dashboard.create`](/documentation/current/en/manual/api/reference/dashboard/create).

#### Configuring a _Map navigation tree_ widget

Configure a _Map navigation tree_ widget that displays the following map navigation tree:

  * Element A 
    * Element A1
    * Element A2
  * Element B 
    * Element B1 (contains linked map "1" that can be displayed in a [linked _Map widget_](/documentation/current/en/manual/api/reference/dashboard/widget_fields/map#configuring-a-linked-map-widget))
    * Element B2
  * Element C

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
                                           "value": "HJQXF"
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
  * [Map](/documentation/current/en/manual/api/reference/dashboard/widget_fields/map)