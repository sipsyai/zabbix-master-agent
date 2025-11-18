---
title: Sender
source: https://www.zabbix.com/documentation/current/en/manual/concepts/sender
downloaded: 2025-11-14 10:33:56
---

# 6 Sender

#### Overview

Zabbix sender is a command line utility that may be used to send performance data to Zabbix server for processing.

The utility is usually used in long running user scripts for periodical sending of availability and performance data.

For sending results directly to Zabbix server or proxy, a [trapper item](/documentation/current/en/manual/config/items/itemtypes/trapper) type must be configured.

See also [zabbix_utils](https://github.com/zabbix/python-zabbix-utils/blob/main/README.md) \- a Python library that has built-in functionality to act like Zabbix sender.

#### Running Zabbix sender

An example of running Zabbix UNIX sender:
    
    
    cd bin
           ./zabbix_sender -z zabbix -s "Linux DB3" -k db.connections -o 43

Copy

✔ Copied

where:

  * z - Zabbix server host (IP address can be used as well)
  * s - technical name of monitored host (as registered in Zabbix frontend)
  * k - item key
  * o - value to send

Options that contain whitespaces, must be quoted using double quotes.

Zabbix sender can be used to send multiple values from an input file. See the [Zabbix sender manpage](/documentation/current/en/manpages/zabbix_sender) for more information.

If a configuration file is specified, Zabbix sender uses all addresses defined in the agent ServerActive configuration parameter for sending data. If sending to one address fails, the sender tries sending to the other addresses. If sending of batch data fails to one address, the following batches are not sent to this address.

Zabbix sender accepts strings in UTF-8 encoding (for both UNIX-like systems and Windows) without byte order mark (BOM) first in the file.

Zabbix sender on Windows can be run similarly:
    
    
    zabbix_sender.exe [options]

Copy

✔ Copied

zabbix_sender realtime sending scenarios will gather multiple values passed to it in close succession and send them to the server in a single connection. A value that is not further apart from the previous value than 0.2 seconds can be put in the same stack, but maximum polling time still is 1 second.

Zabbix sender will terminate if invalid (not following _parameter=value_ notation) parameter entry is present in the specified configuration file.

#### Running Zabbix sender with low-level discovery

An example of running Zabbix sender for sending a JSON-formatted value for low-level discovery:
    
    
    ./zabbix_sender -z 192.168.1.113 -s "Zabbix server" -k trapper.discovery.item -o '[{"{#FSNAME}":"/","{#FSTYPE}":"rootfs"},{"{#FSNAME}":"/sys","{#FSTYPE}":"sysfs"}]'

Copy

✔ Copied

For this to work, the low-level discovery rule must have a Zabbix trapper item type (in this example, with `trapper.discovery.item` key).