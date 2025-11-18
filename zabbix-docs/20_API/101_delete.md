---
title: graph.delete
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/graph/delete
downloaded: 2025-11-14 10:41:35
---

# graph.delete

### Description

`object graph.delete(array graphIds)`

This method allows to delete graphs.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(array)` IDs of the graphs to delete.

### Return values

`(object)` Returns an object containing the IDs of the deleted graphs under the `graphids` property.

### Examples

#### Deleting multiple graphs

Delete two graphs.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "graph.delete",
               "params": [
                   "652",
                   "653"
               ],
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "graphids": [
                       "652",
                       "653"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CGraph::delete() in _ui/include/classes/api/services/CGraph.php_.