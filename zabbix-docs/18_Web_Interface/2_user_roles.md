---
title: User roles
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles
downloaded: 2025-11-14 10:39:17
---

# 2 User roles

#### Overview

In the _Users > User roles_ section you may create user roles.

User roles allow to create fine-grained permissions based on the initially selected user type (_User_ , _Admin_ , _Super admin_).

Upon selecting a user type, all available permissions for this user type are granted (checked by default).

Permissions can only be revoked from the subset that is available for the user type; they cannot be extended beyond what is available for the user type.

Checkboxes for unavailable permissions are grayed out; users will not be able to access the element even by entering a direct URL to this element into the browser.

Restricting access to some UI elements only prevents opening that page—it does not remove the ability to access underlying data on other parts of the interface.

User roles can be assigned to system users. Each user may have only one role assigned.

#### Default user roles

By default, Zabbix is configured with four user roles, which have a pre-defined set of permissions:

  * Guest role
  * User role
  * Admin role
  * Super admin role

![](/documentation/current/assets/en/manual/web_interface/user_roles.png)

These are based on the main user types in Zabbix. The list of all users assigned the respective role is displayed. The users included in disabled groups are stated in red. The _Guest role_ is a user-type role with the only permissions to view some frontend sections.

The default _Super admin role_ cannot be modified or deleted, because at least one Super admin user with unlimited privileges must exist in Zabbix. Users of type _Super admin_ can modify settings of their own role, but not the user type.

#### Configuration

To create a new role, click on the _Create user role_ button at the upper-right corner. To update an existing role, click on the role name to open the configuration form.

![](/documentation/current/assets/en/manual/web_interface/user_role.png)

Available permissions are displayed. To revoke a certain permission, unmark its checkbox.

Available permissions along with the defaults for each pre-configured user role in Zabbix are described below.

#### Default permissions

**Access to UI elements**

The default access to menu sections depends on the user type. See the Permissions page for [details](/documentation/current/en/manual/config/users_and_usergroups/permissions#user-types).

**Access to other options**

**Parameter** | **Description** | **Default user roles**  
---|---|---  
| _Super admin role_ | _Admin role_ | _User role_ | _Guest role_  
_Default access to new UI elements_ | This option specifies how new menu sections will be accessible after a Zabbix upgrade. Existing menu sections of modules remain unaffected. | Yes | Yes | Yes | Yes  
**Access to services**  
| Read-write access to services | Select read-write access to services:  
**None** \- no access at all  
**All** \- access to all services is read-write  
**Service list** \- select services for read-write access  
  
The read-write access, if granted, takes precedence over the read-only access settings and is dynamically inherited by the child services. | All | All | None | None  
Read-write access to services with tag | Specify tag name and, optionally, value to additionally grant read-write access to services matching the tag.  
This option is available if 'Service list' is selected in the _Read-write access to services_ parameter.  
The read-write access, if granted, takes precedence over the read-only access settings and is dynamically inherited by the child services.  
Read-only access to services | Select read-only access to services:  
**None** \- no access at all  
**All** \- access to all services is read-only  
**Service list** \- select services for read-only access  
  
The read-only access does not take precedence over the read-write access and is dynamically inherited by the child services. | All | All  
Read-only access to services with tag | Specify tag name and, optionally, value to additionally grant read-only access to services matching the tag.  
This option is available if 'Service list' is selected in the _Read-only access to services_ parameter.  
The read-only access does not take precedence over the read-write access and is dynamically inherited by the child services.  
**Access to modules**  
| <Module name> | Allow/deny access to a specific module. Only enabled modules are shown in this section. It is not possible to grant or restrict access to a module that is currently disabled. | Yes | Yes | Yes | Yes  
_Default access to new modules_ | This option specifies how new modules and widgets will be accessible after a Zabbix upgrade. It also applies to modules and widgets added in the _Administration > General > Modules section_.  
**Access to API**  
| _Enabled_ | Enable/disable access to API. | Yes | Yes | Yes | No  
_API methods_ | Select either _Allow list_ to allow, or _Deny list_ to deny the API methods specified in the search field. Note that it is not possible to allow some API methods and deny others.  
  
In the search field, start typing the method name, then select the method from the auto-complete list.  
You can also press the Select button and select methods from the full list available for this user type. Note that if certain action from the Access to actions block is unchecked, users will not be able to use API methods related to this action.  
  
Wildcards are supported. Examples: `dashboard.*` (all methods of 'dashboard.' API service) `*` (any method), `*.export` (methods with '.export' name from all API services).  
  
If no methods have been specified the _Allow/Deny list_ rule will be ignored.  
**Access to actions**  
| Create and edit dashboards | Clearing this checkbox will also revoke the rights to use `.create`, `.update` and `.delete` API methods for the corresponding elements. | Yes | Yes | Yes | No  
Create and edit maps |   
Create and edit maintenance | No  
Add problem comments | Clearing this checkbox will also revoke the rights to perform corresponding action via `event.acknowledge` API method. | Yes  
Change severity |   
Acknowledge problems  
Suppress problems  
Close problems  
Execute scripts | Clearing this checkbox will also revoke the rights to use the `script.execute` API method.  
Manage API tokens | Clearing this checkbox will also revoke the rights to use all `token.` API methods.  
Manage scheduled reports | Clearing this checkbox will also revoke the rights to use all `report.` API methods. | No  
Manage SLA | Enable/disable the rights to manage [SLA](/documentation/current/en/manual/web_interface/frontend_sections/services/sla).  
Invoke "Execute now" on read-only hosts | Allow to use the "Execute now" option in latest data for items of read-only hosts. | Yes  
Change problem ranking | Allow to change the problem ranking from cause to symptom, and vice versa.  
Create and edit own media | Allow to create/edit their own media.  
Create and edit user media | Allow to create/edit media for users. This option is only available for Super admin users. | No | No  
Default access to new actions | This option specifies how new actions will be accessible after a Zabbix upgrade. | Yes | Yes  
  
See also:

  * [Configuring a user](/documentation/current/en/manual/config/users_and_usergroups/user)