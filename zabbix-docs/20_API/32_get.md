---
title: connector.get
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/connector/get
downloaded: 2025-11-14 10:40:25
---

# connector.get

### Description

`integer/array connector.get(object parameters)`

The method allows to retrieve connector objects according to the given parameters.

This method is only available to _Super admin_ user type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object)` Parameters defining the desired output.

The method supports the following parameters.

connectorids | ID/array | Return only connectors with the given IDs.  
---|---|---  
selectTags | query | Return a `tags` property with connector [tag filter](/documentation/current/en/manual/api/reference/connector/object#tag-filter).  
  
Supports `count`.  
sortfield | string/array | Sort the result by the given properties.  
  
Possible values: `connectorid`, `name`, `data_type`, `status`.  
countOutput | boolean | These parameters are described in the [reference commentary](/documentation/current/en/manual/api/reference_commentary#common-get-method-parameters).  
excludeSearch | boolean  
filter | object  
limit | integer  
output | query  
preservekeys | boolean  
search | object  
searchByAny | boolean  
searchWildcardsEnabled | boolean  
sortorder | string/array  
startSearch | boolean  
  
### Return values

`(integer/array)` Returns either:

  * an array of objects;
  * the count of retrieved objects, if the `countOutput` parameter has been used.

### Examples

#### Retrieving all connectors

Retrieve all data about all connectors and their properties.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "connector.get",
               "params": {
                   "output": "extend",
                   "selectTags": ["tag", "operator", "value"],
                   "preservekeys": true
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": [
                   {
                       "connectorid": "1",
                       "name": "Export of item values",
                       "protocol": "0",
                       "data_type": "0",
                       "url": "{$DATA_EXPORT_VALUES_URL}",
                       "item_value_type": "31",
                       "authtype": "4",
                       "username": "{$DATA_EXPORT_VALUES_USERNAME}",
                       "password": "{$DATA_EXPORT_VALUES_PASSWORD}",
                       "token": "",
                       "max_records": "0",
                       "max_senders": "4",
                       "max_attempts": "2",
                       "attempt_interval": "10s",
                       "timeout": "10s",
                       "http_proxy": "{$DATA_EXPORT_VALUES_PROXY}",
                       "verify_peer": "1",
                       "verify_host": "1",
                       "ssl_cert_file": "{$DATA_EXPORT_VALUES_SSL_CERT_FILE}",
                       "ssl_key_file": "{$DATA_EXPORT_VALUES_SSL_KEY_FILE}",
                       "ssl_key_password": "",
                       "description": "",
                       "status": "1",
                       "tags_evaltype": "0",
                       "tags": [
                           {
                               "tag": "component",
                               "operator": "0",
                               "value": "memory"
                           }
                       ]
                   },
                   {
                       "connectorid": "2",
                       "name": "Export of events",
                       "protocol": "0",
                       "data_type": "1",
                       "url": "{$DATA_EXPORT_EVENTS_URL}",
                       "item_value_type": "31",
                       "authtype": "5",
                       "username": "",
                       "password": "",
                       "token": "{$DATA_EXPORT_EVENTS_BEARER_TOKEN}",
                       "max_records": "0",
                       "max_senders": "2",
                       "max_attempts": "1",
                       "attempt_interval": "5s",
                       "timeout": "5s",
                       "http_proxy": "",
                       "verify_peer": "1",
                       "verify_host": "1",
                       "ssl_cert_file": "",
                       "ssl_key_file": "",
                       "ssl_key_password": "",
                       "description": "",
                       "status": "1",
                       "tags_evaltype": "0",
                       "tags": [
                           {
                               "tag": "scope",
                               "operator": "0",
                               "value": "performance"
                           }
                       ]
                   }
               ],
               "id": 1
           }

Copy

✔ Copied

### Source

CConnector:get() in _ui/include/classes/api/services/CConnector.php_.