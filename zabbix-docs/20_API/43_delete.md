---
title: dashboard.delete
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/dashboard/delete
downloaded: 2025-11-14 10:40:36
---

# dashboard.delete

### Description

`object dashboard.delete(array dashboardids)`

This method allows to delete dashboards.

This method is available to users of any type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(array)` IDs of the dashboards to delete.

### Return values

`(object)` Returns an object containing the IDs of the deleted dashboards under the `dashboardids` property.

### Examples

#### Deleting multiple dashboards

Delete two dashboards.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "dashboard.delete",
               "params": [
                   "2",
                   "3"
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
                       "2",
                       "3"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CDashboard::delete() in _ui/include/classes/api/services/CDashboard.php_.