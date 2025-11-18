---
title: Discovery prototypes
source: https://www.zabbix.com/documentation/current/en/manual/discovery/low_level_discovery/discovery_prototypes
downloaded: 2025-11-14 10:37:23
---

# 5 Discovery prototypes

#### Overview

Discovery prototypes are **nested low-level discovery** rules within a "parent" discovery rule, allowing to create multi-level discovery of objects with their own items, triggers, etc. For example, you may want to discover all database instances on a database server, then discover tablespaces for each instance, then discover tables for each tablespace.

Discovery prototypes have their own item, trigger, graph, host, and discovery prototypes. A nested discovery prototype will use the same JSON value as the parent rule if you specify a _Nested_ type.

The levels of nesting for discovery prototypes are unlimited.

#### Configuration

To create a discovery prototype:

  * Click on _Discovery prototypes_ in the row of an existing discovery rule

![](/documentation/current/assets/en/manual/discovery/low_level_discovery/discovery_prototypes.png)

  * Click on _Create discovery prototype_

![](/documentation/current/assets/en/manual/discovery/low_level_discovery/discovery_prototype.png)

Configuration fields of this form are shared with the regular [low-level discovery](/documentation/current/en/manual/discovery/low_level_discovery#discovery-rule).

If you select "Nested" as _Type_ in the opened discovery prototype form, then discovery rules (from the discovery prototype) are generated based on a JSON object from the same JSON value as the parent discovery rule. For example, if the original JSON is [<object A>, <object B>] and there is one nested discovery rule prototype then two discovery rules would be generated based on object A and object B data respectively.

In this case the discovery prototype is activated at the same time as the parent rule. The nested rule thus can use preprocessing, to work on another "slice" of the same data, already acquired by the parent.

LLD macros from the parent LLD rule are available for nested discovery rules.

##### Nested LLD rules on discovered hosts

A _Nested_ low-level discovery rule can be used on a host template assigned to host prototype. If a _Nested_ discovery rule exists on a discovered host, then the JSON object used to discover the host is also sent to all LLD rules of nested type on this host. For more details, see example.

LLD macros from the discovery rule that created the host are available for nested discovery rules.

#### Example

Let's illustrate possible application of discovery prototypes, based on receiving the following example of multi-level JSON.
    
    
    [
             {
               "database": "db1",
               "created_at": "2024-02-01T12:30:00Z",
               "encoding": "UTF8",
               "tablespaces": [
                 { "name": "ts1", "max_size": "10GB" },
                 { "name": "ts2", "max_size": "20GB" },
                 { "name": "ts3", "max_size": "15GB" }
               ]
             },
             {
               "database": "db2",
               "created_at": "2023-11-15T08:45:00Z",
               "encoding": "UTF16",
               "tablespaces": [
                 { "name": "ts1", "max_size": "5GB" },
                 { "name": "ts2", "max_size": "25GB" },
                 { "name": "ts3", "max_size": "30GB" }
               ]
             },
             {
               "database": "db3",
               "created_at": "2024-01-05T15:10:00Z",
               "encoding": "UTF8",
               "tablespaces": [
                 { "name": "ts1", "max_size": "12GB" },
                 { "name": "ts2", "max_size": "18GB" },
                 { "name": "ts3", "max_size": "22GB" }
               ]
             }
           ]

Copy

✔ Copied

###### Case 1

Discovering database instances on a database server, then discovering the tablespaces for each instance.

  1. You have at least one host related to database server discovery.

  2. Create an [LLD rule](/documentation/current/en/manual/discovery/low_level_discovery#discovery-rule) for this host named _Discover databases and tablespaces_.

  3. Switch to the _LLD Macros_ tab on this rule, add macro `{#DB}=$.database`.

  4. Add an item prototype for this rule named _Active connections to {#DB}_ (Type: Agent, Key: `db.connections[{#DB}]`).

  5. The items related to each database are discovered:

    
    
    Active connections to db1, Active connections to db2, Active connections to db3.

Copy

✔ Copied

  6. Create a discovery prototype for this rule named _Discover tablespaces for {#DB}_ (Type: Nested, Key: `db.tablespace.discovery[{#DB}]`).

  7. Switch to the _Preprocessing_ tab of this discovery prototype and add the step `JSONPath=$.tablespaces`.

  8. Switch to the _LLD Macros_ tab of this discovery prototype, add macro `{#TSNAME}=$.name`.

  9. Create an item prototype for this discovery prototype named  _Size of tablespace {#TSNAME} for {#DB}_ (Type: Agent, Key: `db.ts.size[{#DB}, {#TSNAME}]`).

  10. The items related to each tablespace of each database are discovered:

    
    
    Size of tablespace ts1 for db1, Size of tablespace ts2 for db1, Size of tablespace ts3 for db1,
           Size of tablespace ts1 for db2, Size of tablespace ts2 for db2, Size of tablespace ts3 for db2,
           Size of tablespace ts1 for db3, Size of tablespace ts2 for db3, Size of tablespace ts3 for db3.

Copy

✔ Copied

with keys `db.ts.size[db1,ts1]`, `db.ts.size[db1,ts2]`, ... `db.ts.size[db3,ts3]`.

###### Case 2

Discovering database instances on the database server by representing them as discovered hosts, then discovering the tablespaces for each instance.

  1. You have at least one host (root host) related to database server discovery.

  2. Create a template to discover the tablespaces for each database.

  3. Create an item in this template named _Active connections to {#DB}_ (Type: Agent, Key: `db.connections[{#DB}]`).

  4. Create an [LLD rule](/documentation/current/en/manual/discovery/low_level_discovery#discovery-rule) for this template named _Discover tablespaces_ (Type: Nested).

  5. Switch to the _Preprocessing_ tab of this rule and add the step `JSONPath=$.tablespaces`.

  6. Switch to the _LLD Macros_ tab of this rule, add macro `{#TSNAME}=$.name`.

  7. Create an item prototype for this rule named  _Size of tablespace {#TSNAME} for {#DB}_ (Type: Agent, Key: `db.ts.size[{#DB}, {#TSNAME}]`).

  8. Back on the root host, create an [LLD rule](/documentation/current/en/manual/discovery/low_level_discovery#discovery-rule) for this host named _Discover databases and tablespaces_.

  9. Switch to the _LLD Macros_ tab on this rule, add macro `{#DB}=$.database`.

  10. Add a host prototype for this rule named _Host for database {#DB}_.

  11. Switch to the _Macros_ tab on this host prototype, add macro `{$DB}={#DB}` (for the item's name and key from Step 3).

  12. Link the template from step 2 to this host prototype.

  13. The discovered hosts contain the discovered items related to each database and its tablespaces:

_Host for database db1_ | Active connections to db1  
Size of tablespace ts1 for db1  
Size of tablespace ts2 for db1  
Size of tablespace ts3 for db1  
---|---  
_Host for database db2_ | Active connections to db2  
Size of tablespace ts1 for db2  
Size of tablespace ts2 for db2  
Size of tablespace ts3 for db2  
_Host for database db3_ | Active connections to db3  
Size of tablespace ts1 for db3  
Size of tablespace ts2 for db3  
Size of tablespace ts3 for db3