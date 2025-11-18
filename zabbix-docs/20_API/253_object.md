---
title: Role object
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/role/object
downloaded: 2025-11-14 10:44:06
---

# Role object

The following objects are directly related to the `role` API.

### Role

The role object has the following properties:

roleid | ID | ID of the role.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
\- _required_ for update operations  
---|---|---  
name | string | Name of the role.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
type | integer | User type.  
  
Possible values:  
1 - _(default)_ User;  
2 - Admin;  
3 - Super admin.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
readonly | integer | Whether the role is readonly.  
  
Possible values:  
0 - _(default)_ No;  
1 - Yes.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
  
### Role rules

The role rules object has the following properties:

ui | array | Array of the [UI element](object#ui-element) objects.  
---|---|---  
ui.default_access | integer | Whether access to new UI elements is enabled.  
  
Possible values:  
0 - Disabled;  
1 - _(default)_ Enabled.  
services.read.mode | integer | Read-only access to services.  
  
Possible values:  
0 - Read-only access to the services, specified by the `services.read.list` or matched by the `services.read.tag` properties;  
1 - _(default)_ Read-only access to all services.  
services.read.list | array | Array of [Service](object#service) objects.  
  
The specified services, including child services, will be granted a read-only access to the user role. Read-only access will not override read-write access to the services.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `services.read.mode` is set to "0"  
services.read.tag | object | Array of [Service tag](object#service-tag) objects.  
  
The tag matched services, including child services, will be granted a read-only access to the user role. Read-only access will not override read-write access to the services.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `services.read.mode` is set to "0"  
services.write.mode | integer | Read-write access to services.  
  
Possible values:  
0 - _(default)_ Read-write access to the services, specified by the `services.write.list` or matched by the `services.write.tag` properties;  
1 - Read-write access to all services.  
services.write.list | array | Array of [Service](object#service) objects.  
  
The specified services, including child services, will be granted a read-write access to the user role. Read-write access will override read-only access to the services.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `services.write.mode` is set to "0"  
services.write.tag | object | Array of [Service tag](object#service-tag) objects.  
  
The tag matched services, including child services, will be granted a read-write access to the user role. Read-write access will override read-only access to the services.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `services.write.mode` is set to "0"  
modules | array | Array of the [module](object#module) objects.  
modules.default_access | integer | Whether access to new modules is enabled.  
  
Possible values:  
0 - Disabled;  
1 - _(default)_ Enabled.  
api.access | integer | Whether access to API is enabled.  
  
Possible values:  
0 - Disabled;  
1 - _(default)_ Enabled.  
api.mode | integer | Mode for treating API methods listed in the `api` property.  
  
Possible values:  
0 - _(default)_ Deny list;  
1 - Allow list.  
api | array | Array of API methods.  
actions | array | Array of the [action](object#action) objects.  
actions.default_access | integer | Whether access to new actions is enabled.  
  
Possible values:  
0 - Disabled;  
1 - _(default)_ Enabled.  
  
#### UI element

The UI element object has the following properties:

name | string | Name of the UI element.  
  
Possible values if `type` of the Role object is set to "User", "Admin", or "Super admin":  
`monitoring.dashboard` \- _Dashboards_ ;  
`monitoring.problems` \- _Monitoring → Problems_ ;  
`monitoring.hosts` \- _Monitoring → Hosts_ ;  
`monitoring.latest_data` \- _Monitoring → Latest data_ ;  
`monitoring.maps` \- _Monitoring → Maps_ ;  
`services.services` \- _Services → Services_ ;  
`services.sla_report` \- _Services → SLA report_ ;  
`inventory.overview` \- _Inventory → Overview_ ;  
`inventory.hosts` \- _Inventory → Hosts_ ;  
`reports.availability_report` \- _Reports → Availability report_ ;  
`reports.top_triggers` \- _Reports → Triggers top 100_.  
  
Possible values if `type` of the Role object is set to "Admin" or "Super admin":  
`monitoring.discovery` \- _Monitoring → Discovery_ ;  
`services.sla` \- _Services → SLA_ ;  
`reports.scheduled_reports` \- _Reports → Scheduled reports_ ;  
`reports.notifications` \- _Reports → Notifications_ ;  
`configuration.template_groups` \- _Data collection → Template groups_ ;  
`configuration.host_groups` \- _Data collection → Host groups_ ;  
`configuration.templates` \- _Data collection → Templates_ ;  
`configuration.hosts` \- _Data collection → Hosts_ ;  
`configuration.maintenance` \- _Data collection → Maintenance_ ;  
`configuration.discovery` \- _Data collection → Discovery_ ;  
`configuration.trigger_actions` \- _Alerts → Actions → Trigger actions_ ;  
`configuration.service_actions` \- _Alerts → Actions → Service actions_ ;  
`configuration.discovery_actions` \- _Alerts → Actions → Discovery actions_ ;  
`configuration.autoregistration_actions` \- _Alerts → Actions → Autoregistration actions_ ;  
`configuration.internal_actions` \- _Alerts → Actions → Internal actions_.  
  
Possible values if `type` of the Role object is set to "Super admin":  
`reports.system_info` \- _Reports → System information_ ;  
`reports.audit` \- _Reports → Audit log_ ;  
`reports.action_log` \- _Reports → Action log_ ;  
`configuration.event_correlation` \- _Data collection → Event correlation_ ;  
`administration.media_types` \- _Alerts → Media types_ ;  
`administration.scripts` \- _Alerts → Scripts_ ;  
`administration.user_groups` \- _Users → User groups_ ;  
`administration.user_roles` \- _Users → User roles_ ;  
`administration.users` \- _Users → Users_ ;  
`administration.api_tokens` \- _Users → API tokens_ ;  
`administration.authentication` \- _Users → Authentication_ ;  
`administration.general` \- _Administration → General_ ;  
`administration.audit_log` \- _Administration → Audit log_ ;  
`administration.housekeeping` \- _Administration → Housekeeping_ ;  
`administration.proxy_groups` \- _Administration → Proxy groups_ ;  
`administration.proxies` \- _Administration → Proxies_ ;  
`administration.macros` \- _Administration → Macros_ ;  
`administration.queue` \- _Administration → Queue_.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
status | integer | Whether access to the UI element is enabled.  
  
Possible values:  
0 - Disabled;  
1 - _(default)_ Enabled.  
  
#### Service

serviceid | ID | ID of the Service.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
  
#### Service tag

tag | string | Tag name.  
  
If empty string is specified, the service tag will not be used for service matching.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
value | string | Tag value.  
  
If no value or empty string is specified, only the tag name will be used for service matching.  
  
#### Module

The module object has the following properties:

moduleid | ID | ID of the module.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
status | integer | Whether access to the module is enabled.  
  
Possible values:  
0 - Disabled;  
1 - _(default)_ Enabled.  
  
#### Action

The action object has the following properties:

name | string | Name of the action.  
  
Possible values if `type` of the Role object is set to "User", "Admin", or "Super admin:  
`edit_dashboards` \- Create and edit dashboards;  
`edit_maps` \- Create and edit maps;  
`add_problem_comments` \- Add problem comments;  
`change_severity` \- Change problem severity;  
`acknowledge_problems` \- Acknowledge problems;  
`suppress_problems` \- Suppress problems;  
`close_problems` \- Close problems;  
`execute_scripts` \- Execute scripts;  
`manage_api_tokens` \- Manage API tokens;  
`edit_own_media` \- Allow to create/edit own media.  
  
Possible values if `type` of the Role object is set to "Admin" or "Super admin":  
`edit_maintenance` \- Create and edit maintenances;  
`manage_scheduled_reports` \- Manage scheduled reports,  
`manage_sla` \- Manage SLA.  
  
Possible values if `type` of the Role object is set to "User" or "Admin":  
`invoke_execute_now` \- allows to execute item checks for users that have only read permissions on host.  
  
Possible values if `type` of the Role object is set to "Super admin":  
`edit_user_media` \- Allow to create/edit media for users.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
status | integer | Whether access to perform the action is enabled.  
  
Possible values:  
0 - Disabled;  
1 - _(default)_ Enabled.