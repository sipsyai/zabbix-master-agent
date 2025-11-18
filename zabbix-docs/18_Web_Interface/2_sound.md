---
title: Sound in browsers
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/user_profile/sound
downloaded: 2025-11-14 10:39:35
---

# 2 Sound in browsers

#### Overview

Sound is used in [global notifications](/documentation/current/en/manual/web_interface/user_profile/global_notifications).

For the sounds to be played in Zabbix frontend, _Frontend notifications_ must be enabled in the user profile's _Frontend notifications_ tab, with all trigger severities checked. Additionally, sounds should be enabled in the global notification pop-up window.

If, for any reason, audio cannot be played on the device, the ![](/documentation/current/assets/en/manual/config/mute_icon.png) button in the global notification pop-up window will remain permanently in the "mute" state, accompanied by the message "Cannot support notification audio for this device" upon hovering over the ![](/documentation/current/assets/en/manual/config/mute_icon.png) button.

Sounds, including the default audio clips, are supported in MP3 format only.

The sounds of Zabbix frontend have been successfully tested in recent Firefox and Opera browsers on Linux, and in Chrome, Firefox, Microsoft Edge, and Opera browsers on Windows.

The autoplay of sounds might be disabled (by default) in recent browser versions. In such cases, you need to enable this setting manually.