---
title: Task object
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/task/object
downloaded: 2025-11-14 10:44:38
---

# Task object

The following objects are directly related to the `task` API.

### Task

The task object has the following properties:

taskid | ID | ID of the task.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
---|---|---  
type | integer | Type of the task.  
  
Possible values:  
1 - Diagnostic information;  
2 - Refresh proxy configuration;  
6 - Execute now.  
  
Since Zabbix 7.4.3, _Admin_ and _User_ type users may create 'Execute now' tasks.  
  
Note that `task.get` always returns "7" (Task execution summary).  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
status | integer | Status of the task.  
  
Possible values:  
1 - new task;  
2 - task in progress;  
3 - task is completed;  
4 - task is expired.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
clock | timestamp | Time when the task was created.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
ttl | integer | The time in seconds after which task expires.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
proxyid | ID | ID of the proxy about which diagnostic information statistic is collected.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `type` is set to "Diagnostic information" or "Refresh proxy configuration"  
request | object | Task request object according to the task type:  
Object of 'Execute now' task is [described in detail below](/documentation/current/en/manual/api/reference/task/object#check-now-request-object);  
Object of 'Refresh proxy configuration' task is [described in detail below](/documentation/current/en/manual/api/reference/task/object#refresh-proxy-configuration);  
Object of 'Diagnostic information' task is [described in detail below](/documentation/current/en/manual/api/reference/task/object#diagnostic-information-request-object).  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
result | object | Result object of the diagnostic information task.  
May contain NULL if result is not yet ready.  
Result object is [described in detail below](/documentation/current/en/manual/api/reference/task/object#statistic-result-object).  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
  
#### 'Execute now' request object

The 'Execute now' task request object has the following properties.

itemid | ID | ID of item and low-level discovery rules.  
  
Since Zabbix 7.4.3, _Admin_ and _User_ type users may 'Execute now' items on hosts for which they have _read-write_ [permission](/documentation/current/en/manual/api/reference/usergroup/object#permission), or _read_ permission and `invoke_execute_now` [action](/documentation/current/en/manual/api/reference/role/object#action) enabled for their role. The same applies to _Admin_ type users for low-level discovery (LLD) rules.  
---|---|---  
  
#### 'Refresh proxy configuration' request object

The 'Refresh proxy configuration' task request object has the following properties.

proxyids | array | Proxy IDs.  
---|---|---  
  
#### 'Diagnostic information' request object

The diagnostic information task request object has the following properties. Statistic request object for all types of properties is [described in detail below](/documentation/current/en/manual/api/reference/task/object#statistic-request-object).

historycache | object | History cache statistic request. Available on server and proxy.  
---|---|---  
valuecache | object | Items cache statistic request. Available on server.  
preprocessing | object | Preprocessing manager statistic request. Available on server and proxy.  
alerting | object | Alert manager statistic request. Available on server.  
lld | object | LLD manager statistic request. Available on server.  
  
##### Statistic request object

Statistic request object is used to define what type of information should be collected about server/proxy internal processes. It has the following properties.

stats | query | Statistic object properties to be returned.  
The list of available fields for each type of diagnostic information statistic are [described in detail below](object#list-of-statistic-fields-available-for-each-type-of-diagnostic-information-request).  
  
Default: `extend` will return all available statistic fields.  
---|---|---  
top | object | Object to sort and limit returned statistic values.  
The list of available fields for each type of diagnostic information statistic are [described in detail below](object#list-of-sorting-fields-available-for-each-type-of-diagnostic-information-request).  
  
Example: { “source.alerts”: 10 }  
  
###### List of statistic fields available for each type of diagnostic information request

Following statistic fields can be requested for each type of diagnostic information request property.

historycache | items | Number of cached items.  
---|---|---  
values | Number of cached values.  
memory | Shared memory statistics (free space, number of used chunks, number of free chunks, max size of free chunk).  
memory.data | History data cache shared memory statistics.  
memory.index | History index cache shared memory statistics.  
valuecache | items | Number of cached items.  
values | Number of cached values.  
memory | Shared memory statistics (free space, number of used chunks, number of free chunks, max size of free chunk).  
mode | Value cache mode.  
preprocessing | values | Number of queued values.  
preproc.values | Number of queued values with preprocessing steps.  
alerting | alerts | Number of queued alerts.  
lld | rules | Number of queued rules.  
values | Number of queued values.  
  
###### List of sorting fields available for each type of diagnostic information request

Following statistic fields can be used to sort and limit requested information.

historycache | values | integer  
---|---|---  
valuecache | values | integer  
request.values | integer  
preprocessing | values | integer  
alerting | media.alerts | integer  
source.alerts | integer  
lld | values | integer  
  
##### Statistic result object

Statistic result object is retrieved in `result` field of task object.

status | integer | Status of the task result.  
  
Possible values:  
-1 - error occurred during performing task;  
0 - task result is created.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
---|---|---  
data | string/object | Results according the statistic request object of particular diagnostic information task.  
Contains error message string if error occurred during performing task.