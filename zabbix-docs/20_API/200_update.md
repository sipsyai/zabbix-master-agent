---
title: maintenance.update
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/maintenance/update
downloaded: 2025-11-14 10:43:13
---

# maintenance.update

### Description

`object maintenance.update(object/array maintenances)`

This method allows to update existing maintenances.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` Maintenance properties to be updated.

The `maintenanceid` property must be defined for each maintenance, all other properties are optional. Only the passed properties will be updated, all others will remain unchanged.

Additionally to the [standard maintenance properties](object#maintenance), the method accepts the following parameters.

groups | object/array | [Host groups](/documentation/current/en/manual/api/reference/hostgroup/object) to replace the current groups.  
  
The host groups must have only the `groupid` property defined.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_ if `hosts` is not set  
---|---|---  
hosts | object/array | [Hosts](/documentation/current/en/manual/api/reference/host/object) to replace the current hosts.  
  
The hosts must have only the `hostid` property defined.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_ if `groups` is not set  
timeperiods | object/array | Maintenance [time periods](/documentation/current/en/manual/api/reference/maintenance/object#time-period) to replace the current periods.  
tags | object/array | [Problem tags](/documentation/current/en/manual/api/reference/maintenance/object#problem-tag) to replace the current tags.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if `maintenance_type` of [Maintenance object](object#maintenance) is set to "with data collection"  
  
### Return values

`(object)` Returns an object containing the IDs of the updated maintenances under the `maintenanceids` property.

### Examples

#### Assigning different hosts

Replace the hosts currently assigned to maintenance with two different ones.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "maintenance.update",
               "params": {
                   "maintenanceid": "3",
                   "hosts": [
                       {"hostid": "10085"},
                       {"hostid": "10084"}
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

CMaintenance::update() in _ui/include/classes/api/services/CMaintenance.php_.