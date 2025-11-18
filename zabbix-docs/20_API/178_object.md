---
title: Item prototype object
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/itemprototype/object
downloaded: 2025-11-14 10:42:51
---

# Item prototype object

The following objects are directly related to the `itemprototype` API.

### Item prototype

The item prototype object has the following properties.

itemid | ID | ID of the item prototype.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
\- _required_ for update operations  
---|---|---  
delay | string | Update interval of the item prototype.  
  
Accepts seconds or time unit with suffix (e.g., 30s, 1m, 2h, 1d) and, optionally, one or more [custom intervals](/documentation/current/en/manual/config/items/item/custom_intervals), all separated by semicolons. Custom intervals can be a mix of flexible and scheduling intervals.  
  
Accepts user macros and LLD macros. If used, the value must be a single macro. Multiple macros or macros mixed with text are not supported. Flexible intervals may be written as two macros separated by a forward slash (e.g., `{$FLEX_INTERVAL}/{$FLEX_PERIOD}`).  
  
Example:  
`1h;wd1-5h9-18;{$Macro1}/1-7,00:00-24:00;0/6-7,12:00-24:00;{$Macro2}/{$Macro3}`  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `type` is set to "Zabbix agent" (0), "Simple check" (3), "Zabbix internal" (5), "External check" (10), "Database monitor" (11), "IPMI agent" (12), "SSH agent" (13), "TELNET agent" (14), "Calculated" (15), "JMX agent" (16), "HTTP agent" (19), "SNMP agent" (20), "Script" (21), "Browser" (22), or if `type` is set to "Zabbix agent (active)" (7) and `key_` does not contain "mqtt.get"  
hostid | ID | ID of the host that the item prototype belongs to.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _constant_  
\- _required_ for create operations  
interfaceid | ID | ID of the item prototype's host interface.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if item prototype belongs to host and `type` is set to "Zabbix agent", "IPMI agent", "JMX agent", "SNMP trap", or "SNMP agent"  
\- _supported_ if item prototype belongs to host and `type` is set to "Simple check", "External check", "SSH agent", "TELNET agent", or "HTTP agent"  
key_ | string | Item prototype key.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
\- _read-only_ for inherited objects  
name | string | Name of the item prototype.  
Supports user macros.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
\- _read-only_ for inherited objects  
type | integer | Type of the item prototype.  
  
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
15 - Calculated;  
16 - JMX agent;  
17 - SNMP trap;  
18 - Dependent item;  
19 - HTTP agent;  
20 - SNMP agent;  
21 - Script;  
22 - Browser.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
\- _read-only_ for inherited objects  
url | string | URL string.  
Supports LLD macros, user macros, {HOST.IP}, {HOST.CONN}, {HOST.DNS}, {HOST.HOST}, {HOST.NAME}, {HOST.PORT}, {ITEM.ID}, {ITEM.KEY}.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `type` is set to "HTTP agent"  
\- _read-only_ for inherited objects  
value_type | integer | Type of information of the item prototype.  
  
