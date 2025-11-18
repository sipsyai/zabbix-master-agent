---
title: Low-level discovery
source: https://www.zabbix.com/documentation/current/en/manual/discovery/low_level_discovery
downloaded: 2025-11-14 10:37:18
---

# 3 Low-level discovery

### Overview

Low-level discovery (LLD) provides a way to automatically create items, triggers, and graphs for different entities on a computer. For instance, Zabbix can automatically start monitoring file systems or network interfaces on your machine, without the need to create items for each file system or network interface manually. LLD can also create hosts, for example, to [populate virtual machines](/documentation/current/en/manual/vm_monitoring) discovered on a hypervisor, and [nested discovery rules](/documentation/current/en/manual/discovery/low_level_discovery/discovery_prototypes), enabling multi-level discovery. Additionally, it is possible to configure Zabbix to remove unneeded entities automatically based on the actual results of periodically performed discovery.

A user can define their own types of discovery, provided they follow a particular JSON protocol.

The general architecture of the discovery process is as follows.

First, a user creates a discovery rule in _Data collection > Templates_, in the _Discovery_ column. A discovery rule consists of (1) an item that discovers the necessary entities (for instance, file systems or network interfaces) and (2) prototypes of items, triggers, and graphs that should be created based on the value of that item.

An item that discovers the necessary entities is like a regular item seen elsewhere: the server asks a Zabbix agent (or whatever the type of the item is set to) for a value of that item, the agent responds with a textual value. The difference is that the value the agent responds with should contain a list of discovered entities in a JSON format. While the details of this format are only important for implementers of custom discovery checks, it is necessary to know that the returned value contains a list of macro → value pairs. For instance, item "net.if.discovery" might return two pairs: "{#IFNAME}" → "lo" and "{#IFNAME}" → "eth0".

These macros are used in names, keys and other prototype fields where they are then substituted with the received values for creating real items, triggers, graphs or even hosts for each discovered entity. See the full list of [options](/documentation/current/en/manual/config/macros/lld_macros) for using LLD macros.

When the server receives a value for a discovery item, it looks at the macro → value pairs and for each pair generates real items, triggers, and graphs, based on their prototypes. In the example with "net.if.discovery" above, the server would generate one set of items, triggers, and graphs for the loopback interface "lo", and another set for interface "eth0".

Note that since **Zabbix 4.2** , the format of the JSON returned by low-level discovery rules has been changed. It is no longer expected that the JSON will contain the "data" object. Low-level discovery will now accept a normal JSON containing an array, in order to support new features such as the item value preprocessing and custom paths to low-level discovery macro values in a JSON document.

