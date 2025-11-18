---
title: Dashboards
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/dashboards
downloaded: 2025-11-14 10:37:58
---

# 1 Dashboards

#### Overview

The _Dashboards_ section is designed to display summaries of all the important information in a **dashboard**.

While only one dashboard can displayed at one time, it is possible to configure several dashboards. Each dashboard may contain one or several pages that can be rotated in a slideshow.

A dashboard page consists of widgets and each widget is designed to display information of a certain kind and source, which can be a summary, a map, a graph, the clock, etc.

Access to hosts in the widgets depends on host [permissions](/documentation/current/en/manual/config/users_and_usergroups/permissions#access-to-hosts).

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/dashboards/dashboard.png)

Pages and widgets are added to the dashboard and edited in the dashboard editing mode. Pages can be viewed and rotated in the dashboard viewing mode.

The time period that is displayed in graph widgets is controlled by the [_Time period_ selector](/documentation/current/en/manual/web_interface/time_period_selector) located above the widgets. The _Time period_ selector label, located to the right, displays the currently selected time period. Clicking the tab label allows expanding and collapsing the _Time period_ selector.

Note that when the dashboard is displayed in kiosk mode and widgets only are displayed, it is possible to zoom out the graph period by double-clicking in the graph.

##### Dashboard size

The minimum width of a dashboard is 1200 pixels. The dashboard will not shrink below this width; instead a horizontal scrollbar is displayed if the browser window is smaller than that.

The maximum width of a dashboard is the browser window width. Dashboard widgets stretch horizontally to fit the window. At the same time, a dashboard widget cannot be stretched horizontally beyond the window limits.

Horizontally, the dashboard is made up of 72 columns of always equal width that stretch/shrink dynamically (but not to less than 1200 pixels total).

Vertically, the dashboard may contain a maximum of 64 rows; each row has a fixed height of 70 pixels.

A widget may be therefore be up to 72 columns wide and 64 rows high.

#### Viewing dashboards

To view all configured dashboards, click on _All dashboards_ just below the section title.

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/dashboards/dashboards.png)

Dashboards are displayed with a sharing tag:

  * _My_ \- indicates a dashboard owned by the current user
  * _Shared_ \- indicates a public dashboard or a private dashboard shared with any user or user group

Note that the sharing tags are shown for the dashboards owned by the current user only. The dashboards owned by other users are listed without sharing tags.

The filter located to the right above the list allows to filter dashboards by name and by those created by the current user.

To delete one or several dashboards, mark the checkboxes of the respective dashboards and click on _Delete_ below the list.

#### Viewing a dashboard

To view a single dashboard, click on its name in the list of dashboards.

When **viewing** a dashboard, the following options are available:

