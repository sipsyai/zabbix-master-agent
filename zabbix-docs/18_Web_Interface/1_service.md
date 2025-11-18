---
title: Services
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/services/service
downloaded: 2025-11-14 10:38:42
---

# 1 Services

### Overview

In this section you can see a high-level status of whole services that have been configured in Zabbix, based on your infrastructure.

A service may be a hierarchy consisting of several levels of other services, called "child" services, which are attributes to the overall status of the service (see also an overview of the [service monitoring](/documentation/current/en/manual/it_services) functionality.)

The main categories of service status are _OK_ or _Problem_ , where the _Problem_ status is expressed by the corresponding problem severity name and color.

While the view mode allows to monitor services with their status and other details, you can also [configure](/documentation/current/en/manual/web_interface/frontend_sections/services/service#editing-services) the service hierarchy in this section (add/edit services, child services) by switching to the edit mode.

To switch from the view to the edit mode (and back) click on the respective button in the upper-right corner:

  * ![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/services_view_mode.png) \- view services
  * ![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/services_edit_mode.png) \- add/edit services, and child services

Note that access to editing depends on [user role](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) settings.

### Viewing services

![](/documentation/current/assets/en/manual/web_interface/services_view.png)

A list of the existing services is displayed.

Displayed data:

_Name_ | Service name.  
The service name is a link to service details.  
The number after the name indicates how many child services the service has.  
---|---  
_Status_ | Service status:  
**OK** \- no problems  
**< problem color and severity>** \- indicates a problem and its severity. In case of multiple problems, the color and severity of the most critical problem are displayed.  
_Root cause_ | Underlying problems that directly or indirectly affect the service status are listed.  
The same problems are listed as returned by the {SERVICE.ROOTCAUSE} [macro](/documentation/current/en/manual/appendix/macros/supported_by_location).  
Click on the problem name to see more details about it in _Monitoring_ → _Problems_.  
Problems that do not affect the service status are not in the list.  
_Created at_ | The time when the service was created is displayed.  
_Tags_ | [Tags](/documentation/current/en/manual/it_services/service_tree#service-tags) of the service are displayed. Tags are used to identify a service in service [actions](/documentation/current/en/manual/web_interface/frontend_sections/alerts/actions) and [SLAs](/documentation/current/en/manual/web_interface/frontend_sections/services/sla).  
  
##### Buttons

View mode buttons being common for all sections are described on the [Monitoring](/documentation/current/en/manual/web_interface/frontend_sections/monitoring#view-mode-buttons) page.

##### Using filter

You can use the filter to display only the services you are interested in.

![](/documentation/current/assets/en/manual/web_interface/services_filter.png)

_Name_ | Filter by service name.  
---|---  
_Status_ | Filter by service status.  
_Only services without children_ | Mark the checkbox to display only services without child services. This parameter is available only in services edit mode.  
_Only services without problem tags_ | Mark the checkbox to display only services without problem tags. This parameter is available only in services edit mode.  
_Tags_ | Filter by service tag name and value, or service problem tag name and value (in services edit mode).  
It is possible to include as well as exclude specific tags and tag values. Several conditions can be set. Tag name matching is always case-sensitive.  
  
There are several operators available for each condition:  
**Exists** \- include the specified tag names;  
**Equals** \- include the specified tag names and values (case-sensitive);  
**Contains** \- include the specified tag names where the tag values contain the entered string (substring match, case-insensitive);  
**Does not exist** \- exclude the specified tag names;  
**Does not equal** \- exclude the specified tag names and values (case-sensitive);  
**Does not contain** \- exclude the specified tag names where the tag values contain the entered string (substring match, case-insensitive).  
  
There are two calculation types for conditions:  
**And/Or** \- all conditions must be met, conditions having the same tag name will be grouped by the Or condition;  
**Or** \- enough if one condition is met.  
  
### Editing services

Click on the _Edit_ button to access the edit mode. When in edit mode, the listing is complemented with checkboxes before the entries and also these additional options:

  * ![](/documentation/current/assets/en/manual/web_interface/add_service.png) \- add a child service to this service
  * ![](/documentation/current/assets/en/manual/web_interface/edit_service.png) \- edit this service
  * ![](/documentation/current/assets/en/manual/web_interface/delete_service.png) \- delete this service

![](/documentation/current/assets/en/manual/web_interface/services_edit.png)

To [configure](/documentation/current/en/manual/it_services/service_tree#service-configuration) a new service, click on the _Create service_ button in the upper-right corner.

### Service details

To access service details, click on the service name. To return to the list of all services, click on _All services_.

Service details include the info box and the list of child services.

![](/documentation/current/assets/en/manual/web_interface/service_details.png)

To access the info box, click on the _Info_ tab. The info box contains the following entries:

  * Names of parent services (if any)
  * Current status of this service
  * Current SLA(s) of this service, in the format `SLA name:service level indicator`. 'SLA name' is also a link to the SLA report for this service. If you position the mouse on the info box next to the service-level indicator (SLI), a pop-up info list is displayed with SLI details. The service-level indicator displays the current service level, in percentage.
  * Service tags

The info box also contains a link to the [service configuration](/documentation/current/en/manual/it_services/service_tree#service-configuration).

To use the filter for child services, click on the _Filter_ tab.

When in edit mode, the child service listing is complemented with additional editing options:

  * ![](/documentation/current/assets/en/manual/web_interface/add_service.png) \- add a child service to this service
  * ![](/documentation/current/assets/en/manual/web_interface/edit_service.png) \- edit this service
  * ![](/documentation/current/assets/en/manual/web_interface/delete_service.png) \- delete this service