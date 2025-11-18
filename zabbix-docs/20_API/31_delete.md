---
title: connector.delete
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/connector/delete
downloaded: 2025-11-14 10:40:24
---

# connector.delete

### Description

`object connector.delete(array connectorids)`

This method allows to delete connector entries.

This method is only available to _Super admin_ user type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(array)` IDs of the connectors to delete.

### Return values

`(object)` Returns an object containing the IDs of the deleted connectors under the `connectorids` property.

### Examples

#### Deleting multiple connectors

Delete two connector entries.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "connector.delete",
               "params": [
                   3,
                   5
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
                       "3",
                       "5"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CConnector::delete() in _ui/include/classes/api/services/CConnector.php_.