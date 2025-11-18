---
title: User macros
source: https://www.zabbix.com/documentation/current/en/manual/config/macros/user_macros
downloaded: 2025-11-14 10:36:31
---

# 2 User macros

#### Overview

User macros are supported in Zabbix for greater flexibility, in addition to the macros [supported](/documentation/current/en/manual/appendix/macros/supported_by_location) out-of-the-box.

User macros can be defined on global, template and host level. These macros have a special syntax:
    
    
    {$MACRO}

Copy

✔ Copied

Zabbix resolves macros according to the following precedence:

  1. host level macros (checked first)
  2. macros defined for first level templates of the host (i.e., templates linked directly to the host), sorted by template ID
  3. macros defined for second level templates of the host, sorted by template ID
  4. macros defined for third level templates of the host, sorted by template ID, etc.
  5. global macros (checked last)

In other words, if a macro does not exist for a host, Zabbix will try to find it in the host templates of increasing depth. If still not found, a global macro will be used, if exists.

If a macro with the **same name** exists on multiple linked templates of the same level, the macro from the template with the lowest ID will be used. Thus having macros with the same name in multiple templates is a configuration risk.

If Zabbix is unable to find a macro, the macro will not be resolved.

Macros (including user macros) are left unresolved in the Configuration section (for example, in the trigger list) by design to make complex configuration more transparent.

User macros can be used in:

  * item name
  * item key parameter
  * item update intervals and flexible intervals
  * trigger name and description
  * trigger expression parameters and constants (see examples)
  * many other locations - see the [full list](/documentation/current/en/manual/appendix/macros/supported_by_location_user)

##### Common use cases of global and host macros

  * use a global macro in several locations; then change the macro value and apply configuration changes to all locations with one click
  * take advantage of templates with host-specific attributes: passwords, port numbers, file names, regular expressions, etc.

It is recommended to use host macros instead of global macros because adding, updating or deleting global macros forces incremental configuration update for all hosts. For more information, see [Passive and active agent checks](/documentation/current/en/manual/appendix/items/activepassive#active-checks).

#### Configuration

To define user macros, go to the corresponding location in the frontend:

  * for global macros, visit _Administration → Macros_
  * for host and template level macros, open host or template properties and look for the _Macros_ tab

A user macro has the following attributes:

![](/documentation/current/assets/en/manual/config/macros/user_macros.png)

_Macro_ | Macro name. The name must be wrapped in curly brackets and start with a dollar sign.  
Example: {$FRONTEND_URL}. The following characters are allowed in the macro names: **A-Z** (uppercase only) , **0-9** , **_** , **.**  
---|---  
_Value_ | Macro value. Three value types are supported:  
**Text** (default) - plain-text value  
**[Secret text](/documentation/current/en/manual/config/macros/secret_macros#secret-text)** \- the value is masked with asterisks  
**[Vault secret](/documentation/current/en/manual/config/macros/secret_macros#vault-secret)** \- the value contains a path/query to a [vault secret](/documentation/current/en/manual/config/secrets).   
  
To change the value type click on the button at the end of the value input field.  
  
Maximum length of a user macro value is 2048 characters.  
_Description_ | Text field used to provide more information about this macro.  
  
When configuring user macros, **note** the following context-specific behaviors:

  * if user macros are used in template items or triggers, consider adding those macros to the template as well (even if they are defined globally); that way, _Text_ type macros will work as expected after exporting the template to XML and importing into another system (secret macro values are not [exported](/documentation/current/en/manual/xml_export_import))
  * if user macros are used in trigger expressions, those macros will resolve only if referencing a parameter or constant; they will NOT resolve if referencing a host, item key, function, operator, or another trigger expression (secret macros cannot be used in trigger expressions)
  * if user macros are used on a host that has a low-level discovery rule with host prototypes, [discovered hosts](/documentation/current/en/manual/discovery/low_level_discovery/host_prototypes#discovered-hosts) will inherit all user macros defined on that host

#### Examples

##### Example 1

Use of host-level macro in the "Status of SSH daemon" item key:

`net.tcp.service[ssh,,{$SSH_PORT}]`

This item can be assigned to multiple hosts, providing that the value of **{$SSH_PORT}** is defined on those hosts.

##### Example 2

Use of host-level macro in the "CPU load is too high" trigger:

`last(/ca_001/system.cpu.load[,avg1])>{$MAX_CPULOAD}`

Such a trigger would be created on the template, not edited in individual hosts.

If you want to use the amount of values as the function parameter (for example, **max(/host/key,#3)**), include hash mark in the macro definition like this: SOME_PERIOD => #3

##### Example 3

Use of two macros in the "CPU load is too high" trigger:

`min(/ca_001/system.cpu.load[,avg1],{$CPULOAD_PERIOD})>{$MAX_CPULOAD}`

Note that a macro can be used as a parameter of trigger function, in this example function **min()**.

##### Example 4

Synchronize the agent unavailability condition with the item update interval:

  * define {$INTERVAL} macro and use it in the item update interval;
  * use {$INTERVAL} as parameter of the agent unavailability trigger:

`nodata(/ca_001/agent.ping,{$INTERVAL})=1`

##### Example 5

Centralize configuration of working hours:

  * create a global {$WORKING_HOURS} macro equal to `1-5,09:00-18:00`;
  * use it in the _Working time_ field in _Administration_ → _General_ → _GUI_ ;
  * use it in the _When active_ field in _Users_ → _Users_ , _Media_ tab of a user;
  * use it to set up more frequent item polling during working hours:

![](/documentation/current/assets/en/manual/config/macros/usermacro_example5.png)

  * use it in the _Time period_ action condition;
  * adjust the working time in _Administration_ → _Macros_ , if needed.

##### Example 6

Use host prototype macro to configure items for discovered hosts:

  * on a host prototype define user macro {$SNMPVALUE} with {#SNMPVALUE} [low-level discovery](/documentation/current/en/manual/config/macros/lld_macros) macro as a value:

![](/documentation/current/assets/en/manual/config/macros/usermacro_example6.png)

  * assign _Generic SNMPv2_ template to the host prototype;
  * use {$SNMPVALUE} in the _SNMP OID_ field of _Generic SNMPv2_ template items.

#### User macro context

See [user macros with context](/documentation/current/en/manual/config/macros/user_macros_context).