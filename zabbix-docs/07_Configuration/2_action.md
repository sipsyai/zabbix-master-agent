---
title: Actions
source: https://www.zabbix.com/documentation/current/en/manual/config/notifications/action
downloaded: 2025-11-14 10:36:18
---

# 2 Actions

#### Overview

If you want some operations taking place as a result of events (for example, notifications sent), you need to configure actions.

Actions can be defined in response to events of all supported types:

  * Trigger actions - for events when trigger status changes from _OK_ to _PROBLEM_ and back
  * Service actions - for events when service status changes from _OK_ to _PROBLEM_ and back
  * Discovery actions - for events when network discovery takes place
  * Autoregistration actions - for events when new active agents auto-register (or host metadata changes for registered ones)
  * Internal actions - for events when items become unsupported or triggers go into an unknown state

The key differences of service actions are:

  * User access to service actions depends on access rights to services granted by user's [role](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles)
  * Service actions support different set of [conditions](/documentation/current/en/manual/config/notifications/action/conditions#service-actions)

#### Configuring an action

To configure an action, do the following:

  * Go to _Alerts_ > _Actions_ and select the required action type from the submenu (you can switch to another type later, using the title dropdown).
  * Click on _Create action_.
  * Name the action.
  * Choose [conditions](/documentation/current/en/manual/config/notifications/action/conditions) upon which operations are carried out.
  * Choose the [operations](/documentation/current/en/manual/config/notifications/action/operation) to carry out.

General action attributes:

![](/documentation/current/assets/en/manual/config/notifications/action.png)

All mandatory input fields are marked with a red asterisk.

_Name_ | Unique action name.  
---|---  
_Type of calculation_ | Select the evaluation [option](/documentation/current/en/manual/config/notifications/action/conditions#type-of-calculation) for action conditions (with more than one condition):  
**And** \- all conditions must be met.  
**Or** \- enough if one condition is met.  
**And/Or** \- combination of the two: AND with different condition types and OR with the same condition type.  
**Custom expression** \- a user-defined calculation formula for evaluating action conditions.  
_Conditions_ | List of action conditions.  
Click on _Add_ to add a new [condition](/documentation/current/en/manual/config/notifications/action/conditions).  
If no conditions are configured, the action will run for every event that corresponds to the action type being configured.  
_Enabled_ | Mark the checkbox to enable the action. Otherwise, it will be disabled.