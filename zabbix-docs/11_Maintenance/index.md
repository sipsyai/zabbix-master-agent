---
title: Maintenance
source: https://www.zabbix.com/documentation/current/en/manual/maintenance
downloaded: 2025-11-14 10:37:03
---

# 11 Maintenance

#### Overview

You can define maintenance periods for hosts and host groups in Zabbix.

Furthermore, it is possible to define maintenance only for a single trigger (or subset of triggers) by specifying trigger tags. In this case maintenance will be activated only for those triggers; all other triggers of the host or host group will not be in maintenance.

There are two maintenance types - with data collection and with no data collection.

During a maintenance "with data collection" triggers are processed as usual and events are created when required. However, problem escalations are paused for hosts/triggers in maintenance, if the _Pause operations for suppressed problems_ option is checked in action configuration. In this case, escalation steps that may include sending notifications or remote commands will be ignored for as long as the maintenance period lasts. Note that problem recovery and update operations are not suppressed during maintenance, only escalations.

For example, if escalation steps are scheduled at 0, 30 and 60 minutes after a problem start, and there is a half-hour long maintenance lasting from 10 minutes to 40 minutes after a real problem arises, steps two and three will be executed a half-hour later, or at 60 minutes and 90 minutes (providing the problem still exists). Similarly, if a problem arises during the maintenance, the escalation will start after the maintenance.

To receive problem notifications during the maintenance normally (without delay), you have to uncheck the _Pause operations for suppressed problems_ option in action configuration.

If at least one host (used in the trigger expression) is not in maintenance mode, Zabbix will send a problem notification.

Zabbix server must be running during maintenance. Maintenances are recalculated every minute or as soon as the configuration cache is reloaded if there are changes to the maintenance period.

