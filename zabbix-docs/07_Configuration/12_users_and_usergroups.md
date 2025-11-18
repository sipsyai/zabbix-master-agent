---
title: Users and user groups
source: https://www.zabbix.com/documentation/current/en/manual/config/users_and_usergroups
downloaded: 2025-11-14 10:36:35
---

# 12 Users and user groups

#### Overview

All users in Zabbix access the Zabbix application through the web-based frontend. Each user is assigned a unique login name and a password.

All user passwords are encrypted and stored in the Zabbix database. Users cannot use their user id and password to log directly into the UNIX server unless they have also been set up accordingly to UNIX. Communication between the web server and the user browser can be protected using SSL.

With a flexible [user permission schema](/documentation/current/en/manual/config/users_and_usergroups/permissions) you can restrict and differentiate rights to:

  * access administrative Zabbix frontend functions
  * perform certain actions in the frontend
  * access monitored hosts in hostgroups
  * use specific API methods