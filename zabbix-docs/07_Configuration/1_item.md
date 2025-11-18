---
title: Creating an item
source: https://www.zabbix.com/documentation/current/en/manual/config/items/item
downloaded: 2025-11-14 10:34:41
---

# 1 Creating an item

#### Overview

To create an item in Zabbix frontend, do the following:

  * Go to: _Data collection_ > _Hosts_
  * Click on _Items_ in the row of the host
  * Click on _Create item_ in the upper-right corner of the screen
  * Enter parameters of the item in the form

You can also create an item by opening an existing one, pressing the _Clone_ button and then saving under a different name.

#### Configuration

The **Item** tab contains general item attributes.

![](/documentation/current/assets/en/manual/config/items/item.png)

All mandatory input fields are marked with a red asterisk.

_Name_ | Item name.  
[User macros](/documentation/current/en/manual/config/macros/user_macros) are supported.  
---|---  
_Type_ | Item type. See individual [item type](/documentation/current/en/manual/config/items/itemtypes) sections.  
_Key_ | Item key (up to 2048 characters).  
The supported [item keys](/documentation/current/en/manual/config/items/itemtypes) can be found in individual item type sections.  
The key must be unique within a single host.  
If key type is 'Zabbix agent', 'Zabbix agent (active)' or 'Simple check', the key value must be supported by Zabbix agent or Zabbix server.  
See also: the correct [key format](/documentation/current/en/manual/config/items/item/key).  
_Type of information_ | Type of data as stored in the database after performing conversions, if any.  
**Numeric (unsigned)** \- 64-bit unsigned integer.  
Note that a floating point value, if received for an integer item, will be trimmed from its decimal part.  
**Numeric (float)** \- 64-bit floating point number.  
This type will allow precision of approximately 15 digits and range from approximately -1.79E+308 to 1.79E+308 (with exception of [PostgreSQL 11 and earlier versions](/documentation/current/en/manual/installation/known_issues#numeric-float-data-type-range-with-postgresql-11-and-earlier)).  
Receiving values in scientific notation is also supported. E.g. 1.23E+7, 1e308, 1.1E-4.  
**Character** \- short text data.  
**Log** \- long text data with optional log related properties (timestamp, source, severity, logeventid).  
**Text** \- long text data. See also text data limits.  
**Binary** \- binary number (supported for dependent items only). A binary number will be resolved to a static "binary value" string in _Latest data_ ; {ITEM.VALUE}, {ITEM.LASTVALUE} and expression macros will resolve to UNKNOWN.  
For item keys that return data only in one specific format, matching type of information is selected automatically.  
_Host interface_ | Select the host interface. This field is available when editing an item on the host level.  
_Units_ | If a unit symbol is set, Zabbix applies postprocessing to the received item value and displays it with the specified unit postfix.  
Supported unit symbols with special formatting (and examples of received item value → displayed value):  
**B** \- bytes (1024 → 1 KB)  
**Bps** \- bytes per second (1024 → 1 KBps)  
**s** \- seconds, displayed using up to three largest non-zero time units (881764 → 10d 4h 56m)  
**uptime** \- elapsed time in hh:mm:ss or N days, hh:mm:ss (881764 → 10 days, 04:56:04)  
**unixtime** \- Unix timestamp, formatted as yyyy.mm.dd hh:mm:ss (881764 → 1970-01-11 04:56:04 AM); for correct formatting, the received item value must be _Numeric (unsigned)_.  
For other units (such as Hz, W, etc.), if the received value exceeds 1000, it is divided by 1000 and displayed with a corresponding prefix (5000 → 5 KHz, 881764 → 881.76 KW).  
If the unit symbol is prefixed with `!`, unit conversion and prefixing are disabled (1024 !B → 1024 B, 61 !s → 61 s).  
For more examples and details on unit symbols and unit conversion, see [Item value suffixes](/documentation/current/en/manual/appendix/suffixes#item-value-suffixes).  
_Update interval_ | Retrieve a new value for this item every N seconds. Maximum allowed update interval is 86400 seconds (1 day).  
[Time suffixes](/documentation/current/en/manual/appendix/suffixes) are supported, e.g., 30s, 1m, 2h, 1d.  
[User macros](/documentation/current/en/manual/config/macros/user_macros) are supported.  
A single macro has to fill the whole field. Multiple macros in a field or macros mixed with text are not supported.  
_Note_ : The update interval can only be set to '0' if custom intervals exist with a non-zero value. If set to '0', and a custom interval (flexible or scheduled) exists with a non-zero value, the item will be polled during the custom interval duration.  
_Note_ that the first item poll after the item became active or after update interval change might occur earlier than the configured value.   
New items will be checked within 60 seconds of their creation, unless they have Scheduling or Flexible update interval and the _Update interval_ is set to 0.   
An existing passive item can be polled for value immediately by pushing the _Execute now_ button.  
_Custom intervals_ | You can create custom rules for checking the item:  
**Flexible** \- create an exception to the _Update interval_ (interval with different frequency).  
**Scheduling** \- create a custom polling schedule.  
For detailed information see [Custom intervals](/documentation/current/en/manual/config/items/item/custom_intervals).  
[Time suffixes](/documentation/current/en/manual/appendix/suffixes) are supported in the _Interval_ field, e.g., 30s, 1m, 2h, 1d.  
[User macros](/documentation/current/en/manual/config/macros/user_macros) are supported.  
A single macro has to fill the whole field. Multiple macros in a field or macros mixed with text are not supported.  
_Timeout_ | Set the item check timeout (available for [supported](/documentation/current/en/manual/web_interface/frontend_sections/administration/general#timeouts) item types). Select the timeout option:  
**Global** \- proxy/global timeout is used (displayed in the grayed out _Timeout_ field).  
**Override** \- custom timeout is used (set in the _Timeout_ field; allowed range: 1 - 600s). [Time suffixes](/documentation/current/en/manual/appendix/suffixes#time-suffixes), e.g. 30s, 1m, and [user macros](/documentation/current/en/manual/config/macros/user_macros) are supported.  
Clicking the _Timeouts_ link allows you to configure [proxy](/documentation/current/en/manual/distributed_monitoring/proxies#configuration) timeouts or [global](/documentation/current/en/manual/web_interface/frontend_sections/administration/general#timeouts) timeouts (if a proxy is not used). Note that the _Timeouts_ link is visible only to users of _Super admin_ type with permissions to _Administration_ > [_General_](/documentation/current/en/manual/web_interface/frontend_sections/administration/general) or _Administration_ > [_Proxies_](/documentation/current/en/manual/web_interface/frontend_sections/administration/proxies) frontend sections.  
_History_ | Select either:  
**Do not store** \- item history is not stored. Useful for master items if only dependent items need to keep history.  
This setting cannot be overridden by global housekeeper [settings](/documentation/current/en/manual/web_interface/frontend_sections/administration/housekeeping).  
**Store up to** \- specify the duration of keeping detailed history in the database (1 hour to 25 years). Older data will be removed by the housekeeper. Stored in seconds.  
[Time suffixes](/documentation/current/en/manual/appendix/suffixes) are supported, e.g., 2h, 1d. [User macros](/documentation/current/en/manual/config/macros/user_macros) are supported.  
The _Store up to_ value can be overridden globally in _Administration > [Housekeeping](/documentation/current/en/manual/web_interface/frontend_sections/administration/housekeeping)_.  
If a global overriding setting exists, an orange ![](/documentation/current/assets/en/manual/config/info_orange.png) info icon is displayed. If you position your mouse on it, a warning message is displayed, e.g., _Overridden by global housekeeper settings (1d)_.  
It is recommended to keep the recorded values for the smallest possible time to reduce the size of value history in the database. Instead of storing a long history of values, you can store longer data of trends.  
See also [History and trends](/documentation/current/en/manual/config/items/history_and_trends).  
_Trends_ | Select either:  
**Do not store** \- trends are not stored.  
This setting cannot be overridden by global housekeeper [settings](/documentation/current/en/manual/web_interface/frontend_sections/administration/housekeeping).  
**Store up to** \- specify the duration of keeping aggregated (hourly min, max, avg, count) history in the database (1 day to 25 years). Older data will be removed by the housekeeper. Stored in seconds.  
[Time suffixes](/documentation/current/en/manual/appendix/suffixes) are supported, e.g., 24h, 1d. [User macros](/documentation/current/en/manual/config/macros/user_macros) are supported.  
The _Store up to_ value can be overridden globally in _Administration > [Housekeeping](/documentation/current/en/manual/web_interface/frontend_sections/administration/housekeeping)_.  
If a global overriding setting exists, an orange ![](/documentation/current/assets/en/manual/config/info_orange.png) info icon is displayed. If you position your mouse on it, a warning message is displayed, e.g., _Overridden by global housekeeper settings (7d)_.  
_Note:_ Keeping trends is not available for non-numeric data - character, log and text.  
See also [History and trends](/documentation/current/en/manual/config/items/history_and_trends).  
_Value mapping_ | Apply value mapping to this item. [Value mapping](/documentation/current/en/manual/config/items/mapping) does not change received values, it is for displaying data only.  
It works with _Numeric(unsigned)_ , _Numeric(float)_ and _Character_ items.  
For example, "Windows service states".  
_Log time format_ | Available for items of type **Log** only. Supported placeholders:  
**y** : _Year (1970-2038)_.  
**M** : _Month (01-12)_.  
**d** : _Day (01-31)_.  
**h** : _Hour (00-23)_.  
**m** : _Minute (00-59)_.  
**s** : _Second (00-59)_.  
If left blank, the timestamp will be set to 0 in Unix time, representing January 1, 1970.  
For example, consider the following line from the Zabbix agent log file:  
" 23480:20100328:154718.045 Zabbix agent started. Zabbix 1.8.2 (revision 11211)."  
It begins with six character positions for PID, followed by date, time, and the rest of the message.  
The log time format for this line would be "pppppp:yyyyMMdd:hhmmss".  
Note that "p" and ":" characters are placeholders and can be any characters except "yMdhms".  
_Populates host inventory field_ | You can select a host inventory field that the value of item will populate. This will work if automatic [inventory](/documentation/current/en/manual/config/hosts/inventory) population is enabled for the host.  
This field is not available if _Type of information_ is set to 'Log'.  
_Description_ | Enter an item description. [User macros](/documentation/current/en/manual/config/macros/user_macros) are supported.  
_Enabled_ | Mark the checkbox to enable the item so it will be processed.  
When you disable the item, it is immediately removed from the history cache (except for its last value, which is kept for logs).  
_Latest data_ | Click on the link to view the latest data for the item.  
This link is only available when editing an already existing item.  
  
Item type specific fields are described on [corresponding pages](/documentation/current/en/manual/config/items/itemtypes).

When editing an existing [template](/documentation/current/en/manual/config/templates) level item on a host level, a number of fields are read-only. You can use the link in the form header and go to the template level and edit them there, keeping in mind that the changes on a template level will change the item for all hosts that the template is linked to.

The **Tags** tab allows to define item-level [tags](/documentation/current/en/manual/config/tagging).

![](/documentation/current/assets/en/manual/config/items/item_b.png)

##### Item value preprocessing

The **Preprocessing** tab allows to define [transformation rules](/documentation/current/en/manual/config/items/preprocessing) for the received values.

#### Item testing

To perform item testing, ensure that the system time on the server and the proxy is [synchronized](/documentation/current/en/manual/installation/requirements#time-synchronization). In the case when the server time is behind, item testing may return an error message "The task has been expired." Having set different time zones on the server and the proxy, however, won't affect the testing result.

It is possible to test an item and, if configured correctly, get a real value in return. Testing can occur even before an item is saved.

Testing is available for host and template items, item prototypes and low-level discovery rules. Testing is not available for active items.

Item testing is available for the following passive item types:

  * Zabbix agent
  * SNMP agent (v1, v2, v3)
  * IPMI agent
  * SSH checks
  * Telnet checks
  * JMX agent
  * Simple checks (except `icmpping*`, `vmware.*` items)
  * Zabbix internal
  * Calculated items
  * External checks
  * Database monitor
  * HTTP agent
  * Script
  * Browser

To test an item, click on the _Test_ button at the bottom of the item configuration form. Note that the _Test_ button will be disabled for items that cannot be tested (like active checks, excluded simple checks).

![](/documentation/current/assets/en/manual/config/items/item_test_button.png)

The item testing form has fields for the required host parameters (host address, port, test with server/proxy (proxy name)) and item-specific details (such as SNMPv2 community or SNMPv3 security credentials). These fields are context aware:

  * The values are pre-filled when possible, i.e., for items requiring an agent, by taking the information from the selected agent interface of the host.
  * The values have to be filled manually for template items.
  * Plain-text macro values are resolved.
  * Fields where the value (or part of the value) is a secret or Vault macro are empty and have to be entered manually. If any item parameter contains a secret macro value, the following warning message is displayed: "Item contains user-defined macros with secret values. Values of these macros should be entered manually."
  * The fields are disabled when not needed in the context of the item type (e.g., the host address field and the proxy field are disabled for calculated items)

To test the item, click on _Get value_. If the value is retrieved successfully, it will fill the _Value_ field, moving the current value (if any) to the _Previous value_ field while also calculating the _Prev. time_ field, i.e., the time difference between the two values (clicks) and trying to detect an EOL sequence and switch to CRLF if detecting "\n\r" in retrieved value.

Click on _Get value and test_ to test the preprocessing.

![](/documentation/current/assets/en/manual/config/items/item_test.png)

Values retrieved from a host and test results are truncated to a maximum size of 512KB when sent to the frontend. If a result is truncated, a warning icon is displayed. The warning description is displayed on mouseover. Note that data larger than 512KB is still processed fully by Zabbix server.

If the configuration is incorrect, an error message is displayed describing the possible cause.

![](/documentation/current/assets/en/manual/config/items/item_test_error.png)

A successfully retrieved value from host can also be used to test [preprocessing steps](/documentation/current/en/manual/config/items/preprocessing#testing).

#### Form buttons

Buttons at the bottom of the form allow to perform several operations.

![](/documentation/current/assets/en/manual/config/button_add.png) | Add an item. This button is only available for new items.  
---|---  
![](/documentation/current/assets/en/manual/config/button_update.png) | Update the properties of an item.  
![](/documentation/current/assets/en/manual/config/button_clone.png) | Create another item based on the properties of the current item.  
![](/documentation/current/assets/en/manual/config/button_execute.png) | Execute a check for a new item value immediately. Supported for **passive** checks only (see [more details](/documentation/current/en/manual/config/items/check_now)).  
_Note_ that when checking for a value immediately, configuration cache is not updated, thus the value will not reflect very recent changes to item configuration.  
![](/documentation/current/assets/en/manual/config/button_test.png) | Test if item configuration is correct by getting a value.  
![](/documentation/current/assets/en/manual/config/button_clear_history.png) | Delete the item history and trends.  
![](/documentation/current/assets/en/manual/config/button_delete.png) | Delete the item.  
![](/documentation/current/assets/en/manual/config/button_cancel.png) | Cancel the editing of item properties.  
  
#### Text data limits

Text data limits depend on the database backend. Before storing text values in the database they get truncated to match the database value type limit:

| **Character** | **Log** | **Text**  
---|---|---|---  
_MySQL_ | 255 characters | 65536 bytes | 65536 bytes  
_PostgreSQL_ | 255 characters | 65536 characters | 65536 characters  
_SQLite (only Zabbix proxy)_ | 255 characters | 65536 characters | 65536 characters  
  
#### Custom script limit

Available custom script length depends on the database used:

_MySQL_ | 65535 | 65535  
---|---|---  
_PostgreSQL_ | 65535 | not limited  
_SQLite (only Zabbix proxy)_ | 65535 | not limited  
  
#### Item timeout

Item timeout specifies how long Zabbix should wait before aborting the check as failed.

When the timeout is reached, the check is aborted even if data retrieval is unfinished. If data is received partially, the item becomes unsupported and an error message is logged (for example, if data is successfully collected for only one of multiple OIDs in an SNMP check).

For many item types, you can set **flexible** item timeouts:

  * per single item
  * per item type (on a [proxy](/documentation/current/en/manual/distributed_monitoring/proxies#adding-proxies) level)
  * per item type (on a [global](/documentation/current/en/manual/web_interface/frontend_sections/administration/general#timeouts) level)

A custom timeout _per single item_ is useful if you want to specify a longer timeout for a specific item, while keeping timeouts for other items low.

**Timeout precedence**

  1. Single item timeout overrides any other timeouts.
  2. Proxy-level timeouts override global timeouts.

The timeout from Zabbix [server](/documentation/current/en/manual/appendix/config/zabbix_server#timeout) or [proxy](/documentation/current/en/manual/appendix/config/zabbix_proxy#timeout) configuration plays **no** role in checks for which flexible timeouts are set.

##### Flexible timeout support

Flexible item timeouts are supported for these item types:

  * [Zabbix agent](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent) (both passive and active checks)
  * [SNMP agent](/documentation/current/en/manual/config/items/itemtypes/snmp) (except legacy SNMP checks**1**)
  * [Simple check](/documentation/current/en/manual/config/items/itemtypes/simple_checks) (except `icmpping*` and VMware items**2**)
  * [SSH agent](/documentation/current/en/manual/config/items/itemtypes/ssh_checks)
  * [Telnet agent](/documentation/current/en/manual/config/items/itemtypes/telnet_checks)
  * [External check](/documentation/current/en/manual/config/items/itemtypes/external)
  * [Database monitor](/documentation/current/en/manual/config/items/itemtypes/odbc_checks)
  * [Script](/documentation/current/en/manual/config/items/itemtypes/script)
  * [HTTP agent](/documentation/current/en/manual/config/items/itemtypes/http)
  * [Browser](/documentation/current/en/manual/config/items/itemtypes/browser)

**1** For legacy SNMP checks (single OID polling), timeout settings from the [server](/documentation/current/en/manual/appendix/config/zabbix_server#timeout) or [proxy](/documentation/current/en/manual/appendix/config/zabbix_proxy#timeout) apply.  
**2** For `icmpping*` items, the timeout value is specified directly in the item key. VMware monitoring items use their own VMwareTimeout parameter from [server](/documentation/current/en/manual/appendix/config/zabbix_server#vmwaretimeout) or [proxy](/documentation/current/en/manual/appendix/config/zabbix_proxy#vmwaretimeout) configuration.

#### Unsupported items

Unsupported items are reported as having a _Not supported_ status and are still rechecked at their standard _[Update interval](/documentation/current/en/manual/config/items/item?#configuration)_.

An item becomes unsupported if its value cannot be retrieved for some reason (e.g. connection error, no pollers configured to process the item). In addition, items that do not receive historical data remain in the _Not supported_ status. This is expected behavior—an item transitions to a _Normal_ status only when it receives new, valid historical data.

Like problems, unsupported items are re-evaluated only when new data is received—even if there is no historical data available for that item anymore. In other words, items and triggers change their state solely upon receiving new data. However, if a trigger expression includes a [date and time](/documentation/current/en/manual/appendix/functions/time) and/or [nodata()](/documentation/current/en/manual/appendix/functions/history#nodata) function, the trigger will be recalculated every 30 seconds (see [triggers calculation time](/documentation/current/en/manual/config/triggers#calculation-time) for details).