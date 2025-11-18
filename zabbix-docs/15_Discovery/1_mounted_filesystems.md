---
title: Discovery of mounted filesystems
source: https://www.zabbix.com/documentation/current/en/manual/discovery/low_level_discovery/examples/mounted_filesystems
downloaded: 2025-11-14 10:37:26
---

# 1 Discovery of mounted filesystems

#### Overview

It is possible to discover mounted filesystems and their properties:

  * mountpoint name
  * filesystem type
  * filesystem size
  * inode statistics
  * mount options

To do that, you may use a combination of:

  * the [`vfs.fs.get`](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#vfs.fs.get) agent item as the master item
  * dependent low-level discovery rule and item prototypes

#### Configuration

##### Master item

Create a Zabbix agent item using the following key:
    
    
    vfs.fs.get

Copy

✔ Copied

![](/documentation/current/assets/en/manual/discovery/low_level_discovery/fs_get_item.png)

Set the type of information to "Text" for possibly big JSON data.

The data returned by this item will contain something like the following for a mounted filesystem:
    
    
    [
             {
               "fsname": "/",
               "fstype": "ext4",
               "bytes": {
                 "total": 249405239296,
                 "free": 24069537792,
                 "used": 212595294208,
                 "pfree": 10.170306,
                 "pused": 89.829694
               },
               "inodes": {
                 "total": 15532032,
                 "free": 12656665,
                 "used": 2875367,
                 "pfree": 81.487503,
                 "pused": 18.512497
               },
               "options": "rw,noatime,errors=remount-ro"
             }
           ]

Copy

✔ Copied

##### Dependent LLD rule

Create a low-level discovery rule as "Dependent item" type:

![](/documentation/current/assets/en/manual/discovery/low_level_discovery/fs_get_lld.png)

As master item select the `vfs.fs.get` item we created.

In the "LLD macros" tab define custom macros with the corresponding JSONPath:

![](/documentation/current/assets/en/manual/discovery/low_level_discovery/fs_get_lld_b.png)

In the "Filters" tab you may add a regular expression that filters only **read-write** filesystems:

![](/documentation/current/assets/en/manual/discovery/low_level_discovery/fs_get_lld_c.png)

##### Dependent item prototype

Create an item prototype with "Dependent item" type in this LLD rule. As master item for this prototype select the `vfs.fs.get` item we created.

![](/documentation/current/assets/en/manual/discovery/low_level_discovery/fs_get_prototype.png)

Note the use of custom macros in the item prototype name and key:

  * _Name_ : Free disk space on {#FSNAME}, type: {#FSTYPE}
  * _Key_ : Free[{#FSNAME}]

As type of information, use:

  * _Numeric (unsigned)_ for metrics like 'free', 'total', 'used'
  * _Numeric (float)_ for metrics like 'pfree', 'pused' (percentage)

In the item prototype "Preprocessing" tab select JSONPath and use the following JSONPath expression as parameter:
    
    
    $.[?(@.fsname=='{#FSNAME}')].bytes.free.first()

Copy

✔ Copied

![](/documentation/current/assets/en/manual/discovery/low_level_discovery/fs_get_prototype_b.png)

When discovery starts, one item per each mountpoint will be created. This item will return the number of free bytes for the given mountpoint.