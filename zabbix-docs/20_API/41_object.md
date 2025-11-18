---
title: Dashboard object
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/dashboard/object
downloaded: 2025-11-14 10:40:34
---

# Dashboard object

The following objects are directly related to the `dashboard` API.

### Dashboard

The dashboard object has the following properties.

dashboardid | ID | ID of the dashboard.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
\- _required_ for update operations  
---|---|---  
name | string | Name of the dashboard.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
userid | ID | ID of the user that is the owner of the dashboard.  
private | integer | Type of dashboard sharing.  
  
Possible values:  
0 - public dashboard;  
1 - _(default)_ private dashboard.  
display_period | integer | Default page display period (in seconds).  
  
Possible values: 10, 30, 60, 120, 600, 1800, 3600.  
  
Default: 30.  
auto_start | integer | Auto start slideshow.  
  
Possible values:  
0 - do not auto start slideshow;  
1 - _(default)_ auto start slideshow.  
  
### Dashboard page

The dashboard page object has the following properties.

dashboard_pageid | ID | ID of the dashboard page.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
---|---|---  
name | string | Dashboard page name.  
  
Default: empty string.  
display_period | integer | Dashboard page display period (in seconds).  
  
Possible values: 0, 10, 30, 60, 120, 600, 1800, 3600.  
  
Default: 0 (will use the default page display period).  
widgets | array | Array of the [dashboard widget](object#dashboard-widget) objects.  
  
#### Dashboard widget

The dashboard widget object has the following properties.

widgetid | ID | ID of the dashboard widget.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
---|---|---  
type | string | Type of the dashboard widget.  
  
Possible values:  
actionlog - Action log;  
clock - Clock;  
discovery - Discovery status;  
favgraphs - Favorite graphs;  
favmaps - Favorite maps;  
gauge - Gauge;  
geomap - Geomap;  
graph - Graph (classic);  
graphprototype - Graph prototype;  
honeycomb - Honeycomb;  
hostavail - Host availability;  
hostcard - Host card;  
hostnavigator - Host navigator;  
itemcard - Item card;  
itemhistory - Item history;  
itemnavigator - Item navigator;  
item - Item value;  
map - Map;  
navtree - Map Navigation Tree;  
piechart - Pie chart;  
problemhosts - Problem hosts;  
problems - Problems;  
problemsbysv - Problems by severity;  
slareport - SLA report;  
svggraph - Graph;  
systeminfo - System information;  
tophosts - Top hosts;  
topitems - Top items;  
toptriggers - Top triggers;  
trigover - Trigger overview;  
url - URL;  
web - Web monitoring.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
name | string | Custom widget name.  
x | integer | A horizontal position from the left side of the dashboard.  
  
Possible values range from 0 to 71.  
y | integer | A vertical position from the top of the dashboard.  
  
Possible values range from 0 to 63.  
width | integer | The widget width.  
  
Possible values range from 1 to 72.  
height | integer | The widget height.  
  
Possible values range from 1 to 64.  
view_mode | integer | The widget view mode.  
  
Possible values:  
0 - _(default)_ default widget view;  
1 - with hidden header;  
fields | array | Array of the [dashboard widget field](object#dashboard-widget-field) objects.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- see individual widgets in [Dashboard widget fields](/documentation/current/en/manual/api/reference/dashboard/widget_fields)  
  
##### Dashboard widget field

The dashboard widget field object has the following properties.

type | integer | Type of the widget field.  
  
Possible values:  
0 - Integer;  
1 - String;  
2 - Host group;  
3 - Host;  
4 - Item;  
5 - Item prototype;  
6 - Graph;  
7 - Graph prototype;  
8 - Map;  
9 - Service;  
10 - SLA;  
11 - User;  
12 - Action;  
13 - Media type.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
name | string | Widget field name.  
  
Possible values: see [Dashboard widget fields](/documentation/current/en/manual/api/reference/dashboard/widget_fields).  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
value | mixed | Widget field value depending on the type.  
  
Possible values: see [Dashboard widget fields](/documentation/current/en/manual/api/reference/dashboard/widget_fields).  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
  
### Dashboard user group

List of dashboard permissions based on user groups. It has the following properties.

usrgrpid | ID | ID of the user group.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
permission | integer | Type of permission level.  
  
Possible values:  
2 - read only;  
3 - read-write.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
  
### Dashboard user

List of dashboard permissions based on users. It has the following properties.

userid | ID | ID of the user.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
permission | integer | Type of permission level.  
  
Possible values:  
2 - read only;  
3 - read-write.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_