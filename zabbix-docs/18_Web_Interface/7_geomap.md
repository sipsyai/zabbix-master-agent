---
title: Geomap
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/geomap
downloaded: 2025-11-14 10:38:06
---

# 7 Geomap

#### Overview

Geomap widget displays hosts as markers on a geographical map using open-source JavaScript interactive maps library Leaflet.

Zabbix offers multiple predefined map tile service providers and an option to add a custom tile service provider or even host tiles themselves (configurable in the _Administration > General > Geographical maps_ [menu section](/documentation/current/en/manual/web_interface/frontend_sections/administration/general#geographical-maps)).

By default, the widget displays all enabled hosts with valid geographical coordinates defined in the host configuration. It is possible to configure host filtering in the widget parameters.

The valid host coordinates are:

  * Latitude: from -90 to 90 (can be integer or float number)
  * Longitude: from -180 to 180 (can be integer or float number)

#### Configuration

To add the widget, select _Geomap_ as type.

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/geomap.png)

In addition to the parameters that are [common](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#common-parameters) for all widgets, you may set the following specific options:

_Host groups_ | Select host groups to be displayed on the map.  
Alternatively, select a compatible widget as the [data source](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/#dynamic-parameters) for host groups.  
This field is auto-complete, so starting to type the name of a group will offer a dropdown of matching groups.  
If nothing is selected in both _Host groups_ and _Hosts_ fields, all hosts with valid coordinates will be displayed.  
This parameter is not available when configuring the widget on a [template dashboard](/documentation/current/en/manual/config/templates/template#adding-dashboards).  
---|---  
_Hosts_ | Select hosts to be displayed on the map.  
Alternatively, select a compatible widget or the dashboard as the [data source](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/#dynamic-parameters) for hosts.  
This field is auto-complete, so starting to type the name of a host will offer a dropdown of matching hosts.  
If nothing is selected in both _Host groups_ and _Hosts_ fields, all hosts with valid coordinates will be displayed.  
This parameter is not available when configuring the widget on a [template dashboard](/documentation/current/en/manual/config/templates/template#adding-dashboards).  
_Tags_ | Specify tags to limit the number of hosts displayed in the widget.  
It is possible to include as well as exclude specific tags and tag values. Several conditions can be set. Tag name matching is always case-sensitive.  
  
There are several operators available for each condition:  
**Exists** \- include the specified tag names;  
**Equals** \- include the specified tag names and values (case-sensitive);  
**Contains** \- include the specified tag names where the tag values contain the entered string (substring match, case-insensitive);  
**Does not exist** \- exclude the specified tag names;  
**Does not equal** \- exclude the specified tag names and values (case-sensitive);  
**Does not contain** \- exclude the specified tag names where the tag values contain the entered string (substring match, case-insensitive).  
  
There are two calculation types for conditions:  
**And/Or** \- all conditions must be met, conditions having the same tag name will be grouped by the _Or_ condition;  
**Or** \- enough if one condition is met.  
  
This parameter is not available when configuring the widget on a [template dashboard](/documentation/current/en/manual/config/templates/template#adding-dashboards).  
_Initial view_ | Comma-separated center coordinates and an optional zoom level to display when the widget is initially loaded in the format `<latitude>,<longitude>,<zoom>`  
If initial zoom is specified, the Geomap widget is loaded at the given zoom level. Otherwise, initial zoom is calculated as half of the [max zoom](/documentation/current/en/manual/web_interface/frontend_sections/administration/general#geographical-maps) for the particular tile provider.  
The initial view is ignored if the default view is set (see below).  
Examples:  
40.6892494,-74.0466891  
40.6892494,-122.0466891  
  
Host markers displayed on the map have the color of the host's most serious problem and green color if a host has no problems. Clicking on a host marker allows viewing the host's visible name and the number of unresolved problems grouped by severity. Clicking on the visible name will open [host menu](/documentation/current/en/manual/web_interface/menu/host_menu).

Hosts displayed on the map can be filtered by problem severity. Press on the filter icon in the widget's upper-right corner and mark the required severities.

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/geomap_widget_filter.png)

It is possible to zoom in and out the map by using the plus and minus buttons in the widget's upper-left corner or by using the mouse scroll wheel or touchpad. To set the current view as default, right-click anywhere on the map and select _Set this view as default_. This setting will override _Initial view_ widget parameter for the current user. To undo this action, right-click anywhere on the map again and select _Reset to initial view_.

When _Initial view_ or _Default view_ is set, you can return to this view at any time by pressing on the home icon on the left.

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/geomap_widget3.png)