---
title: Item prototypes
source: https://www.zabbix.com/documentation/current/en/manual/discovery/low_level_discovery/item_prototypes
downloaded: 2025-11-14 10:37:19
---

# 1 Item prototypes

Once a rule is created, go to the items for that rule and press "Create item prototype" to create an item prototype.

Note how the {#FSNAME} macro is used where a file system name is required. The use of a low-level discovery macro is mandatory in the item key to make sure that the discovery is processed correctly. When the discovery rule is processed, this macro will be substituted with the discovered file system.

![](/documentation/current/assets/en/manual/discovery/low_level_discovery/item_prototype_fs.png)

Low-level discovery [macros](/documentation/current/en/manual/config/macros/lld_macros) and user [macros](/documentation/current/en/manual/appendix/macros/supported_by_location_user) are supported in item prototype configuration and item value preprocessing [parameters](/documentation/current/en/manual/config/items/item#item-value-preprocessing). Note that when used in update intervals, a single macro has to fill the whole field. Multiple macros in one field or macros mixed with text are not supported.

Context-specific escaping of low-level discovery macros is performed for safe use in regular expression and XPath preprocessing parameters.

Attributes that are specific for item prototypes:

_Create enabled_ | If checked the item will be added in an enabled state.  
If unchecked, the item will be added to a discovered entity, but in a disabled state.  
---|---  
_Discover_ | If checked (default) the item will be added to a discovered entity.  
If unchecked, the item will not be added to a discovered entity, unless this setting is [overridden](/documentation/current/en/manual/discovery/low_level_discovery#override) in the discovery rule.  
  
We can create several item prototypes for each file system metric we are interested in:

![](/documentation/current/assets/en/manual/discovery/low_level_discovery/item_prototypes_fs.png)

Click on the three-dot icon to open the menu for the specific item prototype with these options:

  * _Create trigger prototype_ \- create a trigger prototype based on this item prototype
  * _Trigger prototypes_ \- click to see a list with links to already-configured trigger prototypes of this item prototype
  * _Create dependent item_ \- create a dependent item for this item prototype

_[Mass update](/documentation/current/en/manual/config/items/itemupdate#using-mass-update)_ option is available if you want to update properties of several item prototypes at once.