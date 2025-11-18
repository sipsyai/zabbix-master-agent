---
title: Settings object
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/settings/object
downloaded: 2025-11-14 10:44:27
---

# Settings object

The following objects are directly related to the `settings` API.

### Settings

The settings object has the following properties.

default_lang | string | System language by default.  
  
Default: `en_US`.  
---|---|---  
default_timezone | string | System time zone by default.  
  
Default: `system` \- system default.  
  
For the full list of supported time zones please refer to [PHP documentation](https://www.php.net/manual/en/timezones.php).  
default_theme | string | Default theme.  
  
Possible values:  
`blue-theme` \- _(default)_ Blue;  
`dark-theme` \- Dark;  
`hc-light` \- High-contrast light;  
`hc-dark` \- High-contrast dark.  
search_limit | integer | Limit for search and filter results.  
  
Default: 1000.  
max_overview_table_size | integer | Max number of columns and rows in Data overview and Trigger overview dashboard widgets.  
  
Default: 50.  
max_in_table | integer | Max count of elements to show inside table cell.  
  
Default: 50.  
server_check_interval | integer | Show warning if Zabbix server is down.  
  
Possible values:  
0 - Do not show warning;  
10 - _(default)_ Show warning.  
work_period | string | Working time.  
  
Default: 1-5,09:00-18:00.  
show_technical_errors | integer | Show technical errors (PHP/SQL) to non-Super admin users and to users that are not part of user groups with debug mode enabled.  
  
Possible values:  
0 - _(default)_ Do not technical errors;  
1 - Show technical errors.  
history_period | string | Max period to display history data in Latest data, Web, and Data overview dashboard widgets.  
Accepts seconds and time unit with suffix.  
  
Default: 24h.  
period_default | string | Time filter default period.  
Accepts seconds and time unit with suffix with month and year support (30s, 1m, 2h, 1d, 1M, 1y).  
  
Default: 1h.  
max_period | string | Max period for time filter.  
Accepts seconds and time unit with suffix with month and year support (30s, 1m, 2h, 1d, 1M, 1y).  
  
Default: 2y.  
severity_color_0 | string | Color for "Not classified" severity as a hexadecimal color code.  
  
Default: 97AAB3.  
severity_color_1 | string | Color for "Information" severity as a hexadecimal color code.  
  
Default: 7499FF.  
severity_color_2 | string | Color for "Warning" severity as a hexadecimal color code.  
  
Default: FFC859.  
severity_color_3 | string | Color for "Average" severity as a hexadecimal color code.  
  
Default: FFA059.  
severity_color_4 | string | Color for "High" severity as a hexadecimal color code.  
  
Default: E97659.  
severity_color_5 | string | Color for "Disaster" severity as a hexadecimal color code.  
  
Default: E45959.  
severity_name_0 | string | Name for "Not classified" severity.  
  
Default: Not classified.  
severity_name_1 | string | Name for "Information" severity.  
  
Default: Information.  
severity_name_2 | string | Name for "Warning" severity.  
  
Default: Warning.  
severity_name_3 | string | Name for "Average" severity.  
  
Default: Average.  
severity_name_4 | string | Name for "High" severity.  
  
Default: High.  
severity_name_5 | string | Name for "Disaster" severity.  
  
Default: Disaster.  
custom_color | integer | Use custom event status colors.  
  
Possible values:  
0 - _(default)_ Do not use custom event status colors;  
1 - Use custom event status colors.  
ok_period | string | Display OK triggers period.  
Accepts seconds and time unit with suffix.  
  
Default: 5m.  
blink_period | string | On status change triggers blink period.  
Accepts seconds and time unit with suffix.  
  
Default: 2m.  
problem_unack_color | string | Color for unacknowledged PROBLEM events as a hexadecimal color code.  
  
Default: CC0000.  
problem_ack_color | string | Color for acknowledged PROBLEM events as a hexadecimal color code.  
  
Default: CC0000.  
ok_unack_color | string | Color for unacknowledged RESOLVED events as a hexadecimal color code.  
  
Default: 009900.  
ok_ack_color | string | Color for acknowledged RESOLVED events as a hexadecimal color code.  
  
Default: 009900.  
problem_unack_style | integer | Blinking for unacknowledged PROBLEM events.  
  
Possible values:  
0 - Do not show blinking;  
1 - _(default)_ Show blinking.  
problem_ack_style | integer | Blinking for acknowledged PROBLEM events.  
  
Possible values:  
0 - Do not show blinking;  
1 - _(default)_ Show blinking.  
ok_unack_style | integer | Blinking for unacknowledged RESOLVED events.  
  
Possible values:  
0 - Do not show blinking;  
1 - _(default)_ Show blinking.  
ok_ack_style | integer | Blinking for acknowledged RESOLVED events.  
  
Possible values:  
0 - Do not show blinking;  
1 - _(default)_ Show blinking.  
url | string | Frontend URL.  
discovery_groupid | ID | ID of the host group to which will be automatically placed discovered hosts.  
default_inventory_mode | integer | Default host inventory mode.  
  
Possible values:  
-1 - _(default)_ Disabled;  
0 - Manual;  
1 - Automatic.  
alert_usrgrpid | ID | ID of the user group to which will be sending database down alarm message.  
  
If set to "0", the alarm message will not be sent.  
snmptrap_logging | integer | Log unmatched SNMP traps.  
  
Possible values:  
0 - Do not log unmatched SNMP traps;  
1 - _(default)_ Log unmatched SNMP traps.  
login_attempts | integer | Number of failed login attempts after which login form will be blocked.  
  
Default: 5.  
login_block | string | Time interval during which login form will be blocked if number of failed login attempts exceeds defined in login_attempts field.  
Accepts seconds and time unit with suffix.  
  
Default: 30s.  
validate_uri_schemes | integer | Validate URI schemes.  
  
Possible values:  
0 - Do not validate;  
1 - _(default)_ Validate.  
uri_valid_schemes | string | Valid URI schemes.  
  
Default: http,https,ftp,file,mailto,tel,ssh.  
x_frame_options | string | X-Frame-Options HTTP header.  
  
Default: SAMEORIGIN.  
iframe_sandboxing_enabled | integer | Use iframe sandboxing.  
  
Possible values:  
0 - Do not use;  
1 - _(default)_ Use.  
iframe_sandboxing_exceptions | string | Iframe sandboxing exceptions.  
connect_timeout | string | Connection timeout with Zabbix server.  
  
Possible values range: 1-30s.  
  
Default: 3s.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
socket_timeout | string | Network default timeout.  
  
Possible values range: 1-300s.  
  
Default: 3s.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
media_type_test_timeout | string | Network timeout for media type test.  
  
Possible values range: 1-300s.  
  
Default: 65s.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
item_test_timeout | string | Network timeout for item tests.  
  
Possible value range: 1-600s.  
  
Default: 60s.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
script_timeout | string | Network timeout for script execution.  
  
Possible values range: 1-300s.  
  
Default: 60s.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
report_test_timeout | string | Network timeout for scheduled report test.  
  
Possible values range: 1-300s.  
  
Default: 60s.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
auditlog_enabled | integer | Whether to enable audit logging.  
  
Possible values:  
0 - Disable;  
1 - _(default)_ Enable.  
auditlog_mode | integer | Whether to enable audit logging of low-level discovery, network discovery and autoregistration activities performed by the server (System user).  
  
Possible values:  
0 - Disable;  
1 - _(default)_ Enable.  
ha_failover_delay | string | Failover delay in seconds.  
  
Default: 1m.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
geomaps_tile_provider | string | Geomap tile provider.  
  
Possible values:  
`OpenStreetMap.Mapnik` \- _(default)_ OpenStreetMap Mapnik;  
`OpenTopoMap` \- OpenTopoMap;  
`Stamen.TonerLite` \- Stamen Toner Lite;  
`Stamen.Terrain` \- Stamen Terrain;  
`USGS.USTopo` \- USGS US Topo;  
`USGS.USImagery` \- USGS US Imagery.  
  
Supports empty string to specify custom values of `geomaps_tile_url`, `geomaps_max_zoom` and `geomaps_attribution`.  
geomaps_tile_url | string | Geomap tile URL.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `geomaps_tile_provider` is set to empty string  
geomaps_max_zoom | integer | Geomap max zoom level.  
  
Possible values: 0-30.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `geomaps_tile_provider` is set to empty string  
geomaps_attribution | string | Geomap attribution text.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `geomaps_tile_provider` is set to empty string  
vault_provider | integer | Vault provider.  
  
Possible values:  
0 - _(default)_ HashiCorp Vault;  
1 - CyberArk Vault.  
proxy_secrets_provider | integer | Resolve secret macro values by:  
  
Possible values:  
0 - _(default)_ server only;  
1 - server and proxies independently.  
timeout_zabbix_agent | string | Spend no more than `timeout_*` seconds on processing.  
Accepts seconds or time unit with suffix (e.g., 30s, 1m). Also accepts user macros.  
  
Possible values range: 1-600s.  
  
Default: 3s.  
Default for `timeout_browser`: 60s.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
timeout_simple_check  
timeout_snmp_agent  
timeout_external_check  
timeout_db_monitor  
timeout_http_agent  
timeout_ssh_agent  
timeout_telnet_agent  
timeout_script  
timeout_browser