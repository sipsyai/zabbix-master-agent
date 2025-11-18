---
title: Macro functions
source: https://www.zabbix.com/documentation/current/en/manual/config/macros/macro_functions
downloaded: 2025-11-14 10:36:30
---

# 1 Macro functions

#### Overview

Macro functions offer the ability to customize [macro](/documentation/current/en/manual/config/macros) values (for example, shorten or extract specific substrings), making them easier to work with.

The syntax of a macro function is:
    
    
    {macro.func(params)}

Copy

✔ Copied

where

  * **macro** \- the macro to customize;
  * **func** \- the function to apply (see supported functions);
  * **params** \- a comma-delimited list of function parameters, which must be **double-quoted** if: 
    * start with a space or double quotes;
    * contain closing parentheses or a comma.

For example:
    
    
    {{TIME}.fmttime(format,time_shift)}
           {{ITEM.VALUE}.regsub(pattern, output)}
           {{$USERMACRO}.regsub(pattern, output)}
           {{#LLDMACRO}.regsub(pattern, output)}

Copy

✔ Copied

Macro functions are supported for

  * [Built-in macros](/documentation/current/en/manual/appendix/macros/supported_by_location)
  * [User macros](/documentation/current/en/manual/appendix/macros/supported_by_location#other-macro-types)
  * [Low-level discovery macros](/documentation/current/en/manual/appendix/macros/supported_by_location#other-macro-types)
  * [Expression macros](/documentation/current/en/manual/appendix/macros/supported_by_location#other-macro-types)

Macro functions can be used in all locations supporting the listed macros. This applies unless explicitly stated that only a macro is expected (for example, when configuring [host macros](/documentation/current/en/manual/config/hosts/host#configuration) or low-level discovery rule [filters](/documentation/current/en/manual/discovery/low_level_discovery#filter)).

A single function per macro is supported; multiple macro functions in chain are not supported.

Please see [escaping examples](/documentation/current/en/manual/appendix/escaping) for cases when macro functions are used inside other contexts (function, item key, another macro, etc).

#### Supported functions

The functions are listed without additional information. Click on the function to see the full details.

btoa | Encoding macro value into Base64 encoding.  
---|---  
fmtnum | Number formatting to control the number of digits printed after the decimal point.  
fmttime | Time formatting.  
htmldecode | Decoding macro value from HTML encoding.  
htmlencode | Encoding macro value into HTML encoding.  
iregsub | Substring extraction by a regular expression match (case-insensitive).  
lowercase | Transformation of macro value characters into lowercase.  
regrepl | Replacement of character/substring in macro value.  
regsub | Substring extraction by a regular expression match (case-sensitive).  
tr | Transliteration of macro value characters.  
uppercase | Transformation of macro value characters into uppercase.  
urldecode | Decoding macro value from URL encoding.  
urlencode | Encoding macro value into URL encoding.  
  
#### Function details

Optional function parameters are indicated by < >.

##### btoa

Encoding a macro value into Base64 encoding. Base64 encoding is a method for representing binary data as text, useful for storing and secure transmission of binary content over text-based protocols.

Example:
    
    
    {{ITEM.VALUE}.btoa()} - will Base64-encode a value like "zabbix" into "emFiYml4"

Copy

✔ Copied

##### fmtnum(digits)

Number formatting to control the number of digits printed after the decimal point.

Parameters:

  * **digits** \- the number of digits after decimal point. Valid range: 0-20. No trailing zeros will be produced.

Examples:
    
    
    {{ITEM.VALUE}.fmtnum(2)} - will return "24.35" from a received value of "24.3483523"
           {{ITEM.VALUE}.fmtnum(0)} - will return "24" from a received value of "24.3483523"

Copy

✔ Copied

##### fmttime(format,<time_shift>)

Time formatting.  
Note that this function can be used with macros that resolve to a value in one of the following time formats:

  * `hh:mm:ss`
  * `yyyy-mm-ddThh:mm:ss[tz]` (ISO8601 standard)
  * UNIX timestamp

Parameters:

  * **format** \- mandatory format string, compatible with `strftime` function formatting;
  * **time_shift** (optional) - the time shift applied to the time before formatting; should start with `-<N><time_unit>` or `+<N><time_unit>`, where: 
    * `N` \- the number of time units to add or subtract;
    * `time_unit` \- h (hour), d (day), w (week), M (month) or y (year).

Comments:

  * The `time_shift` parameter supports multistep time operations and may include `/<time_unit>` for shifting to the beginning of the time unit (`/d` \- midnight, `/w` \- 1st day of the week (Monday), `/M` \- 1st day of the month, etc.). Examples: `-1w` \- exactly 7 days back; `-1w/w` \- Monday of the previous week; `-1w/w+1d` \- Tuesday of the previous week.
  * Time operations are calculated from left to right without priorities. For example, `-1M/d+1h/w` will be parsed as `((-1M/d)+1h)/w`.

Examples:
    
    
    {{TIME}.fmttime(%B)} - will return "October" from a received value of "1633098961"
           {{TIME}.fmttime(%d %B,-1M/M)} - will return "1 September" from a received value of "1633098961"

Copy

✔ Copied

##### htmldecode

Decoding a macro value from HTML encoding.

The following characters are supported:

`&amp;` | `&`  
---|---  
`&lt;` | `<`  
`&gt;` | `>`  
`&quot;` | `"`  
`&#039;` | `'`  
`&#39;` | `'`  
  
Example:
    
    
    {{ITEM.VALUE}.htmldecode()} - will HTML-decode a value like "&lt;" into "<"

Copy

✔ Copied

##### htmlencode

Encoding a macro value into HTML encoding.

The following characters are supported:

`&` | `&amp;`  
---|---  
`<` | `&lt;`  
`>` | `&gt;`  
`"` | `&quot;`  
`'` | `&#39;`  
  
Example:
    
    
    {{ITEM.VALUE}.htmlencode()} - will HTML-encode a character like "<" into "&lt;"

Copy

✔ Copied

##### iregsub(pattern,output)

Substring extraction by a regular expression match (case-insensitive).

Parameters:

  * **pattern** \- the regular expression to match;
  * **output** \- the output options. **\1 - \9** placeholders are supported to capture groups. **\0** returns the matched text.

Comments:

  * If there is no match for the regular expression, the function returns an empty string.
  * If the function pattern is an incorrect regular expression, then the macro evaluates to 'UNKNOWN' (except for low-level discovery macros, in which case the function will be ignored, and the macro will remain unresolved).
  * References to non-existent capture groups in the replacement string are replaced with an empty string.

Example:
    
    
    {{ITEM.VALUE}.iregsub("fail|error|fault|problem","ERROR")} - will resolve to "ERROR" if "fail", "error", "fault", or "problem" substrings are received (case-insensitive); will return an empty string if there is no match

Copy

✔ Copied

##### lowercase

Transformation of all macro value characters into lowercase. Works with single-byte character sets (such as ASCII) and does not support UTF-8.

Example:
    
    
    {{ITEM.VALUE}.lowercase()} - will transform a value like "Zabbix SERVER" into "zabbix server" (lowercase)

Copy

✔ Copied

##### regrepl(pattern,replacement,<pattern2>,<replacement2>,...)

Replacement of character/substring in macro value.

Parameters:

  * **pattern** \- the regular expression to match;
  * **replacement** \- the replacement string. **\1 - \9** placeholders are supported in replacement strings to capture groups.

Comments:

  * The patterns and replacements are processed sequentially, with each subsequent pair being applied in accordance with the outcome of the previous replacement;
  * References to non-existent capture groups in the replacement string are replaced with an empty string.

Examples:
    
    
    {{ITEM.VALUE}.regrepl("oldParam", "newParam")} - will replace "oldParam" with "newParam"
           {{ITEM.VALUE}.regrepl("([^a-z])","\\\1")} - all non-letter characters will be escaped with a backslash
           {$THRESHOLD:"{{#FSNAME}.regrepl(\"\\$\",\"\")}"} - will remove a trailing backslash (for example, to replace "C:\" with "C:")
           {{ITEM.VALUE}.regrepl("_v1\.0", "_v2.0", "\(final\)", "")} - will replace multiple parts in item value

Copy

✔ Copied

##### regsub(pattern,output)

Substring extraction by a regular expression match (case-sensitive).

Parameters:

  * **pattern** \- the regular expression to match;
  * **output** \- the output options. **\1 - \9** placeholders are supported to capture groups. **\0** returns the matched text.

Comments:

  * If there is no match for the regular expression, the function returns an empty string.
  * If the function pattern is an incorrect regular expression, then the macro evaluates to 'UNKNOWN' (except for low-level discovery macros, in which case the function will be ignored, and the macro will remain unresolved).
  * References to non-existent capture groups in the replacement string are replaced with an empty string.

Examples:
    
    
    {{ITEM.VALUE}.regsub("^([0-9]+)", Problem ID: \1)} - will resolve to "Problem ID: 123" if a value like "123 Log line" is received
           {{ITEM.VALUE}.regsub("fail|error|fault|problem","ERROR")} - will resolve to "ERROR" if "fail", "error", "fault", or "problem" substrings are received (case-sensitive); will return an empty string if there is no match

Copy

✔ Copied

See more examples.

##### tr(characters,replacement)

Transliteration of macro value characters.

  * **characters** \- the set of characters to replace;
  * **replacement** \- the set of positionally corresponding replacement characters.

Examples:
    
    
    {{ITEM.VALUE}.tr(abc, xyz)} - will replace all occurrences of "a" with "x", "b" with "y", "c" with "z"
           {{ITEM.VALUE}.tr(abc, xyzq)} - will replace all occurrences of "a" with "x", "b" with "y", "c" with "z" ("q" is ignored)
           {{ITEM.VALUE}.tr(abcde, xyz)} - will replace all occurrences of "a" with "x", "b" with "y", "c" with "z", "d" with "z", "e" with "z" (i.e. xyzzz)
           {{ITEM.VALUE}.tr("\\\'", "\/\"")} - will replace all occurrences of backslash with forward slash, single quotes with double quotes
           {{ITEM.VALUE}.tr(A-Z,a-z)} - will convert all letters to lowercase
           {{ITEM.VALUE}.tr(0-9a-z,*)} - will replace all numbers and lowercase letters with "*"
           {{ITEM.VALUE}.tr(0-9,ab)} - will replace all occurrences of 0 with "a", and replace all occurrences of 1, 2, 3, 4, 5, 6, 7, 8, and 9 with "b"
           {{ITEM.VALUE}.tr(0-9abcA-L,*)} - will replace all numbers, "abc" characters, and A-L range with "*"
           {{ITEM.VALUE}.tr("\n","*")} - will replace end-of-line occurrences with *
           {{ITEM.VALUE}.tr("e", "\n")} - will replace all "e" with end-of-line

Copy

✔ Copied

To include literal characters:
    
    
    backslash - must be escaped as \\
           single quote - must be escaped as \'
           double quote - must be escaped as \"

Copy

✔ Copied

Supported escape sequences with backslash:
    
    
    \\\\ => \\ - double backslash to single backslash
           \\a  => \a - alert
           \\b  => \b - backspace
           \\f  => \f - form feed
           \\n  => \n - newline
           \\r  => \r - return
           \\t  => \t - horizontal tab
           \\v  => \v - vertical tab

Copy

✔ Copied

##### uppercase

Transformation of all macro value characters into uppercase. Works with single-byte character sets (such as ASCII) and does not support UTF-8.

Example:
    
    
    {{ITEM.VALUE}.uppercase()} - will transform a value like "Zabbix Server" into "ZABBIX SERVER" (uppercase)

Copy

✔ Copied

##### urldecode

Decoding a macro value from URL encoding.

Example:
    
    
    {{ITEM.VALUE}.urldecode()} - will URL-decode a value like "%2F" into "/"

Copy

✔ Copied

##### urlencode

Encoding a macro value into URL encoding.

Example:
    
    
    {{ITEM.VALUE}.urlencode()} - will URL-encode a character like "/" into "%2F"

Copy

✔ Copied

#### Additional examples

The table below shows more examples of using macro functions.

`{#IFALIAS}` is an [LLD macros](/documentation/current/en/manual/config/macros/lld_macros) and is only defined in low-level discovery contexts (discovery rules, prototypes and the items/triggers created from them). Using it outside LLD will leave the token unexpanded.

`{{ITEM.VALUE}.regsub(^[0-9]+, Problem)}` | `123Log line` | `Problem`  
---|---|---  
`{{ITEM.VALUE}.regsub("^([0-9]+)", "Problem")}` | `123 Log line` | `Problem`  
`{{ITEM.VALUE}.regsub(".*", "Problem ID: \1")}` | `Log line` | `Problem ID:`  
`{{ITEM.VALUE}.regsub("^(\w+).*?([0-9]+)", " Problem ID: \1_\2 ")}` | `MySQL crashed errno 123` | `Problem ID: MySQL_123 `  
`{{ITEM.VALUE}.regsub("([1-9]+", "Problem ID: \1")}` | `123 Log line` | `*UNKNOWN*` (invalid regular expression)  
`{{#IFALIAS}.regsub("(.*)_([0-9]+)", \1)}` | `customername_1` | `customername`  
`{{#IFALIAS}.regsub("(.*)_([0-9]+)", \2)}` | `customername_1` | `1`  
`{{#IFALIAS}.regsub("(.*)_([0-9]+", \1)}` | `customername_1` | `{{#IFALIAS}.regsub("(.*)_([0-9]+", \1)}` (invalid regular expression)  
`{$MACRO:"{{#IFALIAS}.regsub(\"(.*)_([0-9]+)\", \1)}"}` | `customername_1` | `{$MACRO:"customername"}`  
`{$MACRO:"{{#IFALIAS}.regsub(\"(.*)_([0-9]+)\", \2)}"}` | `customername_1` | `{$MACRO:"1"}`  
`{$MACRO:"{{#IFALIAS}.regsub(\"(.*)_([0-9]+\", \1)}"}` | `customername_1` | `{$MACRO:"{{#IFALIAS}.regsub(\"(.*)_([0-9]+\", \1)}"}` (invalid regular expression)  
`"{$MACRO:"\{{#IFALIAS}.regsub("(.*)_([0-9]+)", \1)}\"}"` | `customername_1` | `"{$MACRO:"\customername\"}"`  
`"{$MACRO:"\{{#IFALIAS}.regsub("(.*)_([0-9]+)", \2)}\"}"` | `customername_1` | `"{$MACRO:"\1\"}"`  
`"{$MACRO:\"{{#IFALIAS}.regsub(\\"(.*)_([0-9]+\\", \1)}\"}"` | `customername_1` | `"{$MACRO:\"{{#IFALIAS}.regsub(\\"(.*)_([0-9]+\\", \1)}\"}"` (invalid regular expression)  
  
##### Seeing full item values

Long values of resolved {ITEM.VALUE} and {ITEM.LASTVALUE} macros for text/log items are truncated to 20 characters in some frontend locations. To see the full values of these macros you may use macro functions, e.g.:
    
    
    {{ITEM.VALUE}.regsub("(.*)", \1)}
           {{ITEM.LASTVALUE}.regsub("(.*)", \1)}

Copy

✔ Copied

See also: {ITEM.VALUE} and {ITEM.LASTVALUE} [macro details](/documentation/current/en/manual/appendix/macros/supported_by_location).