---
title: Page parameters
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/page_parameters
downloaded: 2025-11-14 10:39:38
---

# 6 Page parameters

#### Overview

Most Zabbix web interface pages support various HTTP GET parameters that control what will be displayed. They may be passed by specifying parameter=value pairs after the URL, separated from the URL by a question mark (?) and from each other by ampersands (&).

#### Monitoring > Problems

The following parameters are supported:

_show_ | Filter option _Show_.  
  
Possible values:  
1 - recent problems;  
2 - all;  
3 - in problem state. | show=1  
---|---|---  
_name_ | Filter option _Problem_ : freeform string. | name=Zabbix agent  
_severities_ | Filter option _Severity_ : array of selected severities in the format `severities[*]=*` (replace * with severity level).   
  
Possible values:   
0 - not classified;  
1 - information;  
2 - warning;  
3 - average;  
4 - high;  
5 - disaster. | severities[3]=3  
_inventory_ | Filter option _Host inventory_ : array of inventory fields `[field],[value]` | inventory[0][field]=type&inventory[0][value]=interface  
_evaltype_ | Filter option _Tags_ : tag [evaluation method](/documentation/current/en/manual/web_interface/frontend_sections/monitoring/problems#using-filter).  
  
Possible values:  
0 - and/or;  
2 - or. | evaltype=0  
_tags_ | Filter option _Tags_ : array of defined tags `[tag], [operator], [value]`  
  
Possible [operator](/documentation/current/en/manual/web_interface/frontend_sections/monitoring/problems#using-filter) values:  
0 - contains;  
1 - equals;  
2 - does not contain;  
3 - does not equal;  
4 - exists;  
5 - does not exist. | tags[0][tag]=target&tags[0][operator]=1&tags[0][value]=database  
_show_tags_ | Filter option _Show tags_.  
  
Possible values:  
0 - none;  
1 - one;  
2 - two;  
3 - three. | show_tags=3  
_tag_name_format_ | Filter option _Tag name_.  
  
Possible values:  
0 - full name;  
1 - shortened name;  
2 - none. | tag_name_format=1  
_tag_priority_ | Filter option _Tag display priority_ : comma-separated string of tag display priority | tag_priority=customer, target  
_show_suppressed_ | Filter option _Show suppressed problems_.   
  
Possible values:  
1 - show;  
2 - do not show. | show_suppressed=1  
_acknowledgement_status_ | Filter option _Acknowledgement status_.  
  
Possible values:  
0 - all;  
1 - unacknowledged;  
2 - acknowledged. | acknowledgement_status=0  
_acknowledged_by_me_ | Filter option _By me_ ; supported only with `acknowledgement_status=2`.  
  
Possible values:  
0 - disabled;  
1 - enabled. | acknowledged_by_me=1  
_compact_view_ | Filter option _Compact view_.  
  
Possible values:  
0 - disabled;  
1 - enabled. | compact_view=1  
_highlight_row_ | Filter option _Highlight whole row_.  
  
Possible values:  
0 - disabled;  
1 - enabled.  
  
For Zabbix versions earlier than 7.4.3, this option is supported only when `compact_view=1`. | highlight_row=1  
_filter_name_ | Filter properties option _Name_ : freeform string | filter_name=Databases  
_filter_show_counter_ | Filter properties option _Show number of records_.  
  
Possible values:  
0 - disabled;  
1 - enabled. | filter_show_counter=1  
_filter_custom_time_ | Filter properties option _Set custom time period_.  
  
Possible values:  
0 - disabled;  
1 - enabled. | filter_custom_time=1  
_sort_ | Column to sort by.  
  
Possible values:  
clock - sort by _Time_ column;  
host - sort by _Host_ column;  
severity - sort by _Severity_ column;  
name - sort by _Problem_ column. | sort=clock  
_sortorder_ | Sort order of results.  
  
Possible values:  
DESC - descending;  
ASC - ascending. | sortorder=DESC  
_age_state_ | Filter option _Age less than_ ; supported only with `show=3`.   
  
Possible values:  
0 - disable `age` parameter;  
1 - enable `age` parameter. | age_state=1  
_age_ | Filter option _Age less than_ : integer, number of days; supported only with `age_state=1` and `show=3`. | age=7  
_groupids_ | Filter option _Host groups_ : array of host group IDs. | groupids[]=4  
_hostids_ | Filter option _Hosts_ : array of host IDs | hostids[]=10084  
_triggerids_ | Filter option _Triggers_ : array of trigger IDs | triggerids[]=22382  
_show_timeline_ | Filter option _Show timeline_ ; not supported with `compact_view=1`.   
  
Possible values:  
0 - do not show;  
1 - show. | show_timeline=1  
_details_ | Filter option _Show details_.   
  
Possible values:  
0 - do not show;  
1 - show. | details=1  
_from_ | Date range start, can be relative (e.g., now-1m); supported only with `filter_custom_time=1` | from=now-2h  
_to_ | Date range end, can be relative (e.g., now-1m); supported only with `filter_custom_time=1` | to=now  
  
See also: Problems page [filter options](/documentation/current/en/manual/web_interface/frontend_sections/monitoring/problems#using-filter).

#### Kiosk mode

The kiosk mode in supported frontend pages can be activated using URL parameters. For example, in dashboards:

  * `/zabbix.php?action=dashboard.view&kiosk=1` \- activate kiosk mode
  * `/zabbix.php?action=dashboard.view&kiosk=0` \- activate normal mode

#### Slideshow

It is possible to activate a slideshow in the dashboard:

  * `/zabbix.php?action=dashboard.view&slideshow=1` \- activate slideshow