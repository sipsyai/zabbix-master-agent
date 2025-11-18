---
title: User macros supported by location
source: https://www.zabbix.com/documentation/current/en/manual/appendix/macros/supported_by_location_user
downloaded: 2025-11-14 10:47:51
---

# 2 User macros supported by location

#### Overview

This section contains a list of locations, where [user-definable](/documentation/current/en/manual/config/macros/user_macros) macros are supported.

Only global-level user macros are supported for _Actions_ , _Network discovery_ , _Proxies_ and all locations listed under _Other locations_ section of this page. In the mentioned locations, host-level and template-level macros will not be resolved.

To customize macro values (for example, shorten or extract specific substrings), you can use [macro functions](/documentation/current/en/manual/config/macros/macro_functions).

#### Actions

In [actions](/documentation/current/en/manual/config/notifications/action), user macros can be used in the following fields:

Trigger-based notifications and commands | yes  
---|---  
Trigger-based internal notifications | yes  
Problem update notifications | yes  
Service-based notifications and commands | yes  
Service update notifications | yes  
Time period condition | no  
_Operations_  
| Default operation step duration | no  
Step duration | no  
  
#### Hosts/host prototypes

In a [host](/documentation/current/en/manual/config/hosts/host) and [host prototype](/documentation/current/en/manual/vm_monitoring/example#create-a-host-prototype) configuration, user macros can be used in the following fields:

Interface IP/DNS | DNS only  
---|---  
Interface port | no  
_SNMP v1, v2_  
| SNMP community | yes  
_SNMP v3_  
| Context name | yes  
Security name | yes  
Authentication passphrase | yes  
Privacy passphrase | yes  
_IPMI_  
| Username | yes  
Password | yes  
_Tags_[2](supported_by_location_user#footnotes)  
| Tag names | yes  
Tag values | yes  
  
#### Items / item prototypes

In an [item](/documentation/current/en/manual/config/items/item) or an [item prototype](/documentation/current/en/manual/discovery/low_level_discovery/item_prototypes) configuration, user macros can be used in the following fields:

Item name | yes  
---|---  
Item key parameters | yes  
Update interval | no  
Custom intervals | no  
Timeout (available for [supported](/documentation/current/en/manual/web_interface/frontend_sections/administration/general#timeouts) item types) | no  
Store up to (for history and trends) | no  
Description | yes  
_Calculated/aggregate item_  
| Formula (expression constants and function parameters; item key parameters; (_aggregate item only_) filter conditions (host group name and tag name)) | yes  
_Database monitor_  
| Username | yes  
Password | yes  
SQL query | yes  
_HTTP agent_  
| URL[3](supported_by_location_user#footnotes) | yes  
Query fields | yes  
Request body | yes  
Headers (names and values) | yes  
Required status codes | yes  
HTTP proxy | yes  
HTTP authentication username | yes  
HTTP authentication password | yes  
SSl certificate file | yes  
SSl key file | yes  
SSl key password | yes  
Allowed hosts | yes  
_JMX agent_  
| JMX endpoint | yes  
_Script item_  
| Parameter names and values | yes  
_Browser item_  
| Parameter names and values | yes  
_SNMP agent_  
| SNMP OID | yes  
_SSH agent_  
| Username | yes  
Public key file | yes  
Private key file | yes  
Password | yes  
Script | yes  
_TELNET agent_  
| Username | yes  
Password | yes  
Script | yes  
_Zabbix trapper_  
| Allowed hosts | yes  
_Tags_[2](supported_by_location_user#footnotes)  
| Tag names | yes  
Tag values | yes  
_Preprocessing steps_  
| Parameters (including custom scripts) | yes  
| Custom error-handling parameters (_Set value to_ and _Set error to_ fields) | yes  
  
#### Low-level discovery

In a [low-level discovery rule](/documentation/current/en/manual/discovery/low_level_discovery#configuring-low-level-discovery), user macros can be used in the following fields:

Key parameters | yes  
---|---  
Update interval | no  
Custom interval | no  
Timeout (available for [supported](/documentation/current/en/manual/web_interface/frontend_sections/administration/general#timeouts) item types) | no  
Delete lost resources | no  
Disable lost resources | no  
Description | yes  
_SNMP agent_  
| SNMP OID | yes  
_SSH agent_  
| Username | yes  
Public key file | yes  
Private key file | yes  
Password | yes  
Script | yes  
_TELNET agent_  
| Username | yes  
Password | yes  
Script | yes  
_Zabbix trapper_  
| Allowed hosts | yes  
_Database monitor_  
| Username | yes  
Password | yes  
SQL query | yes  
_JMX agent_  
| JMX endpoint | yes  
_HTTP agent_  
| URL[3](supported_by_location_user#footnotes) | yes  
Query fields | yes  
Request body | yes  
Headers (names and values) | yes  
Required status codes | yes  
HTTP authentication username | yes  
HTTP authentication password | yes  
_Filters_  
| Regular expression | yes  
_Overrides_  
| Filters: regular expression | yes  
Operations: update interval (for item prototypes) | no  
Operations: history storage period (for item prototypes) | no  
Operations: trend storage period (for item prototypes) | no  
  
#### Network discovery

In a [network discovery rule](/documentation/current/en/manual/discovery/network_discovery/rule), user macros can be used in the following fields:

Update interval | no  
---|---  
_SNMP v1, v2_  
| SNMP community | yes  
SNMP OID | yes  
_SNMP v3_  
| Context name | yes  
Security name | yes  
Authentication passphrase | yes  
Privacy passphrase | yes  
SNMP OID | yes  
  
#### Proxies

In a [proxy](/documentation/current/en/manual/distributed_monitoring/proxies#configuration) configuration, user macros can be used in the following fields:

_Address for active agents > Port_ (if the proxy belongs to a group) | no  
---|---  
Interface address and port (for passive proxy) | no  
Timeouts for item types | no  
  
#### Proxy groups

In a [proxy group](/documentation/current/en/manual/distributed_monitoring/proxies/ha#configuring-a-proxy-group) configuration, user macros can be used in the following fields:

Failover period | no  
---|---  
Minimum number of proxies | no  
  
#### Templates

In a [template](/documentation/current/en/manual/config/templates/template) configuration, user macros can be used in the following fields:

_Tags_[2](supported_by_location_user#footnotes)  
---  
| Tag names | yes  
Tag values | yes  
  
#### Triggers

In a [trigger](/documentation/current/en/manual/config/triggers/trigger) configuration, user macros can be used in the following fields:

Name | yes  
---|---  
Operational data | yes  
Expression (only in constants and function parameters; secret macros are not supported) | yes  
Tag for matching | yes  
Menu entry name | yes  
Menu entry URL[3](supported_by_location_user#footnotes) | yes  
Description | yes  
_Tags_[2](supported_by_location_user#footnotes)  
| Tag names | yes  
Tag values | yes  
  
#### Web scenario

In a [web scenario](/documentation/current/en/manual/web_monitoring) configuration, user macros can be used in the following fields:

Name | yes  
---|---  
Update interval | no  
Agent | yes  
HTTP proxy | yes  
Variables (values only) | yes  
Headers (names and values) | yes  
_Steps_  
| Name | yes  
URL[3](supported_by_location_user#footnotes) | yes  
Variables (values only) | yes  
Headers (names and values) | yes  
Timeout | no  
Required string | yes  
Required status codes | no  
_Authentication_  
| User | yes  
Password | yes  
SSL certificate | yes  
SSL key file | yes  
SSL key password | yes  
_Tags_[2](supported_by_location_user#footnotes)  
| Tag names | yes  
Tag values | yes  
  
#### Other locations

In addition to the locations listed here, user macros can be used in the following fields:

Global scripts (URL, script, SSH, Telnet, IPMI), including confirmation text | yes  
---|---  
Webhooks  
| JavaScript script | no  
JavaScript script parameter name | no  
JavaScript script parameter value | yes  
_Dashboards_  
| Column of data type _Text_ in _Top hosts_ dashboard widget | yes  
_Description_ parameter in _Item value_ and _Gauge_ dashboard widget | yes  
Primary/Secondary label _Text_ parameter in _Honeycomb_ dashboard widget | yes  
_URL_[3](supported_by_location_user#footnotes) parameter in _URL_ dashboard widget | yes  
_Users → Users → Media_  
| When active | no  
_Administration → General → GUI_  
| Working time | no  
_Administration → General → Timeouts_  
| Timeouts for item types | no  
_Administration → General → Connectors_  
| URL | yes  
Username | yes  
Password | yes  
Bearer token | yes  
Timeout | no  
HTTP proxy | yes  
SSL certificate file | yes  
SSL key file | yes  
SSL key password | yes  
_Alerts → Media types → Message templates_  
| Subject | yes  
Message | yes  
_Alerts → Media types → Script_  
| Script parameters | yes  
_Alerts → Media types → Media type_  
| _Username_ and _Password_ fields for the _Email_ media type (when _Authentication_ is set to "Username and password"; [secret macros](/documentation/current/en/manual/config/macros/user_macros#configuration) recommended) | yes  
  
For a complete list of all macros supported in Zabbix, see [supported macros](/documentation/current/en/manual/appendix/macros/supported_by_location).

##### Footnotes

**1** If multiple macros in a field or macros mixed with text are not supported for the location, a single macro has to fill the whole field.

**2** Macros used in tag names and values are resolved only during event generation process.

**3** URLs that contain a [secret macro](/documentation/current/en/manual/config/macros/user_macros#configuration) will not work, as the macro in them will be resolved as "******".