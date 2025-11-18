---
title: SNMP agent
source: https://www.zabbix.com/documentation/current/en/manual/config/items/itemtypes/snmp
downloaded: 2025-11-14 10:34:58
---

# 2 SNMP agent

## Overview

You may want to use SNMP monitoring on devices such as printers, network switches, routers or UPS that usually are SNMP-enabled and on which it would be impractical to attempt setting up complete operating systems and Zabbix agents.

To be able to retrieve data provided by SNMP agents on these devices, Zabbix server must be [initially configured](/documentation/current/en/manual/installation/install#configure-the-sources) with SNMP support by specifying the `--with-net-snmp` flag. It is recommended to also [install MIB files](/documentation/current/en/manual/config/items/itemtypes/snmp/mibs) to ensure that item values are displayed in the correct format. Without the MIB files, formatting issues, such as displaying values in HEX instead of UTF-8 or vice versa, may occur.

SNMP checks are performed over the UDP protocol only.

Zabbix server and proxy daemons log lines similar to the following if they receive an incorrect SNMP response:
    
    
    SNMP response from host "gateway" does not contain all of the requested variable bindings

Copy

✔ Copied

While they do not cover all the problematic cases, they are useful for identifying individual SNMP devices for which combined requests should be disabled.

Zabbix server/proxy will retry up to 5 times for SNMP `walk` and `get` items. The retry mechanism doesn't apply to DNS resolution failures.

For legacy SNMP checks (single OID number or string) Zabbix server/proxy will retry at least one time after an unsuccessful query attempt: either through the SNMP library's retrying mechanism or through the internal combined processing mechanism.

If monitoring SNMPv3 devices, make sure that msgAuthoritativeEngineID (also known as snmpEngineID or "Engine ID") is never shared by two devices. According to [RFC 2571](http://www.ietf.org/rfc/rfc2571.txt) (section 3.1.1.1) it must be unique for each device.

RFC3414 requires the SNMPv3 devices to persist their engineBoots. Some devices do not do that, which results in their SNMP messages being discarded as outdated after being restarted. In such situation, SNMP cache needs to be manually cleared on a server/proxy (by using [-R snmp_cache_reload](/documentation/current/en/manual/concepts/server#runtime-control)) or the server/proxy needs to be restarted.

## Configuring SNMP monitoring

To start monitoring a device through SNMP, the following steps have to be performed:

#### Step 1

Find out the SNMP string (or OID) of the item you want to monitor.

To get a list of SNMP strings, use the **snmpwalk** command (part of [net-snmp](http://www.net-snmp.org/) software which you should have installed as part of the Zabbix installation) or equivalent tool:
    
    
    snmpwalk -v 2c -c public <host IP> .

Copy

✔ Copied

As '2c' here stands for SNMP version, you may also substitute it with '1', to indicate SNMP Version 1 on the device.

This should give you a list of SNMP strings and their last value. If it doesn't then it is possible that the SNMP 'community' is different from the standard 'public' in which case you will need to find out what it is.

You can then go through the list until you find the string you want to monitor, e.g. if you wanted to monitor the bytes coming in to your switch on port 3 you would use the `IF-MIB::ifHCInOctets.3` string from this line:
    
    
    IF-MIB::ifHCInOctets.3 = Counter64: 3409739121

Copy

✔ Copied

You may now use the **snmpget** command to find out the numeric OID for 'IF-MIB::ifHCInOctets.3':
    
    
    snmpget -v 2c -c public -On <host IP> IF-MIB::ifHCInOctets.3

Copy

✔ Copied

Note that the last number in the string is the port number you are looking to monitor. See also: [Dynamic indexes](/documentation/current/en/manual/config/items/itemtypes/snmp/dynamicindex).

This should give you something like the following:
    
    
    .1.3.6.1.2.1.31.1.1.1.6.3 = Counter64: 3472126941

Copy

✔ Copied

Again, the last number in the OID is the port number.

Some of the most used SNMP OIDs are [translated automatically to a numeric representation](/documentation/current/en/manual/config/items/itemtypes/snmp/special_mibs) by Zabbix.

In the last example above value type is "Counter64", which internally corresponds to ASN_COUNTER64 type. The full list of supported types is ASN_COUNTER, ASN_COUNTER64, ASN_UINTEGER, ASN_UNSIGNED64, ASN_INTEGER, ASN_INTEGER64, ASN_FLOAT, ASN_DOUBLE, ASN_TIMETICKS, ASN_GAUGE, ASN_IPADDRESS, ASN_OCTET_STR and ASN_OBJECT_ID. These types roughly correspond to "Counter32", "Counter64", "UInteger32", "INTEGER", "Float", "Double", "Timeticks", "Gauge32", "IpAddress", "OCTET STRING", "OBJECT IDENTIFIER" in **snmpget** output, but might also be shown as "STRING", "Hex-STRING", "OID" and other, depending on the presence of a display hint.

#### Step 2

[Create a host](/documentation/current/en/manual/config/hosts/host) corresponding to a device.

![](/documentation/current/assets/en/manual/config/items/itemtypes/snmp/snmp_host.png)

Add an SNMP interface for the host:

  * Enter the IP address/DNS name and port number.
  * Select the _SNMP version_ from the dropdown.
  * Add interface credentials depending on the selected SNMP version: 
    * SNMPv1, v2 require only the community (usually 'public').
    * SNMPv3 requires more specific options (see below).
  * Specify the max repetition value (default: 10) for native SNMP bulk requests (GetBulkRequest-PDUs); only for `discovery[]` and `walk[]` items in SNMPv2 and v3. Note that setting this value too high may cause the SNMP agent check timeout.
  * Mark the _Use combined requests_ checkbox to allow combined processing of SNMP requests (not related to native SNMP bulk requests "walk" and "get").

_Context name_ | Enter context name to identify item on SNMP subnet.  
User macros are resolved in this field.  
---|---  
_Security name_ | Enter security name.  
User macros are resolved in this field.  
_Security level_ | Select security level:  
**noAuthNoPriv** \- no authentication nor privacy protocols are used  
**AuthNoPriv** \- authentication protocol is used, privacy protocol is not  
**AuthPriv** \- both authentication and privacy protocols are used  
_Authentication protocol_ | Select authentication protocol - _MD5_ , _SHA1_ ; with net-snmp 5.8 and newer _SHA224_ , _SHA256_ , _SHA384_ or _SHA512_.  
_Authentication passphrase_ | Enter authentication passphrase.  
User macros are resolved in this field.  
_Privacy protocol_ | Select privacy protocol - _DES_ , _AES128_ , _AES192_ , _AES256_ , _AES192C_ (Cisco) or _AES256C_ (Cisco).  
See notes about privacy protocol support  
_Privacy passphrase_ | Enter privacy passphrase.  
User macros are resolved in this field.  
  
In case of wrong SNMPv3 credentials (security name, authentication protocol/passphrase, privacy protocol):

  * Zabbix receives an ERROR from net-snmp, except for wrong _Privacy passphrase_ in which case Zabbix receives a TIMEOUT error from net-snmp.
  * SNMP interface availability will switch to red (unavailable).

Changes in _Authentication protocol_ , _Authentication passphrase_ , _Privacy protocol_ or _Privacy passphrase_ , made without changing the _Security name_ , are normally applied automatically when the corresponding SNMPv3 interface is updated in Zabbix. In cases where _Security name_ is also changed, all parameters will be updated immediately.

You can use one of the provided SNMP templates that will automatically add a set of items.Before using a template, verify that it is compatible with the host.

Click on _Add_ to save the host.

###### Privacy protocol support

Depending on your operating system and net-snmp configuration, some privacy protocols may not be available:

  * On some newer operating systems (for example, RHEL9) support of DES is dropped for the net-snmp package.

  * Encryption protocols AES192 and stronger are not supported out-of-the-box on the operating systems older then RHEL 8, CentOS 8, Oracle Linux 8, Debian 12, Ubuntu LTS 22.04, openSUSE Leap 15.5.

To check whether net-snmp library supports AES192+, use one of the following options:

  1. `net-snmp-config`:

    
    
    net-snmp-config --configure-options

Copy

✔ Copied

If the output contains `--enable-blumenthal-aes`, AES192+ is supported.

Note that net-snmp-config is part of the development package for SNMP (libsnmp-dev for Debian/Ubuntu, net-snmp-devel for CentOS/RHEL/OL/SUSE) and may not be installed by default.

  2. `snmpget`:

    
    
    snmpget -v 3 -x AES-256

Copy

✔ Copied

If the output contains `Invalid privacy protocol specified after -3x flag: AES-256`, AES192+ is not supported. If the output contains `No hostname specified.`, AES192+ is not supported.

If your net-snmp library does not support AES192 and higher protocols, recompile net-snmp with `--enable-blumenthal-aes` option, then recompile Zabbix server specifying the option `--with-net-snmp=/home/user/yourcustomnetsnmp/bin/net-snmp-config`.

#### Step 3

Create an item for monitoring.

So, now go back to Zabbix and click on _Items_ for the SNMP host you created earlier. Depending on whether you used a template or not when creating your host, you will have either a list of SNMP items associated with your host or just an empty list. We will work on the assumption that you are going to create the item yourself using the information you have just gathered using snmpwalk and snmpget, so click on _Create item_.

Fill in the required parameters in the new item form:

![](/documentation/current/assets/en/manual/config/items/itemtypes/snmp_item.png)

_Name_ | Enter the item name.  
---|---  
_Type_ | Select **SNMP agent** here.  
_Key_ | Enter the key as something meaningful.  
_Host interface_ | Make sure to select the SNMP interface, e.g. of your switch/router.  
_SNMP OID_ | Use one of the supported formats to enter OID value(s):  
  
**walk[OID1,OID2,...]** \- retrieve a subtree of values.  
For example: `walk[1.3.6.1.2.1.2.2.1.2,1.3.6.1.2.1.2.2.1.3]`.  
This option makes use of native SNMP bulk requests (GetBulkRequest-PDUs) asynchronously.  
The timeout settings for this item can be set in the [item configuration](/documentation/current/en/manual/config/items/item#configuration) form. Consider setting a low timeout value to avoid long delays if the device is unreachable, as up to 5 retries will be made if earlier ones time out or fail (e.g., 3-second timeout can result in 15-second wait time).  
You may use this as the master item, with dependent items that extract data from the master using preprocessing.  
It is possible to specify multiple OIDs in a single snmp walk, such as `walk[OID1,OID2,...]` to asynchronously process one OID at a time.  
If the bulk request returns no results then it is attempted to retrieve a single record without bulk request.  
MIB names are supported as parameters; thus `walk[1.3.6.1.2.1.2.2.1.2]` and `walk[ifDescr]` will return the same output.  
If several OIDs/MIBs are specified, i.e. `walk[ifDescr,ifType,ifPhysAddress]`, then the output is a concatenated list.  
GetBulk requests are used with SNMPv2 and v3 interfaces and GetNext for SNMPv1 interfaces; max repetitions for bulk requests are configured on the interface level.  
The max repetitions parameter affects bulk requests by determining the maximum number of OIDs returned in a single bulk response.  
A higher value results in larger bulk responses, reducing the number of transmissions required. However, not all devices might support very high values, which could cause issues.  
This item returns the output of the snmpwalk utility with -Oe -Ot -On parameters.  
You may use this item as a master item in [SNMP discovery](/documentation/current/en/manual/discovery/low_level_discovery/examples/snmp_oids_walk).  
  
**get[OID]** \- retrieve a _single_ value asynchronously.  
For example: `get[1.3.6.1.2.1.31.1.1.1.6.3]`  
The timeout settings for this item can be set in the [item configuration](/documentation/current/en/manual/config/items/item#configuration) form. Consider setting a low timeout value to avoid long delays if the device is unreachable, as up to 5 retries will be made if earlier ones time out or fail (e.g., 3-second timeout can result in 15-second wait time).  
  
**OID** \- (legacy) enter a single textual or numeric OID to retrieve a single value synchronously, optionally combined with other values.  
For example: `1.3.6.1.2.1.31.1.1.1.6.3`.  
For this option, the item check timeout will be equal to the value set in the server [configuration file](/documentation/current/en/manual/appendix/config/zabbix_server#timeout).  
  
It is **recommended** to use `walk[OID]` and `get[OID]` items for better performance. All `walk[OID]` and `get[OID]` items are executed asynchronously - it is not required to receive the response to one request before other checks are started. DNS resolving is asynchronous as well.  
The maximum concurrency of asynchronous checks is 1000 (defined by [MaxConcurrentChecksPerPoller](/documentation/current/en/manual/appendix/config/zabbix_server#maxconcurrentchecksperpoller)). The number of asynchronous SNMP pollers is defined by the [StartSNMPPollers](/documentation/current/en/manual/appendix/config/zabbix_server#startsnmppollers) parameter.  
  
Note that for network traffic statistics, returned by any of the methods, a _Change per second_ step must be added in the _Preprocessing_ tab; otherwise you will get the cumulative value from the SNMP device instead of the latest change.  
  
All mandatory input fields are marked with a red asterisk.

Now save the item and go to _Monitoring_ > _Latest data_ for your SNMP data.

#### Example 1

General example:

**OID** | 1.2.3.45.6.7.8.0 (or .1.2.3.45.6.7.8.0)  
---|---  
**Key** | <Unique string to be used as reference to triggers>  
For example, "my_param".  
  
Note that OID can be given in either numeric or string form. However, in some cases, string OID must be converted to numeric representation. Utility snmpget may be used for this purpose:
    
    
    snmpget -On localhost public enterprises.ucdavis.memory.memTotalSwap.0

Copy

✔ Copied

#### Example 2

Monitoring of uptime:

**OID** | MIB::sysUpTime.0  
---|---  
**Key** | router.uptime  
**Value type** | Float  
**Units** | uptime  
**Preprocessing step: Custom multiplier** | 0.01  
  
## Native SNMP bulk requests

The **walk[OID1,OID2,...]** item allows to use native SNMP functionality for bulk requests (GetBulkRequest-PDUs), available in SNMP versions 2/3.

A GetBulk request in SNMP executes multiple GetNext requests and returns the result in a single response. This may be used for regular SNMP items as well as for SNMP discovery to minimize network roundtrips.

The SNMP **walk[OID1,OID2,...]** item may be used as the master item that collects data in one request with dependent items that parse the response as needed using preprocessing.

Note that using native SNMP bulk requests is not related to the option of combining SNMP requests, which is Zabbix own way of combining multiple SNMP requests (see next section).

Up to five retries will occur for SNMP bulk items to avoid failure if one of the packets is lost. The timeout for SNMP items with `get` and `walk` (set in the [item configuration](/documentation/current/en/manual/config/items/item#configuration) form) is set for a whole session. Timeout is applied irrespective of whether data is retrieved completely; if data is received partially (for example, data is successfully collected for only one of multiple OIDs), then the item becomes unsupported with a message "Only partial data received". If the timeout is reached then a retry will occur, the timeout will be reset, and the last request will be resent allowing to continue the session from last request if a single packet is lost or arrived too late. Consider setting a low timeout value to avoid long delays if the device is unreachable, as up to 5 retries will be made if earlier ones time out or fail (e.g., 3-second timeout can result in 15-second wait time).

## Internal workings of combined processing

Zabbix server and proxy may query SNMP devices for multiple values in a single request. This affects several types of SNMP items:

  * regular SNMP items
  * SNMP items [with dynamic indexes](/documentation/current/en/manual/config/items/itemtypes/snmp/dynamicindex)
  * SNMP [low-level discovery rules](/documentation/current/en/manual/discovery/low_level_discovery/examples/snmp_oids_walk)

All SNMP items on a single interface with identical parameters are scheduled to be queried at the same time. The first two types of items are taken by pollers in batches of at most 128 items, whereas low-level discovery rules are processed individually, as before.

On the lower level, there are two kinds of operations performed for querying values: getting multiple specified objects and walking an OID tree.

For "getting", a GetRequest-PDU is used with at most 128 variable bindings. For "walking", a GetNextRequest-PDU is used for SNMPv1 and GetBulkRequest with "max-repetitions" field of at most 128 is used for SNMPv2 and SNMPv3.

Thus, the benefits of combined processing for each SNMP item type are outlined below:

  * regular SNMP items benefit from "getting" improvements;
  * SNMP items with dynamic indexes benefit from both "getting" and "walking" improvements: "getting" is used for index verification and "walking" for building the cache;
  * SNMP low-level discovery rules benefit from "walking" improvements.

However, there is a technical issue that not all devices are capable of returning 128 values per request. Some always return a proper response, but others either respond with a "tooBig(1)" error or do not respond at all once the potential response is over a certain limit.

In order to find an optimal number of objects to query for a given device, Zabbix uses the following strategy. It starts cautiously with querying 1 value in a request. If that is successful, it queries 2 values in a request. If that is successful again, it queries 3 values in a request and continues similarly by multiplying the number of queried objects by 1.5, resulting in the following sequence of request sizes: 1, 2, 3, 4, 6, 9, 13, 19, 28, 42, 63, 94, 128.

However, once a device refuses to give a proper response (for example, for 42 variables), Zabbix does two things.

First, for the current item batch it halves the number of objects in a single request and queries 21 variables. If the device is alive, then the query should work in the vast majority of cases, because 28 variables were known to work and 21 is significantly less than that. However, if that still fails, then Zabbix falls back to querying values one by one. If it still fails at this point, then the device is definitely not responding and request size is not an issue.

The second thing Zabbix does for subsequent item batches is it starts with the last successful number of variables (28 in our example) and continues incrementing request sizes by 1 until the limit is hit. For example, assuming the largest response size is 32 variables, the subsequent requests will be of sizes 29, 30, 31, 32, and 33. The last request will fail and Zabbix will never issue a request of size 33 again. From that point on, Zabbix will query at most 32 variables for this device.

If large queries fail with this number of variables, it can mean one of two things. The exact criteria that a device uses for limiting response size cannot be known, but we try to approximate that using the number of variables. So the first possibility is that this number of variables is around the device's actual response size limit in the general case: sometimes response is less than the limit, sometimes it is greater than that. The second possibility is that a UDP packet in either direction simply got lost. For these reasons, if Zabbix gets a failed query, it reduces the maximum number of variables to try to get deeper into the device's comfortable range, but only up to two times.

In the example above, if a query with 32 variables happens to fail, Zabbix will reduce the count to 31. If that happens to fail, too, Zabbix will reduce the count to 30. However, Zabbix will not reduce the count below 30, because it will assume that further failures are due to UDP packets getting lost, rather than the device's limit.

If, however, a device cannot handle combined requests properly for other reasons and the heuristic described above does not work, there is a "Use combined requests" setting for each interface that allows to disable combined requests for that device.

If combined requests cause partial or malformed responses that result in incorrect per-second (delta) calculations (for example, apparent spikes in interface counters), disable _Use combined requests_ for the affected interface to force separate per-item queries; this often prevents false spikes. Alternatively, consider using asynchronous `get[]` or `walk[]` items, which are executed asynchronously and are not subject to the per-interface _Use combined requests_ batching — they can be used instead of legacy synchronous OID checks to avoid combined-request related issues. Look for server/proxy log entries similar to the one shown in the Overview section to help identify affected devices.

Additionally, if the interface frequently becomes unavailable, it may be necessary to increase the `UnavailableDelay` parameter in the [Zabbix server](/documentation/current/en/manual/appendix/config/zabbix_server#unavailabledelay) or [Zabbix proxy](/documentation/current/en/manual/appendix/config/zabbix_proxy#unavailabledelay) configuration files to reduce the frequency of requests. Items may become unsupported if partial data is received during discovery or OID walks.