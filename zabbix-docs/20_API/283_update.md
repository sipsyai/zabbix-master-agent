---
title: sla.update
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/sla/update
downloaded: 2025-11-14 10:44:36
---

# sla.update

### Description

`object sla.update(object/array slaids)`

This method allows to update existing SLA entries.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` SLA properties to be updated.

The `slaid` property must be defined for each SLA, all other properties are optional. Only the passed properties will be updated, all others will remain unchanged.

Additionally to the [standard SLA properties](object#sla), the method accepts the following parameters.

service_tags | array | [SLA service tags](/documentation/current/en/manual/api/reference/sla/object#sla-service-tag) to replace the current SLA service tags.  
---|---|---  
schedule | array | [SLA schedule](/documentation/current/en/manual/api/reference/sla/object#sla-schedule) to replace the current one.  
Specifying parameter as empty will be interpreted as a 24x7 schedule.  
excluded_downtimes | array | [SLA excluded downtimes](/documentation/current/en/manual/api/reference/sla/object#sla-excluded-downtime) to replace the current ones.  
  
### Return values

`(object)` Returns an object containing the IDs of the updated SLAs under the `slaids` property.

### Examples

#### Updating service tags

Make SLA with ID "5" to be calculated at monthly intervals for NoSQL related services, without changing its schedule or excluded downtimes; set SLO to 95%.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "sla.update",
               "params": [
                   {
                       "slaid": "5",
                       "name": "NoSQL Database engines",
                       "slo": "95",
                       "period": 2,
                       "service_tags": [
                           {
                               "tag": "database",
                               "operator": "0",
                               "value": "redis"
                           },
                           {
                               "tag": "database",
                               "operator": "0",
                               "value": "mongodb"
                           }
                       ]
                   }
               ],
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "slaids": [
                       "5"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Changing the schedule of an SLA

Switch the SLA with ID "5" to a 24x7 schedule.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "sla.update",
               "params": {
                   "slaid": "5",
                   "schedule": []
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "slaids": [
                       "5"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Changing the excluded downtimes for an SLA

Add a planned 4 hour long RAM upgrade downtime on the 6th of April, 2022, while keeping (needs to be defined anew) a previously existing software upgrade planned on the 4th of July for the SLA with ID "5".

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "sla.update",
               "params": {
                   "slaid": "5",
                   "excluded_downtimes": [
                       {
                           "name": "Software version upgrade rollout",
                           "period_from": "1648760400",
                           "period_to": "1648764900"
                       },
                       {
                           "name": "RAM upgrade",
                           "period_from": "1649192400",
                           "period_to": "1649206800"
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
                   "slaids": [
                       "5"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CSla::update() in _ui/include/classes/api/services/CSla.php_.