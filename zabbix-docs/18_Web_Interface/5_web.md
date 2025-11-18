---
title: Web scenarios
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/data_collection/templates/web
downloaded: 2025-11-14 10:39:07
---

# 5 Web scenarios

#### Overview

The [web scenario](/documentation/current/en/manual/web_monitoring) list for a template can be accessed from _Data collection → Templates_ by clicking on _Web_ for the respective template.

A list of existing web scenarios is displayed.

![](/documentation/current/assets/en/manual/web_interface/template_web_scenarios.png)

Displayed data:

_Name_ | Name of the web scenario. Clicking on the web scenario name opens the web scenario [configuration form](/documentation/current/en/manual/web_monitoring#configuring-a-web-scenario).  
If the web scenario is inherited from another template, the template name is displayed before the web scenario name as a gray link. Clicking on the template link opens the web scenario list on that template level.  
---|---  
_Number of steps_ | The number of steps the scenario contains.  
_Update interval_ | How often the scenario is performed.  
_Attempts_ | How many attempts for executing web scenario steps are performed.  
_Authentication_ | Authentication method is displayed - Basic, NTLM on None.  
_HTTP proxy_ | Displays HTTP proxy or 'No' if not used.  
_Status_ | Web scenario status is displayed - _Enabled_ or _Disabled_.  
By clicking on the status you can change it.  
_Tags_ | Web scenario tags are displayed.  
Up to three tags (name:value pairs) can be displayed. If there are more tags, a "..." link is displayed that allows to see all tags on mouseover.  
  
To configure a new web scenario, click on the _Create web scenario_ button at the upper-right corner.

##### Mass editing options

Buttons below the list offer some mass-editing options:

  * _Enable_ \- change the scenario status to _Enabled_
  * _Disable_ \- change the scenario status to _Disabled_
  * _Delete_ \- delete the web scenarios

To use these options, mark the checkboxes before the respective web scenarios, then click on the required button.

##### Using filter

You can use the filter to display only the scenarios you are interested in. For better search performance, data is searched with macros unresolved.

The _Filter_ link is available above the list of web scenarios. If you click on it, a filter becomes available where you can filter scenarios by template group, template, status and tags.

![](/documentation/current/assets/en/manual/web_interface/template_web_scenario_filter.png)