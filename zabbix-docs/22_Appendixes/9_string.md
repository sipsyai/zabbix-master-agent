---
title: String functions
source: https://www.zabbix.com/documentation/current/en/manual/appendix/functions/string
downloaded: 2025-11-14 10:47:47
---

# 9 String functions

All functions listed here are supported in:

  * [Trigger expressions](/documentation/current/en/manual/config/triggers/expression)
  * [Calculated items](/documentation/current/en/manual/config/items/itemtypes/calculated)
  * [Expression macros](/documentation/current/en/manual/config/macros/expression_macros)

The functions are listed without additional information. Click on the function to see the full details.

ascii | The ASCII code of the leftmost character of the value.  
---|---  
bitlength | The length of value in bits.  
bytelength | The length of value in bytes.  
char | Return the character by interpreting the value as ASCII code.  
concat | The string resulting from concatenating the referenced item values or constant values.  
insert | Insert specified characters or spaces into the character string beginning at the specified position in the string.  
jsonpath | Return the JSONPath result.  
left | Return the leftmost characters of the value.  
length | The length of value in characters.  
ltrim | Remove specified characters from the beginning of string.  
mid | Return a substring of N characters beginning at the character position specified by 'start'.  
repeat | Repeat a string.  
replace | Find the pattern in the value and replace with replacement.  
right | Return the rightmost characters of the value.  
rtrim | Remove specified characters from the end of string.  
trim | Remove specified characters from the beginning and end of string.  
xmlxpath | Return the XML XPath result.  
  
### Function details

Some general notes on function parameters:

  * Function parameters are separated by a comma
  * Expressions are accepted as parameters
  * String parameters must be double-quoted; otherwise they might get misinterpreted
  * Optional function parameters (or parameter parts) are indicated by `<` `>`

##### ascii(value)

The ASCII code of the leftmost character of the value.  
Supported value types: _String_ , _Text_ , _Log_.

Parameter:

  * **value** \- the value to check

For example, a value like 'Abc' will return '65' (ASCII code for 'A').

Example:
    
    
    ascii(last(/host/key))

Copy

✔ Copied

##### bitlength(value)

The length of value in bits.  
Supported value types: _String_ , _Text_ , _Log_ , _Integer_.

Parameter:

  * **value** \- the value to check

Example:
    
    
    bitlength(last(/host/key))

Copy

✔ Copied

##### bytelength(value)

The length of value in bytes.  
Supported value types: _String_ , _Text_ , _Log_ , _Integer_.

Parameter:

  * **value** \- the value to check

Example:
    
    
    bytelength(last(/host/key))

Copy

✔ Copied

##### char(value)

Return the character by interpreting the value as ASCII code.  
Supported value types: _Integer_.

Parameter:

  * **value** \- the value to check

The value must be in the 0-255 range. For example, a value like '65' (interpreted as ASCII code) will return 'A'.

Example:
    
    
    char(last(/host/key))

Copy

✔ Copied

##### concat(<value1>,<value2>,...)

The string resulting from concatenating the referenced item values or constant values.  
Supported value types: _String_ , _Text_ , _Log_ , _Float_ , _Integer_.

Parameter:

  * **valueX** \- the value returned by one of the history functions or a constant value (string, integer, or float number). Must contain at least two parameters.

For example, a value like 'Zab' concatenated to 'bix' (the constant string) will return 'Zabbix'.

Examples:
    
    
    concat(last(/host/key),"bix")
           concat("1 min: ",last(/host/system.cpu.load[all,avg1]),", 15 min: ",last(/host/system.cpu.load[all,avg15]))

Copy

✔ Copied

##### insert(value,start,length,replacement)

Insert specified characters or spaces into the character string beginning at the specified position in the string.  
Supported value types: _String_ , _Text_ , _Log_.

Parameters:

  * **value** \- the value to check;  

  * **start** \- start position;  

  * **length** \- positions to replace;  

  * **replacement** \- replacement string.

For example, a value like 'Zabbbix' will be replaced by 'Zabbix' if 'bb' (starting position 3, positions to replace 2) is replaced by 'b'.

Example:
    
    
    insert(last(/host/key),3,2,"b")

Copy

✔ Copied

##### jsonpath(value,path,<default>)

Return the JSONPath result.  
Supported value types: _String_ , _Text_ , _Log_.

Parameters:

  * **value** \- the value to check;  

  * **path** \- the path (must be quoted);  

  * **default** \- the optional fallback value if the JSONPath query returns no data. Note that on other errors failure is returned (e.g. "unsupported construct").

Example:
    
    
    jsonpath(last(/host/proc.get[zabbix_agentd,,,summary]),"$..size")

Copy

✔ Copied

##### left(value,count)

Return the leftmost characters of the value.  
Supported value types: _String_ , _Text_ , _Log_.

