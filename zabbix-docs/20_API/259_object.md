---
title: Script object
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/script/object
downloaded: 2025-11-14 10:44:12
---

# Script object

The following objects are directly related to the `script` API.

### Script

The script object has the following properties.

scriptid | ID | ID of the script.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
\- _required_ for update operations  
---|---|---  
name | string | Name of the script.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
type | integer | Script type.  
  
Possible values if `scope` is set to "action operation":  
0 - Script;  
1 - IPMI;  
2 - SSH;  
3 - TELNET;  
5 - Webhook.  
  
Possible values if `scope` is set to "manual host action" or "manual event action":  
6 - URL.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
command | string | Command to run.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `type` is set to "Script", "IPMI", "SSH", "TELNET", or "Webhook"  
scope | integer | Script scope.  
  
Possible values:  
1 - action operation;  
2 - manual host action;  
4 - manual event action.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
execute_on | integer | Where to run the script.  
  
Possible values:  
0 - run on Zabbix agent;  
1 - run on Zabbix server. It is _supported_ only if execution of global scripts is enabled on Zabbix server;  
2 - _(default)_ run on Zabbix server or proxy.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `type` is set to "Script"  
menu_path | string | Folders separated by slash that form a menu like navigation in frontend when clicked on host or event.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `scope` is set to "manual host action" or "manual event action"  
authtype | integer | Authentication method used for SSH script type.  
  
Possible values:  
0 - password;  
1 - public key.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `type` is set to "SSH"  
username | string | User name used for authentication.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `type` is set to "SSH" or "TELNET"  
password | string | Password used for SSH scripts with password authentication and TELNET scripts.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `type` is set to "SSH" and `authtype` is set to "password", or `type` is set to "TELNET"  
publickey | string | Name of the public key file used for SSH scripts with public key authentication.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `type` is set to "SSH" and `authtype` is set to "public key"  
privatekey | string | Name of the private key file used for SSH scripts with public key authentication.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `type` is set to "SSH" and `authtype` is set to "public key"  
port | string | Port number used for SSH and TELNET scripts.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `type` is set to "SSH" or "TELNET"  
groupid | ID | ID of the host group that the script can be run on.  
  
If set to "0", the script will be available on all host groups.  
  
Default: 0.  
usrgrpid | ID | ID of the user group that will be allowed to run the script.  
  
If set to "0", the script will be available for all user groups.  
  
Default: 0.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `scope` is set to "manual host action" or "manual event action"  
host_access | integer | Host permissions needed to run the script.  
  
Possible values:  
2 - _(default)_ read;  
3 - write.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `scope` is set to "manual host action" or "manual event action"  
confirmation | string | Confirmation pop up text.  
The pop up will appear when trying to run the script from the Zabbix frontend.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `scope` is set to "manual host action" or "manual event action"  
timeout | string | Webhook script execution timeout in seconds. Time suffixes are supported (e.g., 30s, 1m).  
  
Possible values: 1-60s.  
  
Default: 30s.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `type` is set to "Webhook"  
parameters | array | Array of [webhook input parameters](/documentation/current/en/manual/api/reference/script/object#webhook-parameters).  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `type` is set to "Webhook"  
description | string | Description of the script.  
url | string | User defined URL.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `type` is set to "URL"  
new_window | integer | Open URL in a new window.  
  
Possible values:  
0 - No;  
1 - _(default)_ Yes.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `type` is set to "URL"  
manualinput | integer | Indicates whether the script accepts user-provided input.  
  
Possible values:  
0 - _(default)_ Disabled;  
1 - Enabled;  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `scope` is set to "manual host action" or "manual event action"  
manualinput_prompt | string | Manual input prompt text.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `manualinput` is set to "Enabled"  
manualinput_validator | string | A character string field used to validate the user provided input. The string consists of either a regular expression or a set of values separated by commas.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `manualinput` is set to "Enabled"  
manualinput_validator_type | integer | Determines the type of user input expected.  
  
Possible values:  
0 - _(default)_ String. Indicates that manualinput_validator is to be treated as a regular expression;  
1 - List. Indicates that manualinput_validator is to be treated as a comma-separated list of possible input values.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `manualinput` is set to "Enabled"  
manualinput_default_value | string | Default value for auto-filling user input.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `manualinput_validator_type` is set to "String"  
  
#### Webhook parameters

Parameters passed to webhook script when it is called have the following properties.

name | string | Parameter name.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
value | string | Parameter value. Supports [macros](/documentation/current/en/manual/appendix/macros/supported_by_location).  
  
### Debug

Debug information of executed webhook script. The debug object has the following properties.

logs | array | Array of [log entries](/documentation/current/en/manual/api/reference/script/object#log-entry).  
---|---|---  
ms | string | Script execution duration in milliseconds.  
  
#### Log entry

The log entry object has the following properties.

level | integer | Log level.  
---|---|---  
ms | string | The time elapsed in milliseconds since the script was run before log entry was added.  
message | string | Log message.