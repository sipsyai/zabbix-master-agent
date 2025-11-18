---
title: Template object
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/template/object
downloaded: 2025-11-14 10:44:42
---

# Template object

The following objects are directly related to the `template` API.

### Template

The template object has the following properties.

templateid | ID | ID of the template.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
\- _required_ for update operations  
---|---|---  
description | text | Description of the template.  
host | string | Technical name of the template.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
name | string | Visible name of the template.  
  
Default: `host` property value.  
readme | text | Template-specific configuration instructions to display in the [Host Wizard](/documentation/current/en/manual/config/hosts/host_wizard#configure-host). Supports Markdown formatting.  
uuid | string | Universal unique identifier, used for linking imported templates to already existing ones. Auto-generated, if not given.  
vendor_name | string | Template vendor name.  
  
For create operations, both `vendor_name` and `vendor_version` should be either set or left empty. For update operations, `vendor_version` can be left empty if it has a value in the database.  
vendor_version | string | Template vendor version.  
  
For create operations, both `vendor_name` and `vendor_version` should be either set or left empty. For update operations, `vendor_name` can be left empty if it has a value in the database.  
wizard_ready | integer | Whether the template is available for selection in the [Host Wizard](/documentation/current/en/manual/config/hosts/host_wizard).  
  
Possible values:  
0 - _(default)_ Not available.  
1 - Available.  
  
### Template tag

The template tag object has the following properties.

tag | string | Template tag name.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
value | string | Template tag value.