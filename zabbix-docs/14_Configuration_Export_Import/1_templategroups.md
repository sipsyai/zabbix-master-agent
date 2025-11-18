---
title: Template groups
source: https://www.zabbix.com/documentation/current/en/manual/xml_export_import/templategroups
downloaded: 2025-11-14 10:37:07
---

# 1 Template groups

#### Overview

In the frontend, template groups can be [exported](/documentation/current/en/manual/xml_export_import) only with template export. When a template is exported, all groups it belongs to are exported with it automatically.

API allows exporting template groups independently of templates.

#### Export format
    
    
      template_groups:
               - uuid: 36bff6c29af64692839d077febfc7079
                 name: 'Network devices'

Copy

✔ Copied

#### Exported elements

uuid | string | Unique identifier for this template group.  
---|---|---  
name | string | Group name.