---
title: Graph prototype object
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/graphprototype/object
downloaded: 2025-11-14 10:41:42
---

# Graph prototype object

The following objects are directly related to the `graphprototype` API.

### Graph prototype

The graph prototype object has the following properties.

graphid | ID | ID of the graph prototype.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
\- _required_ for update operations  
---|---|---  
height | integer | Height of the graph prototype in pixels.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
name | string | Name of the graph prototype.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
width | integer | Width of the graph prototype in pixels.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
flags | integer | [Origin](/documentation/current/en/manual/api/reference_commentary#entity-origin-flags) of the graph prototype.  
  
Possible values:  
2 - a graph prototype;  
6 - a discovered graph prototype  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
graphtype | integer | Graph prototypes's layout type.  
  
Possible values:  
0 - _(default)_ normal;  
1 - stacked;  
2 - pie;  
3 - exploded.  
percent_left | float | Left percentile.  
  
Default: 0.  
percent_right | float | Right percentile.  
  
Default: 0.  
show_3d | integer | Whether to show discovered pie and exploded graphs in 3D.  
  
Possible values:  
0 - _(default)_ show in 2D;  
1 - show in 3D.  
show_legend | integer | Whether to show the legend on the discovered graph.  
  
Possible values:  
0 - hide;  
1 - _(default)_ show.  
show_work_period | integer | Whether to show the working time on the discovered graph.  
  
Possible values:  
0 - hide;  
1 - _(default)_ show.  
templateid | ID | ID of the parent template graph prototype.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
yaxismax | float | The fixed maximum value for the Y axis.  
yaxismin | float | The fixed minimum value for the Y axis.  
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
discover | integer | Graph prototype discovery status.  
  
Possible values:  
0 - _(default)_ new graphs will be discovered;  
1 - new graphs will not be discovered and existing graphs will be marked as lost.  
uuid | string | Universal unique identifier, used for linking imported graph prototypes to already existing ones. Auto-generated, if not given.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if the graph prototype belongs to a template