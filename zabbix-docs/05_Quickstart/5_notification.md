---
title: Receiving problem notification
source: https://www.zabbix.com/documentation/current/en/manual/quickstart/notification
downloaded: 2025-11-14 10:34:30
---

# 5 Receiving problem notification

#### Overview

In this section you will learn how to set up alerting in the form of notifications in Zabbix.

With items collecting data and triggers designed to "fire" upon problem situations, it would also be useful to have some alerting mechanism in place that would notify us about important events even when we are not directly looking at Zabbix frontend.

This is what notifications do. Email being the most popular delivery method for problem notifications, we will learn how to set up an email notification.

#### Email settings

Initially there are several predefined notification [delivery methods](/documentation/current/en/manual/config/notifications/media) in Zabbix. [Email](/documentation/current/en/manual/config/notifications/media/email) is one of those.

To configure email settings, go to _Alerts > Media types_ and click on _Email_ in the list of pre-defined media types.

![](/documentation/current/assets/en/manual/quickstart/media_types.png)

This will present us with the email settings definition form.

![](/documentation/current/assets/en/manual/quickstart/media_type_email.png)

All mandatory input fields are marked with a red asterisk.

In the _Media type_ tab, set the values of _SMTP server_ , _SMTP helo_ , and _Email_ to the appropriate for your environment.

The value in the _Email_ field will be used as the 'From' address for the notifications sent from Zabbix.

Next, it is required to define the content of the problem message. The content is defined by means of a message template, configured in the _Message templates_ tab.

Click on _Add_ to create a message template, and select _Problem_ as the message type.

![](/documentation/current/assets/en/manual/quickstart/media_type_email2.png)

Click on _Add_ when ready and save the form.

Now you have configured _Email_ as a working media type. The media type must also be linked to users by defining specific delivery addresses (like we did when [configuring a new user](login#adding-user)), otherwise it will not be used.

#### New action

Delivering notifications is one of the things [actions](/documentation/current/en/manual/config/notifications/action) do in Zabbix. Therefore, to set up a notification, go to _Alerts > Actions > Trigger actions_ and click on _Create action_.

![](/documentation/current/assets/en/manual/quickstart/new_action.png)

All mandatory input fields are marked with a red asterisk.

In this form, enter a name for the action.

In the most simple case, if we do not add any more specific [conditions](/documentation/current/en/manual/config/notifications/action/conditions), the action will be taken upon any trigger change from 'Ok' to 'Problem'.

We still should define what the action should do - and that is done in the _Operations_ tab. Click on _Add_ in the _Operations_ block, which opens a new operation form.

![](/documentation/current/assets/en/manual/quickstart/new_operation.png)

All mandatory input fields are marked with a red asterisk.

Here, click on _Select_ in the _Send to Users_ block and select the user ('user') we have defined. Select "Email" as the value of _Send to media type_. When done with this, click on _Add_ , and the operation should be added:

![](/documentation/current/assets/en/manual/quickstart/operation_list.png)

That is all for a simple action configuration, so click _Add_ in the action form.

#### Receiving notification

Now, with delivering notifications configured, it would be fun to actually receive one. To help with that, we might on purpose increase the load on our host - so that our [trigger](trigger#adding-trigger) "fires" and we receive a problem notification.

Open the console on your host and run:
    
    
    cat /dev/urandom | md5sum

Copy

✔ Copied

You may run one or several of [these processes](http://en.wikipedia.org/wiki/Md5sum).

Now go to _Monitoring > Latest data_ and see how the values of 'CPU Load' have increased.Remember, for our trigger to "fire", the 'CPU Load' value has to go over '2' for 3 minutes running. Once it does:

  * in _Monitoring > Problems_ you should see the trigger with a flashing 'Problem' status;
  * you should receive a problem notification in your email.

If notifications do not work:

  * verify once again that both the email settings and the action have been configured properly
  * make sure the user you created has at least read permissions on the host which generated the event, as noted in the _[Adding user](login#adding-user)_ step. The user, being part of the 'Zabbix administrators' user group must have at least read access to 'Linux servers' host group that our host belongs to.
  * Additionally, you can check out the action log by going to _Reports > Action log_.