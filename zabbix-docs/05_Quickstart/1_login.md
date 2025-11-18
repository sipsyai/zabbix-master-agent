---
title: Login and configuring user
source: https://www.zabbix.com/documentation/current/en/manual/quickstart/login
downloaded: 2025-11-14 10:34:26
---

# 1 Login and configuring user

#### Overview

In this section, you will learn how to log in and set up a system user in Zabbix.

#### Login

![](/documentation/current/assets/en/manual/quickstart/login.png)

This is the Zabbix welcome screen. Enter the user name **Admin** with password **zabbix** to log in as a [Zabbix superuser](/documentation/current/en/manual/config/users_and_usergroups/permissions). Access to all menu sections will be granted.

For security reasons, it is strongly recommended to change the default password for the Admin account immediately after the first login.

##### Persistent login

To stay logged in for up to 30 days, select _Remember for 30 days_ before clicking _Sign in_.

Remember for 30 days enabled:

  * Your session remains active for 30 days.
  * [_Auto-logout_](/documentation/current/en/manual/web_interface/user_profile#user-profile) is overridden, keeping you signed in until the period ends.
  * You will be auto‑logged in on future visits within 30 days without re‑entering credentials.

Remember for 30 days disabled:

  * Any previously enabled auto-login is cleared.
  * Session will expire according to the configured _Auto‑logout_ interval.

##### Protection against brute force attacks

In case of five consecutive failed login attempts, Zabbix interface will pause for 30 seconds in order to prevent brute force and dictionary attacks.

The IP address of a failed login attempt will be displayed after a successful login.

#### Adding user

To view information about users, go to _Users > Users_ in the sidebar's vertical menu.

![](/documentation/current/assets/en/manual/web_interface/users.png)

To add a new user, select _Create user_ in the upper-right corner.

In the new user form, make sure to add your user to one of the existing [user groups](/documentation/current/en/manual/config/users_and_usergroups/usergroup), for example 'Zabbix administrators'.

![](/documentation/current/assets/en/manual/quickstart/new_user.png)

All mandatory input fields are marked with a red asterisk. For details about input fields on this configuration form, refer to the [User settings](/documentation/current/en/manual/web_interface/user_profile) page.

By default, new users have no media (notification delivery methods) defined for them. To create one, go to the 'Media' tab and click on _Add_.

![](/documentation/current/assets/en/manual/quickstart/new_media_tab.png)

In the pop-up, enter the user's email address.

You can specify a time period when the medium will be active (see [Time period specification](/documentation/current/en/manual/appendix/time_period) page for a description of the format). By default a medium is always active. You can also customize [trigger severity](/documentation/current/en/manual/config/triggers/severity) levels for which the medium will be active, but leave all of them enabled for now.

![](/documentation/current/assets/en/manual/quickstart/new_media.png)

Click on _Add_ to save the medium, then go to the Permissions tab.

Permissions tab has a mandatory field _Role_. The role determines which frontend elements the user can view and which actions he is allowed to perform. Press Select and select one of the roles from the list. For example, select _Admin role_ to allow access to all Zabbix frontend sections, except Administration. Later on, you can modify permissions or create more user roles. Upon selecting a role, permissions will appear in the same tab:

![user_permissions.png](/documentation/current/assets/en/manual/config/user_permissions.png)

Click _Add_ in the user properties form to save the user. The new user appears in the userlist.

![](/documentation/current/assets/en/manual/quickstart/userlist2.png)

##### Adding permissions

By default, a new user has no permissions to access hosts and templates. To grant the user rights, click on the group of the user in the _Groups_ column (in this case - 'Zabbix administrators'). In the _User groups_ properties form, go to the _Host permissions_ tab to assign permissions to host groups. Click on ![](/documentation/current/assets/en/manual/config/add_link.png) for the host group selection field to be displayed:

![](/documentation/current/assets/en/manual/quickstart/group_permissions.png)

Then click on _Select_ next to the field to see the list of the host groups. This user is to have read-only access to _Linux servers_ group, so mark the appropriate checkbox in the list and click on _Select_ to confirm your choice.

![](/documentation/current/assets/en/manual/quickstart/add_permissions.png)

Click the _Read_ button to set the permission level and then _Update_ to save the changes made to the user group configuration.

To grant permissions to templates, you will need to switch to the _Template permissions_ tab and specify template groups. The steps are identical to assigning permissions to host groups. An overview of templates is available in the [New template](/documentation/current/en/manual/quickstart/template) section of this Quickstart.

In Zabbix, access rights to hosts and templates are assigned to [user groups](/documentation/current/en/manual/config/users_and_usergroups/usergroup), not individual users.

Done! You may try to log in using the credentials of the new user.