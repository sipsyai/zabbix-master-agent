---
title: Simple checks
source: https://www.zabbix.com/documentation/current/en/manual/config/items/itemtypes/simple_checks
downloaded: 2025-11-14 10:35:04
---

# 5 Simple checks

### Overview

Simple checks are normally used for remote agent-less checks of services.

Note that Zabbix agent is not needed for simple checks. Zabbix server/proxy is responsible for the processing of simple checks (making external connections, etc).

Examples of using simple checks:
    
    
    net.tcp.service[ftp,,155]
           net.tcp.service[http]
           net.tcp.service.perf[http,,8080]
           net.udp.service.perf[ntp]

Copy

✔ Copied

_User name_ and _Password_ fields (limited to 255 characters) in simple check item configuration are used for VMware monitoring items; ignored otherwise.

### Supported checks

The item keys are listed without optional parameters and additional information. Click on the item key to see the full details.

See also [VMware monitoring item keys](/documentation/current/en/manual/vm_monitoring/vmware_keys).

icmpping | The host accessibility by ICMP ping.  
---|---  
icmppingloss | The percentage of lost packets.  
icmppingretry | The host accessibility by ICMP ping with retries.  
icmppingsec | The ICMP ping response time.  
net.tcp.service | Checks if a service is running and accepting TCP connections.  
net.tcp.service.perf | Checks the performance of a TCP service.  
net.udp.service | Checks if a service is running and responding to UDP requests.  
net.udp.service.perf | Checks the performance of a UDP service.  
  
### Item key details

Parameters without angle brackets are mandatory. Parameters marked with angle brackets **<** **>** are optional.

##### icmpping[<target>,<packets>,<interval>,<size>,<timeout>,<options>]

  
The host accessibility by ICMP ping.  
Return value: _0_ \- ICMP ping fails; _1_ \- ICMP ping successful.

Parameters:

  * **target** \- the host IP or DNS name;
  * **packets** \- the number of packets;
  * **interval** \- the time between successive packets in milliseconds;
  * **size** \- the packet size in bytes;
  * **timeout** \- the timeout in milliseconds;
  * **options** \- used for allowing redirect: if empty (default value), redirected responses are treated as target host down; if set to _allow_redirect_ , redirected responses are treated as target host up.

See also the table of default values.

Example:
    
    
    icmpping[,4] #If at least one packet of the four is returned, the item will return 1.

Copy

✔ Copied

##### icmppingloss[<target>,<packets>,<interval>,<size>,<timeout>,<options>]

  
The percentage of lost packets.  
Return value: _Float_.

Parameters:

  * **target** \- the host IP or DNS name;
  * **packets** \- the number of packets;
  * **interval** \- the time between successive packets in milliseconds;
  * **size** \- the packet size in bytes;
  * **timeout** \- the timeout in milliseconds;
  * **options** \- used for allowing redirect: if empty (default value), redirected responses are treated as target host down; if set to _allow_redirect_ , redirected responses are treated as target host up.

See also the table of default values.

##### icmppingretry[<target>,<retries>,<backoff>,<size>,<timeout>,<options>]

  
The host accessibility by ICMP ping with retries. If the first packet succeeds then stop; if the packet fails then retry. This item is useful to reduce the number of packets sent over the network.  
Return value: _0_ \- ICMP ping fails; _1_ \- ICMP ping successful.

Parameters:

  * **target** \- the host IP or DNS name;
  * **retries** \- the number of times an attempt at pinging a target will be made, not including the first try (0 or greater; default 1);
  * **backoff** \- the number by which the wait time is multiplied on each successive request (1.0-5.0 range; default 1.0);
  * **size** \- the packet size in bytes;
  * **timeout** \- the timeout in milliseconds;
  * **options** \- used for allowing redirect: if empty (default value), redirected responses are treated as target host down; if set to _allow_redirect_ , redirected responses are treated as target host up.

See also the table of default values.

##### icmppingsec[<target>,<packets>,<interval>,<size>,<timeout>,<mode>,<options>]

  
The ICMP ping response time (in seconds).  
Return value: _Float_.

