---
title: Problem suppression
source: https://www.zabbix.com/documentation/current/en/manual/acknowledgment/suppression
downloaded: 2025-11-14 10:37:06
---

# 1 Problem suppression

#### Overview

Problem suppression offers a way of temporarily hiding a problem that can be dealt with later. This is useful for cleaning up the problem list in order to give the highest priority to the most urgent issues. For example, sometimes an issue may arise on the weekend that is not urgent enough to be dealt with immediately, so it can be "snoozed" until Monday morning.

Problem suppression allows to hide a _single_ problem, in contrast to problem suppression through host maintenance when all problems of the maintenance host are hidden.

Operations for trigger actions will be paused for suppressed problems the same way as it is done with [host maintenance](/documentation/current/en/manual/maintenance).

#### Configuration

A problem can be suppressed through the **[problem update](/documentation/current/en/manual/acknowledgment#updating-problems)** window, where suppression is one of the problem update options along with commenting, changing severity, acknowledging, etc.

A problem may also be unsuppressed through the same problem update window.

#### Display

Once suppressed the problem is marked by a blinking ![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/icon_suppression.png) suppression icon in the _Info_ column, before being hidden.

The suppression icon is blinking while the suppression task is in the waiting list. Once the task manager has suppressed the problem, the icon will stop blinking. If the suppression icon keeps blinking for a long time, this may indicate a server problem, for example, if the server is down and the task manager cannot complete the task. The same logic applies to unsuppression. In the short period after the task is submitted and the server has not completed it, the unsuppression icon is blinking.

A suppressed problem may be both hidden or shown, depending on the problem filter/widget settings.

When shown in the problem list, a suppressed problem is marked by the suppression icon and suppression details are shown on mouseover:

![](/documentation/current/assets/en/manual/web_interface/suppressed_problem_listed.png)

Suppression details are also displayed in a popup when positioning the mouse on the suppression icon in the _Actions_ column.