---
title: Host groups
source: https://www.zabbix.com/documentation/current/en/manual/xml_export_import/hostgroups
downloaded: 2025-11-14 10:37:08
---

# 2 Host groups  
  
#### Overview

In the frontend, host groups can be [exported](/documentation/current/en/manual/xml_export_import) only with host export. When a host is exported, all groups it belongs to are exported with it automatically.

API allows exporting host groups independently of hosts.

#### Export format
    
    
       host_groups:
               - uuid: 6f6799aa69e844b4b3918f779f2abf08
                 name: 'Zabbix servers'

Copy

✔ Copied

#### Exported elements

uuid | string | Unique identifier for this host group.  
---|---|---  
name | string | Group name.