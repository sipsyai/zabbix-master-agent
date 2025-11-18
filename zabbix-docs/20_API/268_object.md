---
title: Service object
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/service/object
downloaded: 2025-11-14 10:44:21
---

# Service object

The following objects are directly related to the `service` API.

### Service

The service object has the following properties.

serviceid | ID | ID of the service.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
\- _required_ for update operations  
---|---|---  
algorithm | integer | Status calculation rule. Only applicable if child services exist.  
  
Possible values:  
0 - set status to OK;  
1 - most critical if all children have problems;  
2 - most critical of child services.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
name | string | Name of the service.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
sortorder | integer | Position of the service used for sorting.  
  
Possible values: 0-999.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
weight | integer | Service weight.  
  
Possible values: 0-1000000.  
  
Default: 0.  
propagation_rule | integer | Status propagation rule.  
  
Possible values:  
0 - _(default)_ propagate service status as is - without any changes;  
1 - increase the propagated status by a given `propagation_value` (by 1 to 5 severities);  
2 - decrease the propagated status by a given `propagation_value` (by 1 to 5 severities);  
3 - ignore this service - the status is not propagated to the parent service at all;  
4 - set fixed service status using a given `propagation_value`.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `propagation_value` is set  
propagation_value | integer | Status propagation value.  
  
Possible values if `propagation_rule` is set to "0" or "3":  
0 - Not classified.  
  
Possible values if `propagation_rule` is set to "1" or "2":  
1 - Information;  
2 - Warning;  
3 - Average;  
4 - High;  
5 - Disaster.  
  
Possible values if `propagation_rule` is set to "4":  
-1 - OK;  
0 - Not classified;  
1 - Information;  
2 - Warning;  
3 - Average;  
4 - High;  
5 - Disaster.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `propagation_rule` is set  
status | integer | Whether the service is in OK or problem state.  
  
If the service is in problem state, `status` is equal either to:  
\- the severity of the most critical problem;  
\- the highest status of a child service in problem state.  
  
If the service is in OK state, `status` is equal to: -1.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
description | string | Description of the service.  
uuid | string | Universal unique identifier, used for linking imported services to already existing ones. Auto-generated, if not given.  
created_at | integer | Unix timestamp when service was created.  
readonly | boolean | Access to the service.  
  
Possible values:  
0 - Read-write;  
1 - Read-only.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
  
### Status rule

The status rule object has the following properties.

type | integer | Condition for setting (New status) status.  
  
Possible values:  
0 - if at least (N) child services have (Status) status or above;  
1 - if at least (N%) of child services have (Status) status or above;  
2 - if less than (N) child services have (Status) status or below;  
3 - if less than (N%) of child services have (Status) status or below;  
4 - if weight of child services with (Status) status or above is at least (W);  
5 - if weight of child services with (Status) status or above is at least (N%);  
6 - if weight of child services with (Status) status or below is less than (W);  
7 - if weight of child services with (Status) status or below is less than (N%).  
  
Where:  
\- N (W) is `limit_value`;  
\- (Status) is `limit_status`;  
\- (New status) is `new_status`.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
limit_value | integer | Limit value.  
  
Possible values:  
\- for N and W: 1-100000;  
\- for N%: 1-100.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
limit_status | integer | Limit status.  
  
Possible values:  
-1 - OK;  
0 - Not classified;  
1 - Information;  
2 - Warning;  
3 - Average;  
4 - High;  
5 - Disaster.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
new_status | integer | New status value.  
  
Possible values:  
0 - Not classified;  
1 - Information;  
2 - Warning;  
3 - Average;  
4 - High;  
5 - Disaster.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
  
### Service tag

The service tag object has the following properties.

tag | string | Service tag name.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
value | string | Service tag value.  
  
### Service alarm

Service alarms cannot be directly created, updated or deleted via the Zabbix API.

The service alarm objects represent a service's state change. It has the following properties.

clock | timestamp | Time when the service state change has happened.  
---|---|---  
value | integer | Status of the service.  
  
Refer to the [service `status` property](object#service) for a list of possible values.  
  
### Problem tag

Problem tags allow linking services with problem events. The problem tag object has the following properties.

tag | string | Problem tag name.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
operator | integer | Mapping condition [operator](/documentation/current/en/manual/it_services/service_tree#service-configuration).  
  
Possible values:  
0 - _(default)_ Equals;  
2 - Contains.  
value | string | Problem tag value.