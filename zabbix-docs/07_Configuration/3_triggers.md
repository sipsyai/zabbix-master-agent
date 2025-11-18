---
title: Triggers
source: https://www.zabbix.com/documentation/current/en/manual/config/triggers
downloaded: 2025-11-14 10:35:31
---

# 3 Triggers

#### Overview

Triggers are logical expressions that "evaluate" data gathered by items and represent the current system state.

While items are used to gather system data, it is highly impractical to follow these data all the time waiting for a condition that is alarming or deserves attention. The job of "evaluating" data can be left to trigger expressions.

Trigger expressions allow to define a threshold of what state of data is "acceptable". Therefore, should the incoming data surpass the acceptable state, a trigger is "fired" - or changes its status to PROBLEM.

A trigger may have the following status:

OK | This is a normal trigger status.  
---|---  
Problem | Something has happened. For example, the processor load is too high.  
Unknown | The trigger value cannot be calculated. See Unknown status.  
  
In a simple trigger we may want to set a threshold for a five-minute average of some data, for example, the CPU load. This is accomplished by defining a trigger expression where:

  * the 'avg' function is applied to the value received in the item key
  * a five minute period for evaluation is used
  * a threshold of '2' is set

    
    
        avg(/host/key,5m)>2

This trigger will "fire" (become PROBLEM) if the five-minute average is _over_ 2.

In a more complex trigger, the expression may include a **combination** of multiple functions and multiple thresholds. See also: [Trigger expression](/documentation/current/en/manual/config/triggers/expression).

Triggers cannot be created for items with binary values.

After enabling a trigger (changing its configuration status from _Disabled_ to _Enabled_), the trigger expression is evaluated as soon as an item in it receives a value or the time to handle [date and time](/documentation/current/en/manual/appendix/functions/time) and/or [nodata()](/documentation/current/en/manual/appendix/functions/history#nodata) functions comes.

Most trigger functions are evaluated based on item value [history](/documentation/current/en/manual/config/items/history_and_trends) data, while some trigger functions for long-term analytics, e.g. **trendavg()** , **trendcount()** , etc, use trend data.

#### Calculation time

A trigger is recalculated every time Zabbix server receives a new value that is part of the expression. When a new value is received, each function that is included in the expression is recalculated (not just the one that received the new value).

Additionally, a trigger is recalculated each time when a new value is received **and** every 30 seconds if [date and time](/documentation/current/en/manual/appendix/functions/time) and/or [nodata()](/documentation/current/en/manual/appendix/functions/history#nodata) functions are used in the expression.

[Date and time](/documentation/current/en/manual/appendix/functions/time) and/or [nodata()](/documentation/current/en/manual/appendix/functions/history#nodata) functions are recalculated every 30 seconds by the Zabbix history syncer process.

Triggers that reference trend functions **only** are evaluated once per the smallest time period in the expression. See also [trend functions](/documentation/current/en/manual/appendix/functions/trends).

#### Evaluation period

An evaluation period is used in functions referencing the item history. It allows to specify the interval we are interested in. It can be specified as time period (30s, 10m, 1h) or as a value range (#5 - for five latest values).

The evaluation period is measured up to "now" - where "now" is the latest recalculation time of the trigger (see Calculation time above); "now" is not the "now" time of the server.

The evaluation period specifies either:

  * To consider all values between "now-time period" and "now" (or, with time shift, between "now-time shift-time period" and "now-time_shift")
  * To consider no more than the num count of values from the past, up to "now" 
    * If there are 0 available values for the time period or num count specified - then the trigger or calculated item that uses this function becomes unsupported

Note that:

  * If only a single function (referencing data history) is used in the trigger, "now" is always the latest received value. For example, if the last value was received an hour ago, the evaluation period will be regarded as up to the latest value an hour ago.
  * A new trigger is calculated as soon as the first value is received (history functions); it will be calculated within 30 seconds for [date and time](/documentation/current/en/manual/appendix/functions/time) and [nodata()](/documentation/current/en/manual/appendix/functions/history#nodata) functions. Thus the trigger will be calculated even though perhaps the set evaluation period (for example, one hour) has not yet passed since the trigger was created. The trigger will also be calculated after the first value, even though the evaluation range was set, for example, to ten latest values.

#### Unknown status

It is possible that an unknown operand appears in a trigger expression if:

  * an unsupported item is used
  * the function evaluation for a supported item results in an error

In this case a trigger generally evaluates to "unknown" (although there are some exceptions). For more details, see [Expressions with unknown operands](/documentation/current/en/manual/config/triggers/expression#expressions-with-unknown-operands).

It is possible to [get notified](/documentation/current/en/manual/config/events/sources#internal-events) on unknown triggers.