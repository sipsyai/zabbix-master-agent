---
title: User macro object
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/usermacro/object
downloaded: 2025-11-14 10:45:54
---

# User macro object

The following objects are directly related to the `usermacro` API.

### Global macro

The global macro object has the following properties.

globalmacroid | ID | ID of the global macro.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
\- _required_ for update operations  
---|---|---  
description | string | Description of the macro.  
macro | string | Macro string.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
type | integer | Type of macro.  
  
Possible values:  
0 - _(default)_ Text macro;  
1 - Secret macro;  
2 - Vault secret.  
value | string | Value of the macro.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _write-only_ if `type` is set to "Secret macro"  
\- _required_ for create operations  
  
### Host macro

The host macro object defines a macro available on a host, host prototype or template. It has the following properties.

hostmacroid | ID | ID of the macro.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
\- _required_ for update operations  
---|---|---  
automatic | integer | Defines whether the macro is controlled by discovery rule.  
  
Possible values:  
0 - _(default)_ Macro is managed by user;  
1 - Macro is managed by discovery rule.  
  
User is not allowed to create automatic macro.  
To update automatic macro, it must be [converted to manual](/documentation/current/en/manual/api/reference/usermacro/update#change-macro-value-that-was-created-by-discovery-rule).  
config | object/array | Macro configuration responsible for how the macro is displayed in the [Host Wizard](/documentation/current/en/manual/config/hosts/host_wizard#configure-host).  
description | string | Description of the macro.  
hostid | ID | ID of the host, host prototype, or template that the macro belongs to.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _constant_  
\- _required_ for create operations  
macro | string | Macro string.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
type | integer | Type of macro.  
  
Possible values:  
0 - _(default)_ Text macro;  
1 - Secret macro;  
2 - Vault secret.  
value | string | Value of the macro.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _write-only_ if `type` is set to "Secret macro"  
\- _required_ for create operations  
  
#### Macro configuration

The macro configuration object defines how a macro is displayed in the [Host Wizard](/documentation/current/en/manual/config/hosts/host_wizard#configure-host).

type | integer | Type of macro input field.  
  
Possible values:  
0 - Macro is not used in Host Wizard;  
1 - Textbox;  
2 - List;  
3 - Checkbox.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
label | string | Label for macro input field.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `type` is set to "Textbox", "List", or "Checkbox"  
description | text | Help text displayed alongside macro input field. Supports Markdown formatting.  
priority | integer | Macro input field position in the macro list.  
  
If `priority` is not set, the macro is added at the end of the ungrouped macro list.  
required | integer | Marks the macro as mandatory.  
  
Possible values:  
0 - Not mandatory;  
1 - Mandatory.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `type` is set to "Textbox" or "List"  
regex | string | Regular expression to validate user input in a textbox field.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `type` is set to "Textbox"  
section_name | string | Label of the collapsible section where the macro is grouped.  
  
If `section_name` is not set, the macro is ungrouped. Ungrouped macros are displayed first; grouped macros are displayed below, ordered by their `priority` within each collapsible section.  
options | text | JSON string defining list items or checkbox values.  
  
For lists: an array of objects with `value` and `text` properties.  
Example: `[{"value": "http", "text": "HTTP"}, {"value": "https", "text": "HTTPS"}]`  
  
For checkboxes: an object with `checked` and `unchecked` properties.  
Example: `{"checked": true, "unchecked": false}`  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `type` is set to "List" or "Checkbox"