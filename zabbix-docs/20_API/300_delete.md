---
title: templatedashboard.delete
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/templatedashboard/delete
downloaded: 2025-11-14 10:44:53
---

# templatedashboard.delete

### Description

`object templatedashboard.delete(array templateDashboardIds)`

This method allows to delete template dashboards.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(array)` IDs of the template dashboards to delete.

### Return values

`(object)` Returns an object containing the IDs of the deleted template dashboards under the `dashboardids` property.

### Examples

#### Deleting multiple template dashboards

Delete two template dashboards.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "templatedashboard.delete",
               "params": [
                   "45",
                   "46"
               ],
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "dashboardids": [
                       "45",
                       "46"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CTemplateDashboard::delete() in _ui/include/classes/api/services/CTemplateDashboard.php_.