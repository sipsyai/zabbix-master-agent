---
title: task.create
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/task/create
downloaded: 2025-11-14 10:44:39
---

# task.create  
  
### Description

`object task.create(object/array tasks)`

This method allows to create tasks.

This method is available to users of any type (to _Admin_ and _User_ type users since Zabbix 7.4.3). Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` A task to create.

The method accepts tasks with the [standard task properties](object#task-object).

Note that 'Execute now' tasks can be created only for the following types of items/discovery rules:

  * Zabbix agent (passive)
  * Simple check
  * SNMP agent (v1/v2/v3)
  * Zabbix internal
  * External check
  * Database monitor
  * HTTP agent
  * IPMI agent
  * SSH agent
  * TELNET agent
  * JMX agent
  * Calculated
  * Dependent item
  * Script
  * Browser

If the item/discovery rule is of type "Dependent item", then its master item must also be one of the above types.

### Return values

`(object)` Returns an object containing the IDs of the created tasks under the `taskids` property. One task is created for each item and low-level discovery rule. The order of the returned IDs matches the order of the passed `itemids`.

### Examples

#### Creating a task

Create an 'Execute now' task for an item and a low-level discovery rule.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "task.create",
               "params": [
                   {
                       "type": 6,
                       "request": {
                           "itemid": "10092"
                       }
                   },
                   {
                       "type": 6,
                       "request": {
                           "itemid": "10093"
                       }
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
                   "taskids": [
                       "1",
                       "2"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

Create a 'Refresh proxy configuration' task for two proxies.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "task.create",
               "params": [
                   {
                       "type": 2,
                       "request": {
                           "proxyids": ["10459", "10460"]
                       }
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
                   "taskids": [
                       "1"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

Create a 'Diagnostic information' task.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "task.create",
               "params": [
                   {
                       "type": 1,
                       "request": {
                           "alerting": {
                               "stats": [
                                   "alerts"
                               ],
                               "top": {
                                   "media.alerts": 10
                               }
                           },
                           "lld": {
                               "stats": "extend",
                               "top": {
                                   "values": 5
                               }
                           }
                       },
                       "proxyid": 0
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
                   "taskids": [
                       "3"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### See also

  * [Task](/documentation/current/en/manual/api/reference/task/object)
  * ['Execute now' request object](/documentation/current/en/manual/api/reference/task/object#execute-now-request-object)
  * ['Refresh proxy configuration' request object](/documentation/current/en/manual/api/reference/task/object#refresh-proxy-configuration-request-object)
  * ['Diagnostic information' request object](/documentation/current/en/manual/api/reference/task/object#diagnostic-information-request-object)

### Source

CTask::create() in _ui/include/classes/api/services/CTask.php_.