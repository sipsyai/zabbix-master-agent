---
title: Custom LLD rules
source: https://www.zabbix.com/documentation/current/en/manual/discovery/low_level_discovery/custom_rules
downloaded: 2025-11-14 10:37:40
---

# 8 Custom LLD rules  
  
### Overview

It is also possible to create a completely custom LLD rule, discovering any type of entities - for example, databases on a database server.

To do so, a custom item should be created that returns a JSON string, specifying the found objects and optionally - some properties of them. The amount of macros per entity is not limited - while the built-in discovery rules return either one or two macros (for example, two for filesystem discovery), it is possible to return more.

### Example

The required JSON string format is best illustrated with an example. Suppose you are running an old Zabbix 1.8 agent (one that does not support the [vfs.fs.discovery](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#vfs.fs.discovery) key), but you still need to discover file systems. Here is a simple Perl script for Linux that discovers mounted file systems and outputs in JSON, which includes both file system name and type. One way to use it would be as a UserParameter with key "vfs.fs.discovery_perl":
    
    
    #!/usr/bin/perl
           
           $first = 1;
           
           print "[\n";
           
           for (`cat /proc/mounts`)
           {
               ($fsname, $fstype) = m/\S+ (\S+) (\S+)/;
           
               print "\t,\n" if not $first;
               $first = 0;
           
               print "\t{\n";
               print "\t\t\"{#FSNAME}\":\"$fsname\",\n";
               print "\t\t\"{#FSTYPE}\":\"$fstype\"\n";
               print "\t}\n";
           }
           
           print "]\n";

Copy

✔ Copied

Allowed symbols for LLD macro names are **0-9** , **A-Z** , **_** , **.** Lowercase letters are not supported in the names.

An example of its output (reformatted for clarity) is shown below. The JSON for custom discovery checks has to follow the same format.
    
    
    [
               { "{#FSNAME}":"/",                           "{#FSTYPE}":"rootfs"   },
               { "{#FSNAME}":"/sys",                        "{#FSTYPE}":"sysfs"    },
               { "{#FSNAME}":"/proc",                       "{#FSTYPE}":"proc"     },
               { "{#FSNAME}":"/dev",                        "{#FSTYPE}":"devtmpfs" },
               { "{#FSNAME}":"/dev/pts",                    "{#FSTYPE}":"devpts"   },
               { "{#FSNAME}":"/lib/init/rw",                "{#FSTYPE}":"tmpfs"    },
               { "{#FSNAME}":"/dev/shm",                    "{#FSTYPE}":"tmpfs"    },
               { "{#FSNAME}":"/home",                       "{#FSTYPE}":"ext3"     },
               { "{#FSNAME}":"/tmp",                        "{#FSTYPE}":"ext3"     },
               { "{#FSNAME}":"/usr",                        "{#FSTYPE}":"ext3"     },
               { "{#FSNAME}":"/var",                        "{#FSTYPE}":"ext3"     },
               { "{#FSNAME}":"/sys/fs/fuse/connections",    "{#FSTYPE}":"fusectl"  }
           ]

Copy

✔ Copied

In the previous example it is required that the keys match the LLD macro names used in prototypes, the alternative is to extract LLD macro values using JSONPath `{#FSNAME}` → `$.fsname` and `{#FSTYPE}` → `$.fstype`, thus making such script possible:
    
    
    #!/usr/bin/perl
            
           $first = 1;
            
           print "[\n";
            
           for (`cat /proc/mounts`)
           {
               ($fsname, $fstype) = m/\S+ (\S+) (\S+)/;
            
               print "\t,\n" if not $first;
               $first = 0;
            
               print "\t{\n";
               print "\t\t\"fsname\":\"$fsname\",\n";
               print "\t\t\"fstype\":\"$fstype\"\n";
               print "\t}\n";
           }
            
           print "]\n";

Copy

✔ Copied

An example of its output (reformatted for clarity) is shown below.
    
    
    [
               { "fsname":"/",                           "fstype":"rootfs"   },
               { "fsname":"/sys",                        "fstype":"sysfs"    },
               { "fsname":"/proc",                       "fstype":"proc"     },
               { "fsname":"/dev",                        "fstype":"devtmpfs" },
               { "fsname":"/dev/pts",                    "fstype":"devpts"   },
               { "fsname":"/lib/init/rw",                "fstype":"tmpfs"    },
               { "fsname":"/dev/shm",                    "fstype":"tmpfs"    },
               { "fsname":"/home",                       "fstype":"ext3"     },
               { "fsname":"/tmp",                        "fstype":"ext3"     },
               { "fsname":"/usr",                        "fstype":"ext3"     },
               { "fsname":"/var",                        "fstype":"ext3"     },
               { "fsname":"/sys/fs/fuse/connections",    "fstype":"fusectl"  }
           ]

Copy

✔ Copied

Then, in the discovery rule's _Filter_ field, you may specify "{#FSTYPE}" as a macro and "rootfs|ext3" as a regular expression.

You don't have to use macro names like FSNAME/FSTYPE with custom LLD rules, you are free to use whatever names you like. In case JSONPath is used then the LLD row will be an array element that can be an object, but it can be also another array or a value.

Note that, if using a user parameter, the return value is limited to 16MB. For more details, see [data limits for LLD return values](/documentation/current/en/manual/discovery/low_level_discovery/notes#data-limits-for-return-values).