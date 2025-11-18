---
title: Bitwise functions
source: https://www.zabbix.com/documentation/current/en/manual/appendix/functions/bitwise
downloaded: 2025-11-14 10:47:40
---

# 2 Bitwise functions

All functions listed here are supported in:

  * [Trigger expressions](/documentation/current/en/manual/config/triggers/expression)
  * [Calculated items](/documentation/current/en/manual/config/items/itemtypes/calculated)
  * [Expression macros](/documentation/current/en/manual/config/macros/expression_macros)

The functions are listed without additional information. Click on the function to see the full details.

bitand | The value of "bitwise AND" of an item value and mask.  
---|---  
bitlshift | The bitwise shift left of an item value.  
bitnot | The value of "bitwise NOT" of an item value.  
bitor | The value of "bitwise OR" of an item value and mask.  
bitrshift | The bitwise shift right of an item value.  
bitxor | The value of "bitwise exclusive OR" of an item value and mask.  
  
### Function details

Some general notes on function parameters:

  * Function parameters are separated by a comma
  * Expressions are accepted as parameters
  * Optional function parameters (or parameter parts) are indicated by `<` `>`

##### bitand(value,mask)

The value of "bitwise AND" of an item value and mask.  
Supported value types: _Integer_.

Parameters:

  * **value** \- the value to check;
  * **mask** (mandatory) - a 64-bit unsigned integer (0 - 18446744073709551615).

Although the comparison is done in a bitwise manner, all the values must be supplied and are returned in decimal. For example, checking for the 3rd bit is done by comparing to 4, not 100.

Examples:
    
    
    bitand(last(/host/key),12)=8 or bitand(last(/host/key),12)=4 #3rd or 4th bit set, but not both at the same time
           bitand(last(/host/key),20)=16 #3rd bit not set and 5th bit set

Copy

✔ Copied

##### bitlshift(value,bits to shift)

The bitwise shift left of an item value.  
Supported value types: _Integer_.

Parameters:

  * **value** \- the value to check;
  * **bits to shift** (mandatory) - the number of bits to shift.

Although the comparison is done in a bitwise manner, all the values must be supplied and are returned in decimal. For example, checking for the 3rd bit is done by comparing to 4, not 100.

##### bitnot(value)

The value of "bitwise NOT" of an item value.  
Supported value types: _Integer_.

Parameter:

  * **value** \- the value to check.

Although the comparison is done in a bitwise manner, all the values must be supplied and are returned in decimal. For example, checking for the 3rd bit is done by comparing to 4, not 100.

##### bitor(value,mask)

The value of "bitwise OR" of an item value and mask.  
Supported value types: _Integer_.

Parameters:

  * **value** \- the value to check;
  * **mask** (mandatory) - a 64-bit unsigned integer (0 - 18446744073709551615).

Although the comparison is done in a bitwise manner, all the values must be supplied and are returned in decimal. For example, checking for the 3rd bit is done by comparing to 4, not 100.

##### bitrshift(value,bits to shift)

The bitwise shift right of an item value.  
Supported value types: _Integer_.

Parameters:

  * **value** \- the value to check;
  * **bits to shift** (mandatory) - the number of bits to shift.

Although the comparison is done in a bitwise manner, all the values must be supplied and are returned in decimal. For example, checking for the 3rd bit is done by comparing to 4, not 100.

##### bitxor(value,mask)

The value of "bitwise exclusive OR" of an item value and mask.  
Supported value types: _Integer_.

Parameters:

  * **value** \- the value to check;
  * **mask** (mandatory) - a 64-bit unsigned integer (0 - 18446744073709551615).

Although the comparison is done in a bitwise manner, all the values must be supplied and are returned in decimal. For example, checking for the 3rd bit is done by comparing to 4, not 100.

See [all supported functions](/documentation/current/en/manual/appendix/functions).