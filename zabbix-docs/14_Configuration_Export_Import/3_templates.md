---
title: Templates
source: https://www.zabbix.com/documentation/current/en/manual/xml_export_import/templates
downloaded: 2025-11-14 10:37:10
---

# 3 Templates  
  
#### Overview

Templates are [exported](/documentation/current/en/manual/xml_export_import) with many related objects and object relations.

Template export contains:

  * Linked template groups
  * Linked host groups (if used in [host prototype](/documentation/current/en/manual/discovery/low_level_discovery/host_prototypes) configuration)
  * Template data
  * Linkage to other templates
  * Linkage to template groups
  * Directly linked items
  * Directly linked triggers
  * Directly linked graphs
  * Directly linked dashboards
  * Directly linked discovery rules with all prototypes
  * Directly linked web scenarios
  * Value maps

#### Exporting

To export templates, do the following:

  1. Go to _Data collection_ → _Templates_.
  2. Mark the checkboxes of the templates to export.
  3. Click _Export_ below the list.

![](/documentation/current/assets/en/manual/xml_export_import/export_templates.png)

Depending on the selected format, templates are exported to a local file with a default name:

  * `zabbix_export_templates.yaml` \- in YAML export (default option for export);
  * `zabbix_export_templates.xml` \- in XML export;
  * `zabbix_export_templates.json` \- in JSON export.

#### Importing

To import templates, do the following:

  1. Go to _Data collection_ → _Templates_.
  2. Click _Import_ in the upper-right corner.
  3. Select the import file.
  4. Click _Import_ in the lower-right corner of the configuration form.

![](/documentation/current/assets/en/manual/xml_export_import/import_templates.png)

If you mark the _Advanced options_ checkbox, a detailed list of all importable elements will be displayed - mark or unmark each import rule as required.

If you click the checkbox in the _All_ row, all elements below it will be marked/unmarked.

Import rules:

_Update existing_ | Existing elements will be updated using data from the import file. Otherwise, they will not be updated.  
---|---  
_Create new_ | New elements will be created using data from the import file. Otherwise, they will not be created.  
_Delete missing_ | Existing elements not present in the import file will be removed. Otherwise, they will not be removed.  
If _Delete missing_ is marked for _Template linkage_ , current template linkage not present in the import file will be unlinked. Entities (items, triggers, graphs, etc.) inherited from the unlinked templates will not be removed (unless the _Delete missing_ option is selected for each entity as well).  
  
On the next screen, you will be able to view the content of a template being imported. If this is a new template, all elements will be listed in green. If updating an existing template, new template elements will be highlighted in green; removed template elements will be highlighted in red; elements that have not changed will be listed on a gray background.

![](/documentation/current/assets/en/manual/xml_export_import/import_templates_details.png)

The menu on the left can be used to navigate through the list of changes. The _Updated_ section highlights all changes made to existing template elements. The _Added_ section lists new template elements. The elements in each section are grouped by element type; click the gray arrow to expand or collapse the group of elements.

![](/documentation/current/assets/en/manual/xml_export_import/import_templates_menu.png)

Review template changes and then click _Import_ to perform the template import. A success or failure message of the import will be displayed in the frontend.

## Export format

When a template is exported, Zabbix generates a structured YAML, JSON, or XML format. The export includes template elements, such as template metadata, items, macros, triggers, dashboards, and more.

Each element serves a specific purpose and may contain nested elements.

The following sections describe each element in the export format. The examples use the [Linux by Zabbix agent](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/os/linux/template_os_linux.yaml) template.

An ellipsis `(...)` indicates elements omitted for brevity. The note `(see table below)` is used when the element is explained in more detail in later sections.

## Template metadata
    
    
    zabbix_export:
             version: '7.4'
             template_groups:
               - uuid: 846977d1dfed4968bc5f8bdb363285bc
                 name: 'Templates/Operating systems'
             templates: (see table below)
             triggers: (see table below)
             graphs: (see table below)

Copy

✔ Copied

