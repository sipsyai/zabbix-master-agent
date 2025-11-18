---
title: Graph item object
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/graphitem/object
downloaded: 2025-11-14 10:41:39
---

# Graph item object

The following objects are directly related to the `graphitem` API.

### Graph item

Graph items can only be modified via the `graph` API.

The graph item object has the following properties.

gitemid | ID | ID of the graph item.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
---|---|---  
color | string | Graph item's draw color as a hexadecimal color code.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
itemid | ID | ID of the item.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
calc_fnc | integer | Value of the item that will be displayed.  
  
Possible values:  
1 - minimum value;  
2 - _(default)_ average value;  
4 - maximum value;  
7 - all values;  
9 - last value, used only by pie and exploded graphs.  
drawtype | integer | Draw style of the graph item.  
  
Possible values:  
0 - _(default)_ line;  
1 - filled region;  
2 - bold line;  
3 - dot;  
4 - dashed line;  
5 - gradient line.  
graphid | ID | ID of the graph that the graph item belongs to.  
sortorder | integer | Position of the item in the graph.  
  
Default: starts with "0" and increases by one with each entry.  
type | integer | Type of graph item.  
  
Possible values:  
0 - _(default)_ simple;  
2 - graph sum, used only by pie and exploded graphs.  
yaxisside | integer | Side of the graph where the graph item's Y scale will be drawn.  
  
Possible values:  
0 - _(default)_ left side;  
1 - right side.