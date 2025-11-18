---
title: Host groups
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/data_collection/hostgroups
downloaded: 2025-11-14 10:38:56
---

# 2 Host groups

#### Overview

In the _Data collection_ → _Host groups_ section users can configure and maintain host groups.

A listing of existing host groups with their details is displayed. You can search and filter host groups by name.

![](/documentation/current/assets/en/manual/web_interface/host_groups1.png)

Displayed data:

_Name_ | Name of the host group. Clicking on the group name opens the group [configuration form](/documentation/current/en/manual/config/hosts/host_groups#configuration).  
Discovered host groups are displayed with low-level discovery rule names as a prefix. Clicking on the LLD rule name opens the host prototype [configuration form](/documentation/current/en/manual/discovery/low_level_discovery/host_prototypes#configuration). Note that discovered host groups are deleted when all LLD rules that discovered it are deleted.  
---|---  
_Hosts_ | Number of hosts in the group (displayed in gray) followed by the list of group members.   
Clicking on a host name will open the host configuration form.  
Clicking on the number will, in the whole listing of hosts, filter out those that belong to the group.  
_Info_ | Error information (if any) regarding the host group is displayed.  
  
##### Mass editing options

Buttons below the list offer some mass-editing options:

  * _Enable hosts_ \- change the status of all hosts in the group to "Monitored"
  * _Disable hosts_ \- change the status of all hosts in the group to "Not monitored"
  * _Delete_ \- delete the host groups

To use these options, mark the checkboxes before the respective host groups, then click on the required button.

##### Using filter

You can use the filter to display only the host groups you are interested in. For better search performance, data is searched with macros unresolved.