---
title: Expression macros
source: https://www.zabbix.com/documentation/current/en/manual/config/macros/expression_macros
downloaded: 2025-11-14 10:36:34
---

# 6 Expression macros

#### Overview

Expression macros let you perform calculations in fields.

Their value is calculated by first resolving any inner macros and then evaluating the resulting expression.

Syntax:
    
    
    {?EXPRESSION}

Copy

✔ Copied

`EXPRESSION` uses the same syntax and supports the same [functions](/documentation/current/en/manual/appendix/functions) as [trigger expressions](/documentation/current/en/manual/config/triggers/expression).

Example:
    
    
    {?trendavg(/host/item1,1M:now/M)/trendavg(/host/item1,1M:now/M-1y)*100}

Copy

✔ Copied

For supported locations, see [Supported macros](/documentation/current/en/manual/appendix/macros/supported_by_location).

Notes on usage:

  * Use [{FUNCTION.*}](/documentation/current/en/manual/appendix/macros/supported_by_location#function-macros) macros to reference function values of trigger expressions/recovery expressions.
  * Use [{HOST.HOST<1-9>}](/documentation/current/en/manual/appendix/macros/supported_by_location#hosthost) and [{ITEM.KEY<1-9>}](/documentation/current/en/manual/appendix/macros/supported_by_location#itemkey) macros to reference hosts and items.
  * In templates, use [{HOST.HOST<1-9>}](/documentation/current/en/manual/appendix/macros/supported_by_location#hosthost) macros or omit the host altogether for the first host—for example, `{?avg(//item1,1h)}`—instead of template names, as template names are not replaced with host names during [template linking](/documentation/current/en/manual/config/templates/linking).

    
    
    {?{FUNCTION.VALUE2} - {FUNCTION.VALUE3}}
           {?max(/{HOST.HOST}/{ITEM.KEY},3h)}

Copy

✔ Copied

See also [Trigger expression examples](/documentation/current/en/manual/config/triggers/expression#example-18) for an example of using an expression macro in an event name.