Parameters:

  * **target** \- the host IP or DNS name;
  * **packets** \- the number of packets;
  * **interval** \- the time between successive packets in milliseconds;
  * **size** \- the packet size in bytes;
  * **timeout** \- the timeout in milliseconds;
  * **mode** \- possible values: _min_ , _max_ , or _avg_ (default);
  * **options** \- used for allowing redirect: if empty (default value), redirected responses are treated as target host down; if set to _allow_redirect_ , redirected responses are treated as target host up.

Comments:

  * Packets which are lost or timed out are not used in the calculation;
  * If the host is not available (timeout reached), the item will return 0;
  * If the return value is less than 0.0001 seconds, the value will be set to 0.0001 seconds;
  * See also the table of default values.

##### net.tcp.service[service,<ip>,<port>]

  
Checks if a service is running and accepting TCP connections.  
Return value: _0_ \- the service is down; _1_ \- the service is running.

Parameters:

  * **service** \- possible values: _ssh_ , _ldap_ , _smtp_ , _ftp_ , _http_ , _pop_ , _nntp_ , _imap_ , _tcp_ , _https_ , _telnet_ (see [details](/documentation/current/en/manual/appendix/items/service_check_details));
  * **ip** \- the IP address or DNS name (by default the host IP/DNS is used);
  * **port** \- the port number (by default the standard service port number is used).

Comments:

  * Note that with _tcp_ service indicating the port is mandatory;
  * These checks may result in additional messages in system daemon logfiles (SMTP and SSH sessions being logged usually);
  * Checking of encrypted protocols (like IMAP on port 993 or POP on port 995) is currently not supported. As a workaround, please use `net.tcp.service[tcp,<ip>,port]` for checks like these.

Example:
    
    
    net.tcp.service[ftp,,45] #This item can be used to test the availability of FTP server on TCP port 45.

Copy

✔ Copied

If SELinux is running in enforced mode, custom TCP/UDP simple checks may be blocked by the policy. To verify and allow the new outgoing connection, review audit denials: with `grep denied /var/log/audit/audit.log`

##### net.tcp.service.perf[service,<ip>,<port>]

  
Checks the performance of a TCP service.  
Return value: _Float_ : _0.000000_ \- the service is down; _seconds_ \- the number of seconds spent while connecting to the service.

Parameters:

  * **service** \- possible values: _ssh_ , _ldap_ , _smtp_ , _ftp_ , _http_ , _pop_ , _nntp_ , _imap_ , _tcp_ , _https_ , _telnet_ (see [details](/documentation/current/en/manual/appendix/items/service_check_details));
  * **ip** \- the IP address or DNS name (by default the host IP/DNS is used);
  * **port** \- the port number (by default the standard service port number is used).

Comments:

  * Note that with _tcp_ service indicating the port is mandatory;
  * Checking of encrypted protocols (like IMAP on port 993 or POP on port 995) is currently not supported. As a workaround, please use `net.tcp.service[tcp,<ip>,port]` for checks like these.

Example:
    
    
    net.tcp.service.perf[ssh] #This item can be used to test the speed of initial response from SSH server.

Copy

✔ Copied

##### net.udp.service[service,<ip>,<port>]

  
Checks if a service is running and responding to UDP requests.  
Return value: _0_ \- the service is down; _1_ \- the service is running.

Parameters:

  * **service** \- possible values: _ntp_ (see [details](/documentation/current/en/manual/appendix/items/service_check_details));
  * **ip** \- the IP address or DNS name (by default the host IP/DNS is used);
  * **port** \- the port number (by default the standard service port number is used).

Example:
    
    
    net.udp.service[ntp,,45] #This item can be used to test the availability of NTP service on UDP port 45.

Copy

✔ Copied

##### net.udp.service.perf[service,<ip>,<port>]

  
Checks the performance of a UDP service.  
Return value: _Float_ : _0.000000_ \- the service is down; _seconds_ \- the number of seconds spent waiting for response from the service.

Parameters:

  * **service** \- possible values: _ntp_ (see [details](/documentation/current/en/manual/appendix/items/service_check_details));
  * **ip** \- the IP address or DNS name (by default the host IP/DNS is used);
  * **port** \- the port number (by default the standard service port number is used).

Example:
    
    
    net.udp.service.perf[ntp] #This item can be used to test the response time from NTP service.

Copy

✔ Copied

For SourceIP support in LDAP simple checks (e.g. `net.tcp.service[ldap]`), OpenLDAP version 2.6.1 or above is required.

