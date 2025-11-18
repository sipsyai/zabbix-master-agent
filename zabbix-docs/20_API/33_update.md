---
title: connector.update
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/connector/update
downloaded: 2025-11-14 10:40:26
---

# connector.update

### Description

`object connector.update(object/array connectors)`

This method allows to update existing connectors.

This method is only available to _Super admin_ user type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` Connector properties to be updated.

The `connectorid` property must be defined for each connector, all other properties are optional. Only the passed properties will be updated, all others will remain unchanged.

Additionally to the [standard connector properties](object#connector), the method accepts the following parameters.

tags | array | Connector [tag filter](/documentation/current/en/manual/api/reference/connector/object#tag-filter) to replace the current tag filter.  
---|---|---  
  
### Return values

`(object)` Returns an object containing the IDs of the updated connectors under the `connectorids` property.

### Examples

#### Changing HTTP authentication type

Change HTTP authentication type to Bearer for connector with ID "3".

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "connector.update",
               "params": {
                   "connectorid": 3,
                   "authtype": 5,
                   "token": "{$DATA_EXPORT_BEARER_TOKEN}"
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "connectorids": [
                       "3"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Updating tag filter

Change tag filter for connector with ID "5".

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "connector.update",
               "params": [
                   {
                       "connectorid": 5,
                       "tags_evaltype": 2,
                       "tags": [
                           {
                               "tag": "service",
                               "operator": 0,
                               "value": "mysqld"
                           },
                           {
                               "tag": "error",
                               "operator": 12,
                               "value": ""
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
                   "connectorids": [
                       "5"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CConnector::update() in _ui/include/classes/api/services/CConnector.php_.