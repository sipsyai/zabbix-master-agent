---
title: Hosts
source: https://www.zabbix.com/documentation/current/en/manual/xml_export_import/hosts
downloaded: 2025-11-14 10:37:11
---

# 4 Hosts

#### Overview

Hosts are [exported](/documentation/current/en/manual/xml_export_import) with many related objects and object relations.

Host export contains:

  * Linked [host groups](/documentation/current/en/manual/xml_export_import/hostgroups)
  * Host data
  * Template linkage
  * Host group linkage
  * Host interfaces
  * Directly linked items
  * Directly linked triggers
  * Directly linked discovery rules with all prototypes
  * Directly linked web scenarios
  * Host macros
  * Host inventory data
  * Value maps
  * Linked [graphs](/documentation/current/en/manual/xml_export_import/hosts#host-graphs)

#### Exporting

To export hosts, do the following:

  1. Go to _Data collection_ → _Hosts_.
  2. Mark the checkboxes of the hosts to export.
  3. Click _Export_ below the list.

![](/documentation/current/assets/en/manual/xml_export_import/export_hosts.png)

Depending on the selected format, hosts are exported to a local file with a default name:

  * `zabbix_export_hosts.yaml` \- in YAML export (default option for export);
  * `zabbix_export_hosts.xml` \- in XML export;
  * `zabbix_export_hosts.json` \- in JSON export.

#### Importing

To import hosts, do the following:

  1. Go to _Data collection_ → _Hosts_.
  2. Click _Import_ in the upper-right corner.
  3. Select the import file.
  4. Click _Import_ in the lower-right corner of the configuration form.

![](/documentation/current/assets/en/manual/xml_export_import/import_hosts.png)

If you mark the _Advanced options_ checkbox, a detailed list of all importable elements will be displayed - mark or unmark each import rule as required.

If you click the checkbox in the _All_ row, all elements below it will be marked/unmarked.

Import rules:

_Update existing_ | Existing elements will be updated using data from the import file. Otherwise, they will not be updated.  
---|---  
_Create new_ | New elements will be created using data from the import file. Otherwise, they will not be created.  
_Delete missing_ | Existing elements not present in the import file will be removed. Otherwise, they will not be removed.  
If _Delete missing_ is marked for _Template linkage_ , current template linkage not present in the import file will be unlinked. Entities (items, triggers, graphs, etc.) inherited from the unlinked templates will not be removed (unless the _Delete missing_ option is selected for each entity as well).  
  
A success or failure message of the import will be displayed in the frontend.

#### Export format

When a host is exported, Zabbix generates a structured YAML, JSON, or XML format. The export includes host elements, such as host metadata, items, macros, triggers, and more.

Each element serves a specific purpose and may contain nested elements.

The following sections describe each element in the export format. The examples use a host with the [MySQL by Zabbix agent 2](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/db/mysql_agent2) template. For element demonstration purposes, the template is unlinked after the host is created. Unlinking keeps all elements in the configuration (unlike unlinking and clearing, which removes them).

An ellipsis `(...)` indicates elements omitted for brevity. The note `(see table below)` is used when the element is explained in more detail in later sections.

## Host metadata
    
    
    zabbix_export:
             version: '7.4'
             host_groups:
               - uuid: 748ad4d098d447d492bb935c907f652f
                 name: Databases
             hosts: (see table below)
             graphs: (see table below)

Copy

✔ Copied

version | string | (required) Zabbix version.  
---|---|---  
host_groups |  | (required) Root element for host groups.  
| uuid | string | (required) Unique identifier for this host group.  
name | string | (required) Host group name.  
hosts |  | Root element for hosts.  
graphs |  | Root element for host graphs.  
  
### Hosts
    
    
    zabbix_export:
             (...)
             hosts:
               - host: 'MySQL server'
                 name: 'MySQL server'
                 groups:
                   - name: Databases
                 interfaces: (see table below)
                 items: (see table below)
                 discovery_rules: (see table below)
                 tags:
                   - tag: location
                     value: Riga
                 macros:
                   (...)
                   - macro: '{$MYSQL.DSN}'
                     value: 192.0.2.0
                   (...)
                   - macro: '{$MYSQL.PASSWORD}'
                     type: SECRET_TEXT
                     description: 'MySQL user password.'
                   (...)
                 valuemaps: (see table below)
             (...)

Copy

✔ Copied

host | string | (required) Unique host name.  
---|---|---  
name | string | Visible host name.  
description | text | Host description.  
monitored_by | string | How the host is monitored.  
Possible values:1 SERVER (0, default), PROXY (1), or PROXY_GROUP (2).  
proxy |  | Root element for proxy.  
| name | string | (required) Name of the proxy (if any) that monitors the host.  
proxy_group |  | Root element for proxy group.  
| name | string | (required) Name of the proxy group (if any) that is used to monitor the host.  
status | string | Host status.  
Possible values:1 ENABLED (0, default), DISABLED (1).  
ipmi_authtype | string | IPMI session authentication type.  
Possible values:1 DEFAULT (-1, default), NONE (0), MD2 (1), MD5 (2), STRAIGHT (4), OEM (5), RMCP_PLUS (6).  
ipmi_privilege | string | IPMI session privilege level.  
Possible values:1 CALLBACK (1), USER (2, default), OPERATOR (3), ADMIN (4), OEM (5).  
ipmi_username | string | Username for IPMI checks.  
ipmi_password | string | Password for IPMI checks.  
templates |  | Root element for linked templates.  
| name | string | (required) Template name.  
groups |  | Root element for host groups to which the host belongs.  
| name | string | (required) Host group name.  
interfaces |  | Root element for host interfaces.  
items |  | Root element for host items.  
discovery_rules |  | Root element for host low-level discovery rules.  
http_tests |  | Root element for host web scenarios.  
tags |  | Root element for host tags.  
| tag | string | (required) Tag name.  
value | string | Tag value.  
macros |  | Root element for host macros.  
| macro | string | (required) User macro name.  
type | string | User macro type.  
Possible values:1 TEXT (0, default), SECRET_TEXT (1), VAULT (2).  
value | string | User macro value.  
description | string | User macro description.  
inventory |  | Root element for host inventory.  
| <inventory_property> | string | Inventory property. All properties have their respective element (`type`, `name`, `os`, etc.; for example, see Export format).  
inventory_mode | string | Inventory mode.  
Possible values:1 DISABLED (-1), MANUAL (0, default), AUTOMATIC (1).  
valuemaps |  | Root element for host value maps.  
  
See also: [Host object](/documentation/current/en/manual/api/reference/host/object) (refer to the relevant property with a matching name).

#### Host interfaces
    
    
    zabbix_export:
             (...)
             hosts:
               - host: 'MySQL server'
                 (...)
                 interfaces:
                   - ip: 192.0.2.0
                     interface_ref: if1
                 (...)

Copy

✔ Copied

default | string | Whether this is the primary host interface. Note that there can be only one primary interface of one type on a host.  
Possible values:1 NO (0), YES (1, default).  
---|---|---  
type | string | Interface type.  
Possible values:1 ZABBIX (1, default), SNMP (2), IPMI (3), JMX (4).  
useip | string | Whether to use IP as the interface for connecting to the host (otherwise, DNS will be used).  
Possible values:1 NO (0), YES (1, default).  
ip | string | (required for IP connections) IP address (IPv4 or IPv6).  
dns | string | (required for DNS connections) DNS name.  
port | string | Port number.  
details |  | Root element for interface details.  
| version | string | Use this SNMP version.  
Possible values:1 SNMPV1 (1), SNMP_V2C (2, default), SNMP_V3 (3).  
community | string | (required for SNMPv1 and SNMPv2 items) SNMP community.  
max_repetitions | string | Max repetition value for native SNMP bulk requests (GetBulkRequest-PDUs).  
Supported for SNMPv2 and SNMPv3 items (`discovery[]` and `walk[]` items).  
Default: 10.  
contextname | string | SNMPv3 context name.  
Supported for SNMPv3 items.  
securityname | string | SNMPv3 security name.  
Supported for SNMPv3 items.  
securitylevel | string | SNMPv3 security level.  
Supported for SNMPv3 items.  
Possible values:1 NOAUTHNOPRIV (0, default), AUTHNOPRIV (1), AUTHPRIV (2).  
authprotocol | string | SNMPv3 authentication protocol.  
Supported for SNMPv3 items.  
Possible values:1 MD5 (0, default), SHA1 (1), SHA224 (2), SHA256 (3), SHA384 (4), SHA512 (5).  
authpassphrase | string | SNMPv3 authentication passphrase.  
Supported for SNMPv3 items.  
privprotocol | string | SNMPv3 privacy protocol.  
Supported for SNMPv3 items.  
Possible values:1 DES (0, default), AES128 (1), AES192 (2), AES256 (3), AES192C (4), AES256C (5).  
privpassphrase | string | SNMPv3 privacy passphrase.  
Supported for SNMPv3 items.  
bulk | string | Use bulk requests for SNMP.  
Possible values:1 NO (0), YES (1, default).  
interface_ref | string | Interface reference name to be used in items (format: `if<N>`).  
  
See also: [Host interface object](/documentation/current/en/manual/api/reference/hostinterface/object) (refer to the relevant property with a matching name).

#### Host items
    
    
    zabbix_export:
             (...)
             hosts:
               - host: 'MySQL server'
                 (...)
                 items:
                   (...)
                   - name: 'Binlog cache disk use'
                     type: DEPENDENT
                     key: mysql.binlog_cache_disk_use
                     value_type: FLOAT
                     description: 'Number of transactions that used a temporary disk cache because they could not fit in the regular binary log cache, being larger than `binlog_cache_size`.'
                     preprocessing: (see table below)
                     master_item:
                       key: 'mysql.get_status_variables["{$MYSQL.DSN}","{$MYSQL.USER}","{$MYSQL.PASSWORD}"]'
                     tags:
                       - tag: component
                         value: cache
                   (...)
                   - name: 'Buffer pool utilization'
                     type: CALCULATED
                     key: mysql.buffer_pool_utilization
                     value_type: FLOAT
                     units: '%'
                     params: |
                       ( last(//mysql.innodb_buffer_pool_pages_total) - 
                       last(//mysql.innodb_buffer_pool_pages_free) ) / 
                       ( last(//mysql.innodb_buffer_pool_pages_total) + 
                       ( last(//mysql.innodb_buffer_pool_pages_total) = 0 ) ) * 100 * 
                       ( last(//mysql.innodb_buffer_pool_pages_total) > 0 )
                     description: 'Ratio of used to total pages in the buffer pool.'
                     tags:
                       - tag: component
                         value: memory
                     triggers: (see table below)
                   (...)
                   - name: Uptime
                     type: DEPENDENT
                     key: mysql.uptime
                     units: uptime
                     description: 'Number of seconds that the server has been up.'
                     preprocessing: (see table below)
                     master_item:
                       key: 'mysql.get_status_variables["{$MYSQL.DSN}","{$MYSQL.USER}","{$MYSQL.PASSWORD}"]'
                     tags:
                       - tag: component
                         value: application
                     triggers: (see table below)
                   (...)

Copy

✔ Copied

name | string | (required) Item name.  
---|---|---  
type | string | Item type.  
Possible values:1 ZABBIX_PASSIVE (0, default), TRAP (2), SIMPLE (3), INTERNAL (5), ZABBIX_ACTIVE (7), EXTERNAL (10), ODBC (11), IPMI (12), SSH (13), TELNET (14), CALCULATED (15), JMX (16), SNMP_TRAP (17), DEPENDENT (18), HTTP_AGENT (19), SNMP_AGENT (20), ITEM_TYPE_SCRIPT (21), ITEM_TYPE_BROWSER (22), ITEM_TYPE_NESTED (23).  
snmp_oid | string | (required for SNMP_AGENT items) SNMP object ID.  
key | string | (required) Item key.  
delay | string | Update interval of the item.  
Default: 1m. The value will always be 0 for TRAP items.  
history | string | Time period (using [time suffix](/documentation/current/en/manual/appendix/suffixes#time-suffixes), [user macro](/documentation/current/en/manual/config/macros/user_macros) or [LLD macro](/documentation/current/en/manual/config/macros/lld_macros)) of how long the history data should be stored.  
Default: 31d.  
trends | string | Time period (using [time suffix](/documentation/current/en/manual/appendix/suffixes#time-suffixes), [user macro](/documentation/current/en/manual/config/macros/user_macros) or [LLD macro](/documentation/current/en/manual/config/macros/lld_macros)) of how long the trends data should be stored.  
Default: 365d.  
status | string | Item status.  
Possible values:1 ENABLED (0, default), DISABLED (1).  
value_type | string | Received value type.  
Possible values:1 FLOAT (0), CHAR (1), LOG (2), UNSIGNED (3, default), TEXT (4), BINARY (5).  
allowed_hosts | string | List of comma-delimited IP addresses of hosts allowed to send data for the item.  
Supported for TRAP and HTTP_AGENT items.  
units | string | Received value units (bps, B, etc.).  
params | text | Additional parameters depending on the type of the item (executed script for SSH and TELNET items; SQL query for ODBC items; formula for CALCULATED items; the script for ITEM_TYPE_SCRIPT and ITEM_TYPE_BROWSER items).  
ipmi_sensor | string | IPMI sensor.  
Supported for IPMI items.  
authtype | string | Authentication type.  
Supported for SSH and HTTP_AGENT items.  
Possible values for SSH items:1 PASSWORD (0, default), PUBLIC_KEY (1).  
Possible values for HTTP_AGENT items:1 NONE (0, default), BASIC (1), NTLM (2).  
username | string | (required for SSH and TELNET items) Username for authentication.  
Supported for SIMPLE, ODBC, JMX and HTTP_AGENT items.  
When used for JMX items, `password` (see below) should also be specified or both elements should be left blank.  
password | string | (required for SSH and TELNET items) Password for authentication.  
Supported for SIMPLE, ODBC, JMX and HTTP_AGENT items.  
When used for JMX items, `username` (see above) should also be specified or both elements should be left blank.  
publickey | string | (required for SSH items) Name of the public key file.  
privatekey | string | (required for SSH items) Name of the private key file.  
description | text | Item description.  
inventory_link | string | Host inventory field that is populated by the item.  
Possible values:1 NONE (0), ALIAS (4), etc. (see [Host inventory](/documentation/current/en/manual/api/reference/host/object#host-inventory) for supported fields).  
valuemap |  | Root element for item value maps.  
| name | string | (required) Name of the value map to use for the item.  
logtimefmt | string | Format of the time in log entries.  
Supported for items of LOG value type.  
preprocessing |  | Root element for item value preprocessing.  
| step |  | Root element for host item value preprocessing steps.  
interface_ref | string | Reference to the host interface (format: `if<N>`).  
jmx_endpoint | string | JMX endpoint.  
Supported for JMX items.  
master_item |  | (required for DEPENDENT items) Root element for dependent item's master item.  
| key | string | (required) Dependent item's master item key.  
timeout | string | Item data polling request timeout.  
Supported for the [Timeouts](/documentation/current/en/manual/web_interface/frontend_sections/administration/general#timeouts) list of item types.  
url | string | (required for HTTP_AGENT items) URL string.  
query_fields |  | Root element for query parameters.  
Supported for HTTP_AGENT items.  
| name | string | (required for HTTP_AGENT items) Query parameter name.  
value | string | Query parameter value.  
Supported for HTTP_AGENT items.  
parameters |  | Root element for user-defined parameters.  
Supported for ITEM_TYPE_SCRIPT and ITEM_TYPE_BROWSER items.  
| name | string | (required for ITEM_TYPE_SCRIPT and ITEM_TYPE_BROWSER items) User-defined parameter name.  
value | string | User-defined parameter value.  
Supported for ITEM_TYPE_SCRIPT and ITEM_TYPE_BROWSER items.  
posts | string | HTTP(S) request body data.  
Supported for HTTP_AGENT items.  
status_codes | string | Ranges of required HTTP status codes, separated by commas.  
Supported for HTTP_AGENT items.  
follow_redirects | string | Follow response redirects while polling data.  
Supported for HTTP_AGENT items.  
Possible values:1 NO (0), YES (1, default).  
post_type | string | Type of post data body.  
Supported for HTTP_AGENT items.  
Possible values:1 RAW (0, default), JSON (2), XML (3).  
http_proxy | string | HTTP(S) proxy connection string.  
Supported for HTTP_AGENT items.  
headers |  | Root element for HTTP(S) request headers.  
Supported for HTTP_AGENT items.  
| name | string | (required for HTTP_AGENT items) Header name.  
value | string | (required for HTTP_AGENT items) Header value.  
retrieve_mode | string | What part of response should be stored.  
Supported for HTTP_AGENT items.  
Possible values:1 BODY (0, default), HEADERS (1), BOTH (2).  
request_method | string | Request method type.  
Supported for HTTP_AGENT items.  
Possible values:1 GET (0, default), POST (1), PUT (2), HEAD (3).  
output_format | string | How to process response.  
Supported for HTTP_AGENT items.  
Possible values:1 RAW (0, default), JSON (1).  
allow_traps | string | Allow to populate value similarly to the trapper item.  
Supported for HTTP_AGENT items.  
Possible values:1 NO (0, default), YES (1).  
ssl_cert_file | string | Public SSL Key file path.  
Supported for HTTP_AGENT items.  
ssl_key_file | string | Private SSL Key file path.  
Supported for HTTP_AGENT items.  
ssl_key_password | string | Password for SSL Key file.  
Supported for HTTP_AGENT items.  
verify_peer | string | Whether to validate that the host's certificate is authentic.  
Supported for HTTP_AGENT items.  
Possible values:1 NO (0, default), YES (1).  
verify_host | string | Whether to validate that the host name for the connection matches the one in the host's certificate.  
Supported for HTTP_AGENT items.  
Possible values:1 NO (0, default), YES (1).  
tags |  | Root element for item tags.  
| tag | string | (required) Tag name.  
value | string | Tag value.  
triggers |  | Root element for host item triggers.  
  
See also: [Item object](/documentation/current/en/manual/api/reference/item/object) (refer to the relevant property with a matching name).

##### Host item value preprocessing steps
    
    
    zabbix_export:
             (...)
             hosts:
               - host: 'MySQL server'
                 (...)
                 items:
                   (...)
                   - name: 'Binlog cache disk use'
                     (...)
                     preprocessing:
                       - type: JSONPATH
                         parameters:
                           - $.Binlog_cache_disk_use
                       - type: DISCARD_UNCHANGED_HEARTBEAT
                         parameters:
                           - 6h
                     (...)

Copy

✔ Copied

type | string | (required) The item value preprocessing step type.  
Possible values:1 MULTIPLIER (1), RTRIM (2), LTRIM (3), TRIM (4), REGEX (5), BOOL_TO_DECIMAL (6), OCTAL_TO_DECIMAL (7), HEX_TO_DECIMAL (8), SIMPLE_CHANGE (9, calculated: received value - previous value), CHANGE_PER_SECOND (10, calculated: (received value - previous value)/(time now - time of last check)), XMLPATH (11), JSONPATH (12), IN_RANGE (13), MATCHES_REGEX (14), NOT_MATCHES_REGEX (15), CHECK_JSON_ERROR (16), CHECK_XML_ERROR (17), CHECK_REGEX_ERROR (18), DISCARD_UNCHANGED (19), DISCARD_UNCHANGED_HEARTBEAT (20), JAVASCRIPT (21), PROMETHEUS_PATTERN (22), PROMETHEUS_TO_JSON (23), CSV_TO_JSON (24), STR_REPLACE (25), CHECK_NOT_SUPPORTED (26), XML_TO_JSON (27), SNMP_WALK_VALUE (28), SNMP_WALK_TO_JSON (29), SNMP_GET_VALUE (30).  
---|---|---  
parameters |  | (required) Root element for parameters of the item value preprocessing step.  
| parameter | string | Individual parameter of the item value preprocessing step.  
error_handler | string | Action type used in case of preprocessing step failure.  
Possible values:1 ORIGINAL_ERROR (0, default), DISCARD_VALUE (1), CUSTOM_VALUE (2), CUSTOM_ERROR (3).  
error_handler_params | string | Error handler parameters.  
  
See also: [Item preprocessing object](/documentation/current/en/manual/api/reference/item/object#item-preprocessing) (refer to the relevant property with a matching name).

##### Host item triggers
    
    
    zabbix_export:
             (...)
             hosts:
               - host: 'MySQL server'
                 (...)
                 items:
                   (...)
                   - name: Uptime
                     (...)
                     triggers:
                       - expression: 'nodata(/MySQL server/mysql.uptime,30m)=1'
                         name: 'MySQL: Failed to fetch info data'
                         event_name: 'MySQL: Failed to fetch info data (or no data for 30m)'
                         priority: INFO
                         description: 'Zabbix has not received any data for items for the last 30 minutes.'
                         dependencies:
                           - name: 'MySQL: Service is down'
                             expression: 'last(/MySQL server/mysql.ping["{$MYSQL.DSN}","{$MYSQL.USER}","{$MYSQL.PASSWORD}"])=0'
                         tags:
                           - tag: scope
                             value: availability
                       - expression: 'last(/MySQL server/mysql.uptime)<10m'
                         name: 'MySQL: Service has been restarted'
                         event_name: 'MySQL: Service has been restarted (uptime < 10m)'
                         priority: INFO
                         description: 'MySQL uptime is less than 10 minutes.'
                         tags:
                           - tag: scope
                             value: notice
                   (...)

Copy

✔ Copied

uuid | string | (required) Unique identifier for this trigger.  
---|---|---  
expression | string | (required) Trigger expression.  
recovery_mode | string | Basis for generating OK events.  
Possible values:1 EXPRESSION (0, default), RECOVERY_EXPRESSION (1), NONE (2).  
recovery_expression | string | Trigger recovery expression.  
correlation_mode | string | Correlation mode (no event correlation or event correlation by tag).  
Possible values:1 DISABLED (0, default), TAG_VALUE (1).  
correlation_tag | string | The tag name to be used for event correlation.  
name | string | (required) Trigger name.  
event_name | string | Event name.  
opdata | string | Operational data.  
url_name | string | Label for the URL associated with the trigger.  
url | string | URL associated with the trigger.  
status | string | Trigger status.  
Possible values:1 ENABLED (0, default), DISABLED (1).  
priority | string | Trigger severity.  
Possible values:1 NOT_CLASSIFIED (0, default), INFO (1), WARNING (2), AVERAGE (3), HIGH (4), DISASTER (5).  
description | text | Trigger description.  
type | string | Event generation type (single problem event or multiple problem events).  
Possible values:1 SINGLE (0, default), MULTIPLE (1).  
manual_close | string | Manual closing of problem events.  
Possible values:1 NO (0, default), YES (1).  
dependencies |  | Root element for dependencies.  
| name | string | (required) Dependency trigger name.  
expression | string | (required) Dependency trigger expression.  
recovery_expression | string | Dependency trigger recovery expression.  
tags |  | Root element for trigger tags.  
| tag | string | (required) Tag name.  
value | string | Tag value.  
  
See also: [Trigger object](/documentation/current/en/manual/api/reference/trigger/object) (refer to the relevant property with a matching name).

#### Host low-level discovery rules
    
    
    zabbix_export:
             (...)
             hosts:
               - host: 'MySQL server'
                 (...)
                 discovery_rules:
                   - name: 'Database discovery'
                     key: 'mysql.db.discovery["{$MYSQL.DSN}","{$MYSQL.USER}","{$MYSQL.PASSWORD}"]'
                     delay: 1h
                     filter: (see table below)
                     description: 'Scanning databases in DBMS.'
                     interface_ref: if1
                     item_prototypes:
                       - name: 'Size of database {#DATABASE}'
                         key: 'mysql.db.size["{$MYSQL.DSN}","{$MYSQL.USER}","{$MYSQL.PASSWORD}","{#DATABASE}"]'
                         delay: 5m
                         units: B
                         description: 'Database size.'
                         preprocessing:
                           - type: DISCARD_UNCHANGED_HEARTBEAT
                             parameters:
                               - 1h
                         interface_ref: if1
                         tags:
                           - tag: component
                             value: storage
                           - tag: database
                             value: '{#DATABASE}'
                     lld_macro_paths:
                       - lld_macro: '{#DATABASE}'
                         path: $.Database
                     preprocessing:
                       - type: DISCARD_UNCHANGED_HEARTBEAT
                         parameters:
                           - 1d
                   (...)

Copy

✔ Copied

Most host low-level discovery rule elements are the same as for host items. The table below describes those elements that differ from host items.

type | string | Item type.  
Possible values:1 ZABBIX_PASSIVE (0, default), TRAP (2), SIMPLE (3), INTERNAL (5), ZABBIX_ACTIVE (7), EXTERNAL (10), ODBC (11), IPMI (12), SSH (13), TELNET (14), JMX (16), DEPENDENT (18), HTTP_AGENT (19), SNMP_AGENT (20), ITEM_TYPE_SCRIPT (21), ITEM_TYPE_BROWSER (22).  
---|---|---  
key | string | (required) The low-level discovery rule key.  
filter |  | Root element for host low-level discovery rule filters.  
lifetime | string | Time period (using seconds, [time suffix](/documentation/current/en/manual/appendix/suffixes#time-suffixes), or [user macro](/documentation/current/en/manual/config/macros/user_macros)), after which no longer discovered resources will be deleted.  
Default: 7d.  
lifetime_type | string | Scenario for deleting lost LLD resources.  
Possible values: DELETE_NEVER, DELETE_IMMEDIATELY, DELETE_AFTER.  
enabled_lifetime | string | Time period (using seconds, [time suffix](/documentation/current/en/manual/appendix/suffixes#time-suffixes), or [user macro](/documentation/current/en/manual/config/macros/user_macros)), after which no longer discovered resources will be disabled.  
enabled_lifetime_type | string | Scenario for disabling lost LLD resources.  
Possible values: DISABLE_NEVER, DISABLE_IMMEDIATELY, DISABLE_AFTER.  
item_prototypes |  | Root element for host item prototype elements, which are the same as for host items.  
trigger_prototypes |  | Root element for host trigger prototype elements, which are the same as for host item triggers.  
graph_prototypes |  | Root element for host graph prototypes, which are the same as for host graphs.  
host_prototypes |  | Root element for host prototypes, which are the same as for hosts.  
parent_discovery_rule |  | Root element for the parent low-level discovery rule (or rule prototype) of the low-level discovery rule prototype. This property denotes that it is an LLD rule prototype, direct child of the referenced rule/rule prototype.  
| key | string | (required) The parent low-level discovery rule (or rule prototype) key.  
master_item | string | (required for DEPENDENT rules) Root element for the dependent rule's master item.  
lld_macro_paths |  | Root element for low-level discovery rule macro paths.  
| lld_macro | string | (required) Low-level discovery rule macro name.  
path | string | (required) Selector for value, which will be assigned to the corresponding macro.  
preprocessing |  | Root element for low-level discovery rule value preprocessing.  
| step |  | Root element for low-level discovery rule value preprocessing step elements, which are the same as for host item value preprocessing steps, except with fewer possible values. See also: [LLD rule preprocessing object](/documentation/current/en/manual/api/reference/discoveryrule/object#lld-rule-preprocessing).  
overrides |  | Root element for low-level discovery rule override rules.  
| name | string | (required) Unique override name.  
step | string | (required) Unique order number of the override.  
stop | string | Stop processing next overrides if matches.  
filter |  | Root element for low-level discovery rule override rule filter elements, which are the same as for host low-level discovery rule filters.  
operations |  | Root element for host low-level discovery rule override operations.  
  
See also: [LLD rule object](/documentation/current/en/manual/api/reference/discoveryrule/object) (refer to the relevant property with a matching name).

##### Host low-level discovery rule filters
    
    
    zabbix_export:
             (...)
             hosts:
               - host: 'MySQL server'
                 (...)
                 discovery_rules:
                   - name: 'Database discovery'
                     (...)
                     filter:
                       evaltype: AND
                       conditions:
                         - macro: '{#DATABASE}'
                           value: '{$MYSQL.DBNAME.MATCHES}'
                         - macro: '{#DATABASE}'
                           value: '{$MYSQL.DBNAME.NOT_MATCHES}'
                           operator: NOT_MATCHES_REGEX
                     (...)

Copy

✔ Copied

evaltype | string | Override filter condition evaluation method.  
Possible values:1 AND_OR (0, default), AND (1), OR (2), FORMULA (3).  
---|---|---  
formula | string | Custom calculation formula for filter conditions.  
conditions |  | Root element for filter conditions.  
| macro | string | (required) The name of the low-level discovery macro to perform the check on.  
value | string | Value to compare with.  
operator | string | Condition operator.  
Possible values:1 MATCHES_REGEX (8, default), NOT_MATCHES_REGEX (9).  
formulaid | string | (required) Arbitrary unique ID that is used to reference a condition from the custom expression. Can only contain capital-case letters. The ID must be defined by the user when modifying filter conditions, but will be generated anew when requesting them afterward.  
  
See also: [LLD rule filter object](/documentation/current/en/manual/api/reference/discoveryrule/object#lld-rule-filter) (refer to the relevant property with a matching name).

##### Host low-level discovery rule override operations

operationobject | string | Object to which the operation is applied.  
Possible values:1 ITEM_PROTOTYPE (0), TRIGGER_PROTOTYPE (1), GRAPH_PROTOTYPE (2), HOST_PROTOTYPE (3), DISCOVERY_PROTOTYPE (4).  
---|---|---  
operator | string | Override condition operator.  
Possible values:1 EQUAL (1), NOT_EQUAL (2), LIKE (3), NOT_LIKE (4), REGEXP (5), NOT_REGEXP (6).  
value | string | A regular expression or a string for the override condition operator.  
status | string | Status of the object upon the override operation.  
discover | string | Whether the object is added as a result of the discovery.  
delay | string | Update interval set for the item prototype upon the override operation.  
history | string | History storage period set for the item prototype upon the override operation.  
trends | string | Trend storage period set for the item prototype upon the override operation.  
severity | string | Trigger prototype severity set upon the override operation.  
tags |  | Root element for the tags set for the object upon the override operation.  
| tag | string | (required) Tag name.  
value | string | Tag value.  
templates |  | Root element for the templates linked to the host prototype upon the override operation.  
| name | string | (required) Template name.  
inventory_mode | string | Host prototype inventory mode set upon the override operation.  
  
See also: [LLD rule override operation object](/documentation/current/en/manual/api/reference/discoveryrule/object#lld-rule-override-operation) (refer to the relevant property with a matching name).

#### Host web scenarios

uuid | string | (required) Unique identifier for this web scenario.  
---|---|---  
name | string | (required) Web scenario name.  
delay | string | Frequency (using seconds, [time suffix](/documentation/current/en/manual/appendix/suffixes#time-suffixes), or [user macro](/documentation/current/en/manual/config/macros/user_macros)) of executing web scenario.  
Default: 1m.  
attempts | integer | The number of attempts for executing web scenario steps.  
Possible values: 1-10 (default: 1).  
agent | string | Client agent. Zabbix will pretend to be the selected browser.  
This is useful when a website returns different content for different browsers.  
Default: Zabbix.  
http_proxy | string | Proxy that will be used by the web scenario given as: `http://[username[:password]@]proxy.example.com[:port]`  
variables |  | Root element for web scenario variables that may be used in scenario steps.  
| name | string | (required) Variable name.  
value | text | (required) Variable value.  
headers |  | Root element for HTTP headers to be sent when performing a request.  
Headers should be listed using the same syntax as they would appear in the HTTP protocol.  
| name | string | (required) Header name.  
value | text | (required) Header value.  
status | string | Web scenario status.  
Possible values:1 ENABLED (0, default), DISABLED (1).  
authentication | string | Authentication method.  
Possible values:1 NONE (0, default), BASIC (1), NTLM (2).  
http_user | string | User name used for BASIC (HTTP) or NTLM authentication.  
http_password | string | Password used for BASIC (HTTP) or NTLM authentication.  
verify_peer | string | Verify the SSL certificate of the web server.  
Possible values:1 NO (0, default), YES (1).  
verify_host | string | Verify that the _Common Name_ field or the _Subject Alternate Name_ field of the web server certificate matches.  
Possible values:1 NO (0, default), YES (1).  
ssl_cert_file | string | Name of the SSL certificate file used for client authentication (must be in PEM format).  
ssl_key_file | string | Name of the SSL private key file used for client authentication (must be in PEM format).  
ssl_key_password | string | SSL private key file password.  
steps |  | (required) Root element for host web scenario steps.  
tags |  | Root element for web scenario tags.  
| tag | string | (required) Tag name.  
value | string | Tag value.  
  
See also: [Web scenario object](/documentation/current/en/manual/api/reference/httptest/object) (refer to the relevant property with a matching name).

##### Host web scenario steps

name | string | (required) Web scenario step name.  
---|---|---  
url | string | (required) URL for monitoring.  
query_fields |  | Root element for query parameters (an array of HTTP fields to be added to the URL when performing a request).  
| name | string | (required) Query parameter name.  
value | string | Query parameter value.  
posts |  | Root element for HTTP POST variables (a string (raw post data) or an array of HTTP fields (form field data)).  
| name | string | (required) Post field name.  
value | string | (required) Post field value.  
variables |  | Root element of step-level variables (macros) that should be applied after this step.  
If the variable value has a 'regex:' prefix, then its value is extracted from the data returned by this step according to the regular expression pattern following the 'regex:' prefix  
| name | string | (required) Variable name.  
value | text | (required) Variable value.  
headers |  | Root element for HTTP headers to be sent when performing a request.  
| name | string | (required) Header name.  
value | text | (required) Header value.  
follow_redirects | string | Follow HTTP redirects.  
Possible values:1 NO (0), YES (1, default).  
retrieve_mode | string | HTTP response retrieve mode.  
Possible values:1 BODY (0, default), HEADERS (1), BOTH (2).  
timeout | string | Timeout (using seconds, [time suffix](/documentation/current/en/manual/appendix/suffixes#time-suffixes), or [user macro](/documentation/current/en/manual/config/macros/user_macros)) of step execution.  
Default: 15s.  
required | string | Text that must be present in the response (ignored if empty).  
status_codes | string | A comma-delimited list of accepted HTTP status codes (e.g., `200-201,210-299`; ignored if empty).  
  
See also: [Web scenario step object](/documentation/current/en/manual/api/reference/httptest/object#scenario-step) (refer to the relevant property with a matching name).

#### Host graphs
    
    
    zabbix_export:
             (...)
             graphs:
               - name: 'MySQL: Bandwidth'
                 graph_items: (see table below)
               (...)

Copy

✔ Copied

uuid | string | Unique identifier of the graph.  
---|---|---  
name | string | (required) Graph name.  
width | integer | Graph width, in pixels.  
Used for preview and for pie/exploded graphs.  
Possible values:1 20-65535 (default: 900).  
height | integer | Graph height, in pixels.  
Used for preview and for pie/exploded graphs.  
Possible values:1 20-65535 (default: 900).  
yaxismin | double | Value of Y axis minimum.  
Supported for FIXED minimum value of Y axis.  
Default: 0.  
yaxismax | double | Value of Y axis maximum.  
Supported for FIXED minimum value of X axis.  
Default: 0.  
show_work_period | string | Highlight non-working hours.  
Supported for NORMAL and STACKED graphs.  
Possible values:1 NO (0), YES (1, default).  
show_triggers | string | Display simple trigger values as a line.  
Supported for NORMAL and STACKED graphs.  
Possible values:1 NO (0), YES (1, default).  
type | string | Graph type.  
Possible values:1 NORMAL (0, default), STACKED (1), PIE (2), EXPLODED (3).  
show_legend | string | Display graph legend.  
Possible values:1 NO (0), YES (1, default).  
show_3d | string | Enable 3D style.  
Supported for NORMAL and STACKED graphs.  
Possible values:1 NO (0, default), YES (1).  
percent_left | double | Show the percentile line for left axis.  
Supported for NORMAL graphs.  
Default: 0.  
percent_right | double | Show the percentile line for right axis.  
Supported for NORMAL graphs.  
Default: 0.  
ymin_type_1 | string | Minimum value of Y axis.  
Supported for NORMAL and STACKED graphs.  
Possible values:1 CALCULATED (0, default), FIXED (1), ITEM (2).  
ymin_item_1 |  | (required if `ymin_type_1` is set to `ITEM`) Root element for individual item details.  
| host | string | (required) Item host.  
key | string | (required) Item key.  
ymax_type_1 | string | Maximum value of Y axis.  
Supported for NORMAL and STACKED graphs.  
Possible values:1 CALCULATED (0, default), FIXED (1), ITEM (2).  
ymax_item_1 |  | (required if `ymax_type_1` is set to `ITEM`) Root element for individual item details.  
| host | string | (required) Item host.  
key | string | (required) Item key.  
graph_items |  | (required) Root element for host graph items.  
  
See also: [Graph object](/documentation/current/en/manual/api/reference/graph/object) (refer to the relevant property with a matching name).

##### Host graph items
    
    
    zabbix_export:
             (...)
             graphs:
               - name: 'MySQL: Bandwidth'
                 graph_items:
                   - drawtype: GRADIENT_LINE
                     color: 199C0D
                     item:
                       host: 'MySQL server'
                       key: mysql.bytes_received.rate
                   - sortorder: '1'
                     drawtype: GRADIENT_LINE
                     color: F63100
                     item:
                       host: 'MySQL server'
                       key: mysql.bytes_sent.rate
               (...)

Copy

✔ Copied

sortorder | integer | Draw order. The smaller value is drawn first. Can be used to draw lines or regions behind (or in front of) another.  
---|---|---  
drawtype | string | Draw style of the graph item.  
Supported for NORMAL graphs.  
Possible values:1 SINGLE_LINE (0, default), FILLED_REGION (1), BOLD_LINE (2), DOTTED_LINE (3), DASHED_LINE (4), GRADIENT_LINE (5).  
color | string | Element color (6 symbols, hex).  
yaxisside | string | Side of the graph where the graph item's Y scale will be drawn.  
Supported for NORMAL and STACKED graphs.  
calc_fnc | string | Data to draw if more than one value exists for an item.  
Possible values:1 MIN (1), AVG (2, default), MAX (4), ALL (7; minimum, average, and maximum; supported for simple graphs), LAST (9, supported for pie/exploded graphs).  
type | string | Graph item type.  
Possible values:1 SIMPLE (0, default), GRAPH_SUM (2; value of the item represents the whole pie; supported for pie/exploded graphs).  
item |  | (required) Individual item.  
| host | string | (required) Item host.  
key | string | (required) Item key.  
  
See also: [Graph item object](/documentation/current/en/manual/api/reference/graphitem/object) (refer to the relevant property with a matching name).

#### Host value maps
    
    
    zabbix_export:
             (...)
             hosts:
               - host: 'MySQL server'
                 (...)
                 valuemaps:
                   - name: Example value map
                     mappings:
                       - value: '1'
                         newvalue: Example value
             (...)

Copy

✔ Copied

uuid | string | (required) Unique identifier for this value map.  
---|---|---  
name | string | (required) Value map name.  
mapping |  | Root element for mappings.  
| type | string | Mapping match type.  
Possible values:1 EQUAL (0, default), GREATER_OR_EQUAL (2), LESS_OR_EQUAL (3), IN_RANGE (4), REGEXP (5), DEFAULT (6).  
value | string | Original value.  
newvalue | string | (required) Value to which the original value is mapped to.  
  
See also: [Value map object](/documentation/current/en/manual/api/reference/valuemap/object) (refer to the relevant property with a matching name).

## Footnotes

1 API integer values in brackets, for example, ENABLED (0), are mentioned only for reference. For more information, see the linked API object page in the table entry or at the end of each section.