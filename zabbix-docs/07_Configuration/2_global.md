---
title: Global event correlation
source: https://www.zabbix.com/documentation/current/en/manual/config/event_correlation/global
downloaded: 2025-11-14 10:35:44
---

# 2 Global event correlation

#### Overview

Global event correlation allows to reach out over all metrics monitored by Zabbix and create correlations.

It is possible to correlate events created by completely different triggers and apply the same operations to them all. By creating intelligent correlation rules it is actually possible to save yourself from thousands of repetitive notifications and focus on root causes of a problem!

Global event correlation is a powerful mechanism, which allows you to untie yourself from one-trigger based problem and resolution logic. So far, a single problem event was created by one trigger and we were dependent on that same trigger for the problem resolution. We could not resolve a problem created by one trigger with another trigger. But with event correlation based on event tagging, we can.

For example, a log trigger may report application problems, while a polling trigger may report the application to be up and running. Taking advantage of event tags you can tag the log trigger as _status:down_ while tag the polling trigger as _status:up_. Then, in a global correlation rule you can relate these triggers and assign an appropriate operation to this correlation such as closing the old events.

In another use, global correlation can identify similar triggers and apply the same operation to them. What if we could get only one problem report per network port problem? No need to report them all. That is also possible with global event correlation.

Global event correlation is configured in **correlation rules**. A correlation rule defines how the new problem events are paired with existing problem events and what to do in case of a match (close the new event, close matched old events by generating corresponding OK events). If a problem is closed by global correlation, it is reported in the _Info_ column of _Monitoring_ > _Problems_.

Configuring global correlation rules is available to Super Admin level users only.

Event correlation must be configured very carefully, as it can negatively affect event processing performance or, if misconfigured, close more events than was intended (in the worst case even all problem events could be closed).

To configure global correlation **safely** , observe the following important tips:

  * Reduce the correlation scope. Always set a unique tag for the new event that is paired with old events and use the _New event tag name_ correlation condition;
  * Add a condition based on the old event when using the _Close old event_ operation (or else all existing problems could be closed);
  * Avoid using common tag names that may end up being used by different correlation configurations;
  * Keep the number of correlation rules limited to the ones you really need.

See also: [known issues](/documentation/current/en/manual/installation/known_issues#global-event-correlation).

#### Configuration

To configure event correlation rules globally:

  * Go to _Data collection_ > _Event correlation_
  * Click on _Create event correlation_ to the right (or on the correlation name to edit an existing rule)
  * Enter parameters of the correlation rule in the form

![correlation_rule.png](/documentation/current/assets/en/manual/config/event_correlation/correlation_rule.png)

All mandatory input fields are marked with a red asterisk.

_Name_ | Unique correlation rule name.  
---|---  
_Type of calculation_ | The following options of calculating conditions are available:  
**And** \- all conditions must be met  
**Or** \- enough if one condition is met  
**And/Or** \- AND with different condition types and OR with the same condition type  
**Custom expression** \- a user-defined calculation formula for evaluating action conditions. It must include all conditions (represented as uppercase letters A, B, C, ...) and may include spaces, tabs, brackets ( ), **and** (case sensitive), **or** (case sensitive), **not** (case sensitive).  
_Conditions_ | List of conditions. See below for details on configuring a condition.  
_Description_ | Correlation rule description.  
_Operations_ | Mark the checkbox of the operation to perform when event is correlated. The following operations are available:  
**Close old events** \- close old events when a new event happens. Always add a condition based on the old event when using the _Close old events_ operation or all existing problems could be closed.  
**Close new event** \- close the new event when it happens  
_Enabled_ | If you mark this checkbox, the correlation rule will be enabled.  
  
To configure details of a new condition, click on ![](/documentation/current/assets/en/manual/config/add_link.png) in the Conditions block. A popup window will open where you can edit the condition details.

![](/documentation/current/assets/en/manual/config/event_correlation/correlation_rule_condition.png)

_New condition_ | Select a condition for correlating events.  
_Note_ that if no old event condition is specified, all old events may be matched and closed. Similarly if no new event condition is specified, all new events may be matched and closed.  
The following conditions are available:  
**Old event tag name** \- specify the old event tag name for matching.  
**New event tag name** \- specify the new event tag name for matching.  
**New event host group** \- specify the new event host group for matching.  
**Event tag pair** \- specify new event tag name and old event tag name for matching. In this case there will be a match if the **values** of the tags in both events match. Tag _names_ need not match.  
This option is useful for matching runtime values, which may not be known at the time of configuration (see also [Example](/documentation/current/en/manual/config/event_correlation/global#example)).  
**Old event tag value** \- specify the old event tag name and value for matching, using the following operators:  
_equals_ \- has the old event tag value  
 _does not equal_ \- does not have the old event tag value  
 _contains_ \- has the string in the old event tag value  
 _does not contain_ \- does not have the string in the old event tag value  
**New event tag value** \- specify the new event tag name and value for matching, using the following operators:  
_equals_ \- has the new event tag value  
 _does not equal_ \- does not have the new event tag value  
 _contains_ \- has the string in the new event tag value  
 _does not contain_ \- does not have the string in the new event tag value  
---|---  
  
Because misconfiguration is possible, when similar event tags may be created for **unrelated** problems, please review the cases outlined below!

  * Actual tags and tag values only become visible when a trigger fires. If the regular expression used is invalid, it is silently replaced with an *UNKNOWN* string. If the initial problem event with an *UNKNOWN* tag value is missed, there may appear subsequent OK events with the same *UNKNOWN* tag value that may close problem events which they shouldn't have closed.

  * If a user uses the {ITEM.VALUE} macro without macro functions as the tag value, the 255-character limitation applies. When log messages are long and the first 255 characters are non-specific, this may also result in similar event tags for unrelated problems.

#### Example

Stop repetitive problem events from the same network port.

![](/documentation/current/assets/en/manual/config/event_correlation/correlation_example.png)

This global correlation rule will correlate problems if _host_ and _port_ tag values exist on the trigger and they are the same in the original event and the new one.

The operation will close new problem events on the same network port, keeping only the original problem open.