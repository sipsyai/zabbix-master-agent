---
title: Network maps
source: https://www.zabbix.com/documentation/current/en/manual/xml_export_import/maps
downloaded: 2025-11-14 10:37:12
---

# 5 Network maps

#### Overview

Network map [export](/documentation/current/en/manual/xml_export_import) contains:

  * All related images
  * Map structure (all map settings, all contained elements with their settings, map links and map link status indicators)

Any host groups, hosts, triggers, other maps or other elements that may be related to the exported map are not exported. Thus, if at least one of the elements the map refers to is missing, importing it will fail.

#### Exporting

To export network maps, do the following:

  1. Go to _Monitoring_ → _Maps_.
  2. Mark the checkboxes of the network maps to export.
  3. Click _Export_ below the list.

![](/documentation/current/assets/en/manual/xml_export_import/export_maps.png)

Depending on the selected format, maps are exported to a local file with a default name:

  * `zabbix_export_maps.yaml` \- in YAML export (default option for export);
  * `zabbix_export_maps.xml` \- in XML export;
  * `zabbix_export_maps.json` \- in JSON export.

#### Importing

To import network maps, do the following:

  1. Go to _Monitoring_ → _Maps_.
  2. Click _Import_ in the upper-right corner.
  3. Select the import file.
  4. Mark the required options in import rules.
  5. Click _Import_ in the lower-right corner of the configuration form.

![](/documentation/current/assets/en/manual/xml_export_import/import_maps.png)

Import rules:

_Update existing_ | Existing maps will be updated using data from the import file. Otherwise, they will not be updated.  
---|---  
_Create new_ | New maps will be created using data from the import file. Otherwise, they will not be created.  
  
If you uncheck both map options and check the respective options for images, images only will be imported. Image importing is only available to _Super admin_ users.

A success or failure message of the import will be displayed in the frontend.

If replacing an existing image, it will affect all maps that are using this image.

#### Export format

Export to YAML:
    
    
    zabbix_export:
             version: '7.4'
             images:
               - name: Zabbix_server_3D_(128)
                 imagetype: '1'
                 encodedImage: iVBOR...5CYII=
             maps:
               - name: 'Local network'
                 width: '680'
                 height: '200'
                 label_type: '0'
                 label_location: '0'
                 highlight: '1'
                 expandproblem: '1'
                 markelements: '1'
                 show_unack: '0'
                 severity_min: '0'
                 show_suppressed: '0'
                 grid_size: '50'
                 grid_show: '1'
                 grid_align: '1'
                 label_format: '0'
                 label_type_host: '2'
                 label_type_hostgroup: '2'
                 label_type_trigger: '2'
                 label_type_map: '2'
                 label_type_image: '2'
                 label_string_host: ''
                 label_string_hostgroup: ''
                 label_string_trigger: ''
                 label_string_map: ''
                 label_string_image: ''
                 expand_macros: '1'
                 background: {  }
                 iconmap: {  }
                 urls: {  }
                 selements:
                   - elementtype: '0'
                     elements:
                       - host: 'Zabbix server'
                     label: |
                       {HOST.NAME}
                       {HOST.CONN}
                     label_location: '0'
                     x: '111'
                     'y': '61'
                     elementsubtype: '0'
                     areatype: '0'
                     width: '200'
                     height: '200'
                     viewtype: '0'
                     use_iconmap: '0'
                     selementid: '1'
                     icon_off:
                       name: Zabbix_server_3D_(128)
                     icon_on: {  }
                     icon_disabled: {  }
                     icon_maintenance: {  }
                     urls: {  }
                     evaltype: '0'
                 shapes:
                   - type: '0'
                     x: '0'
                     'y': '0'
                     width: '680'
                     height: '15'
                     text: '{MAP.NAME}'
                     font: '9'
                     font_size: '11'
                     font_color: '000000'
                     text_halign: '0'
                     text_valign: '0'
                     border_type: '0'
                     border_width: '0'
                     border_color: '000000'
                     background_color: ''
                     zindex: '0'
                 lines: {  }
                 links: {  }

Copy

✔ Copied

### Exported elements

Exported elements are explained in the table below.

images |  | Root element for images.  
---|---|---  
| name | string | Unique image name.  
imagetype | integer | Image type.  
Possible values:  
1 - Image;  
2 - Background.  
encodedImage | string | Base64 encoded image.  
maps |  | Root element for maps.  
  
#### Maps

