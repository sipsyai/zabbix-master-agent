---
title: Map object
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/map/object
downloaded: 2025-11-14 10:43:15
---

# Map object

The following objects are directly related to the `map` API.

### Map

The map object has the following properties.

sysmapid | ID | ID of the map.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
\- _required_ for update operations  
---|---|---  
height | integer | Height of the map in pixels.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
name | string | Name of the map.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
width | integer | Width of the map in pixels.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
backgroundid | ID | ID of the image used as the background for the map.  
background_scale | integer | Whether to enable background image proportional scaling.  
  
Possible values:  
0 - disable scaling;  
1 - _(default)_ enable image scaling.  
expand_macros | integer | Whether to expand macros in labels when configuring the map.  
  
Possible values:  
0 - _(default)_ do not expand macros;  
1 - expand macros.  
expandproblem | integer | Whether the problem trigger will be displayed for elements with a single problem.  
  
Possible values:  
0 - always display the number of problems;  
1 - _(default)_ display the problem trigger if there's only one problem.  
grid_align | integer | Whether to enable grid aligning.  
  
Possible values:  
0 - disable grid aligning;  
1 - _(default)_ enable grid aligning.  
grid_show | integer | Whether to show the grid on the map.  
  
Possible values:  
0 - do not show the grid;  
1 - _(default)_ show the grid.  
grid_size | integer | Size of the map grid in pixels.  
  
Supported values: 20, 40, 50, 75 and 100.  
  
Default: 50.  
highlight | integer | Whether icon highlighting is enabled.  
  
Possible values:  
0 - highlighting disabled;  
1 - _(default)_ highlighting enabled.  
iconmapid | ID | ID of the icon map used on the map.  
label_format | integer | Whether to enable advanced labels.  
  
Possible values:  
0 - _(default)_ disable advanced labels;  
1 - enable advanced labels.  
label_location | integer | Location of the map element label.  
  
Possible values:  
0 - _(default)_ bottom;  
1 - left;  
2 - right;  
3 - top.  
label_string_host | string | Custom label for host elements.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `label_type_host` is set to "custom"  
label_string_hostgroup | string | Custom label for host group elements.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `label_type_hostgroup` is set to "custom"  
label_string_image | string | Custom label for image elements.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `label_type_image` is set to "custom"  
label_string_map | string | Custom label for map elements.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `label_type_map` is set to "custom"  
label_string_trigger | string | Custom label for trigger elements.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `label_type_trigger` is set to "custom"  
label_type | integer | Map element label type.  
  
Possible values:  
0 - label;  
1 - IP address;  
2 - _(default)_ element name;  
3 - status only;  
4 - nothing.  
label_type_host | integer | Label type for host elements.  
  
Possible values:  
0 - label;  
1 - IP address;  
2 - _(default)_ element name;  
3 - status only;  
4 - nothing;  
5 - custom.  
label_type_hostgroup | integer | Label type for host group elements.  
  
Possible values:  
0 - label;  
2 - _(default)_ element name;  
3 - status only;  
4 - nothing;  
5 - custom.  
label_type_image | integer | Label type for host group elements.  
  
Possible values:  
0 - label;  
2 - _(default)_ element name;  
4 - nothing;  
5 - custom.  
label_type_map | integer | Label type for map elements.  
  
Possible values:  
0 - label;  
2 - _(default)_ element name;  
3 - status only;  
4 - nothing;  
5 - custom.  
label_type_trigger | integer | Label type for trigger elements.  
  
Possible values:  
0 - label;  
2 - _(default)_ element name;  
3 - status only;  
4 - nothing;  
5 - custom.  
markelements | integer | Whether to highlight map elements that have recently changed their status.  
  
Possible values:  
0 - _(default)_ do not highlight elements;  
1 - highlight elements.  
severity_min | integer | Minimum severity of the triggers that will be displayed on the map.  
  