version | string | (required) Export version.  
---|---|---  
template_groups |  | (required) Root element for template groups.  
| uuid | string | (required) Unique identifier for this template group.  
name | string | (required) Template group name.  
host_groups |  | Root element for host groups that are used by host prototypes.  
| uuid | string | (required) Unique identifier for this host group.  
name | string | (required) Host group name.  
templates |  | Root element for templates.  
triggers |  | Root element for template trigger elements, which are the same as for template item triggers.  
graphs |  | Root element for template graph elements, which are the same as for [host graphs](/documentation/current/en/manual/xml_export_import/hosts#host-graphs).  
  
### Templates
    
    
    zabbix_export:
             (...)
             templates:
               - uuid: f8f7908280354f2abeed07dc788c3747
                 template: 'Linux by Zabbix agent'
                 name: 'Linux by Zabbix agent'
                 description: |
                   This is an official Linux template. It requires Zabbix agent 7.4 or newer. (...)
                 wizard_ready: 'YES'
                 readme: |
                   ## Overview
                   
                   This is an official Linux template. It requires Zabbix agent 7.4 or newer. (...)
                 vendor:
                   name: Zabbix
                   version: 7.4-2
                 groups:
                   - name: 'Templates/Operating systems'
                 items: (see table below)
                 discovery_rules: (see table below)
                 tags:
                   - tag: class
                     value: os
                   - tag: target
                     value: linux
                 macros:
                   - macro: '{$AGENT.TIMEOUT}'
                     value: 3m
                     description: 'Timeout after which agent is considered unavailable. Works only for agents reachable from Zabbix server/proxy (passive mode).'
                     config: (see table below)
                   - macro: '{$CPU.UTIL.CRIT}'
                     value: '90'
                     description: 'Critical threshold of CPU utilization expressed in %.'
                     config: (see table below)
                   (...)
                 dashboards: (see table below)
                 valuemaps: (see table below)
               (...)

Copy

✔ Copied

uuid | string | (required) Unique identifier for this template.  
---|---|---  
template | string | (required) Unique template name.  
name | string | Visible template name.  
description | text | Template description.  
wizard_ready | text | Whether the template is available for selection in the [Host Wizard](/documentation/current/en/manual/config/hosts/host_wizard).  
Possible values:1 NO (0, default), YES (1).  
See also: [Template object](/documentation/current/en/manual/api/reference/template/object) (`wizard_ready`).  
readme | text | Template-specific configuration instructions to display in the [Host Wizard](/documentation/current/en/manual/config/hosts/host_wizard#configure-host). Supports Markdown formatting.  
vendor |  | Root element for template vendor (present if the exported template contains vendor data).  
| name | string | (required) Template vendor name.  
version | string | (required) Template version.  
For [out-of-the-box templates](/documentation/current/en/manual/config/templates_out_of_the_box), version is displayed as follows: major version of Zabbix, delimiter ("-"), revision number (increased with each new version of the template, and reset with each major version of Zabbix). For example, 7.0-0, 7.0-3, 7.4-0, 7.4-3.  
templates |  | Root element for linked templates.  
| name | string | (required) Template name.  
groups |  | Root element for template groups.  
| name | string | (required) Template group name.  
items |  | Root element for template items.  
discovery_rules |  | Root element for template low-level discovery rules.  
httptests |  | Root element for template web scenarios.  
tags |  | Root element for template tags.  
| tag | string | (required) Tag name.  
value | string | Tag value.  
macros |  | Root element for template user macros.  
| macro | string | (required) User macro name.  
type | string | User macro type.  
Possible values:1 TEXT (0, default), SECRET_TEXT (1), VAULT (2).  
See also: [User macro object](/documentation/current/en/manual/api/reference/usermacro/object) (`type`).  
value | string | User macro value.  
description | string | User macro description.  
config |  | Root element for template macro configuration responsible for how the macro is displayed in the [Host Wizard](/documentation/current/en/manual/config/hosts/host_wizard#configure-host).  
dashboards |  | Root element for template dashboards.  
valuemaps |  | Root element for template value maps.  
  
#### Template items
    
    
    zabbix_export:
             (...)
             templates:
               (...)
                 items:
                   - uuid: f94f9f4699e94c369e6c98b2a2f485ce
                     name: 'Zabbix agent ping'
                     key: agent.ping
                     description: 'The agent always returns "1" for this item. May be used in combination with `nodata()` for the availability check.'
                     valuemap:
                       name: 'Zabbix agent ping status'
                     tags:
                       - tag: component
                         value: system
                   (...)
                   - uuid: 58818005e76d46dda14d6592f601ab00
                     name: 'Number of installed packages'
                     key: system.sw.packages.get
                     delay: 1h
                     preprocessing: (see table below)
                     tags:
                       - tag: component
                         value: os
                     triggers: (see table below)
                   - uuid: 403cebed115441369e94d35d070ca7b8
                     name: 'Memory utilization'
                     type: DEPENDENT
                     key: vm.memory.utilization
                     value_type: FLOAT
                     units: '%'
                     description: 'The percentage of used memory is calculated as `100-pavailable`.'
                     preprocessing: (see table below)
                     master_item:
                       key: 'vm.memory.size[pavailable]'
                     tags:
                       - tag: component
                         value: memory
                     triggers: (see table below)
                   (...)

Copy

✔ Copied

uuid | string | (required) Unique identifier for this item.  
---|---|---  
name | string | (required) Item name.  
type | string | Item type.  
Possible values:1 ZABBIX_PASSIVE (0, default), TRAP (2), SIMPLE (3), INTERNAL (5), ZABBIX_ACTIVE (7), EXTERNAL (10), ODBC (11), IPMI (12), SSH (13), TELNET (14), CALCULATED (15), JMX (16), SNMP_TRAP (17), DEPENDENT (18), HTTP_AGENT (19), SNMP_AGENT (20), ITEM_TYPE_SCRIPT (21), ITEM_TYPE_BROWSER (22).  
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
| step |  | Root element for template item value preprocessing steps.  
jmx_endpoint | string | JMX endpoint.  
Supported for JMX items.  
master_item |  | (required for DEPENDENT items) Root element for dependent item's master item.  
| key | string | (required) Dependent item's master item key.  
timeout | string | Item data polling request timeout.  
Supported for [Timeouts](/documentation/current/en/manual/web_interface/frontend_sections/administration/general#timeouts) list of item types.  
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
triggers | Root element for template item triggers.  
  
See also: [Item object](/documentation/current/en/manual/api/reference/item/object) (refer to the relevant property with a matching name).

##### Template item value preprocessing steps
    
    
    zabbix_export:
             (...)
             templates:
               (...)
                 items:
                   (...)
                   - uuid: 58818005e76d46dda14d6592f601ab00
                     (...)
                     preprocessing:
                       - type: JSONPATH
                         parameters:
                           - $.length()
                       - type: DISCARD_UNCHANGED_HEARTBEAT
                         parameters:
                           - 12h
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

##### Template item triggers
    
    
    zabbix_export:
             (...)
             templates:
               (...)
                 items:
                   (...)
                   - uuid: 58818005e76d46dda14d6592f601ab00
                     (...)
                     triggers:
                       - uuid: b950c306394f4b3c902060a8273cbcde
                         expression: 'change(/Linux by Zabbix agent/system.sw.packages.get)<>0'
                         name: 'Linux: Number of installed packages has been changed'
                         priority: WARNING
                         manual_close: 'YES'
                         tags:
                           - tag: scope
                             value: notice
                   (...)
                   - uuid: 403cebed115441369e94d35d070ca7b8
                     (...)
                     triggers:
                       - uuid: cfd395b1cde74ef18a5e5f840bd5142a
                         expression: 'min(/Linux by Zabbix agent/vm.memory.utilization,5m)>{$MEMORY.UTIL.MAX}'
                         name: 'Linux: High memory utilization'
                         event_name: 'Linux: High memory utilization (>{$MEMORY.UTIL.MAX}% for 5m)'
                         priority: AVERAGE
                         description: 'The system is running out of free memory.'
                         dependencies:
                           - name: 'Linux: Lack of available memory'
                             expression: 'max(/Linux by Zabbix agent/vm.memory.size[available],5m)<{$MEMORY.AVAILABLE.MIN} and last(/Linux by Zabbix agent/vm.memory.size[total])>0'
                         tags:
                           - tag: scope
                             value: capacity
                           - tag: scope
                             value: performance
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

#### Template low-level discovery rules
    
    
    zabbix_export:
             (...)
             templates:
               (...)
                 discovery_rules:
                   - uuid: acfdea9c46ef48c68e6636f43b8f96a2
                     name: 'Network interface discovery'
                     key: net.if.discovery
                     delay: 1h
                     filter: (see table below)
                     description: 'The discovery of network interfaces.'
                     item_prototypes: (see table below)
                     trigger_prototypes: (see table below)
                     graph_prototypes: (see table below)
                   (...)

Copy

✔ Copied

Most template low-level discovery rule elements are the same as for template items. The table below describes those elements that differ from template items.

type | string | Item type.  
Possible values:1 ZABBIX_PASSIVE (0, default), TRAP (2), SIMPLE (3), INTERNAL (5), ZABBIX_ACTIVE (7), EXTERNAL (10), ODBC (11), IPMI (12), SSH (13), TELNET (14), JMX (16), DEPENDENT (18), HTTP_AGENT (19), SNMP_AGENT (20), ITEM_TYPE_SCRIPT (21), ITEM_TYPE_BROWSER (22).  
---|---|---  
key | string | (required) The low-level discovery rule key.  
filter |  | Root element for template low-level discovery rule filters.  
lifetime | string | Time period (using seconds, [time suffix](/documentation/current/en/manual/appendix/suffixes#time-suffixes), or [user macro](/documentation/current/en/manual/config/macros/user_macros)), after which no longer discovered resources will be deleted.  
Default: 7d.  
lifetime_type | string | Scenario for deleting lost LLD resources.  
Possible values: DELETE_NEVER, DELETE_IMMEDIATELY, DELETE_AFTER.  
enabled_lifetime | string | Time period (using seconds, [time suffix](/documentation/current/en/manual/appendix/suffixes#time-suffixes), or [user macro](/documentation/current/en/manual/config/macros/user_macros)), after which no longer discovered resources will be disabled.  
enabled_lifetime_type | string | Scenario for disabling lost LLD resources.  
Possible values: DISABLE_NEVER, DISABLE_IMMEDIATELY, DISABLE_AFTER.  
item_prototypes |  | Root element for template item prototype elements, which are the same as for template items.  
trigger_prototypes |  | Root element for template trigger prototype elements, which are the same as for template item triggers.  
graph_prototypes |  | Root element for template graph prototype elements, which are the same as for [host graphs](/documentation/current/en/manual/xml_export_import/hosts#host-graphs).  
host_prototypes |  | Root element for template host prototype elements, which are the same as for [hosts](/documentation/current/en/manual/xml_export_import/hosts#hosts).  
parent_discovery_rule |  | Root element for the parent low-level discovery rule (or rule prototype) of the low-level discovery rule prototype. This property denotes that it is an LLD rule prototype, direct child of the referenced rule/rule prototype.  
| key | string | (required) The parent low-level discovery rule (or rule prototype) key.  
master_item | string | (required for DEPENDENT rules) Root element for the dependent rule's master item.  
lld_macro_paths |  | Root element for low-level discovery rule macro paths.  
| lld_macro | string | (required) Low-level discovery rule macro name.  
path | string | (required) Selector for value, which will be assigned to the corresponding macro.  
preprocessing |  | Root element for low-level discovery rule value preprocessing.  
| step |  | Root element for low-level discovery rule value preprocessing step elements, which are the same as for template item value preprocessing steps, except with fewer possible values. See also: [LLD rule preprocessing object](/documentation/current/en/manual/api/reference/discoveryrule/object#lld-rule-preprocessing).  
overrides |  | Root element for low-level discovery rule override rules.  
| name | string | (required) Unique override name.  
step | string | (required) Unique order number of the override.  
stop | string | Stop processing next overrides if matches.  
filter |  | Root element for template low-level discovery rule override rule filter elements, which are the same as for template low-level discovery rule filters.  
operations |  | Root element for template low-level discovery rule override operations.  
  
See also: [LLD rule object](/documentation/current/en/manual/api/reference/discoveryrule/object) (refer to the relevant property with a matching name).

##### Template low-level discovery rule filters
    
    
    zabbix_export:
             (...)
             templates:
               (...)
                 discovery_rules:
                   - uuid: acfdea9c46ef48c68e6636f43b8f96a2
                     (...)
                     filter:
                       evaltype: AND
                       conditions:
                         - macro: '{#IFNAME}'
                           value: '{$NET.IF.IFNAME.MATCHES}'
                         - macro: '{#IFNAME}'
                           value: '{$NET.IF.IFNAME.NOT_MATCHES}'
                           operator: NOT_MATCHES_REGEX
                     (...)
                   - uuid: 2bbdc79f082d4c618e01bec625e9c90a
                     (...)
                     filter:
                       evaltype: AND
                       conditions:
                         - macro: '{#DEVNAME}'
                           value: '{$VFS.DEV.DEVNAME.MATCHES}'
                         - macro: '{#DEVNAME}'
                           value: '{$VFS.DEV.DEVNAME.NOT_MATCHES}'
                           operator: NOT_MATCHES_REGEX
                         - macro: '{#DEVTYPE}'
                           value: disk
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

##### Template low-level discovery rule override operations

operationobject | string | Object to which the operation is applied.  
Possible values:1 ITEM_PROTOTYPE (0), TRIGGER_PROTOTYPE (1), GRAPH_PROTOTYPE (2), HOST_PROTOTYPE (3).  
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

#### Template web scenarios

uuid | string | (required) Unique identifier for this web scenario.  
---|---|---  
name | string | (required) Web scenario name.  
delay | string | Frequency (using seconds, [time suffix](/documentation/current/en/manual/appendix/suffixes#time-suffixes), or [user macro](/documentation/current/en/manual/config/macros/user_macros)) of executing web scenario.  
Default: 1m.  
attempts | integer | The number of attempts for executing web scenario steps.  
Possible values:1 1-10 (default: 1).  
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
steps |  | (required) Root element for template web scenario steps.  
tags |  | Root element for web scenario tags.  
| tag | string | (required) Tag name.  
value | string | Tag value.  
  
See also: [Web scenario object](/documentation/current/en/manual/api/reference/httptest/object) (refer to the relevant property with a matching name).

##### Template web scenario steps

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

#### Template macro configuration
    
    
    zabbix_export:
             (...)
             templates:
               - uuid: f8f7908280354f2abeed07dc788c3747
                 (...)
                 macros:
                   - macro: '{$AGENT.TIMEOUT}'
                     (...)
                     config:
                       type: TEXT
                       priority: '1'
                       label: 'Seconds since the last Zabbix agent seen'
                       description: 'Timeout after which agent is considered unavailable.'
                   - macro: '{$CPU.UTIL.CRIT}'
                     (...)
                     config:
                       type: TEXT
                       priority: '2'
                       section_name: Thresholds
                       label: 'Threshold of CPU utilization expressed'
                       description: 'Critical threshold of CPU utilization expressed in %. In the range from 0 to 100 inclusive.'
                       regex: '^-?([0-9]+|(([0-9]+)\.([0-9]+)))$'
                   (...)
                   - macro: '{$IFCONTROL}'
                     (...)
                     config:
                       type: CHECKBOX
                       priority: '19'
                       label: 'Interfaces control'
                       description: 'Fire a trigger when the interface operational status changes to "Link down".'
                       options:
                         - checked: '1'
                           unchecked: '0'
                   (...)

Copy

✔ Copied

type | string | (required) Type of macro input field.  
Possible values:1 NOCONF (0), TEXT (1), LIST (2), CHECKBOX (3).  
---|---|---  
priority | string | Macro position in the macro list.  
section_name | string | Label of the collapsible section where the macro is grouped.  
label | string | (required for TEXT, LIST, CHECKBOX macros) Macro label.  
description | text | Macro help text. Supports Markdown formatting.  
required | string | Marks the macro as mandatory.  
Possible values:1 NO (0), YES (1).  
Supported for TEXT and LIST macros.  
regex | string | Regular expression to validate user input in a textbox field.  
Supported for TEXT macros.  
options |  | Root element for LIST items or CHECKBOX values.  
| value | string | (required for LIST macros) LIST item value.  
text | string | (required for LIST macros) LIST item text.  
checked | string | (required for CHECKBOX macros) Value representing a checked state.  
Possible values:1 0 (false), 1 (true).  
Supported for CHECKBOX macros.  
unchecked | string | (required for CHECKBOX macros) Value representing an unchecked state.  
Possible values:1 0 (false), 1 (true).  
Supported for CHECKBOX macros.  
  
See also: [Macro configuration object](/documentation/current/en/manual/api/reference/usermacro/object#macro-configuration) (refer to the relevant property with a matching name).

#### Template dashboards
    
    
    zabbix_export:
             (...)
             templates:
               (...)
                 dashboards:
                   - uuid: c689ad3115fd46a4b927d1f70ee2e5a4
                     name: Filesystems
                     pages:
                       - name: Overview
                         widgets: (see table below)
                   (...)

Copy

✔ Copied

uuid | string | (required) Unique identifier for this dashboard.  
---|---|---  
name | string | (required) Template dashboard name.  
display period | integer | Display period of dashboard pages.  
auto_start | string | Slideshow auto start.  
Possible values:1 NO (0), YES (1, default).  
pages |  | Root element for template dashboard pages.  
| name | string | Page name.  
display period | integer | Page display period.  
sortorder | integer | Page sorting order.  
widgets |  | Root element for template dashboard widgets.  
  
See also: [Template dashboard object](/documentation/current/en/manual/api/reference/templatedashboard/object) (refer to the relevant property with a matching name).

##### Template dashboard widgets
    
    
    zabbix_export:
             (...)
             templates:
               (...)
                 dashboards:
                   - uuid: c689ad3115fd46a4b927d1f70ee2e5a4
                     name: Filesystems
                     pages:
                       - name: Overview
                         widgets:
                           - type: graphprototype
                             width: '72'
                             height: '5'
                             fields:
                               - type: INTEGER
                                 name: columns
                                 value: '3'
                               - type: GRAPH_PROTOTYPE
                                 name: graphid.0
                                 value:
                                   host: 'Linux by Zabbix agent'
                                   name: 'FS [{#FSTYPE}({#FSNAME})]: Space utilization chart (relative to total)'
                               - type: STRING
                                 name: reference
                                 value: AAAEB
                           - type: graphprototype
                             'y': '5'
                             width: '72'
                             height: '5'
                             fields:
                               - type: INTEGER
                                 name: columns
                                 value: '1'
                               - type: GRAPH_PROTOTYPE
                                 name: graphid.0
                                 value:
                                   host: 'Linux by Zabbix agent'
                                   name: 'FS [{#FSTYPE}({#FSNAME})]: Space usage graph, in % (relative to max available)'
                               - type: STRING
                                 name: reference
                                 value: AAAEC
                   (...)

Copy

✔ Copied

type | string | (required) Widget type.  
---|---|---  
name | string | Widget name.  
x | integer | Horizontal position from the left side of the template dashboard.  
Possible values:1 0-71.  
y | integer | Vertical position from the top of the template dashboard.  
Possible values:1 0-63.  
width | integer | Widget width.  
Possible values:1 1-72.  
height | integer | Widget height.  
Possible values:1 1-64.  
hide_header | string | Hide widget header.  
Possible values:1 NO (0, default), YES (1).  
fields |  | Root element for the template dashboard widget fields.  
| type | string | (required) Widget field type.  
Possible values:1 INTEGER (0), STRING (1), ITEM (4), ITEM_PROTOTYPE (5), GRAPH (6), GRAPH_PROTOTYPE (7), MAP (8), SERVICE (9), SLA (10), USER (11), ACTION (12), MEDIA_TYPE (13).  
name | string | (required) Widget field name.  
value | mixed | (required) Widget field value, depending on the field type.  
  
See also: [Template dashboard widget object](/documentation/current/en/manual/api/reference/templatedashboard/object#template-dashboard-widget) (refer to the relevant property with a matching name).

#### Template value maps
    
    
    zabbix_export:
             (...)
             templates:
               (...)
                 valuemaps:
                   - uuid: 8c048c6cca8248f2860c208e8db0f59e
                     name: ifOperStatus
                     mappings:
                       - value: '0'
                         newvalue: unknown
                       - value: '1'
                         newvalue: notpresent
                       - value: '2'
                         newvalue: down
                       - value: '3'
                         newvalue: lowerlayerdown
                       - value: '4'
                         newvalue: testing
                       - value: '5'
                         newvalue: dormant
                       - value: '6'
                         newvalue: up
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