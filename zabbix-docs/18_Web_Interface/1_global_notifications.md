---
title: Global notifications
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/user_profile/global_notifications
downloaded: 2025-11-14 10:39:34
---

# 1 Global notifications

#### Overview

Global notifications provide a way to display real-time issues directly on your current screen within Zabbix frontend.

Without global notifications, when working outside the _Problems_ or _Dashboard_ sections, you would not receive any information about current issues. Global notifications ensure that this information is displayed, regardless of your current location within the Zabbix frontend.

Global notifications include both displaying a message and [playing a sound](sound).

The autoplay of sounds might be disabled (by default) in recent browser versions. In such cases, you need to enable this setting manually.

#### Configuration

Global notifications can be enabled per user in the **Frontend notifications** tab of [Notifications](/documentation/current/en/manual/web_interface/user_profile#notifications) section.

![profile_c.png](/documentation/current/assets/en/manual/web_interface/profile_c.png)

_Frontend notifications_ | Mark the checkbox to enable global notifications.  
---|---  
_Message timeout_ | Set the duration for which the message will be displayed. By default, messages remain on the screen for 60 seconds.  
[Time suffixes](/documentation/current/en/manual/appendix/suffixes) are supported, for example: 30s, 5m, 2h, 1d.  
_Play sound_ | Set the duration for which the sound will be played.  
**Once** \- sound is played once and fully;  
**10 seconds** \- sound is repeated for 10 seconds;  
**Message timeout** \- sound is repeated while the message is visible.  
_Trigger severity_ | Set the trigger severities for which global notifications and sounds will be activated. You can also select sounds appropriate for various severities.  
If no severity is marked, no messages will be displayed.  
Additionally, recovery messages will only be displayed for marked severities. For instance, if _Recovery_ and _Disaster_ are marked, global notifications will be displayed for problems and recoveries of _Disaster_ severity triggers.  
_Show suppressed problems_ | Mark the checkbox to display notifications for problems that would otherwise be suppressed (not shown) due to host maintenance.  
  
##### Global messages displayed

As messages arrive, they are displayed in a floating section on the right-hand side. You can freely reposition this section by dragging the section header.

![global_messages.png](/documentation/current/assets/en/manual/web_interface/global_messages.png)

For this section, several controls are available:

  * ![](/documentation/current/assets/en/manual/about/message_button_snooze.png) **Snooze** button silences the currently active alarm sound;
  * ![](/documentation/current/assets/en/manual/about/message_button_mute.png) **Mute/Unmute** button switches between playing and not playing the alarm sounds at all.