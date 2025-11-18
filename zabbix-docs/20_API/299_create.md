---
title: templatedashboard.create
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/templatedashboard/create
downloaded: 2025-11-14 10:44:52
---

# templatedashboard.create  
  
### Description

`object templatedashboard.create(object/array templateDashboards)`

This method allows to create new template dashboards.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` Template dashboards to create.

Additionally to the [standard template dashboard properties](object#template-dashboard), the method accepts the following parameters.

pages | array | [Template dashboard pages](/documentation/current/en/manual/api/reference/templatedashboard/object#template-dashboard-page) to be created for the dashboard. Dashboard pages will be ordered in the same order as specified.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
---|---|---  
  
### Return values

`(object)` Returns an object containing the IDs of the created template dashboards under the `dashboardids` property. The order of the returned IDs matches the order of the passed template dashboards.

### Examples

#### Creating a template dashboard

Create a template dashboard named “Graphs” with one Graph widget on a single dashboard page.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "templatedashboard.create",
               "params": {
                   "templateid": "10318",
                   "name": "Graphs",
                   "pages": [
                       {
                           "widgets": [
                               {
                                   "type": "graph",
                                   "x": 0,
                                   "y": 0,
                                   "width": 12,
                                   "height": 5,
                                   "view_mode": 0,
                                   "fields": [
                                       {
                                           "type": 6,
                                           "name": "graphid",
                                           "value": "1123"
                                       }
                                   ]
                               }
                           ]
           
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
                       "32"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### See also

  * [Template dashboard page](object#template-dashboard-page)
  * [Template dashboard widget](object#template-dashboard-widget)
  * [Template dashboard widget field](object#template-dashboard-widget-field)

### Source

CTemplateDashboard::create() in _ui/include/classes/api/services/CTemplateDashboard.php_.