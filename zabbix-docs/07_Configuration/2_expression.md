---
title: Trigger expression
source: https://www.zabbix.com/documentation/current/en/manual/config/triggers/expression
downloaded: 2025-11-14 10:35:33
---

# 2 Trigger expression

#### Overview

The expressions used in [triggers](/documentation/current/en/manual/config/triggers) are very flexible. You can use them to create complex logical tests regarding monitored statistics.

A simple expression uses a **function** that is applied to the item with some parameters. The function returns a result that is compared to the threshold, using an operator and a constant.

The syntax of a simple useful expression is `function(/host/key,parameter)<operator><constant>`.

For example:
    
    
    min(/Zabbix server/net.if.in[eth0,bytes],5m)>100K

Copy

✔ Copied

will trigger if the number of received bytes during the last five minutes was always over 100 kilobytes.

While the syntax is exactly the same, from the functional point of view there are two types of trigger expressions:

  * problem expression - defines the conditions of the problem
  * recovery expression (optional) - defines additional conditions of the problem resolution

When defining a problem expression alone, this expression will be used both as the problem threshold and the problem recovery threshold. As soon as the problem expression evaluates to TRUE, there is a problem. As soon as the problem expression evaluates to FALSE, the problem is resolved.

When defining both problem expression and the supplemental recovery expression, problem resolution becomes more complex: not only the problem expression has to be FALSE, but also the recovery expression has to be TRUE. This is useful to create hysteresis and avoid trigger flapping.

It is unproductive to use the {TRIGGER.VALUE} macro in a recovery expression because this expression is only evaluated when the trigger is in the "Problem" state.Consequently, {TRIGGER.VALUE} will always resolve to "1" (which indicates a "Problem" state) while evaluating the expression.

#### Functions

Functions allow to calculate the collected values (average, minimum, maximum, sum), find strings, reference current time and other factors.

A complete list of [supported functions](/documentation/current/en/manual/appendix/functions) is available.

Typically functions return numeric values for comparison. When returning strings, comparison is possible with the **=** and **< >** operators (see example).

#### Function parameters

Function parameters allow to specify:

  * host and item key (functions referencing the host item history only)
  * function-specific parameters
  * other expressions (not available for functions referencing the host item history, see other expressions for examples)

