---
title: SNMP traps
source: https://www.zabbix.com/documentation/current/en/manual/config/items/itemtypes/snmptrap
downloaded: 2025-11-14 10:35:02
---

# 3 SNMP traps

#### Overview

Receiving SNMP traps is the opposite to querying SNMP-enabled devices.

In this case, the information is sent from an SNMP-enabled device to snmptrapd and is collected or "trapped" by Zabbix server or Zabbix proxy from file.

Usually, traps are sent upon some condition change and the agent connects to the server on port 162 (as opposed to port 161 on the agent side that is used for queries). Using traps may detect some short problems that occur amidst the query interval and may be missed by the query data.

Receiving SNMP traps in Zabbix is designed to work with **snmptrapd** and one of the mechanisms for passing the traps to Zabbix - either a Bash or Perl script or SNMPTT.

The simplest way to set up trap monitoring after configuring Zabbix is to use the Bash script solution, because Perl and SNMPTT are often missing in modern distributions and require more complex configuration. However, this solution uses a script configured as `traphandle`. For better performance on production systems, use the embedded Perl solution (either script with `do perl` option or SNMPTT).

The workflow of receiving a trap:

  1. `snmptrapd` receives a trap
  2. `snmptrapd` passes the trap to the receiver script (Bash, Perl) or SNMPTT
  3. The receiver parses, formats and writes the trap to a file
  4. Zabbix SNMP trapper reads and parses the trap file
  5. For each trap Zabbix finds all "SNMP trapper" items with host interfaces matching the received trap address. Note that only the selected "IP" or "DNS" in host interface is used during the matching.
  6. For each found item, the trap is compared to regexp in `snmptrap[regexp]`. The trap is set as the value of **all** matched items. If no matching item is found and there is an `snmptrap.fallback` item, the trap is set as the value of that.
  7. If the trap was not set as the value of any item, Zabbix by default logs the unmatched trap. (This is configured by "Log unmatched SNMP traps" in Administration > General > Other.)

##### Notes on HA failover

During high-availability (HA) node switch, Zabbix will continue processing after the last record within the last ISO 8601 timestamp; if the same record is not found then only the timestamp will be used to identify last position.

#### Configuring SNMP traps

This item type requires the following frontend configuration.

1\. Create an SNMP interface for your host

  * In _Data collection > Hosts_, create/edit the host, and in the _Interfaces_ field, add the interface type "SNMP", specifying the IP or DNS address.  
  
The address from each received trap will be compared to the IP and DNS addresses of all SNMP interfaces to find the corresponding hosts.

2\. Configure the item

  * In _Data collection > Hosts_, create/edit the necessary item.
  * In the _Key_ field, use one of the SNMP trap keys:

Description | Return value | Comments  
---|---|---  
**snmptrap**[regexp]  
Catches all SNMP traps that match the [regular expression](/documentation/current/en/manual/regular_expressions) specified in **regexp**. If regexp is unspecified, catches any trap. | SNMP trap | This item can be set only for SNMP interfaces.  
User macros and global regular expressions are supported in the parameter of this item key.  
**snmptrap.fallback**  
Catches all SNMP traps that were not caught by any of the snmptrap[] items for that interface. | SNMP trap | This item can be set only for SNMP interfaces.  
  
Multiline regular expression matching is not supported at this time.

  * Set the _Type of information_ to "Log" for the timestamps to be parsed. Other formats such as "Numeric" are also acceptable but might require a custom trap handler.

#### Setting up SNMP trap monitoring

##### Configuring Zabbix server/proxy

To read the traps, Zabbix server or proxy must be configured to start the SNMP trapper process and point to the trap file that is being written by SNMPTT or a Bash/Perl trap receiver. To do that, edit the configuration file ([zabbix_server.conf](/documentation/current/en/manual/appendix/config/zabbix_server) or [zabbix_proxy.conf](/documentation/current/en/manual/appendix/config/zabbix_proxy)):
    
    
    StartSNMPTrapper=1
           SNMPTrapperFile=[TRAP FILE]

Copy

✔ Copied

