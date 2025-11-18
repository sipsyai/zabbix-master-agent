---
title: Event menu
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/menu/event_menu
downloaded: 2025-11-14 10:37:54
---

# 1 Event menu

#### Overview

The event menu contains shortcuts to actions or frontend sections that are frequently required for an event.

The event menu can be opened by clicking on the event name.

![](/documentation/current/assets/en/manual/web_interface/event_context_menu.png)

#### Content

The event context menu has six sections: _View_ , _Actions_ , _Configuration_ , _Problem_ , _Links_ , and _Scripts_. For the entities that are not configured, links are disabled and displayed in gray. The sections _Scripts_ and _Links_ are displayed if their entities are configured.

The _View_ section contains links to:

  * **Problems** \- opens the list of unresolved problems of the underlying trigger;
  * **History** \- leads to the _Latest data_ graph/item history for the underlying item(s). If a trigger uses several items, links will be available for each of them.

The _Actions_ section is available in _Trigger overview_ widgets only. It contains a link to:

  * **Update problem** \- opens the [problem update](/documentation/current/en/manual/acknowledgment#updating-problems) screen.

The _Configuration_ section contains links to the configuration of:

  * **Trigger** that fired the problem;
  * **Items** used in the trigger expression.

Note that configuration section is available only for Admin and Super admin users.

The _Problem_ section contains the options to:

  * **Mark as cause** \- mark the problem as cause;
  * **Mark selected as symptoms** \- mark the selected problems as symptoms of this problem.

The _Links_ section contains links to:

  * access a configured [trigger URL](/documentation/current/en/manual/config/triggers/trigger#configuration);
  * access custom links configured in [Global scripts](/documentation/current/en/manual/web_interface/frontend_sections/alerts/scripts) (with scope 'Manual event action' and type 'URL');
  * access a configured external ticket for the problem (see the _Include event menu entry_ option when configuring [webhooks](/documentation/current/en/manual/config/notifications/media/webhook)).

The _Scripts_ section contains links to execute a global [script](/documentation/current/en/manual/web_interface/frontend_sections/alerts/scripts) (with scope _Manual event action_). This feature may be handy for running scripts used for managing problem tickets in external systems.

#### Supported locations

The event context menu is accessible by clicking on a problem or event name in various frontend sections, for example:

  * Dashboards [widgets](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets), such as _Problems_ widget, _Trigger overview_ widget, etc.
  * Monitoring → [Problems](/documentation/current/en/manual/web_interface/frontend_sections/monitoring/problems)
  * Monitoring → [Problems](/documentation/current/en/manual/web_interface/frontend_sections/monitoring/problems) → Event details
  * Reports → [Top 100 triggers](/documentation/current/en/manual/web_interface/frontend_sections/reports/triggers_top) (global scripts and access to external ticket are not supported in this location)