Timer processes check if host status must be changed to/from maintenance at 0 seconds of every minute. Additionally, every second the timer process checks if any maintenances must be started/stopped based on whether there are changes to the maintenance periods after the configuration update. Thus the speed of starting/stopping maintenance periods depends on the configuration [update interval](/documentation/current/en/manual/appendix/config/zabbix_server#cacheupdatefrequency) (10 seconds by default). Note that maintenance period changes do not include _Active since/Active till_ settings. Also, if a host/host group is added to an existing active maintenance period, the changes will only be activated by the timer process at the start of next minute.

Note that when a host enters maintenance, Zabbix server timer processes will read all open problems to check if it is required to suppress those. This may have a performance impact if there are many open problems. Zabbix server will also read all open problems upon startup, even if there are no maintenances configured at the time.

Note that the Zabbix server (or proxy) always collects data regardless of the maintenance type (including "no data" maintenance). The data is later ignored by the server if 'no data collection' is set.

When "no data" maintenance ends, triggers using nodata() function will not fire before the next check during the period they are checking.

If a log item is added while a host is in maintenance and the maintenance ends, only new logfile entries since the end of the maintenance will be gathered.

If a timestamped value is sent for a host that is in a “no data” maintenance type (e.g. using [Zabbix sender](/documentation/current/en/manpages/zabbix_sender)) then this value will be dropped however it is possible to send a timestamped value in for an expired maintenance period and it will be accepted.

If maintenance period, hosts, groups or tags are changed by the user, the changes will only take effect after configuration cache synchronization.

#### Configuration

To configure a maintenance period:

  1. Go to: _Data collection > Maintenance_.
  2. Click on _Create maintenance period_ (or on the name of an existing maintenance period).
  3. Enter maintenance parameters in the form.

![](/documentation/current/assets/en/manual/maintenance/maintenance.png)

All mandatory input fields are marked with a red asterisk.

_Name_ | Name of the maintenance period.  
---|---  
_Maintenance type_ | Two types of maintenance can be set:  
**With data collection** \- data will be collected by the server during maintenance, triggers will be processed;  
**No data collection** \- data will not be collected by the server during maintenance.  
See [Effect of maintenance periods](/documentation/current/en/manual/web_interface/frontend_sections/reports/availability#effect-of-maintenance-periods) for how each type affects the availability report.  
_Active since_ | The date and time when executing maintenance periods becomes active.  
_Note:_ Setting this time alone does not activate a maintenance period; maintenance periods must be configured in _Periods_ (see below).  
_Active till_ | The date and time when executing maintenance periods stops being active.  
_Periods_ | This block allows you to define the exact days and hours when the maintenance takes place. Clicking on ![](/documentation/current/assets/en/manual/maintenance/add_link.png) opens a popup window with a flexible _Maintenance period_ form where you can define maintenance schedule. See Maintenance periods for a detailed description.  
_Host groups_ | Select host groups that the maintenance will be activated for. The maintenance will be activated for all hosts from the specified host group(s). This field is auto-complete, so starting to type in it will display a dropdown of all available host groups.  
Specifying a parent host group implicitly selects all nested host groups. Thus the maintenance will also be activated on hosts from nested groups.  
_Hosts_ | Select hosts that the maintenance will be activated for. This field is auto-complete, so starting to type in it will display a dropdown of all available hosts.  
  
_Tags_ | Specify tags to [suppress problems](/documentation/current/en/manual/acknowledgment/suppression) with matching tags on hosts in maintenance.  
Several conditions can be set. Tag name matching is always case-sensitive.  
  
There are two operators available for each condition:  
**Contains** \- include the specified tag names where the tag values contain the entered string (substring match, case-sensitive);  
**Equals** \- include the specified tag names and values (case-sensitive).  
  
There are two calculation types for conditions:  
**And/Or** \- all conditions must be met, conditions having the same tag name will be grouped by the Or condition;  
**Or** \- enough if one condition is met.  
  
Tags can be specified only if _With data collection_ mode is selected.  
_Description_ | Description of maintenance period.  
  
##### Maintenance periods

The maintenance period window is for scheduling time for a recurring or a one-time maintenance. The form is dynamic with available fields changing based on the _Period type_ selected.

![](/documentation/current/assets/en/manual/maintenance/maintenance_period.png)

_One time only_ | Configure a one time only maintenance period:  
_Date_ \- date and time of the maintenance period;  
_Maintenance period length_ \- for how long the maintenance will be active.  
---|---  
_Daily_ | Configure a daily maintenance period:  
_Every day(s)_ \- maintenance frequency (1 - _(default)_ every day, 2 - every two days, etc.);  
_At (hour:minute)_ \- time of the day when maintenance starts;  
_Maintenance period length_ \- for how long the maintenance will be active.  
  
When _Every day(s)_ parameter is greater than "1", the starting day is the day that the _Active since_ time falls on. Examples:  
\- if _Active since_ is set to "2021-01-01 12:00", _Every day(s)_ is set to "2", and _At (hour:minute)_ is set to "23:00", then the first maintenance period will start on January 1 at 23:00, while the second maintenance period will start on January 3 at 23:00;  
\- if _Active since_ is set to "2021-01-01 12:00", _Every day(s)_ is set to "2", and _At (hour:minute)_ is set to "01:00", then the first maintenance period will start on January 3 at 01:00, while the second maintenance period will start on January 5 at 01:00.  
_Weekly_ | Configure a weekly maintenance period:  
_Every week(s)_ \- maintenance frequency (1 - _(default)_ every week, 2 - every two weeks, etc.);  
_Day of week_ \- on which day the maintenance should take place;  
_At (hour:minute)_ \- time of the day when maintenance starts;  
_Maintenance period length_ \- for how long the maintenance will be active.  
  
When _Every week(s)_ parameter is greater than "1", the starting week is the week that the _Active since_ time falls on. For examples, see parameter _Daily_ description above.  
_Monthly_ | Configure a monthly maintenance period:  
_Month_ \- select all months during which the regular maintenance is carried out;  
_Date:**Day of month**_ \- select this option if the maintenance should take place on the same date each month (for example, every 1st day of the month), and then select the required day in the field _Day of month_ that appears;  
_Date:**Day of week**_ \- select this option if the maintenance should take place only on certain days (for example, every first Monday of the month), then select (in the drop-down) the required week of the month (first, second, third, fourth, or last), and then mark the checkboxes for maintenance day(s);  
_At (hour:minute)_ \- time of the day when maintenance starts;  
_Maintenance period length_ \- for how long the maintenance will be active.  
  
When creating a maintenance period, the [time zone](/documentation/current/en/manual/web_interface/time_zone) of the user who creates it is used. However, when recurring maintenance periods (_Daily_ , _Weekly_ , _Monthly_) are scheduled, the time zone of the Zabbix server is used. To ensure predictable behavior of recurring maintenance periods, it is required to use a common time zone for all parts of Zabbix.

When done, press _Add_ to add the maintenance period to the _Periods_ block.

Note that Daylight Saving Time (DST) changes do not affect how long the maintenance will be. For example, let's say that we have a two-hour maintenance configured that usually starts at 01:00 and finishes at 03:00:

  * if after one hour of maintenance (at 02:00) a DST change happens and current time changes from 02:00 to 03:00, the maintenance will continue for one more hour (till 04:00);
  * if after two hours of maintenance (at 03:00) a DST change happens and current time changes from 03:00 to 02:00, the maintenance will stop, because two hours have passed;
  * if a maintenance period starts during the hour that is skipped by a DST change, then the maintenance will not start.

If a maintenance period is set to "1 day" (the actual period of the maintenance is 24 hours, since Zabbix calculates days in hours), starts at 00:00 and finishes at 00:00 the next day:

  * the maintenance will stop at 01:00 the next day if current time changes forward one hour;
  * the maintenance will stop at 23:00 that day if current time changes back one hour.

#### Display

##### Displaying hosts in maintenance

An orange wrench icon ![](/documentation/current/assets/en/manual/web_interface/frontend_sections/configuration/maintenance_wrench_icon.png) next to the host name indicates that this host is in maintenance in:

  * _Dashboards_
  * _Monitoring > Problems_
  * _Inventory > Hosts > Host inventory details_
  * _Data collection > Hosts_ (See 'Status' column)

![](/documentation/current/assets/en/manual/maintenance/maintenance_icon.png)

Maintenance details are displayed when the mouse pointer is positioned over the icon.

Additionally, hosts in maintenance get an orange background in _Monitoring > Maps_.

##### Displaying suppressed problems

Normally problems for hosts in maintenance are suppressed, i.e. not displayed in the frontend. However, it is also possible to configure that suppressed problems are shown, by selecting the _Show suppressed problems_ option in these locations:

  * _Dashboards_ (in _Problem hosts_ , _Problems_ , _Problems by severity_ , _Trigger overview_ widget configuration)
  * _Monitoring_ > _Problems_ (in the filter)
  * _Monitoring_ > _Maps_ (in map configuration)
  * Global [notifications](/documentation/current/en/manual/web_interface/user_profile/global_notifications) (in user profile configuration)

When suppressed problems are displayed, the following icon is displayed: ![](/documentation/current/assets/en/manual/web_interface/icon_suppressed.png). Rolling a mouse over the icon displays more details.

![](/documentation/current/assets/en/manual/web_interface/info_suppressed2.png)

#### Calculation of queues during maintenance

Queues displayed in the Zabbix frontend ([Administration > Queue](/documentation/current/en/manual/web_interface/frontend_sections/administration/queue)) are calculated by the Zabbix server. They do not include items under maintenance with no data collection—queue length is always zero for these items even when their values are delayed. Delayed items in maintenance with data collection are still counted in the queue.

The Zabbix [proxy](/documentation/current/en/manual/concepts/proxy) is not aware of maintenance periods because there is no synchronization of maintenance configuration between the Zabbix server and proxy. Internal checks calculated on Zabbix proxies (for example, [`zabbix[queue,,]`](/documentation/current/en/manual/config/items/itemtypes/internal#queue) and [`zabbix[stats,,,queue,,]`](/documentation/current/en/manual/config/items/itemtypes/internal#stats.queue)) report delayed items regardless of the maintenance status on the Zabbix server.

As a result, different queue lengths may be reported for the same items in maintenance with no data collection by the Zabbix frontend and by internal checks on Zabbix proxies.