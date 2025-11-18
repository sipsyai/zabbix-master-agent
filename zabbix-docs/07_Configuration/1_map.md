---
title: Configuring a network map
source: https://www.zabbix.com/documentation/current/en/manual/config/visualization/maps/map
downloaded: 2025-11-14 10:35:53
---

# 1 Configuring a network map

#### Overview

Configuring a map in Zabbix requires that you first create a map by defining its general parameters and then you start filling the actual map with elements and their links.

You can populate the map with elements that are a host, a host group, a trigger, an image, or another map.

Icons are used to represent map elements. You can define the information that will be displayed with the icons and set that recent problems are displayed in a special way. You can link the icons and define information to be displayed on the links.

You can add custom URLs to be accessible by clicking on the icons. Thus you may link a host icon to host properties or a map icon to another map.

The problem count in maps is displayed for cause problems only.

Maps are managed in _Monitoring_ → _[Maps](/documentation/current/en/manual/web_interface/frontend_sections/monitoring/maps)_ , where they can be configured, managed and viewed. In the monitoring view, you can click on the icons and take advantage of the links to some scripts and URLs.

Network maps are based on vector graphics (SVG).

#### Public and private maps

All users in Zabbix (including non-admin users) can create network maps. Maps have an owner - the user who created them. Maps can be made public or private.

  * _Public_ maps are visible to all users, although to see it the user must have read access to at least one map element. Public maps can be edited in case a user/ user group has read-write permissions for this map and at least read permissions to all elements of the corresponding map including triggers in the links.

  * _Private_ maps are visible only to their owner and the users/user groups the map is [shared](/documentation/current/en/manual/config/visualization/maps/map) with by the owner. Regular (non-Super admin) users can only share with the groups and users they are members of. Admin level users can see private maps regardless of being the owner or belonging to the shared user list. Private maps can be edited by the owner of the map and in case a user/ user group has read-write permissions for this map and at least read permissions to all elements of the corresponding map including triggers in the links.

Map elements that the user does not have read permission to are displayed with a grayed-out icon and all textual information on the element is hidden. However, the trigger label is visible even if the user has no permission to the trigger.

To add an element to the map the user must also have at least read permission to the element.

#### Creating a map

To create a map, do the following:

  * Go to _Monitoring → Maps_
  * Go to the view with all maps
  * Click on _Create map_

You can also use the _Clone_ button in the configuration form of an existing map to create a new map. This map will have all of the properties of the existing map, including general layout attributes, as well as the elements of the existing map.

The **Map** tab contains general map attributes:

![](/documentation/current/assets/en/manual/config/visualization/map_config.png)

All mandatory input fields are marked with a red asterisk.

General map attributes:

