---
title: Discovery of JMX objects
source: https://www.zabbix.com/documentation/current/en/manual/discovery/low_level_discovery/examples/jmx
downloaded: 2025-11-14 10:37:31
---

# 6 Discovery of JMX objects

#### Overview

It is possible to [discover](/documentation/current/en/manual/discovery/low_level_discovery) all JMX MBeans or MBean attributes or to specify a pattern for the discovery of these objects.

It is mandatory to understand the difference between an MBean and MBean attributes for discovery rule configuration. An MBean is an object which can represent a device, an application, or any resource that needs to be managed.

For example, there is an MBean which represents a web server. Its attributes are connection count, thread count, request timeout, http file cache, memory usage, etc. Expressing this thought in human comprehensive language we can define a coffee machine as an MBean which has the following attributes to be monitored: water amount per cup, average consumption of water for a certain period of time, number of coffee beans required per cup, coffee beans and water refill time, etc.

#### Item key

In [discovery rule](/documentation/current/en/manual/discovery/low_level_discovery#discovery-rule) configuration, select **JMX agent** in the _Type_ field.

Two item keys are supported for JMX object discovery - jmx.discovery[] and jmx.get[]:

| Return value | Parameters | Comment  
---|---|---|---  
**jmx.discovery**[<discovery mode>,<object name>,<unique short description>]  
| This item returns a JSON array with LLD macros describing MBean objects or their attributes. | **discovery mode** \- one of the following: _attributes_ (retrieve JMX MBean attributes, default) or _beans_ (retrieve JMX MBeans)  
**object name** \- object name pattern (see [documentation](https://docs.oracle.com/javase/7/docs/api/javax/management/ObjectName.html)) identifying the MBean names to be retrieved (empty by default, retrieving all registered beans)  
**unique short description** \- a unique description that allows multiple JMX items with the same discovery mode and object name on the host (optional) | Examples:  
→ jmx.discovery - retrieve all JMX MBean attributes  
→ jmx.discovery[beans] - retrieve all JMX MBeans  
→ jmx.discovery[attributes,"*:type=GarbageCollector,name=*"] - retrieve all garbage collector attributes  
→ jmx.discovery[beans,"*:type=GarbageCollector,name=*"] - retrieve all garbage collectors  
  
There are some limitations to what MBean properties this item can return based on limited characters that are supported in macro name generation (supported characters can be described by the following regular expression: `A-Z0-9_\.`). So, for example, to discover MBean properties with a hyphenated word or non-ASCII characters, you need to use `jmx.get[]`.  
**jmx.get**[<discovery mode>,<object name>,<unique short description>]  
| This item returns a JSON array with MBean objects or their attributes.  
  
Compared to `jmx.discovery[]` it does not define LLD macros. | **discovery mode** \- one of the following: _attributes_ (retrieve JMX MBean attributes, default) or _beans_ (retrieve JMX MBeans)  
**object name** \- object name pattern (see [documentation](https://docs.oracle.com/javase/7/docs/api/javax/management/ObjectName.html)) identifying the MBean names to be retrieved (empty by default, retrieving all registered beans)  
**unique short description** \- a unique description that allows multiple JMX items with the same discovery mode and object name on the host (optional) | When using this item, it is needed to define custom low-level discovery macros, pointing to values extracted from the returned JSON using JSONPath.  
  
If no parameters are passed, all MBean attributes from JMX are requested. Not specifying parameters for JMX discovery or trying to receive all attributes for a wide range like `*:type=*,name=*` may lead to potential performance problems.

#### Using jmx.discovery

This item returns a JSON object with low-level discovery macros describing MBean objects or attributes. For example, in the discovery of MBean attributes (reformatted for clarity):
    
    
    [
               {
                   "{#JMXVALUE}":"0",
                   "{#JMXTYPE}":"java.lang.Long",
                   "{#JMXOBJ}":"java.lang:type=GarbageCollector,name=PS Scavenge",
                   "{#JMXDESC}":"java.lang:type=GarbageCollector,name=PS Scavenge,CollectionCount",
                   "{#JMXATTR}":"CollectionCount"
               },
               {
                   "{#JMXVALUE}":"0",
                   "{#JMXTYPE}":"java.lang.Long",
                   "{#JMXOBJ}":"java.lang:type=GarbageCollector,name=PS Scavenge",
                   "{#JMXDESC}":"java.lang:type=GarbageCollector,name=PS Scavenge,CollectionTime",
                   "{#JMXATTR}":"CollectionTime"
               },
               {
                   "{#JMXVALUE}":"true",
                   "{#JMXTYPE}":"java.lang.Boolean",
                   "{#JMXOBJ}":"java.lang:type=GarbageCollector,name=PS Scavenge",
                   "{#JMXDESC}":"java.lang:type=GarbageCollector,name=PS Scavenge,Valid",
                   "{#JMXATTR}":"Valid"
               },
               {
                   "{#JMXVALUE}":"PS Scavenge",
                   "{#JMXTYPE}":"java.lang.String",
                   "{#JMXOBJ}":"java.lang:type=GarbageCollector,name=PS Scavenge",
                   "{#JMXDESC}":"java.lang:type=GarbageCollector,name=PS Scavenge,Name",
                   "{#JMXATTR}":"Name"
               },
               {
                   "{#JMXVALUE}":"java.lang:type=GarbageCollector,name=PS Scavenge",
                   "{#JMXTYPE}":"javax.management.ObjectName",
                   "{#JMXOBJ}":"java.lang:type=GarbageCollector,name=PS Scavenge",
                   "{#JMXDESC}":"java.lang:type=GarbageCollector,name=PS Scavenge,ObjectName",
                   "{#JMXATTR}":"ObjectName"
               }
           ]

Copy

✔ Copied

In the discovery of MBeans (reformatted for clarity):
    
    
    [
               {
                   "{#JMXDOMAIN}":"java.lang",
                   "{#JMXTYPE}":"GarbageCollector",
                   "{#JMXOBJ}":"java.lang:type=GarbageCollector,name=PS Scavenge",
                   "{#JMXNAME}":"PS Scavenge"
               }
           ]

Copy

✔ Copied

##### Supported macros

The following macros are supported for use in the discovery rule [filter](/documentation/current/en/manual/discovery/low_level_discovery#discovery-rule-filter) and prototypes of items, triggers and graphs:

Discovery of MBean attributes  
---  
{#JMXVALUE} | Attribute value.  
{#JMXTYPE} | Attribute type.  
{#JMXOBJ} | Object name.  
{#JMXDESC} | Object name including attribute name.  
{#JMXATTR} | Attribute name.  
Discovery of MBeans  
{#JMXDOMAIN} | MBean domain. (_Zabbix reserved name_)  
{#JMXOBJ} | Object name. (_Zabbix reserved name_)  
{#JMX<key property>} | MBean properties (like {#JMXTYPE}, {#JMXNAME}) (see Limitations below).  
  
##### Limitations

There are some limitations associated with the algorithm of creating LLD macro names from MBean property names:

  * attribute names are changed to uppercase
  * attribute names are ignored (no LLD macros are generated) if they consist of unsupported characters for LLD macro names. Supported characters can be described by the following regular expression: `A-Z0-9_\.`
  * if an attribute is called "obj" or "domain" they will be ignored because of the overlap with the values of the reserved Zabbix properties {#JMXOBJ} and {#JMXDOMAIN}

Please consider this jmx.discovery (with "beans" mode) example. MBean has the following properties defined (some of which will be ignored; see below):
    
    
    name=test
           тип=Type
           attributes []=1,2,3
           Name=NameOfTheTest
           domAin=some

Copy

✔ Copied

As a result of JMX discovery, the following LLD macros will be generated:

  * {#JMXDOMAIN} - Zabbix internal, describing the domain of MBean
  * {#JMXOBJ} - Zabbix internal, describing MBean object
  * {#JMXNAME} - created from "name" property

Ignored properties are:

  * тип : its name contains unsupported characters (non-ASCII)
  * attributes[] : its name contains unsupported characters (square brackets are not supported)
  * Name : it's already defined (name=test)
  * domAin : it's a Zabbix reserved name

##### Examples

Let's review two more practical examples of an LLD rule creation with the use of MBean. To understand the difference between an LLD rule collecting MBeans and an LLD rule collecting MBean attributes better please take a look at following table:

**MBean1** | **MBean2** | **MBean3**  
---|---|---  
MBean1Attribute1 | MBean2Attribute1 | MBean3Attribute1  
MBean1Attribute2 | MBean2Attribute2 | MBean3Attribute2  
MBean1Attribute3 | MBean2Attribute3 | MBean3Attribute3  
  
##### Example 1: Discovering MBeans

This rule will return 3 objects: the top row of the column: MBean1, MBean2, MBean3.

For more information about objects please refer to [supported macros](/documentation/current/en/manual/discovery/low_level_discovery/examples/jmx#supported-macros) table, _Discovery of MBeans_ section.

Discovery rule configuration collecting MBeans (without the attributes) looks like the following:

![lld_rule_mbean.png](/documentation/current/assets/en/manual/discovery/low_level_discovery/lld_rule_mbean.png)

The key used here:
    
    
    jmx.discovery[beans,"*:type=GarbageCollector,name=*"]

Copy

✔ Copied

All the garbage collectors without attributes will be discovered. As Garbage collectors have the same attribute set, we can use desired attributes in item prototypes the following way:

![lld_rule_mbean_prototypes.png](/documentation/current/assets/en/manual/discovery/low_level_discovery/lld_rule_mbean_prototypes.png)

The keys used here:
    
    
    jmx[{#JMXOBJ},CollectionCount] 
           jmx[{#JMXOBJ},CollectionTime] 
           jmx[{#JMXOBJ},Valid] 

Copy

✔ Copied

LLD discovery rule will result in something close to this (items are discovered for two Garbage collectors):

![discovery_rule_mbean_3.png](/documentation/current/assets/en/manual/discovery/low_level_discovery/discovery_rule_mbean_3.png)

##### Example 2: Discovering MBean attributes

This rule will return 9 objects with the following fields: MBean1Attribute1, MBean2Attribute1, MBean3Attribute1,MBean1Attribute2,MBean2Attribute2, MBean3Attribute2, MBean1Attribute3, MBean2Attribute3, MBean3Attribute3.

For more information about objects please refer to [supported macros](/documentation/current/en/manual/discovery/low_level_discovery/examples/jmx#supported-macros) table, _Discovery of MBean attributes_ section.

Discovery rule configuration collecting MBean attributes looks like the following:

![lld_rule_mbean_attr.png](/documentation/current/assets/en/manual/discovery/low_level_discovery/lld_rule_mbean_attr.png)

The key used here:
    
    
    jmx.discovery[attributes,"*:type=GarbageCollector,name=*"]

Copy

✔ Copied

All the garbage collectors with a single item attribute will be discovered.

![lld_rule_mbean_attr_prototypes.png](/documentation/current/assets/en/manual/discovery/low_level_discovery/lld_rule_mbean_attr_prototypes.png)

In this particular case an item will be created from prototype for every MBean attribute. The main drawback of this configuration is that trigger creation from trigger prototypes is impossible as there is only one item prototype for all attributes. So this setup can be used for data collection, but is not recommended for automatic monitoring.

#### Using jmx.get

`jmx.get[]` is similar to the `jmx.discovery[]` item, but it does not turn Java object properties into low-level discovery macro names and therefore can return values without limitations that are associated with LLD macro name generation such as hyphens or non-ASCII characters.

When using `jmx.get[]` for discovery, low-level discovery macros can be defined separately in the custom [LLD macro](/documentation/current/en/manual/discovery/low_level_discovery#discovery-rule) tab of the discovery rule configuration, using JSONPath to point to the required values.

##### Discovering MBeans

Discovery item: `jmx.get[beans,"com.example:type=*,*"]`

Response:
    
    
    [
               {
                   "object": "com.example:type=Hello,data-src=data-base,ключ=значение",
                   "domain": "com.example",
                   "properties": {
                       "data-src": "data-base",
                       "ключ": "значение",
                       "type": "Hello"
                   }
               },
               {
                   "object": "com.example:type=Atomic",
                   "domain": "com.example",
                   "properties": {
                       "type": "Atomic"
                   }
               }
           ]

Copy

✔ Copied

##### Discovering MBean attributes

Discovery item: `jmx.get[attributes,"com.example:type=*,*"]`

Response:
    
    
    [
               {
                   "object": "com.example:type=*",
                   "domain": "com.example",
                   "properties": {
                       "type": "Simple"
                   }
               },
               {
                   "object": "com.zabbix:type=yes,domain=zabbix.com,data-source=/dev/rand,ключ=значение,obj=true",
                   "domain": "com.zabbix",
                   "properties": {
                       "type": "Hello",
                       "domain": "com.example",
                       "data-source": "/dev/rand",
                       "ключ": "значение",
                       "obj": true
                   }
               }
           ]

Copy

✔ Copied