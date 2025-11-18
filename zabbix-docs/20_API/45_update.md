---
title: dashboard.update
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/dashboard/update
downloaded: 2025-11-14 10:40:38
---

# dashboard.update

### Description

`object dashboard.update(object/array dashboards)`

This method allows to update existing dashboards.

This method is available to users of any type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` Dashboard properties to be updated.

The `dashboardid` property must be defined for each dashboard, all other properties are optional. Only the passed properties will be updated, all others will remain unchanged.

Additionally to the [standard dashboard properties](object#dashboard), the method accepts the following parameters.

pages | array | [Dashboard pages](object#dashboard-page) to replace the existing dashboard pages.  
  
Dashboard pages are updated by the `dashboard_pageid` property. New dashboard pages will be created for objects without `dashboard_pageid` property and the existing dashboard pages will be deleted if not reused. Dashboard pages will be ordered in the same order as specified. Only the specified properties of the dashboard pages will be updated.  
---|---|---  
users | array | [Dashboard user](object#dashboard-user) shares to replace the existing elements.  
userGroups | array | [Dashboard user group](object#dashboard-user-group) shares to replace the existing elements.  
  
### Return values

`(object)` Returns an object containing the IDs of the updated dashboards under the `dashboardids` property.

### Examples

#### Renaming a dashboard

Rename a dashboard to "SQL server status".

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "dashboard.update",
               "params": {
                   "dashboardid": "2",
                   "name": "SQL server status"
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
                       "2"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Updating dashboard pages

Rename the first dashboard page, replace widgets on the second dashboard page and add a new page as the third one. Delete all other dashboard pages.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "dashboard.update",
               "params": {
                   "dashboardid": "2",
                   "pages": [
                       {
                           "dashboard_pageid": 1,
                           "name": "Renamed Page"
                       },
                       {
                           "dashboard_pageid": 2,
                           "widgets": [
                               {
                                   "type": "clock",
                                   "x": 0,
                                   "y": 0,
                                   "width": 12,
                                   "height": 3
                               }
                           ]
                       },
                       {
                           "display_period": 60
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
                       "2"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Change dashboard owner

Available only for admins and super admins.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "dashboard.update",
               "params": {
                   "dashboardid": "2",
                   "userid": "1"
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
                       "2"
                   ]
               },
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

CDashboard::update() in _ui/include/classes/api/services/CDashboard.php_.