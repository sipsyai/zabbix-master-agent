---
title: LLD rule prototype object
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/discoveryruleprototype/object
downloaded: 2025-11-14 10:43:03
---

# LLD rule prototype object

The following objects are directly related to the `discoveryruleprototype` API.

### LLD rule prototype

The low-level discovery rule prototype object has the following properties.

itemid | ID | ID of the LLD rule prototype.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
\- _required_ for update operations  
---|---|---  
ruleid | ID | ID of the parent LLD rule/LLD rule prototype.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
\- _required_ for create operations  
delay | string | Update interval of the LLD rule prototype.  
  
Accepts seconds or time unit with suffix (e.g., 30s, 1m, 2h, 1d) and, optionally, one or more [custom intervals](/documentation/current/en/manual/config/items/item/custom_intervals), all separated by semicolons. Custom intervals can be a mix of flexible and scheduling intervals.  
  
Accepts user macros. If used, the value must be a single macro. Multiple macros or macros mixed with text are not supported. Flexible intervals may be written as two macros separated by a forward slash (e.g., `{$FLEX_INTERVAL}/{$FLEX_PERIOD}`).  
  
Example:  
`1h;wd1-5h9-18;{$Macro1}/1-7,00:00-24:00;0/6-7,12:00-24:00;{$Macro2}/{$Macro3}`  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `type` is set to "Zabbix agent" (0), "Simple check" (3), "Zabbix internal" (5), "External check" (10), "Database monitor" (11), "IPMI agent" (12), "SSH agent" (13), "TELNET agent" (14), "JMX agent" (16), "HTTP agent" (19), "SNMP agent" (20), "Script" (21), "Browser" (22), or if `type` is set to "Zabbix agent (active)" (7) and `key_` does not contain "mqtt.get"  
hostid | ID | ID of the host that the LLD rule prototype belongs to.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _constant_  
\- _required_ for create operations  
flags | integer | [Origin](/documentation/current/en/manual/api/reference_commentary#entity-origin-flags) of the LLD rule prototype.  
  
Possible values:  
3 - a low-level discovery rule prototype;  
7 - a discovered low-level discovery rule prototype.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
interfaceid | ID | ID of the LLD rule prototype's host interface.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if LLD rule prototype belongs to host and `type` is set to "Zabbix agent", "IPMI agent", "JMX agent", or "SNMP agent"  
\- _supported_ if LLD rule prototype belongs to host and `type` is set to "Simple check", "External check", "SSH agent", "TELNET agent", or "HTTP agent"  
key_ | string | LLD rule prototype key. At least one LLD macro is required.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
\- _read-only_ for inherited objects  
name | string | Name of the LLD rule prototype.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
\- _read-only_ for inherited objects  
type | integer | Type of the LLD rule prototype.  
  
Possible values:  
0 - Zabbix agent;  
2 - Zabbix trapper;  
3 - Simple check;  
5 - Zabbix internal;  
7 - Zabbix agent (active);  
10 - External check;  
11 - Database monitor;  
12 - IPMI agent;  
13 - SSH agent;  
14 - TELNET agent;  
16 - JMX agent;  
18 - Dependent item;  
19 - HTTP agent;  
20 - SNMP agent;  
21 - Script;  
22 - Browser;  
23 - Nested.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
\- _read-only_ for inherited objects  
url | string | URL string.  
Supports user macros, {HOST.IP}, {HOST.CONN}, {HOST.DNS}, {HOST.HOST}, {HOST.NAME}, {HOST.PORT}, {ITEM.ID}, {ITEM.KEY}.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `type` is set to "HTTP agent"  
\- _read-only_ for inherited objects  
allow_traps | integer | Allow to populate value similarly to the trapper item.  
  
Possible values:  
0 - _(default)_ Do not allow to accept incoming data;  
1 - Allow to accept incoming data.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `type` is set to "HTTP agent"  
authtype | integer | Authentication method.  
  
Possible values if `type` is set to "SSH agent":  
0 - _(default)_ password;  
1 - public key.  
  
Possible values if `type` is set to "HTTP agent":  
0 - _(default)_ none;  
1 - basic;  
2 - NTLM.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `type` is set to "SSH agent" or "HTTP agent"  
\- _read-only_ for inherited objects (if `type` is set to "HTTP agent")  
description | string | Description of the LLD rule prototype.  
error | string | Error text if there are problems updating the LLD rule prototype value.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
follow_redirects | integer | Follow response redirects while polling data.  
  
Possible values:  
0 - Do not follow redirects;  
1 - _(default)_ Follow redirects.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `type` is set to "HTTP agent"  
\- _read-only_ for inherited objects  
headers | array | Array of headers that will be sent when performing an HTTP request.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `type` is set to "HTTP agent"  
\- _read-only_ for inherited objects  
http_proxy | string | HTTP(S) proxy connection string.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `type` is set to "HTTP agent"  
\- _read-only_ for inherited objects  
ipmi_sensor | string | IPMI sensor.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `type` is set to "IPMI agent" and `key_` is not set to "ipmi.get"  
\- _supported_ if `type` is set to "IPMI agent"  
\- _read-only_ for inherited objects  
jmx_endpoint | string | JMX agent custom connection string.  
  
Default: service:jmx:rmi:///jndi/rmi://{HOST.CONN}:{HOST.PORT}/jmxrmi  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `type` is set to "JMX agent"  
lifetime | string | Time period after which items that are no longer discovered will be deleted. Accepts seconds, time unit with suffix, or a user macro.  
  
Default: `7d`.  
lifetime_type | integer | Scenario to delete lost LLD resources.  
  
Possible values:  
0 - _(default)_ Delete after lifetime threshold is reached;  
1 - Do not delete;  
2 - Delete immediately.  
enabled_lifetime | string | Time period after which items that are no longer discovered will be disabled. Accepts seconds, time unit with suffix, or a user macro.  
  
Default: `0`.  
enabled_lifetime_type | integer | Scenario to disable lost LLD resources.  
  
Possible values:  
0 - Disable after lifetime threshold is reached;  
1 - Do not disable;  
2 - _(default)_ Disable immediately.  
master_itemid | ID | ID of the master item.  
Discovery rule cannot be master item for another discovery rule.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `type` is set to "Dependent item"  
\- _read-only_ for inherited objects  
output_format | integer | Should the response be converted to JSON.  
  
Possible values:  
0 - _(default)_ Store raw;  
1 - Convert to JSON.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `type` is set to "HTTP agent"  
\- _read-only_ for inherited objects  
params | string | Additional parameters depending on the type of the LLD rule prototype:  
\- executed script for SSH and Telnet LLD rules;  
\- SQL query for database monitor LLD rules;  
\- formula for calculated LLD rules;  
\- the script for script and browser LLD rules.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `type` is set to "Database monitor", "SSH agent", "TELNET agent", "Script" or "Browser"  
\- _read-only_ for inherited objects (if `type` is set to "Script" or "Browser")  
parameters | object/array | Additional parameters if `type` is set to "Script" or "Browser".  
Array of objects with `name` and `value` properties, where `name` must be unique.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `type` is set to "Script" or "Browser"  
\- _read-only_ for inherited objects  
password | string | Password for authentication.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `type` is set to "JMX agent" and `username` is set  
\- _supported_ if `type` is set to "Simple check", "Database monitor", "SSH agent", "TELNET agent", or "HTTP agent"  
\- _read-only_ for inherited objects (if `type` is set to "HTTP agent")  
post_type | integer | Type of post data body stored in `posts` property.  
  
Possible values:  
0 - _(default)_ Raw data;  
2 - JSON data;  
3 - XML data.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `type` is set to "HTTP agent"  
\- _read-only_ for inherited objects  
posts | string | HTTP(S) request body data.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `type` is set to "HTTP agent" and `post_type` is set to "JSON data" or "XML data"  
\- _supported_ if `type` is set to "HTTP agent" and `post_type` is set to "Raw data"  
\- _read-only_ for inherited objects  
privatekey | string | Name of the private key file.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `type` is set to "SSH agent" and `authtype` is set to "public key"  
publickey | string | Name of the public key file.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `type` is set to "SSH agent" and `authtype` is set to "public key"  
query_fields | array | Array of query fields that will be sent when performing an HTTP request.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `type` is set to "HTTP agent"  
\- _read-only_ for inherited objects  
request_method | integer | Type of request method.  
  
Possible values:  
0 - _(default)_ GET;  
1 - POST;  
2 - PUT;  
3 - HEAD.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `type` is set to "HTTP agent"  
\- _read-only_ for inherited objects  
retrieve_mode | integer | What part of response should be stored.  
  
Possible values if `request_method` is set to "GET", "POST", or "PUT":  
0 - _(default)_ Body;  
1 - Headers;  
2 - Both body and headers will be stored.  
  
Possible values if `request_method` is set to "HEAD":  
1 - Headers.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `type` is set to "HTTP agent"  
\- _read-only_ for inherited objects  
snmp_oid | string | SNMP OID.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `type` is set to "SNMP agent"  
\- _read-only_ for inherited objects  
ssl_cert_file | string | Public SSL Key file path.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `type` is set to "HTTP agent"  
\- _read-only_ for inherited objects  
ssl_key_file | string | Private SSL Key file path.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `type` is set to "HTTP agent"  
\- _read-only_ for inherited objects  
ssl_key_password | string | Password for SSL Key file.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `type` is set to "HTTP agent"  
\- _read-only_ for inherited objects  
state | integer | State of the LLD rule prototype.  
  
Possible values:  
0 - _(default)_ normal;  
1 - not supported.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
status | integer | Status of the LLD rule prototype.  
  
Possible values:  
0 - _(default)_ enabled LLD rule prototype;  
1 - disabled LLD rule prototype.  
status_codes | string | Ranges of required HTTP status codes, separated by commas. Also supports user macros as part of comma separated list.  
  
Example: 200,200-{$M},{$M},200-400  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `type` is set to "HTTP agent"  
\- _read-only_ for inherited objects  
templateid | ID | ID of the parent template LLD rule prototype.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
timeout | string | Item data polling request timeout.  
Accepts seconds or time unit with suffix (e.g., 30s, 1m). Also accepts user macros.  
  
Possible values range: 1-600s.  
  
Default: "" - use proxy/global settings.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `type` is set to "Zabbix agent" (0), "Simple check" (3) and `key_` does not start with "`vmware.`" and "`icmpping`", "Zabbix agent (active)" (7), "External check" (10), "Database monitor" (11), "SSH agent" (13), "TELNET agent" (14), "HTTP agent" (19), "SNMP agent" (20) and `snmp_oid` starts with "`walk[`" or "`get[`", "Script" (21), "Browser" (22)  
\- _read-only_ for inherited objects  
trapper_hosts | string | Allowed hosts.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `type` is set to "Zabbix trapper", or if `type` is set to "HTTP agent" and `allow_traps` is set to "Allow to accept incoming data"  
username | string | Username for authentication.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `type` is set to "SSH agent", "TELNET agent", or if `type` is set to "JMX agent" and `password` is set  
\- _supported_ if `type` is set to "Simple check", "Database monitor", or "HTTP agent"  
\- _read-only_ for inherited objects (if `type` is set to "HTTP agent")  
uuid | string | Universal unique identifier, used for linking imported LLD rule prototypes to already existing ones. Auto-generated, if not given.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if the LLD rule prototype belongs to a template  
verify_host | integer | Whether to validate that the host name for the connection matches the one in the host's certificate.  
  
Possible values:  
0 - _(default)_ Do not validate;  
1 - Validate.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `type` is set to "HTTP agent"  
\- _read-only_ for inherited objects  
verify_peer | integer | Whether to validate that the host's certificate is authentic.  
  
Possible values:  
0 - _(default)_ Do not validate;  
1 - Validate.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `type` is set to "HTTP agent"  
\- _read-only_ for inherited objects  
  
#### HTTP header

The header object has the following properties:

name | string | HTTP header name.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
value | string | Header value.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
  
#### HTTP query field

The query field object defines a name and value that is used to specify a URL parameter. It has the following properties:

name | string | Name of the parameter.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
value | string | Parameter value.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
  
### LLD rule prototype filter

The LLD rule prototype filter object defines a set of conditions that can be used to filter discovered objects. It has the following properties:

conditions | object/array | Set of filter conditions to use for filtering results. The conditions will be sorted in the order of their placement in the formula.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
evaltype | integer | Filter condition [evaluation method](/documentation/current/en/manual/discovery/low_level_discovery#filter).  
  
Possible values:  
0 - And/Or;  
1 - And;  
2 - Or;  
3 - Custom expression.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
eval_formula | string | Generated expression that will be used for evaluating filter conditions. The expression contains IDs that reference specific filter conditions by its `formulaid`. The value of `eval_formula` is equal to the value of `formula` for filters with a custom expression.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
formula | string | User-defined expression to be used for evaluating conditions of filters with a custom expression. The expression must contain IDs that reference specific filter conditions by its `formulaid`. The IDs used in the expression must exactly match the ones defined in the filter conditions: no condition can remain unused or omitted.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `evaltype` is set to "custom expression"  
  
#### LLD rule prototype filter condition

The LLD rule prototype filter condition object defines a separate check to perform on the value of an LLD macro. It has the following properties:

macro | string | LLD macro to perform the check on.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
value | string | Value to compare with.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `operator` is set to "matches regular expression" or "does not match regular expression"  
formulaid | string | Arbitrary unique ID that is used to reference the condition from a custom expression. Can only contain capital-case letters. The ID must be defined by the user when modifying filter conditions, but will be generated anew when requesting them afterward.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `evaltype` of LLD rule prototype filter object is set to "custom expression"  
operator | integer | Condition operator.  
  
Possible values:  
8 - _(default)_ matches regular expression;  
9 - does not match regular expression;  
12 - exists;  
13 - does not exist.  
  
To better understand how to use filters with various types of expressions, see examples on the [discoveryruleprototype.get](get#retrieving-filter-conditions) and [discoveryruleprototype.create](create#using-a-custom-expression-filter) method pages.

### LLD macro path

The LLD macro path has the following properties:

lld_macro | string | LLD macro.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
path | string | Selector for value which will be assigned to corresponding macro.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
  
### LLD rule prototype preprocessing

The LLD rule prototype preprocessing object has the following properties.

type | integer | The preprocessing option type.  
  
Possible values:  
5 - Regular expression;  
11 - XML XPath;  
12 - JSONPath;  
14 - Matches regular expression;  
15 - Does not match regular expression;  
16 - Check for error in JSON;  
17 - Check for error in XML;  
20 - Discard unchanged with heartbeat;  
21 - JavaScript;  
23 - Prometheus to JSON;  
24 - CSV to JSON;  
25 - Replace;  
27 - XML to JSON;  
28 - SNMP walk value;  
29 - SNMP walk to JSON;  
30 - SNMP get value.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
params | string | Additional parameters used by preprocessing option. Multiple parameters are separated by the newline (\n) character.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `type` is set to "Regular expression" (5), "XML XPath" (11), "JSONPath" (12), "Matches regular expression" (14), "Does not match regular expression" (15), "Check for error in JSON" (16), "Check for error in XML" (17), "Discard unchanged with heartbeat" (20), "JavaScript" (21), "Prometheus to JSON" (23), "CSV to JSON" (24), "Replace" (25), "SNMP walk value" (28), "SNMP walk to JSON" (29), or "SNMP get value" (30)  
error_handler | integer | Action type used in case of preprocessing step failure.  
  
Possible values:  
0 - Error message is set by Zabbix server;  
1 - Discard value;  
2 - Set custom value;  
3 - Set custom error message.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `type` is set to "Regular expression" (5), "XML XPath" (11), "JSONPath" (12), "Matches regular expression" (14), "Does not match regular expression" (15), "Check for error in JSON" (16), "Check for error in XML" (17), "Prometheus to JSON" (23), "CSV to JSON" (24), "XML to JSON" (27), "SNMP walk value" (28), "SNMP walk to JSON" (29), or "SNMP get value" (30)  
error_handler_params | string | Error handler parameters.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `error_handler` is set to "Set custom value" or "Set custom error message"  
  
The following parameters and error handlers are supported for each preprocessing type.

5 | Regular expression | pattern1 | output2 | 0, 1, 2, 3  
---|---|---|---|---  
11 | XML XPath | path3 | 0, 1, 2, 3  
12 | JSONPath | path3 | 0, 1, 2, 3  
14 | Matches regular expression | pattern1 | 0, 1, 2, 3  
15 | Does not match regular expression | pattern1 | 0, 1, 2, 3  
16 | Check for error in JSON | path3 | 0, 1, 2, 3  
17 | Check for error in XML | path3 | 0, 1, 2, 3  
20 | Discard unchanged with heartbeat | seconds4, 5  
21 | JavaScript | script2  
23 | Prometheus to JSON | pattern5, 6 | 0, 1, 2, 3  
24 | CSV to JSON | character2 | character2 | 0,1 | 0, 1, 2, 3  
25 | Replace | search string2 | replacement2  
27 | XML to JSON | 0, 1, 2, 3  
28 | SNMP walk value | OID2 | Format:  
0 - Unchanged  
1 - UTF-8 from Hex-STRING  
2 - MAC from Hex-STRING  
3 - Integer from BITS | 0, 1, 2, 3  
29 | SNMP walk to JSON7 | Field name2 | OID prefix2 | Format:  
0 - Unchanged  
1 - UTF-8 from Hex-STRING  
2 - MAC from Hex-STRING  
3 - Integer from BITS | 0, 1, 2, 3  
30 | SNMP get value | Format:  
1 - UTF-8 from Hex-STRING  
2 - MAC from Hex-STRING  
3 - Integer from BITS | 0, 1, 2, 3  
  
1 regular expression  
2 string  
3 JSONPath or XML XPath  
4 positive integer (with support of time suffixes, e.g. 30s, 1m, 2h, 1d)  
5 user macro  
6 Prometheus pattern following the syntax: `<metric name>{<label name>="<label value>", ...} == <value>`. Each Prometheus pattern component (metric, label name, label value and metric value) can be user macro.  
7 Supports multiple "Field name,OID prefix,Format records" records delimited by a new line character.

### LLD rule prototype overrides

The LLD rule prototype overrides object defines a set of rules (filters, conditions and operations) that are used to override properties of different prototype objects. It has the following properties:

name | string | Unique override name.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
step | integer | Unique order number of the override.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
stop | integer | Stop processing next overrides if matches.  
  
Possible values:  
0 - _(default)_ don't stop processing overrides;  
1 - stop processing overrides if filter matches.  
filter | object | Override filter.  
operations | object/array | Override operations.  
  
#### LLD rule prototype override filter

The LLD rule prototype override filter object defines a set of conditions that if they match the discovered object the override is applied. It has the following properties:

conditions | object/array | Set of override filter conditions to use for matching the discovered objects. The conditions will be sorted in the order of their placement in the formula.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
evaltype | integer | Override filter condition [evaluation method](/documentation/current/en/manual/discovery/low_level_discovery#override).  
  
Possible values:  
0 - And/Or;  
1 - And;  
2 - Or;  
3 - Custom expression.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
eval_formula | string | Generated expression that will be used for evaluating override filter conditions. The expression contains IDs that reference specific override filter conditions by its `formulaid`. The value of `eval_formula` is equal to the value of `formula` for filters with a custom expression.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
formula | string | User-defined expression to be used for evaluating conditions of override filters with a custom expression. The expression must contain IDs that reference specific override filter conditions by its `formulaid`. The IDs used in the expression must exactly match the ones defined in the override filter conditions: no condition can remain unused or omitted.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `evaltype` is set to "custom expression"  
  
##### LLD rule prototype override filter condition

The LLD rule prototype override filter condition object defines a separate check to perform on the value of an LLD macro. It has the following properties:

macro | string | LLD macro to perform the check on.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
value | string | Value to compare with.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `operator` is set to "matches regular expression" or "does not match regular expression"  
formulaid | string | Arbitrary unique ID that is used to reference the condition from a custom expression. Can only contain capital-case letters. The ID must be defined by the user when modifying filter conditions, but will be generated anew when requesting them afterward.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `evaltype` of LLD rule prototype override filter object is set to "custom expression"  
operator | integer | Condition operator.  
  
Possible values:  
8 - _(default)_ matches regular expression;  
9 - does not match regular expression;  
12 - exists;  
13 - does not exist.  
  
#### LLD rule prototype override operation

The LLD rule prototype override operation is combination of conditions and actions to perform on the prototype object. It has the following properties:

operationobject | integer | Type of discovered object to perform the action.  
  
Possible values:  
0 - Item prototype;  
1 - Trigger prototype;  
2 - Graph prototype;  
3 - Host prototype.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
operator | integer | Override condition [operator](/documentation/current/en/manual/discovery/low_level_discovery#discovery-rule).  
  
Possible values:  
0 - _(default)_ equals;  
1 - does not equal;  
2 - contains;  
3 - does not contain;  
8 - matches;  
9 - does not match.  
value | string | Pattern to match item, trigger, graph or host prototype name depending on selected object.  
opstatus | object | Override operation status object for item, trigger and host prototype objects.  
opdiscover | object | Override operation discover status object (all object types).  
opperiod | object | Override operation period (update interval) object for item prototype object.  
ophistory | object | Override operation history object for item prototype object.  
optrends | object | Override operation trends object for item prototype object.  
opseverity | object | Override operation severity object for trigger prototype object.  
optag | object/array | Override operation tag object for trigger and host prototype objects.  
optemplate | object/array | Override operation template object for host prototype object.  
opinventory | object | Override operation inventory object for host prototype object.  
  
##### LLD rule prototype override operation status

LLD rule prototype override operation status that is set to discovered object. It has the following properties:

status | integer | Override the status for selected object.  
  
Possible values:  
0 - Create enabled;  
1 - Create disabled.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
  
##### LLD rule prototype override operation discover

LLD rule prototype override operation discover status that is set to discovered object. It has the following properties:

discover | integer | Override the discover status for selected object.  
  
Possible values:  
0 - Yes, continue discovering the objects;  
1 - No, new objects will not be discovered and existing ones will be marked as lost.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
  
##### LLD rule prototype override operation period

LLD rule prototype override operation period is an update interval value that is set to discovered item. It has the following properties:

delay | string | Override the update interval of the item prototype.  
  
Accepts seconds or time unit with suffix (e.g., 30s, 1m, 2h, 1d) and, optionally, one or more [custom intervals](/documentation/current/en/manual/config/items/item/custom_intervals), all separated by semicolons. Custom intervals can be a mix of flexible and scheduling intervals.  
  
Accepts user macros or LLD macros. If used, the value must be a single macro. Multiple macros or macros mixed with text are not supported. Flexible intervals may be written as two macros separated by a forward slash (e.g., `{$FLEX_INTERVAL}/{$FLEX_PERIOD}`).  
  
Example:  
`1h;wd1-5h9-18;{$Macro1}/1-7,00:00-24:00;0/6-7,12:00-24:00;{$Macro2}/{$Macro3}`  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
  
##### LLD rule prototype override operation history

LLD rule prototype override operation history value that is set to discovered item. It has the following properties:

history | string | Override the history of item prototype which is a time unit of how long the history data should be stored. Also accepts user macro and LLD macro.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
  
##### LLD rule prototype override operation trends

LLD rule prototype override operation trends value that is set to discovered item. It has the following properties:

trends | string | Override the trends of item prototype which is a time unit of how long the trends data should be stored. Also accepts user macro and LLD macro.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
  
##### LLD rule prototype override operation severity

LLD rule prototype override operation severity value that is set to discovered trigger. It has the following properties:

severity | integer | Override the severity of trigger prototype.  
  
Possible values:  
0 - _(default)_ not classified;  
1 - information;  
2 - warning;  
3 - average;  
4 - high;  
5 - disaster.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
  
##### LLD rule prototype override operation tag

LLD rule prototype override operation tag object contains tag name and value that are set to discovered object. It has the following properties:

tag | string | New tag name.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
value | string | New tag value.  
  
##### LLD rule prototype override operation template

LLD rule prototype override operation template object that is linked to discovered host. It has the following properties:

templateid | ID | Override the template of host prototype linked templates.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
  
##### LLD rule prototype override operation inventory

LLD rule prototype override operation inventory mode value that is set to discovered host. It has the following properties:

inventory_mode | integer | Override the host prototype inventory mode.  
  
Possible values:  
-1 - disabled;  
0 - _(default)_ manual;  
1 - automatic.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---