![](/documentation/current/assets/en/manual/web_interface/dashboard_edit_button.png) | Switch to the dashboard **editing** mode.  
The editing mode is also opened when a new dashboard is being created and when you click on the ![](/documentation/current/assets/en/manual/web_interface/widget_edit.png) edit button of a widget.  
---|---  
![](/documentation/current/assets/en/manual/web_interface/dashboard_action_menu2.png) | Open the action menu (see action descriptions below).  
![](/documentation/current/assets/en/manual/web_interface/frontend_sections/dashboards/dashboard_view_actions.png) | _Sharing_ \- edit sharing preferences for the dashboard.  
_Create new_ \- create a new dashboard.  
_Clone_ \- create a new dashboard by copying properties of the existing one. First you are prompted to enter dashboard parameters. Then, the new dashboard opens in editing mode with all the widgets of the original dashboard.  
_Delete_ \- delete the dashboard.  
_Create new report_ \- open a pop-up window with report [configuration form](/documentation/current/en/manual/config/reports). Disabled if the user does not have permission to manage scheduled reports.  
_View related reports_ \- open a pop-up window with a list of existing reports based on the current dashboard. Disabled if there are no related reports or the user does not have permission to view scheduled reports.  
![](/documentation/current/assets/en/manual/web_interface/button_kiosk.png) | Display only page content ([kiosk mode](/documentation/current/en/manual/web_interface/frontend_sections/monitoring#view-mode-buttons)).  
Kiosk mode can also be accessed with the following URL parameters: `/zabbix.php?action=dashboard.view&kiosk=1`.  
To exit to normal mode: `/zabbix.php?action=dashboard.view&kiosk=0`  
  
##### Sharing

Dashboards can be made public or private.

Public dashboards are visible to all users. Private dashboards are visible only to their owner and to the users/user groups added in the sharing preferences.

To edit the sharing status of a dashboard, click on the _Sharing_ option in the action menu when viewing a single dashboard:

_Type_ | Select dashboard type:  
**Private** \- dashboard is visible only to selected user groups and users  
**Public** \- dashboard is visible to all  
---|---  
_List of user group shares_ | Select user groups that the dashboard is accessible to.  
You may allow read-only or read-write access.  
_List of user shares_ | Select users that the dashboard is accessible to.  
You may allow read-only or read-write access.  
  
See Permissions to dashboards to find out how sharing options limit the actions available to users.

#### Editing a dashboard

When **editing** a dashboard, the following options are available:

![](/documentation/current/assets/en/manual/web_interface/dashboard_properties.png) | Edit general dashboard parameters.  
---|---  
![](/documentation/current/assets/en/manual/web_interface/frontend_sections/dashboards/dashboard_add_button.png) | Add a new widget.  
Clicking on the arrow button will open the action menu (see action descriptions below).  
| ![](/documentation/current/assets/en/manual/web_interface/frontend_sections/dashboards/dashboard_edit_actions.png) | _Add widget_ \- add a new widget  
 _Add page_ \- add a new page  
 _Paste widget_ \- paste a copied widget. This option is grayed out if no widget has been copied. Only one entity (widget or page) can be copied at one time.  
_Paste page_ \- paste a copied page. This option is grayed out if no page has been copied.  
![](/documentation/current/assets/en/manual/web_interface/dashboard_save.png) | Save dashboard changes.  
![](/documentation/current/assets/en/manual/web_interface/dashboard_cancel.png) | Cancel dashboard changes.  
  
#### Creating a dashboard

It is possible to create a new dashboard in two ways:

  * Click on _Create dashboard_ , when viewing all dashboards
  * Select _Create new_ from the action menu, when viewing a single dashboard

You will be first asked to enter general dashboard parameters:

![dashboard_properties.png](/documentation/current/assets/en/manual/web_interface/frontend_sections/dashboards/dashboard_properties.png)

_Owner_ | Select system user that will be the dashboard owner.  
---|---  
_Name_ | Enter dashboard name.  
_Default page display period_ | Select period for how long a dashboard page is displayed before rotating to the next page in a slideshow.  
_Start slideshow automatically_ | Mark this checkbox to run a slideshow automatically one more than one dashboard page exists.  
  
When you click on _Apply_ , an empty dashboard is opened:

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/dashboards/dashboard_add.png)

To populate the dashboard, you can add widgets and pages.

Click on the _Save changes_ button to save the dashboard. If you click on _Cancel_ , the dashboard will not be created.

#### Adding widgets

You can add various [widgets](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets) (Action log, Clock, Discovery status, etc.) to a dashboard. Widgets can be added in two ways:

  * Click the _Add_ button or the arrow next to it, then select _Add widget_ from the action menu. After configuring the widget, it will be added in its default size and placed after any existing widget.

![](/documentation/current/assets/en/manual/web_interface/dashboard_add_button.png)

  * Move the mouse to an empty spot on the dashboard. Notice a placeholder appear, then click on it to open the widget configuration form. After configuring the widget, it will be added in its default size or resized to fit the available space. Alternatively, drag the placeholder to determine the widget size and release it to open the widget configuration form (if a widget is copied to the clipboard, you will first be prompted to choose between _Add widget_ or _Paste widget_).

![](/documentation/current/assets/en/manual/web_interface/dashboard_click.png) | ![](/documentation/current/assets/en/manual/web_interface/dashboard_select.png)  
---|---  
  
In the widget configuration form:

  1. Select the widget type.
  2. Configure widget parameters.
  3. Click _Add_ to add the widget to the dashboard.

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/dashboards/widget_add.png)

#### Editing widgets

Widgets can be resized and repositioned in dashboard editing mode by dragging their title bar. You can also reposition the widget configuration form by dragging its title bar.

Each widget includes controls in its upper-right corner:

  * ![](/documentation/current/assets/en/manual/web_interface/widget_edit.png) \- edit the widget
  * ![](/documentation/current/assets/en/manual/web_interface/button_widget_menu.png) \- open the widget menu

While editing, the widget is highlighted and changes are previewed in real time. If mandatory widget parameters are not configured, the widget enters the _Widget is not fully configured_ state.

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/dashboards/widget_edit.png)

After editing, click _Apply_ in the widget, then _Save changes_ in the upper-right corner of the dashboard to apply your changes.

#### Copying/pasting widgets

You can copy and paste dashboard widgets to quickly create new widgets with the same configuration. Widgets can be copy-pasted within the same dashboard or between dashboards opened in different tabs.

