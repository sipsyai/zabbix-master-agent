---
title: Host group elements
source: https://www.zabbix.com/documentation/current/en/manual/config/visualization/maps/host_groups
downloaded: 2025-11-14 10:35:54
---

# 2 Host group elements

#### Overview

This section explains how to add a ["Host group"](/documentation/current/en/manual/config/hosts/host_groups) type element when configuring a [network map](/documentation/current/en/manual/config/visualization/maps/map).

#### Configuration

![](/documentation/current/assets/en/manual/config/visualization/maps/map_host_group.png)

All mandatory input fields are marked with a red asterisk.

This table consists of parameters typical for _Host group_ element type:

_Type_ | Select Type of the element:  
**Host group** \- icon representing the status of all triggers of all hosts belonging to the selected group  
---|---  
_Show_ | Show options:  
**Host group** \- selecting this option will result as one single icon displaying corresponding information about the certain host group  
**Host group elements** \- selecting this option will result as multiple icons displaying corresponding information about every single element (host) of the certain host group  
_Area type_ | This setting is available if the “Host group elements” parameter is selected:  
**Fit to map** \- all host group elements are equally placed within the map  
**Custom size** \- a manual setting of the map area for all the host group elements to be displayed  
_Area size_ | This setting is available if “Host group elements” parameter and “Area type” parameter are selected:  
**Width** \- numeric value to be entered to specify map area width  
**Height** \- numeric value to be entered to specify map area height  
_Placing algorithm_ | **Grid** – only available option of displaying all the host group elements  
_Label_ | Icon label, any string.  
[Macros](/documentation/current/en/manual/config/macros) and multiline strings can be used in labels.  
If the type of the map element is “Host group” specifying certain macros has an impact on the map view displaying corresponding information about every single host. For example, if [{HOST.IP}](/documentation/current/en/manual/appendix/macros/supported_by_location#hostip) macro is used, the edit map view will only display the macro {HOST.IP} itself while map view will include and display each host's unique IP address  
  
#### Viewing host group elements

This option is available if the "Host group elements" show option is chosen. When selecting "Host group elements" as the _show_ option, you will at first see only one icon for the host group. However, when you save the map and then go to the map view, you will see that the map includes all the elements (hosts) of the certain host group:

![](/documentation/current/assets/en/manual/config/visualization/maps/map_host_group_conf.png) | ![](/documentation/current/assets/en/manual/config/visualization/maps/map_host_group_view.png)  
---|---  
  
Notice how the [{HOST.HOST}](/documentation/current/en/manual/appendix/macros/supported_by_location#hosthost) macro is used. In map editing, the macro name is unresolved, while in map view all the unique names of the hosts are displayed.