_Owner_ | Name of map owner.  
---|---  
_Name_ | Unique map name.  
_Width_ | Map width in pixels.  
_Height_ | Map height in pixels.  
_Background image_ | Use background image:  
**No image** \- no background image (white background)  
**Image** \- selected image to be used as a background image. You may use a geographical map or any other image to enhance your map.  
_Background scale_ | Use background scaling:  
**None** \- no scaling;  
**Proportionally** \- cover the entire map background, but keep the image proportions (default).  
_Automatic icon mapping_ | You can set to use an automatic icon mapping, configured in _Administration → General → Icon mapping_. Icon mapping allows mapping certain icons against certain host inventory fields.  
_Icon highlight_ | If you check this box, map elements will be highlighted.  
Elements with an active trigger will receive a round background, in the same color as the highest severity trigger. Moreover, a thick green line will be displayed around the circle, if all problems are acknowledged.  
Elements with "disabled" or "in maintenance" status will get a square background, gray and orange respectively.  
See also: [Viewing maps](/documentation/current/en/manual/web_interface/frontend_sections/monitoring/maps#viewing-maps)  
_Mark elements on trigger status change_ | A recent change of trigger status (recent problem or resolution) will be highlighted with markers (inward-pointing red triangles) on the three sides of the element icon that are free of the label. Markers are displayed for 30 minutes.  
_Display problems_ | Select how problems are displayed with a map element:  
**Expand single problem** \- if there is only one problem, the problem name is displayed. Otherwise, the total number of problems is displayed.  
**Number of problems** \- the total number of problems is displayed  
**Number of problems and expand most critical one** \- the name of the most critical problem and the total number of problems is displayed.  
'Most critical' is determined based on problem severity and, if equal, problem event ID (higher ID or later problem displayed first). For a _trigger map element_ it is based on problem severity and if equal, trigger position in the trigger list. In case of multiple problems of the same trigger, the most recent one will be displayed.  
_Advanced labels_ | If you check this box you will be able to define separate label types for separate element types.  
_Map element label type_ | Label type used for map elements:  
**Label** \- map element label  
**IP address** \- IP address  
**Element name** \- element name (for example, host name)  
**Status only** \- status only (OK or PROBLEM)  
**Nothing** \- no labels are displayed  
_Map element label location_ | Label location in relation to the map element:  
**Bottom** \- beneath the map element  
**Left** \- to the left  
**Right** \- to the right  
**Top** \- above the map element  
_Show map element labels_ | Select how to display map element labels:  
**Always** \- always displayed (default);  
**Auto hide** \- hide the label if it's not hovered on or selected.  
_Show link labels_ | Select how to display link labels:  
**Always** \- always displayed (default);  
**Auto hide** \- hide the label if it's not hovered on or selected.  
_Problem display_ | Display problem count as:  
**All** \- full problem count will be displayed  
**Separated** \- unacknowledged problem count will be displayed separated as a number of the total problem count  
**Unacknowledged only** \- only the unacknowledged problem count will be displayed  
_Minimum trigger severity_ | Problems below the selected minimum severity level will not be displayed on the map.  
For example, with _Warning_ selected, changes with _Information_ and _Not classified_ level triggers will not be reflected in the map.  
_Show suppressed problems_ | Mark the checkbox to display problems that would otherwise be suppressed (not shown) because of host maintenance.  
_URLs_ | URLs (up to 2048 characters) for each element type can be defined. A label for the URL can also be defined. These will be displayed as links when a user clicks on the element in the map viewing mode.  
Macros can be used in map URL names and values. For a full list, see [supported macros](/documentation/current/en/manual/appendix/macros/supported_by_location) and search for 'map URL names and values'.  
  
#### Sharing

The **Sharing** tab contains the map type as well as sharing options (user groups, users) for private maps:

![](/documentation/current/assets/en/manual/config/visualization/map_config2.png)

_Type_ | Select map type:  
**Private** \- map is visible only to selected user groups and users  
**Public** \- map is visible to all  
---|---  
_List of user group shares_ | Select user groups that the map is accessible to.  
You may allow read-only or read-write access.  
_List of user shares_ | Select users that the map is accessible to.  
You may allow read-only or read-write access.  
  
When you click on _Add_ to save this map, you have created an empty map with a name, dimensions, and certain preferences. Now you need to add some elements. For that, click on _Edit_ in the map list to open the editable area.

#### Adding elements

To add an element, click on _Add_ next to `Map element`. The new element will appear at the upper-left corner of the map. Drag and drop it wherever you like.

Note that with the Grid option "On", elements will always align to the grid (you can pick various grid sizes from the dropdown, also hide/show the grid). If you want to put elements anywhere without alignment, turn the option to "Off". (You can align random elements to the grid later, by clicking on _Align map elements_.)

Now that you have some elements in place, you may want to start differentiating them by giving names, etc. By clicking on the element, a form is displayed and you can set the element type, give a name, choose a different icon, etc.

![](/documentation/current/assets/en/manual/config/visualization/map_element.png)

Map element attributes:

_Type_ | Type of the element:  
**Host** \- icon representing status of all triggers of the selected host  
**Map** \- icon representing status of all elements of a map  
**Trigger** \- icon representing status of one or more triggers  
**[Host group](/documentation/current/en/manual/config/visualization/maps/host_groups)** \- icon representing status of all triggers of all hosts belonging to the selected group  
**Image** \- an icon, not linked to any resource  
---|---  
_Label_ | Icon label, any string.  
Macros and multiline strings can be used.  
Expression [macros](/documentation/current/en/manual/appendix/macros/supported_by_location) are supported in this field, but only with `avg`, `last`, `min` and `max` functions, with time as parameter (for example, `{?avg(/host/key,1h)}`).  
For a full list of supported macros, see [supported macros](/documentation/current/en/manual/appendix/macros/supported_by_location) and search for 'map element labels'.  
_Show label_ | Select how to display the element label:  
**Default** \- use _Show map element labels_ settings from map configuration (default);  
**Always** \- always displayed (default);  
**Auto hide** \- hide the label if it's not hovered on or selected.  
_Label location_ | Label location in relation to the icon:  
**Default** \- map's default label location  
**Bottom** \- beneath the icon  
**Left** \- to the left  
**Right** \- to the right  
**Top** \- above the icon  
_Host_ | Enter the host if the element type is 'Host'. This field is auto-complete so starting to type the name of a host will offer a dropdown of matching hosts. Scroll down to select. Click on 'x' to remove the selected.  
_Map_ | Select the map if the element type is 'Map'. This field is auto-complete so starting to type the name of a map will offer a dropdown of matching maps. Scroll down to select. Click on 'x' to remove the selected.  
_Triggers_ | If the element type is 'Trigger', select one or more triggers in the _New triggers_ field below and click on _Add_.  
The order of selected triggers can be changed, but only within the same severity of triggers. Multiple trigger selection also affects {HOST.*} macro resolution both in the editing and view modes.  
// 1 In editing mode// the first displayed {HOST.*} macros will be resolved depending on the first trigger in the list (based on trigger severity).  
// 2 View mode// depends on the [Display problems](/documentation/current/en/manual/config/visualization/maps/map#creating-a-map) parameter in General map attributes.  
* If _Expand single problem_ mode is chosen, the first displayed {HOST.*} macros will be resolved depending on the latest detected problem trigger (not mattering the severity) or the first trigger in the list (in case no problem detected);  
* If _Number of problems and expand most critical one_ mode is chosen, the first displayed {HOST.*} macros will be resolved depending on the trigger severity.  
  
_Host group_ | Enter the host group if the element type is 'Host group'. This field is auto-complete so starting to type the name of a group will offer a dropdown of matching groups. Scroll down to select. Click on 'x' to remove the selected.  
_Tags_ | Specify tags to limit the number of problems displayed in the widget. It is possible to include as well as exclude specific tags and tag values. Several conditions can be set. Tag name matching is always case-sensitive.  
There are several operators available for each condition:  
**Exists** \- include the specified tag names  
**Equals** \- include the specified tag names and values (case-sensitive)  
**Contains** \- include the specified tag names where the tag values contain the entered string (substring match, case-insensitive)  
**Does not exist** \- exclude the specified tag names  
**Does not equal** \- exclude the specified tag names and values (case-sensitive)  
**Does not contain** \- exclude the specified tag names where the tag values contain the entered string (substring match, case-insensitive)  
There are two calculation types for conditions:  
**And/Or** \- all conditions must be met, conditions having the same tag name will be grouped by the Or condition  
**Or** \- enough if one condition is met  
This field is available for host and host group element types.  
_Automatic icon selection_ | In this case an icon mapping will be used to determine which icon to display.  
_Icons_ | You can choose to display different icons for the element in these cases: default, problem, maintenance, disabled.  
_Coordinate X_ | X coordinate of the map element.  
_Coordinate Y_ | Y coordinate of the map element.  
_URLs_ | Element-specific URLs (up to 2048 characters) can be set for the element. A label for the URL can also be defined. These will be displayed as links when a user clicks on the element in the map viewing mode. If the element has its own URLs and there are map level URLs for its type defined, they will be combined in the same menu.  
Macros can be used in map element names and values. For a full list, see [supported macros](/documentation/current/en/manual/appendix/macros/supported_by_location) and search for 'map URL names and values'.  
  
Added elements are not automatically saved. If you navigate away from the page, all changes may be lost.

Therefore it is a good idea to click on the **Update** button in the upper-right corner. Once clicked, the changes are saved regardless of what you choose in the following popup.

Selected grid options are also saved with each map.

#### Selecting elements

To select elements, select one and then hold down _Ctrl_ to select the others.

You can also select multiple elements by dragging a rectangle in the editable area and selecting all elements in it.

Once you select more than one element, the element property form shifts to the mass-update mode so you can change attributes of selected elements in one go. To do so, mark the attribute using the checkbox and enter a new value for it. You may use macros here (for example, {HOST.NAME} for the element label).

![](/documentation/current/assets/en/manual/config/visualization/map_update.png)

#### Linking elements

Once you have put some elements on the map, it is time to start linking them. To link two elements you must first select them. With the elements selected, click on _Add_ next to Link.

With a link created, the single element form now contains an additional _Links_ section. Click on _Edit_ to edit link attributes.

![](/documentation/current/assets/en/manual/config/visualization/map_links.png)

Link attributes:

_Label_ | Label that will be rendered on top of the link.  
Expression [macros](/documentation/current/en/manual/appendix/macros/supported_by_location) are supported in this field, but only with `avg`, `last`, `min` and `max` functions, with time as parameter (for example, `{?avg(/host/key,1h)}`).  
---|---  
_Show label_ | Select how to display the link label:  
**Default** \- use _Show map element labels_ settings from map configuration (default);  
**Always** \- always displayed (default);  
**Auto hide** \- hide the label if it's not hovered on or selected.  
_Connect to_ | The element that the link connects to.  
_Type (OK)_ | Default link style:  
**Line** \- single line  
**Bold line** \- bold line  
**Dot** \- dots  
**Dashed line** \- dashed line  
_Color (OK)_ | Default link color.  
_Indicator type_ | Select the link indicator type:  
**Static link** \- no indicators;  
**Trigger** \- allow trigger-based link indicators;  
**Item value** \- allow item value-based link indicators.  
_Item_ | Select the item. The value of this item will affect the link style.  
This field is only available if "Item value" is selected in the _Indicator type_ field.  
_[Indicators](links)_ | List of link indicators.  
  
**Triggers**  
If "Trigger" is selected in the _Indicator type_ field, click on _Add_ to add triggers. Select the trigger style (color, line type). In case a trigger has status PROBLEM, its style will be applied to the link.  
  
**Item value thresholds/patterns**  
If "Item value" is selected in the _Indicator type_ field, add item value thresholds (for a numeric item) or patterns (for a text item). Select the style of threshold/pattern (color, line type). If the item value reaches the specified threshold (or matches the pattern), its style will be applied to the link.  
  
#### Moving and copy-pasting elements

Several selected elements can be **moved** to another place in the map by clicking on one of the selected elements, holding down the mouse button, and moving the cursor to the desired location.

One or more elements can be **copied** by selecting the elements, then clicking on a selected element with the right mouse button and selecting _Copy_ from the menu.

![](/documentation/current/assets/en/manual/config/visualization/map_copy.png)

To paste the elements, click on a map area with the right mouse button and select _Paste_ from the menu. The _Paste without external links_ option will paste the elements retaining only the links that are between the selected elements.

Copy-pasting works within the same browser window. Keyboard shortcuts are not supported.

#### Ordering elements

To bring one element in front of the other (or vice versa) click on the element with the right mouse button and select _Bring forward_ /_Bring to front_ or _Send backward_ /_Send to back_.

![](/documentation/current/assets/en/manual/config/visualization/map_element_menu.png)

#### Adding shapes

In addition to map elements, it is also possible to add some shapes. Shapes are not map elements; they are just a visual representation. For example, a rectangle shape can be used as a background to group some hosts. Rectangle and ellipse shapes can be added.

To add a shape, click on _Add_ next to Shape. The new shape will appear at the upper-left corner of the map. Drag and drop it wherever you like.

A new shape is added with default colors. By clicking on the shape, a form is displayed and you can customize the way a shape looks, add text, etc.

![](/documentation/current/assets/en/manual/config/visualization/map_shape.png)

To select shapes, select one and then hold down _Ctrl_ to select the others. With several shapes selected, common properties can be mass updated, similarly as with elements.

Text can be added in the shapes. Expression [macros](/documentation/current/en/manual/appendix/macros/supported_by_location) are supported in the text, but only with `avg`, `last`, `min` and `max` functions, with time as parameter (for example, `{?avg(/host/key,1h)}`).

To display text only, the shape can be made invisible by removing the shape border (select 'None' in the _Border_ field). For example, take note of how the {MAP.NAME} macro, visible in the screenshot above, is actually a rectangle shape with text, which can be seen when clicking on the macro:

![](/documentation/current/assets/en/manual/config/visualization/map_name_macro.png)

{MAP.NAME} resolves to the configured map name when viewing the map.

If hyperlinks are used in the text, they become clickable when viewing the map.

Line wrapping for text is always "on" within shapes. However, within an ellipse, the lines are wrapped as though the ellipse were a rectangle. Word wrapping is not implemented, so long words (words that do not fit the shape) are not wrapped, but are masked (on map editing page) or clipped (other pages with maps).

#### Adding lines

In addition to shapes, it is also possible to add some lines. Lines can be used to link elements or shapes in a map.

To add a line, click on _Add_ next to Shape. A new shape will appear at the upper-left corner of the map. Select it and click on _Line_ in the editing form to change the shape into a line. Then adjust line properties, such as line type, width, color, etc.

![map_line.png](/documentation/current/assets/en/manual/config/visualization/map_line.png)

#### Ordering shapes and lines

To bring one shape in front of the other (or vice versa) click on the shape with the right mouse button bringing up the map shape menu.

![](/documentation/current/assets/en/manual/config/visualization/map_shape_menu.png)