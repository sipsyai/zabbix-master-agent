---
title: report.update
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/report/update
downloaded: 2025-11-14 10:44:04
---

# report.update

### Description

`object report.update(object/array reports)`

This method allows to update existing scheduled reports.

This method is only available to _Admin_ and _Super admin_ user type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` Scheduled report properties to be updated.

The `reportid` property must be defined for each scheduled report, all other properties are optional. Only the passed properties will be updated, all others will remain unchanged.

Additionally to the [standard scheduled report properties](object#report) the method accepts the following parameters.

users | object/array | [Users](object#users) to replace the current users assigned to the scheduled report.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_ if `user_groups` is not set  
---|---|---  
user_groups | object/array | [User groups](object#user-groups) to replace the current user groups assigned to the scheduled report.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_ if `users` is not set  
  
### Return values

`(object)` Returns an object containing the IDs of the updated scheduled reports under the `reportids` property.

### Examples

#### Disabling scheduled report

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "report.update",
               "params": {
                   "reportid": "1",
                   "status": "0"
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

CReport::update() in _ui/include/classes/api/services/CReport.php_.