If systemd parameter **[PrivateTmp](http://www.freedesktop.org/software/systemd/man/systemd.exec.html#PrivateTmp=)** is used, this file is unlikely to work in _/tmp_.

##### Configuring Bash trap receiver

Requirements: only snmptrapd.

A Bash trap receiver [script](https://raw.githubusercontent.com/zabbix/zabbix-docker/trunk/Dockerfiles/snmptraps/alpine/conf/usr/sbin/zabbix_trap_handler.sh) can be used to pass traps to Zabbix server from snmptrapd using trapper file. To configure it, add the `traphandle` option to snmptrapd configuration file (`snmptrapd.conf`), see [example](https://raw.githubusercontent.com/zabbix/zabbix-docker/trunk/Dockerfiles/snmptraps/alpine/conf/etc/snmp/snmptrapd.conf).

snmptrapd might need to be restarted to pick up changes to its configuration.

##### Configuring Perl trap receiver

Requirements: Perl, Net-SNMP compiled with --enable-embedded-perl (done by default since Net-SNMP 5.4)

A Perl trap receiver (look for misc/snmptrap/zabbix_trap_receiver.pl) can be used to pass traps to Zabbix server directly from snmptrapd. To configure it:

  * add the Perl script to the snmptrapd configuration file (snmptrapd.conf), e.g.:

    
    
    perl do "[FULL PATH TO PERL RECEIVER SCRIPT]";

Copy

✔ Copied

  * configure the receiver, e.g:

    
    
    $SNMPTrapperFile = '[TRAP FILE]';
           $DateTimeFormat = '[DATE TIME FORMAT]';

Copy

✔ Copied

snmptrapd might need to be restarted to pick up changes to its configuration.

If the script name is not quoted, snmptrapd will refuse to start up with messages, similar to these:  
  

    
    
    Regexp modifiers "/l" and "/a" are mutually exclusive at (eval 2) line 1, at end of line
           Regexp modifier "/l" may not appear twice at (eval 2) line 1, at end of line

Copy

✔ Copied

##### Configuring SNMPTT

At first, snmptrapd should be configured to use SNMPTT.

For the best performance, SNMPTT should be configured as a daemon using **snmptthandler-embedded** to pass the traps to it. See instructions for [configuring SNMPTT](http://snmptt.sourceforge.net/docs/snmptt.shtml).

When SNMPTT is configured to receive the traps, configure `snmptt.ini`:

  1. enable the use of the Perl module from the NET-SNMP package:

    
    
    net_snmp_perl_enable = 1

Copy

✔ Copied

  2. log traps to the trap file which will be read by Zabbix:

    
    
    log_enable = 1
           log_file = [TRAP FILE]

Copy

✔ Copied

  3. set the date-time format:

    
    
    date_time_format = %Y-%m-%dT%H:%M:%S%z

Copy

✔ Copied

The "net-snmp-perl" package has been removed in RHEL 8.0-8.2; re-added in RHEL 8.3. For more information, see the [known issues](/documentation/current/en/manual/installation/known_issues#snmp-traps).

Now format the traps for Zabbix to recognize them (edit snmptt.conf):

  1. Each FORMAT statement should start with "ZBXTRAP [address]", where [address] will be compared to IP and DNS addresses of SNMP interfaces on Zabbix. E.g.:

    
    
    EVENT coldStart .1.3.6.1.6.3.1.1.5.1 "Status Events" Normal
           FORMAT ZBXTRAP $aA Device reinitialized (coldStart)

Copy

✔ Copied

  2. See more about SNMP trap format below.

Do not use unknown traps - Zabbix will not be able to recognize them. Unknown traps can be handled by defining a general event in snmptt.conf:  
  

    
    
    EVENT general .* "General event" Normal

Copy

✔ Copied

##### SNMP trap format

All customized Perl trap receivers and SNMPTT trap configuration must format the trap in the following way:
    
    
    [timestamp] [the trap, part 1] ZBXTRAP [address] [the trap, part 2]

Copy

✔ Copied

where

  * [timestamp] - the timestamp in "%Y-%m-%dT%H:%M:%S%z" format
  * ZBXTRAP - header that indicates that a new trap starts in this line
  * [address] - IP address used to find the host for this trap

Note that "ZBXTRAP" and "[address]" will be cut out from the message during processing. If the trap is formatted otherwise, Zabbix might parse the traps unexpectedly.

Example trap:
    
    
    2024-01-11T15:28:47+0200 .1.3.6.1.6.3.1.1.5.3 Normal "Status Events" localhost - ZBXTRAP 192.168.1.1 Link down on interface 2. Admin state: 1. Operational state: 2

Copy

✔ Copied

This will result in the following trap for SNMP interface with IP=192.168.1.1:
    
    
    2024-01-11T15:28:47+0200 .1.3.6.1.6.3.1.1.5.3 Normal "Status Events"
           localhost - Link down on interface 2. Admin state: 1. Operational state: 2

Copy

✔ Copied

#### System requirements

It is recommended to [install MIB files](/documentation/current/en/manual/config/items/itemtypes/snmp/mibs) to ensure that item values are displayed in the correct format. Without the MIB files, formatting issues, such as displaying values in HEX instead of UTF-8 or vice versa, may occur.

##### Large file support

Zabbix has large file support for SNMP trapper files. The maximum file size that Zabbix can read is 2^63 (8 EiB). Note that the filesystem may impose a lower limit on the file size.

##### Log rotation

Zabbix does not provide any log rotation system - that should be handled by the user. The log rotation should first rename the old file and only later delete it so that no traps are lost:  

  1. Zabbix opens the trap file at the last known location and goes to step 3
  2. Zabbix checks if the currently opened file has been rotated by comparing the inode number to the defined trap file's inode number. If there is no opened file, Zabbix resets the last location and goes to step 1.
  3. Zabbix reads the data from the currently opened file and sets the new location.
  4. The new data are parsed. If this was the rotated file, the file is closed and goes back to step 2.
  5. If there was no new data, Zabbix sleeps for 1 second and goes back to step 2.

##### File system

Because of the trap file implementation, Zabbix needs the file system to support inodes to differentiate files (the information is acquired by a stat() call).

#### Setup examples using different SNMP protocol versions

This example uses snmptrapd and a Bash receiver script to pass traps to Zabbix server.

Setup:

  1. Configure Zabbix to start SNMP trapper and set the trap file. Add to `zabbix_server.conf`:

    
    
    StartSNMPTrapper=1
           SNMPTrapperFile=/var/lib/zabbix/snmptraps/snmptraps.log

Copy

✔ Copied

  2. Download the Bash script to `/usr/sbin/zabbix_trap_handler.sh`:

    
    
    curl -o /usr/sbin/zabbix_trap_handler.sh https://raw.githubusercontent.com/zabbix/zabbix-docker/trunk/Dockerfiles/snmptraps/alpine/conf/usr/sbin/zabbix_trap_handler.sh

Copy

✔ Copied

If necessary, adjust the ZABBIX_TRAPS_FILE variable in the script. To use the default value, create the parent directory first:
    
    
    mkdir -p /var/lib/zabbix/snmptraps

Copy

✔ Copied

  3. Add the following to `snmtrapd.conf` (refer to working [example](https://raw.githubusercontent.com/zabbix/zabbix-docker/trunk/Dockerfiles/snmptraps/alpine/conf/etc/snmp/snmptrapd.conf))

    
    
    traphandle default /bin/bash /usr/sbin/zabbix_trap_handler.sh

Copy

✔ Copied

snmptrapd might need to be restarted to pick up changes to its configuration.

  4. [Create](/documentation/current/en/manual/config/items/item) an SNMP item TEST (keep in mind the initial [configuration requirements](/documentation/current/en/manual/config/items/itemtypes/snmptrap#configuring-snmp-traps)):  

Type: SNMP trap  
Type of information: Log Host interface: SNMP 127.0.0.1  
Key: `snmptrap["linkUp"]`  
Log time format: yyyyMMdd.hhmmss

Note that the ISO 8601 date and time format is used.

  5. Next we will configure `snmptrapd` for our chosen SNMP protocol version and send test traps using the `snmptrap` utility.

##### SNMPv1, SNMPv2

SNMPv1 and SNMPv2 protocols rely on "community string" authentication. In the example below we will use "secret" as community string. It must be set to the same value on SNMP trap senders.

Please note that while still widely used in production environments, SNMPv2 doesn't offer any encryption and real sender authentication. The data is sent as plain text and therefore these protocol versions should only be used in secure environments such as private network and should never be used over any public or third-party network.

SNMP version 1 isn't really used these days since it doesn't support 64-bit counters and is considered a legacy protocol.

To enable accepting SNMPv1 or SNMPv2 traps you should add the following line to `snmptrapd.conf`. Replace "secret" with the SNMP community string configured on SNMP trap senders:
    
    
    authCommunity log,execute,net secret

Copy

✔ Copied

Next we can send a test trap using `snmptrap`. We will use the common "link up" OID in this example:
    
    
    snmptrap -v 2c -c secret localhost '' linkUp.0

Copy

✔ Copied

##### SNMPv3

SNMPv3 addresses SNMPv1/v2 security issues and provides authentication and encryption. You can use the MD5 or multiple SHA authentication methods and DES/multiple AES as cipher.

To enable accepting SNMPv3 add the following lines to `snmptrapd.conf`:
    
    
    createUser -e 0x8000000001020304 traptest SHA mypassword AES
           authuser log,execute traptest

Copy

✔ Copied

Please note the "execute" keyword that allows to execute scripts for this user security model.
    
    
    snmptrap -v 3 -n "" -a SHA -A mypassword -x AES -X mypassword -l authPriv -u traptest -e 0x8000000001020304 localhost 0 linkUp.0

Copy

✔ Copied

If you wish to use strong encryption methods such as AES192 or AES256, please use net-snmp starting with version 5.8. You might have to recompile it with `configure` option: `--enable-blumenthal-aes`. Older versions of net-snmp do not support AES192/AES256. See also: [Strong Authentication or Encryption](http://www.net-snmp.org/wiki/index.php/Strong_Authentication_or_Encryption).

##### Verification

In both examples you will see similar lines in your `/var/lib/zabbix/snmptraps/snmptraps.log`:
    
    
    2024-01-30T10:04:23+0200 ZBXTRAP 127.0.0.1
           UDP: [127.0.0.1]:56585->[127.0.0.1]:162
           DISMAN-EVENT-MIB::sysUpTimeInstance = 2538834
           SNMPv2-MIB::snmpTrapOID.0 = IF-MIB::linkUp.0

Copy

✔ Copied

The item value in Zabbix will be:
    
    
    2024-01-30 10:04:23 2024-01-30 10:04:21 
           
           2024-01-30T10:04:21+0200 UDP: [127.0.0.1]:56585->[127.0.0.1]:162
           DISMAN-EVENT-MIB::sysUpTimeInstance = 2538834
           SNMPv2-MIB::snmpTrapOID.0 = IF-MIB::linkUp.0

Copy

✔ Copied

Example with Perl:
    
    
    2024-01-30T11:42:54+0200 ZBXTRAP 127.0.0.1
           PDU INFO:
             receivedfrom                   UDP: [127.0.0.1]:58649->[127.0.0.1]:162
             notificationtype               TRAP
             version                        1
             community                      public
             errorstatus                    0
             transactionid                  1
             requestid                      2101882550
             messageid                      0
             errorindex                     0
           VARBINDS:
             DISMAN-EVENT-MIB::sysUpTimeInstance type=67 value=Timeticks: (457671) 1:16:16.71
             SNMPv2-MIB::snmpTrapOID.0      type=6  value=OID: IF-MIB::linkUp.0

Copy

✔ Copied

#### See also

  * [Zabbix blog article on SNMP traps](https://blog.zabbix.com/snmp-traps-in-zabbix)
  * [Configuring snmptrapd (official net-snmp documentation)](https://net-snmp.sourceforge.io/wiki/index.php/TUT:Configuring_snmptrapd)
  * [Configuring snmptrapd to receive SNMPv3 notifications (official net-snmp documentation)](https://net-snmp.sourceforge.io/wiki/index.php/TUT:Configuring_snmptrapd_to_receive_SNMPv3_notifications)