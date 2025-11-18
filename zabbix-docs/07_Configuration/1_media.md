---
title: Media types
source: https://www.zabbix.com/documentation/current/en/manual/config/notifications/media
downloaded: 2025-11-14 10:36:10
---

# 1 Media types

#### Overview

Media types are the delivery channels used for sending notifications and alerts from Zabbix.

Media types support the following delivery methods:

  * [Email](/documentation/current/en/manual/config/notifications/media/email)
  * [SMS](/documentation/current/en/manual/config/notifications/media/sms)
  * [Custom script](/documentation/current/en/manual/config/notifications/media/script)
  * [Webhook](/documentation/current/en/manual/config/notifications/media/webhook)

Media types are maintained in _Alerts_ > _Media types_. Some media types come pre-defined in the default dataset. You just need to finetune their parameters to get them working.

![](/documentation/current/assets/en/manual/config/notifications/media_type_list.png)

To see how media types fit within the alerting process, let's look at the three requirements to deliver notifications from Zabbix to end users:

  1. An action [operation](/documentation/current/en/manual/config/notifications/action/operation#configuring-an-operation) must be defined that sends notifications
  2. A working media type must be defined (such as _Email_ that send alerts using SMTP)
  3. User-level delivery details (such as e-mail addresses, phone numbers, etc) must be defined in user media

###### Media type testing

To test if a configured media type works, click on _Test_ in the media type list.

The testing request will be sent to Zabbix server. Zabbix server will attempt to send an alert using the specified media type and will return the result to frontend. The frontend will wait for the server to return the results. Media type testing has a 65-second timeout by default (configurable in _Administration_ > _General_ > _[Timeouts](/documentation/current/en/manual/web_interface/frontend_sections/administration/general#timeouts)_).

See also testing details for:

  * [Email](/documentation/current/en/manual/config/notifications/media/email#testing)
  * [Webhook](/documentation/current/en/manual/config/notifications/media/webhook#testing)
  * [Script](/documentation/current/en/manual/config/notifications/media/script#testing)

#### Configuration

To create a media type in Zabbix frontend:

  * Go to: _Alerts_ > _Media types_
  * Click on _Create media type_
  * Enter parameters of the media type in the form

Some parameters are **common** for all delivery methods.

![](/documentation/current/assets/en/manual/config/notifications/media_types_common.png)

_Name_ | Name of the media type.  
---|---  
_Type_ | Select the delivery method for the media type.  
_Description_ | Enter a description for the media type.  
_Enabled_ | Mark the checkbox to enable the media type.  
  
For method-specific parameters, see [email](/documentation/current/en/manual/config/notifications/media/email#configuration), [SMS](/documentation/current/en/manual/config/notifications/media/sms#configuration), [custom alertscript](/documentation/current/en/manual/config/notifications/media/script#configuration), or [webhook](/documentation/current/en/manual/config/notifications/media/webhook#configuration) pages.

###### Message templates

The **Message templates** tab contains default messages per event type (problem, problem recovery, discovery, etc).

![](/documentation/current/assets/en/manual/config/notifications/media_type_messages.png)

Click on **Add** to define a default message (or **Edit** to update an existing message):

![](/documentation/current/assets/en/manual/config/notifications/media/media_types2.png)

_Message type_ | Type of an event for which the default message should be used.  
Only one default message can be defined for each event type.  
  
---|---  
_Subject_ | Subject of the default message. The subject may contain macros. It is limited to 255 characters.  
Subject is not available for SMS media type.  
_Message_ | The default message. It is limited to certain amount of characters depending on the database type (see [Sending messages](/documentation/current/en/manual/config/notifications/action/operation/message/) for more information).  
The message may contain supported [macros](/documentation/current/en/manual/appendix/macros/supported_by_location).  
In problem and problem update messages, expression macros are supported (for example, `{?avg(/host/key,1h)}`).  
  
Note that default messages are overridden by custom messages, if defined in [action operations](/documentation/current/en/manual/config/notifications/action/operation#operation-details).

Defining message templates is mandatory for all delivery methods, including webhooks or custom alert scripts that do not use default messages for notifications. For example, the action "Send message to Pushover webhook" will fail to send problem notifications, if the problem message for the Pushover webhook is not defined.

###### Options

The **Options** tab contains alert processing settings. The same set of options is configurable for each media type.

All media types are processed in parallel. While the maximum number of concurrent sessions is configurable per media type, the total number of alerter processes on the server can only be limited by the StartAlerters [parameter](/documentation/current/en/manual/appendix/config/zabbix_server). Alerts generated by one trigger are processed sequentially. So multiple notifications may be processed simultaneously only if they are generated by multiple triggers.

![](/documentation/current/assets/en/manual/config/notifications/media/media_type_options.png)

_Concurrent sessions_ | Select the number of parallel alerter sessions for the media type:  
**One** \- one session  
**Unlimited** \- unlimited number of sessions  
**Custom** \- select a custom number of sessions  
Unlimited/high values mean more parallel sessions and increased capacity for sending notifications. Unlimited/high values should be used in large environments where lots of notifications may need to be sent simultaneously.  
If more notifications need to be sent than there are concurrent sessions, the remaining notifications will be queued; they will not be lost.  
---|---  
_Attempts_ | Number of attempts for trying to send a notification. Up to 100 attempts can be specified; the default value is '3'. If '1' is specified, Zabbix will send the notification only once and will not retry if the sending fails.  
_Attempt interval_ | Frequency of trying to resend a notification in case the sending failed, in seconds (0-3600). If '0' is specified, Zabbix will retry immediately.  
Time suffixes are supported, e.g., 5s, 3m, 1h.  
  
#### User media

While media types define **how** a notification will be sent, user media define **where** the notification must be sent.

User media (e.g. email address, webhook user ID, etc.) must be defined in the user profile regardless of the delivery method. An action sending messages to _Admin_ user using webhook _X_ will fail to deliver if the webhook _X_ delivery details are not defined in the Admin user profile.

To define user media:

  * Go to _Users_ > _Users_ and open the user properties form (or go to _User settings_ > _Notifications_ of your own user profile)
  * Click on _Add_ in the Media tab

![](/documentation/current/assets/en/manual/config/notifications/media/user_media2.png)

_Type_ | The drop-down list contains the names of enabled media types.  
Note that when editing a medium of a disabled media type, the type will be displayed in red.  
---|---  
_Send to_ | Enter the contact information where messages should be sent.  
For the email media type, multiple addresses can be added by clicking the ![](/documentation/current/assets/en/manual/config/add_link.png) button below the address field. In this case, notifications will be sent to all listed addresses. For address examples, see the _Email_ parameter description for the [email](/documentation/current/en/manual/config/notifications/media/email#configuration) media type.  
_When active_ | You can limit the time when messages are sent, for example, set the working days only (1-5,09:00-18:00). Note that this limit is based on the user [time zone](/documentation/current/en/manual/web_interface/time_zone). If the user time zone is changed and is different from the system time zone this limit may need to be adjusted accordingly so as not to miss important messages.  
See the [Time period specification](/documentation/current/en/manual/appendix/time_period) page for description of the format.  
User macros are supported.  
_Use if severity_ | Mark the checkboxes of trigger severities that you want to receive notifications for.  
_Note_ that the default severity ('Not classified') **must be** checked if you want to receive notifications for non-trigger [events](/documentation/current/en/manual/config/events).  
After saving, the selected trigger severities will be displayed in the corresponding severity colors, while unselected ones will be grayed out.  
_Status_ | Status of the user media.  
**Enabled** \- is in use.  
**Disabled** \- is not being used.