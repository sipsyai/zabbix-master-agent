---
title: sla.getsli
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/sla/getsli
downloaded: 2025-11-14 10:44:35
---

# sla.getsli

### Description

`object sla.getsli(object parameters)`

This method allows to calculate the Service Level Indicator (SLI) data for a Service Level Agreement (SLA).

This method is available to users of any type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object)` Parameters containing the SLA ID, reporting periods and, optionally, the IDs of the services - to calculate the SLI for.

slaid | ID | ID of the SLA to return availability information for.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
---|---|---  
period_from | timestamp | Starting timestamp (inclusive) to report the SLI for.  
  
Possible values: Unix timestamp.  
period_to | timestamp | Ending timestamp (inclusive) to report the SLI for.  
  
Possible values: Unix timestamp.  
periods | integer | Number of periods to report.  
  
Possible values: 1-100  
serviceids | ID/array | IDs of services to return the SLI for.  
  
#### Partitioning of periods

The following table demonstrates the arrangement of returned period slices based on combinations of parameters.

Returned periods do not precede the first available period (based on the effective date of the SLA) and do not exceed the current period.

**period_from** | **period_to** | **periods** |   
---|---|---|---  
- | - | - | Last 20 periods, including the current one.  
- | - | N | Last N periods.  
- | specified | - | Last 20 periods before `period_to`.  
- | specified | N | Last N periods before `period_to`.  
specified | - | - | First 20 periods starting with `period_from`.  
specified | - | N | First N periods starting with `period_from`.  
specified | specified | - | Up to 100 periods in the specified range.  
specified | specified | N | N periods in the specified range.  
  
### Return values

`(object)` Returns the results of the calculation.

periods | array | List of the reported periods.  
  
Each reported period is represented as an object consisting of:  
\- `period_from` \- `(timestamp)` Starting timestamp (inclusive) of the reported period.  
\- `period_to` \- `(timestamp)` Ending timestamp (exclusive) of the reported period.  
  
Periods are sorted by `period_from`, with earliest periods appearing first.  
---|---|---  
serviceids | array | List of service IDs in the reported periods.  
  
The sorting order of the list is not defined. Even if `serviceids` parameter was passed to the `sla.getsli` method.  
sli | array | SLI data (as a **two-dimensional array**) for each reported period and service.  
  
The index of the `periods` property is used as the **first** dimension of the `sli` property.  
  
The index of the `serviceids` property is used as the **second** dimension of the `sli` property.  
  
#### SLI data

The SLI data returned for each reported period and service consists of:

uptime | integer | Amount of time service spent in an _OK_ state during scheduled uptime, less the excluded downtimes.  
---|---|---  
downtime | integer | Amount of time service spent in a _not OK_ state during scheduled uptime, less the excluded downtimes.  
sli | float | SLI (per cent of total uptime), based on uptime and downtime.  
error_budget | integer | Error budget (in seconds), based on the SLI and the SLO.  
excluded_downtimes | array | Array of excluded downtimes in this reporting period.  
  
Each object will contain the following parameters:  
\- `name` \- `(string)` Name of the excluded downtime.  
\- `period_from` \- `(timestamp)` Starting timestamp (inclusive) of the excluded downtime.  
\- `period_to` \- `(timestamp)` Ending timestamp (exclusive) of the excluded downtime.  
  
Excluded downtimes are sorted by `period_from`, with earliest periods appearing first.  
  
### Examples

#### Calculating SLI for a daily SLA

Retrieve SLI data for services with IDs "1" and "4" that are linked to the SLA with ID "1". Retrieve data for a single period until "1761861599" (Oct 30 2025 23:59:59 GMT+0200). Since the [reporting period](/documentation/current/en/manual/it_services/sla) of the SLA is daily, SLI data is retrieved from "1761775200" (Oct 30 2025 00:00:00 GMT+0200) to "1761861600" (Oct 31 2025 00:00:00 GMT+0200).

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "sla.getsli",
               "params": {
                   "slaid": "1",
                   "serviceids": [
                       1,
                       4
                   ],
                   "periods": 1,
                   "period_to": 1761861599,
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "periods": [
                       {
                           "period_from": 1761775200,
                           "period_to": 1761861600
                       }
                   ],
                   "serviceids": [
                       1,
                       4
                   ],
                   "sli": [
                       [
                           {
                               "uptime": 43843,
                               "downtime": 0,
                               "sli": 100,
                               "error_budget": 0,
                               "excluded_downtimes": [
                                   {
                                       "name": "Maintenance OCT",
                                       "period_from": 1761825600,
                                       "period_to": 1761829200
                                   }
                               ]
                           },
                           {
                               "uptime": 32225,
                               "downtime": 0,
                               "sli": 100,
                               "error_budget": 0,
                               "excluded_downtimes": []
                           }
                       ]
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Calculating SLI for a monthly SLA

Retrieve SLI data on services with IDs "50", "60" and "70" that are linked to the SLA with ID "5". Retrieve data for three periods starting from "1635724800" (Nov 01 2021 00:00:00 UTC). Since the [reporting period](/documentation/current/en/manual/it_services/sla) of the SLA is monthly, SLI data is retrieved for the following three months:

  * From "1635724800" (Nov 01 2021 00:00:00 UTC) to "1638316800" (Dec 01 2021 00:00:00 UTC)
  * From "1638316800" (Dec 01 2021 00:00:00 UTC) to "1640995200" (Jan 01 2022 00:00:00 UTC)
  * From "1640995200" (Jan 01 2022 00:00:00 UTC) to "1643673600" (Feb 01 2022 00:00:00 UTC)

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "sla.getsli",
               "params": {
                   "slaid": "5",
                   "serviceids": [
                       50,
                       60,
                       70
                   ],
                   "periods": 3,
                   "period_from": "1635724800"
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "periods": [
                       {
                           "period_from": 1635724800,
                           "period_to": 1638316800
                       },
                       {
                           "period_from": 1638316800,
                           "period_to": 1640995200
                       },
                       {
                           "period_from": 1640995200,
                           "period_to": 1643673600
                       }
                   ],
                   "serviceids": [
                       50,
                       60,
                       70
                   ],
                   "sli": [
                       [
                           {
                               "uptime": 1186212,
                               "downtime": 0,
                               "sli": 100,
                               "error_budget": 0,
                               "excluded_downtimes": [
                                   {
                                       "name": "Maintenance Nov 25 - Dec 01",
                                       "period_from": 1637836212,
                                       "period_to": 1638316800
                                   }
                               ]
                           },
                           {
                               "uptime": 1186212,
                               "downtime": 0,
                               "sli": 100,
                               "error_budget": 0,
                               "excluded_downtimes": [
                                   {
                                       "name": "Maintenance Nov 25 - Dec 01",
                                       "period_from": 1637836212,
                                       "period_to": 1638316800
                                   }
                               ]
                           },
                           {
                               "uptime": 1186212,
                               "downtime": 0,
                               "sli": 100,
                               "error_budget": 0,
                               "excluded_downtimes": [
                                   {
                                       "name": "Maintenance Nov 25 - Dec 01",
                                       "period_from": 1637836212,
                                       "period_to": 1638316800
                                   }
                               ]
                           }
                       ],
                       [
                           {
                               "uptime": 1147548,
                               "downtime": 0,
                               "sli": 100,
                               "error_budget": 0,
                               "excluded_downtimes": [
                                   {
                                       "name": "Maintenance Dec 02 - Dec 10",
                                       "period_from": 1638439200,
                                       "period_to": 1639109652
                                   }
                               ]
                           },
                           {
                               "uptime": 1147548,
                               "downtime": 0,
                               "sli": 100,
                               "error_budget": 0,
                               "excluded_downtimes": [
                                   {
                                       "name": "Maintenance Dec 02 - Dec 10",
                                       "period_from": 1638439200,
                                       "period_to": 1639109652
                                   }
                               ]
                           },
                           {
                               "uptime": 1147548,
                               "downtime": 0,
                               "sli": 100,
                               "error_budget": 0,
                               "excluded_downtimes": [
                                   {
                                       "name": "Maintenance Dec 02 - Dec 10",
                                       "period_from": 1638439200,
                                       "period_to": 1639109652
                                   }
                               ]
                           }
                       ],
                       [
                           {
                               "uptime": 1674000,
                               "downtime": 0,
                               "sli": 100,
                               "error_budget": 0,
                               "excluded_downtimes": []
                           },
                           {
                               "uptime": 1674000,
                               "downtime": 0,
                               "sli": 100,
                               "error_budget": 0,
                               "excluded_downtimes": []
                           },
                           {
                               "uptime": 1674000,
                               "downtime": 0,
                               "sli": 100,
                               "error_budget": 0,
                               "excluded_downtimes": []
                           }
                       ]
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CSla::getSli() in _ui/include/classes/api/services/CSla.php_