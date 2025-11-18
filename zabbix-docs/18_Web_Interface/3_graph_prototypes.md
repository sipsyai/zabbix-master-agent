---
title: Graph prototypes
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/data_collection/templates/discovery/graph_prototypes
downloaded: 2025-11-14 10:39:04
---

# 3 Graph prototypes

#### Overview

In this section the configured graph prototypes of a low-level discovery rule on the template are displayed.

If the template is linked to the host, graph prototypes will become the basis of creating real host [graphs](/documentation/current/en/manual/web_interface/frontend_sections/data_collection/hosts/graphs) during low-level discovery.

![](/documentation/current/assets/en/manual/web_interface/template_graph_prototypes.png)

Displayed data:

_Name_ | Name of the graph prototype, displayed as a blue link.  
Clicking on the name opens the graph prototype [configuration form](/documentation/current/en/manual/discovery/low_level_discovery/graph_prototypes).  
If the graph prototype belongs to a linked template, the template name is displayed before the graph name as a gray link. Clicking on the template link opens the graph prototype list on the linked template level.  
---|---  
_Width_ | Width of the graph prototype is displayed.  
_Height_ | Height of the graph prototype is displayed.  
_Type_ | Type of the graph prototype is displayed - _Normal_ , _Stacked_ , _Pie_ or _Exploded_.  
_Discover_ | Discover the graph based on this prototype:  
**Yes** \- discover  
**No** \- do not discover. You can switch between 'Yes' and 'No' by clicking on them.  
  
To configure a new graph prototype, click on the _Create graph prototype_ button at the upper-right corner.

##### Mass editing options

Buttons below the list offer some mass-editing options:

  * _Delete_ \- delete these graph prototypes

To use these options, mark the checkboxes before the respective graph prototypes, then click on the required button.