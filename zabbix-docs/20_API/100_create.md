---
title: graph.create
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/graph/create
downloaded: 2025-11-14 10:41:34
---

# graph.create  
  
### Description

`object graph.create(object/array graphs)`

This method allows to create new graphs.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` Graphs to create.

Additionally to the [standard graph properties](object#graph), the method accepts the following parameters.

gitems | array | [Graph items](/documentation/current/en/manual/api/reference/graphitem/object) to be created for the graph.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
---|---|---  
  
### Return values

`(object)` Returns an object containing the IDs of the created graphs under the `graphids` property. The order of the returned IDs matches the order of the passed graphs.

### Examples

#### Creating a graph

Create a graph with two items.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "graph.create",
               "params": {
                   "name": "MySQL bandwidth",
                   "width": 900,
                   "height": 200,
                   "gitems": [
                       {
                           "itemid": "22828",
                           "color": "00AA00"
                       },
                       {
                           "itemid": "22829",
                           "color": "3333FF"
                       }
                   ]
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
                       "652"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### See also

  * [Graph item](/documentation/current/en/manual/api/reference/graphitem/object#graph-item)

### Source

CGraph::create() in _ui/include/classes/api/services/CGraph.php_.