name | string | Unique map name.  
---|---|---  
width | integer | Map width, in pixels.  
height | integer | Map height, in pixels.  
label_type | integer | Map element label type.  
Possible values:  
0 - Label;  
1 - Host IP address;  
2 - Element name;  
3 - Status only;  
4 - Nothing.  
label_location | integer | Map element label location by default.  
Possible values:  
0 - Bottom;  
1 - Left;  
2 - Right;  
3 - Top.  
highlight | integer | Enable icon highlighting for active triggers and host statuses.  
Possible values:  
0 - No;  
1 - Yes.  
expandproblem | integer | Display problem trigger for elements with a single problem.  
Possible values:  
0 - No;  
1 - Yes.  
markelements | integer | Highlight map elements that have recently changed their status.  
Possible values:  
0 - No;  
1 - Yes.  
show_unack | integer | Problem display.  
Possible values:  
0 - Count of all problems;  
1 - Count of unacknowledged problems;  
2 - Count of acknowledged and unacknowledged problems separately.  
severity_min | integer | Minimum trigger severity to show on the map by default.  
Possible values:  
0 - Not classified;  
1 - Information;  
2 - Warning;  
3 - Average;  
4 - High;  
5 - Disaster.  
show_suppressed | integer | Display problems, which would otherwise be suppressed (not shown) because of host maintenance.  
Possible values:  
0 - No;  
1 - Yes.  
grid_size | integer | Cell size of a map grid in pixels.  
Supported if `grid_show` is set to `0`.  
Possible values: 20, 40, 50, 75 or 100.  
grid_show | integer | Display a grid in map configuration.  
Possible values:  
0 - Yes;  
1 - No.  
grid_align | integer | Automatically align icons in map configuration.  
Possible values:  
0 - Yes;  
1 - No.  
label_format | integer | Use advanced label configuration.  
Possible values:  
0 - No;  
1 - Yes.  
label_type_host | integer | Display label as host label.  
Supported if `label_format` is set to `1`.  
Possible values:  
0 - Label;  
1 - Host IP address;  
2 - Element name;  
3 - Status only;  
4 - Nothing;  
5 - Custom label.  
label_type_hostgroup | integer | Display label as host group label.  
Supported if `label_format` is set to `1`.  
Possible values:  
0 - Label;  
2 - Element name;  
3 - Status only;  
4 - Nothing;  
5 - Custom label.  
label_type_trigger | integer | Display label as trigger label.  
Supported if `label_format` is set to `1`.  
Possible values:  
0 - Label;  
2 - Element name;  
3 - Status only;  
4 - Nothing;  
5 - Custom label.  
label_type_map | integer | Display label as map label.  
Supported if `label_format` is set to `1`.  
Possible values:  
0 - Label;  
2 - Element name;  
3 - Status only;  
4 - Nothing;  
5 - Custom label.  
label_type_image | integer | Display label as image label.  
Supported if `label_format` is set to `1`.  
Possible values:  
0 - Label;  
2 - Element name;  
4 - Nothing;  
5 - Custom label.  
label_string_host | string | Custom label for host elements.  
Supported if `label_type_host` is set to `5`.  
label_string_hostgroup | string | Custom label for host group elements.  
Supported if `label_type_hostgroup` is set to `5`.  
label_string_trigger | string | Custom label for trigger elements.  
Supported if `label_type_trigger` is set to `5`.  
label_string_map | string | Custom label for map elements.  
Supported if `label_type_map` is set to `5`.  
label_string_image | string | Custom label for image elements.  
Supported if `label_type_image` is set to `5`.  
expand_macros | integer | Expand macros in labels in map configuration.  
Possible values:  
0 - No;  
1 - Yes.  
background |  | Root element for background image (if any).  
Supported if `imagetype` is set to `2`.  
| name | string | Background image name.  
iconmap |  | Root element for icon mapping (if any).  
| name | string | Icon mapping name.  
urls |  | Root element for URLs used by maps or each map element.  
| name | string | Link name.  
url | string | Link URL.  
elementtype | integer | Map item type the link belongs to.  
Possible values:  
0 - Host;  
1 - Map;  
2 - Trigger;  
3 - Host group;  
4 - Image.  
selements |  | Root element for map selements.  
shapes |  | Root element for map shapes.  
| type | integer | Shape type.  
Possible values:  
0 - Rectangle;  
1 - Ellipse.  
x | integer | X coordinates of the shape in pixels.  
y | integer | Y coordinates of the shape in pixels.  
width | integer | Shape width.  
height | integer | Shape height.  
text | string | Text inside of shape.  
font | integer | Text font style.  
Possible values:  
0 - Georgia, serif;  
1 - "Palatino Linotype", "Book Antiqua", Palatino, serif;  
2 - "Times New Roman", Times, serif;  
3 - Arial, Helvetica, sans-serif;  
4 - "Arial Black", Gadget, sans-serif;  
5 - "Comic Sans MS", cursive, sans-serif;  
6 - Impact, Charcoal, sans-serif;  
7 - "Lucida Sans Unicode", "Lucida Grande", sans-serif;  
8 - Tahoma, Geneva, sans-serif;  
9 - "Trebuchet MS", Helvetica, sans-serif;  
10 - Verdana, Geneva, sans-serif;  
11 - "Courier New", Courier, monospace;  
12 - "Lucida Console", Monaco, monospace.  
font_size | integer | Font size in pixels.  
font_color | string | Font color represented in hexadecimal code.  
text_halign | integer | Horizontal alignment of text.  
Possible values:  
0 - Center;  
1 - Left;  
2 - Right.  
text_valign | integer | Vertical alignment of text.  
Possible values:  
0 - Middle;  
1 - Top;  
2 - Bottom.  
border_type | integer | Type of the border for the shape.  
Possible values:  
0 - None;  
1 - Bold line;  
2 - Dotted line;  
3 - Dashed line.  
border_width | integer | Width of the border in pixels.  
border_color | string | Border color represented in hexadecimal code.  
background_color | string | Background (fill) color represented in hexadecimal code.  
zindex | integer | Value for ordering all shapes and lines (z-index).  
lines |  | Root element for map lines.  
| x1 | integer | X coordinates of the line point 1 in pixels.  
y1 | integer | Y coordinates of the line point 1 in pixels.  
x2 | integer | X coordinates of the line point 2 in pixels.  
y2 | integer | Y coordinates of the line point 2 in pixels.  
line_type | integer | Line type.  
Possible values:  
0 - None;  
1 - Bold line;  
2 - Dotted line;  
3 - Dashed line.  
line_width | integer | Line width in pixels.  
line_color | string | Line color represented in hexadecimal code.  
zindex | integer | Value for ordering all shapes and lines (z-index).  
links |  | Root element for links between map elements.  
| drawtype | integer | Link style.  
Possible values:  
0 - Line;  
2 - Bold line;  
3 - Dotted line;  
4 - Dashed line.  
color | string | Link color (6 symbols, hex).  
label | string | Link label.  
selementid1 | id | ID of one element to connect.  
selementid2 | id | ID of the other element to connect.  
linktriggers |  | Root element for link status indicators.  
  
