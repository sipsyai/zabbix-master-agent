---
title: Web monitoring items
source: https://www.zabbix.com/documentation/current/en/manual/web_monitoring/items
downloaded: 2025-11-14 10:36:54
---

# 1 Web monitoring items

#### Overview

Some new items are automatically added for monitoring when web scenarios are created.

All items inherit tags from the web scenario.

#### Scenario items

As soon as a scenario is created, Zabbix automatically adds the following items for monitoring.

_Download speed for scenario <Scenario>_ | This item will collect information about the download speed (bytes per second) of the whole scenario, i.e. average for all steps.  
Item key: web.test.in[Scenario,,bps]  
Type: _Numeric(float)_  
---|---  
_Failed step of scenario <Scenario>_ | This item will display the number of the step that failed on the scenario. If all steps are executed successfully, 0 is returned.  
Item key: web.test.fail[Scenario]  
Type: _Numeric(unsigned)_  
_Last error message of scenario <Scenario>_ | This item returns the last error message text of the scenario. A new value is stored only if the scenario has a failed step. If all steps are ok, no new value is collected.  
Item key: web.test.error[Scenario]  
Type: _Character_  
  
The actual scenario name will be used instead of "Scenario".

If the scenario name contains [user macros](/documentation/current/en/manual/config/macros/user_macros), these macros will be left unresolved in web monitoring item names.   
  
If the scenario name starts with a doublequote or contains a comma or a square bracket, it will be properly quoted in item keys. In other cases no additional quoting will be performed.

Web monitoring items are added with a 30 day history and a 90 day trend retention period.

These items can be used to create triggers and define notification conditions.

##### Example 1

To create a "Web scenario failed" trigger, you can define a trigger expression:
    
    
    last(/host/web.test.fail[Scenario])<>0

Copy

✔ Copied

Make sure to replace 'Scenario' with the real name of your scenario.

##### Example 2

To create a "Web scenario failed" trigger with a useful problem description in the trigger name, you can define a trigger with name:
    
    
    Web scenario "Scenario" failed: {ITEM.VALUE}

Copy

✔ Copied

and trigger expression:
    
    
    length(last(/host/web.test.error[Scenario]))>0 and last(/host/web.test.fail[Scenario])>0

Copy

✔ Copied

Make sure to replace 'Scenario' with the real name of your scenario.

##### Example 3

To create a "Web application is slow" trigger, you can define a trigger expression:
    
    
    last(/host/web.test.in[Scenario,,bps])<10000

Copy

✔ Copied

Make sure to replace 'Scenario' with the real name of your scenario.

#### Scenario step items

As soon as a step is created, Zabbix automatically adds the following items for monitoring.

_Download speed for step <Step> of scenario <Scenario>_ | This item will collect information about the download speed (bytes per second) of the step.  
Item key: web.test.in[Scenario,Step,bps]  
Type: _Numeric(float)_  
---|---  
_Response time for step <Step> of scenario <Scenario>_ | This item will collect information about the response time of the step in seconds. Response time is counted from the beginning of the request until all information has been transferred.  
Item key: web.test.time[Scenario,Step,resp]  
Type: _Numeric(float)_  
_Response code for step <Step> of scenario <Scenario>_ | This item will collect response codes of the step.  
Item key: web.test.rspcode[Scenario,Step]  
Type: _Numeric(unsigned)_  
  
Actual scenario and step names will be used instead of "Scenario" and "Step" respectively.

Web monitoring items are added with a 30 day history and a 90 day trend retention period.

If scenario name starts with a doublequote or contains comma or square bracket, it will be properly quoted in item keys. In other cases no additional quoting will be performed.

These items can be used to create triggers and define notification conditions. For example, to create a "Zabbix GUI login is too slow" trigger, you can define a trigger expression:
    
    
    last(/zabbix/web.test.time[ZABBIX GUI,Login,resp])>3

Copy

✔ Copied