---
title: connector.create
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/connector/create
downloaded: 2025-11-14 10:40:23
---

# connector.create  
  
### Description

`object connector.create(object/array connectors)`

This method allows to create new connector objects.

This method is only available to _Super admin_ user type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` Connector objects to create.

Additionally to the [standard connector properties](object#connector), the method accepts the following parameters.

tags | array | Connector [tag filter](/documentation/current/en/manual/api/reference/connector/object#tag-filter).  
---|---|---  
  
### Return values

`(object)` Returns an object containing the IDs of the created connectors under the `connectorids` property. The order of the returned IDs matches the order of the passed connectors.

### Examples

#### Creating a connector

Create a connector to export trigger events with a tag filter. HTTP authentication will be performed using Bearer token.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "connector.create",
               "params": [
                   {
                       "name": "Export of events",
                       "data_type": 1,
                       "url": "{$DATA_EXPORT_URL}",
                       "authtype": 5,
                       "token": "{$DATA_EXPORT_BEARER_TOKEN}",
                       "tags": [
                           {
                               "tag": "service",
                               "operator": 0,
                               "value": "mysqld"
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
                   "connectorid": [
                       "3"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CConnector::create() in _ui/include/classes/api/services/CConnector.php_.