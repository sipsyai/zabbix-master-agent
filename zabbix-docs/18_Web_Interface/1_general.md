---
title: General
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/administration/general
downloaded: 2025-11-14 10:39:26
---

# 1 General

#### Overview

The _Administration → General_ section contains a number of subsections for setting frontend-related defaults and customizing Zabbix.

The list of available subsections appears upon pressing on _General_ in the _Administration_ menu section. It is also possible to switch between subsections by using the title dropdown in the upper-left corner.

#### GUI

This section provides customization of several frontend-related defaults.

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/administration/general_gui.png)

Configuration parameters:

_Default language_ | Default language for users who have not specified a language in their profiles and guest users.  
For more information, see [Installation of additional frontend languages](/documentation/current/en/manual/appendix/install/locales).  
---|---  
_Default time zone_ | Default [time zone](/documentation/current/en/manual/web_interface/time_zone#overview) for users who have not specified a time zone in their profiles and guest users.  
_Default theme_ | Default theme for users who have not specified a theme in their profiles and guest users.  
_Limit for search and filter results_ | Maximum amount of elements (rows) that will be displayed in a web-interface list, for example, in _Data collection > Hosts_.  
_Note_ : If set to, for example, '50', only the first 50 elements will be displayed in all affected frontend lists. If some list contains more than fifty elements, the indication of that will be the '+' sign in _"Displaying 1 to 50 of**50+** found"_. Also, if filtering is used and still there are more than 50 matches, only the first 50 will be displayed.  
Note that increasing the value of this parameter may lead to decreased performance and increased memory consumption on the web server side.  
_Max number of columns  
and rows in overview tables_ | Maximum number of columns and rows to display in the _Trigger overview_ dashboard widget. The same limit applies to both columns and rows. If more rows and/or columns than shown exist, the system will display a warning at the bottom of the table: "Not all results are displayed. Please provide more specific search criteria."  
_Max count of elements  
to show inside table cell_ | For entries that are displayed in a single table cell, no more than configured here will be shown.  
_Show warning if Zabbix server is down_ | This parameter enables a warning message to be displayed in a browser window if the Zabbix server cannot be reached (possibly down). The message remains visible even if the user scrolls down the page. When hovered over, the message is temporarily hidden to reveal the contents underneath it.  
_Working time_ | This system-wide parameter defines working hours. In graphs, working time is displayed as a white background and non-working time is displayed as gray.  
See [Time period specification](/documentation/current/en/manual/appendix/time_period) page for description of the time format.  
[User macros](/documentation/current/en/manual/config/macros/user_macros) are supported.  
_Show technical errors_ | If checked, all registered users will be able to see technical errors (PHP/SQL). If unchecked, the information is only available to [Zabbix Super Admins](/documentation/current/en/manual/web_interface/frontend_sections/users/user_list#users-1) and users belonging to the user groups with enabled [debug mode](/documentation/current/en/manual/web_interface/debug_mode).  
_Max history display period_ | Maximum time period for which to display historical data in _Monitoring > Latest data_, host [web scenario](/documentation/current/en/manual/web_interface/frontend_sections/monitoring/hosts/web) information in _Monitoring > Hosts_, and in the _Top items_ dashboard widget.  
Allowed range: 24 hours (default) - 1 week. [Time suffixes](/documentation/current/en/manual/appendix/suffixes), e.g. 1w (one week), 36h (36 hours), are supported.  
_Time filter default period_ | Time period to be used in graphs and dashboards by default. Allowed range: 1 minute - 10 years (default: 1 hour).  
[Time suffixes](/documentation/current/en/manual/appendix/suffixes), e.g. 10m (ten minutes), 5w (five weeks), are supported.  
Note: when a user changes the time period while viewing a graph, this time period is stored as user preference, replacing the global default or a previous user selection.  
_Max period for time selector_ | Maximum available time period for graphs and dashboards. Users will not be able to visualize older data. Allowed range: 1 year - 10 years (default: 2 years).  
[Time suffixes](/documentation/current/en/manual/appendix/suffixes), e.g. 1y (one year), 365w (365 weeks), are supported.  
  
#### Autoregistration

In this section, you can configure the encryption level for active agent autoregistration.

![adm_autoreg2.png](/documentation/current/assets/en/manual/web_interface/frontend_sections/administration/adm_autoreg2.png)

Parameters marked with an asterisk are mandatory.

Configuration parameters:

_Encryption level_ | Select one or both options for encryption level:  
**No encryption** \- unencrypted connections are allowed  
**PSK** \- TLS encrypted connections with a pre-shared key are allowed  
---|---  
_PSK identity_ | Enter the pre-shared key identity string.  
This field is only available if 'PSK' is selected as _Encryption level_.  
Do not put sensitive information in the PSK identity, it is transmitted unencrypted over the network to inform a receiver which PSK to use.  
_PSK_ | Enter the pre-shared key (an even number of hexadecimal characters).  
Maximum length: 512 hex-digits (256-byte PSK) if Zabbix uses GnuTLS or OpenSSL library, 64 hex-digits (32-byte PSK) if Zabbix uses mbed TLS (PolarSSL) library.  
Example: 1f87b595725ac58dd977beef14b97461a7c1045b9a1c963065002c5473194952  
This field is only available if 'PSK' is selected as _Encryption level_.  
  
See also: [Secure autoregistration](/documentation/current/en/manual/discovery/auto_registration#secure-autoregistration)

#### Timeouts

In this section, it is possible to set global item-type timeouts and network timeouts. All fields in this form are mandatory.

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/administration/global_timeout.png)

_Timeouts for item types_ | How many seconds to wait for a response from a monitored item (based on its type).  
Allowed range: 1 - 600s (default: 3s; default for [Browser](/documentation/current/en/manual/config/items/itemtypes/browser) item type: 60s).  
[Time suffixes](/documentation/current/en/manual/appendix/suffixes#time-suffixes), e.g. 30s, 1m, and [user macros](/documentation/current/en/manual/config/macros/user_macros) are supported.  
  
Supported item types:  
\- [Zabbix agent](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent) (both passive and active checks)  
\- [Simple check](/documentation/current/en/manual/config/items/itemtypes/simple_checks) (except `icmpping*`, `vmware.*` items)  
\- [SNMP agent](/documentation/current/en/manual/config/items/itemtypes/snmp) (only for SNMP `walk[OID]` and `get[OID]` items)  
\- [External check](/documentation/current/en/manual/config/items/itemtypes/external)  
\- [Database monitor](/documentation/current/en/manual/config/items/itemtypes/odbc_checks)  
\- [HTTP agent](/documentation/current/en/manual/config/items/itemtypes/http)  
\- [SSH agent](/documentation/current/en/manual/config/items/itemtypes/ssh_checks)  
\- [TELNET agent](/documentation/current/en/manual/config/items/itemtypes/telnet_checks)  
\- [Script](/documentation/current/en/manual/config/items/itemtypes/script)  
\- [Browser](/documentation/current/en/manual/config/items/itemtypes/browser)  
  
Note that if a proxy is used and has timeouts [configured](/documentation/current/en/manual/distributed_monitoring/proxies#adding-proxies), the timeout settings of the proxy will override the global ones. If there are timeouts set for specific [items](/documentation/current/en/manual/config/items/item#configuration), they will override the proxy and global settings.  
---|---  
_Network timeouts for UI_  
| _Communication_ | How many seconds to wait before closing an idle socket (if a connection to Zabbix server has been established earlier, but frontend cannot finish data reading/sending operation during this time, the connection will be dropped). Allowed range: 1 - 300s (default: 3s).  
_Connection_ | How many seconds to wait before stopping an attempt to connect to Zabbix server. Allowed range: 1 - 30s (default: 3s).  
_Media type test_ | How many seconds to wait for a response when testing a media type. Allowed range: 1 - 300s (default: 65s).  
_Script execution_ | How many seconds to wait for a response when executing a script. Allowed range: 1 - 300s (default: 60s).   
This timeout is for the entire script execution chain, which can be of various length. For example, if the script is executed on the agent, it is a roundtrip through server (possibly also proxy) to the agent and back.  
For scripts that are executed on the agent, the [server](/documentation/current/en/manual/appendix/config/zabbix_server#timeout) or [proxy](\(/manual/appendix/config/zabbix_proxy#timeout\)) timeout applies.  
For scripts that are executed on an active agent only, it is likely that the default server/proxy timeout must be raised. The server/proxy timeout must be higher than the active check refresh frequency, otherwise the server/proxy timeout may be exceeded before the active agent even receives the script.  
See also: [Script timeout](/documentation/current/en/manual/web_interface/frontend_sections/alerts/scripts#script-timeout)  
_Item test_ | How many seconds to wait for returned data when testing an item. Allowed range: 1 - 600s (default: 60s).  
_Scheduled report test_ | How many seconds to wait for returned data when testing a scheduled report. Allowed range: 1 - 300s (default: 60s).  
  
#### Images

The Images section displays all the images available in Zabbix. Images are stored in the database.

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/administration/general_images.png)

The _Type_ dropdown allows you to switch between icon and background images:

  * Icons are used to display [network map](/documentation/current/en/manual/config/visualization/maps/map) elements
  * Backgrounds are used as background images of network maps

**Adding image**

You can add your own image by clicking on the _Create icon_ or _Create background_ button in the upper-right corner.

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/administration/general_img_upload.png)

Image attributes:

_Name_ | Unique name of an image.  
---|---  
_Upload_ | Select the file (PNG, JPEG, GIF) from a local system to be uploaded to Zabbix.  
_Note_ that it may be possible to upload other formats that will be converted to PNG during upload. GD library is used for image processing, therefore formats that are supported depend on the library version used (2.0.28 or higher is required by Zabbix).  
  
Maximum size of the upload file is limited by the value of ZBX_MAX_IMAGE_SIZE that is 1024x1024 bytes or 1 MB.  
  
The upload of an image may fail if the image size is close to 1 MB and the `max_allowed_packet` MySQL configuration parameter is at a default of 1MB. In this case, increase the [max_allowed_packet](http://dev.mysql.com/doc/refman/5.5/en/server-system-variables.html#sysvar_max_allowed_packet) parameter.

#### Icon mapping

This section allows creating the mapping of certain hosts with certain icons. Host inventory field information is used to create the mapping.

The mappings can then be used in [network map configuration](/documentation/current/en/manual/config/visualization/maps/map) to assign appropriate icons to matching hosts automatically.

To create a new icon map, click on _Create icon map_ in the upper-right corner.

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/administration/general_icon_map.png)

Configuration parameters:

_Name_ | Unique name of icon map.  
---|---  
_Mappings_ | A list of mappings. The order of mappings determines which one will have priority. You can move mappings up and down the list with drag-and-drop.  
_Inventory field_ | Host inventory field that will be looked into to seek a match.  
_Expression_ | Regular expression describing the match.  
_Icon_ | Icon to use if a match for the expression is found.  
_Default_ | Default icon to use.  
  
#### Regular expressions

This section allows creating custom regular expressions that can be used in several places in the frontend. See [Regular expressions](/documentation/current/en/manual/regular_expressions) section for details.

#### Trigger displaying options

This section allows customizing how trigger status is displayed in the frontend and [trigger severity](/documentation/current/en/manual/config/triggers/severity) names and colors.

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/administration/general_triggers.png)

_Use custom event status colors_ | Checking this parameter turns on the customization of colors for acknowledged/unacknowledged problems.  
---|---  
_Unacknowledged PROBLEM events_ ,  
_Acknowledged PROBLEM events_ ,  
_Unacknowledged RESOLVED events_ ,  
_Acknowledged RESOLVED events_ | Enter new color code or click on the color to select a new one from the provided palette.  
If _blinking_ checkbox is marked, triggers will blink for some time upon the status change to become more visible.  
_Display OK triggers for_ | Time period for displaying OK triggers. Allowed range: 0 - 24 hours. [Time suffixes](/documentation/current/en/manual/appendix/suffixes), e.g. 5m, 2h, 1d, are supported.  
_On status change triggers blink for_ | Length of trigger blinking. Allowed range: 0 - 24 hours. [Time suffixes](/documentation/current/en/manual/appendix/suffixes), e.g. 5m, 2h, 1d, are supported.  
_Not classified_ ,  
_Information_ ,  
_Warning_ ,  
_Average_ ,  
_High_ ,  
_Disaster_ | Custom severity names and/or colors to display instead of system default.  
Enter new color code or click on the color to select a new one from the provided palette.  
  
Note that custom severity names entered here will be used in all locales. If you need to translate them to other languages for certain users, see [Customizing trigger severities](/documentation/current/en/manual/config/triggers/customseverities) page.  
  
#### Geographical maps

This section allows selecting geographical map tile service provider and configuring service provider settings for the Geomap [dashboard widget](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/geomap). To provide visualization using the geographical maps, Zabbix uses open-source JavaScript interactive maps library Leaflet. Please note that Zabbix has no control over the quality of images provided by third-party tile providers, including the predefined tile providers.

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/administration/geo_maps.png)

Tile provider | Select one of the available tile service providers or select _Other_ to add another tile provider or self-hosted tiles (see Using a custom tile service provider).  
---|---  
Tile URL | The URL template (up to 2048 characters) for loading and displaying the tile layer on geographical maps.  
This field is editable only if _Tile provider_ is set to _Other_.  
  
The following placeholders are supported:  
_{s}_ represents one of the available subdomains;  
_{z}_ represents zoom level parameter in the URL;  
_{x}_ and _{y}_ represent tile coordinates;  
_{r}_ can be used to add "@2x" to the URL to load retina tiles.  
  
Example: `https://{s}.example.com/{z}/{x}/{y}{r}.png`  
Attribution text | Tile provider attribution text to be displayed in a small text box on the map. This field is visible only if _Tile provider_ is set to _Other_.  
Max zoom level | Maximum zoom level of the map. This field is editable only if _Tile provider_ is set to _Other_.  
  
##### Using a custom tile service provider

The Geomap widget is capable to load raster tile images from a custom self-hosted or a third-party tile provider service. To use a custom third-party tile provider service or a self-hosted tile folder or server, select _Other_ in the _Tile provider_ field and specify the custom URL in the _Tile URL_ field using proper placeholders.

#### Modules

This section allows to administer custom, as well as built-in [frontend modules](/documentation/current/en/manual/extensions/frontendmodules).

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/administration/general_modules.png)

Click on _Scan directory_ to register/unregister any custom modules. Registered modules will appear in the list; unregistered modules will be removed from the list.

Click on the module status in the list to enable/disable a module. You may also mass enable/disable modules by selecting them in the list and then clicking on the _Enable/Disable_ buttons below the list.

Click on the module name in the list to view its [details](/documentation/current/en/devel/modules/file_structure/manifest) in a pop-up window.

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/administration/general_modules_details.png)

