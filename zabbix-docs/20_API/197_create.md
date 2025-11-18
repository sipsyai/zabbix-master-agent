---
title: maintenance.create
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/maintenance/create
downloaded: 2025-11-14 10:43:10
---

# maintenance.create  
  
### Description

`object maintenance.create(object/array maintenances)`

This method allows to create new maintenances.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` Maintenances to create.

Additionally to the [standard maintenance properties](object#maintenance), the method accepts the following parameters.

groups | object/array | [Host groups](/documentation/current/en/manual/api/reference/hostgroup/object) that will undergo maintenance.  
  
The host groups must have only the `groupid` property defined.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_ if `hosts` is not set  
---|---|---  
hosts | object/array | [Hosts](/documentation/current/en/manual/api/reference/host/object) that will undergo maintenance.  
  
The hosts must have only the `hostid` property defined.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_ if `groups` is not set  
timeperiods | object/array | Maintenance [time periods](/documentation/current/en/manual/api/reference/maintenance/object#time-period).  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
tags | object/array | [Problem tags](/documentation/current/en/manual/api/reference/maintenance/object#problem-tag).  
  
Define what problems must be suppressed.  
If no tags are given, all active maintenance host problems will be suppressed.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if `maintenance_type` of [Maintenance object](object#maintenance) is set to "with data collection"  
  
### Return values

`(object)` Returns an object containing the IDs of the created maintenances under the `maintenanceids` property. The order of the returned IDs matches the order of the passed maintenances.

### Examples

#### Creating a maintenance

Create a maintenance with data collection for host group with ID "2" and with problem tags **service:mysqld** and **error**. It must be active from 22.01.2013 till 22.01.2014, come in effect each Sunday at 18:00 and last for one hour.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "maintenance.create",
               "params": {
                   "name": "Sunday maintenance",
                   "active_since": 1358844540,
                   "active_till": 1390466940,
                   "tags_evaltype": 0,
                   "groups": [
                       {"groupid": "2"}
                   ],
                   "timeperiods": [
                       {
                           "period": 3600,
                           "timeperiod_type": 3,
                           "start_time": 64800,
                           "every": 1,
                           "dayofweek": 64
                       }
                   ],
                   "tags": [
                       {
                           "tag": "service",
                           "operator": "0",
                           "value": "mysqld"
                       },
                       {
                           "tag": "error",
                           "operator": "2",
                           "value": ""
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
                   "maintenanceids": [
                       "3"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### See also

  * [Time period](object#time-period)

### Source

CMaintenance::create() in _ui/include/classes/api/services/CMaintenance.php_.