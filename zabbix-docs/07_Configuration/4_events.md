---
title: Events
source: https://www.zabbix.com/documentation/current/en/manual/config/events
downloaded: 2025-11-14 10:35:39
---

# 4 Events

#### Overview

There are several types of events generated in Zabbix:

  * trigger events - whenever a trigger changes its status (_OK→PROBLEM→OK_)
  * service events - whenever a service changes its status (_OK→PROBLEM→OK_)
  * discovery events - when hosts or services are detected
  * autoregistration events - when active agents are auto-registered by server
  * internal events - when an item/low-level discovery rule becomes unsupported or a trigger goes into an unknown state

Events are time-stamped and can be the basis of actions such as sending notification email etc.

To view details of events in the frontend, go to _Monitoring_ → _Problems_. There you can click on the event date and time to view details of an event.

More information is available on:

  * [trigger events](/documentation/current/en/manual/config/events/trigger_events)
  * [other event sources](/documentation/current/en/manual/config/events/sources)