Module status can also be updated in the module details pop-up window; to do this, mark/unmark the _Enabled_ checkbox and then click on _Update_.

You may filter modules by name or status (enabled/disabled).

#### Connectors

This section allows to configure connectors for Zabbix data [streaming to external systems](/documentation/current/en/manual/config/export/streaming) over HTTP.

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/administration/general_connectors.png)

Click on _Create connector_ to configure a new [connector](/documentation/current/en/manual/config/export/streaming#configuration).

You may filter connectors by name or status (enabled/disabled). Click on the connector status in the list to enable/disable a connector. You may also mass enable/disable connectors by selecting them in the list and then clicking on the _Enable/Disable_ buttons below the list.

#### Other

This section allows configuring miscellaneous other frontend parameters.

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/administration/general_other.png)

_Frontend URL_ | URL (up to 2048 characters) to Zabbix web interface.  
This parameter is used by Zabbix web service for communication with frontend and should be specified to enable scheduled reports.  
---|---  
_Group for discovered hosts_ | Hosts discovered by [network discovery](/documentation/current/en/manual/discovery/network_discovery) and [agent autoregistration](/documentation/current/en/manual/discovery/auto_registration) will be automatically placed in the host group, selected here.  
_Default host inventory mode_ | Default [mode](/documentation/current/en/manual/config/hosts/inventory) for host inventory. It will be followed whenever a new host or host prototype is created by server or frontend unless overridden during host discovery/autoregistration by the _Set host inventory mode_ operation.  
_User group for database down message_ | User group for sending alarm message or 'None'.  
Zabbix server depends on the availability of the backend database. It cannot work without a database. If the database is down, selected users can be notified by Zabbix. Notifications will be sent to the user group set here using the enabled user media entries. Notifications are transmitted using the following [media types](/documentation/current/en/manual/config/notifications/media) (when enabled): email; SMS; custom alert scripts. Even if a webhook media entry is configured and enabled, it will not trigger notifications.  
Zabbix server will not stop; it will wait until the database is back again to continue processing.  
Notification consists of the following content:  
`[MySQL|PostgreSQL] database <DB Name> [on <DB Host>:<DB Port>] is not available: <error message depending on the type of DBMS (database)>`  
<DB Host> is not added to the message if it is defined as an empty value and <DB Port> is not added if it is the default value ("0"). The alert manager (a special Zabbix server process) tries to establish a new connection to the database every 10 seconds. If the database is still down the alert manager repeats sending alerts, but not more often than every 15 minutes.  
_Log unmatched SNMP traps_ | Log [SNMP trap](/documentation/current/en/manual/config/items/itemtypes/snmptrap) if no corresponding SNMP interfaces have been found.  
  