Parameters:

  * **value** \- the value to check;  

  * **count** \- the number of characters to return.

For example, you may return 'Zab' from 'Zabbix' by specifying 3 leftmost characters to return. See also right().

Example:
    
    
    left(last(/host/key),3) #return three leftmost characters

Copy

✔ Copied

##### length(value)

The length of value in characters.  
Supported value types: _String_ , _Text_ , _Log_.

Parameter:

  * **value** \- the value to check.

Examples:
    
    
    length(last(/host/key)) #the length of the latest value
           length(last(/host/key,#3)) #the length of the third most recent value
           length(last(/host/key,#1:now-1d)) #the length of the most recent value one day ago

Copy

✔ Copied

##### ltrim(value,<chars>)

Remove specified characters from the beginning of string.  
Supported value types: _String_ , _Text_ , _Log_.

Parameters:

  * **value** \- the value to check;  

  * **chars** (optional) - specify the characters to remove.

Whitespace is left-trimmed by default (if no optional characters are specified). See also: rtrim(), trim().

Examples:
    
    
    ltrim(last(/host/key)) #remove whitespace from the beginning of string
           ltrim(last(/host/key),"Z") #remove any 'Z' from the beginning of string
           ltrim(last(/host/key)," Z") #remove any space and 'Z' from the beginning of string

Copy

✔ Copied

##### mid(value,start,length)

Return a substring of N characters beginning at the character position specified by 'start'.  
Supported value types: _String_ , _Text_ , _Log_.

Parameters:

  * **value** \- the value to check;  

  * **start** \- start position of the substring;  

  * **length** \- positions to return in substring.

For example, it is possible return 'abbi' from a value like 'Zabbix' if starting position is 2, and positions to return is 4.

Example:
    
    
    mid(last(/host/key),2,4)="abbi"

Copy

✔ Copied

##### repeat(value,count)

Repeat a string.  
Supported value types: _String_ , _Text_ , _Log_.

Parameters:

  * **value** \- the value to check;  

  * **count** \- the number of times to repeat.

Example:
    
    
    repeat(last(/host/key),2) #repeat the value two times

Copy

✔ Copied

##### replace(value,pattern,replacement)

Find the pattern in the value and replace with replacement. All occurrences of the pattern will be replaced.  
Supported value types: _String_ , _Text_ , _Log_.

Parameters:

  * **value** \- the value to check;  

  * **pattern** \- the pattern to find;  

  * **replacement** \- the string to replace the pattern with.

Example:
    
    
    replace(last(/host/key),"ibb","abb") #replace all 'ibb' with 'abb'

Copy

✔ Copied

##### right(value,count)

Return the rightmost characters of the value.  
Supported value types: _String_ , _Text_ , _Log_.

Parameters:

  * **value** \- the value to check;  

  * **count** \- the number of characters to return.

For example, you may return 'bix' from 'Zabbix' by specifying 3 rightmost characters to return. See also left().

Example:
    
    
    right(last(/host/key),3) #return three rightmost characters

Copy

✔ Copied

##### rtrim(value,<chars>)

Remove specified characters from the end of string.  
Supported value types: _String_ , _Text_ , _Log_.

Parameters:

  * **value** \- the value to check;  

  * **chars** (optional) - specify the characters to remove.

Whitespace is right-trimmed by default (if no optional characters are specified). See also: ltrim(), trim().

Examples:
    
    
    rtrim(last(/host/key)) #remove whitespace from the end of string
           rtrim(last(/host/key),"x") #remove any 'x' from the end of string
           rtrim(last(/host/key),"x ") #remove any 'x' and space from the end of string

Copy

✔ Copied

##### trim(value,<chars>)

Remove specified characters from the beginning and end of string.  
Supported value types: _String_ , _Text_ , _Log_.

Parameters:

  * **value** \- the value to check;  

  * **chars** (optional) - specify the characters to remove.

Whitespace is trimmed from both sides by default (if no optional characters are specified). See also: ltrim(), rtrim().

Examples:
    
    
    trim(last(/host/key)) #remove whitespace from the beginning and end of string
           trim(last(/host/key),"_") #remove '_' from the beginning and end of string

Copy

✔ Copied

##### xmlxpath(value,path,<default>)

Return the XML XPath result.  
Supported value types: _String_ , _Text_ , _Log_.

Parameters:

  * **value** \- the value to check;  

  * **path** \- the path (must be quoted);  

  * **default** \- the optional fallback value if the XML XPath query returns an empty nodeset. It will not be returned if the empty result is not a nodeset (i.e., empty string). On other errors failure is returned (e.g. "invalid expression").

Example:
    
    
    xmlxpath(last(/host/xml_result),"/response/error/status")

Copy

✔ Copied

See [all supported functions](/documentation/current/en/manual/appendix/functions).