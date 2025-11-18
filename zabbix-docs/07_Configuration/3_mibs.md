---
title: MIB files
source: https://www.zabbix.com/documentation/current/en/manual/config/items/itemtypes/snmp/mibs
downloaded: 2025-11-14 10:35:01
---

# 3 MIB files  
  
#### Introduction

MIB stands for the Management Information Base. MIB files allow to use textual representation of an OID (Object Identifier). It is possible to use raw OIDs when monitoring SNMP devices with Zabbix, but if you feel more comfortable using textual representation, you need to install MIB files.

For example,
    
    
    ifHCOutOctets

Copy

✔ Copied

is textual representation of the OID
    
    
    1.3.6.1.2.1.31.1.1.1.10

Copy

✔ Copied

#### Installing MIB files

On Debian-based systems:
    
    
    apt install snmp-mibs-downloader
           download-mibs

Copy

✔ Copied

On RedHat-based systems:
    
    
    dnf install net-snmp-libs

Copy

✔ Copied

#### Enabling MIB files

On RedHat-based systems, MIB files should be enabled by default. On Debian-based systems, you have to edit the file `/etc/snmp/snmp.conf` and comment out the line that says `mibs :`
    
    
    # As the snmp packages come without MIB files due to license reasons, loading
           # of MIBs is disabled by default. If you added the MIBs you can re-enable
           # loading them by commenting out the following line.
           mibs :

Copy

✔ Copied

#### Testing MIB files

Testing SNMP MIBs can be done using `snmpwalk` utility. If you don't have it installed, use the following instructions.

On Debian-based systems:
    
    
    apt install snmp

Copy

✔ Copied

On RedHat-based systems:
    
    
    dnf install net-snmp-utils

Copy

✔ Copied

After that, the following command must not give error when you query a network device:
    
    
    $ snmpwalk -v 2c -c public <NETWORK DEVICE IP> ifInOctets
           IF-MIB::ifInOctets.1 = Counter32: 176137634
           IF-MIB::ifInOctets.2 = Counter32: 0
           IF-MIB::ifInOctets.3 = Counter32: 240375057
           IF-MIB::ifInOctets.4 = Counter32: 220893420
           [...]

Copy

✔ Copied

#### Using MIBs in Zabbix

The most important to keep in mind is that Zabbix processes do not get informed of the changes made to MIB files. So after every change you must restart Zabbix server or proxy, e. g.:
    
    
    systemctl restart zabbix-server

Copy

✔ Copied

After that, the changes made to MIB files are in effect.

#### Using custom MIB files

There are standard MIB files coming with every GNU/Linux distribution. But some device vendors provide their own.

Let's say, you would like to use [CISCO-SMI](ftp://ftp.cisco.com/pub/mibs/v2/CISCO-SMI.my) MIB file. The following instructions will download and install it:
    
    
    wget ftp://ftp.cisco.com/pub/mibs/v2/CISCO-SMI.my -P /tmp
           mkdir -p /usr/local/share/snmp/mibs
           grep -q '^mibdirs +/usr/local/share/snmp/mibs' /etc/snmp/snmp.conf 2>/dev/null || echo "mibdirs +/usr/local/share/snmp/mibs" >> /etc/snmp/snmp.conf
           cp /tmp/CISCO-SMI.my /usr/local/share/snmp/mibs

Copy

✔ Copied

Now you should be able to use it. Try to translate the name of the object _ciscoProducts_ from the MIB file to OID:
    
    
    snmptranslate -IR -On CISCO-SMI::ciscoProducts
           .1.3.6.1.4.1.9.1

Copy

✔ Copied

If you receive errors instead of the OID, ensure all the previous commands did not return any errors.

The object name translation worked, you are ready to use custom MIB file. Note the MIB name prefix (_CISCO-SMI::_) used in the query. You will need this when using command-line tools as well as Zabbix.

Don't forget to restart Zabbix server/proxy before using this MIB file in Zabbix.

Keep in mind that MIB files can have dependencies. That is, one MIB may require another. In order to satisfy these dependencies you have to install all the affected MIB files.