##### Authorization

_Login attempts_ | Number of unsuccessful login attempts before the possibility to log in gets blocked.  
---|---  
_Login blocking interval_ | Period of time for which logging in will be prohibited when _Login attempts_ limit is exceeded. Allowed range: 0 - 3600 seconds. [Time suffixes](/documentation/current/en/manual/appendix/suffixes), e.g. 90s, 5m, 1h, are supported.  
  
##### Storage of secrets

_Vault provider_ | Select the secret management software for storing [user macro](/documentation/current/en/manual/config/macros/user_macros#configuration) values - _HashiCorp Vault_ (default) or _CyberArk Vault_.  
---|---  
_Resolve secret vault macros by_ | Resolve secret vault macros by:  
**Zabbix server** \- secrets are retrieved by Zabbix server and forwarded to proxies when needed (default);  
**Zabbix server and proxy** \- secrets are retrieved by both Zabbix server and proxies, allowing them to resolve macros independently.  
  
See also: [Storage of secrets](/documentation/current/en/manual/config/secrets).

##### Security

_Validate URI schemes_ | Unmark this checkbox to disable URI scheme validation (enabled by default).  
If marked, you can specify a comma-separated list of allowed URI schemes (default: http,https,ftp,file,mailto,tel,ssh). Applies to all fields in the frontend where URIs are used (for example, map element URLs).  
---|---  
_Use X-Frame-Options HTTP header_ | Unmark this checkbox to disable the HTTP X-Frame-options header (not recommended).  
If marked, you can specify the value of the HTTP X-Frame-options header. Supported values:  
**SAMEORIGIN** (default) or **'self'** (must be single-quoted) - the page can only be displayed in a frame on the same origin as the page itself;  
**DENY** or **'none'** (must be single-quoted) - the page cannot be displayed in a frame, regardless of the site attempting to do so;  
**a string of space-separated hostnames** ; adding **'self'** (must be single-quoted) to the list allows the page to be displayed in a frame on the same origin as the page itself.  
Note that using **'self'** or **'none'** without single quotes will result in them being regarded as hostnames.  
_Use iframe sandboxing_ | Unmark this checkbox to disable putting the retrieved URL content into sandbox (not recommended).  
If marked, you can specify the iframe sandboxing exceptions; unspecified restrictions will still be applied. If this field is empty, all sandbox attribute restrictions apply.  
For more information, see the description of the [`sandbox`](https://www.w3.org/TR/2010/WD-html5-20100624/the-iframe-element.html#attr-iframe-sandbox) attribute.