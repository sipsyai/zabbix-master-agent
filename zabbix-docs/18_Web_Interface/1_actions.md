---
title: Actions
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/alerts/actions
downloaded: 2025-11-14 10:39:12
---

# 1 Actions

#### Overview

In the _Alerts → Actions_ section users can configure and maintain actions.

The actions displayed are actions assigned to the selected event source (trigger, services, discovery, autoregistration, internal actions).

To switch to a different event source, click on _Actions_ in the _Alerts_ menu section. It is also possible to switch between sources by using the title dropdown in the upper-left corner.

![](/documentation/current/assets/en/manual/web_interface/actions.png)

Displayed data:

_Name_ | Name of the action. Clicking on the action name opens the action [configuration form](/documentation/current/en/manual/config/notifications/action#configuring-an-action).  
---|---  
_Conditions_ | Action conditions are displayed.  
_[Operations](/documentation/current/en/manual/config/notifications/action/operation#configuring-an-operation)_ | Action operations are displayed.  
The operation list also displays the media type (email, SMS or script) used for notification as well as the name and surname (in parentheses after the username) of a notification recipient.  
Action operation can both be a [notification](/documentation/current/en/manual/config/notifications/action/operation/message) or a [remote command](/documentation/current/en/manual/config/notifications/action/operation/remote_command) depending on the selected type of operation.  
_Status_ | Action status is displayed - _Enabled_ or _Disabled_.  
By clicking on the status you can change it.  
See the [Escalations](/documentation/current/en/manual/config/notifications/action/escalations) section for more details as to what happens if an action is disabled during an escalation in progress.  
_Info_ | If everything is working correctly, no icon is displayed in this column. In case of errors, such as missing action operations or conditions after upgrade/low-level discovery, a warning icon is displayed. Hover over the icon to see a tooltip with the error description.  
  
To configure a new action, click on the _Create action_ button in the upper-right corner.

For users without Super admin rights actions are displayed according to the permission settings. That means in some cases a user without Super admin rights isn't able to view the complete action list because of certain permission restrictions. An action is displayed to the user without Super admin rights if the following conditions are fulfilled:

  * The user has read-write access to host groups, hosts, templates, and triggers in action conditions
  * The user has read-write access to host groups, hosts, and templates in action operations, recovery operations, and update operations
  * The user has read access to user groups and users in action operations, recovery operations, and update operations

##### Mass editing options

Buttons below the list offer some mass-editing options:

  * _Enable_ \- change the action status to _Enabled_
  * _Disable_ \- change the action status to _Disabled_
  * _Delete_ \- delete the actions

To use these options, mark the checkboxes before the respective actions, then click on the required button.

##### Using filter

You can use the filter to display only the actions you are interested in. For better search performance, data is searched with macros unresolved.

The _Filter_ link is available above the list of actions. If you click on it, a filter becomes available where you can filter actions by name and status.

![](/documentation/current/assets/en/manual/web_interface/action_filter.png)