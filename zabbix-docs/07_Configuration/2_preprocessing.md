---
title: Item value preprocessing
source: https://www.zabbix.com/documentation/current/en/manual/config/items/preprocessing
downloaded: 2025-11-14 10:34:44
---

# 2 Item value preprocessing

#### Overview

Preprocessing allows you to apply transformations to the received item values before saving them to the database. These transformations/preprocessing steps are performed by Zabbix server or proxy (if items are monitored by proxy).

This feature supports a variety of use cases, such as:

  * converting bytes to bits (e.g., multiplying network traffic values by "8");
  * calculating per-second statistics for incrementally increasing values;
  * applying regular expressions to extract or modify values;
  * executing custom scripts on values;
  * discarding unchanged values to optimize database storage.

One or more preprocessing steps can be configured for an item. These steps are executed in the order they are configured.

If a preprocessing step fails, an item becomes [unsupported](/documentation/current/en/manual/config/items/item#unsupported-items). This can be avoided by _Custom on fail_ error-handling (available for most transformations), allowing you to discard values or set custom values.   
  
For log items, log metadata (without value) will always reset the item unsupported state, making it supported again. This happens even if the initial error occurred after receiving a log value from agent.

All values passed to preprocessing are initially treated as strings. Conversion to the desired value type (as defined in item configuration) is performed at the end of the preprocessing pipeline. However, specific preprocessing steps may trigger earlier conversions, if required. For detailed technical information, see [Preprocessing details](/documentation/current/en/manual/config/items/preprocessing/preprocessing_details).

To ensure that your preprocessing configuration works as expected, you can [test it](/documentation/current/en/manual/config/items/preprocessing/testing).

See also: [Preprocessing examples](/documentation/current/en/manual/config/items/preprocessing/examples)

#### Configuration

Preprocessing steps are defined in the **Preprocessing** tab of the item [configuration](/documentation/current/en/manual/config/items/item#configuration) form.

![](/documentation/current/assets/en/manual/config/items/item_c.png)

Click on _Add_ to select a supported transformation.

The _Type of information_ field is displayed at the bottom of the tab when at least one preprocessing step is defined. If required, it is possible to change the type of information without leaving the _Preprocessing_ tab. See [Creating an item](/documentation/current/en/manual/config/items/item) for the detailed parameter description.

#### Supported transformations

All supported transformations are listed below. Click on the transformation name to see full details about it.

Regular expression | Match the value to the regular expression and replace with the required output. | Text  
---|---|---  
Replace | Find the search string and replace it with another (or nothing).  
Trim | Remove specified characters from the beginning and end of the value.  
Right trim | Remove specified characters from the end of the value.  
Left trim | Remove specified characters from the beginning of the value.  
XML XPath | Extract value or fragment from XML data using XPath functionality. | Structured data  
JSON Path | Extract value or fragment from JSON data using [JSONPath functionality](/documentation/current/en/manual/config/items/preprocessing/jsonpath_functionality).  
CSV to JSON | Convert CSV file data into JSON format.  
XML to JSON | Convert data in XML format to JSON.  
SNMP walk value | Extract value by the specified OID/MIB name and apply formatting options. | SNMP  
SNMP walk to JSON | Convert SNMP values to JSON.  
SNMP get value | Apply formatting options to the SNMP get value.  
Custom multiplier | Multiply the value by the specified integer or floating-point value. | Arithmetic  
Simple change | Calculate the difference between the current and previous value. | Change  
Change per second | Calculate the value change (difference between the current and previous value) speed per second.  
Boolean to decimal | Convert the value from boolean format to decimal. | Numeral systems  
Octal to decimal | Convert the value from octal format to decimal.  
Hexadecimal to decimal | Convert the value from hexadecimal format to decimal.  
JavaScript | Enter JavaScript code. | Custom scripts  
In range | Define a range that a value should be in. | Validation  
Matches regular expression | Specify a regular expression that a value must match.  
Does not match regular expression | Specify a regular expression that a value must not match.  
Check for error in JSON | Check for an application-level error message located at JSONPath.  
Check for error in XML | Check for an application-level error message located at XPath.  
Check for error using a regular expression | Check for an application-level error message using a regular expression.  
Check for not supported value | Check if no item value could be retrieved.  
Discard unchanged | Discard a value if it has not changed. | Throttling  
Discard unchanged with heartbeat | Discard a value if it has not changed within the defined time period.  
Prometheus pattern | Use the following query to extract the required data from Prometheus metrics. | Prometheus  
Prometheus to JSON | Convert the required Prometheus metrics to JSON.  
  
Note that for _Change_ and _Throttling_ preprocessing steps, Zabbix has to remember the last value to calculate/compare the new value as required. These previous values are handled by the preprocessing manager. If Zabbix server or proxy is restarted or there is any change made to preprocessing steps, the last value of the corresponding item is reset, resulting in:

  * for _Simple change_ , _Change per second_ steps - the next value will be ignored because there is no previous value to calculate the change from;
  * for _Discard unchanged_ , _Discard unchanged with heartbeat_ steps - the next value will never be discarded, even if it should have been because of discarding rules.

##### Regular expression

Match the value to the regular expression and replace with the required output.

Parameters:

  * **pattern** \- the regular expression;  

  * **output** \- the output formatting template. An \N (where N=1…9) escape sequence is replaced with the Nth matched group. A \0 escape sequence is replaced with the matched text.

Comments:

  * A failure to match the input value will make the item unsupported;  

  * The regular expression supports extraction of maximum 10 captured groups with the \N sequence;  

  * If you mark the _Custom on fail_ checkbox, it is possible to specify custom error-handling options: either to discard the value, set a specified value, or set a specified error message. In case of a failed preprocessing step, the item will not become unsupported if the option to discard the value or set a specified value is selected.  

  * Please refer to [regular expressions](/documentation/current/en/manual/regular_expressions#example) section for some existing examples.

##### Replace

Find the search string and replace it with another (or nothing).

Parameters:

  * **search string** \- the string to find and replace, case-sensitive (required);  

  * **replacement** \- the string to replace the search string with. The replacement string may also be empty effectively allowing to delete the search string when found.

Comments:

  * All occurrences of the search string will be replaced;
  * It is possible to use escape sequences to search for or replace line breaks, carriage return, tabs and spaces "\n \r \t \s"; backslash can be escaped as "\\\" and escape sequences can be escaped as "\\\n";
  * Escaping of line breaks, carriage return, tabs is automatically done during low-level discovery.

##### Trim

Remove specified characters from the beginning and end of the value.

##### Right trim

Remove specified characters from the end of the value.

##### Left trim

Remove specified characters from the beginning of the value.

##### XML XPath

Extract value or fragment from XML data using XPath functionality.

Comments:

  * For this option to work, Zabbix server (or Zabbix proxy) must be compiled with libxml support;  

  * Namespaces are not supported;  

  * If you mark the _Custom on fail_ checkbox, it is possible to specify custom error-handling options: either to discard the value, set a specified value, or set a specified error message. In case of a failed preprocessing step, the item will not become unsupported if the option to discard the value or set a specified value is selected.

Examples:
    
    
    number(/document/item/value) #will extract '10' from <document><item><value>10</value></item></document>
           number(/document/item/@attribute) #will extract '10' from <document><item attribute="10"></item></document>
           /document/item #will extract '<item><value>10</value></item>' from <document><item><value>10</value></item></document>

Copy

✔ Copied

##### JSON Path

Extract value or fragment from JSON data using [JSONPath functionality](/documentation/current/en/manual/config/items/preprocessing/jsonpath_functionality).

If you mark the _Custom on fail_ checkbox, it is possible to specify custom error-handling options: either to discard the value, set a specified value, or set a specified error message. In case of a failed preprocessing step, the item will not become unsupported if the option to discard the value or set a specified value is selected.

##### CSV to JSON

Convert CSV file data into JSON format.

For more information, see: [CSV to JSON preprocessing](/documentation/current/en/manual/config/items/preprocessing/csv_to_json#csv-header-processing).

##### XML to JSON

Convert data in XML format to JSON.

For more information, see: [Serialization rules](/documentation/current/en/manual/config/items/preprocessing/javascript/javascript_objects#serialization-rules).

If you mark the _Custom on fail_ checkbox, it is possible to specify custom error-handling options: either to discard the value, set a specified value, or set a specified error message. In case of a failed preprocessing step, the item will not become unsupported if the option to discard the value or set a specified value is selected.

##### SNMP walk value

Extract value by the specified OID/MIB name and apply formatting options:  

  * **Unchanged** \- return hex-string as unescaped hex string (_note_ that display hints are still applied);  

  * **UTF-8 from hex-STRING** \- convert hex-string to UTF-8 string;  

  * **MAC from hex-STRING** \- validate hex-string as MAC address and return a proper MAC address string (where `' '` are replaced by `':'`);  

  * **Integer from BITS** \- convert the first 8 bytes of a bit string expressed as a sequence of hex characters (e.g., "1A 2B 3C 4D") into a 64-bit unsigned integer. In bit strings longer than 8 bytes, consequent bytes will be ignored.

If you mark the _Custom on fail_ checkbox, it is possible to specify custom error-handling options: either to discard the value, set a specified value, or set a specified error message. In case of a failed preprocessing step, the item will not become unsupported if the option to discard the value or set a specified value is selected.

##### SNMP walk to JSON

Convert SNMP values to JSON.

Specify a field name in the JSON and the corresponding SNMP OID path. Field values will be populated by values in the specified SNMP OID path.

Comments:

  * Similar value formatting options as in the _SNMP walk value_ step are available;  

  * You may use this preprocessing step for [SNMP OID discovery](/documentation/current/en/manual/discovery/low_level_discovery/examples/snmp_oids_walk);  

  * If you mark the _Custom on fail_ checkbox, it is possible to specify custom error-handling options: either to discard the value, set a specified value, or set a specified error message. In case of a failed preprocessing step, the item will not become unsupported if the option to discard the value or set a specified value is selected.

##### SNMP get value

Apply formatting options to the SNMP get value:  

  * **UTF-8 from Hex-STRING** \- convert hex-string to UTF-8 string;  

  * **MAC from Hex-STRING** \- validate hex-string as MAC address and return a proper MAC address string (where `' '` are replaced by `':'`);  

  * **Integer from BITS** \- convert the first 8 bytes of a bit string expressed as a sequence of hex characters (e.g., "1A 2B 3C 4D") into a 64-bit unsigned integer. In bit strings longer than 8 bytes, consequent bytes will be ignored.

If you mark the _Custom on fail_ checkbox, it is possible to specify custom error-handling options: either to discard the value, set a specified value, or set a specified error message. In case of a failed preprocessing step, the item will not become unsupported if the option to discard the value or set a specified value is selected.

##### Custom multiplier

Multiply the value by the specified integer or floating-point value.

Comments:

  * Use this option to convert values received in KB, MBps, etc., into B, Bps. Otherwise, Zabbix cannot correctly set [prefixes](/documentation/current/en/manual/appendix/suffixes) (K, M, G, etc.).  

  * Note that if the item type of information is _Numeric (unsigned)_ , incoming values with a fractional part will be trimmed (i.e., '0.9' will become '0') before the custom multiplier is applied;  

  * If you use a custom multiplier or store value as _Change per second_ for items with the type of information set to _Numeric (unsigned)_ and the resulting calculated value is actually a float number, the calculated value is still accepted as a correct one by trimming the decimal part and storing the value as an integer;  

  * Supported: scientific notation, for example, `1e+70`; user macros and LLD macros; strings that include macros, for example, `{#MACRO}e+10`, `{$MACRO1}e+{$MACRO2}`. The macros must resolve to an integer or a floating-point number.
  * If you mark the _Custom on fail_ checkbox, it is possible to specify custom error-handling options: either to discard the value, set a specified value, or set a specified error message. In case of a failed preprocessing step, the item will not become unsupported if the option to discard the value or set a specified value is selected.

##### Simple change

Calculate the difference between the current and previous value.

Comments:

  * This step can be useful to measure a constantly growing value;  

  * Evaluated as **value** -**prev_value** , where _value_ \- the current value; _prev_value_ \- the previously received value;  

  * Only one change operation per item ("Simple change" or "Change per second") is allowed;
  * If the current value is smaller than the previous value, Zabbix discards that difference (stores nothing) and waits for another value;  

  * If you mark the _Custom on fail_ checkbox, it is possible to specify custom error-handling options: either to discard the value, set a specified value, or set a specified error message. In case of a failed preprocessing step, the item will not become unsupported if the option to discard the value or set a specified value is selected.

##### Change per second

Calculate the value change (difference between the current and previous value) speed per second.

Comments:

  * This step is useful for calculating the speed per second of a constantly growing value;  

  * As this calculation may produce floating-point numbers, it is recommended to set the 'Type of information' to _Numeric (float)_ , even if the incoming raw values are integers. This is especially relevant for small numbers where the decimal part matters. If the floating-point values are large and may exceed the 'float' field length in which case the entire value may be lost, it is actually recommended to use _Numeric (unsigned)_ and thus trim only the decimal part.  

  * Evaluated as (**value** -**prev_value**)/(**time** -**prev_time**), where _value_ \- the current value; _prev_value_ \- the previously received value; _time_ \- the current timestamp; _prev_time_ \- the timestamp of the previous value;  

  * Only one change operation per item ("Simple change" or "Change per second") is allowed;
  * If the current value is smaller than the previous value, Zabbix discards that difference (stores nothing) and waits for another value. This helps to work correctly with, for instance, a wrapping (overflow) of 32-bit SNMP counters.  

  * If you mark the _Custom on fail_ checkbox, it is possible to specify custom error-handling options: either to discard the value, set a specified value, or set a specified error message. In case of a failed preprocessing step, the item will not become unsupported if the option to discard the value or set a specified value is selected.

##### Boolean to decimal

Convert the value from boolean format to decimal.

Comments:

  * The textual representation is translated into either 0 or 1. Thus, 'TRUE' is stored as 1 and 'FALSE' is stored as 0. All values are matched in a case-insensitive way. Currently recognized values are, for _TRUE_ \- true, t, yes, y, on, up, running, enabled, available, ok, master; for _FALSE_ \- false, f, no, n, off, down, unused, disabled, unavailable, err, slave. Additionally, any non-zero numeric value is considered to be TRUE and zero is considered to be FALSE.  

  * If you mark the _Custom on fail_ checkbox, it is possible to specify custom error-handling options: either to discard the value, set a specified value, or set a specified error message. In case of a failed preprocessing step, the item will not become unsupported if the option to discard the value or set a specified value is selected.

##### Octal to decimal

Convert the value from octal format to decimal.

If you mark the _Custom on fail_ checkbox, it is possible to specify custom error-handling options: either to discard the value, set a specified value, or set a specified error message. In case of a failed preprocessing step, the item will not become unsupported if the option to discard the value or set a specified value is selected.

##### Hexadecimal to decimal

Convert the value from hexadecimal format to decimal.

If you mark the _Custom on fail_ checkbox, it is possible to specify custom error-handling options: either to discard the value, set a specified value, or set a specified error message. In case of a failed preprocessing step, the item will not become unsupported if the option to discard the value or set a specified value is selected.

##### JavaScript

Enter JavaScript code in the modal editor that opens when clicking in the parameter field or on the pencil icon next to it.

Do not use undeclared assignments in preprocessing JavaScript. Use `var` to declare local variables.

Comments:

  * The available JavaScript length depends on the [database used](/documentation/current/en/manual/config/items/item#custom-script-limit);  

  * For more information, see: [Javascript preprocessing](/documentation/current/en/manual/config/items/preprocessing/javascript).

##### In range

Define a range that a value should be in by specifying minimum/maximum values (inclusive).

Comments:

  * Numeric values are accepted (including any number of digits, optional decimal part and optional exponential part, negative values);  

  * The minimum value should be less than the maximum;  

  * At least one value must exist;  

  * User macros and low-level discovery macros can be used;  

  * If you mark the _Custom on fail_ checkbox, it is possible to specify custom error-handling options: either to discard the value, set a specified value, or set a specified error message. In case of a failed preprocessing step, the item will not become unsupported if the option to discard the value or set a specified value is selected.

##### Matches regular expression

Specify a regular expression that a value must match.

If you mark the _Custom on fail_ checkbox, it is possible to specify custom error-handling options: either to discard the value, set a specified value, or set a specified error message. In case of a failed preprocessing step, the item will not become unsupported if the option to discard the value or set a specified value is selected.

##### Does not match regular expression

Specify a regular expression that a value must not match.

If you mark the _Custom on fail_ checkbox, it is possible to specify custom error-handling options: either to discard the value, set a specified value, or set a specified error message. In case of a failed preprocessing step, the item will not become unsupported if the option to discard the value or set a specified value is selected.

##### Check for error in JSON

Check for an application-level error message located at JSONPath. Stop processing if succeeded and the message is not empty; otherwise, continue processing with the value that was before this preprocessing step.

Comments:

  * These external service errors are reported to the user as is, without adding preprocessing step information;  

  * No error will be reported in case of failing to parse invalid JSON;  

  * If you mark the _Custom on fail_ checkbox, it is possible to specify custom error-handling options: either to discard the value, set a specified value, or set a specified error message. In case of a failed preprocessing step, the item will not become unsupported if the option to discard the value or set a specified value is selected.

##### Check for error in XML

Check for an application-level error message located at XPath. Stop processing if succeeded and the message is not empty; otherwise, continue processing with the value that was before this preprocessing step.

Comments:

  * These external service errors are reported to the user as is, without adding preprocessing step information;  

  * No error will be reported in case of failing to parse invalid XML;  

  * If you mark the _Custom on fail_ checkbox, it is possible to specify custom error-handling options: either to discard the value, set a specified value, or set a specified error message. In case of a failed preprocessing step, the item will not become unsupported if the option to discard the value or set a specified value is selected.

##### Check for error using a regular expression

Check for an application-level error message using a regular expression. Stop processing if succeeded and the message is not empty; otherwise, continue processing with the value that was before this preprocessing step.

Parameters:

  * **pattern** \- the regular expression;  

  * **output** \- the output formatting template. An \N (where N=1…9) escape sequence is replaced with the Nth matched group. A \0 escape sequence is replaced with the matched text.

Comments:

  * These external service errors are reported to the user as is, without adding preprocessing step information;  

  * If you mark the _Custom on fail_ checkbox, it is possible to specify custom error-handling options: either to discard the value, set a specified value, or set a specified error message. In case of a failed preprocessing step, the item will not become unsupported if the option to discard the value or set a specified value is selected.

##### Check for not supported value

Check if no item value could be retrieved. Specify how the failure should be processed, based on inspecting the returned error message.

Parameters:

  * **scope** \- select the error processing scope:  
_any error_ \- any error;  
_error matches_ \- only the error that matches the regular expression specified in _pattern_ ;  
_error does not match_ \- only the error that does not match the regular expression specified in _pattern_  

  * **pattern** \- the regular expression to match the error to. If _any error_ is selected in the scope parameter, this field is not displayed. If displayed, this field is mandatory.  

Comments:

  * Normally, the absence/failure to retrieve a value would lead to the item becoming unsupported. This preprocessing step allows you to modify this behavior. If you mark the _Custom on fail_ checkbox (always marked and grayed out for this preprocessing step), it is possible to specify custom error-handling options: either to discard the value, set a specified value, or set a specified error message. In case of a failed preprocessing step, the item will not become unsupported if the option to discard the value or set a specified value is selected.
  * This preprocessing step only checks if no item value could be retrieved. It does not check, for example, if the type of the retrieved value (e.g., string) matches the item's type of information (e.g., numeric); for details, see [Preprocessing examples](/documentation/current/en/manual/config/items/preprocessing/examples#checking-for-not-supported-value). If there is a type mismatch, the item may still become unsupported after all preprocessing steps are executed. To check for a type mismatch, you may use, for example, the _Custom multiplier_ preprocessing step; see [Preprocessing examples](/documentation/current/en/manual/config/items/preprocessing/examples#checking-retrieved-value-type).
  * Capturing regular expression groups is supported in the _Set value to_ or _Set error to_ fields. Use \N (where N=1…9) to retrieve the Nth matched group; use \0 to retrieve the matched text;
  * These steps are always executed as the first preprocessing steps and are placed above all others after saving changes to the item;
  * Multiple _Check for not supported value_ steps are supported, in the specified order. A step for _any error_ will be automatically placed as the last step in this group.

##### Discard unchanged

Discard a value if it has not changed.

Comments:

  * If a value is discarded, it is not saved in the database and Zabbix server has no knowledge that this value was received. No trigger expressions will be evaluated, as a result, no problems for related triggers will be created/resolved. Functions will work only based on data that is actually saved in the database. As trends are built based on data in the database, if there is no value saved for an hour then there will also be no trends data for that hour.  

  * Only one throttling option can be specified per item.

##### Discard unchanged with heartbeat

Discard a value if it has not changed within the defined time period (in seconds).

Comments:

  * Positive integer values are supported to specify the seconds (minimum - 1 second);  

  * Time suffixes can be used (e.g., 30s, 1m, 2h, 1d);  

  * User macros and low-level discovery macros can be used;  

  * If a value is discarded, it is not saved in the database and Zabbix server has no knowledge that this value was received. No trigger expressions will be evaluated, as a result, no problems for related triggers will be created/resolved. Functions will work only based on data that is actually saved in the database. As trends are built based on data in the database, if there is no value saved for an hour then there will also be no trends data for that hour.  

  * Only one throttling option can be specified per item.

##### Prometheus pattern

Use the following query to extract the required data from Prometheus metrics.

See [Prometheus checks](/documentation/current/en/manual/config/items/itemtypes/prometheus) for more details.

##### Prometheus to JSON

Convert the required Prometheus metrics to JSON.

See [Prometheus checks](/documentation/current/en/manual/config/items/itemtypes/prometheus) for more details.

#### Macro support

[User macros](/documentation/current/en/manual/config/macros/user_macros) and user macros with context are supported in:

  * preprocessing step parameters, including JavaScript code;
  * custom error-handling parameters (_Set value to_ and _Set error to_ fields).

The macro context is ignored when a macro is replaced with its value. The macro value is inserted in the code as is, it is not possible to add additional escaping before placing the value in the JavaScript code. Please be advised that this can cause JavaScript errors in some cases.

#### Testing

See [preprocessing testing](/documentation/current/en/manual/config/items/preprocessing/testing).