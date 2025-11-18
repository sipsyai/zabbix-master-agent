---
title: Permissions
source: https://www.zabbix.com/documentation/current/en/manual/config/users_and_usergroups/permissions
downloaded: 2025-11-14 10:36:37
---

# 2 Permissions

#### Overview

Permissions in Zabbix depend on the user type, customized user roles and access to hosts, which is specified based on the user group.

#### User types

Permissions in Zabbix depend, primarily, on the user type:

  * _User_ \- has limited access rights to menu sections (see below) and no access to any resources by default. Any permissions to host or template groups must be explicitly assigned;
  * _Admin_ \- has incomplete access rights to menu sections (see below). The user has no access to any host groups by default. Any permissions to host or template groups must be explicitly given;
  * _Super admin_ \- has access to all menu sections. The user has a read-write access to all host and template groups. Permissions cannot be revoked by denying access to specific groups.

**Menu access**

Restricted access to some UI elements only prevents opening that page—it does not remove the ability to access underlying data on other parts of the interface.

The following table illustrates access to Zabbix menu sections per user type:

**Dashboards** | + | + | +  
---|---|---|---  
**Monitoring** | + | + | +  
| _Problems_ | + | + | +  
_Hosts_ | + | + | +  
_Latest data_ | + | + | +  
_Maps_ | + | + | +  
_Discovery_ |  | + | +  
**Services** | + | + | +  
| _Services_ | + | + | +  
_SLA_ |  | + | +  
_SLA report_ | + | + | +  
**Inventory** | + | + | +  
| _Overview_ | + | + | +  
_Hosts_ | + | + | +  
**Reports** | + | + | +  
| _System information_ |  |  | +  
_Scheduled reports_ |  | + | +  
_Availability report_ | + | + | +  
_Top 100 triggers_ | + | + | +  
_Audit log_ |  |  | +  
_Action log_ |  |  | +  
_Notifications_ |  | + | +  
**Data collection** |  | + | +  
| _Template groups_ |  | + | +  
_Host groups_ |  | + | +  
_Templates_ |  | + | +  
_Hosts_ |  | + | +  
_Maintenance_ |  | + | +  
_Event correlation_ |  |  | +  
_Discovery_ |  | + | +  
**Alerts** |  | + | +  
| _Trigger actions_ |  | + | +  
| _Service actions_ |  | + | +  
| _Discovery actions_ |  | + | +  
| _Autoregistration actions_ |  | + | +  
| _Internal actions_ |  | + | +  
_Media types_ |  |  | +  
_Scripts_ |  |  | +  
**Users** |  |  | +  
| _User groups_ |  |  | +  
_User roles_ |  |  | +  
_Users_ |  |  | +  
_API tokens_ |  |  | +  
_Authentication_ |  |  | +  
**Administration** |  |  | +  
| _General_ |  |  | +  
_Audit log_ |  |  | +  
_Housekeeping_ |  |  | +  
_Proxy groups_ |  |  | +  
_Proxies_ |  |  | +  
_Macros_ |  |  | +  
_Queue_ |  |  | +  
  
#### User roles

User roles allow making custom adjustments to the permissions defined by the user type. While no permissions can be added (that would exceed those of the user type), some permissions can be revoked.

Furthermore, a user role determines access not only to menu sections, but also to services, modules, API methods and various actions in the frontend.

[User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) are configured in the _Users → User roles_ section by Super admin users.

User roles are assigned to users in the user configuration form, _Permissions_ tab, by Super admin users.

![](/documentation/current/assets/en/manual/config/user_permissions.png)

#### Access to hosts

Access to any host and template data in Zabbix is granted to [user groups](/documentation/current/en/manual/config/users_and_usergroups/usergroup) on the host/template group level only.

That means that an individual user cannot be directly granted access to a host (or host group). It can only be granted access to a host by being part of a user group that is granted access to the host group that contains the host.

Similarly, a user can only be granted access to a template by being part of a user group that is granted access to the template group that contains the template.