To copy a widget, use the widget menu. To paste a copied widget (available in dashboard editing mode):

  * Click the arrow next to the _Add_ button and select _Paste widget_.
  * Alternatively, click an empty area in the dashboard and select _Paste widget_.

You can also paste a copied widget over an existing widget using the _Paste_ option in its widget menu.

#### Creating a slideshow

A slideshow will run automatically if the dashboard contains two or more pages (see Adding pages) and if one of the following is true:

  * The _Start slideshow automatically_ option is marked in dashboard properties
  * The dashboard URL contains a `slideshow=1` parameter

The pages rotate according to the intervals given in the properties of the dashboard and individual pages. Click on:

  * _Stop slideshow_ \- to stop the slideshow
  * _Start slideshow_ \- to start the slideshow

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/dashboards/dashboard_page_tabs.png)

Slideshow-related controls are also available in kiosk mode (where only the page content is shown):

  * ![](/documentation/current/assets/en/manual/web_interface/frontend_sections/dashboards/slideshow_stop_kiosk.png) \- stop slideshow
  * ![](/documentation/current/assets/en/manual/web_interface/frontend_sections/dashboards/slideshow_start_kiosk.png) \- start slideshow
  * ![](/documentation/current/assets/en/manual/web_interface/frontend_sections/dashboards/slideshow_back_kiosk.png) \- go back one page
  * ![](/documentation/current/assets/en/manual/web_interface/frontend_sections/dashboards/slideshow_next_kiosk.png) \- go to the next page

#### Adding pages

To add a new page to a dashboard:

  * Make sure the dashboard is in the editing mode
  * Click on the arrow next to the _Add_ button and select the _Add page_ option

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/dashboards/dashboard_page_add.png)

  * Fill the general page parameters and click on _Apply_. If you leave the name empty, the page will be added with a `Page N` name where 'N' is the incremental number of the page. The page display period allows to customize how long a page is displayed in a slideshow.

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/dashboards/dashboard_page_properties.png)

A new page will be added, indicated by a new tab (_Page 2_).

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/dashboards/dashboard_page_new.png)

The pages can be reordered by dragging-and-dropping the page tabs. Reordering maintains the original page naming. It is always possible to go to each page by clicking on its tab.

When a new page is added, it is empty. You can add widgets to it as described above.

#### Copying/pasting pages

Dashboard pages can be copied and pasted, allowing to create a new page with the properties of an existing one. They can be pasted from the same dashboard or a different dashboard.

To paste an existing page to the dashboard, first copy it, using the page menu:

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/dashboards/dashboard_page_copy.png)

To paste the copied page:

  * Make sure the dashboard is in the editing mode
  * Click on the arrow next to the _Add_ button and select the _Paste page_ option

#### Page menu

The page menu can be opened by clicking on the three dots ![](/documentation/current/assets/en/manual/web_interface/frontend_sections/dashboards/dashboard_page_menu.png) next to the page name:

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/dashboards/page_menu.png)

It contains the following options:

  * _Copy_ \- copy the page
  * _Delete_ \- delete the page (pages can only be deleted in the dashboard editing mode)
  * _Properties_ \- customize the page parameters (the name and the page display period in a slideshow)

#### Widget menu

The widget menu contains different options based on whether the dashboard is in the edit or view mode:

In dashboard edit mode:  
![widget_menu_edit.png](/documentation/current/assets/en/manual/web_interface/widget_menu_edit.png) | _Copy_ \- copy the widget  
 _Paste_ \- paste a copied widget over this widget  
This option is grayed out if no widget has been copied.  
_Delete_ \- delete the widget  
---|---  
In dashboard view mode:  
![widget_menu_view.png](/documentation/current/assets/en/manual/web_interface/widget_menu_view.png) | _Copy_ \- copy the widget  
 _Download image_ \- download the widget as a PNG image  
(only available for [graph](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/graph)/[classic graph](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/graph_classic) widgets)  
_Refresh interval_ \- select the frequency of refreshing  
the widget contents  
  
#### Permissions to dashboards

Permissions to dashboards for regular users and users of 'Admin' type (provided the access to dashboards and the _Create and edit dashboards_ option are enabled for the [user role](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles#default-permissions) they are assigned) are limited in the way described below.

  * They can see and clone a public dashboard even when no users or user groups are added in the dashboard's sharing preferences.
  * They can see and clone a private dashboard if they have at least _Read_ rights to it set by means of the sharing preferences.
  * They can edit and delete a dashboard only if they have _Read-write_ rights to it set by means of the sharing preferences.
  * They cannot change the dashboard owner.