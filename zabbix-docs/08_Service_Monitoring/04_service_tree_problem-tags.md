---
title: tagging
source: https://www.zabbix.com/documentation/current/en/manual/it_services/service_tree#problem-tags
downloaded: 2025-11-14 10:36:51
---

# 1 Service tree

The service tree is configured in the _Services - > Services_ menu section. In the upper-right corner, switch from [View](/documentation/current/en/manual/web_interface/frontend_sections/services/service#viewing-services) to the Edit mode.

![](/documentation/current/assets/en/manual/config/service_config.png)

To configure a new service, click on the _Create service_ button in the upper-right corner.

To quickly add a child service, you can alternatively press a plus icon next to the parent service. This will open the same service configuration form, but the _Parent services_ parameter will be pre-filled.

### Service configuration

In the **Service** tab, specify required service parameters:

![](/documentation/current/assets/en/manual/web_interface/service.png)

All mandatory input fields are marked with a red asterisk.

_**Name**_ | Service name.  
---|---  
_**Parent services**_ | Parent services the service belongs to.  
Leave this field empty if you are adding the service of highest level.  
One service may have multiple parent services. In this case, it will be displayed in the service tree under each of the parent services.  
_**Problem tags**_ | Specify tags to map problem data to the service.  
Several conditions can be set. Tag name matching is always case-sensitive.  
There are two operators available for each condition:  
**Equals** \- include the specified tag names and values (case-sensitive)  
**Contains** \- include the specified tag names where the tag values contain the entered string (substring match, case-sensitive)  
_**Sort order**_ | Sort order for display, lowest comes first.  
_**Status calculation rule**_ | Rule for calculating service status:  
**Most critical if all children have problems** \- the most critical problem in the child services is used to color the service status, if all children have problems  
**Most critical of child services** \- the most critical problem in the child services is used to color the service status  
**Set status to OK** \- do not calculate service status  
Additional status calculation rules can be configured in the advanced configuration options.  
_**Description**_ | Service description.  
_**Created at**_ | The time when the service was created; displayed when editing an existing service.  
_**Advanced configuration**_ | Click on the _Advanced configuration_ label to display advanced configuration options.  
  
#### Advanced configuration

![](/documentation/current/assets/en/manual/web_interface/service_a.png)

_**Additional rules**_ | Click on _Add_ to configure additional status calculation rules.  
---|---  
_Set status to_ | Set service status to either _OK_ (default), _Not classified_ , _Information_ , _Warning_ , _Average_ , _High_ or _Disaster_ in case of a condition match.  
_Condition_ | Select the condition for direct child services:  
**if at least (N) child services have (Status) status or above**  
**if at least (N%) of child services have (Status) status or above**  
**if less than (N) child services have (Status) status or below**  
**if less than (N%) of child services have (Status) status or below**  
**if weight of child services with (Status) status or above is at least (W)**  
**if weight of child services with (Status) status or above is at least (N%)**  
**if weight of child services with (Status) status or below is less than (W)**  
**if weight of child services with (Status) status or below is less than (N%)**   
  
If several conditions are specified and the situation matches more than one condition, the highest severity will be set.  
_N (W)_ | Set the value of N or W (1-100000), or N% (1-100) in the condition.  
_Status_ | Select the value of _Status_ in the condition: _OK_ (default), _Not classified_ , _Information_ , _Warning_ , _Average_ , _High_ or _Disaster_.  
_**Status propagation rule**_ | Rule for propagating the service status to the parent service:  
**As is** \- the status is propagated without change  
**Increase by** \- you may increase the propagated status by 1 to 5 severities  
**Decrease by** \- you may decrease the propagated status by 1 to 5 severities  
**Ignore this service** \- the status is not propagated to the parent service at all  
**Fixed status** \- the status is propagated statically, i.e. as always the same  
_**Weight**_ | Weight of the service (integer in the range from 0 (default) to 1000000).  
  
Additional status calculation rules can only be used to increase severity level over the level calculated according to the main _Status calculation rule_ parameter. If according to additional rules the status should be Warning, but according to the _Status calculation rule_ the status is Disaster - the service will have status Disaster.

The **Tags** tab contains service-level tags. Service-level tags are used to identify a service. Tags of this type are not used to map problems to the service (for that, use _Problem tags_ from the first tab).

The **Child services** tab allows to specify dependant services. Click on _Add_ to add a service from the list of existing services. If you want to add a new child service, save this service first, then click on a plus icon next to the service that you have just created.

### Tags

There are two different types of tags in services:

  * Service tags
  * Problem tags

#### Service tags

Service tags are used to match services with [service actions](/documentation/current/en/manual/config/notifications/action) and [SLAs](/documentation/current/en/manual/it_services/sla). These tags are specified at the _Tags_ service configuration tab. For mapping SLAs, _OR_ logic is used: a service will be mapped to an SLA if it has at least one matching tag. In service actions, mapping rules are configurable and can use either _AND_ , _OR_ , or _AND/OR_ logic.

![](/documentation/current/assets/en/manual/config/service_tags.png)

#### Problem tags

Problem tags are used to match problems and services. These tags are specified at the primary service configuration tab.

Only child services of the lowest hierarchy level may have problem tags defined and be directly correlated to problems. If problem tags match, the service status will change to the same status as the problem has. In case of several problems, a service will have the status of the most severe one. Status of a parent service is then calculated based on child services statuses according to Status calculation rules.

If several tags are specified, _AND_ logic is used: a problem must have all tags specified in the service configuration to be mapped to the service.

![](/documentation/current/assets/en/manual/config/problem_tags.png)

A problem in Zabbix inherits tags from the whole chain of templates, hosts, items, web scenarios, and triggers. Any of these tags can be used for matching problems to services.

_Example:_

Problem _Web camera 3 is down_ has tags `type:video-surveillance`, `floor:1` and `name:webcam-3` and status _Warning_

The service **Web camera 3** has the only problem tag specified: `name:webcam-3`

![](/documentation/current/assets/en/manual/config/services_example_tags.png)

Service status will change from _OK_ to _Warning_ when this problem is detected.

If the service **Web camera 3** had problem tags `name:webcam-3` and `floor:2`, its status would not be changed, when the problem is detected, because the conditions are only partially met.

### Modifying existing services

The buttons described below are visible only when _Services_ section is in the Edit mode.

To edit an existing service, press the pencil icon next to the service.

To clone an existing service, press the pencil icon to open its configuration and then press Clone button. When a service is cloned, its parent links are preserved, while the child links are not.

To delete a service, press on the `x` icon next to it. When you delete a parent service, its child services will not be deleted and will move one level higher in the service tree (1st level children will get the same level as the deleted parent service).

Two buttons below the list of services offer some mass-editing options:

  * _Mass update_ \- mass update service properties
  * _Delete_ \- delete the services

To use these options, mark the checkboxes before the respective services, then click on the required button.