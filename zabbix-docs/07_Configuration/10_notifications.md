---
title: Notifications upon events
source: https://www.zabbix.com/documentation/current/en/manual/config/notifications
downloaded: 2025-11-14 10:36:09
---

# 10 Notifications upon events

#### Overview

Assuming that we have configured some items and triggers and now are getting some events happening as a result of triggers changing state, it is time to consider some actions.

To begin with, we would not want to stare at the triggers or events list all the time. It would be much better to receive notification if something significant (such as a problem) has happened. Also, when problems occur, we would like to see that all the people concerned are informed.

That is why sending notifications is one of the primary actions offered by Zabbix. Who and when should be notified upon a certain event can be defined.

To be able to send and receive notifications from Zabbix you have to:

  * [define some media](/documentation/current/en/manual/config/notifications/media)
  * [configure an action](/documentation/current/en/manual/config/notifications/action) that sends a message to one of the defined media

Actions consist of _conditions_ and _operations_. Basically, when conditions are met, operations are carried out. The two principal operations are sending a message (notification) and executing a remote command.

For discovery and autoregistration created events, some additional operations are available. Those include adding or removing a host, linking a template etc.