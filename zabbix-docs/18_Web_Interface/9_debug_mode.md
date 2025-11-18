---
title: Debug mode
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/debug_mode
downloaded: 2025-11-14 10:39:41
---

# 9 Debug mode

#### Overview

Debug mode may be used to diagnose performance problems with frontend pages.

#### Configuration

Debug mode can be activated for individual users who belong to a user group:

  * when configuring a [user group](/documentation/current/en/manual/config/users_and_usergroups/usergroup#configuration);
  * when viewing configured [user groups](/documentation/current/en//manual/web_interface/frontend_sections/users/user_groups).

When _Debug mode_ is enabled for a user group, its users will see a _Debug_ button in the lower-right corner of the browser window:

![](/documentation/current/assets/en/manual/web_interface/debug_button.png)

Clicking on the _Debug_ button opens a new window below the page contents which contains the SQL statistics of the page, along with a list of API calls and individual SQL statements:

![](/documentation/current/assets/en/manual/web_interface/debug_mode.png)

In case of performance problems with the page, this window may be used to search for the root cause of the problem.

Enabled _Debug mode_ negatively affects frontend performance.