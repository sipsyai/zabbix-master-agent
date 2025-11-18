---
title: Value mapping
source: https://www.zabbix.com/documentation/current/en/manual/config/items/mapping
downloaded: 2025-11-14 10:35:26
---

# 8 Value mapping

#### Overview

Value mapping allows configuring a more user-friendly representation of received values using mappings between numeric/string values and string representations.

For example, when an item's value is "0" or "1," value mappings can be used to represent these values in a more user-friendly manner:

  * 0 → Not Available
  * 1 → Available

Value mappings for data backup types could be configured as follows:

  * F → Full
  * D → Differential
  * I → Incremental

Value ranges for voltage could be configured as follows:

  * <=209 → Low
  * 210-230 → OK
  * >=231 → High

Value mapping is used in Zabbix frontend and notifications sent by media types.

Substitution of the received value with the configured representation is performed both in Zabbix frontend and server; however, the server handles substitution only in the following cases:  
  

  * when populating [host inventory](/documentation/current/en/manual/config/hosts/inventory#inventory-overview);
  * when expanding [supported macros](/documentation/current/en/manual/appendix/macros/supported_by_location) {ITEM.VALUE}, {ITEM.LASTVALUE}, {EVENT.OPDATA}, and {EVENT.CAUSE.OPDATA}.

Value mappings are set up on templates or hosts. Once configured, they are available for all items within the respective template or host. When [configuring items](/documentation/current/en/manual/config/items/item#configuration), specify the name of a previously configured value mapping in the _Value mapping_ parameter.

There is no value map inheritance - hosts and templates do not inherit value mappings from linked templates. Template items on a host will continue to use the value mappings configured on the template.

Value mappings can be used with items having _Numeric (unsigned)_ , _Numeric (float)_ , and _Character_ types of information.

Value mappings are exported/imported with the respective template or host. They can also be mass-updated using the [host](/documentation/current/en/manual/config/hosts/hostupdate) and [template](/documentation/current/en/manual/config/templates/mass) mass update forms.

#### Configuration

To configure a value mapping, follow these steps:

1\. Open the host or template configuration form.

2\. In the _Value mapping_ tab, click _Add_ to add a new value mapping, or click on the name of an existing mapping to edit it.

![](/documentation/current/assets/en/manual/config/items/value_mapping.png)

Parameters of a value mapping:

_Name_ | Unique name for the set of value mappings.  
---|---  
_Mappings_ | Individual rules for mapping numeric/string values to string representations.  
  
Mapping is applied in the order of the rules that can be reordered by dragging.  
| _Type_ | Mapping type:  
**equals** \- equal values will be mapped;  
**is greater than or equals** \- equal or greater values will be mapped;  
**is less than or equals** \- equal or smaller values will be mapped;  
**in range** \- values in range will be mapped; the range is expressed as <number1>-<number2> or <number>; multiple ranges are supported (for example, 1-10,101-110,201);  
**regexp** \- values corresponding to the [regular expression](/documentation/current/en/manual/regular_expressions) will be mapped (global regular expressions are not supported);  
**default** \- all outstanding values will be mapped, other than those with specific mappings.  
  
For mapping ranges, only numeric value types (_is greater than or equals_ , _is less than or equals_ , _in range_) are supported.  
_Value_ | Incoming value (may contain a range or regular expression, depending on the mapping type).  
_Mapped to_ | String representation (up to 64 characters) for the incoming value.  
  
All mandatory input fields are marked with a red asterisk.

When viewing the value mapping in the list, only the first three mappings are visible, with three dots indicating that more mappings exist.

![](/documentation/current/assets/en/manual/config/items/value_map_list.png)

#### Value mapping example

One of the predefined agent items _Zabbix agent ping_ uses a template-level value mapping "Zabbix agent ping status" to display its values.

![](/documentation/current/assets/en/manual/config/items/value_mapping2.png)

In the item [configuration form](/documentation/current/en/manual/config/items/item#configuration), you can find a reference to this value mapping in the _Value mapping_ field:

![](/documentation/current/assets/en/manual/config/items/item_value_mapping.png)

This mapping is used in the _Monitoring_ → _Latest data_ section to display "Up" (with the raw value in parentheses).

![](/documentation/current/assets/en/manual/config/items/value_display.png)

In the _Latest data_ section, displayed values are shortened to 20 symbols. If value mapping is used, this shortening is not applied to the mapped value but only to the raw value (displayed in parentheses).

Without a predefined value mapping, you would only see "1", which might be challenging to understand.

![](/documentation/current/assets/en/manual/config/items/value_display2.png)