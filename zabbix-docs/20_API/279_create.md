---
title: sla.create
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/sla/create
downloaded: 2025-11-14 10:44:32
---

# sla.create  
  
### Description

`object sla.create(object/array SLAs)`

This method allows to create new SLA objects.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` SLA objects to create.

Additionally to the [standard SLA properties](object#sla), the method accepts the following parameters.

service_tags | array | [SLA service tags](/documentation/current/en/manual/api/reference/sla/object#sla-service-tag) to be created for the SLA.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
---|---|---  
schedule | array | [SLA schedule](/documentation/current/en/manual/api/reference/sla/object#sla-schedule) to be created for the SLA.  
Specifying an empty parameter will be interpreted as a 24x7 schedule.  
Default: 24x7 schedule.  
excluded_downtimes | array | [SLA excluded downtimes](/documentation/current/en/manual/api/reference/sla/object#sla-excluded-downtime) to be created for the SLA.  
  
### Return values

`(object)` Returns an object containing the IDs of the created SLAs under the `slaids` property. The order of the returned IDs matches the order of the passed SLAs.

### Examples

#### Creating an SLA

Instruct to create an SLA entry for: * tracking uptime for SQL-engine related services; * custom schedule of all weekdays excluding last hour on Saturday; * an effective date of the last day of the year 2022; * with 1 hour and 15 minutes long planned downtime starting at midnight on the 4th of July; * SLA weekly report calculation will be on; * the minimum acceptable SLO will be 99.9995%.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "sla.create",
               "params": [
                   {
                       "name": "Database Uptime",
                       "slo": "99.9995",
                       "period": "1",
                       "timezone": "America/Toronto",
                       "description": "Provide excellent uptime for main database engines.",
                       "effective_date": 1672444800,
                       "status": 1,
                       "schedule": [
                           {
                               "period_from": 0,
                               "period_to": 601200
                           }
                       ],
                       "service_tags": [
                           {
                               "tag": "database",
                               "operator": "0",
                               "value": "mysql"
                           },
                           {
                               "tag": "database",
                               "operator": "0",
                               "value": "postgresql"
                           }
                       ],
                       "excluded_downtimes": [
                           {
                               "name": "Software version upgrade rollout",
                               "period_from": "1648760400",
                               "period_to": "1648764900"
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

### Source

CSla::create() in _ui/include/classes/api/services/CSla.php_.