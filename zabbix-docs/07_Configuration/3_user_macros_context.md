---
title: User macros with context
source: https://www.zabbix.com/documentation/current/en/manual/config/macros/user_macros_context
downloaded: 2025-11-14 10:36:31
---

# 3 User macros with context

#### Overview

An optional context can be used in [user macros](/documentation/current/en/manual/config/macros/user_macros), allowing to override the default value with a context-specific one.

The context is appended to the macro name; the syntax depends on whether the context is a static text value:
    
    
    {$MACRO:"static text"}

Copy

✔ Copied

or a regular expression:
    
    
    {$MACRO:regex:"regular expression"} 

Copy

✔ Copied

Note that a macro with regular expression context can only be defined in user macro configuration. If the `regex:` prefix is used elsewhere as user macro context, like in a trigger expression, it will be treated as static context.

Context quoting is optional (see also important notes).

Macro context examples:

`{$LOW_SPACE_LIMIT}` | User macro without context.  
---|---  
`{$LOW_SPACE_LIMIT:/tmp}` | User macro with context (static string).  
`{$LOW_SPACE_LIMIT:regex:"^/tmp$"}` | User macro with context (regular expression). Same as `{$LOW_SPACE_LIMIT:/tmp}`.  
`{$LOW_SPACE_LIMIT:regex:"^/var/log/.*$"}` | User macro with context (regular expression). Matches all strings prefixed with /var/log/.  
  
#### Use cases

User macros with context can be defined to accomplish more flexible thresholds in trigger expressions (based on the values retrieved by low-level discovery). For example, you may define the following macros:

  * {$LOW_SPACE_LIMIT} = 10
  * {$LOW_SPACE_LIMIT:/home} = 20
  * {$LOW_SPACE_LIMIT:regex:"^/[a-z]+$"} = 30

Then a low-level discovery macro may be used as macro context in a trigger prototype for mounted file system discovery:
    
    
    last(/host/vfs.fs.size[{#FSNAME},pfree])<{$LOW_SPACE_LIMIT:"{#FSNAME}"}

Copy

✔ Copied

After the discovery different low-space thresholds will apply in triggers depending on the discovered mount points or file system types. Problem events will be generated if:

  * /home folder has less than 20% of free disk space
  * folders that match the regexp pattern (like /etc, /tmp or /var) have less than 30% of free disk space
  * folders that don't match the regexp pattern and are not /home have less than 10% of free disk space

#### Important notes

  * If more than one user macro with context exists, Zabbix will try to match the simple context macros first and then context macros with regular expressions in an undefined order.

Do not create different context macros matching the same string to avoid undefined behavior.

  * If a macro with its context is not found on host, linked templates or globally, then the macro without context is searched for.
  * Only low-level discovery macros are supported in the context. Any other macros are ignored and treated as plain text.

Technically, macro context is specified using rules similar to [item key](/documentation/current/en/manual/config/items/item/key) parameters, except macro context is not parsed as several parameters if there is a `,` character:

  * Macro context must be quoted with `"` if the context contains a `}` character or starts with a `"` character. Quotes inside quoted context must be escaped with the `\` character.
  * The `\` character itself is not escaped, which means it's impossible to have a quoted context ending with the `\` character - the macro {$MACRO:"a:\b\c\"} is invalid.
  * The leading spaces in context are ignored, the trailing spaces are not: 
    * For example {$MACRO:A} is the same as {$MACRO: A}, but not {$MACRO:A }.
  * All spaces before leading quotes and after trailing quotes are ignored, but all spaces inside quotes are not: 
    * Macros {$MACRO:"A"}, {$MACRO: "A"}, {$MACRO:"A" } and {$MACRO: "A" } are the same, but macros {$MACRO:"A"} and {$MACRO:" A "} are not.

The following macros are all equivalent, because they have the same context: {$MACRO:A}, {$MACRO: A} and {$MACRO:"A"}. This is in contrast with item keys, where 'key[a]', 'key[ a]' and 'key["a"]' are the same semantically, but different for uniqueness purposes.