The host and item key can be specified as `/host/key`.  
Omission of the host name in the first parameter (i.e. as in `function(//key,parameter,...)`) is only supported in certain contexts:

  * In the formula of calculated items
  * In expression macros, which can be used in: 
    * The [_Event name_](/documentation/current/en/manual/config/triggers/trigger#configuration) field
    * Graph name
    * The label of "Host" and "Trigger" [map elements](/documentation/current/en/manual/config/visualization/maps/map#adding-elements)

In these contexts, you may also use the [`{HOST.HOST}`](/documentation/current/en/manual/appendix/macros/supported_by_location#hosthost) macro. `{HOST.HOST<1-9>}` could be used in the case of the _Event name_ field and the "Trigger" map element to refer to a specific item in the trigger expression. When the host name is omitted or replaced by `{HOST.HOST}` in these contexts, the reference points to the first item in the trigger expression or to the first item in the graph. Outside of these supported contexts, omitting the host name in trigger expressions will result in an error. See Example 18 for an illustration of double-slash usage in Event name macros.

The referenced item must be in a supported state (except for **nodata()** function, which is calculated for unsupported items as well).

While other trigger expressions as function parameters are limited to non-history functions in triggers, this limitation does not apply in [calculated items](/documentation/current/en/manual/config/items/itemtypes/calculated).

##### Function-specific parameters

Function-specific parameters are placed after the item key and are separated from the item key by a comma. See the [supported functions](/documentation/current/en/manual/appendix/functions) for a complete list of these parameters.

Most of numeric functions accept time as a parameter. You may use seconds or [time suffixes](/documentation/current/en/manual/appendix/suffixes) to indicate time. Preceded by a hash mark, the parameter has a different meaning:

**sum**(/host/key,**10m)** | Sum of values in the last 10 minutes.  
---|---  
**sum**(/host/key,**#10)** | Sum of the last ten values.  
  
Parameters with a hash mark have a different meaning with the function **last** \- they denote the Nth previous value, so given the values 30, 70, 20, 60, 50 (from the most recent to the least recent):

  * `last(/host/key,#2)` would return '70'
  * `last(/host/key,#5)` would return '50'

##### Time shift

An optional time shift is supported with time or value count as the function parameter. This parameter allows to reference data from a period of time in the past.

Time shift starts with `now` \- specifying the current time, and is followed by `+N<time unit>` or `-N<time unit>` \- to add or subtract N time units.

For example, `avg(/host/key,1h:now-1d)` will return the average value for an hour one day ago.

Time shift specified in months (M) and years (y) is only supported for [trend functions](/documentation/current/en/manual/appendix/functions/trends). Other functions support seconds (s), minutes (m), hours (h), days (d), and weeks (w).

**Time shift with absolute time periods**

Absolute time periods are supported in the time shift parameter, for example, midnight to midnight for a day, Monday-Sunday for a week, first day-last day of the month for a month.

Time shift for absolute time periods starts with `now` \- specifying the current time, and is followed by any number of time operations: `/<time unit>` \- defines the beginning and end of the time unit, for example, midnight to midnight for a day, `+N<time unit>` or `-N<time unit>` \- to add or subtract N time units.

Please note that the value of time shift can be greater or equal to 0, while the time period minimum value is 1.

1d:now/d | Yesterday  
---|---  
1d:now/d+1d | Today  
2d:now/d+1d | Last 2 days  
1w:now/w | Last week  
1w:now/w+1w | This week  
  
##### Other expressions

Function parameters may contain other expressions, as in the following syntax:
    
    
    min(min(/host/key,1h),min(/host2/key2,1h)*10)

Copy

✔ Copied

Note that other expressions may not be used, if the function references item history. For example, the following syntax is **not** allowed:

~~`min(/host/key,#5*10)`~~

#### Operators

The following operators are supported for triggers **(in descending priority of execution)** :

**1** | **-** | Unary minus | **-** Unknown → Unknown | Yes  
---|---|---|---|---  
**2** | **not** | Logical NOT | **not** Unknown → Unknown | Yes  
**3** | ***** | Multiplication | 0 ***** Unknown → Unknown  
(yes, Unknown, not 0 - to not lose  
Unknown in arithmetic operations)  
1.2 ***** Unknown → Unknown | Yes  
| **/** | Division | Unknown **/** 0 → error  
Unknown **/** 1.2 → Unknown  
0.0 **/** Unknown → Unknown | Yes  
**4** | **+** | Arithmetical plus | 1.2 **+** Unknown → Unknown | Yes  
| **-** | Arithmetical minus | 1.2 **-** Unknown → Unknown | Yes  
**5** | **<** | Less than. The operator is defined as:  
  
A<B ⇔ (A<B-0.000001) | 1.2 **<** Unknown → Unknown | Yes  
| **< =** | Less than or equal to. The operator is defined as:  
  
A<=B ⇔ (A≤B+0.000001) | Unknown **< =** Unknown → Unknown | Yes  
| **>** | More than. The operator is defined as:  
  
A>B ⇔ (A>B+0.000001) |  | Yes  
| **> =** | More than or equal to. The operator is defined as:  
  
A>=B ⇔ (A≥B-0.000001) |  | Yes  
**6** | **=** | Is equal. The operator is defined as:  
  
A=B ⇔ (A≥B-0.000001) and (A≤B+0.000001) |  | No **1**  
| **< >** | Not equal. The operator is defined as:  
  
A<>B ⇔ (A<B-0.000001) or (A>B+0.000001) |  | No **1**  
**7** | **and** | Logical AND | 0 **and** Unknown → 0  
1 **and** Unknown → Unknown  
Unknown **and** Unknown → Unknown | Yes  
**8** | **or** | Logical OR | 1 **or** Unknown → 1  
0 **or** Unknown → Unknown  
Unknown **or** Unknown → Unknown | Yes  
  
**1** String operand is still cast to numeric if:

  * another operand is numeric
  * operator other than **=** or **< >** is used on an operand

(If the cast fails - numeric operand is cast to a string operand and both operands get compared as strings.)

**not** , **and** and **or** operators are case-sensitive and must be in lowercase. They also must be surrounded by spaces or parentheses.

All operators, except unary **-** and **not** , have left-to-right associativity. Unary **-** and **not** are non-associative (meaning **-(-1)** and **not (not 1)** should be used instead of **\--1** and **not not 1**).

Evaluation result:

  * **<** , **< =**, **>** , **> =**, **=** , **< >** operators shall yield '1' in the trigger expression if the specified relation is true and '0' if it is false. If at least one operand is Unknown the result is Unknown;
  * **and** for known operands shall yield '1' if both of its operands compare unequal to '0'; otherwise, it yields '0'; for unknown operands **and** yields '0' only if one operand compares equal to '0'; otherwise, it yields 'Unknown';
  * **or** for known operands shall yield '1' if either of its operands compare unequal to '0'; otherwise, it yields '0'; for unknown operands **or** yields '1' only if one operand compares unequal to '0'; otherwise, it yields 'Unknown';
  * The result of the logical negation operator **not** for a known operand is '0' if the value of its operand compares unequal to '0'; '1' if the value of its operand compares equal to '0'. For unknown operand **not** yields 'Unknown'.

#### Value caching

Values required for trigger evaluation are cached by Zabbix server. Because of this trigger evaluation causes a higher database load for some time after the server restarts. The value cache is not cleared when item history values are removed (either manually or by housekeeper), so the server will use the cached values until they are older than the time periods defined in trigger functions or server is restarted.

If there is no recent data in the cache and there is no defined querying period in the function, Zabbix will by default go as far back in the past as one week to query the database for historical values.

#### Examples of triggers

##### Example 1

The processor load is too high on Zabbix server.
    
    
    last(/Zabbix server/system.cpu.load[all,avg1])>5

Copy

✔ Copied

By using the function 'last()', we are referencing the most recent value. `/Zabbix server/system.cpu.load[all,avg1]` gives a short name of the monitored parameter. It specifies that the host is 'Zabbix server' and the key being monitored is 'system.cpu.load[all,avg1]'. Finally, `>5` means that the trigger is in the PROBLEM state whenever the most recent processor load measurement from Zabbix server is greater than 5.

##### Example 2

www.example.com is overloaded.
    
    
    last(/www.example.com/system.cpu.load[all,avg1])>5 or min(/www.example.com/system.cpu.load[all,avg1],10m)>2 

Copy

✔ Copied

The expression is true when either the current processor load is more than 5 or the processor load was more than 2 during last 10 minutes.

##### Example 3

/etc/passwd has been changed.
    
    
    last(/www.example.com/vfs.file.cksum[/etc/passwd],#1)<>last(/www.example.com/vfs.file.cksum[/etc/passwd],#2)

Copy

✔ Copied

The expression is true when the previous value of /etc/passwd checksum differs from the most recent one.

Similar expressions could be useful to monitor changes in important files, such as /etc/passwd, /etc/inetd.conf, /kernel, etc.

##### Example 4

Someone is downloading a large file from the Internet.

Use of function min:
    
    
    min(/www.example.com/net.if.in[eth0,bytes],5m)>100K

Copy

✔ Copied

The expression is true when number of received bytes on eth0 is more than 100 KB within last 5 minutes.

##### Example 5

Both nodes of clustered SMTP server are down.

Note use of two different hosts in one expression:
    
    
    last(/smtp1.example.com/net.tcp.service[smtp])=0 and last(/smtp2.example.com/net.tcp.service[smtp])=0

Copy

✔ Copied

The expression is true when both SMTP servers are down on both smtp1.example.com and smtp2.example.com.

##### Example 6

Zabbix agent needs to be upgraded.

Use of function find():
    
    
    find(/example.example.com/agent.version,,"like","beta8")=1

Copy

✔ Copied

The expression is true if Zabbix agent has version beta8.

##### Example 7

Server is unreachable.
    
    
    count(/example.example.com/icmpping,30m,,"0")>5

Copy

✔ Copied

The expression is true if host "example.example.com" is unreachable more than 5 times in the last 30 minutes.

##### Example 8

No heartbeats within last 3 minutes.

Use of function nodata():
    
    
    nodata(/example.example.com/tick,3m)=1

Copy

✔ Copied

To make use of this trigger, 'tick' must be defined as a Zabbix [trapper](/documentation/current/en/manual/config/items/itemtypes/trapper) item. The host should periodically send data for this item using zabbix_sender. If no data is received within 180 seconds, the trigger value becomes PROBLEM.

_Note_ that 'nodata' can be used for any item type.

##### Example 9

CPU activity at night time.

Use of function time():
    
    
    min(/Zabbix server/system.cpu.load[all,avg1],5m)>2 and time()<060000

Copy

✔ Copied

The trigger may change its state to problem only at night time (00:00 - 06:00).

##### Example 10

CPU activity at any time with exception.

Use of function time() and **not** operator:
    
    
    min(/zabbix/system.cpu.load[all,avg1],5m)>2
           and not (dayofweek()=7 and time()>230000)
           and not (dayofweek()=1 and time()<010000)

Copy

✔ Copied

The trigger may change its state to problem at any time, except for 2 hours on a week change (Sunday, 23:00 - Monday, 01:00).

##### Example 11

Check if client local time is in sync with Zabbix server time.

Use of function fuzzytime():
    
    
    fuzzytime(/MySQL_DB/system.localtime,10s)=0

Copy

✔ Copied

The trigger will change to the problem state in case when local time on server MySQL_DB and Zabbix server differs by more than 10 seconds. Note that 'system.localtime' must be configured as a [passive check](/documentation/current/en/manual/appendix/items/activepassive#passive-checks).

##### Example 12

Comparing average load today with average load of the same time yesterday (using time shift as `now-1d`).
    
    
    avg(/server/system.cpu.load,1h)/avg(/server/system.cpu.load,1h:now-1d)>2

Copy

✔ Copied

The trigger will fire if the average load of the last hour tops the average load of the same hour yesterday more than two times.

##### Example 13

Using the value of another item to get a trigger threshold:
    
    
    last(/Template PfSense/hrStorageFree[{#SNMPVALUE}])<last(/Template PfSense/hrStorageSize[{#SNMPVALUE}])*0.1

Copy

✔ Copied

The trigger will fire if the free storage drops below 10 percent.

##### Example 14

Using evaluation result to get the number of triggers over a threshold:
    
    
    (last(/server1/system.cpu.load[all,avg1])>5) + (last(/server2/system.cpu.load[all,avg1])>5) + (last(/server3/system.cpu.load[all,avg1])>5)>=2

Copy

✔ Copied

The trigger will fire if at least two of the triggers in the expression are in a problem state.

##### Example 15

Comparing string values of two items - operands here are functions that return strings.

Problem: create an alert if Ubuntu version is different on different hosts
    
    
    last(/NY Zabbix server/vfs.file.contents[/etc/os-release])<>last(/LA Zabbix server/vfs.file.contents[/etc/os-release])

Copy

✔ Copied

##### Example 16

Comparing two string values - operands are:

  * a function that returns a string
  * a combination of macros and strings

Problem: detect changes in the DNS query

The item key is:
    
    
    net.dns.record[192.0.2.0,{$WEBSITE_NAME},{$DNS_RESOURCE_RECORD_TYPE},2,1]

Copy

✔ Copied

with macros defined as
    
    
    {$WEBSITE_NAME} = example.com
           {$DNS_RESOURCE_RECORD_TYPE} = MX

Copy

✔ Copied

and normally returns:
    
    
    example.com           MX       0 mail.example.com

Copy

✔ Copied

So our trigger expression to detect if the DNS query result deviated from the expected result is:
    
    
    last(/Zabbix server/net.dns.record[192.0.2.0,{$WEBSITE_NAME},{$DNS_RESOURCE_RECORD_TYPE},2,1])<>"{$WEBSITE_NAME}           {$DNS_RESOURCE_RECORD_TYPE}       0 mail.{$WEBSITE_NAME}"

Copy

✔ Copied

Notice the quotes around the second operand.

##### Example 17

Comparing two string values - operands are:

  * a function that returns a string
  * a string constant with special characters \ and "

Problem: detect if the `/tmp/hello` file content is equal to:
    
    
    \" //hello ?\"

Copy

✔ Copied

Option 1) write the string directly:
    
    
    last(/Zabbix server/vfs.file.contents[/tmp/hello])="\\\" //hello ?\\\""

Copy

✔ Copied

Notice how \ and " characters are escaped when the string gets compared directly.

Option 2) use a macro
    
    
    {$HELLO_MACRO} = \" //hello ?\"

Copy

✔ Copied

in the expression:
    
    
    last(/Zabbix server/vfs.file.contents[/tmp/hello])={$HELLO_MACRO}

Copy

✔ Copied

##### Example 18

Comparing long-term periods.

Problem: Load of Exchange server increased by more than 10% last month
    
    
    trendavg(/Exchange/system.cpu.load,1M:now/M)>1.1*trendavg(/Exchange/system.cpu.load,1M:now/M-1M)

Copy

✔ Copied

You may also use the [Event name](/documentation/current/en/manual/config/triggers/trigger#configuration) field in trigger configuration to build a meaningful alert message, for example to receive something like

`"Load of Exchange server increased by 24% in July (0.69) comparing to June (0.56)"`

the event name must be defined as:
    
    
    Load of {HOST.HOST} server increased by {{?100*trendavg(//system.cpu.load,1M:now/M)/trendavg(//system.cpu.load,1M:now/M-1M)}.fmtnum(0)}% in {{TIME}.fmttime(%B,-1M)} ({{?trendavg(//system.cpu.load,1M:now/M)}.fmtnum(2)}) comparing to {{TIME}.fmttime(%B,-2M)} ({{?trendavg(//system.cpu.load,1M:now/M-1M)}.fmtnum(2)})

Copy

✔ Copied

It is also useful to allow manual closing in trigger configuration for this kind of problem.

Have a trigger expressions example that might be useful to others? Use the Example suggestion form to send it to Zabbix developers.

#### Hysteresis

Sometimes an interval is needed between problem and recovery states, rather than a simple threshold. For example, if we want to define a trigger that reports a problem when server room temperature goes above 20°C and we want it to stay in the problem state until the temperature drops below 15°C, a simple trigger threshold at 20°C will not be enough.

Instead, we need to define a trigger expression for the problem event first (temperature above 20°C). Then we need to define an additional recovery condition (temperature below 15°C). This is done by defining an additional _Recovery expression_ parameter when [defining](/documentation/current/en/manual/config/triggers/trigger) a trigger.

In this case, problem recovery will take place in two steps:

  * First, the problem expression (temperature above 20°C) will have to evaluate to FALSE
  * Second, the recovery expression (temperature below 15°C) will have to evaluate to TRUE

The recovery expression will be evaluated only when the problem event is resolved first.

The recovery expression being TRUE alone does not resolve a problem if the problem expression is still TRUE!

##### Example 1

Temperature in server room is too high.

Problem expression:
    
    
    last(/server/temp)>20

Copy

✔ Copied

Recovery expression:
    
    
    last(/server/temp)<=15

Copy

✔ Copied

##### Example 2

Free disk space is too low.

Problem expression: it is less than 10GB for last 5 minutes
    
    
    max(/server/vfs.fs.size[/,free],5m)<10G

Copy

✔ Copied

Recovery expression: it is more than 40GB for last 10 minutes
    
    
    min(/server/vfs.fs.size[/,free],10m)>40G

Copy

✔ Copied

#### Expressions with unknown operands

Generally an unknown operand (such as an unsupported item) in the expression will immediately render the trigger value to `Unknown`.

However, in some cases unknown operands (unsupported items, function errors) are admitted into expression evaluation:

  * The `nodata()` function is evaluated regardless of whether the referenced item is supported or not.
  * Logical expressions with OR and AND can be evaluated to known values in two cases regardless of unknown operands: 
    * **Case 1** : "`1 or some_function(unsupported_item1) or some_function(unsupported_item2) or ...`" can be evaluated to known result ('1' or "Problem"),
    * **Case 2** : "`0 and some_function(unsupported_item1) and some_function(unsupported_item2) and ...`" can be evaluated to known result ('0' or "OK").  
Zabbix tries to evaluate such logical expressions by taking unsupported items as unknown operands. In the two cases above a known value will be produced ("Problem" or "OK", respectively); in **all other** cases the trigger will evaluate to `Unknown`.
  * If the function evaluation for a supported item results in error, the function value becomes `Unknown` and it takes part as unknown operand in further expression evaluation.

Note that unknown operands may "disappear" only in logical expressions as described above. In arithmetic expressions unknown operands always lead to the result `Unknown` (except division by 0).

An expression that results in `Unknown` does not change the trigger state ("Problem/OK"). So, if it was "Problem" (see Case 1), it stays in the same problem state even if the known part is resolved ('1' becomes '0'), because the expression is now evaluated to `Unknown` and that does not change the trigger state.

If a trigger expression with several unsupported items evaluates to `Unknown` the error message in the frontend refers to the last unsupported item evaluated.