##### Timeout processing

Zabbix will not process a simple check longer than the _Timeout_ seconds defined in the [item configuration](/documentation/current/en/manual/config/items/item#configuration) form. For [VMware items](/documentation/current/en/manual/vm_monitoring/vmware_keys) items, Zabbix will not process a simple check longer than the `Timeout` seconds defined in the Zabbix [server](/documentation/current/en/manual/appendix/config/zabbix_server#timeout) or [proxy](/documentation/current/en/manual/appendix/config/zabbix_proxy#timeout) configuration file. For icmpping* items, the timeout and retries values are specified directly in the item key and not influenced by the global `Timeout` parameter. Ensure these values are configured appropriately in the item key.

### ICMP pings

Zabbix uses an external utility **[fping](https://fping.org/)** to process ICMP pings (**icmpping** , **icmppingloss** , **icmppingretry** , **icmppingsec**).

##### Installation

fping is not included with Zabbix and needs to be installed separately:

  * Various Unix-based platforms have the fping package in their default repositories, but it is not pre-installed. In this case you can use the package manager to install fping.

  * Zabbix provides [fping packages](https://repo.zabbix.com/third-party/2024-10/) for RHEL and its derivatives. Please note that these packages are provided without official support.

  * fping can also be compiled [from source](https://github.com/schweikert/fping/blob/develop/README.md#installation).

##### Configuration

Specify fping location in the _[FpingLocation](/documentation/current/en/manual/appendix/config/zabbix_server#fpinglocation)_ parameter of Zabbix server/proxy configuration file (or _[Fping6Location](/documentation/current/en/manual/appendix/config/zabbix_server#fping6location)_ parameter for using IPv6 addresses).

fping should be executable by the user Zabbix server/proxy run as and this user should have sufficient rights.

See also: [Known issues](/documentation/current/en/manual/installation/known_issues#simple-checks) for processing simple checks with fping versions below 3.10.

##### Default values

Defaults, limits and description of values for ICMP check parameters:

|  |  |  | **fping** | **Zabbix** | **min** | **max**  
---|---|---|---|---|---|---|---  
packets | number | Number of request packets sent to a target | -C |  | 3 | 1 | 10000  
interval | milliseconds | Time to wait between successive packets to an individual target | -p | 1000 |  | 20 | unlimited  
size | bytes | Packet size in bytes  
56 bytes on x86, 68 bytes on x86_64 | -b | 56 or 68 |  | 24 | 65507  
timeout | milliseconds | **fping v3.x** \- timeout to wait after last packet sent, affected by _-C_ flag  
**fping v4.x** \- individual timeout for each packet | -t | **fping v3.x** \- 500  
**fping v4.x** and newer - inherited from _-p_ flag, but not more than 2000 |  | 50 | unlimited  
retries | number | Number of times an attempt at pinging a target will be made, not including the first try | -r | 3 | 1 | 0 | unlimited  
backoff factor | number | Number by which the wait time is multiplied on each successive request | -B | 1.5 | 1.0 | 1.0 | 5.0  
  
The defaults may differ slightly depending on the platform and version.

In addition, Zabbix uses fping options _-i interval ms_ (do not mix up with the item parameter _interval_ mentioned in the table above, which corresponds to fping option _-p_) and _-S source IP address_ (or _-I_ in older fping versions). These options are auto-detected by running checks with different option combinations. Zabbix tries to detect the minimal value in milliseconds that fping allows to use with _-i_ by trying 3 values: 0, 1 and 10. The value that first succeeds is then used for subsequent ICMP checks. This process is done by each [ICMP pinger](/documentation/current/en/manual/concepts/server#server-process-types-and-threads) process individually.

Auto-detected fping options are invalidated every hour and detected again on the next attempt to perform ICMP check. Set [DebugLevel](/documentation/current/en/manual/appendix/config/zabbix_server#debuglevel)>=4 in order to view details of this process in the server or proxy log file.

Zabbix writes IP addresses to be checked by any of the _icmpping*_ keys to a temporary file, which is then passed to fping. If items have different key parameters, only the ones with identical key parameters are written to a single file. All IP addresses written to the single file will be checked by fping in parallel, so Zabbix ICMP pinger process will spend fixed amount of time disregarding the number of IP addresses in the file.