---
title: Time zones
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/time_zone
downloaded: 2025-11-14 10:39:43
---

# 11 Time zones

#### Overview

The frontend time zone can be set globally in the frontend and adjusted for individual users.

![](/documentation/current/assets/en/manual/web_interface/time_zone_global.png)

If _System_ is selected, the web server time zone will be used for the frontend (including the value of 'date.timezone' of php.ini, if set), while Zabbix server will use the time zone of the machine it is running on.

Zabbix server will only use the specified global/user time zone when expanding macros in notifications (e.g. {EVENT.TIME} can expand to a different time zone per user) and for the time limit when notifications are sent (see "When active" setting in user [media configuration](/documentation/current/en/manual/config/notifications/media#user-media)).

The choice of time zone does not affect the frontend time/date format. Instead, you may adjust the interface language (either at installation or under [user settings](/documentation/current/en/manual/web_interface/user_profile#user-profile)) - selecting _English (en_US)_ will also enable the US time/date format in the frontend.

#### Configuration

The global time zone:

  * can be set manually when [installing](/documentation/current/en/manual/installation/frontend) the frontend
  * can be modified in _Administration_ → _General_ → _[GUI](/documentation/current/en/manual/web_interface/frontend_sections/administration/general#gui)_

User-level time zone:

  * can be set when [configuring/updating](/documentation/current/en/manual/config/users_and_usergroups/user#general-attributes) a user
  * can be set by each user in their [user profile](/documentation/current/en/manual/web_interface/user_profile#user-profile)

**See also:** Aligning time zones when using [scheduling intervals](/documentation/current/en/manual/config/items/item/custom_intervals#aligning-time-zones-for-proxies-and-agent).