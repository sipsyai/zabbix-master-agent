---
title: Graph object
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/graph/object
downloaded: 2025-11-14 10:41:33
---

# Graph object

The following objects are directly related to the `graph` API.

### Graph

The graph object has the following properties.

graphid | ID | ID of the graph.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
\- _required_ for update operations  
---|---|---  
height | integer | Height of the graph in pixels.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
name | string | Name of the graph.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
width | integer | Width of the graph in pixels.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
flags | integer | [Origin](/documentation/current/en/manual/api/reference_commentary#entity-origin-flags) of the graph.  
  
Possible values:  
0 - _(default)_ a plain graph;  
4 - a graph converted from prototype.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
graphtype | integer | Graph's layout type.  
  
Possible values:  
0 - _(default)_ normal;  
1 - stacked;  
2 - pie;  
3 - exploded.  
percent_left | float | Left percentile.  
  
Default: 0.  
percent_right | float | Right percentile.  
  
Default: 0.  
show_3d | integer | Whether to show pie and exploded graphs in 3D.  
  
Possible values:  
0 - _(default)_ show in 2D;  
1 - show in 3D.  
show_legend | integer | Whether to show the legend on the graph.  
  
Possible values:  
0 - hide;  
1 - _(default)_ show.  
show_work_period | integer | Whether to show the working time on the graph.  
  
Possible values:  
0 - hide;  
1 - _(default)_ show.  
show_triggers | integer | Whether to show the trigger line on the graph.  
  
Possible values:  
0 - hide;  
1 - _(default)_ show.  
templateid | ID | ID of the parent template graph.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
yaxismax | float | The fixed maximum value for the Y axis.  
  
Default: 100.  
yaxismin | float | The fixed minimum value for the Y axis.  
  
Default: 0.  
ymax_itemid | ID | ID of the item that is used as the maximum value for the Y axis.  
  
If a user has no access to the specified item, the graph is rendered as if `ymax_type` is set to "calculated".  
ymax_type | integer | Maximum value calculation method for the Y axis.  
  
Possible values:  
0 - _(default)_ calculated;  
1 - fixed;  
2 - item.  
ymin_itemid | ID | ID of the item that is used as the minimum value for the Y axis.  
  
If a user has no access to the specified item, the graph is rendered as if `ymin_type` is set to "calculated".  
ymin_type | integer | Minimum value calculation method for the Y axis.  
  
Possible values:  
0 - _(default)_ calculated;  
1 - fixed;  
2 - item.  
uuid | string | Universal unique identifier, used for linking imported graphs to already existing ones. Auto-generated, if not given.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if the graph belongs to a template