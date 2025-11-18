---
title: Regular expression object
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/regexp/object
downloaded: 2025-11-14 10:43:54
---

# Regular expression object

The following objects are directly related to the `regexp` API.

### Regular expression

The global regular expression object has the following properties.

regexpid | ID | ID of the regular expression.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
\- _required_ for update operations  
---|---|---  
name | string | Name of the regular expression.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
test_string | string | Test string.  
  
### Expressions

The expressions object has the following properties.

expression | string | Regular expression.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
expression_type | integer | Type of Regular expression.  
  
Possible values:  
0 - Character string included;  
1 - Any character string included;  
2 - Character string not included;  
3 - Result is TRUE;  
4 - Result is FALSE.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
exp_delimiter | string | Expression delimiter.  
  
Default value: `","`.  
  
Possible values: `","` or `"."`, or `"/"`.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `expression_type` is set to "Any character string included"  
case_sensitive | integer | Case sensitivity.  
  
Default value: `0`.  
  
Possible values:  
0 - Case insensitive;  
1 - Case sensitive.