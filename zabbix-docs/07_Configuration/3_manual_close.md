---
title: Manual closing of problems
source: https://www.zabbix.com/documentation/current/en/manual/config/events/manual_close
downloaded: 2025-11-14 10:35:42
---

# 3 Manual closing of problems

#### Overview

While generally problem events are resolved automatically when trigger status goes from 'Problem' to 'OK', there may be cases when it is difficult to determine if a problem has been resolved by means of a trigger expression. In such cases, the problem needs to be resolved manually.

For example, _syslog_ may report that some kernel parameters need to be tuned for optimal performance. In this case the issue is reported to Linux administrators, they fix it and then close the problem manually.

Problems can be closed manually only for triggers with the _Allow manual close_ option enabled.

When a problem is "manually closed", Zabbix generates a new internal task for Zabbix server. Then the _task manager_ process executes this task and generates an OK event, therefore closing problem event.

A manually closed problem does not mean that the underlying trigger will never go into a 'Problem' state again. The trigger expression is re-evaluated and may result in a problem:

  * When new data arrive for any item included in the trigger expression (note that the values discarded by a throttling preprocessing step are not considered as received and will not cause trigger expression to be re-evaluated);
  * When [date and time](/documentation/current/en/manual/appendix/functions/time) and/or [nodata()](/documentation/current/en/manual/appendix/functions/history#nodata) functions are used in the expression.

#### Configuration

Two steps are required to close a problem manually.

##### Trigger configuration

In trigger configuration, enable the _Allow manual close_ option.

![](/documentation/current/assets/en/manual/config/manual_close_conf1.png)

##### Problem update window

If a problem arises for a trigger with the _Manual close_ flag, you can open the [problem update](/documentation/current/en/manual/acknowledgment#updating-problems) popup window of that problem and close the problem manually.

To close the problem, check the _Close problem_ option in the form and click on _Update_.

![](/documentation/current/assets/en/manual/config/close_problem1.png)

All mandatory input fields are marked with a red asterisk.

The request is processed by Zabbix server. Normally it will take a few seconds to close the problem. During that process _CLOSING_ is displayed in _Monitoring_ → _Problems_ as the status of the problem.

#### Verification

It can be verified that a problem has been closed manually:

  * in event details, available through _Monitoring_ → _Problems_ ;
  * by using the {EVENT.UPDATE.HISTORY} macro in notification messages that will provide this information.