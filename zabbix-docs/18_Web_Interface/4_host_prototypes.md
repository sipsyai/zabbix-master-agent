---
title: Host prototypes
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/data_collection/templates/discovery/host_prototypes
downloaded: 2025-11-14 10:39:05
---

# 4 Host prototypes

#### Overview

In this section the configured host prototypes of a low-level discovery rule on the template are displayed.

If the template is linked to the host, host prototypes will become the basis of creating real [hosts](/documentation/current/en/manual/web_interface/frontend_sections/data_collection/hosts) during low-level discovery.

![](/documentation/current/assets/en/manual/web_interface/template_host_prototypes.png)

Displayed data:

_Name_ | Name of the host prototype, displayed as a blue link.  
Clicking on the name opens the host prototype configuration form.  
If the host prototype belongs to a linked template, the template name is displayed before the host name as a gray link. Clicking on the template link opens the host prototype list on the linked template level.  
---|---  
_Templates_ | Templates of the host prototype are displayed.  
_Create enabled_ | Create the host based on this prototype as:  
**Yes** \- enabled  
**No** \- disabled. You can switch between 'Yes' and 'No' by clicking on them.  
_Discover_ | Discover the host based on this prototype:  
**Yes** \- discover  
**No** \- do not discover. You can switch between 'Yes' and 'No' by clicking on them.  
_Tags_ | Tags of the host prototype are displayed.  
  
To configure a new host prototype, click on the _Create host prototype_ button at the upper-right corner.

##### Mass editing options

Buttons below the list offer some mass-editing options:

  * _Create enabled_ \- create these hosts as _Enabled_
  * _Create disabled_ \- create these hosts as _Disabled_
  * _Delete_ \- delete these host prototypes

To use these options, mark the checkboxes before the respective host prototypes, then click on the required button.