See also: [Map object](/documentation/current/en/manual/api/reference/map/object) (refer to the relevant property with a matching name).

##### Map selements

elementtype | integer | Map element type.  
Possible values:  
0 - Host;  
1 - Map;  
2 - Trigger;  
3 - Host group;  
4 - Image.  
---|---|---  
elements |  | Root element for Zabbix entities (host, host group, map, etc.) that are represented on the map.  
All entities have their respective element (`host`, etc.; see, for example, Export format).  
label | string | Icon label.  
label_location | integer | Label location.  
Possible values:  
-1 - Use map default;  
0 - Bottom;  
1 - Left;  
2 - Right;  
3 - Top.  
x | integer | Location on the X axis.  
y | integer | Location on the Y axis.  
elementsubtype | integer | Element subtype.  
Supported if `elementtype` is set to `3`.  
Possible values:  
0 - Single host group;  
1 - All host groups.  
areatype | integer | Area size.  
Supported if `elementtype` is set to `1`.  
Possible values:  
0 - Same as whole map;  
1 - Custom size.  
width | integer | Width of area.  
Supported if `areatype` is set to `1`.  
height | integer | Height of area.  
Supported if `areatype` is set to `1`.  
viewtype | integer | Area placement algorithm.  
Supported if `elementsubtype` is set to `1`.  
Possible values:  
0 - Place evenly in the area.  
use_iconmap | integer | Use icon mapping for this element. Relevant only if icon mapping is activated on map level.  
Possible values:  
0 - No;  
1 - Yes.  
selementid | id | Unique element record ID.  
icon_off |  | Root element for image to use when element is in 'OK' status.  
| name | string | Unique image name.  
icon_on |  | Root element for image to use when element is in 'Problem' status.  
| name | string | Unique image name.  
icon_disabled |  | Root element for image to use when element is disabled.  
| name | string | Unique image name.  
icon_maintenance |  | Root element for image to use when element is in maintenance.  
| name | string | Unique image name.  
urls |  | Root element for URLs used by maps or each map element.  
| name | string | Link name.  
url | string | Link URL.  
evaltype | integer | Evaluation type for tags.  
tags |  | Root element for problem tags (for host and host group elements).  
If tags are given, only problems with these tags will be displayed on the map.  
| tag | string | Tag name.  
value | string | Tag value.  
operator | integer | Operator.  
  
See also: [Map element object](/documentation/current/en/manual/api/reference/map/object#map-element) (refer to the relevant property with a matching name).

##### Map link status indicators

drawtype | integer | Link style when trigger is in the 'Problem' state.  
Possible values:  
0 - Line;  
2 - Bold line;  
3 - Dotted line;  
4 - Dashed line.  
---|---|---  
color | string | Link color (6 symbols, hex) when trigger is in the 'Problem' state.  
trigger |  | Root element for trigger used to indicate link status.  
| description | string | Trigger name.  
expression | string | Trigger expression.  
recovery_expression | string | Trigger recovery expression.  
  
See also: [Map link trigger object](/documentation/current/en/manual/api/reference/map/object#map-link-trigger) (refer to the relevant property with a matching name).