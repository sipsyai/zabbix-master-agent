---
title: Custom graphs
source: https://www.zabbix.com/documentation/current/en/manual/config/visualization/graphs/custom
downloaded: 2025-11-14 10:35:49
---

# 2 Custom graphs

#### Overview

Custom graphs, as the name suggests, offer customization capabilities.

While simple graphs are good for viewing data of a single item, they do not offer configuration capabilities.

Thus, if you want to change graph style or the way lines are displayed or compare several items, for example, incoming and outgoing traffic in a single graph, you need a custom graph.

Custom graphs are configured manually.

They can be created for a host or several hosts or for a single template.

#### Configuring custom graphs

To create a custom graph, do the following:

  * Go to _Data collection > Hosts (or Templates)_
  * Click on _Graphs_ in the row next to the desired host or template
  * In the Graphs screen click on _Create graph_
  * Edit graph attributes

![](/documentation/current/assets/en/manual/config/visualization/graph2.png)

All mandatory input fields are marked with a red asterisk.

Graph attributes:

_Name_ | Unique graph name.  
Expression [macros](/documentation/current/en/manual/appendix/macros/supported_by_location) are supported in this field, but only with `avg`, `last`, `min` and `max` functions, with time as parameter (for example, `{?avg(/host/key,1h)}`).  
{HOST.HOST<1-9>} macros are supported for the use within this macro, referencing the first, second, third, etc. host in the graph, for example `{?avg(/{HOST.HOST2}/key,1h)}`. Note that referencing the first host with this macro is redundant, as the first host can be referenced implicitly, for example `{?avg(//key,1h)}`.  
---|---  
_Width_ | Graph width in pixels (for preview and pie/exploded graphs only).  
_Height_ | Graph height in pixels.  
_Graph type_ | Graph type:  
**Normal** \- normal graph, values displayed as lines  
**Stacked** \- stacked graph, filled areas displayed  
**Pie** \- pie graph  
**Exploded** \- "exploded" pie graph, portions displayed as "cut out" of the pie  
_Show legend_ | Checking this box will set to display the graph legend.  
_Show working time_ | If selected, non-working hours will be shown with a gray background. This parameter is not available for pie and exploded pie graphs.  
_Show triggers_ | If selected, [simple triggers](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/graph#displaying-options) will be displayed as lines with black dashes over trigger severity color. This parameter is not available for pie and exploded pie graphs.  
_Percentile line (left)_ | Display percentile for left Y-axis. If, for example, 95% percentile is set, then the percentile line will be at the level where 95 percent of the values fall under. Displayed as a bright green line. Only available for normal graphs.  
_Percentile line (right)_ | Display percentile for right Y-axis. If, for example, 95% percentile is set, then the percentile line will be at the level where 95 percent of the values fall under. Displayed as a bright red line. Only available for normal graphs.  
_Y axis MIN value_ | Minimum value of Y-axis:  
**Calculated** \- Y axis minimum value will be automatically calculated.  
**Fixed** \- fixed minimum value for Y-axis.   
**Item** \- last value of the selected item will be the minimum value.  
  
This parameter is not available for pie and exploded pie graphs.  
_Y axis MAX value_ | Maximum value of Y-axis:  
**Calculated** \- Y axis maximum value will be automatically calculated.  
**Fixed** \- fixed maximum value for Y-axis.   
**Item** \- last value of the selected item will be the maximum value  
  
This parameter is not available for pie and exploded pie graphs.  
_3D view_ | Enable 3D style. For pie and exploded pie graphs only.  
_Items_ | Items, data of which are to be displayed in this graph. Click on _Add_ to select items. You can also select various displaying options (function, draw style, left/right axis display, color).  
| _Sort order (0→100)_ | Draw order. 0 will be processed first. Can be used to draw lines or regions behind (or in front of) another.  
You can drag and drop items using the icon at the beginning of a line to set the sort order or which item is displayed in front of the other.  
_Name_ | Name of the selected item is displayed as a link. Clicking on the link opens the list of other available items.  
_Type_ | Type (only available for pie and exploded pie graphs):  
**Simple** \- the value of the item is represented proportionally on the pie  
**Graph sum** \- the value of the item represents the whole pie  
Note that coloring of the "graph sum" item will only be visible to the extent that it is not taken up by "proportional" items.  
_Function_ | Select what values will be displayed when more than one value exists per vertical graph pixel for an item:  
**all** \- display all possible values (minimum, maximum, average) in the graph. Note that for shorter periods this setting has no effect; only for longer periods, when data congestion in a vertical graph pixel increases, 'all' starts displaying minimum, maximum, and average values. This function is only available for _Normal_ graph type. See also: Generating graphs [from history/trends](/documentation/current/en/manual/config/visualization/graphs/simple#generating-from-historytrends).  
**avg** \- display the average values  
**last** \- display the latest values. This function is only available if either _Pie/Exploded pie_ is selected as graph type.  
**max** \- display the maximum values  
**min** \- display the minimum values  
_Draw style_ | Select the draw style (only available for normal graphs; for stacked graphs filled region is always used) to apply to the item data - _Line_ , _Bold line_ , _Filled region_ , _Dot_ , _Dashed line_ , _Gradient line_.  
_Y axis side_ | Select the Y axis side to show the item data - _Left_ , _Right_.  
_Color_ | Select the color to apply to the item data.  
  
##### Graph preview

In the _Preview_ tab, a preview of the graph is displayed so you can immediately see what you are creating.

![](/documentation/current/assets/en/manual/config/visualization/graph_preview.png)

Note that the preview will not show any data for template items.

![](/documentation/current/assets/en/manual/config/visualization/graph_preview2.png)

In this example, pay attention to the dashed bold line displaying the trigger level and the trigger information displayed in the legend.

No more than 3 trigger lines can be displayed. If there are more triggers then the triggers with lower severity are prioritized for display.  
  
If graph height is set as less than 120 pixels, no trigger will be displayed in the legend.