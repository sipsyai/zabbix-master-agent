---
title: graph.update
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/graph/update
downloaded: 2025-11-14 10:41:37
---

# graph.update

### Description

`object graph.update(object/array graphs)`

This method allows to update existing graphs.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` Graph properties to be updated.

The `graphid` property must be defined for each graph, all other properties are optional. Only the passed properties will be updated, all others will remain unchanged.

Additionally to the [standard graph properties](object#graph) the method accepts the following parameters.

gitems | array | [Graph items](/documentation/current/en/manual/api/reference/graphitem/object) to replace existing graph items. If a graph item has the `gitemid` property defined it will be updated, otherwise a new graph item will be created.  
---|---|---  
  
### Return values

`(object)` Returns an object containing the IDs of the updated graphs under the `graphids` property.

### Examples

#### Setting the maximum for the Y scale

Set the maximum of the Y scale to a fixed value of 100.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "graph.update",
               "params": {
                   "graphid": "439",
                   "ymax_type": 1,
                   "yaxismax": 100
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "graphids": [
                       "439"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CGraph::update() in _ui/include/classes/api/services/CGraph.php_.