Possible values:  
0 - numeric float;  
1 - character;  
2 - log;  
3 - numeric unsigned;  
4 - text;  
5 - binary.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
\- _read-only_ for inherited objects  
allow_traps | integer | Allow to populate value similarly to the trapper item.  
  
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
2 - NTLM;  
3 - Kerberos.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `type` is set to "SSH agent" or "HTTP agent"  
\- _read-only_ for inherited objects (if `type` is set to "HTTP agent")  
description | string | Description of the item prototype.  
flags | integer | [Origin](/documentation/current/en/manual/api/reference_commentary#entity-origin-flags) of the item prototype.  
  
Possible values:  
2 - an item prototype;  
6 - a discovered item prototype  
  
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
history | string | A time unit of how long the history data should be stored.  
Also accepts user macro and LLD macro.  
  
Default: 31d.  
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
logtimefmt | string | Format of the time in log entries.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `value_type` is set to "log"  
\- _read-only_ for inherited objects  
master_itemid | ID | ID of the master item.  
  
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
params | string | Additional parameters depending on the type of the item prototype:  
\- executed script for SSH agent and TELNET agent item prototypes;  
\- SQL query for database monitor item prototypes;  
\- formula for calculated item prototypes;  
\- the script for script and browser item prototypes.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `type` is set to "Database monitor", "SSH agent", "TELNET agent", "Calculated", "Script", or "Browser"  
\- _read-only_ for inherited objects (if `type` is set to "Script" or "Browser")  
parameters | object/array | Additional parameters if `type` is set to "Script" or "Browser". Array of objects with `name` and `value` properties, where `name` must be unique.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `type` is set to "Script" or "Browser"  
\- _read-only_ for inherited objects  
password | string | Password for authentication.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `type` is set to "JMX agent" and `username` is set  
\- _supported_ if `type` is set to "Simple check", "SSH agent", "TELNET agent", "Database monitor", or "HTTP agent"  
\- _read-only_ for inherited objects (if `type` is set to "HTTP agent")  
post_type | integer | Type of post data body stored in `posts` property.  
  
Possible values:  
0 - _(default)_ Raw data.  
2 - JSON data.  
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
status | integer | Status of the item prototype.  
  
Possible values:  
0 - _(default)_ enabled item prototype;  
1 - disabled item prototype;  
3 - unsupported item prototype.  
status_codes | string | Ranges of required HTTP status codes, separated by commas.  
Also supports user macros or LLD macros as part of comma separated list.  
  
Example: 200,200-{$M},{$M},200-400  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `type` is set to "HTTP agent"  
\- _read-only_ for inherited objects  
templateid | ID | ID of the parent template item prototype.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
timeout | string | Item data polling request timeout.  
Accepts seconds or time unit with suffix (e.g., 30s, 1m). Also accepts user macros and LLD macros.  
  
Possible values range: 1-600s.  
  
Default: "" - use proxy/global settings.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `type` is set to "Zabbix agent" (0), "Simple check" (3) and `key_` does not start with "`vmware.`" and "`icmpping`", "Zabbix agent (active)" (7), "External check" (10), "Database monitor" (11), "SSH agent" (13), "TELNET agent" (14), "HTTP agent" (19), "SNMP agent" (20) and `snmp_oid` starts with "`walk[`" or "`get[`", "Script" (21), "Browser" (22)  
\- _read-only_ for inherited objects  
trapper_hosts | string | Allowed hosts.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `type` is set to "Zabbix trapper", or if `type` is set to "HTTP agent" and `allow_traps` is set to "Allow to accept incoming data"  
trends | string | A time unit of how long the trends data should be stored.  
Also accepts user macro and LLD macro.  
  
Default: 365d.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `value_type` is set to "numeric float" or "numeric unsigned"  
units | string | Value units.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `value_type` is set to "numeric float" or "numeric unsigned"  
\- _read-only_ for inherited objects  
username | string | Username for authentication.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `type` is set to "SSH agent" or "TELNET agent", or if `type` is set to "JMX agent" and `password` is set  
\- _supported_ if `type` is set to "Simple check", "Database monitor", or "HTTP agent"  
\- _read-only_ for inherited objects (if `type` is set to "HTTP agent")  
uuid | string | Universal unique identifier, used for linking imported item prototypes to already existing ones. Auto-generated, if not given.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if the item prototype belongs to a template  
valuemapid | ID | ID of the associated value map.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `value_type` is set to "numeric float", "character", or "numeric unsigned"  
\- _read-only_ for inherited objects  
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
discover | integer | Item prototype discovery status.  
  
Possible values:  
0 - _(default)_ new items will be discovered;  
1 - new items will not be discovered and existing items will be marked as lost.  
  
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
  
### Item prototype tag

The item prototype tag object has the following properties.

tag | string | Item prototype tag name.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
value | string | Item prototype tag value.  
  
### Item prototype preprocessing

The item prototype preprocessing object has the following properties.

type | integer | The preprocessing option type.  
  
Possible values:  
1 - Custom multiplier;  
2 - Right trim;  
3 - Left trim;  
4 - Trim;  
5 - Regular expression;  
6 - Boolean to decimal;  
7 - Octal to decimal;  
8 - Hexadecimal to decimal;  
9 - Simple change;  
10 - Change per second;  
11 - XML XPath;  
12 - JSONPath;  
13 - In range;  
14 - Matches regular expression;  
15 - Does not match regular expression;  
16 - Check for error in JSON;  
17 - Check for error in XML;  
18 - Check for error using regular expression;  
19 - Discard unchanged;  
20 - Discard unchanged with heartbeat;  
21 - JavaScript;  
22 - Prometheus pattern;  
23 - Prometheus to JSON;  
24 - CSV to JSON;  
25 - Replace;  
26 - Check unsupported;  
27 - XML to JSON;  
28 - SNMP walk value;  
29 - SNMP walk to JSON;  
30 - SNMP get value.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
params | string | Additional parameters used by preprocessing option.  
Multiple parameters are separated by the newline (\n) character.  
  
If `type` is set to "Check unsupported", the parameters follow a `<scope>[\n<pattern>]` syntax, where _pattern_ is a regular expression, and _scope_ is one of:  
-1 - match any error;  
0 - check if error message matches _pattern_ ;  
1 - check if error message does not match _pattern_.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `type` is set to "Custom multiplier" (1), "Right trim" (2), "Left trim" (3), "Trim" (4), "Regular expression" (5), "XML XPath" (11), "JSONPath" (12), "In range" (13), "Matches regular expression" (14), "Does not match regular expression" (15), "Check for error in JSON" (16), "Check for error in XML" (17), "Check for error using regular expression" (18), "Discard unchanged with heartbeat" (20), "JavaScript" (21), "Prometheus pattern" (22), "Prometheus to JSON" (23), "CSV to JSON" (24), "Replace" (25), "Check unsupported" (26), "SNMP walk value" (28), "SNMP walk to JSON" (29), or "SNMP get value" (30)  
error_handler | integer | Action type used in case of preprocessing step failure.  
  
Possible values:  
0 - Error message is set by Zabbix server;  
1 - Discard value;  
2 - Set custom value;  
3 - Set custom error message.  
  
Possible values if `type` is set to "Check unsupported":  
1 - Discard value;  
2 - Set custom value;  
3 - Set custom error message.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `type` is set to "Custom multiplier" (1), "Regular expression" (5), "Boolean to decimal" (6), "Octal to decimal" (7), "Hexadecimal to decimal" (8), "Simple change" (9), "Change per second" (10), "XML XPath" (11), "JSONPath" (12), "In range" (13), "Matches regular expression" (14), "Does not match regular expression" (15), "Check for error in JSON" (16), "Check for error in XML" (17), "Check for error using regular expression" (18), "Prometheus pattern" (22), "Prometheus to JSON" (23), "CSV to JSON" (24), "Check unsupported" (26), "XML to JSON" (27), "SNMP walk value" (28), "SNMP walk to JSON" (29), or "SNMP get value" (30)  
error_handler_params | string | Error handler parameters.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `error_handler` is set to "Set custom value" or "Set custom error message"  
  
The following parameters and error handlers are supported for each preprocessing type.

1 | Custom multiplier | number1, 6 | 0, 1, 2, 3  
---|---|---|---  
2 | Right trim | list of characters2  
3 | Left trim | list of characters2  
4 | Trim | list of characters2  
5 | Regular expression | pattern3 | output2 | 0, 1, 2, 3  
6 | Boolean to decimal | 0, 1, 2, 3  
7 | Octal to decimal | 0, 1, 2, 3  
8 | Hexadecimal to decimal | 0, 1, 2, 3  
9 | Simple change | 0, 1, 2, 3  
10 | Change per second | 0, 1, 2, 3  
11 | XML XPath | path4 | 0, 1, 2, 3  
12 | JSONPath | path4 | 0, 1, 2, 3  
13 | In range | min1, 6 | max1, 6 | 0, 1, 2, 3  
14 | Matches regular expression | pattern3 | 0, 1, 2, 3  
15 | Does not match regular expression | pattern3 | 0, 1, 2, 3  
16 | Check for error in JSON | path4 | 0, 1, 2, 3  
17 | Check for error in XML | path4 | 0, 1, 2, 3  
18 | Check for error using regular expression | pattern3 | output2 | 0, 1, 2, 3  
19 | Discard unchanged  
20 | Discard unchanged with heartbeat | seconds5, 6  
21 | JavaScript | script2  
22 | Prometheus pattern | pattern6, 7 | `value`, `label`, `function` | output8, 9 | 0, 1, 2, 3  
23 | Prometheus to JSON | pattern6, 7 | 0, 1, 2, 3  
24 | CSV to JSON | character2 | character2 | 0,1 | 0, 1, 2, 3  
25 | Replace | search string2 | replacement2  
26 | Check unsupported | scope1 | pattern3, 6 | 1, 2, 3  
27 | XML to JSON | 0, 1, 2, 3  
28 | SNMP walk value | OID2 | Format:  
0 - Unchanged  
1 - UTF-8 from Hex-STRING  
2 - MAC from Hex-STRING  
3 - Integer from BITS | 0, 1, 2, 3  
29 | SNMP walk to JSON10 | Field name2 | OID prefix2 | Format:  
0 - Unchanged  
1 - UTF-8 from Hex-STRING  
2 - MAC from Hex-STRING  
3 - Integer from BITS | 0, 1, 2, 3  
30 | SNMP get value | Format:  
1 - UTF-8 from Hex-STRING  
2 - MAC from Hex-STRING  
3 - Integer from BITS | 0, 1, 2, 3  
  
1 integer or floating-point number  
2 string  
3 regular expression  
4 JSONPath or XML XPath  
5 positive integer (with support of time suffixes, e.g. 30s, 1m, 2h, 1d)  
6 user macro, LLD macro  
7 Prometheus pattern following the syntax: `<metric name>{<label name>="<label value>", ...} == <value>`. Each Prometheus pattern component (metric, label name, label value and metric value) can be user macro or LLD macro.  
8 Prometheus output following the syntax: `<label name>` (can be a user macro or an LLD macro) if `label` is selected as the second parameter.  
9 One of the aggregation functions: `sum`, `min`, `max`, `avg`, `count` if `function` is selected as the second parameter.  
10 Supports multiple "Field name,OID prefix,Format records" records delimited by a new line character.