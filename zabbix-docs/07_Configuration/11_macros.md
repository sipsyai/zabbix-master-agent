---
title: Macros
source: https://www.zabbix.com/documentation/current/en/manual/config/macros
downloaded: 2025-11-14 10:36:29
---

# 11 Macros

#### Overview

Zabbix supports a number of built-in macros which may be used in various situations. These macros are variables, identified by a specific syntax:
    
    
    {MACRO} 

Copy

✔ Copied

Macros resolve to a specific value depending on the context.

Effective use of macros allows to save time and make Zabbix configuration more transparent.

In one of typical uses, a macro may be used in a template. Thus a trigger on a template may be named "Processor load is too high on {HOST.NAME}". When the template is applied to the host, such as Zabbix server, the name will resolve to "Processor load is too high on Zabbix server" when the trigger is displayed in the Monitoring section.

Macros may be used in item key parameters. A macro may be used for only a part of the parameter, for example `item.key[server_{HOST.HOST}_local]`. Double-quoting the parameter is not necessary as Zabbix will take care of any ambiguous special symbols, if present in the resolved macro.

There are other types of macros in Zabbix.

Zabbix supports the following macros:

  * `{MACRO}` \- built-in macro (see [full list](/documentation/current/en/manual/appendix/macros/supported_by_location))
  * `{<macro>.<func>(<params>)}` \- macro [functions](/documentation/current/en/manual/config/macros/macro_functions)
  * `{$MACRO}` \- [user-defined macro](/documentation/current/en/manual/config/macros/user_macros), optionally [with context](/documentation/current/en/manual/config/macros/user_macros_context)
  * `{#MACRO}` \- macro for [low-level discovery](/documentation/current/en/manual/config/macros/lld_macros)
  * `{?EXPRESSION}` \- [expression macro](/documentation/current/en/manual/config/macros/expression_macros)