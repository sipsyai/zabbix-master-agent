---
title: report.create
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/report/create
downloaded: 2025-11-14 10:44:01
---

# report.create  
  
### Description

`object report.create(object/array reports)`

This method allows to create new scheduled reports.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` Scheduled reports to create.

Additionally to the [standard scheduled report properties](object#report), the method accepts the following parameters.

users | object/array | [Users](object#users) to send the report to.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_ if `user_groups` is not set  
---|---|---  
user_groups | object/array | [User groups](object#user-groups) to send the report to.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_ if `users` is not set  
  
### Return values

`(object)` Returns an object containing the IDs of the created scheduled reports under the `reportids` property. The order of the returned IDs matches the order of the passed scheduled reports.

### Examples

#### Creating a scheduled report

Create a weekly report that will be prepared for the previous week every Monday-Friday at 12:00 from 2021-04-01 to 2021-08-31.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "report.create",
               "params": {
                   "userid": "1",
                   "name": "Weekly report",
                   "dashboardid": "1",
                   "period": "1",
                   "cycle": "1",
                   "start_time": "43200",
                   "weekdays": "31",
                   "active_since": "2021-04-01",
                   "active_till": "2021-08-31",
                   "subject": "Weekly report",
                   "message": "Report accompanying text",
                   "status": "1",
                   "description": "Report description",
                   "users": [
                       {
                           "userid": "1",
                           "access_userid": "1",
                           "exclude": "0"
                       },
                       {
                           "userid": "2",
                           "access_userid": "0",
                           "exclude": "1"
                       }
                   ],
                   "user_groups": [
                       {
                           "usrgrpid": "7",
                           "access_userid": "0"
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
                   "reportids": [
                       "1"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### See also

  * [Users](object#users)
  * [User groups](object#user-groups)

### Source

CReport::create() in _ui/include/classes/api/services/CReport.php_.