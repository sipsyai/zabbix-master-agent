---
title: Cause and symptom problems
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/monitoring/problems/cause_and_symptom
downloaded: 2025-11-14 10:38:33
---

# 1 Cause and symptom problems

#### Overview

By default all new problems are classified as cause problems. It is possible to manually reclassify certain problems as symptom problems of the cause problem.

For example, power outage may be the actual root cause why some host is unreachable or some service is down. In this case, "host is unreachable" and "service is down" problems must be classified as symptom problems of "power outage" - the cause problem.

The cause-symptom hierarchy supports only two levels. A problem that is already a symptom cannot be assigned "subordinate" symptom problems; any problems assigned as symptoms to a symptom problem will become symptoms of the same cause problem.

Only cause problems are counted in problem totals in maps, dashboard widgets such as _Problems by severity_ or _Problem hosts_ , etc. However, problem ranking does not affect services.

A symptom problem can be linked to only one cause problem. Symptom problems are not automatically resolved, if the cause problem is resolved or closed.

#### Configuration

To reclassify a problem as symptom problem, first select it in the list of [problems](/documentation/current/en/manual/web_interface/frontend_sections/monitoring/problems). One or several problems can be selected.

Then go to the cause problem, and in its context menu click on the _Mark selected as symptoms_ option.

![cause_symptom_conf.png](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/cause_symptom_conf.png)

After that, the selected problems will be updated by the server to symptom problems of the cause problem.

While the status of the problem is being updated, it is displayed in one of two ways:

  * A blinking "UPDATING" status is displayed in the Status column;
  * A blinking ![icon_symptom.png](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/icon_symptom.png) or ![icon_cause.png](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/icon_cause.png) icon in the Info column (this is in effect if _Problems_ only are selected in the filter and thus the Status column is not shown).

#### Display

Symptom problems are displayed below the cause problem and marked accordingly in _Monitoring_ -> _Problems_ (and the _Problems_ dashboard widget) - with an icon, smaller font and different background.

![cause_symptom_display2.png](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/cause_symptom_display2.png)

In collapsed view, only the cause problem is seen; the existence of symptom problems is indicated by the number in the beginning of the line and the icon for expanding the view.

![cause_symptom_display.png](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/cause_symptom_display.png)

It is also possible to additionally display symptom problems in normal font and in their own line. For that select _Show symptoms_ in the filter settings or the widget configuration.

#### Reverting to cause problem

A symptom problem can be reverted back to a cause problem. To do that, either:

  * click on the _Mark as cause_ option in the context menu of the symptom problem;
  * mark the _Convert to cause_ option in to the [problem update](/documentation/current/en/manual/acknowledgment#updating-problems) screen and click on _Update_ (this option will also work if several problems are selected).