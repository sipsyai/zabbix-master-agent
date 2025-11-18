---
title: Maps
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/monitoring/maps
downloaded: 2025-11-14 10:38:39
---

# 4 Maps

#### Overview

In the _Monitoring → Maps_ section you can configure, manage and view [network maps](/documentation/current/en/manual/config/visualization/maps).

When you open this section, you will either see the last map you accessed or a listing of all maps you have access to.

All maps can be either public or private. Public maps are available to all users, while private maps are accessible only to their owner and the users the map is shared with.

#### Map listing

![](/documentation/current/assets/en/manual/web_interface/map_list.png)

Displayed data:

_Name_ | Name of the map. Click on the name to [view](/documentation/current/en/manual/web_interface/frontend_sections/monitoring/maps#viewing-maps) the map.  
---|---  
_Width_ | Map width is displayed.  
_Height_ | Map height is displayed.  
_Actions_ | Two actions are available:  
**Properties** \- set general map [properties](/documentation/current/en/manual/config/visualization/maps/map#creating-a-map)  
**Edit** \- access the grid for adding [map elements](/documentation/current/en/manual/config/visualization/maps/map#adding-elements)  
  
To [configure](/documentation/current/en/manual/config/visualization/maps/map#creating-a-map) a new map, click on the _Create map_ button in the upper-right corner. To import a map from a YAML, XML, or JSON file, click on the _Import_ button in the upper-right corner. The user who imports the map will be set as its owner.

Two buttons below the list offer some mass-editing options:

  * _Export_ \- export the maps to a YAML, XML, or JSON file
  * _Delete_ \- delete the maps

To use these options, mark the checkboxes before the respective maps, then click on the required button.

##### Using filter

You can use the filter to display only the maps you are interested in. For better search performance, data is searched with macros unresolved.

#### Viewing maps

To view a map, click on its name in the list of all maps.

![](/documentation/current/assets/en/manual/web_interface/maps.png)

You can use the drop-down in the map title bar to select the lowest severity level of the problem triggers to display. The severity marked as _default_ is the level set in the map configuration. If the map contains a sub-map, navigating to the sub-map will retain the higher-level map severity (except if it is _Not classified_ , in this case, it will not be passed to the sub-map).

##### Icon highlighting

If a map element is in problem status, it is highlighted with a round circle. The fill color of the circle corresponds to the severity color of the problem. Only problems on or above the selected severity level will be displayed with the element. If all problems are acknowledged, a thick green border around the circle is displayed.

Additionally:

  * a host in [maintenance](/documentation/current/en/manual/maintenance) is highlighted with an orange, filled square. Note that maintenance highlighting has priority over the problem severity highlighting, if the map element is host.
  * a disabled (not-monitored) host is highlighted with a gray, filled square.

Highlighting is displayed if the _Icon highlighting_ check-box is marked in map [configuration](/documentation/current/en/manual/config/visualization/maps/map#creating-a-map).

##### Recent change markers

Inward pointing red triangles around an element indicate a recent trigger status change - one that's happened within the last 30 minutes. These triangles are shown if the _Mark elements on trigger status change_ check-box is marked in map [configuration](/documentation/current/en/manual/config/visualization/maps/map#creating-a-map).

##### Links

Clicking on a map element opens a menu with some available links. Clicking on the host name brings up the [host menu](/documentation/current/en/manual/web_interface/menu/host_menu).

##### Buttons

Buttons to the right offer the following options:

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/edit_map.png) | Go to editing of the map content.  
---|---  
![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/add_to_fav1.png) | Add map to the favorites widget in [Dashboards](/documentation/current/en/manual/web_interface/frontend_sections/dashboards).  
![](/documentation/current/assets/en/manual/web_interface/button_add_fav2.png) | The map is in the favorites widget in [Dashboards](/documentation/current/en/manual/web_interface/frontend_sections/dashboards). Click to remove map from the favorites widget.  
  
View mode buttons being common for all sections are described on the [Monitoring](/documentation/current/en/manual/web_interface/frontend_sections/monitoring#view-mode-buttons) page.

##### Readable summary in maps

A hidden "aria-label" property is available allowing map information to be read with a screen reader. Both general map description and individual element description is available, in the following format:

  * for map description: `<Map name>, <* of * items in problem state>, <* problems in total>.`
  * for describing one element with one problem: `<Element type>, Status <Element status>, <Element name>, <Problem description>.`
  * for describing one element with multiple problems: `<Element type>, Status <Element status>, <Element name>, <* problems>.`
  * for describing one element without problems: `<Element type>, Status <Element status>, <Element name>.`

For example, this description is available:
    
    
    'Local network, 1 of 6 elements in problem state, 1 problem in total. Host, Status problem, My host, Free disk space is less than 20% on volume \/. Host group, Status ok, Virtual servers. Host, Status ok, Server 1. Host, Status ok, Server 2. Host, Status ok, Server 3. Host, Status ok, Server 4. '

Copy

✔ Copied

for the following map:

![](/documentation/current/assets/en/manual/web_interface/map_aria_label.png)

##### Referencing a network map

Network maps can be referenced by both `sysmapid` and `mapname` GET parameters. For example,
    
    
    http://zabbix/zabbix/zabbix.php?action=map.view&mapname=Local%20network

Copy

✔ Copied

will open the map with that name (Local network).

If both `sysmapid` (map ID) and `mapname` (map name) are specified, `mapname` has higher priority.