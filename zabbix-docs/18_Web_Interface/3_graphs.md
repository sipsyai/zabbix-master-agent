---
title: Graphs
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/data_collection/templates/graphs
downloaded: 2025-11-14 10:39:00
---

# 3 Graphs  
  
#### Overview

The custom graph list for a template can be accessed from _Data collection → Templates_ by clicking on _Graphs_ for the respective template.

A list of existing graphs is displayed.

![](/documentation/current/assets/en/manual/web_interface/template_graphs.png)

Displayed data:

_Template_ | Template the graph belongs to.  
Clicking on the template name opens the template [configuration form](/documentation/current/en/manual/config/templates/template#creating-a-template).  
This column is displayed only if multiple templates or no templates are selected in the filter.  
---|---  
_Name_ | Name of the custom graph, displayed as a blue link to graph details.  
Clicking on the graph name link opens the graph [configuration form](/documentation/current/en/manual/config/visualization/graphs/custom#configuring-custom-graphs).  
If the graph is inherited from another template, the template name is displayed before the graph name as a gray link. Clicking on the template link opens the graph list on that template level.  
_Width_ | Graph width is displayed.  
_Height_ | Graph height is displayed.  
_Graph type_ | Graph type is displayed - _Normal_ , _Stacked_ , _Pie_ or _Exploded_.  
  
To [configure](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/graph#configuration) a new graph, click on the _Create graph_ button at the upper-right corner.

##### Mass editing options

Buttons below the list offer some mass-editing options:

  * _Copy_ \- copy the graphs to other hosts or templates
  * _Delete_ \- delete the graphs

To use these options, mark the checkboxes before the respective graphs, then click on the required button.

##### Using filter

You can filter graphs by template group and template. For better search performance, data is searched with macros unresolved.