---
title: Sending message
source: https://www.zabbix.com/documentation/current/en/manual/config/notifications/action/operation/message
downloaded: 2025-11-14 10:36:21
---

# 1 Sending message

#### Overview

Sending a message is one of the best ways of notifying people about a problem. That is why it is one of the primary actions offered by Zabbix.

#### Configuration

To be able to send and receive notifications from Zabbix you have to:

  * [define the media](/documentation/current/en/manual/config/notifications/media) to send a message to

If the operation takes place outside of the [When active](/documentation/current/en/manual/config/notifications/media#user-media) time period defined for the selected media in the user configuration, the message will not be sent.

The default trigger severity ('Not classified') **must be** checked in user media [configuration](/documentation/current/en/manual/config/notifications/media/email#user-media) if you want to receive notifications for non-trigger events such as discovery, active agent autoregistration or internal events.

  * [configure an action operation](/documentation/current/en/manual/config/notifications/action/operation) that sends a message to one of the defined media

Zabbix sends notifications only to those users that have at least 'read' permissions to the host that generated the event. At least one host of a trigger expression must be accessible.

You can configure custom scenarios for sending messages using [escalations](/documentation/current/en/manual/config/notifications/action/escalations).

To successfully receive and read emails from Zabbix, email servers/clients must support standard 'SMTP/MIME email' format since Zabbix sends UTF-8 data (If the subject contains ASCII characters only, it is not UTF-8 encoded.). The subject and the body of the message are base64-encoded to follow 'SMTP/MIME email' format standard.

Message limit after all macros expansion is the same as message limit for [Remote commands](/documentation/current/en/manual/config/notifications/action/operation/remote_command).

#### Tracking messages

You can view the status of messages sent in _Monitoring → Problems_.

In the _Actions_ column you can see summarized information about actions taken. In there green numbers represent messages sent, red ones - failed messages. _In progress_ indicates that an action is initiated. _Failed_ informs that no action has executed successfully.

If you click on the event time to view event details, you will be able to see details of messages sent (or not sent) due to the event in the _Actions_ block.

In _Reports → Action log_ you will see details of all actions taken for those events that have an action configured.