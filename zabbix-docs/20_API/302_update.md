---
title: templatedashboard.update
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/templatedashboard/update
downloaded: 2025-11-14 10:44:55
---

# templatedashboard.update

### Description

`object templatedashboard.update(object/array templateDashboards)`

This method allows to update existing template dashboards.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` Template dashboard properties to be updated.

The `dashboardid` property must be specified for each dashboard, all other properties are optional. Only the specified properties will be updated.

Additionally to the [standard template dashboard properties](object#template-dashboard), the method accepts the following parameters.

pages | array | [Template dashboard pages](object#template-dashboard-page) to replace the existing dashboard pages.  
  
Dashboard pages are updated by the `dashboard_pageid` property. New dashboard pages will be created for objects without `dashboard_pageid` property and the existing dashboard pages will be deleted if not reused. Dashboard pages will be ordered in the same order as specified. Only the specified properties of the dashboard pages will be updated. At least one dashboard page object is required for `pages` property.  
---|---|---  
  
### Return values

`(object)` Returns an object containing the IDs of the updated template dashboards under the `dashboardids` property.

### Examples

#### Renaming a template dashboard

Rename a template dashboard to "Performance graphs".

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "templatedashboard.update",
               "params": {
                   "dashboardid": "23",
                   "name": "Performance graphs"
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
                       "23"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Updating template dashboard pages

Rename the first dashboard page, replace widgets on the second dashboard page and add a new page as the third one. Delete all other dashboard pages.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "templatedashboard.update",
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

### See also

  * [Template dashboard widget](object#template-dashboard-widget)
  * [Template dashboard widget field](object#template-dashboard-widget-field)

### Source

CTemplateDashboard::update() in _ui/include/classes/api/services/CTemplateDashboard.php_.