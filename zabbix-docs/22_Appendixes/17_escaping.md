---
title: Escaping examples
source: https://www.zabbix.com/documentation/current/en/manual/appendix/escaping
downloaded: 2025-11-14 10:48:01
---

# 17 Escaping examples

#### Overview

This page provides examples of using correct escaping when using regular expressions in various contexts.

When using the trigger expression constructor, correct escaping in regular expressions is added automatically.

#### Examples

**User macro with context**

Regular expression: `\.+\"[a-z]+`  
User macro with context: `{$MACRO:regex:"\.+\\"[a-z]+"}`

Notice:

  * backslashes are [not escaped](/documentation/current/en/manual/config/macros/user_macros_context#important-notes);
  * quotation marks are escaped.

**Macro function inside item key parameter**

Regular expression: `.+:(\d+)$`  
Item key: `net.tcp.service[tcp,,"{{$ENDPOINT}.regsub(\".+:(\d+)$\",\1)}"]`

Notice:

  * regular expression inside the `regsub` macro function is double-quoted (because of contains closing parenthesis);
  * quotation marks around the regular expression are escaped (because the whole third item parameter is double-quoted);
  * third item key parameter is double-quoted because it contains a comma.

**LLD macro function**

Regular expression: `\.+\"([a-z]+)`  
LLD macro: `{{#MACRO}.iregsub("\.+\\"([a-z]+)", \1)}`

Notice:

  * backslashes are not escaped;
  * quotation marks are escaped.

**LLD macro function inside user macro context**

Regular expression: `\.+\"([a-z]+)`  
LLD macro: `{{#MACRO}.iregsub("\.+\\"([a-z]+)", \1)}`  
User macro with context: `{$MACRO:"{{#MACRO}.iregsub(\"\.+\\\"[a-z]+\", \1)}"}`

Notice:

  * backslash escaping for LLD does not change;
  * upon inserting the LLD macro into user macro context, we need to put it into string:

  1. Quotation marks are added around the macro expression;
  2. Quotation marks get escaped; in total, 3 new backslashes are introduced.

**String parameter of function (any)**

`concat` is used as example.

String content: `\.+\"[a-z]+`  
Expression: `concat("abc", "\\.\\\"[a-z]+")`

Notice:

  * String parameters require escaping both for backslashes and quotation marks.

**LLD macro function inside string parameter of function**

Regular expression: `\.+\"([a-z]+)`  
LLD macro: `{{#MACRO}.iregsub("\.+\\"([a-z]+)", \1)}`  
Expression: `concat("abc, "{{#MACRO}.iregsub(\"\\.+\\\\\"([a-z]+)\", \\1)}")`

Notice:

  * String parameters require escaping both for backslashes and quotation marks;
  * Another layer of escaping is added, because the macro will be resolved only after string is unquoted;

**User macro with context inside string parameter of function**

Regular expression: `\.+\"[a-z]+`  
User macro with context: `{$MACRO:regex:"\.+\\"[a-z]+"}`  
Expression: `concat("abc, "{$MACRO:regex:\"\\.+\\\\\"[a-z]+\"}")`

Notice:

  * Same as in the previous example an additional layer of escaping is needed;
  * Backslashes and quotation marks are escaped only for the top-level escaping (by virtue of it being a string parameter).

**LLD macro function inside user macro context inside function**

Regular expression: `\.+\"([a-z])+`  
LLD macro: `{{#MACRO}.iregsub("\.+\\"([a-z]+)", \1)}`  
User macro with context: `{$MACRO:"{{#MACRO}.iregsub(\"\.+\\\"([a-z]+)\", \1)}"}`  
Expression: `concat("abc, "{$MACRO:\"{{#MACRO}.iregsub(\\\"\.+\\\\\\\"([a-z]+)\\\", \\1)}\"}")`

Notice the three layers of escaping:

  1. For LLD macro function, without escaping of backslashes;
  2. For User macro with context, without escaping of backslashes;
  3. For the string parameter of a function, with escaping of backslashes.

**User macro with context just inside string**

Regular expression: `\.+\"[a-z]+`  
User macro with context: `{$MACRO:regex:"\.+\\"[a-z]+"}`  
Inside string of some expression, for example: `func(arg1, arg2, arg3)="{$MACRO:regex:\"\\.+\\\\\"[a-z]+\"}"`

Notice:

  * Strings also require backslash escaping;
  * Strings also require quotation mark escaping;
  * Again a case with 2 levels of escaping: 
    1. Escaping for user macro context without backslash escaping;
    2. Escaping for it being a string with backslash escaping.