Refer to the [trigger `severity` property](/documentation/current/en/manual/api/reference/trigger/object#trigger) for a list of supported trigger severities.  
show_element_label | integer | How to display element labels by default.  
  
Possible values:  
0 - always display;  
1 - _(default)_ auto-hide.  
show_link_label | integer | How to display link labels by default.  
  
Possible values:  
0 - always display;  
1 - _(default)_ auto-hide.  
show_unack | integer | How problems should be displayed.  
  
Possible values:  
0 - _(default)_ display the count of all problems;  
1 - display only the count of unacknowledged problems;  
2 - display the count of acknowledged and unacknowledged problems separately.  
userid | ID | ID of the user that is the owner of the map.  
private | integer | Type of map sharing.  
  
Possible values:  
0 - public map;  
1 - _(default)_ private map.  
show_suppressed | integer | Whether suppressed problems are shown.  
  
Possible values:  
0 - _(default)_ hide suppressed problems;  
1 - show suppressed problems.  
  
### Map element

The map element object defines an object displayed on a map. It has the following properties.

selementid | ID | ID of the map element.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
---|---|---  
elements | array | Element data object.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `elementtype` is set to "host", "map", "trigger" or "host group"  
elementtype | integer | Type of map element.  
  
Possible values:  
0 - host;  
1 - map;  
2 - trigger;  
3 - host group;  
4 - image.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
iconid_off | ID | ID of the image used to display the element in default state.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
areatype | integer | How separate host group hosts should be displayed.  
  
Possible values:  
0 - _(default)_ the host group element will take up the whole map;  
1 - the host group element will have a fixed size.  
elementsubtype | integer | How a host group element should be displayed on a map.  
  
Possible values:  
0 - _(default)_ display the host group as a single element;  
1 - display each host in the group separately.  
evaltype | integer | Map element tag filtering condition [evaluation method](/documentation/current/en/manual/config/visualization/maps/map#adding-elements).  
  
Possible values:  
0 - _(default)_ And/Or;  
2 - Or.  
height | integer | Height of the fixed size host group element in pixels.  
  
Default: 200.  
iconid_disabled | ID | ID of the image used to display disabled map elements.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `elementtype` is set to "host", "map", "trigger", or "host group"  
iconid_maintenance | ID | ID of the image used to display map elements in maintenance.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `elementtype` is set to "host", "map", "trigger", or "host group"  
iconid_on | ID | ID of the image used to display map elements with problems.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `elementtype` is set to "host", "map", "trigger", or "host group"  
label | string | Label of the element.  
label_location | integer | Location of the map element label.  
  
Possible values:  
-1 - _(default)_ default location;  
0 - bottom;  
1 - left;  
2 - right;  
3 - top.  
permission | integer | Type of permission level.  
  
Possible values:  
-1 - none;  
2 - read only;  
3 - read-write.  
show_label | integer | How to display the element label.  
  
Possible values:  
-1 - _(default)_ map default;  
0 - always display;  
1 - auto-hide.  
sysmapid | ID | ID of the map that the element belongs to.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
urls | array | Map element URLs.  
  
The map element URL object is [described in detail below](object#map-element-url).  
use_iconmap | integer | Whether icon mapping must be used for host elements.  
  
Possible values:  
0 - do not use icon mapping;  
1 - _(default)_ use icon mapping.  
viewtype | integer | Host group element placing algorithm.  
  
Possible values:  
0 - _(default)_ grid.  
width | integer | Width of the fixed size host group element in pixels.  
  
Default: 200.  
x | integer | X-coordinates of the element in pixels.  
  
Default: 0.  
y | integer | Y-coordinates of the element in pixels.  
  
Default: 0.  
zindex | integer | Value used to order map elements (z-index).  
  
Default: 0.  
  
#### Map element Host

The map element Host object defines one host element.

hostid | ID | ID of the host.  
---|---|---  
  
#### Map element Host group

The map element Host group object defines one host group element.

groupid | ID | ID of the host group.  
---|---|---  
  
#### Map element Map

The map element Map object defines one map element.

sysmapid | ID | ID of the map.  
---|---|---  
  
#### Map element Trigger

The map element Trigger object defines one or more trigger elements.

triggerid | ID | ID of the trigger.  
---|---|---  
  
#### Map element Tag

The map element Tag object has the following properties.

tag | string | Map element tag name.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
operator | integer | Map element tag condition [operator](/documentation/current/en/manual/config/visualization/maps/map#adding-elements).  
  
Possible values:  
0 - _(default)_ Contains;  
1 - Equals;  
2 - Does not contain;  
3 - Does not equal;  
4 - Exists;  
5 - Does not exist.  
value | string | Map element tag value.  
  
#### Map element URL

The map element URL object defines a clickable link that will be available for a specific map element. It has the following properties:

sysmapelementurlid | ID | ID of the map element URL.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
---|---|---  
name | string | Link caption.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
url | string | Link URL.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
selementid | ID | ID of the map element that the URL belongs to.  
  
### Map link

The map link object defines a link between two map elements. It has the following properties.

linkid | ID | ID of the map link.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
---|---|---  
sysmapid | ID | ID of the map the link belongs to.  
selementid1 | ID | ID of the first map element linked on one end.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
selementid2 | ID | ID of the first map element linked on the other end.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
drawtype | integer | Link line draw style.  
  
Possible values:  
0 - _(default)_ line;  
2 - bold line;  
3 - dotted line;  
4 - dashed line.  
color | string | Line color as a hexadecimal color code.  
  
Default: `000000`.  
label | string | Link label.  
show_label | integer | How to display the link label.  
  
Possible values:  
-1 - _(default)_ map default;  
0 - always display;  
1 - auto-hide.  
indicator_type | integer | Select the link indicator type.  
  
Possible values:  
0 - _(default)_ static link;  
1 - trigger;  
2 - item value.  
linktriggers | array | Map link triggers to use as link status indicators.  
  
The map link trigger object is [described in detail below](object#map-link-trigger).  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `indicator_type` is set to "trigger" (1).  
itemid | ID | ID of the item.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `indicator_type` is set to "item value" (2).  
highlights | array | Map link highlights to use as link status indicators.  
  
The map link indicators object is [described in detail below](object#map-link-indicators).  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `indicator_type` is set to "item value" (2).  
thresholds | array | Map link thresholds to use as link status indicators.  
  
The map link indicators object is [described in detail below](object#map-link-indicators).  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `indicator_type` is set to "item value" (2).  
permission | integer | Type of permission level.  
  
Possible values:  
-1 - none;  
2 - read only;  
3 - read-write.  
  
#### Map link trigger

The map link trigger object defines a map link status indicator based on the state of a trigger. It has the following properties:

triggerid | ID | ID of the trigger used as a link indicator.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
color | string | Indicator color as a hexadecimal color code.  
  
Default: `DD0000`.  
drawtype | integer | Indicator draw style.  
  
Possible values:  
0 - _(default)_ line;  
2 - bold line;  
3 - dotted line;  
4 - dashed line.  
  
#### Map link indicators

The map link indicators object defines a map link status indicator based on the item value. It has the following properties:

pattern | string | Regular expression to compare against. Available only for highlights.  
---|---|---  
sortorder | integer | Used for defining the sort order of highlights. Available only for highlights.  
threshold | string | Numeric value to compare against. Available only for thresholds.  
drawtype | integer | Indicator draw style.  
  
Possible values:  
0 - _(default)_ line;  
2 - bold line;  
3 - dotted line;  
4 - dashed line.  
color | string | Indicator color as a hexadecimal color code.  
  
Default: `DD0000`.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
  
### Map URL

The map URL object defines a clickable link that will be available for all elements of a specific type on the map. It has the following properties:

sysmapurlid | ID | ID of the map URL.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
---|---|---  
name | string | Link caption.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
url | string | Link URL.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
elementtype | integer | Type of map element for which the URL will be available.  
  
Refer to the [map element `type` property](object#map-element) for a list of supported types.  
  
Default: 0.  
sysmapid | ID | ID of the map that the URL belongs to.  
  
### Map user

List of map permissions based on users. It has the following properties:

sysmapuserid | ID | ID of the map user.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
---|---|---  
userid | ID | ID of the user.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
permission | integer | Type of permission level.  
  
Possible values:  
2 - read only;  
3 - read-write.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
  
### Map user group

List of map permissions based on user groups. It has the following properties:

sysmapusrgrpid | ID | ID of the map user group.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
---|---|---  
usrgrpid | ID | ID of the user group.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
permission | integer | Type of permission level.  
  
Possible values:  
2 - read only;  
3 - read-write.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
  
### Map shapes

The map shape object defines a geometric shape (with or without text) displayed on a map. It has the following properties:

sysmap_shapeid | ID | ID of the map shape element.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
---|---|---  
type | integer | Type of map shape element.  
  
Possible values:  
0 - rectangle;  
1 - ellipse.  
  
Property is required when new shapes are created.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
x | integer | X-coordinates of the shape in pixels.  
  
Default: 0.  
y | integer | Y-coordinates of the shape in pixels.  
  
Default: 0.  
width | integer | Width of the shape in pixels.  
  
Default: 200.  
height | integer | Height of the shape in pixels.  
  
Default: 200.  
text | string | Text of the shape.  
font | integer | Font of the text within shape.  
  
Possible values:  
0 - Georgia, serif  
1 - “Palatino Linotype”, “Book Antiqua”, Palatino, serif  
2 - “Times New Roman”, Times, serif  
3 - Arial, Helvetica, sans-serif  
4 - “Arial Black”, Gadget, sans-serif  
5 - “Comic Sans MS”, cursive, sans-serif  
6 - Impact, Charcoal, sans-serif  
7 - “Lucida Sans Unicode”, “Lucida Grande”, sans-serif  
8 - Tahoma, Geneva, sans-serif  
9 - “Trebuchet MS”, Helvetica, sans-serif  
10 - Verdana, Geneva, sans-serif  
11 - “Courier New”, Courier, monospace  
12 - “Lucida Console”, Monaco, monospace  
  
Default: 9.  
font_size | integer | Font size in pixels.  
  
Default: 11.  
font_color | string | Font color.  
  
Default: `000000`.  
text_halign | integer | Horizontal alignment of text.  
  
Possible values:  
0 - center;  
1 - left;  
2 - right.  
  
Default: 0.  
text_valign | integer | Vertical alignment of text.  
  
Possible values:  
0 - middle;  
1 - top;  
2 - bottom.  
  
Default: 0.  
border_type | integer | Type of the border.  
  
Possible values:  
0 - none;  
1 - `—————`;  
2 - `·····`;  
3 - `- - -`.  
  
Default: 0.  
border_width | integer | Width of the border in pixels.  
  
Default: 0.  
border_color | string | Border color.  
  
Default: `000000`.  
background_color | string | Background color (fill color).  
  
Default: `(empty)`.  
zindex | integer | Value used to order all shapes and lines (z-index).  
  
Default: 0.  
  
### Map lines

The map line object defines a line displayed on a map. It has the following properties:

sysmap_shapeid | ID | ID of the map shape element.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
---|---|---  
x1 | integer | X-coordinates of the line point 1 in pixels.  
  
Default: 0.  
y1 | integer | Y-coordinates of the line point 1 in pixels.  
  
Default: 0.  
x2 | integer | X-coordinates of the line point 2 in pixels.  
  
Default: 200.  
y2 | integer | Y-coordinates of the line point 2 in pixels.  
  
Default: 200.  
line_type | integer | Type of the lines.  
  
Possible values:  
0 - none;  
1 - `—————`;  
2 - `·····`;  
3 - `- - -`.  
  
Default: 0.  
line_width | integer | Width of the lines in pixels.  
  
Default: 0.  
line_color | string | Line color.  
  
Default: `000000`.  
zindex | integer | Value used to order all shapes and lines (z-index).  
  
Default: 0.