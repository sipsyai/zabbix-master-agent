---
title: Trigger prototypes
source: https://www.zabbix.com/documentation/current/en/manual/discovery/low_level_discovery/trigger_prototypes
downloaded: 2025-11-14 10:37:20
---

# 2 Trigger prototypes

We create trigger prototypes in a similar way as item prototypes:

![](/documentation/current/assets/en/manual/discovery/low_level_discovery/trigger_prototype_fs.png)

Attributes that are specific for trigger prototypes:

_Create enabled_ | If checked the trigger will be added in an enabled state.  
If unchecked, the trigger will be added to a discovered entity, but in a disabled state.  
---|---  
_Discover_ | If checked (default) the trigger will be added to a discovered entity.  
If unchecked, the trigger will not be added to a discovered entity, unless this setting is [overridden](/documentation/current/en/manual/discovery/low_level_discovery#override) in the discovery rule.  
  
When real triggers are created from the prototypes, there may be a need to be flexible as to what constant ('20' in our example) is used for comparison in the expression. See how [user macros with context](/documentation/current/en/manual/config/macros/user_macros_context#use-cases) can be useful to accomplish such flexibility.

You can define [dependencies](/documentation/current/en/manual/config/triggers/dependencies) between trigger prototypes. To do that, go to the _Dependencies_ tab. A trigger prototype may depend on another trigger prototype from the same low-level discovery (LLD) rule or on a regular trigger. A trigger prototype may not depend on a trigger prototype from a different LLD rule or on a trigger created from trigger prototype. Host trigger prototype cannot depend on a trigger from a template.

![](/documentation/current/assets/en/manual/discovery/low_level_discovery/trigger_prototypes_fs.png)