Built-in discovery keys have been updated to return an array of LLD rows at the root of JSON document. Zabbix will automatically extract a macro and value if an array field uses the {#MACRO} syntax as a key. Any new native discovery checks will use the new syntax without the "data" elements. When processing a low-level discovery value first the root is located (array at `$.` or `$.data`).

While the "data" element has been removed from all native items related to discovery, for backward compatibility Zabbix will still accept the JSON notation with a "data" element, though its use is discouraged. If the JSON contains an object with only one "data" array element, then it will automatically extract the content of the element using JSONPath `$.data`. Low-level discovery now accepts optional user-defined LLD macros with a custom path specified in JSONPath syntax.

As a result of the changes above, newer agents no longer will be able to work with an older Zabbix server.

See also: Discovered entities

### Configuring low-level discovery

We will illustrate low-level discovery based on an example of file system discovery.

To configure the discovery, do the following:

  * Go to: _Data collection_ > _Templates_ or _Hosts_.
  * Click on _Discovery_ in the row of an appropriate template/host.

![](/documentation/current/assets/en/manual/discovery/low_level_discovery/fs_templates.png)

  * Click on _Create discovery rule_ in the upper-right corner of the screen.
  * Fill in the discovery rule form with the required details.

#### Discovery rule

The discovery rule form contains five tabs, representing, from left to right, the data flow during discovery:

  * _Discovery rule_ \- specifies, most importantly, the built-in item or custom script to retrieve discovery data.
  * _Preprocessing_ \- applies some preprocessing to the discovered data.
  * _LLD macros_ \- allows to extract some macro values to use in discovered items, triggers, etc.
  * _Filters_ \- allows to filter the discovered values.
  * _Overrides_ \- allows to modify items, triggers, graphs or host prototypes when applying to specific discovered objects.

The **Discovery rule** tab contains the item key to use for discovery (as well as some general discovery rule attributes):

![](/documentation/current/assets/en/manual/discovery/low_level_discovery/lld_rule_fs.png)

All mandatory input fields are marked with a red asterisk.

_Name_ | Name of discovery rule.  
---|---  
_Type_ | The type of check to perform discovery.  
In this example we are using a _Zabbix agent_ item type.  
The discovery rule can also be a [dependent item](/documentation/current/en/manual/config/items/itemtypes/dependent_items), depending on a regular item. It cannot depend on another discovery rule. For a dependent item, select the respective type (_Dependent item_) and specify the master item in the 'Master item' field. The master item must exist.  
_Key_ | Enter the discovery item key (up to 2048 characters).  
For example, you may use the built-in "vfs.fs.discovery" item key to return a JSON string with the list of file systems present on the computer, their types and mount options.  
Note that another option for filesystem discovery is using discovery results by the "vfs.fs.get" agent key (see [example](/documentation/current/en/manual/discovery/low_level_discovery/examples/mounted_filesystems)).  
_Update interval_ | This field specifies how often Zabbix performs discovery. In the beginning, when you are just setting up file system discovery, you might wish to set it to a small interval, but once you know it works you can set it to 30 minutes or more, because file systems usually do not change very often.  
[Time suffixes](/documentation/current/en/manual/appendix/suffixes) are supported, e.g. 30s, 1m, 2h, 1d.  
[User macros](/documentation/current/en/manual/config/macros/user_macros) are supported.  
_Note_ : The update interval can only be set to '0' if custom intervals exist with a non-zero value. If set to '0', and a custom interval (flexible or scheduled) exists with a non-zero value, the item will be polled during the custom interval duration.  
New discovery rules will be checked within 60 seconds of their creation, unless they have Scheduling or Flexible update interval and the _Update interval_ is set to 0.  
_Note_ that for an existing discovery rule the discovery can be performed immediately by pushing the _Execute now_ button.  
_Custom intervals_ | You can create custom rules for checking the item:  
**Flexible** \- create an exception to the _Update interval_ (interval with different frequency)  
**Scheduling** \- create a custom polling schedule.  
For detailed information see [Custom intervals](/documentation/current/en/manual/config/items/item/custom_intervals).  
_Timeout_ | Set the discovery check timeout. Select the timeout option:  
**Global** \- proxy/global timeout is used (displayed in the grayed out _Timeout_ field);  
**Override** \- custom timeout is used (set in the _Timeout_ field; allowed range: 1 - 600s). [Time suffixes](/documentation/current/en/manual/appendix/suffixes#time-suffixes), e.g. 30s, 1m, and [user macros](/documentation/current/en/manual/config/macros/user_macros) are supported.  
Clicking the _Timeouts_ link allows you to configure [proxy](/documentation/current/en/manual/distributed_monitoring/proxies#configuration) timeouts or [global](/documentation/current/en/manual/web_interface/frontend_sections/administration/general#timeouts) timeouts (if a proxy is not used). Note that the _Timeouts_ link is visible only to users of _Super admin_ type with permissions to _Administration_ > [_General_](/documentation/current/en/manual/web_interface/frontend_sections/administration/general) or _Administration_ > [_Proxies_](/documentation/current/en/manual/web_interface/frontend_sections/administration/proxies) frontend sections.  
_Delete lost resources_ | Specify how soon the discovered entity will be deleted once its discovery status becomes "Not discovered anymore":  
_Never_ \- it will not be deleted;  
_Immediately_ \- it will be deleted immediately;  
_After_ \- it will be deleted after the specified time period. The value must be greater than _Disable lost resources_ value.  
[Time suffixes](/documentation/current/en/manual/appendix/suffixes) are supported, e.g. 2h, 1d.  
[User macros](/documentation/current/en/manual/config/macros/user_macros) are supported.  
_Note_ : Using "Immediately" is not recommended, since just wrongly editing the filter may end up in the entity being deleted with all the historical data.  
Note that manually disabled resources will not be deleted by low-level discovery.  
_Disable lost resources_ | Specify how soon the discovered entity will be disabled once its discovery status becomes "Not discovered anymore":  
_Never_ \- it will not be disabled;  
_Immediately_ \- it will be disabled immediately;  
_After_ \- it will be disabled after the specified time period. The value should be greater than the discovery rule update interval.  
Note that automatically disabled resources will become enabled again, if re-discovered by low-level discovery. Manually disabled resources will not become enabled again if re-discovered.  
This field is not displayed if _Delete lost resources_ is set to "Immediately".  
[Time suffixes](/documentation/current/en/manual/appendix/suffixes) are supported, e.g. 2h, 1d.  
[User macros](/documentation/current/en/manual/config/macros/user_macros) are supported.  
_Description_ | Enter a description.  
_Enabled_ | If checked, the rule will be processed.  
  
Discovery rule history is not preserved.

#### Preprocessing

The **Preprocessing** tab allows to define transformation rules to apply to the result of discovery. One or several transformations are possible in this step. Transformations are executed in the order in which they are defined. All preprocessing is done by Zabbix server.

See also:

  * [Preprocessing details](/documentation/current/en/manual/config/items/preprocessing/preprocessing_details)
  * [Preprocessing testing](/documentation/current/en/manual/config/items/preprocessing#testing)

![](/documentation/current/assets/en/manual/discovery/low_level_discovery/lld_fs_b.png)

| _Transformation_ | Description  
---|---|---  
Text  
| _Regular expression_ | Match the received value to the <pattern> regular expression and replace value with the extracted <output>. The regular expression supports extraction of maximum 10 captured groups with the \N sequence.  
Parameters:  
**pattern** \- regular expression  
**output** \- output formatting template. An \N (where N=1…9) escape sequence is replaced with the Nth matched group. A \0 escape sequence is replaced with the matched text.  
If you mark the _Custom on fail_ checkbox, it is possible to specify custom error-handling options: either to discard the value, set a specified value or set a specified error message.  
_Replace_ | Find the search string and replace it with another (or nothing). All occurrences of the search string will be replaced.  
Parameters:  
**search string** \- the string to find and replace, case-sensitive (required)  
**replacement** \- the string to replace the search string with. The replacement string may also be empty effectively allowing to delete the search string when found.  
It is possible to use escape sequences to search for or replace line breaks, carriage return, tabs and spaces "\n \r \t \s"; backslash can be escaped as "\\\" and escape sequences can be escaped as "\\\n". Escaping of line breaks, carriage return, tabs is automatically done during low-level discovery.  
Structured data  
| _JSONPath_ | Extract value or fragment from JSON data using [JSONPath functionality](/documentation/current/en/manual/config/items/preprocessing/jsonpath_functionality).  
If you mark the _Custom on fail_ checkbox, it is possible to specify custom error-handling options: either to discard the value, set a specified value or set a specified error message.  
| _XML XPath_ | Extract value or fragment from XML data using XPath functionality.  
For this option to work, Zabbix server must be compiled with libxml support.  
Examples:  
`number(/document/item/value)` will extract `10` from `<document><item><value>10</value></item></document>`  
`number(/document/item/@attribute)` will extract `10` from `<document><item attribute="10"></item></document>`  
`/document/item` will extract `<item><value>10</value></item>` from `<document><item><value>10</value></item></document>`  
Note that namespaces are not supported.  
If you mark the _Custom on fail_ checkbox, it is possible to specify custom error-handling options: either to discard the value, set a specified value or set a specified error message.  
| _CSV to JSON_ | Convert CSV file data into JSON format.  
For more information, see: [CSV to JSON preprocessing](/documentation/current/en/manual/config/items/preprocessing/csv_to_json#csv-header-processing).  
_XML to JSON_ | Convert data in XML format to JSON.  
For more information, see: [Serialization rules](/documentation/current/en/manual/config/items/preprocessing/javascript/javascript_objects#serialization-rules).  
If you mark the _Custom on fail_ checkbox, it is possible to specify custom error-handling options: either to discard the value, set a specified value or set a specified error message.  
SNMP  
| _SNMP walk value_ | Extract value by the specified OID/MIB name and apply formatting options:  
**Unchanged** \- return Hex-STRING as unescaped hex string (_note_ that display hints are still applied);  
**UTF-8 from Hex-STRING** \- convert Hex-STRING to UTF-8 string;  
**MAC from Hex-STRING** \- convert Hex-STRING to MAC address string (which will have `' '` replaced by `':'`);  
**Integer from BITS** \- convert the first 8 bytes of a bit string expressed as a sequence of hex characters (e.g. "1A 2B 3C 4D") into a 64-bit unsigned integer. In bit strings longer than 8 bytes, consequent bytes will be ignored.  
If you mark the _Custom on fail_ checkbox, it is possible to specify custom error-handling options: either to discard the value, set a specified value or set a specified error message.  
| _SNMP walk to JSON_ | Convert SNMP values to JSON. Specify a field name in the JSON and the corresponding SNMP OID path. Field values will be populated by values in the specified SNMP OID path.  
You may use this preprocessing step for [SNMP OID discovery](/documentation/current/en/manual/discovery/low_level_discovery/examples/snmp_oids_walk).  
Similar value formatting options as in the _SNMP walk value_ step are available.  
If you mark the _Custom on fail_ checkbox, it is possible to specify custom error-handling options: either to discard the value, set a specified value or set a specified error message.  
| _SNMP get value_ | Apply formatting options to the SNMP get value:  
**UTF-8 from Hex-STRING** \- convert Hex-STRING to UTF-8 string;  
**MAC from Hex-STRING** \- convert Hex-STRING to MAC address string (which will have `' '` replaced by `':'`);  
**Integer from BITS** \- convert the first 8 bytes of a bit string expressed as a sequence of hex characters (e.g. "1A 2B 3C 4D") into a 64-bit unsigned integer. In bit strings longer than 8 bytes, consequent bytes will be ignored.  
If you mark the _Custom on fail_ checkbox, it is possible to specify custom error-handling options: either to discard the value, set a specified value or set a specified error message.  
Custom scripts  
| _JavaScript_ | Enter JavaScript code in the modal editor that opens when clicking in the parameter field or on the pencil icon next to it.  
Note that available JavaScript length depends on the [database used](/documentation/current/en/manual/config/items/item#custom-script-limit).  
For more information, see: [Javascript preprocessing](/documentation/current/en/manual/config/items/preprocessing/javascript)  
Validation  
| _Does not match regular expression_ | Specify a regular expression that a value must not match.  
E.g. `Error:(.*?)\.`  
If you mark the _Custom on fail_ checkbox, it is possible to specify custom error-handling options: either to discard the value, set a specified value or set a specified error message.  
_Check for error in JSON_ | Check for an application-level error message located at JSONPath. Stop processing if succeeded and message is not empty; otherwise continue processing with the value that was before this preprocessing step. Note that these external service errors are reported to user as is, without adding preprocessing step information.  
E.g. `$.errors`. If a JSON like `{"errors":"e1"}` is received, the next preprocessing step will not be executed.  
If you mark the _Custom on fail_ checkbox, it is possible to specify custom error-handling options: either to discard the value, set a specified value or set a specified error message.  
_Check for error in XML_ | Check for an application-level error message located at Xpath. Stop processing if succeeded and message is not empty; otherwise continue processing with the value that was before this preprocessing step. Note that these external service errors are reported to user as is, without adding preprocessing step information.  
No error will be reported in case of failing to parse invalid XML.  
If you mark the _Custom on fail_ checkbox, it is possible to specify custom error-handling options: either to discard the value, set a specified value or set a specified error message.  
| _Matches regular expression_ | Specify a regular expression that a value must match.  
If you mark the _Custom on fail_ checkbox, it is possible to specify custom error-handling options: either to discard the value, set a specified value or set a specified error message.  
Throttling  
| _Discard unchanged with heartbeat_ | Discard a value if it has not changed within the defined time period (in seconds).  
Positive integer values are supported to specify the seconds (minimum - 1 second). Time suffixes can be used in this field (e.g. 30s, 1m, 2h, 1d). User macros and low-level discovery macros can be used in this field.  
Only one throttling option can be specified for a discovery item.  
E.g. `1m`. If identical text is passed into this rule twice within 60 seconds, it will be discarded.  
_Note_ : Changing item prototypes does not reset throttling. Throttling is reset only when preprocessing steps are changed.  
Prometheus  
| _Prometheus to JSON_ | Convert required Prometheus metrics to JSON.  
See [Prometheus checks](/documentation/current/en/manual/config/items/itemtypes/prometheus) for more details.  
  
Note that if the discovery rule has been applied to the host via template then the content of this tab is read-only.

#### Custom macros

The **LLD macros** tab allows to specify custom low-level discovery macros.

Custom macros are useful in cases when the returned JSON does not have the required macros already defined. So, for example:

  * The native `vfs.fs.discovery` key for filesystem discovery returns a JSON with some pre-defined LLD macros such as {#FSNAME}, {#FSTYPE}. These macros can be used in item, trigger prototypes (see subsequent sections of the page) directly; defining custom macros is not needed;
  * The `vfs.fs.get` agent item also returns a JSON with [filesystem data](/documentation/current/en/manual/discovery/low_level_discovery/examples/mounted_filesystems), but without any pre-defined LLD macros. In this case you may define the macros yourself, and map them to the values in the JSON using JSONPath:

![](/documentation/current/assets/en/manual/discovery/low_level_discovery/lld_fs_c.png)

The extracted values can be used in discovered items, triggers, etc. Note that values will be extracted from the result of discovery and any preprocessing steps so far.

_LLD macro_ | Name of the low-level discovery macro, using the following syntax: {#MACRO}.  
---|---  
_JSONPath_ | Path that is used to extract LLD macro value from an LLD row, using JSONPath syntax.  
The values extracted from the returned JSON are used to replace the LLD macros in item, trigger, etc. prototype fields.  
JSONPath can be specified using the dot notation or the bracket notation. Bracket notation should be used in case of any special characters and Unicode, like `$['unicode + special chars #1']['unicode + special chars #2']`.  
  
For example, `$.foo` will extract "bar" and "baz" from this JSON: `[{"foo":"bar"}, {"foo":"baz"}]`  
Note that `$.foo` will extract "bar" and "baz" also from this JSON: `{"data":[{"foo":"bar"}, {"foo":"baz"}]}` because a single "data" object is processed automatically (for backwards compatibility with the low-level discovery implementation in Zabbix versions before 4.2).  
  
#### Filter

A filter can be used to generate real items, triggers, and graphs only for entities that match the criteria. The **Filters** tab contains discovery rule filter definitions allowing to filter discovery values:

![](/documentation/current/assets/en/manual/discovery/low_level_discovery/lld_fs_d.png)

_Type of calculation_ | The following options for calculating filters are available:  
**And** \- all filters must be passed;  
**Or** \- enough if one filter is passed;  
**And/Or** \- uses _And_ with different macro names and _Or_ with the same macro name;  
**Custom expression** \- offers the possibility to define a custom calculation of filters. The formula must include all filters in the list. Limited to 255 symbols.  
---|---  
_Filters_ | The following filter condition operators are available: _matches_ , _does not match_ , _exists_ , _does not exist_.  
_Matches_ and _does not match_ operators expect a [Perl Compatible Regular Expression](https://en.wikipedia.org/wiki/Perl_Compatible_Regular_Expressions) (PCRE). For instance, if you are only interested in C:, D:, and E: file systems, you could put {#FSNAME} into "Macro" and "^C|^D|^E" regular expression into "Regular expression" text fields. Filtering is also possible by file system types using {#FSTYPE} macro (e.g. "^ext|^reiserfs") and by drive types (supported only by Windows agent) using {#FSDRIVETYPE} macro (e.g., "fixed").  
You can enter a regular expression or reference a global [regular expression](/documentation/current/en/manual/regular_expressions) in "Regular expression" field.  
In order to test a regular expression you can use "grep -E", for example: `for f in ext2 nfs reiserfs smbfs; do echo $f | grep -E '^ext|^reiserfs' || echo "SKIP: $f"; done`   
  
_Exists_ and _does not exist_ operators allow to filter entities based on the presence or absence of the specified LLD macro in the response.  
Note that if a macro from the filter is missing in the response, the found entity will be ignored, unless a "does not exist" condition is specified for this macro.  
  
A warning will be displayed, if the absence of a macro affects the expression result. For example, if {#B} is missing in:  
{#A} matches 1 and {#B} matches 2 - will give a warning  
{#A} matches 1 or {#B} matches 2 - no warning  
  
A mistake or a typo in the regular expression used in the LLD rule (for example, an incorrect "File systems for discovery" regular expression) may cause deletion of thousands of configuration elements, historical values, and events for many hosts.

Zabbix database in MySQL must be created as case-sensitive if file system names that differ only by case are to be discovered correctly.

#### Override

The **Overrides** tab allows setting rules to modify the list of item, trigger, graph, host, and discovery prototypes or their attributes for discovered objects that meet given criteria.

![](/documentation/current/assets/en/manual/discovery/low_level_discovery/lld_fs_e.png)

Overrides (if any) are displayed in a reorderable drag-and-drop list and executed in the order in which they are defined. To configure details of a new override, click on ![](/documentation/current/assets/en/manual/config/add_link.png) in the _Overrides_ block. To edit an existing override, click on the override name. A popup window will open allowing to edit the override rule details.

![](/documentation/current/assets/en/manual/discovery/low_level_discovery/lld_override.png)

All mandatory parameters are marked with red asterisks.

_Name_ | A unique (per LLD rule) override name.  
---|---  
_If filter matches_ | Defines whether next overrides should be processed when filter conditions are met:  
**Continue overrides** \- subsequent overrides will be processed.  
**Stop processing** \- operations from preceding (if any) and this override will be executed, subsequent overrides will be ignored for matched LLD rows.  
_Filters_ | Determines to which discovered entities the override should be applied. Override filters are processed after discovery rule [filters](low_level_discovery#filter) and have the same functionality.  
_Operations_ | Override operations are displayed with these details:  
**Condition** \- an object type (item prototype/trigger prototype/graph prototype/host prototype) and a condition to be met (equals/does not equal/contains/does not contain/matches/does not match)  
**Actions** \- links for editing and removing an operation are displayed.  
  
**Configuring an operation**

To configure details of a new operation, click on ![](/documentation/current/assets/en/manual/config/add_link.png) in the Operations block. To edit an existing operation, click on ![](/documentation/current/assets/en/manual/config/edit_link.png) next to the operation. A popup window where you can edit the operation details will open.

![](/documentation/current/assets/en/manual/discovery/low_level_discovery/lld_override_op.png)

_Object_ | Four types of objects are available:  
Item prototype  
Trigger prototype  
Graph prototype  
Host prototype  
Discovery prototype  
---|---  
_Condition_ | Allows filtering entities to which the operation should be applied.  
| Operator | Supported operators:  
**equals** \- apply to this prototype  
**does not equal** \- apply to all prototypes, except this  
**contains** \- apply, if prototype name contains this string  
**does not contain** \- apply, if prototype name does not contain this string  
**matches** \- apply, if prototype name matches regular expression  
**does not match** \- apply, if prototype name does not match regular expression  
  
Pattern | A [regular expression](/documentation/current/en/manual/regular_expressions) or a string to search for.  
Object: _Item prototype_  
| _Create enabled_ | When the checkbox is marked, the buttons will appear, allowing to override original item prototype settings:  
_Yes_ \- the item will be added in an enabled state.  
_No_ \- the item will be added to a discovered entity but in a disabled state.  
_Discover_ | When the checkbox is marked, the buttons will appear, allowing to override original item prototype settings:  
_Yes_ \- the item will be added.  
_No_ \- the item will not be added.  
_Update interval_ | When the checkbox is marked, two options will appear, allowing to set different interval for the item:  
_Delay_ \- Item update interval. [User macros](/documentation/current/en/manual/config/macros/user_macros) and [time suffixes](/documentation/current/en/manual/appendix/suffixes) (e.g. 30s, 1m, 2h, 1d) are supported. Should be set to 0 if _Custom interval_ is used.  
_Custom interval_ \- click ![](/documentation/current/assets/en/manual/config/add_link.png) to specify flexible/scheduling intervals. For detailed information see [Custom intervals](/documentation/current/en/manual/config/items/item/custom_intervals).  
_History_ | When the checkbox is marked, the buttons will appear, allowing different history storage period to be set for the item:  
_Do not store_ \- if selected, the history will not be stored.  
_Store up to_ \- if selected, an input field for specifying storage period will appear to the right. [User macros](/documentation/current/en/manual/config/macros/user_macros) and [LLD macros](/documentation/current/en/manual/config/macros/lld_macros) are supported.  
_Trends_ | When the checkbox is marked, the buttons will appear, allowing different trend storage period to be set for the item:  
_Do not store_ \- if selected, the trends will not be stored.  
_Store up to_ \- if selected, an input field for specifying storage period will appear to the right. [User macros](/documentation/current/en/manual/config/macros/user_macros) and [LLD macros](/documentation/current/en/manual/config/macros/lld_macros) are supported.  
_Tags_ | When the checkbox is marked, a new block will appear, allowing to specify tag-value pairs.  
These tags will be appended to the tags specified in the item prototype, even if the tag names match.  
Object: _Trigger prototype_  
| _Create enabled_ | When the checkbox is marked, the buttons will appear, allowing to override original trigger prototype settings:  
_Yes_ \- the trigger will be added in an enabled state.  
_No_ \- the trigger will be added to a discovered entity, but in a disabled state.  
_Discover_ | When the checkbox is marked, the buttons will appear, allowing to override original trigger prototype settings:  
_Yes_ \- the trigger will be added.  
_No_ \- the trigger will not be added.  
_Severity_ | When the checkbox is marked, trigger severity buttons will appear, allowing to modify trigger severity.  
_Tags_ | When the checkbox is marked, a new block will appear, allowing to specify tag-value pairs.  
These tags will be appended to the tags specified in the trigger prototype, even if the tag names match.  
Object: _Graph prototype_  
| _Discover_ | When the checkbox is marked, the buttons will appear, allowing to override original graph prototype settings:  
_Yes_ \- the graph will be added.  
_No_ \- the graph will not be added.  
Object: _Host prototype_  
| _Create enabled_ | When the checkbox is marked, the buttons will appear, allowing to override original host prototype settings:  
_Yes_ \- the host will be created in an enabled state.  
_No_ \- the host will be created in a disabled state.  
_Discover_ | When the checkbox is marked, the buttons will appear, allowing to override original host prototype settings:  
_Yes_ \- the host will be discovered.  
_No_ \- the host will not be discovered.  
_Link templates_ | When the checkbox is marked, an input field for specifying templates will appear. Start typing the template name or click on _Select_ next to the field and select templates from the list in a popup window.  
Templates from this override are added to all templates already linked to the host prototype.  
_Tags_ | When the checkbox is marked, a new block will appear, allowing to specify tag-value pairs.  
These tags will be appended to the tags specified in the host prototype, even if the tag names match.  
_Host inventory_ | When the checkbox is marked, the buttons will appear, allowing to select different inventory [mode](/documentation/current/en/manual/config/hosts/inventory) for the host prototype:  
_Disabled_ \- do not populate host inventory  
 _Manual_ \- provide details manually  
 _Automated_ \- auto-fill host inventory data based on collected metrics.  
  
#### Form buttons

Buttons at the bottom of the form allow to perform several operations.

![](/documentation/current/assets/en/manual/config/button_add.png) | Add a discovery rule. This button is only available for new discovery rules.  
---|---  
![](/documentation/current/assets/en/manual/config/button_update.png) | Update the properties of a discovery rule. This button is only available for existing discovery rules.  
![](/documentation/current/assets/en/manual/config/button_clone.png) | Create another discovery rule based on the properties of the current discovery rule.  
![](/documentation/current/assets/en/manual/config/button_execute.png) | Perform discovery based on the discovery rule immediately. The discovery rule must already exist. See [more details](/documentation/current/en/manual/config/items/check_now).  
_Note_ that when performing discovery immediately, configuration cache is not updated, thus the result will not reflect very recent changes to discovery rule configuration.  
![](/documentation/current/assets/en/manual/config/button_test.png) | Test the discovery rule configuration. Use this button to verify the configuration settings (such as connectivity and parameter correctness) without permanently applying any changes.  
![](/documentation/current/assets/en/manual/config/button_delete.png) | Delete the discovery rule.  
![](/documentation/current/assets/en/manual/config/button_cancel.png) | Cancel the editing of discovery rule properties.  
  
### Discovered entities

The screenshots below illustrate how discovered items, triggers, and graphs look like in the host's configuration. Discovered entities are prefixed with an orange link to a discovery rule they come from.

![](/documentation/current/assets/en/manual/discovery/low_level_discovery/discovered_items1.png)

Note that discovered entities will not be created in case there are already existing entities with the same uniqueness criteria, for example, an item with the same key or graph with the same name. An error message is displayed in this case in the frontend that the low-level discovery rule could not create certain entities. The discovery rule itself, however, will not turn unsupported because some entity could not be created and had to be skipped. The discovery rule will go on creating/updating other entities.

If a discovered entity (host, file system, interface, etc) stops being discovered (or does not pass the filter anymore) the entities that were created based on it may be automatically disabled and eventually deleted.

Lost resources may be automatically disabled based on the value of the _Disable lost resources_ parameter. This affects lost hosts, items and triggers.

Lost resources may be automatically deleted based on the value of the _Delete lost resources_ parameter. This affects lost hosts, host groups, items, triggers, and graphs.

When discovered entities become 'Not discovered anymore', a lifetime indicator is displayed in the entity list. Move your mouse pointer over it and a message will be displayed indicating its status details.

![](/documentation/current/assets/en/manual/discovery/low_level_discovery/not_discovered_message.png)

If entities were marked for deletion, but were not deleted at the expected time (disabled discovery rule or item host), they will be deleted the next time the discovery rule is processed.

Entities containing other entities, which are marked for deletion, will not update if changed on the discovery rule level. For example, LLD-based triggers will not update if they contain items that are marked for deletion.

![](/documentation/current/assets/en/manual/discovery/low_level_discovery/discovered_triggers1.png)

![](/documentation/current/assets/en/manual/discovery/low_level_discovery/discovered_graphs1.png)

### Other types of discovery

More detail and how-tos on other types of out-of-the-box discovery is available in the following sections:

  * discovery of [network interfaces](/documentation/current/en/manual/discovery/low_level_discovery/examples/network_interfaces)
  * discovery of [CPUs and CPU cores](/documentation/current/en/manual/discovery/low_level_discovery/examples/cpu)
  * discovery of [SNMP OIDs](/documentation/current/en/manual/discovery/low_level_discovery/examples/snmp_oids)
  * discovery of [JMX objects](/documentation/current/en/manual/discovery/low_level_discovery/examples/jmx);
  * discovery using [ODBC SQL queries](/documentation/current/en/manual/discovery/low_level_discovery/examples/sql_queries)
  * discovery of [Windows services](/documentation/current/en/manual/discovery/low_level_discovery/examples/windows_services)
  * discovery of [host interfaces](/documentation/current/en/manual/discovery/low_level_discovery/examples/host_interfaces) in Zabbix

For more detail on the JSON format for discovery items and an example of how to implement your own file system discoverer as a Perl script, see [creating custom LLD rules](/documentation/current/en/manual/discovery/low_level_discovery/custom_rules).