---
title: Receiving notification on unsupported items
source: https://www.zabbix.com/documentation/current/en/manual/config/notifications/unsupported_item
downloaded: 2025-11-14 10:36:28
---

# 3 Receiving notification on unsupported items

#### Overview

It is possible to receive notifications on unsupported items in Zabbix.

It is part of the concept of internal events in Zabbix, allowing users to be notified on these occasions. [Internal events](/documentation/current/en/manual/config/events/sources#internal-events) reflect a change of state:

  * when items go from 'normal' to 'unsupported' (and back);
  * when triggers go from 'normal' to 'unknown' (and back);
  * when low-level discovery rules go from 'normal' to 'unsupported' (and back).

This section presents a how-to for **receiving notification** when an item turns unsupported.

#### Configuration

Overall, the process of setting up the notification should feel familiar to those who have set up alerts in Zabbix before.

##### Step 1

Configure [some media](media), such as email, SMS, or script to use for the notifications. Refer to the corresponding sections of the manual to perform this task.

For notifying on internal events the default severity ('Not classified') is used, so leave it checked when configuring [user media](/documentation/current/en/manual/config/notifications/media/email#user-media) if you want to receive notifications for internal events.

##### Step 2

Go to _Alerts → Actions_ → _Internal actions_.

Click on _Create action_ at the upper-right corner of the page to open an action configuration form.

##### Step 3

In the _Action_ tab enter a name for the action. Then click on _Add_ in the _Conditions_ block to add a new condition.

![](/documentation/current/assets/en/manual/config/notifications/report_items_actions.png)

In the _New condition_ pop-up window select "Event type" as the condition type and then select "Item in 'not supported' state" as the event type.

![](/documentation/current/assets/en/manual/config/notifications/report_items_actions_details.png)

Don't forget to click on _Add_ to actually list the condition in the _Conditions_ block.

##### Step 4

In the _Operations_ tab, click on _Add_ in the _Operations_ block to add a new operation.

![](/documentation/current/assets/en/manual/config/notifications/report_items_operations1.png)

Select some recipients of the message (user groups/users) and the media type (or "All") to use for delivery. Check the _Custom message_ checkbox if you wish to enter the custom subject/content of the problem message.

![](/documentation/current/assets/en/manual/config/notifications/report_items_operations1_details.png)

Click on _Add_ to actually list the operation in the _Operations_ block.

If you wish to receive more than one notification, set the operation step duration (interval between messages sent) and add another step.

##### Step 5

The _Recovery operations_ block allows to configure a recovery notification when an item goes back to the normal state. Click on _Add_ in the _Recovery operations_ block to add a new recovery operation.

![](/documentation/current/assets/en/manual/config/notifications/report_items_operations2.png)

Select the operation type "Notify all involved". Select _Custom message_ checkbox if you wish to enter the custom subject/content of the problem message.

![](/documentation/current/assets/en/manual/config/notifications/report_items_operations2_details.png)

Click on _Add_ in the _Operation details_ pop-up window to actually list the operation in the _Recovery operations_ block.

##### Step 6

When finished, click on the _Add_ button at the bottom of the form.

![](/documentation/current/assets/en/manual/config/notifications/report_items_operations3.png)

And that's it, you're done! Now you can look forward to receiving your first notification from Zabbix if some item turns unsupported.