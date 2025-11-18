---
title: Problems
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/monitoring/problems
downloaded: 2025-11-14 10:38:32
---

# 1 Problems  
  
#### Overview

In _Monitoring > Problems_ you can see what problems you currently have. Problems are those triggers that are in the "Problem" state.

By default all new problems are classified as cause problems. It is possible to manually reclassify certain problems as symptom problem of the cause problem. For more details, see [cause and symptom events](/documentation/current/en/manual/web_interface/frontend_sections/monitoring/problems/cause_and_symptom).

![](/documentation/current/assets/en/manual/web_interface/problems.png)

_Checkbox_ | Checkboxes for problem selection are displayed.  
Icons, next to the checkboxes, have the following meaning:  
![icon_number.png](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/icon_number.png) \- the number of symptom events for the cause problem;  
![icon_expand.png](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/icon_expand.png) \- expand to show symptom events;  
![icon_collapse.png](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/icon_collapse.png) \- collapse to hide symptom events;  
![icon_symptom.png](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/icon_symptom.png) \- this is a symptom event.  
---|---  
_Time_ | Problem start time is displayed.  
_Severity_ | Problem severity is displayed.  
Problem severity is originally based on the severity of the underlying problem trigger, however, after the event has happened it can be updated using the _Update problem_ [screen](/documentation/current/en/manual/acknowledgment#updating-problems). Color of the problem severity is used as cell background during problem time.  
_Recovery time_ | Problem resolution time is displayed.  
_Status_ | Problem status is displayed:  
**Problem** \- unresolved problem  
**Resolved** \- recently resolved problem. You can hide recently resolved problems using the filter.  
New and recently resolved problems blink for 2 minutes. Resolved problems are displayed for 5 minutes in total. Both of these values are configurable in _Administration_ > _General_ > _[Trigger displaying options](/documentation/current/en/manual/web_interface/frontend_sections/administration/general#trigger-displaying-options)_.  
_Info_ | A green information icon is displayed if a problem is closed by global correlation or manually when updating the problem. Rolling a mouse over the icon will display more details:  
![info.png](/documentation/current/assets/en/manual/web_interface/info.png)  
The following icon is displayed if a suppressed problem is being shown (see _Show suppressed problems_ option in the filter). Rolling a mouse over the icon will display more details:  
![](/documentation/current/assets/en/manual/web_interface/info_suppressed2.png)  
_Host_ | Problem host is displayed.   
Clicking on the host name brings up the [host menu](/documentation/current/en/manual/web_interface/menu/host_menu).  
_Problem_ | Problem name is displayed.  
Problem name is based on the name of the underlying problem trigger.  
Macros in the trigger name are resolved at the time of the problem happening and the resolved values do not update any more.  
_Note_ that it is possible to append the problem name with operational data showing some latest item values.  
Clicking on the problem name brings up the [event menu](/documentation/current/en/manual/web_interface/menu/event_menu).  
Hovering on the ![](/documentation/current/assets/en/manual/web_interface/item_description_icon.png) icon after the problem name will bring up the trigger description (for those problems that have it).  
_Operational data_ | Operational data are displayed containing latest item values.  
Operational data can be a combination of text and item value macros if configured on a trigger level. If no operational data is configured on a trigger level, the latest values of all items from the expression are displayed.  
This column is only displayed if _Separately_ is selected for _Show operational data_ in the filter.  
_Duration_ | Problem duration is displayed.  
See also: Negative problem duration  
_Update_ | Click on the _Update_ link to go to the [problem update](/documentation/current/en/manual/acknowledgment#updating-problems) screen where various actions can be taken on the problem, including commenting and acknowledging the problem.  
_Actions_ | History of activities about the problem is displayed using symbolic icons:  
![icon_acknowledged_green.png](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/icon_acknowledged_green.png) \- problem has been acknowledged. This icon is always displayed first.  
![icon_comment.png](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/icon_comment.png) \- comments have been made. The number of comments is also displayed.  
![icon_sev_up1.png](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/icon_sev_up1.png) \- problem severity has been increased (e.g. Information → Warning)  
![icon_sev_down1.png](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/icon_sev_down1.png) \- problem severity has been decreased (e.g. Warning → Information)  
![icon_severity_back.png](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/icon_severity_back.png) \- problem severity has been changed, but returned to the original level (e.g. Warning → Information → Warning)  
![icon_actions.png](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/icon_actions.png) \- actions have been taken. The number of actions is also displayed.  
![icon_actions_progress1.png](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/icon_actions_progress1.png) \- actions have been taken, at least one is in progress. The number of actions is also displayed.  
![icon_actions_failed.png](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/icon_actions_failed.png) \- actions have been taken, at least one has failed. The number of actions is also displayed.  
When rolling the mouse over the icons, popups with details about the activity are displayed. See viewing details to learn more about icons used in the popup for actions taken.  
_Tags_ | [Tags](/documentation/current/en/manual/config/tagging) are displayed (if any).  
In addition, tags from an external ticketing system may also be displayed (see the _Process tags_ option when configuring [webhooks](/documentation/current/en/manual/config/notifications/media/webhook)).  
  
#### Operational data of problems

It is possible to display operational data for current problems, i.e. the latest item values as opposed to the item values at the time of the problem.

Operational data display can be configured in the filter of _Monitoring_ > _Problems_ or in the configuration of the respective [dashboard widget](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/problems), by selecting one of the three options:

  * _None_ \- no operational data is displayed
  * _Separately_ \- operational data is displayed in a separate column

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/problem_live_data_b0.png)

  * _With problem name_ \- operational data is appended to the problem name and in parentheses. Operational data are appended to the problem name only if the _Operational data_ field is non-empty in the trigger configuration.

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/problem_live_data_a0.png)

The content of operational data can be configured with each [trigger](/documentation/current/en/manual/config/triggers/trigger), in the _Operational data_ field. This field accepts an arbitrary string with macros, most importantly, the `{ITEM.LASTVALUE<1-9>}` macro.

`{ITEM.LASTVALUE<1-9>}` in this field will always resolve to the latest values of items in the trigger expression. `{ITEM.VALUE<1-9>}` in this field will resolve to the item values at the moment of trigger status change (i.e. change into problem, change into OK, being closed manually by a user or being closed by correlation).

Note that closing the problem manually does not produce a new value so the resolved value of `{ITEM.LASTVALUE<1-9>}` or `{ITEM.VALUE<1-9>}` will still show the value from the problem time.

`{ITEM.LASTVALUE<1-9>}` or `{ITEM.VALUE<1-9>}` will resolve to *UNKNOWN* if the latest history value has been collected more than the _Max history display period_ time ago (see _[Administration> General](/documentation/current/en/manual/web_interface/frontend_sections/administration/general#gui)_).

#### Negative problem duration

It is actually possible in some common situations to have negative problem duration i.e. when the problem resolution time is earlier than problem creation time, e. g.:

  * If some host is monitored by proxy and a network error happens, leading to no data received from the proxy for a while, the nodata(/host/key) trigger will be fired by the server. When the connection is restored, the server will receive item data from the proxy having a time from the past. Then, the nodata(/host/key) problem will be resolved and it will have a negative problem duration;
  * When item data that resolve the problem event are sent by Zabbix sender and contain a timestamp earlier than the problem creation time, a negative problem duration will also be displayed.

Negative problem duration is not affecting [SLA calculation](/documentation/current/en/manual/it_services) or [Availability report](/documentation/current/en/manual/web_interface/frontend_sections/reports/availability) of a particular trigger in any way; it neither reduces nor expands problem time.

##### Mass editing options

Buttons below the list offer some mass-editing options:

  * _Mass update_ \- update the selected problems by navigating to the [problem update](/documentation/current/en/manual/acknowledgment#updating-problems) screen

To use this option, mark the checkboxes before the respective problems, then click on the _Mass update_ button.

##### Buttons

The button to the right offers the following option:

![](/documentation/current/assets/en/manual/web_interface/button_csv.png) | Export content from all pages to a CSV file.  
---|---  
  
View mode buttons, being common for all sections, are described on the [Monitoring](/documentation/current/en/manual/web_interface/frontend_sections/monitoring#view-mode-buttons) page.

#### Using filter

You can use the filter to display only the problems you are interested in. For better search performance, data is searched with macros unresolved.

The filter is located above the table. Favorite filter settings can be saved as tabs and then quickly accessed by clicking on the [tabs above the filter](/documentation/current/en/manual/web_interface/frontend_sections/monitoring/problems#tabs-for-favorite-filters).

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/problem_filter.png)

_Show_ | Filter by problem status:  
**Recent problems** \- unresolved and recently resolved problems are displayed (default)  
**Problems** \- unresolved problems are displayed  
**History** \- history of all events is displayed  
---|---  
_Host groups_ | Filter by one or more host groups.  
Specifying a parent host group implicitly selects all nested host groups.  
_Hosts_ | Filter by one or more hosts.  
_Triggers_ | Filter by one or more triggers.  
_Problem_ | Filter by problem name.  
_Severity_ | Filter by trigger (problem) severity.  
_Age less than_ | Filter by how old the problem is.  
_Show symptoms_ | Mark the checkbox to display in its own line problems classified as symptoms.  
_Show suppressed problems_ | Mark the checkbox to display problems that would otherwise be suppressed (not shown) because of host maintenance or single [problem suppression](/documentation/current/en/manual/acknowledgment/suppression).  
_Acknowledgement status_ | Filter to display all problems, unacknowledged problems only, or acknowledged problems only. Mark the additional checkbox to filter out those problems ever acknowledged by you.  
_Host inventory_ | Filter by inventory type and value.  
_Tags_ | Filter by [event tag](/documentation/current/en/manual/config/tagging) name and value. It is possible to include as well as exclude specific tags and tag values. Several conditions can be set. Tag name matching is always case-sensitive.  
There are several operators available for each condition:  
**Exists** \- include the specified tag names  
**Equals** \- include the specified tag names and values (case-sensitive)  
**Contains** \- include the specified tag names where the tag values contain the entered string (substring match, case-insensitive)  
**Does not exist** \- exclude the specified tag names  
**Does not equal** \- exclude the specified tag names and values (case-sensitive)  
**Does not contain** \- exclude the specified tag names where the tag values contain the entered string (substring match, case-insensitive)  
There are two calculation types for conditions:  
**And/Or** \- all conditions must be met, conditions having the same tag name will be grouped by the Or condition  
**Or** \- enough if one condition is met  
When filtered, the tags specified here will be displayed first with the problem, unless overridden by the _Tag display priority_ (see below) list.  
_Show tags_ | Select the number of displayed tags:  
**None** \- no _Tags_ column in _Monitoring > Problems_  
**1** \- _Tags_ column contains one tag  
**2** \- _Tags_ column contains two tags  
**3** \- _Tags_ column contains three tags  
To see all tags for the problem roll your mouse over the three dots icon.  
_Tag name_ | Select tag name display mode:  
**Full** \- tag names and values are displayed in full  
**Shortened** \- tag names are shortened to 3 symbols; tag values are displayed in full  
**None** \- only tag values are displayed; no names  
_Tag display priority_ | Enter tag display priority for a problem, as a comma-separated list of tags (for example: `customer,scope,component`). Tag names only should be used, no values. The tags of this list will always be displayed first, overriding the natural ordering by alphabet.  
_Show operational data_ | Select the mode for displaying operational data:  
**None** \- no operational data is displayed  
**Separately** \- operational data is displayed in a separate column  
**With problem name** \- append operational data to the problem name, using parentheses for the operational data  
_Compact view_ | Mark the checkbox to enable compact view.  
_Show details_ | Mark the checkbox to display underlying trigger expressions of the problems. Disabled if _Compact view_ checkbox is marked.  
_Show timeline_ | Mark the checkbox to display the visual timeline and grouping. Disabled if _Compact view_ checkbox is marked.  
_Highlight whole row_ | Mark the checkbox to highlight the full line for unresolved problems. The problem severity color is used for highlighting.  
_Highlight whole row_ is not available in the high-contrast themes.  
  
For Zabbix versions earlier than 7.4.3, this option is supported only when _Compact view_ checkbox is marked in the standard blue and dark themes.  
  
##### Tabs for favorite filters

Frequently used sets of filter parameters can be saved in tabs.

To save a new set of filter parameters, open the main tab, and configure the filter settings, then press the _Save as_ button. In a new popup window, define _Filter properties_.

![problem_filter0.png](/documentation/current/assets/en/manual/web_interface/filter_properties.png)

_Name_ | The name of the filter to display in the tab list.  
---|---  
_Show number of records_ | Check, if you want the number of problems to be displayed next to the tab name.  
_Override time period selector_ | Check to set specific default time period for this filter set. If set, you will only be able to change the time period for this tab by updating filter settings. For tabs without a custom time period, the time range can be changed by pressing the time selector button in the upper-right corner (button name depends on selected time interval: This week, Last 30 minutes, Yesterday, etc.).  
This option is available only for filters in _Monitoring > Problems_.  
_From/To_ | [Time period](/documentation/current/en/manual/web_interface/time_period_selector) start and end in absolute (`Y-m-d H:i:s`) or relative time syntax (`now-1d`). Available if _Set custom time period_ is checked.  
  
When saved, the filter is created as a named filter tab and immediately activated.

To edit the filter properties of an existing filter, press the gear symbol next to the active tab name.

![problem_filter2.png](/documentation/current/assets/en/manual/web_interface/filter_properties_link.png)

Notes:

  * To hide the filter area, click on the name of the current tab. Click on the active tab name again to open the filter area again.
  * Keyboard navigation is supported: use arrows to switch between tabs, press _Enter_ to open.
  * The left/right buttons above the filter may be used to switch between saved filters. Alternatively, the downward pointing button opens a drop-down menu with all saved filters and you can click on the one you need.
  * Filter tabs can be re-arranged by dragging and dropping.
  * If the settings of a saved filter have been changed (but not saved), a green dot is displayed after the filter name. To update the filter according to the new settings, click on the _Update_ button, which is displayed instead of the _Save as_ button.
  * Current filter settings are remembered in the user profile. When the user opens the page again, the filter settings will have stayed the same.

To share filters, copy and send to others a URL of an active filter. After opening this URL, other users will be able to save this set of parameters as a permanent filter in their Zabbix account.  
See also: [Page parameters](/documentation/current/en/manual/web_interface/page_parameters).

##### Filter buttons

![filter_apply.png](/documentation/current/assets/en/manual/web_interface/filter_apply.png) | Apply specified filtering criteria (without saving).  
---|---  
![filter_reset.png](/documentation/current/assets/en/manual/web_interface/filter_reset.png) | Reset current filter and return to saved parameters of the current tab. On the main tab, this will clear the filter.  
![filter_save_as.png](/documentation/current/assets/en/manual/web_interface/filter_save_as.png) | Save current filter parameters in a new tab. Only available on the main tab.  
![filter_update.png](/documentation/current/assets/en/manual/web_interface/filter_update.png) | Replace tab parameters with currently specified parameters. Not available on the main tab.  
  
#### Viewing details

The times for problem start and recovery in _Monitoring > Problems_ are links. Clicking on them opens more details of the event.

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/event_details.png)

Note that the problem severity may differ for the trigger and the problem event - if it has been updated for the problem event using the _Update problem_ [screen](/documentation/current/en/manual/acknowledgment#updating-problems).

In the action list, the following icons are used to denote the activity type:

  * ![icon_generated.png](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/icon_generated.png) \- problem event generated
  * ![icon_message.png](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/icon_message.png) \- message has been sent
  * ![icon_acknowledged.png](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/icon_acknowledged.png) \- problem event acknowledged
  * ![icon_unacknowledged.png](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/icon_unacknowledged.png) \- problem event unacknowledged
  * ![icon_comment2.png](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/icon_comment2.png) \- a comment has been added
  * ![icon_sev_up1.png](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/icon_sev_up1.png) \- problem severity has been increased (e.g. Information → Warning)
  * ![icon_sev_down1.png](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/icon_sev_down1.png) \- problem severity has been decreased (e.g. Warning → Information)
  * ![icon_severity_back.png](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/icon_severity_back.png) \- problem severity has been changed, but returned to the original level (e.g. Warning → Information → Warning)
  * ![icon_remote.png](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/icon_remote.png) \- a remote command has been executed
  * ![icon_recovery.png](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/icon_recovery.png) \- problem event has recovered
  * ![icon_closed.png](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/icon_closed.png) \- the problem has been closed manually
  * ![icon_suppression.png](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/icon_suppression.png) \- the problem has been suppressed
  * ![icon_unsuppressed.png](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/icon_unsuppressed.png) \- the problem has been unsuppressed
  * ![icon_symptom.png](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/icon_symptom.png) \- the problem has been converted to a symptom problem
  * ![icon_cause.png](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/icon_cause.png) \- the problem has been converted to a cause problem