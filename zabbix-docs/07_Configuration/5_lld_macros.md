---
title: Low-level discovery macros
source: https://www.zabbix.com/documentation/current/en/manual/config/macros/lld_macros
downloaded: 2025-11-14 10:36:33
---

# 5 Low-level discovery macros  
  
#### Overview

There is a type of macro used within the [low-level discovery](/documentation/current/en/manual/discovery/low_level_discovery) (LLD) function:
    
    
    {#MACRO} 

Copy

✔ Copied

It is a macro that is used in an LLD rule and returns real values of the file system name, network interface, SNMP OID, etc.

These macros can be used for creating item, trigger, graph, and LLD rule _prototypes_. Then, when discovering real file systems, network interfaces etc., these macros are substituted with real values and are the basis for creating real entities.

These macros are also used in creating host and host group _prototypes_ in virtual machine [discovery](/documentation/current/en/manual/vm_monitoring#host-prototypes).

Some low-level discovery macros come "pre-packaged" with the LLD function in Zabbix - {#FSNAME}, {#FSTYPE}, {#IFNAME}, {#SNMPINDEX}, {#SNMPVALUE}. However, adhering to these names is not compulsory when creating a [custom](/documentation/current/en/manual/discovery/low_level_discovery/custom_rules) low-level discovery rule. Then you may use any other LLD macro name and refer to that name.

#### Supported data types

When defining custom discovery rules, property values returned in JSON objects for LLD macros must be one of the following primitive types:

  * string;
  * number;
  * boolean.

Arrays, objects, and null values are not supported. Any LLD macro referring to such a value will remain unexpanded and will appear literally (e.g. `'{#MY_MACRO}'`) during item preprocessing and creation.

#### Supported locations

LLD macros can be used:

  * in the low-level discovery rule filter
  * for item prototypes and discovery prototypes in 
    * name
    * key parameters
    * unit
    * update interval[1](lld_macros#footnotes)
    * timeout[1](lld_macros#footnotes)
    * history storage period[1](lld_macros#footnotes)
    * trend storage period[1](lld_macros#footnotes)
    * item value preprocessing steps
    * SNMP OID
    * IPMI sensor field
    * calculated/aggregate item expression, in: 
      * expression constants and function parameters
      * item key parameters
    * aggregate item filter conditions (host group name and tag name)
    * SSH script and Telnet script
    * database monitoring SQL query
    * JMX item endpoint field
    * description
    * HTTP agent URL field
    * HTTP agent HTTP query fields field
    * HTTP agent request body field
    * HTTP agent required status codes field
    * HTTP agent headers field key and value
    * HTTP agent HTTP authentication username field
    * HTTP agent HTTP authentication password field
    * HTTP agent HTTP proxy field
    * HTTP agent HTTP SSL certificate file field
    * HTTP agent HTTP SSL key file field
    * HTTP agent HTTP SSL key password field
    * tags
  * for trigger prototypes in 
    * name
    * operational data
    * expression (only in constants and function parameters)
    * URL
    * description
    * tags
  * for graph prototypes in 
    * name
  * for host prototypes in 
    * name
    * visible name
    * custom interface fields: IP, DNS, port, SNMP v1/v2 community, SNMP v3 context name, SNMP v3 security name, SNMP v3 authentication passphrase, SNMP v3 privacy passphrase
    * host group prototype name
    * host tag value
    * host macro value
    * (see the [full list](/documentation/current/en/manual/vm_monitoring/discovery_fields))

In all those places, except the low-level discovery rule filter, LLD macros can be used inside static user [macro context](/documentation/current/en/manual/config/macros/user_macros_context).

#### Using macro functions

Macro functions are supported with low-level discovery macros (except in low-level discovery rule [filter](/documentation/current/en/manual/discovery/low_level_discovery#filter)), allowing to extract a certain part of the macro value using a regular expression.

For example, you may want to extract the customer name and interface number from the following LLD macro for the purposes of event tagging:
    
    
    {#IFALIAS}=customername_1

Copy

✔ Copied

To do so, the `regsub` macro function can be used with the macro in the event tag value field of a trigger prototype:

![](/documentation/current/assets/en/manual/config/macros/lld_macro_function.png)

Note that commas are not allowed in unquoted item [key parameters](/documentation/current/en/manual/config/items/item/key#key-parameters), so the parameter containing a macro function has to be quoted. The backslash (`\`) character should be used to escape double quotes inside the parameter. Example:
    
    
    net.if.in["{{#IFALIAS}.regsub(\"(.*)_([0-9]+)\", \1)}",bytes]

Copy

✔ Copied

For more information on macro function syntax, see: [Macro functions](/documentation/current/en/manual/config/macros/macro_functions)

Macro functions are supported in low-level discovery macros since Zabbix 4.0.

##### Footnotes

**1** In the fields marked with [1](lld_macros#footnotes) a single macro has to fill the whole field. Multiple macros in a field or macros mixed with text are not supported.