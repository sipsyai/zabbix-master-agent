---
title: dashboard.create
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/dashboard/create
downloaded: 2025-11-14 10:40:35
---

# dashboard.create  
  
### Description

`object dashboard.create(object/array dashboards)`

This method allows to create new dashboards.

This method is available to users of any type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` Dashboards to create.

Additionally to the [standard dashboard properties](object#dashboard), the method accepts the following parameters.

pages | array | [Dashboard pages](object#dashboard-page) to be created for the dashboard. Dashboard pages will be ordered in the same order as specified.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
---|---|---  
users | array | [Dashboard user](object#dashboard-user) shares to be created on the dashboard.  
userGroups | array | [Dashboard user group](object#dashboard-user-group) shares to be created on the dashboard.  
  
### Return values

`(object)` Returns an object containing the IDs of the created dashboards under the `dashboardids` property. The order of the returned IDs matches the order of the passed dashboards.

### Examples

#### Creating a dashboard

Create a dashboard named "My dashboard" with one Problems widget with tags and using two types of sharing (user group and user) on a single dashboard page.

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
                                   "type": "problems",
                                   "x": 0,
                                   "y": 0,
                                   "width": 36,
                                   "height": 5,
                                   "view_mode": 0,
                                   "fields": [
                                       {
                                           "type": 1,
                                           "name": "tags.0.tag",
                                           "value": "service"
                                       },
                                       {
                                           "type": 0,
                                           "name": "tags.0.operator",
                                           "value": 1
                                       },
                                       {
                                           "type": 1,
                                           "name": "tags.0.value",
                                           "value": "zabbix_server"
                                       }
                                   ]
                               }
                           ]
                       }
                   ],
                   "userGroups": [
                       {
                           "usrgrpid": "7",
                           "permission": 2
                       }
                   ],
                   "users": [
                       {
                           "userid": "4",
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

CDashboard::create() in _ui/include/classes/api/services/CDashboard.php_.