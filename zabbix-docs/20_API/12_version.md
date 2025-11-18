---
title: apiinfo.version
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/apiinfo/version
downloaded: 2025-11-14 10:40:05
---

# apiinfo.version

### Description

`string apiinfo.version(array)`

This method allows to retrieve the version of the Zabbix API.

This method is only available to unauthenticated users.

### Parameters

`(array)` The method accepts an empty array.

### Return values

`(string)` Returns the version of the Zabbix API.

Starting from Zabbix 2.0.4 the version of the API matches the version of Zabbix.

### Examples

#### Retrieving the version of the API

Retrieve the version of the Zabbix API.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "apiinfo.version",
               "params": [],
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": "7.4.0",
               "id": 1
           }

Copy

✔ Copied

### Source

CAPIInfo::version() in _ui/include/classes/api/services/CAPIInfo.php_.