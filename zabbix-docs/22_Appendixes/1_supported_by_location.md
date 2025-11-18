---
title: Macros supported by location
source: https://www.zabbix.com/documentation/current/en/manual/appendix/macros/supported_by_location
downloaded: 2025-11-14 10:47:49
---

# 1 Macros supported by location

#### Overview

The macros supported by location table contains reference of all macros (built-in, expression, and user-definable) that are supported in the specific location.

If all macros from a related group are supported, then only the group name is given. Click on each macro name or group name to see full details of the macros.

The macro details list contains a detailed list of all **built-in** macros, grouped by application area. Note that to customize macro values (for example, shorten or extract specific substrings), you can use [macro functions](/documentation/current/en/manual/config/macros/macro_functions).

#### Macros supported by location

**Action**  
---  
| _Time period condition, Default operation step duration, Step duration_ | [User-definable](/documentation/current/en/manual/config/macros/user_macros) macros (global only) | A single macro has to fill the whole field; multiple macros/mix with text are not supported  
**Notifications and commands**  
| _Trigger-based_ | Action macros  
Date/time macros  
{ESC.HISTORY}  
Event macros, Cause/symptom event macros  
Event update macros: {EVENT.UPDATE.HISTORY}, {EVENT.UPDATE.STATUS}  
Expression macro: [{?EXPRESSION}](/documentation/current/en/manual/config/macros/expression_macros)  
{FUNCTION.VALUE}  
Host macros: {HOST.CONN}, {HOST.DESCRIPTION}, {HOST.DNS}, {HOST.HOST}, {HOST.ID}, {HOST.IP}, {HOST.NAME}, {HOST.PORT}  
Target host macros (commands only)  
Host inventory macros  
Item macros (except {ITEM.STATE}, {ITEM.STATE.ERROR})  
Proxy macros  
Trigger macros: {TRIGGER.DESCRIPTION}, {TRIGGER.EVENTS.*}, {TRIGGER.EXPRESSION}, {TRIGGER.EXPRESSION.EXPLAIN}, {TRIGGER.EXPRESSION.RECOVERY}, {TRIGGER.ID}, {TRIGGER.HOSTGROUP.NAME}, {TRIGGER.NAME}, {TRIGGER.NAME.ORIG}, {TRIGGER.NSEVERITY}, {TRIGGER.SEVERITY}, {TRIGGER.STATUS}, {TRIGGER.TEMPLATE.NAME}, {TRIGGER.URL}, {TRIGGER.URL.NAME}, {TRIGGER.VALUE}  
[User-definable](/documentation/current/en/manual/config/macros/user_macros) macros | See also: [Using macros in messages](/documentation/current/en/manual/config/notifications/action/operation/macros)  
_Problem update_ | Action macros  
Date/time macros  
{ESC.HISTORY}  
Event macros, Cause/symptom event macros, Recovery event macros  
Event update macros: all (except [{EVENT.UPDATE.NSEVERITY}, {EVENT.UPDATE.SEVERITY})  
Expression macro: [{?EXPRESSION}](/documentation/current/en/manual/config/macros/expression_macros)  
Function macros  
Host macros: {HOST.CONN}, {HOST.DESCRIPTION}, {HOST.DNS}, {HOST.HOST}, {HOST.ID}, {HOST.IP}, {HOST.NAME}, {HOST.PORT}  
Target host macros (commands only)  
Host inventory macros  
Item macros (except {ITEM.STATE}, {ITEM.STATE.ERROR})  
Proxy macros  
Trigger macros: {TRIGGER.DESCRIPTION}, {TRIGGER.EVENTS.*}, {TRIGGER.EXPRESSION}, {TRIGGER.EXPRESSION.EXPLAIN}, {TRIGGER.EXPRESSION.RECOVERY}, {TRIGGER.ID}, {TRIGGER.HOSTGROUP.NAME}, {TRIGGER.NAME}, {TRIGGER.NAME.ORIG}, {TRIGGER.NSEVERITY}, {TRIGGER.SEVERITY}, {TRIGGER.STATUS}, {TRIGGER.TEMPLATE.NAME}, {TRIGGER.URL}, {TRIGGER.URL.NAME}, {TRIGGER.VALUE}  
{USER.FULLNAME}  
[User-definable](/documentation/current/en/manual/config/macros/user_macros) macros |   
_Problem recovery_ | Recovery event macros  
{FUNCTION.RECOVERY.VALUE}  
{TRIGGER.EXPRESSION.RECOVERY.EXPLAIN} |   
_Discovery_ | Action macros  
Date/time macros  
Discovery macros  
Event macros: {EVENT.AGE}, {EVENT.DATE}, {EVENT.ID}, {EVENT.OBJECT}, {EVENT.SOURCE}, {EVENT.TIME}, {EVENT.TIMESTAMP}  
Target host macros (commands only)  
Proxy macros |   
_Autoregistration_ | Action macros  
Date/time macros  
Event macros: {EVENT.AGE}, {EVENT.DATE}, {EVENT.ID}, {EVENT.OBJECT}, {EVENT.SOURCE}, {EVENT.TIME}, {EVENT.TIMESTAMP}  
Host macros: {HOST.HOST}, {HOST.IP}, {HOST.PORT}, {HOST.METADATA}  
Target host macros (commands only)  
Proxy macros |   
_Service-based_ | Action macros  
Date/time macros  
{ESC.HISTORY}  
Event macros: all except {EVENT.ACK.STATUS}, {EVENT.OPDATA}  
Service macros  
[User-definable](/documentation/current/en/manual/config/macros/user_macros) macros |   
_Service recovery_ | Event macros (except {EVENT.ACK.STATUS}, {EVENT.OPDATA}), Recovery event macros |   
_Service update_ | Action macros  
Date/time macros  
{ESC.HISTORY}  
Event macros (except {EVENT.ACK.STATUS}, {EVENT.OPDATA})  
Event update macros: {EVENT.UPDATE.DATE}, {EVENT.UPDATE.MESSAGE}, {EVENT.UPDATE.NSEVERITY}, {EVENT.UPDATE.SEVERITY}, {EVENT.UPDATE.STATUS}, {EVENT.UPDATE.TIME}, {EVENT.UPDATE.TIMESTAMP}  
Service macros  
[User-definable](/documentation/current/en/manual/config/macros/user_macros) macros |   
**Internal notifications** | Action macros  
Date/time macros  
{ESC.HISTORY}  
Event macros (except {EVENT.NSEVERITY}, {EVENT.SEVERITY}), Recovery event macros  
Host macros: {HOST.CONN}, {HOST.DESCRIPTION}, {HOST.DNS}, {HOST.HOST}, {HOST.IP}, {HOST.NAME}, {HOST.PORT}  
Host inventory macros  
Item macros: {ITEM.DESCRIPTION}, {ITEM.DESCRIPTION.ORIG}, {ITEM.ID}, {ITEM.KEY}, {ITEM.KEY.ORIG}, {ITEM.NAME}, {ITEM.NAME.ORIG}, {ITEM.VALUETYPE}  
Proxy macros |   
| _Item-based_ | Item macros: {ITEM.STATE}, {ITEM.STATE.ERROR} |   
_LLD rule-based_ | Low-level discovery notification macros |   
_Trigger-based_ | Trigger macros: {TRIGGER.DESCRIPTION}, {TRIGGER.EXPRESSION}, {TRIGGER.EXPRESSION.RECOVERY}, {TRIGGER.HOSTGROUP.NAME}, {TRIGGER.ID}, {TRIGGER.NAME}, {TRIGGER.NAME.ORIG}, {TRIGGER.NSEVERITY}, {TRIGGER.SEVERITY}, {TRIGGER.STATE}, {TRIGGER.STATE.ERROR}, {TRIGGER.TEMPLATE.NAME}, {TRIGGER.URL}, {TRIGGER.URL.NAME}  
[User-definable](/documentation/current/en/manual/config/macros/user_macros) macros |   
**Alert script parameters** | Alert macros  
[User-definable](/documentation/current/en/manual/config/macros/user_macros) macros (global only) |   
**Connector**  
| _URL, Username, Password, Bearer token, HTTP proxy, SSL certificate, SSL key file, SSL key password_ field | [User-definable](/documentation/current/en/manual/config/macros/user_macros) macros (global only) |   
_Timeout_ field | [User-definable](/documentation/current/en/manual/config/macros/user_macros) macros (global only) | A single macro has to fill the whole field; multiple macros/mix with text are not supported.  
**Graph name** | Expression macro: [{?EXPRESSION}](/documentation/current/en/manual/config/macros/expression_macros) | Only a single **avg** , **last** , **max** , **min** function with seconds as parameter (time [suffixes](/documentation/current/en/manual/appendix/suffixes) can be used) is supported in this macro in this location.  
The {HOST.HOST<1-9>} macro can be used as host within the macro (see also indexed macros).  
Example usage:  
{?avg(/{HOST.HOST}/item.key,1h)}  
Unsupported usage:  
{?last(/host/item1)/last(/host/item2)}  
{?last(/host/item1)*10}  
{?count(/host/item1,5m)}  
**Host, host prototype**  
| _Interface IP/DNS_ | Host macros: {HOST.CONN}, {HOST.DNS}, {HOST.HOST}, {HOST.IP}, {HOST.NAME}  
[User-definable](/documentation/current/en/manual/config/macros/user_macros) macros **1** | **1** For IP address, a single macro has to fill the whole field; multiple macros/mix with text are not supported  
_Interface port_ | [User-definable](/documentation/current/en/manual/config/macros/user_macros) macros | A single macro has to fill the whole field; multiple macros/mix with text are not supported  
_SNMP community_ | [User-definable](/documentation/current/en/manual/config/macros/user_macros) macros |   
_SNMPv3 Context name, Security name, Authentication passphrase, Privacy passphrase_  
_IPMI username, password_  
**Item, item prototype, LLD rule**  
| _Name_ | [User-definable](/documentation/current/en/manual/config/macros/user_macros) macros | Not supported in LLD rule names.  
_Description_ | [User-definable](/documentation/current/en/manual/config/macros/user_macros) macros |   
_Key parameters_ | Host macros: {HOST.CONN}, {HOST.DNS}, {HOST.HOST}, {HOST.IP}, {HOST.NAME}, {HOST.PORT}  
[User-definable](/documentation/current/en/manual/config/macros/user_macros) macros | The supported {HOST.*} macros will resolve to the interface that is selected for the item. When used in items without interfaces they will resolve to either the Zabbix agent, SNMP, JMX or IPMI interface of the host in this order of priority or to 'UNKNOWN' if the host does not have any interface.  
_Update interval, Custom intervals, Timeout (available for[supported](/documentation/current/en/manual/web_interface/frontend_sections/administration/general#timeouts) item types), Store up to (for history/trends)_ fields | [User-definable](/documentation/current/en/manual/config/macros/user_macros) macros | A single macro has to fill the whole field; multiple macros/mix with text are not supported.  
_Delete lost resources, Disable lost resources_ fields | [User-definable](/documentation/current/en/manual/config/macros/user_macros) macros | These fields are supported for LLD rules only.  
  
A single macro has to fill the whole field; multiple macros/mix with text are not supported.  
_Preprocessing step parameters_ (including custom scripts),   
_custom error-handling parameters_ (_Set value to_ and _Set error to_ fields) | [User-definable](/documentation/current/en/manual/config/macros/user_macros) macros |   
_Filter regular expressions_ | Host macros: {HOST.CONN}, {HOST.DNS}, {HOST.HOST}, {HOST.IP}, {HOST.NAME}, {HOST.PORT}  
[User-definable](/documentation/current/en/manual/config/macros/user_macros) macros | These fields are supported for LLD rules only.  
_Override filter regular expressions_ | [User-definable](/documentation/current/en/manual/config/macros/user_macros) macros | These fields are supported for LLD rules only.  
Override operations: _Update interval_ , _History storage period_ , _Trend storage period_ (for item prototypes) | [User-definable](/documentation/current/en/manual/config/macros/user_macros) macros | These fields are supported for LLD rules only.  
  
A single macro has to fill the whole field; multiple macros/mix with text are not supported.  
**Item types**  
| **Browser** item  
 _parameter names and values_ | Host macros: {HOST.CONN}, {HOST.DNS}, {HOST.HOST}, {HOST.IP}, {HOST.NAME}, {HOST.PORT}  
Host inventory macros  
Item macros: {ITEM.ID}, {ITEM.KEY}, {ITEM.KEY.ORIG}  
[User-definable](/documentation/current/en/manual/config/macros/user_macros) macros |   
**Script** item  
 _parameter names and values_  
**Calculated/aggregate** item formula  
(_expression constants_ , _function parameters_ , _item key parameters_ , (aggregate item only) _filter conditions_ (host group name and tag name)) | [User-definable](/documentation/current/en/manual/config/macros/user_macros) macros |   
**Database monitor** item  
 _Username, Password, SQL query_ fields | [User-definable](/documentation/current/en/manual/config/macros/user_macros) macros |   
**HTTP agent** item  
 _URL, Query fields, Request body, Headers (names and values), SSL certificate file, SSL key file_ fields | Host macros: {HOST.CONN}, {HOST.DNS}, {HOST.HOST}, {HOST.IP}, {HOST.NAME}, {HOST.PORT}  
Item macros: {ITEM.ID}, {ITEM.KEY}, {ITEM.KEY.ORIG}  
[User-definable](/documentation/current/en/manual/config/macros/user_macros) macros | URLs that contain a [secret macro](/documentation/current/en/manual/config/macros/secret_macros) will not work, as the macro in them will be resolved as "******"  
**HTTP agent** item  
 _HTTP Proxy_ field | Item macros: {ITEM.ID}, {ITEM.KEY}, {ITEM.KEY.ORIG}  
[User-definable](/documentation/current/en/manual/config/macros/user_macros) macros |   
**HTTP agent** item  
 _Required status codes, HTTP authentication username/password, SSL key password_ fields | [User-definable](/documentation/current/en/manual/config/macros/user_macros) macros |   
**HTTP agent** item  
 _Allowed hosts_ field | Host macros: {HOST.CONN}, {HOST.DNS}, {HOST.HOST}, {HOST.IP}, {HOST.NAME}, {HOST.PORT}  
[User-definable](/documentation/current/en/manual/config/macros/user_macros) macros |   
**JMX agent** item  
 _Endpoint_ field | Host macros: {HOST.CONN}, {HOST.DNS}, {HOST.HOST}, {HOST.IP}, {HOST.PORT}  
[User-definable](/documentation/current/en/manual/config/macros/user_macros) macros |   
**Trapper** item  
 _Allowed hosts_ field  
**SNMP agent** item  
 _SNMP OID_ field | [User-definable](/documentation/current/en/manual/config/macros/user_macros) macros |   
**SSH and Telnet** item  
 _script_ | Host macros: {HOST.CONN}, {HOST.DNS}, {HOST.HOST}, {HOST.IP}, {HOST.NAME}, {HOST.PORT}  
[User-definable](/documentation/current/en/manual/config/macros/user_macros) macros |   
**SSH agent** item  
 _Username, Public key file, Private key file, Password_ fields | [User-definable](/documentation/current/en/manual/config/macros/user_macros) macros |   
**Telnet agent** item  
 _Username, Password_ fields | [User-definable](/documentation/current/en/manual/config/macros/user_macros) macros |   
**Map**  
| _URL, URL name_ | Host macros: {HOST.CONN}, {HOST.DESCRIPTION}, {HOST.DNS}, {HOST.HOST}, {HOST.ID}, {HOST.IP}, {HOST.NAME}, {HOST.PORT}  
{HOSTGROUP.ID}  
Host inventory macros  
Map macros  
{TRIGGER.ID} |   
_Element label_ | Expression macro: [{?EXPRESSION}](/documentation/current/en/manual/config/macros/expression_macros) **1**  
Host macros: {HOST.CONN}, {HOST.DESCRIPTION}, {HOST.DNS}, {HOST.HOST}, {HOST.ID}, {HOST.IP}, {HOST.NAME}, {HOST.PORT}  
{HOSTGROUP.ID}  
Host inventory macros  
Map macros  
Trigger macros: {TRIGGER.EVENTS.*}, {TRIGGER.ID}, {TRIGGER.PROBLEM.EVENTS.*}, {TRIGGERS.ACK}, {TRIGGERS.PROBLEM.ACK}, {TRIGGERS.PROBLEM.UNACK}, {TRIGGERS.UNACK} | **1** Only a single **avg** , **last** , **max** , **min** function with seconds as parameter (time [suffixes](/documentation/current/en/manual/appendix/suffixes) can be used) is supported in this macro in this location.  
The {HOST.HOST<1-9>} macro can be used as host within the macro.  
Example usage:  
{?avg(/{HOST.HOST}/item.key,1h)}  
Unsupported usage:  
{?last(/host/item1)/last(/host/item2)}  
{?last(/host/item1)*10}  
{?count(/host/item1,5m)}  
_Link label_ | Expression macro: [{?EXPRESSION}](/documentation/current/en/manual/config/macros/expression_macros) **1**  
_Shape label_ | Expression macro: [{?EXPRESSION}](/documentation/current/en/manual/config/macros/expression_macros) **1**  
_Text field in map shapes_ | {MAP.NAME} |   
**Network discovery**  
| _Update interval_ field | [User-definable](/documentation/current/en/manual/config/macros/user_macros) macros (global only) | A single macro has to fill the whole field; multiple macros/mix with text are not supported.  
_SNMP community, SNMP OID_ fields | [User-definable](/documentation/current/en/manual/config/macros/user_macros) macros (global only) |   
_SNMPv3 Context name, Security name, Authentication passphrase, Privacy passphrase_ fields |   
**Proxy**  
| _Address for active agents > Port_ (if the proxy belongs to a group)  
For passive proxy mode: interface _Address_ and _Port_ fields  
 _Timeouts for item types_ fields in override mode | [User-definable](/documentation/current/en/manual/config/macros/user_macros) macros (global only) | A single macro has to fill the whole field; multiple macros/mix with text are not supported.  
**Proxy group**  
| _Failover period, Minimum number of proxies_ fields | [User-definable](/documentation/current/en/manual/config/macros/user_macros) macros (global only) | A single macro has to fill the whole field; multiple macros/mix with text are not supported.  
**[Scripts](/documentation/current/en/manual/web_interface/frontend_sections/alerts/scripts)**  
| _Commands, confirmation text_   
(Type: script, manual **host action**) | Host macros: {HOST.CONN}, {HOST.DNS}, {HOST.HOST}, {HOST.ID} **1** , {HOST.IP}, {HOST.NAME}, {HOST.PORT}  
Host inventory macros **2**  
{MANUALINPUT}  
Username macros  
[User-definable](/documentation/current/en/manual/config/macros/user_macros) macros | **1** Confirmation text only  
**2** Supported for Zabbix server and Zabbix proxy  
  
_Commands_   
(Type: script, manual **event action**) | Date/time macros  
Event macros, Cause/symptom event macros, Recovery event macros (if recovery took place)  
Event update macros: {EVENT.UPDATE.HISTORY}, {EVENT.UPDATE.STATUS}  
{FUNCTION.VALUE}  
Host macros: {HOST.CONN}, {HOST.DESCRIPTION}, {HOST.DNS}, {HOST.HOST}, {HOST.ID}, {HOST.IP}, {HOST.NAME}, {HOST.PORT}  
Host inventory macros  
Item macros (except {ITEM.STATE}, {ITEM.STATE.ERROR})  
{MANUALINPUT}  
Proxy macros  
Trigger macros: {TRIGGER.DESCRIPTION}, {TRIGGER.EVENTS.*}, {TRIGGER.EXPRESSION}, {TRIGGER.EXPRESSION.EXPLAIN}, {TRIGGER.EXPRESSION.RECOVERY}, {TRIGGER.EXPRESSION.RECOVERY.EXPLAIN}, {TRIGGER.HOSTGROUP.NAME}, {TRIGGER.ID}, {TRIGGER.NAME}, {TRIGGER.NAME.ORIG}, {TRIGGER.NSEVERITY}, {TRIGGER.SEVERITY}, {TRIGGER.STATUS}, {TRIGGER.TEMPLATE.NAME}, {TRIGGER.URL}, {TRIGGER.URL.NAME}, {TRIGGER.VALUE}  
Username macros  
[User-definable](/documentation/current/en/manual/config/macros/user_macros) macros |   
_Confirmation text_   
(Type: script, manual **event action**) | Event macros: {EVENT.ID}, {EVENT.NAME}, {EVENT.NSEVERITY}, {EVENT.SEVERITY}, {EVENT.STATUS}, {EVENT.VALUE}  
Host macros: {HOST.CONN}, {HOST.DNS}, {HOST.HOST}, {HOST.ID}, {HOST.IP}, {HOST.NAME}, {HOST.PORT}  
Host inventory macros  
{MANUALINPUT}  
Username macros  
[User-definable](/documentation/current/en/manual/config/macros/user_macros) macros |   
_URL, confirmation text_   
(Type: URL, manual **host/event action**)  
**Tag name and value** | Host macros: {HOST.CONN}, {HOST.DNS}, {HOST.HOST}, {HOST.ID}, {HOST.IP}, {HOST.NAME}, {HOST.PORT}  
Host inventory macros  
Item macros: {ITEM.LASTVALUE*}, {ITEM.LOG.*}, {ITEM.VALUE*}  
Trigger macros: {TRIGGER.ID} (trigger tag value only)  
[User-definable](/documentation/current/en/manual/config/macros/user_macros) macros | Tag name and value macros are resolved during the event generation process only.  
**Trigger**  
| _Name_ | Host macros: {HOST.CONN}, {HOST.DNS}, {HOST.HOST}, {HOST.IP}, {HOST.NAME}, {HOST.PORT}  
Item macros: {ITEM.LASTVALUE*}, {ITEM.LOG.*}, {ITEM.VALUE*}  
Positional macros/references: `$1...$9`  
[User-definable](/documentation/current/en/manual/config/macros/user_macros) macros |   
_Event name_ | Date/time macros: {TIME}, {TIMESTAMP}  
Expression macro: [{?EXPRESSION}](/documentation/current/en/manual/config/macros/expression_macros)  
Function macros  
Host macros: {HOST.CONN}, {HOST.DNS}, {HOST.HOST}, {HOST.IP}, {HOST.NAME}, {HOST.PORT}  
Item macros: {ITEM.LASTVALUE*}, {ITEM.LOG.*}, {ITEM.VALUE*}  
Trigger macros: {TRIGGER.EXPRESSION.EXPLAIN} |   
_Operational data_ | Host macros: {HOST.CONN}, {HOST.DNS}, {HOST.HOST}, {HOST.IP}, {HOST.NAME}, {HOST.PORT}  
Item macros: {ITEM.LASTVALUE*}, {ITEM.LOG.*}, {ITEM.VALUE*}  
[User-definable](/documentation/current/en/manual/config/macros/user_macros) macros |   
_Expression_ | {TRIGGER.VALUE}  
[User-definable](/documentation/current/en/manual/config/macros/user_macros) macros **1** | **1** Only in constants and function parameters; secret macros are not supported  
_Tag for matching, Menu entry name, Menu entry URL_ fields | [User-definable](/documentation/current/en/manual/config/macros/user_macros) macros | URLs that contain a [secret macro](/documentation/current/en/manual/config/macros/secret_macros) will not work, as the macro in them will be resolved as "******".  
_Description_ | Host macros: {HOST.CONN}, {HOST.DNS}, {HOST.HOST}, {HOST.IP}, {HOST.NAME}, {HOST.PORT}  
Item macros: {ITEM.LASTVALUE*}, {ITEM.LOG.*}, {ITEM.VALUE*}  
[User-definable](/documentation/current/en/manual/config/macros/user_macros) macros |   
_URL_ | {EVENT.ID}  
Host macros: {HOST.CONN}, {HOST.DNS}, {HOST.HOST}, {HOST.ID}, {HOST.IP}, {HOST.NAME}, {HOST.PORT}  
Item macros: {ITEM.LASTVALUE*}, {ITEM.LOG.*}, {ITEM.VALUE*}  
{TRIGGER.ID} |   
**User parameter commands** | Positional macros/references: `$1...$9` |   
**Web scenario**  
| _Name, Agent, HTTP proxy_ fields | [User-definable](/documentation/current/en/manual/config/macros/user_macros) macros |   
| _Update interval_ field | [User-definable](/documentation/current/en/manual/config/macros/user_macros) macros | A single macro has to fill the whole field; multiple macros/mix with text are not supported.  
_Variables, Headers, SSL certificate, SSL key file_ fields | Host macros: {HOST.CONN}, {HOST.DNS}, {HOST.HOST}, {HOST.IP}, {HOST.NAME}, {HOST.PORT}  
[User-definable](/documentation/current/en/manual/config/macros/user_macros) macros |   
_User, Password, SSL key password_ fields | [User-definable](/documentation/current/en/manual/config/macros/user_macros) macros |   
Web scenario step  
 _Name, Variables (values only)_ fields | [User-definable](/documentation/current/en/manual/config/macros/user_macros) macros |   
Web scenario step  
 _Timeout, Required status codes_ fields | [User-definable](/documentation/current/en/manual/config/macros/user_macros) macros | A single macro has to fill the whole field; multiple macros/mix with text are not supported.  
Web scenario step  
 _URL, Headers (names and values), Required string_ fields | Host macros: {HOST.CONN}, {HOST.DNS}, {HOST.HOST}, {HOST.IP}, {HOST.NAME}, {HOST.PORT}  
[User-definable](/documentation/current/en/manual/config/macros/user_macros) macros |   
Web scenario step  
 _Post_ field | Host macros: {HOST.CONN}, {HOST.DNS}, {HOST.HOST}, {HOST.IP}, {HOST.NAME}, {HOST.PORT} |   
**Webhook media type**  
| _Parameter values_ | Alert macros  
All macros supported in trigger-based problem notifications (see above) | A single macro has to fill the whole field; multiple macros/mix with text are not supported.  
_JavaScript_ script, _JavaScript_ script parameter name | [User-definable](/documentation/current/en/manual/config/macros/user_macros) macros (global only) |   
_Menu entry name, Menu entry URL_ | {EVENT.TAGS.<tag name>} |   
**Widgets**  
| **Gauge** widget  
 _Description_ field | Host macros: {HOST.CONN}, {HOST.DESCRIPTION}, {HOST.DNS}, {HOST.HOST}, {HOST.ID}, {HOST.IP}, {HOST.NAME}, {HOST.PORT}  
Host inventory macros  
Item macros (except {ITEM.STATE.ERROR})  
[User-definable](/documentation/current/en/manual/config/macros/user_macros) macros (global only) |   
**Honeycomb** widget  
 _Primary/secondary label_ field |   
**Item value** widget  
 _Description_ field |   
**Top hosts** widget  
 _Text data_ column | Host macros: {HOST.CONN}, {HOST.DESCRIPTION}, {HOST.DNS}, {HOST.HOST}, {HOST.ID}, {HOST.IP}, {HOST.NAME}, {HOST.PORT}  
Host inventory macros  
[User-definable](/documentation/current/en/manual/config/macros/user_macros) macros (global only) |   
**URL** (Dynamic) widget  
 _URL_ field | Host macros: {HOST.CONN}, {HOST.DNS}, {HOST.HOST}, {HOST.ID}, {HOST.IP}, {HOST.NAME}, {HOST.PORT}  
[User-definable](/documentation/current/en/manual/config/macros/user_macros) macros |   
**Other locations**  
| _Working time_ field | [User-definable](/documentation/current/en/manual/config/macros/user_macros) macros (global only) | A single macro has to fill the whole field; multiple macros/mix with text are not supported.  
_Timeouts for item types_ field (global setting)  
User media  
 _When active_ field  
Email media type  
 _Username, Password_ fields | [User-definable](/documentation/current/en/manual/config/macros/user_macros) macros (global only) | [Secret macros](/documentation/current/en/manual/config/macros/secret_macros) are recommended.  
Scheduled reports  
 _Subject, Message_ fields | Date/time macros: {TIME}, {TIMESTAMP} |   
  
#### Macro details

This list contains details for each built-in macro grouped by application area:

  * Action macros
  * Alert macros
  * Date/time macros
  * Discovery macros
  * Event macros
    * Event update macros
    * Cause/symptom event macros
    * Recovery event macros
  * Escalation macros
  * Function macros
  * Host macros
    * Target host macros
  * Host group macros
  * Host inventory macros
  * Item macros
  * Low-level discovery notification macros
  * Map macros
  * Proxy macros
  * Script macros
  * Service macros
  * Trigger macros
  * Username macros

#### Action macros

##### {ACTION.ID}

The numeric ID of the triggered action.  

##### {ACTION.NAME}

The name of the triggered action.  

#### Alert macros

##### {ALERT.MESSAGE}

The _Default message_ value from action configuration.  

##### {ALERT.SENDTO}

The _Send to_ value from user media configuration.  

##### {ALERT.SUBJECT}

The _Default subject_ value from action configuration.  

#### Date and time macros

##### {DATE}

The current date in `yyyy.mm.dd.` format.  

##### {TIME}

The current time in `hh:mm:ss` format.  

##### {TIMESTAMP}

The current time in UNIX timestamp format.  

#### Discovery macros

##### {DISCOVERY.DEVICE.IPADDRESS}

The IP address of the discovered device.  
Available always, does not depend on host being added.

##### {DISCOVERY.DEVICE.DNS}

The DNS name of the discovered device.  
Available always, does not depend on host being added.

##### {DISCOVERY.DEVICE.STATUS}

The status of the discovered device (UP/DOWN).  

##### {DISCOVERY.DEVICE.UPTIME}

The time since the last change of discovery status for a particular device.  
For example: 1h 29m 01s.  
For devices with status DOWN, this is the period of their downtime.

##### {DISCOVERY.RULE.NAME}

The name of the discovery rule that discovered the presence or absence of device/service.

##### {DISCOVERY.SERVICE.NAME}

The name of the discovered service.  
For example: HTTP.

##### {DISCOVERY.SERVICE.PORT}

The port of the discovered service.  
For example: 80.

##### {DISCOVERY.SERVICE.STATUS}

The status of the discovered service (UP/DOWN).  

##### {DISCOVERY.SERVICE.UPTIME}

The time since the last change of discovery status for a particular service.  
For example: 1h 29m 01s.  
For services with status DOWN, this is the period of their downtime.

#### Escalation macros

##### {ESC.HISTORY}

The log of previously sent notifications, their escalation step and status (_sent_ , _in progress_ or _failed_).  

#### Event macros

##### {EVENT.ACK.STATUS}

The acknowledgment status of the event (Yes/No).  

##### {EVENT.AGE}

The age of the event that triggered an action, with precision down to a second.  
Useful in escalated messages. For example: 9m 13s.

##### {EVENT.DATE}

The date of the event that triggered an action.   
For example: 2025.04.14.

##### {EVENT.DURATION}

The duration of the event (time difference between problem and recovery events), with precision down to a second.  
Useful in problem recovery messages.

##### {EVENT.ID}

The numeric ID of the event that triggered an action.  

##### {EVENT.NAME}

The name of the event that triggered an action.  

##### {EVENT.NSEVERITY}

The numeric value of the event severity.  
Possible values: _0_ \- Not classified, _1_ \- Information, _2_ \- Warning, _3_ \- Average, _4_ \- High, _5_ \- Disaster.

##### {EVENT.OBJECT}

The numeric value of the event object.  
Possible values: _0_ \- Trigger, _1_ \- Discovered host, _2_ \- Discovered service, _3_ \- Autoregistration, _4_ \- Item, _5_ \- Low-level discovery rule.

##### {EVENT.OPDATA}

The operational data of the underlying trigger of the problem.  

##### {EVENT.SEVERITY}

The name of the event severity.  

##### {EVENT.SOURCE}

The numeric value of the event source.  
Possible values: _0_ \- Trigger, _1_ \- Discovery, _2_ \- Autoregistration, _3_ \- Internal, _4_ \- Service.

##### {EVENT.STATUS}

The verbal value of the event that triggered an action.  

##### {EVENT.TAGS}

A comma-separated list of event tags.  
Expanded to an empty string if no tags exist.  

##### {EVENT.TAGSJSON}

A JSON array containing event tag [objects](/documentation/current/en/manual/api/reference/event/object#event-tag).  
Expanded to an empty array if no tags exist.  

##### {EVENT.TAGS.<tag name>}

The event tag value referenced by the tag name.  
A tag name containing non-alphanumeric characters (including non-English multibyte-UTF characters) must be double quoted. Quotes and backslashes inside a quoted tag name must be escaped with a backslash.

##### {EVENT.TIME}

The time of the event that triggered an action.  
For example: 12:57:53.

##### {EVENT.TIMESTAMP}

The UNIX timestamp of the event that triggered an action.  

##### {EVENT.VALUE}

The numeric value of the event that triggered an action.  
Possible values: _1_ \- problem, _0_ \- recovering.  

#### Cause/symptom event macros

##### {EVENT.CAUSE.ACK.STATUS}

The acknowledgment status of the cause event (Yes/No).  
Used in the context of a symptom event.

##### {EVENT.CAUSE.AGE}

The age of the cause event, with precision down to a second.  
Useful in escalated messages.  
Used in the context of a symptom event.

##### {EVENT.CAUSE.DATE}

The date of the cause event.  
Used in the context of a symptom event.

##### {EVENT.CAUSE.DURATION}

The duration of the cause event (time difference between problem and recovery events), with precision down to a second.  
Useful in problem recovery messages.  
Used in the context of a symptom event.

##### {EVENT.CAUSE.ID}

The numeric ID of the cause event.  
Used in the context of a symptom event.

##### {EVENT.CAUSE.NAME}

The name of the cause event.  
Used in the context of a symptom event.

##### {EVENT.CAUSE.NSEVERITY}

The numeric value of the cause event severity.  
Possible values: _0_ \- Not classified, _1_ \- Information, _2_ \- Warning, _3_ \- Average, _4_ \- High, _5_ \- Disaster.  
Used in the context of a symptom event.

##### {EVENT.CAUSE.OBJECT}

The numeric value of the cause event object.  
Possible values: _0_ \- Trigger, _1_ \- Discovered host, _2_ \- Discovered service, _3_ \- Autoregistration, _4_ \- Item, _5_ \- Low-level discovery rule.  
Used in the context of a symptom event.

##### {EVENT.CAUSE.OPDATA}

The operational data of the underlying trigger of the cause problem.  
Used in the context of a symptom event.

##### {EVENT.CAUSE.SEVERITY}

The name of the cause event severity.  
Possible values: _Not classified_ , _Information_ , _Warning_ , _Average_ , _High_ , _Disaster_.  
Used in the context of a symptom event.

##### {EVENT.CAUSE.SOURCE}

The numeric value of the cause event source.  
Possible values: _0_ \- Trigger, _1_ \- Discovery, _2_ \- Autoregistration, _3_ \- Internal.  
Used in the context of a symptom event.

##### {EVENT.CAUSE.STATUS}

The verbal value of the cause event.  
Used in the context of a symptom event.

##### {EVENT.CAUSE.TAGS}

A comma-separated list of cause event tags.  
Expanded to an empty string if no tags exist.  
Used in the context of a symptom event.

##### {EVENT.CAUSE.TAGSJSON}

A JSON array containing cause event tag [objects](/documentation/current/en/manual/api/reference/event/object#event-tag).  
Expanded to an empty array if no tags exist.  
Used in the context of a symptom event.

##### {EVENT.CAUSE.TAGS.<tag name>}

The cause event tag value referenced by the tag name.  
A tag name containing non-alphanumeric characters (including non-English multibyte-UTF characters) must be double quoted. Quotes and backslashes inside a quoted tag name must be escaped with a backslash.  
Used in the context of a symptom event.

##### {EVENT.CAUSE.TIME}

The time of the cause event.  
Used in the context of a symptom event.

##### {EVENT.CAUSE.TIMESTAMP}

The UNIX timestamp of the cause event.  
Used in the context of a symptom event.

##### {EVENT.CAUSE.UPDATE.HISTORY}

The log of cause problem updates (acknowledgments, etc).  
Used in the context of a symptom event.

##### {EVENT.CAUSE.VALUE}

The numeric value of the cause event  
Possible values: _1_ \- Problem, _0_ \- Recovering.  
Used in the context of a symptom event.

##### {EVENT.SYMPTOMS}

The list of symptom events. Includes the following details: host name, event name, severity, age, service tags and values.  
This macro is used in the context of the cause event and returns information about symptom events.

#### Recovery event macros

##### {EVENT.RECOVERY.DATE}

The date of the recovery event.  

##### {EVENT.RECOVERY.ID}

The numeric ID of the recovery event.  

##### {EVENT.RECOVERY.NAME}

The name of the recovery event.  

##### {EVENT.RECOVERY.STATUS}

The verbal value of the recovery event.  

##### {EVENT.RECOVERY.TAGS}

A comma-separated list of recovery event tags. Expanded to an empty string if no tags exist.  

##### {EVENT.RECOVERY.TAGSJSON}

A JSON array containing recovery event tag [objects](/documentation/current/en/manual/api/reference/event/object#event-tag). Expanded to an empty arrahy if no tags exist.  

##### {EVENT.RECOVERY.TIME}

The time of the recovery event.  

##### {EVENT.RECOVERY.TIMESTAMP}

The UNIX timestamp of the recovery event.  

##### {EVENT.RECOVERY.VALUE}

The numeric value of the recovery event.  

#### Event update macros

##### {EVENT.UPDATE.ACTION}

Human-readable name of the action(s) performed during [problem update](/documentation/current/en/manual/acknowledgment#updating-problems).  
Resolves to the following values: _acknowledged_ , _unacknowledged_ , _commented_ , _changed severity from (original severity) to (updated severity)_ and _closed_ (depending on how many actions are performed in one update).

##### {EVENT.UPDATE.ACTIONJSON}

A JSON array containing details of the action(s) performed during [problem update](/documentation/current/en/manual/acknowledgment#updating-problems).  
Possible JSON property values:  
\- true (for `acknowledge`, `unacknowledge`, `close`, `unsuppress`, `cause`, and `symptom` properties);  
\- <message string> (for `message` property);  
\- timestamp (for `suppress_until` and `timestamp` properties) or 0 (for `suppress_until` property if suppressed indefinitely);  
\- 0, 1, 2, 3, 4, 5 (for `old` and `new` severity properties).  
  
For example: `{"acknowledge":true,"message":"Monthly maintenance.","severity":{"old":2,"new":1},"suppress_until":1730851199,"timestamp":1730822048}`

##### {EVENT.UPDATE.DATE}

The date of the event [update](/documentation/current/en/manual/config/notifications/action/update_operations) (acknowledgment, etc)  
Deprecated name: {ACK.DATE}

##### {EVENT.UPDATE.HISTORY}

The log of problem updates (acknowledgments, etc).  
Deprecated name: {EVENT.ACK.HISTORY}

##### {EVENT.UPDATE.MESSAGE}

The problem update message.  
Deprecated name: {ACK.MESSAGE}

##### {EVENT.UPDATE.NSEVERITY}

The numeric value of the new event severity set during problem update operation.  

##### {EVENT.UPDATE.SEVERITY}

The name of the new event severity set during problem update operation.  

##### {EVENT.UPDATE.STATUS}

The Numeric value of the problem update status.  
Possible values: _0_ \- Webhook was called because of problem/recovery event, _1_ \- Update operation.  

##### {EVENT.UPDATE.TIME}

The time of the event [update](/documentation/current/en/manual/config/notifications/action/update_operations) (acknowledgment, etc)  
Deprecated name: {ACK.TIME}

##### {EVENT.UPDATE.TIMESTAMP}

The UNIX timestamp of the event [update](/documentation/current/en/manual/config/notifications/action/update_operations) (acknowledgment, etc)  

#### Function macros

##### {FUNCTION.VALUE}

The value of the Nth item-based function in the trigger expression at the time of the event.  
Only functions with `/host/key` as the first parameter are counted.  
  
This macro may be used with a numeric index e.g. {FUNCTION.VALUE[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. function in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {FUNCTION.RECOVERY.VALUE}

The value of the Nth item-based function in the recovery expression at the time of the event.*  
Only functions with `/host/key`s as the first parameter are counted.  
  
This macro may be used with a numeric index e.g. {FUNCTION.RECOVERY.VALUE[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. function in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

#### Host macros

##### {HOST.CONN}

The host IP address or DNS name, depending on host settings.  
In global scripts, interface IP/DNS fields and web scenarios the macro will resolve to the main agent interface. If an agent interface is not defined, the main SNMP interface will be used. If an SNMP interface is also not defined, the main JMX interface will be used. If a JMX interface is not defined either, the main IPMI interface will be used. If the host does not have any interface, the macro resolves to 'UNKNOWN'.  
  
This macro may be used with a numeric index as {HOST.CONN[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {HOST.DESCRIPTION}

The host description.  
  
This macro may be used with a numeric index as {HOST.DESCRIPTION[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {HOST.DNS}

The host DNS name.  
In global scripts, interface IP/DNS fields and web scenarios the macro will resolve to the main agent interface. If an agent interface is not defined, the main SNMP interface will be used. If an SNMP interface is also not defined, the main JMX interface will be used. If a JMX interface is not defined either, the main IPMI interface will be used. If the host does not have any interface, the macro resolves to 'UNKNOWN'.  
  
This macro may be used with a numeric index as {HOST.DNS[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {HOST.HOST}

The technical host name.  
[Macro functions](/documentation/current/en/manual/config/macros/macro_functions) are not supported for this macro if it is used as a placeholder in the first parameter of a [history function](/documentation/current/en/manual/appendix/functions/history), for example, `last(/{HOST.HOST}/{ITEM.KEY})`.  
`{HOSTNAME<1-9>}` is deprecated.  
  
This macro may be used with a numeric index as {HOST.HOST[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {HOST.ID}

The host ID.  
  
This macro may be used with a numeric index as {HOST.ID[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {HOST.IP}

The host IP address.  
In global scripts, interface IP/DNS fields and web scenarios the macro will resolve to the main agent interface. If an agent interface is not defined, the main SNMP interface will be used. If an SNMP interface is also not defined, the main JMX interface will be used. If a JMX interface is not defined either, the main IPMI interface will be used. If the host does not have any interface, the macro resolves to 'UNKNOWN'.  
`{IPADDRESS<1-9>}` is deprecated.  
  
This macro may be used with a numeric index as {HOST.IP[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {HOST.METADATA}

The host metadata.  
  
Used only for active agent autoregistration.

##### {HOST.NAME}

The visible host name.  
  
This macro may be used with a numeric index as {HOST.NAME[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {HOST.PORT}

The host (agent) port.  
In global scripts, interface IP/DNS fields and web scenarios the macro will resolve to the main agent interface. If an agent interface is not defined, the main SNMP interface will be used. If an SNMP interface is also not defined, the main JMX interface will be used. If a JMX interface is not defined either, the main IPMI interface will be used. If the host does not have any interface, the macro resolves to 'UNKNOWN'.  
  
This macro may be used with a numeric index as {HOST.PORT[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

#### Target host macros

##### {HOST.TARGET.CONN}

The IP address or DNS name of the target host.

##### {HOST.TARGET.DNS}

The DNS name of the target host.

##### {HOST.TARGET.HOST}

The technical name of the target host.

##### {HOST.TARGET.IP}

The IP address of the target host.

##### {HOST.TARGET.NAME}

The visible name of the target host.

### Host group macros

##### {HOSTGROUP.ID}

The host group ID.  
  

#### Host inventory macros

##### {INVENTORY.ALIAS}

The _Alias_ field in host inventory.  
  
This macro may be used with a numeric index e.g. {INVENTORY.ALIAS[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.ASSET.TAG}

The _Asset tag_ field in host inventory.  
  
This macro may be used with a numeric index e.g. {INVENTORY.ASSET.TAG[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.CHASSIS}

The _Chassis_ field in host inventory.  
  
This macro may be used with a numeric index e.g. {INVENTORY.CHASSIS[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.CONTACT}

The _Contact_ field in host inventory.  
`{PROFILE.CONTACT<1-9>}` is deprecated.  
  
This macro may be used with a numeric index e.g. {INVENTORY.CONTACT[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.CONTRACT.NUMBER}

The _Contract number_ field in host inventory.  
  
This macro may be used with a numeric index e.g. {INVENTORY.CONTRACT.NUMBER[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.DEPLOYMENT.STATUS}

The _Deployment status_ field in host inventory.  
  
This macro may be used with a numeric index e.g. {INVENTORY.DEPLOYMENT.STATUS[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.HARDWARE}

The _Hardware_ field in host inventory.  
`{PROFILE.HARDWARE<1-9>}` is deprecated.  
  
This macro may be used with a numeric index e.g. {INVENTORY.HARDWARE[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.HARDWARE.FULL}

The _Hardware (Full details)_ field in host inventory.  
  
This macro may be used with a numeric index e.g. {INVENTORY.HARDWARE.FULL[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.HOST.NETMASK}

The _Host subnet mask_ field in host inventory.  
  
This macro may be used with a numeric index e.g. {INVENTORY.HOST.NETMASK[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.HOST.NETWORKS}

The _Host networks_ field in host inventory.  
  
This macro may be used with a numeric index e.g. {INVENTORY.HOST.NETWORKS[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.HOST.ROUTER}

The _Host router_ field in host inventory.  
  
This macro may be used with a numeric index e.g. {INVENTORY.HOST.ROUTER[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.HW.ARCH}

The _Hardware architecture_ field in host inventory.  
  
This macro may be used with a numeric index e.g. {INVENTORY.HW.ARCH[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.HW.DATE.DECOMM}

The _Date hardware decommissioned_ field in host inventory.  
  
This macro may be used with a numeric index e.g. {INVENTORY.HW.DATE.DECOMM[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.HW.DATE.EXPIRY}

The _Date hardware maintenance expires_ field in host inventory.  
  
This macro may be used with a numeric index e.g. {INVENTORY.HW.DATE.EXPIRY[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.HW.DATE.INSTALL}

The _Date hardware installed_ field in host inventory.  
  
This macro may be used with a numeric index e.g. {INVENTORY.HW.DATE.INSTALL[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.HW.DATE.PURCHASE}

The _Date hardware purchased_ field in host inventory.  
  
This macro may be used with a numeric index e.g. {INVENTORY.HW.DATE.PURCHASE[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.INSTALLER.NAME}

The _Installer name_ field in host inventory.  
  
This macro may be used with a numeric index e.g. {INVENTORY.INSTALLER.NAME[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.LOCATION}

The _Location_ field in host inventory.  
`{PROFILE.LOCATION<1-9>}` is deprecated.  
  
This macro may be used with a numeric index e.g. {INVENTORY.LOCATION[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.LOCATION.LAT}

The _Location latitude_ field in host inventory.  
  
This macro may be used with a numeric index e.g. {INVENTORY.LOCATION.LAT[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.LOCATION.LON}

The _Location longitude_ field in host inventory.  
  
This macro may be used with a numeric index e.g. {INVENTORY.LOCATION.LON[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.MACADDRESS.A}

The _MAC address A_ field in host inventory.  
`{PROFILE.MACADDRESS<1-9>}` is deprecated.  
  
This macro may be used with a numeric index e.g. {INVENTORY.MACADDRESS.A[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.MACADDRESS.B}

The _MAC address B_ field in host inventory.  
  
This macro may be used with a numeric index e.g. {INVENTORY.MACADDRESS.B[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.MODEL}

The _Model_ field in host inventory.  
  
This macro may be used with a numeric index e.g. {INVENTORY.MODEL[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.NAME}

The _Name_ field in host inventory.  
`{PROFILE.NAME<1-9>}` is deprecated.  
  
This macro may be used with a numeric index e.g. {INVENTORY.NAME[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.NOTES}

The _Notes_ field in host inventory.  
`{PROFILE.NOTES<1-9>}` is deprecated.  
  
This macro may be used with a numeric index e.g. {INVENTORY.NOTES[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.OOB.IP}

The _OOB IP address_ field in host inventory.  
  
This macro may be used with a numeric index e.g. {INVENTORY.OOB.IP[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.OOB.NETMASK}

The _OOB subnet mask_ field in host inventory.  
  
This macro may be used with a numeric index e.g. {INVENTORY.OOB.NETMASK[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.OOB.ROUTER}

The _OOB router_ field in host inventory.  
  
This macro may be used with a numeric index e.g. {INVENTORY.OOB.ROUTER[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.OS}

The _OS_ field in host inventory.  
`{PROFILE.OS<1-9>}` is deprecated.  
  
This macro may be used with a numeric index e.g. {INVENTORY.OS[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.OS.FULL}

The _OS (Full details)_ field in host inventory.  
  
This macro may be used with a numeric index e.g. {INVENTORY.OS.FULL[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.OS.SHORT}

The _OS (Short)_ field in host inventory.  
  
This macro may be used with a numeric index e.g. {INVENTORY.OS.SHORT[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.POC.PRIMARY.CELL}

The _Primary POC cell_ field in host inventory.  
  
This macro may be used with a numeric index e.g. {INVENTORY.POC.PRIMARY.CELL[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.POC.PRIMARY.EMAIL}

The _Primary POC email_ field in host inventory.  
  
This macro may be used with a numeric index e.g. {INVENTORY.POC.PRIMARY.EMAIL[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.POC.PRIMARY.NAME}

The _Primary POC name_ field in host inventory.  
  
This macro may be used with a numeric index e.g. {INVENTORY.POC.PRIMARY.NAME[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.POC.PRIMARY.NOTES}

The _Primary POC notes_ field in host inventory.  
  
This macro may be used with a numeric index e.g. {INVENTORY.POC.PRIMARY.NOTES[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.POC.PRIMARY.PHONE.A}

The _Primary POC phone A_ field in host inventory.  
  
This macro may be used with a numeric index e.g. {INVENTORY.POC.PRIMARY.PHONE.A[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.POC.PRIMARY.PHONE.B}

The _Primary POC phone B_ field in host inventory.  
  
This macro may be used with a numeric index e.g. {INVENTORY.POC.PRIMARY.PHONE.B[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.POC.PRIMARY.SCREEN}

The _Primary POC screen name_ field in host inventory.  
  
This macro may be used with a numeric index e.g. {INVENTORY.POC.PRIMARY.SCREEN[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.POC.SECONDARY.CELL}

The _Secondary POC cell_ field in host inventory.  
  
This macro may be used with a numeric index e.g. {INVENTORY.POC.SECONDARY.CELL[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.POC.SECONDARY.EMAIL}

The _Secondary POC email_ field in host inventory.  
  
This macro may be used with a numeric index e.g. {INVENTORY.POC.SECONDARY.EMAIL[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.POC.SECONDARY.NAME}

The _Secondary POC name_ field in host inventory.  
  
This macro may be used with a numeric index e.g. {INVENTORY.POC.SECONDARY.NAME[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.POC.SECONDARY.NOTES}

The _Secondary POC notes_ field in host inventory.  
  
This macro may be used with a numeric index e.g. {INVENTORY.POC.SECONDARY.NOTES[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.POC.SECONDARY.PHONE.A}

The _Secondary POC phone A_ field in host inventory.  
  
This macro may be used with a numeric index e.g. {INVENTORY.POC.SECONDARY.PHONE.A[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.POC.SECONDARY.PHONE.B}

The _Secondary POC phone B_ field in host inventory.  
  
This macro may be used with a numeric index e.g. {INVENTORY.POC.SECONDARY.PHONE.B[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.POC.SECONDARY.SCREEN}

The _Secondary POC screen name_ field in host inventory.  
  
This macro may be used with a numeric index e.g. {INVENTORY.POC.SECONDARY.SCREEN[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.SERIALNO.A}

The _Serial number A_ field in host inventory.  
`{PROFILE.SERIALNO<1-9>}` is deprecated.  
  
This macro may be used with a numeric index e.g. {INVENTORY.SERIALNO.A[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.SERIALNO.B}

The _Serial number B_ field in host inventory.  
  
This macro may be used with a numeric index e.g. {INVENTORY.SERIALNO.B[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.SITE.ADDRESS.A}

The _Site address A_ field in host inventory.  
  
This macro may be used with a numeric index e.g. {INVENTORY.SITE.ADDRESS.A[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.SITE.ADDRESS.B}

The _Site address B_ field in host inventory.  
  
This macro may be used with a numeric index e.g. {INVENTORY.SITE.ADDRESS.B[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.SITE.ADDRESS.C}

The _Site address C_ field in host inventory.  
  
This macro may be used with a numeric index e.g. {INVENTORY.SITE.ADDRESS.C[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.SITE.CITY}

The _Site city_ field in host inventory.  
  
This macro may be used with a numeric index e.g. {INVENTORY.SITE.CITY[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.SITE.COUNTRY}

The _Site country_ field in host inventory.  
  
This macro may be used with a numeric index e.g. {INVENTORY.SITE.COUNTRY[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.SITE.NOTES}

The _Site notes_ field in host inventory.  
  
This macro may be used with a numeric index e.g. {INVENTORY.SITE.NOTES[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.SITE.RACK}

The _Site rack location_ field in host inventory.  
  
This macro may be used with a numeric index e.g. {INVENTORY.SITE.RACK[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.SITE.STATE}

The _Site state/province_ field in host inventory.  
  
This macro may be used with a numeric index e.g. {INVENTORY.SITE.STATE[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.SITE.ZIP}

The _Site ZIP/postal_ field in host inventory.  
  
This macro may be used with a numeric index e.g. {INVENTORY.SITE.ZIP[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.SOFTWARE}

The _Software_ field in host inventory.  
`{PROFILE.SOFTWARE<1-9>}` is deprecated.  
  
This macro may be used with a numeric index e.g. {INVENTORY.SOFTWARE[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.SOFTWARE.APP.A}

The _Software application A_ field in host inventory.  
  
This macro may be used with a numeric index e.g. {INVENTORY.SOFTWARE.APP.A[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.SOFTWARE.APP.B}

The _Software application B_ field in host inventory.  
  
This macro may be used with a numeric index e.g. {INVENTORY.SOFTWARE.APP.B[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.SOFTWARE.APP.C}

The _Software application C_ field in host inventory.  
  
This macro may be used with a numeric index e.g. {INVENTORY.SOFTWARE.APP.C[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.SOFTWARE.APP.D}

The _Software application D_ field in host inventory.  
  
This macro may be used with a numeric index e.g. {INVENTORY.SOFTWARE.APP.D[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.SOFTWARE.APP.E}

The _Software application E_ field in host inventory.  
  
This macro may be used with a numeric index e.g. {INVENTORY.SOFTWARE.APP.E[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.SOFTWARE.FULL}

The _Software (Full details)_ field in host inventory.  
  
This macro may be used with a numeric index e.g. {INVENTORY.SOFTWARE.FULL[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.TAG}

The _Tag_ field in host inventory.  
`{PROFILE.TAG<1-9>}` is deprecated.  
  
This macro may be used with a numeric index e.g. {INVENTORY.TAG[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.TYPE}

The _Type_ field in host inventory.  
`{PROFILE.DEVICETYPE<1-9>}` is deprecated.  
  
This macro may be used with a numeric index e.g. {INVENTORY.TYPE[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.TYPE.FULL}

The _Type (Full details)_ field in host inventory.  
  
This macro may be used with a numeric index e.g. {INVENTORY.TYPE.FULL[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.URL.A}

The _URL A_ field in host inventory.  
  
This macro may be used with a numeric index e.g. {INVENTORY.URL.A[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.URL.B}

The _URL B_ field in host inventory.  
  
This macro may be used with a numeric index e.g. {INVENTORY.URL.B[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.URL.C}

The _URL C_ field in host inventory.  
  
This macro may be used with a numeric index e.g. {INVENTORY.URL.C[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {INVENTORY.VENDOR}

The _Vendor_ field in host inventory.  
  
This macro may be used with a numeric index e.g. {INVENTORY.VENDOR[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

#### Item macros

##### {ITEM.DESCRIPTION}

The description of the Nth item in the trigger expression that caused a notification.  
  
This macro may be used with a numeric index as {ITEM.DESCRIPTION[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {ITEM.DESCRIPTION.ORIG}

The original description (with macros unresolved) of the Nth item in the trigger expression that caused a notification.  
  
This macro may be used with a numeric index as {ITEM.DESCRIPTION.ORIG[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {ITEM.ID}

The numeric ID of the Nth item in the trigger expression that caused a notification.  
  
This macro may be used with a numeric index as {ITEM.ID[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {ITEM.KEY}

The key of the Nth item in the trigger expression that caused a notification.  
[Macro functions](/documentation/current/en/manual/config/macros/macro_functions) are not supported for this macro if it is used as a placeholder in the first parameter of a [history function](/documentation/current/en/manual/appendix/functions/history), for example, `last(/{HOST.HOST}/{ITEM.KEY})`.  
`{TRIGGER.KEY}` is deprecated.  
  
This macro may be used with a numeric index as {ITEM.KEY[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {ITEM.KEY.ORIG}

The original key (with macros unresolved) of the Nth item in the trigger expression that caused a notification.  
  
This macro may be used with a numeric index as {ITEM.KEY.ORIG[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. host in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {ITEM.LASTVALUE}

The latest value of the Nth item in the trigger expression that caused a notification.  
It will resolve to *UNKNOWN* in the frontend if the latest history value has been collected more than the _Max history display period_ time ago (set in the [Administration → General](/documentation/current/en/manual/web_interface/frontend_sections/administration/general#gui) menu section).  
When used in the problem name, the macro will not resolve to the latest item value when viewing problem events; instead, it will keep the item value from the time when the problem happened.  
When used in notifications, in some cases the macro might not resolve to the latest item value at the moment the trigger fired. For example, if an item quickly receives two values, "A" and "B", and the trigger fires for "A", notifications might show "B" as the latest value due to a slight processing delay - the latest item value changed between the time the trigger fired and when the notification was created. To avoid this, you can use the {ITEM.VALUE} macro, which resolves to the value at the moment the trigger fires, ensuring the correct value is used in the notification.  
It is alias to `last(/{HOST.HOST}/{ITEM.KEY})`.  
The resolved value for text/log items is truncated to 20 characters by the frontend in the following locations:  
\- Operational data;  
\- Trigger description;  
\- Trigger URLs;  
\- Trigger URL labels;  
\- Description of the item value widget.  
To resolve to a full value, you may use [macro functions](/documentation/current/en/manual/config/macros/macro_functions), as no values are truncated by the server. For example: `{{ITEM.LASTVALUE}.regsub("(.*)", \1)}`  
  
This macro may be used with a numeric index e.g. {ITEM.LASTVALUE[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. item in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {ITEM.LASTVALUE.AGE}

The time that elapsed between the latest item value collection and macro evaluation.  
Displayed in a human-readable format (e.g. 1m 45s).  
  
This macro may be used with a numeric index e.g. {ITEM.LASTVALUE.AGE[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. item in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {ITEM.LASTVALUE.DATE}

The date when the latest item value was collected.  
Displayed in a `YYYYMMDD` format.  
Server time zone is used in trigger names (in Monitoring -> Problems list), event names, and tag names and values. In all other cases user time zone is used.  
  
This macro may be used with a numeric index e.g. {ITEM.LASTVALUE.DATE[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. item in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {ITEM.LASTVALUE.TIME}

The time when the latest item value was collected.  
Displayed in an `HHMMSS` format.  
Server time zone is used in trigger names (in Monitoring -> Problems list), event names, and tag names and values. In all other cases user time zone is used.  
  
This macro may be used with a numeric index e.g. {ITEM.LASTVALUE.TIME[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. item in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {ITEM.LASTVALUE.TIMESTAMP}

The UNIX timestamp when the latest item value was collected.  
  
This macro may be used with a numeric index e.g. {ITEM.LASTVALUE.TIMESTAMP[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. item in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {ITEM.LOG.AGE}

The age of the log event.  
With precision down to a second.  
  
This macro may be used with a numeric index e.g. {ITEM.LOG.AGE[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. item in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {ITEM.LOG.DATE}

The date when the log entry was written to the log.  
  
This macro may be used with a numeric index e.g. {ITEM.LOG.DATE[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. item in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {ITEM.LOG.EVENTID}

The ID of the event in the event log.  
For Windows event log monitoring only.  
  
This macro may be used with a numeric index e.g. {ITEM.LOG.EVENTID[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. item in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {ITEM.LOG.NSEVERITY}

The numeric severity of the event in the event log.  
For Windows event log monitoring only.  
  
This macro may be used with a numeric index e.g. {ITEM.LOG.NSEVERITY[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. item in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {ITEM.LOG.SEVERITY}

The verbal severity of the event in the event log.  
For Windows event log monitoring only.  
  
This macro may be used with a numeric index e.g. {ITEM.LOG.SEVERITY[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. item in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {ITEM.LOG.SOURCE}

The source of the event in the event log.  
For Windows event log monitoring only.  
  
This macro may be used with a numeric index e.g. {ITEM.LOG.SOURCE[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. item in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {ITEM.LOG.TIME}

The time when the log entry was written to the log.  
  
This macro may be used with a numeric index e.g. {ITEM.LOG.TIME[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. item in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {ITEM.LOG.TIMESTAMP}

The UNIX timestamp when the log entry was written to the log.  
  
This macro may be used with a numeric index e.g. {ITEM.LOG.TIMESTAMP[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. item in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {ITEM.NAME}

The name of the item with all macros resolved.  
  
This macro may be used with a numeric index e.g. {ITEM.NAME[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. item in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {ITEM.NAME.ORIG}

The original name (with macros unresolved) of the item.  
  
This macro may be used with a numeric index e.g. {ITEM.NAME.ORIG[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. item in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {ITEM.STATE}

The latest state of the Nth item in the trigger expression that caused a notification.  
Possible values: _Not supported_ , _Normal_.  
  
This macro may be used with a numeric index e.g. {ITEM.STATE[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. item in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {ITEM.STATE.ERROR}

The error message with details why an item became unsupported.  
If an item goes into the unsupported state and then immediately gets supported again the error field can be empty.

##### {ITEM.VALUE}

Resolved to either:  
1) the historical (at-the-time-of-event) value of the Nth item in the trigger expression, if used in the context of trigger status change, for example, when displaying events or sending notifications.  
2) the latest value of the Nth item in the trigger expression, if used without the context of trigger status change, for example, when displaying a list of triggers in a pop-up selection window. In this case works the same as {ITEM.LASTVALUE}  
In the first case it will resolve to *UNKNOWN* if the history value has already been deleted or has never been stored.  
In the second case, and in the frontend only, it will resolve to *UNKNOWN* if the latest history value has been collected more than the _Max history display period_ time ago (set in the [Administration→General](/documentation/current/en/manual/web_interface/frontend_sections/administration/general#gui) menu section).  
The resolved value for text/log items is truncated to 20 characters by the frontend in the following locations:  
\- Operational data;  
\- Trigger description;  
\- Trigger URLs;  
\- Trigger URL labels;  
\- Description of the item value widget.  
To resolve to a full value, you may use [macro functions](/documentation/current/en/manual/config/macros/macro_functions), as no values are truncated by the server. For example: `{{ITEM.VALUE}.regsub("(.*)", \1)}`  
  
This macro may be used with a numeric index e.g. {ITEM.VALUE[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. item in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {ITEM.VALUE.AGE}

The time that elapsed between the item value collection and macro evaluation.  
Displayed in a human-readable format (e.g. 1m 45s).  
  
This macro may be used with a numeric index e.g. {ITEM.VALUE.AGE[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. item in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {ITEM.VALUE.DATE}

The date when the item value was collected.  
Displayed in a `YYYYMMDD` format.  
The server time zone is used in trigger names (in Monitoring -> Problems list), event names, and tag names and values. In all other cases user time zone is used.  
  
This macro may be used with a numeric index e.g. {ITEM.VALUE.DATE[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. item in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {ITEM.VALUE.TIME}

The time when the item value was collected.  
Displayed in an `HHMMSS` format.  
The server time zone is used in trigger names (in Monitoring -> Problems list), event names, and tag names and values. In all other cases user time zone is used.  
  
This macro may be used with a numeric index e.g. {ITEM.VALUE.TIME[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. item in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {ITEM.VALUE.TIMESTAMP}

The UNIX timestamp when the item value was collected.  
  
This macro may be used with a numeric index e.g. {ITEM.VALUE.TIMESTAMP[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. item in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {ITEM.VALUETYPE}

The value type of the Nth item in the trigger expression that caused a notification.  
Possible values: _0_ \- Numeric float, _1_ \- Character, _2_ \- Log, _3_ \- Numeric unsigned, _4_ \- Text.  
  
This macro may be used with a numeric index e.g. {ITEM.VALUETYPE[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. item in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

#### Low-level discovery notification macros

##### {LLDRULE.DESCRIPTION}

The description of the low-level discovery rule that caused a notification.

##### {LLDRULE.DESCRIPTION.ORIG}

The original description (with macros unresolved) of the low-level discovery rule that caused a notification.

##### {LLDRULE.ID}

The numeric ID of the low-level discovery rule that caused a notification.

##### {LLDRULE.KEY}

The key of the low-level discovery rule that caused a notification.

##### {LLDRULE.KEYORIG}

The original key (with macros unresolved) of the low-level discovery rule that caused a notification.

##### {LLDRULE.NAME}

The name of the low-level discovery rule that caused a notification.

##### {LLDRULE.NAMEORIG}

The original name (with macros unresolved) of the low-level discovery rule that caused a notification.

##### {LLDRULE.STATE}

The latest state of the low-level discovery rule.  
Possible values: _Not supported_ , _Normal_.  
  
This macro may be used with a numeric index e.g. {LLDRULE.STATE[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. item in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {LLDRULE.STATE.ERROR}

The error message with details why the low-level discovery rule became unsupported.  
If a low-level discovery rule goes into the unsupported state and then immediately gets supported again the error field can be empty.

#### Map macros

##### {MAP.ID}

The network map ID.

##### {MAP.NAME}

The network map name.

#### Proxy macros

##### {PROXY.DESCRIPTION}

The proxy description.  
Resolves to either:  
1) proxy of the Nth item in the trigger expression (in trigger-based notifications). You may use [indexed](/documentation/current/en/manual/appendix/macros/supported_by_location#indexed-macros) macros here.  
2) proxy, which executed discovery (in discovery notifications). Use {PROXY.DESCRIPTION} here, without indexing.  
3) proxy to which an active agent registered (in autoregistration notifications). Use {PROXY.DESCRIPTION} here, without indexing.  
  
This macro may be used with a numeric index e.g. {PROXY.DESCRIPTION[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. item in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

##### {PROXY.NAME}

The proxy name.  
Resolves to either:  
1) proxy of the Nth item in the trigger expression (in trigger-based notifications). You may use [indexed](/documentation/current/en/manual/appendix/macros/supported_by_location#indexed-macros) macros here.  
2) proxy, which executed discovery (in discovery notifications). Use {PROXY.NAME} here, without indexing.  
3) proxy to which an active agent registered (in autoregistration notifications). Use {PROXY.NAME} here, without indexing.  
  
This macro may be used with a numeric index e.g. {PROXY.NAME[<1-9>](supported_by_location#indexed-macros)} to point to the first, second, third, etc. item in a trigger expression. See [indexed macros](supported_by_location#indexed-macros).

#### Script macros

##### {MANUALINPUT}

The manual input value specified by user at script execution time.  

#### Service macros

##### {SERVICE.DESCRIPTION}

The service description with macros resolved.  

##### {SERVICE.ID}

The numeric ID of the service that triggered an action.  

##### {SERVICE.NAME}

The service name with macros resolved.  

##### {SERVICE.ROOTCAUSE}

The list of trigger problem events that caused a service to fail, sorted by severity and host name.  
Includes the following details: host name, event name, severity, age, service tags and values.

##### {SERVICE.TAGS}

A comma-separated list of service event tags.  
Service event tags can be defined in the service configuration tags section. Expanded to an empty string if no tags exist.  

##### {SERVICE.TAGSJSON}

A JSON array containing service event tag objects.  
Service event tags can be defined in the service configuration tags section. Expanded to an empty array if no tags exist.

##### {SERVICE.TAGS<tag name>}

The service event tag value referenced by the tag name.  
The service event tags can be defined in the service configuration tags section.  
A tag name containing non-alphanumeric characters (including non-English multibyte-UTF characters) must be double quoted. Quotes and backslashes inside a quoted tag name must be escaped with a backslash.

#### Trigger macros

##### {TRIGGER.DESCRIPTION}

The trigger description.  
All macros supported in a trigger description will be expanded if `{TRIGGER.DESCRIPTION}` is used in notification text.  
`{TRIGGER.COMMENT}` is deprecated.

##### {TRIGGER.EVENTS.ACK}

The number of acknowledged events for a map element in maps, or for the trigger which generated current event in notifications.

##### {TRIGGER.EVENTS.PROBLEM.ACK}

The number of acknowledged problem events for all triggers disregarding their state.

##### {TRIGGER.EVENTS.PROBLEM.UNACK}

The number of unacknowledged problem events for all triggers disregarding their state.

##### {TRIGGER.EVENTS.UNACK}

The number of unacknowledged events for a map element in maps, or for the trigger which generated current event in notifications.

##### {TRIGGER.EXPRESSION}

The trigger expression.  

##### {TRIGGER.EXPRESSION.EXPLAIN}

A partially-evaluated trigger expression.  
Item-based functions are evaluated and replaced by the results at the time of event generation whereas all other functions are displayed as written in the expression. Can be used for debugging trigger expressions.

##### {TRIGGER.EXPRESSION.RECOVERY}

The trigger recovery expression if _OK event generation_ in [trigger configuration](/documentation/current/en/manual/config/triggers/trigger) is set to "Recovery expression"; otherwise an empty string is returned.  

##### {TRIGGER.EXPRESSION.RECOVERY.EXPLAIN}

A partially-evaluated trigger recovery expression.  
Item-based functions are evaluated and replaced by the results at the time of event generation whereas all other functions are displayed as written in the expression. Can be used for debugging trigger recovery expressions.

##### {TRIGGER.HOSTGROUP.NAME}

A sorted (by SQL query), comma-space separated list of host groups in which the trigger is defined.

##### {TRIGGER.ID}

The numeric trigger ID which triggered this action.  

##### {TRIGGER.NAME}

The trigger name with macros resolved.  
Note that `{EVENT.NAME}` can be used in actions to display the triggered event/problem name with macros resolved.

##### {TRIGGER.NAME.ORIG}

The original trigger name (with macros unresolved).  

##### {TRIGGER.NSEVERITY}

The numerical trigger severity.  
Possible values: _0_ \- Not classified, _1_ \- Information, _2_ \- Warning, _3_ \- Average, _4_ \- High, _5_ \- Disaster.

##### {TRIGGER.PROBLEM.EVENTS.PROBLEM.ACK}

The number of acknowledged problem events for triggers in problem state.

##### {TRIGGER.PROBLEM.EVENTS.PROBLEM.UNACK}

The number of unacknowledged problem events for triggers in problem state.

##### {TRIGGER.SEVERITY}

The trigger severity name.  
Can be defined in _Administration > General > Trigger displaying options_.

##### {TRIGGER.STATE}

The latest state of the trigger.  
Possible values: _Unknown_ , _Normal_.

##### {TRIGGER.STATE.ERROR}

The error message with details why a trigger became unsupported.  
If a trigger goes into the unsupported state and then immediately gets supported again the error field can be empty.

##### {TRIGGER.STATUS}

The trigger value at the time of operation step execution.  
Possible values: _Problem_ , _OK_.  
`{STATUS}` is deprecated.

##### {TRIGGER.TEMPLATE.NAME}

A sorted (by SQL query), comma-space separated list of templates in which the trigger is defined, or *UNKNOWN* if the trigger is defined in a host.

##### {TRIGGER.URL}

The trigger URL.  

##### {TRIGGER.URL.NAME}

The label for the trigger URL.  

##### {TRIGGER.VALUE}

The current numeric trigger value.  
Possible values: _0_ \- trigger is in OK status, _1_ \- trigger is in Problem status.

##### {TRIGGERS.ACK}

The number of acknowledged triggers for a map element, disregarding trigger state.  
A trigger is considered to be acknowledged if all of its problem events are acknowledged.

##### {TRIGGERS.PROBLEM.ACK}

The number of acknowledged problem triggers for a map element.  
A trigger is considered to be acknowledged if all of its problem events are acknowledged.

##### {TRIGGERS.PROBLEM.UNACK}

The number of unacknowledged problem triggers for a map element.  
A trigger is considered to be unacknowledged if at least one of its problem events is unacknowledged.

##### {TRIGGERS.UNACK}

The number of unacknowledged triggers for a map element, disregarding trigger state.  
A trigger is considered to be unacknowledged if at least one of its problem events is unacknowledged.

#### Username macros

##### {USER.FULLNAME}

The name, surname and username of the user who added event acknowledgment or started the script.  

##### {USER.NAME}

The name of the user who started the script.  

##### {USER.SURNAME}

The surname of the user who started the script.  

##### {USER.USERNAME}

The username of the user who started the script.  
`{USER.ALIAS}` is now deprecated.

#### Indexed macros

The indexed macro syntax **{MACRO <1-9>}** can only reference the N-th item, function, or host in a trigger's _Expression_ field:

  * **{HOST.IP1}, {HOST.IP2}, {HOST.IP3}** resolve to the IP addresses of the first, second, and third hosts in the trigger expression (if present).
  * **{ITEM.VALUE1}, {ITEM.VALUE2}, {ITEM.VALUE3}** resolve to the values of the first, second, and third items in the trigger expression at the time of the event (if present).
  * **{FUNCTION.VALUE1}, {FUNCTION.VALUE2}, {FUNCTION.VALUE3}** resolve to the values of the first, second, and third item-based functions at the time of the event (if present).

In the context of triggers, indexed macros always refer to the _Expression_ field of the trigger configuration, not the _Recovery expression_. For example, in a recovery event, **{ITEM.VALUE2}** will resolve to the value of the second item from the problem expression at the time of recovery.

The **{HOST.HOST <1-9>}** macro is also supported within the `{?func(/host/key,param)}` expression macro in **graph names**. For example, `{?func(/{HOST.HOST2}/key,param)}` in a graph name will resolve to the host of the second item in the graph.

Indexed macros will not resolve in any other context beyond the cases mentioned here. For other contexts, use macros without an index (**{HOST.HOST}, {HOST.IP}** , etc.).