---
title: Value map object
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/valuemap/object
downloaded: 2025-11-14 10:46:03
---

# Value map object

The following objects are directly related to the `valuemap` API.

### Value map

The value map object has the following properties.

valuemapid | ID | ID of the value map.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
\- _required_ for update operations  
---|---|---  
hostid | ID | ID of the host or template that the value map belongs to.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _constant_  
\- _required_ for create operations  
name | string | Name of the value map.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
mappings | array | Value mappings for current value map. The mapping object is [described in detail below](object#value-mappings).  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
uuid | string | Universal unique identifier, used for linking imported value maps to already existing ones. Auto-generated, if not given.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if the value map belongs to a template  
  
#### Value mappings

The value mappings object defines value mappings of the value map. It has the following properties.

type | integer | Mapping match type.  
  
Possible values:  
0 - _(default)_ mapping will be applied if value is equal;  
1 - mapping will be applied if value is greater or equal1;  
2 - mapping will be applied if value is less or equal1;  
3 - mapping will be applied if value is in range (ranges are inclusive; multiple ranges, separated by comma character, can be defined)1;  
4 - mapping will be applied if value matches a regular expression2;  
5 - if no matches are found, mapping will not be applied, and the default value will be used.  
  
If `type` is set to "0", "1", "2", "3", "4", then `value` cannot be empty.  
  
If `type` is set to "5", then `value` must be empty.  
---|---|---  
value | string | Original value.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `type` is set to "1", "2", "3", "4"  
\- _supported_ if `type` is set to "5"  
newvalue | string | Value to which the original value is mapped to.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
  
1 supported only for items having value type "numeric unsigned", "numeric float".  
2 supported only for items having value type "character".