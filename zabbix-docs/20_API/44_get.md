---
title: dashboard.get
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/dashboard/get
downloaded: 2025-11-14 10:40:37
---

# dashboard.get

### Description

`integer/array dashboard.get(object parameters)`

The method allows to retrieve dashboards according to the given parameters.

This method is available to users of any type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object)` Parameters defining the desired output.

The method supports the following parameters.

dashboardids | ID/array | Return only dashboards with the given IDs.  
---|---|---  
selectPages | query | Return a [`pages`](/documentation/current/en/manual/api/reference/dashboard/object#dashboard-page) property with dashboard pages, correctly ordered.  
selectUsers | query | Return a [`users`](/documentation/current/en/manual/api/reference/dashboard/object#dashboard-user) property with users that the dashboard is shared with.  
selectUserGroups | query | Return a [`userGroups`](/documentation/current/en/manual/api/reference/dashboard/object#dashboard-user-group) property with user groups that the dashboard is shared with.  
sortfield | string/array | Sort the result by the given properties.  
  
Possible values: `dashboardid`.  
countOutput | boolean | These parameters are described in the [reference commentary](/documentation/current/en/manual/api/reference_commentary#common-get-method-parameters).  
editable | boolean  
excludeSearch | boolean  
filter | object  
limit | integer  
output | query  
preservekeys | boolean  
search | object  
searchByAny | boolean  
searchWildcardsEnabled | boolean  
sortorder | string/array  
startSearch | boolean  
  
### Return values

`(integer/array)` Returns either:

  * an array of objects;
  * the count of retrieved objects, if the `countOutput` parameter has been used.

### Examples

#### Retrieving a dashboard by ID

Retrieve all data about dashboards "1" and "2".

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "dashboard.get",
               "params": {
                   "output": "extend",
                   "selectPages": "extend",
                   "selectUsers": "extend",
                   "selectUserGroups": "extend",
                   "dashboardids": [
                       "1",
                       "2"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": [
                   {
                       "dashboardid": "1",
                       "name": "Dashboard",
                       "userid": "1",
                       "private": "0",
                       "display_period": "30",
                       "auto_start": "1",
                       "users": [],
                       "userGroups": [],
                       "pages": [
                           {
                               "dashboard_pageid": "1",
                               "name": "",
                               "display_period": "0",
                               "widgets": [
                                   {
                                       "widgetid": "9",
                                       "type": "systeminfo",
                                       "name": "",
                                       "x": "12",
                                       "y": "8",
                                       "width": "12",
                                       "height": "5",
                                       "view_mode": "0",
                                       "fields": []
                                   },
                                   {
                                       "widgetid": "8",
                                       "type": "problemsbysv",
                                       "name": "",
                                       "x": "12",
                                       "y": "4",
                                       "width": "12",
                                       "height": "4",
                                       "view_mode": "0",
                                       "fields": []
                                   },
                                   {
                                       "widgetid": "7",
                                       "type": "problemhosts",
                                       "name": "",
                                       "x": "12",
                                       "y": "0",
                                       "width": "12",
                                       "height": "4",
                                       "view_mode": "0",
                                       "fields": []
                                   },
                                   {
                                       "widgetid": "6",
                                       "type": "discovery",
                                       "name": "",
                                       "x": "6",
                                       "y": "9",
                                       "width": "18",
                                       "height": "4",
                                       "view_mode": "0",
                                       "fields": []
                                   },
                                   {
                                       "widgetid": "5",
                                       "type": "web",
                                       "name": "",
                                       "x": "0",
                                       "y": "9",
                                       "width": "18",
                                       "height": "4",
                                       "view_mode": "0",
                                       "fields": []
                                   },
                                   {
                                       "widgetid": "4",
                                       "type": "problems",
                                       "name": "",
                                       "x": "0",
                                       "y": "3",
                                       "width": "12",
                                       "height": "6",
                                       "view_mode": "0",
                                       "fields": []
                                   },
                                   {
                                       "widgetid": "3",
                                       "type": "favmaps",
                                       "name": "",
                                       "x": "8",
                                       "y": "0",
                                       "width": "12",
                                       "height": "3",
                                       "view_mode": "0",
                                       "fields": []
                                   },
                                   {
                                       "widgetid": "1",
                                       "type": "favgraphs",
                                       "name": "",
                                       "x": "0",
                                       "y": "0",
                                       "width": "12",
                                       "height": "3",
                                       "view_mode": "0",
                                       "fields": []
                                   }
                               ]
                           },
                           {
                               "dashboard_pageid": "2",
                               "name": "",
                               "display_period": "0",
                               "widgets": []
                           },
                           {
                               "dashboard_pageid": "3",
                               "name": "Custom page name",
                               "display_period": "60",
                               "widgets": []
                           }
                       ]
                   },
                   {
                       "dashboardid": "2",
                       "name": "My dashboard",
                       "userid": "1",
                       "private": "1",
                       "display_period": "60",
                       "auto_start": "1",
                       "users": [
                           {
                               "userid": "4",
                               "permission": "3"
                           }
                       ],
                       "userGroups": [
                           {
                               "usrgrpid": "7",
                               "permission": "2"
                           }
                       ],
                       "pages": [
                           {
                               "dashboard_pageid": "4",
                               "name": "",
                               "display_period": "0",
                               "widgets": [
                                   {
                                       "widgetid": "10",
                                       "type": "problems",
                                       "name": "",
                                       "x": "0",
                                       "y": "0",
                                       "width": "12",
                                       "height": "5",
                                       "view_mode": "0",
                                       "fields": [
                                           {
                                               "type": "2",
                                               "name": "groupids",
                                               "value": "4"
                                           }
                                       ]
                                   }
                               ]
                           }
                       ]
                   }
               ],
               "id": 1
           }

Copy

✔ Copied

### See also

  * [Dashboard page](object#dashboard-page)
  * [Dashboard widget](object#dashboard-widget)
  * [Dashboard widget field](object#dashboard-widget-field)
  * [Dashboard user](object#dashboard-user)
  * [Dashboard user group](object#dashboard-user-group)

### Source

CDashboard::get() in _ui/include/classes/api/services/CDashboard.php_.