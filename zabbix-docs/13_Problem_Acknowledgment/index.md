---
title: Problem acknowledgment
source: https://www.zabbix.com/documentation/current/en/manual/acknowledgment
downloaded: 2025-11-14 10:37:05
---

# 13 Problem acknowledgment  
  
#### Overview

Problem events in Zabbix can be acknowledged by users.

If a user gets notified about a problem event, they can go to Zabbix frontend, open the problem update popup window of that problem using one of the ways listed below and acknowledge the problem. When acknowledging, they can enter their comment for it, saying that they are working on it or whatever else they may feel like saying about it.

This way, if another system user spots the same problem, they immediately see if it has been acknowledged and the comments so far.

This way the workflow of resolving problems with more than one system user can take place in a coordinated way.

Acknowledgment status is also used when defining [action operations](/documentation/current/en/manual/config/notifications/action/operation). You can define, for example, that a notification is sent to a higher level manager only if an event is not acknowledged for some time.

To acknowledge events and comment on them, a user must have at least read permissions to the corresponding triggers. To change problem severity or close problem, a user must have read-write permissions to the corresponding triggers.

There are **several** ways to access the problem update popup window, which allows acknowledging a problem.

  * You may select problems in _Monitoring_ → _Problems_ and then click on _Mass update_ below the list
  * You can click on _Update_ in the _Update_ column of a problem in: 
    * _Dashboards_ (_Problems_ and _Problems by severity_ widgets)
    * _Monitoring → Problems_
    * _Monitoring → Problems → Event details_
  * You can click on an unresolved problem cell in: 
    * _Dashboards_ (_Trigger overview_ widget)

The popup menu contains an _Update_ option that will take you to the problem update window.

#### Updating problems

The problem update popup allows to:

  * comment on the problem
  * view comments and actions so far
  * change problem severity
  * suppress/unsuppress problem
  * acknowledge/unacknowledge problem
  * change symptom problem to cause problem
  * manually close problem

![](/documentation/current/assets/en/manual/acknowledges/update_problem.png)

All mandatory input fields are marked with a red asterisk.

_Problem_ | If only one problem is selected, the problem name is displayed.  
If several problems are selected, _N problems selected_ is displayed.  
---|---  
_Message_ | Enter text to comment on the problem (maximum 2048 characters).  
_History_ | Previous activities and comments on the problem are listed, along with the time and user details.  
For the meaning of icons used to denote user actions see the [event detail](/documentation/current/en/manual/web_interface/frontend_sections/monitoring/problems#viewing-details) page.  
Note that history is displayed if only one problem is selected for the update.  
_Scope_ | Define the scope of such actions as changing severity, acknowledging or manually closing problems:  
**Only selected problem** \- will affect this event only  
**Selected and all other problems of related triggers** \- in case of acknowledgment/closing problem, will affect this event and all other problems that are not acknowledged/closed so far. If the scope contains problems already acknowledged or closed, these problems will not be acknowledged/closed repeatedly. On the other hand, the number of message and severity change operations are not limited.  
_Change severity_ | Mark the checkbox and click on the severity button to update problem severity.  
The checkbox for changing severity is available if read-write permissions exist for at least one of the selected problems. Only those problems that are read-writable will be updated when clicking on _Update_.  
If read-write permissions exist for none of the selected triggers, the checkbox is disabled.  
_Suppress_ | Mark the checkbox to suppress the problem:  
**Indefinitely** \- suppress indefinitely  
**Until** \- suppress until a given time. Both [absolute and relative](/documentation/current/en/manual/web_interface/time_period_selector) time formats are supported, for example:  
`now+1d` \- for one day from now (default)  
`now/w` \- until the end of the current week  
`2022-05-28 12:00:00` \- until absolute date/time  
Note that a simple period (e. g., `1d`, `1w`) is not supported.  
Availability of this option depends on the "Suppress problems" user role settings.  
See also: [Problem suppression](/documentation/current/en/manual/acknowledgment/suppression)  
_Unsuppress_ | Mark the checkbox to unsuppress the problem. This checkbox is active only if at least one of the selected problems is suppressed.  
Availability of this option depends on the "Suppress problems" user role settings.  
_Acknowledge_ | Mark the checkbox to acknowledge the problem.  
This checkbox is available if there is at least one unacknowledged problem among the selected.  
It is not possible to add another acknowledgment for an already acknowledged problem (it is possible to add another comment though).  
_Unacknowledge_ | Mark the checkbox to unacknowledge the problem.  
This checkbox is available if there is at least one acknowledged problem among the selected.  
_Convert to cause_ | Mark the checkbox to convert the symptom problem(s) to cause problem(s).  
_Close problem_ | Mark the checkbox to manually close the selected problem(s).  
The checkbox for closing a problem is available if the _Allow manual close_ option is checked in [trigger configuration](/documentation/current/en/manual/config/triggers/trigger) for at least one of the selected problems. Only those problems will be closed that are allowed to be closed when clicking on _Update_.  
If no problem is manually closeable, the checkbox is disabled.  
Already closed problems will not be closed repeatedly.  
  
#### Display

Based on acknowledgment information it is possible to configure how the problem count is displayed in the dashboard or maps. To do that, you have to make selections in the _Problem display_ option, available in both [map configuration](/documentation/current/en/manual/config/visualization/maps/map#creating-a-map) and the _Problems by severity_ [dashboard widget](/documentation/current/en/manual/web_interface/frontend_sections/dashboards##adding-widgets). It is possible to display all problem count, unacknowledged problem count as separated from the total or unacknowledged problem count only.

Based on problem update information (acknowledgment, etc.), it is possible to configure update operations - send a message or execute remote commands.