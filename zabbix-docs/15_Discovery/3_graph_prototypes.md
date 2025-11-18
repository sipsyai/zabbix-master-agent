---
title: Graph prototypes
source: https://www.zabbix.com/documentation/current/en/manual/discovery/low_level_discovery/graph_prototypes
downloaded: 2025-11-14 10:37:21
---

# 3 Graph prototypes

We can create graph prototypes, too:

![](/documentation/current/assets/en/manual/discovery/low_level_discovery/graph_prototype_fs.png)

Attributes that are specific for graph prototypes:

_Discover_ | If checked (default) the graph will be added to a discovered entity.  
If unchecked, the graph will not be added to a discovered entity, unless this setting is [overridden](/documentation/current/en/manual/discovery/low_level_discovery#override) in the discovery rule.  
---|---  
  
![](/documentation/current/assets/en/manual/discovery/low_level_discovery/graph_prototypes_fs.png)

Finally, we have created a discovery rule that looks as shown below. It has five item prototypes, two trigger prototypes, and one graph prototype.

![](/documentation/current/assets/en/manual/discovery/low_level_discovery/lld_rules_fs.png)