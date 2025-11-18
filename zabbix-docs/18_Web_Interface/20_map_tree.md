---
title: Map navigation tree
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/map_tree
downloaded: 2025-11-14 10:38:18
---

# 20 Map navigation tree  
  
#### Overview

This widget allows building a hierarchy of existing maps while also displaying problem statistics with each included map and map group.

It becomes even more powerful if you link the _Map_ widget to the navigation tree. In this case, clicking on a map name in the navigation tree displays the map in full in the _Map_ widget.

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/map_to_display.png)

Statistics with the top-level map in the hierarchy display a sum of problems of all submaps and their own problems.

#### Configuration

To configure, select _Map navigation tree_ as type:

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/map_tree.png)

In addition to the parameters that are [common](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#common-parameters) for all widgets, you may set the following specific options:

_Show unavailable maps_ | Mark this checkbox to display maps that the user does not have read permission to.  
Unavailable maps in the navigation tree will be displayed with a grayed-out icon.  
Note that if this checkbox is marked, available [submaps](/documentation/current/en/manual/config/visualization/maps/map#adding-elements) are displayed even if the parent level map is unavailable. If unmarked, available submaps to an unavailable parent map will not be displayed at all.  
Problem count is calculated based on available maps and available map elements.  
---|---  
  
Navigation tree elements are displayed in a list. You can:

  * drag an element (including its child elements) to a new place in the list;
  * expand or collapse an element to display or hide its child elements;
  * add a child element (with or without a linked map) to an element;
  * add multiple child elements (with linked maps) to an element;
  * edit an element;
  * remove an element (including its child elements).

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/map_tree_element.png)

##### Element configuration

To configure a navigation tree element, either add a new element or edit an existing element.

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/map_tree_element_configuration.png)

The following navigation tree element configuration parameters are available:

_Name_ | Enter the navigation tree element name.  
---|---  
_Linked map_ | Select the map to link to the navigation tree element.  
This field is auto-complete, so starting to type the name of a map will offer a dropdown of matching maps.  
_Add submaps_ | Mark this checkbox to add the [submaps](/documentation/current/en/manual/config/visualization/maps/map#adding-elements) of the linked map as child elements to the navigation tree element.