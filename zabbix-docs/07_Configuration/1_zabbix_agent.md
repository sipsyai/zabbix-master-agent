---
title: Zabbix agent
source: https://www.zabbix.com/documentation/current/en/manual/config/items/itemtypes/zabbix_agent
downloaded: 2025-11-14 10:34:55
---

# 1 Zabbix agent

### Overview

This section provides details on the item keys that use communication with Zabbix agent for data gathering.

There are [passive and active](/documentation/current/en/manual/appendix/items/activepassive) agent checks. When configuring an item, you can select the required type:

  * _Zabbix agent_ \- for passive checks
  * _Zabbix agent (active)_ \- for active checks

Note that all item keys supported by Zabbix agent on Windows are also supported by the new generation Zabbix agent 2. See the [additional item keys](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent/zabbix_agent2) that you can use with the agent 2 only.

### Supported item keys

The item keys that you can use with Zabbix agent are listed below.

The item keys are listed without parameters and additional information. Click on the item key to see the full details.

kernel.maxfiles | The maximum number of opened files supported by OS. | Kernel  
---|---|---  
kernel.maxproc | The maximum number of processes supported by OS.  
kernel.openfiles | The number of currently open file descriptors.  
log | The monitoring of a log file. | [Log monitoring](log_items)  
log.count | The count of matched lines in a monitored log file.  
logrt | The monitoring of a log file that is rotated.  
logrt.count | The count of matched lines in a monitored log file that is rotated.  
modbus.get | Reads Modbus data. | Modbus  
net.dns | Checks the status of a DNS service. | Network  
net.dns.perf | Checks the performance of a DNS service.  
net.dns.record | Performs a DNS query.  
net.if.collisions | The number of out-of-window collisions.  
net.if.discovery | The list of network interfaces.  
net.if.in | The incoming traffic statistics on a network interface.  
net.if.out | The outgoing traffic statistics on a network interface.  
net.if.total | The sum of incoming and outgoing traffic statistics on a network interface.  
net.tcp.listen | Checks if this TCP port is in LISTEN state.  
net.tcp.port | Checks if it is possible to make a TCP connection to the specified port.  
net.tcp.service | Checks if a service is running and accepting TCP connections.  
net.tcp.service.perf | Checks the performance of a TCP service.  
net.tcp.socket.count | Returns the number of TCP sockets that match parameters.  
net.udp.listen | Checks if this UDP port is in LISTEN state.  
net.udp.service | Checks if a service is running and responding to UDP requests.  
net.udp.service.perf | Checks the performance of a UDP service.  
net.udp.socket.count | Returns the number of UDP sockets that match parameters.  
proc.cpu.util | The process CPU utilization percentage. | Processes  
proc.get | The list of OS processes and their parameters.  
proc.mem | The memory used by the process in bytes.  
proc.num | The number of processes.  
sensor | Hardware sensor reading. | Sensors  
system.boottime | The system boot time. | System  
system.cpu.discovery | The list of detected CPUs/CPU cores.  
system.cpu.intr | The device interrupts.  
system.cpu.load | The CPU load.  
system.cpu.num | The number of CPUs.  
system.cpu.switches | The count of context switches.  
system.cpu.util | The CPU utilization percentage.  
system.hostname | The system host name.  
system.hw.chassis | The chassis information.  
system.hw.cpu | The CPU information.  
system.hw.devices | The listing of PCI or USB devices.  
system.hw.macaddr | The listing of MAC addresses.  
system.localtime | The system time.  
system.run | Run the specified command on the host.  
system.stat | The system statistics.  
system.sw.arch | The software architecture information.  
system.sw.os | The operating system information.  
system.sw.os.get | Detailed information about the operating system (version, type, distribution name, minor and major version, etc).  
system.sw.packages | The listing of installed packages.  
system.sw.packages.get | A detailed listing of installed packages.  
system.swap.in | The swap-in (from device into memory) statistics.  
system.swap.out | The swap-out (from memory onto device) statistics.  
system.swap.size | The swap space size in bytes or in percentage from total.  
system.uname | Identification of the system.  
system.uptime | The system uptime in seconds.  
system.users.num | The number of users logged in.  
vfs.dev.discovery | The list of block devices and their type. | Virtual file systems  
vfs.dev.read | The disk read statistics.  
vfs.dev.write | The disk write statistics.  
vfs.dir.count | The directory entry count.  
vfs.dir.get | The directory entry list.  
vfs.dir.size | The directory size.  
vfs.file.cksum | The file checksum, calculated by the UNIX cksum algorithm.  
vfs.file.contents | Retrieving the contents of a file.  
vfs.file.exists | Checks if the file exists.  
vfs.file.get | Returns information about a file.  
vfs.file.md5sum | The MD5 checksum of file.  
vfs.file.owner | Retrieves the owner of a file.  
vfs.file.permissions | Returns a 4-digit string containing the octal number with UNIX permissions.  
vfs.file.regexp | Retrieve a string in the file.  
vfs.file.regmatch | Find a string in the file.  
vfs.file.size | The file size.  
vfs.file.time | The file time information.  
vfs.fs.discovery | The list of mounted filesystems with their type and mount options.  
vfs.fs.get | The list of mounted filesystems with their type, available disk space, inode statistics and mount options.  
vfs.fs.inode | The number or percentage of inodes.  
vfs.fs.size | The disk space in bytes or in percentage from total.  
vm.memory.size | The memory size in bytes or in percentage from total. | Virtual memory  
web.page.get | Get the content of a web page. | Web monitoring  
web.page.perf | The loading time of a full web page.  
web.page.regexp | Find a string on the web page.  
agent.hostmetadata | The agent host metadata. | Zabbix  
agent.hostname | The agent host name.  
agent.ping | The agent availability check.  
agent.variant | The variant of Zabbix agent (Zabbix agent or Zabbix agent 2).  
agent.version | The version of Zabbix agent.  
zabbix.stats | Returns a set of Zabbix server or proxy internal metrics remotely.  
zabbix.stats | Returns the number of monitored items in the queue which are delayed on Zabbix server or proxy remotely.  
  
#### Supported platforms

Except where specified differently in the item details, the agent items (and all parameters) are supported on:

  * **Linux**
  * **FreeBSD**
  * **Solaris**
  * **HP-UX**
  * **AIX**
  * **MacOS X**
  * **OpenBSD**
  * **NetBSD**

Many agent items are also supported on **Windows**. See the [Windows agent item](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent/win_keys#shared-items) page for details.

### Item key details

Parameters without angle brackets are mandatory. Parameters marked with angle brackets **<** **>** are optional.

##### kernel.maxfiles

  
The maximum number of opened files supported by OS.  
Return value: _Integer_.  
Supported platforms: Linux, FreeBSD, MacOS X, OpenBSD, NetBSD.

##### kernel.maxproc

  
The maximum number of processes supported by OS.  
Return value: _Integer_.  
Supported platforms: Linux 2.6 and later, FreeBSD, Solaris, MacOS X, OpenBSD, NetBSD.

##### kernel.openfiles

  
The number of currently open file descriptors.  
Return value: _Integer_.  
Supported platforms: Linux (the item may work on other UNIX-like platforms).

##### log[file,<regexp>,<encoding>,<maxlines>,<mode>,<output>,<maxdelay>,<options>,<persistent dir>]

  
The monitoring of a log file.  
Return value: _Log_.  
See supported platforms.

Parameters:

  * **file** \- the full path and name of a log file;  

  * **regexp** \- a regular [expression](/documentation/current/en/manual/regular_expressions#overview) describing the required pattern;  

  * **encoding** \- the code page [identifier](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#encoding-settings);  

  * **maxlines** \- the maximum number of new lines per second the agent will send to Zabbix server or proxy. This parameter overrides the value of 'MaxLinesPerSecond' in [zabbix_agentd.conf](/documentation/current/en/manual/appendix/config/zabbix_agentd);  

  * **mode** \- possible values: _all_ (default) or _skip_ \- skip processing of older data (affects only newly created items);  

  * **output** \- an optional output formatting template. The **\0** escape sequence is replaced with the matched part of text (from the first character where match begins until the character where match ends) while an **\N** (where N=1...9) escape sequence is replaced with Nth matched group (or an empty string if the N exceeds the number of captured groups);  

  * **maxdelay** \- the maximum delay in seconds. Type: float. Values: 0 - (default) never ignore log file lines; > 0.0 - ignore older lines in order to get the most recent lines analyzed within "maxdelay" seconds. Read the [maxdelay](log_items#using-maxdelay-parameter) notes before using it!  

  * **options** \- additional options:  
_mtime-noreread_ \- non-unique records, reread only if the file size changes (ignore modification time change). (This parameter is deprecated since 5.0.2, because now mtime is ignored.)  

  * **persistent dir** (only in zabbix_agentd on Unix systems; not supported in Zabbix agent 2) - the absolute pathname of directory where to store persistent files. See also additional notes on [persistent files](log_items#notes-on-persistent-files-for-log-items).

Comments:

  * The item must be configured as an [active check](/documentation/current/en/manual/appendix/items/activepassive#active-checks);
  * If the file is missing or permissions do not allow access, the item turns unsupported;
  * If `output` is left empty - the whole line containing the matched text is returned. Note that all global regular expression types except 'Result is TRUE' always return the whole matched line and the `output` parameter is ignored.
  * Content extraction using the `output` parameter takes place on the agent.

Examples:
    
    
    log[/var/log/syslog]
           log[/var/log/syslog,error]
           log[/home/zabbix/logs/logfile,,,100]

Copy

✔ Copied

Example of using the `output` parameter for extracting a number from log record:
    
    
    log[/app1/app.log,"task run [0-9.]+ sec, processed ([0-9]+) records, [0-9]+ errors",,,,\1] #this item will match a log record "2015-11-13 10:08:26 task run 6.08 sec, processed 6080 records, 0 errors" and send only '6080' to server. Because a numeric value is being sent, the "Type of information" for this item can be set to "Numeric (unsigned)" and the value can be used in graphs, triggers etc.

Copy

✔ Copied

Example of using the `output` parameter for rewriting a log record before sending to server:
    
    
    log[/app1/app.log,"([0-9 :-]+) task run ([0-9.]+) sec, processed ([0-9]+) records, ([0-9]+) errors",,,,"\1 RECORDS: \3, ERRORS: \4, DURATION: \2"] #this item will match a log record "2015-11-13 10:08:26 task run 6.08 sec, processed 6080 records, 0 errors" and send a modified record "2015-11-13 10:08:26 RECORDS: 6080, ERRORS: 0, DURATION: 6.08" to the server.

Copy

✔ Copied

##### log.count[file,<regexp>,<encoding>,<maxproclines>,<mode>,<maxdelay>,<options>,<persistent dir>]

  
The count of matched lines in a monitored log file.  
Return value: _Integer_.  
See supported platforms.

Parameters:

  * **file** \- the full path and name of log file;  

  * **regexp** \- a regular [expression](/documentation/current/en/manual/regular_expressions#overview) describing the required pattern;  

  * **encoding** \- the code page [identifier](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#encoding-settings);  

  * **maxproclines** \- the maximum number of new lines per second the agent will analyze (cannot exceed 10000). The default value is 10*'MaxLinesPerSecond' in [zabbix_agentd.conf](/documentation/current/en/manual/appendix/config/zabbix_agentd).  

  * **mode** \- possible values: _all_ (default) or _skip_ \- skip processing of older data (affects only newly created items).  

  * **maxdelay** \- the maximum delay in seconds. Type: float. Values: 0 - (default) never ignore log file lines; > 0.0 - ignore older lines in order to get the most recent lines analyzed within "maxdelay" seconds. Read the [maxdelay](log_items#using-maxdelay-parameter) notes before using it!  

  * **options** \- additional options:  
_mtime-noreread_ \- non-unique records, reread only if the file size changes (ignore modification time change). (This parameter is deprecated since 5.0.2, because now mtime is ignored.)  

  * **persistent dir** (only in zabbix_agentd on Unix systems; not supported in Zabbix agent 2) - the absolute pathname of directory where to store persistent files. See also additional notes on [persistent files](log_items#notes-on-persistent-files-for-log-items).

Comments:

  * The item must be configured as an [active check](/documentation/current/en/manual/appendix/items/activepassive#active-checks);
  * Matching lines are counted in the new lines since the last log check by the agent, and thus depend on the item update interval;
  * If the file is missing or permissions do not allow access, the item turns unsupported.

##### logrt[file regexp,<regexp>,<encoding>,<maxlines>,<mode>,<output>,<maxdelay>,<options>,<persistent dir>]

  
The monitoring of a log file that is rotated.  
Return value: _Log_.  
See supported platforms.

Parameters:

  * **file regexp** \- the absolute path to file, with the file name specified using a regular [expression](/documentation/current/en/manual/regular_expressions). Note that the regular expression applies only to the file name and does not need to match the entire name (e.g., /path/to/agent will match zabbix_agentd.log).  

  * **regexp** \- a regular [expression](/documentation/current/en/manual/regular_expressions#overview) describing the required content pattern.  

  * **encoding** \- the code page [identifier](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#encoding-settings).  

  * **maxlines** \- the maximum number of new lines per second the agent will send to Zabbix server or proxy. This parameter overrides the value of 'MaxLinesPerSecond' in [zabbix_agentd.conf](/documentation/current/en/manual/appendix/config/zabbix_agentd).  

  * **mode** \- possible values: _all_ (default) or _skip_ \- skip processing of older data (affects only newly created items).  

  * **output** \- an optional output formatting template. The **\0** escape sequence is replaced with the matched part of text (from the first character where match begins until the character where match ends) while an **\N** (where N=1...9) escape sequence is replaced with Nth matched group (or an empty string if the N exceeds the number of captured groups).  

  * **maxdelay** \- the maximum delay in seconds. Type: float. Values: 0 - (default) never ignore log file lines; > 0.0 - ignore older lines in order to get the most recent lines analyzed within "maxdelay" seconds. Read the [maxdelay](log_items#using-maxdelay-parameter) notes before using it!  

  * **options** \- the type of log file rotation and other options. Possible values:  
_rotate_ (default),  
_copytruncate_ \- note that _copytruncate_ cannot be used together with _maxdelay_. In this case _maxdelay_ must be 0 or not specified; see [copytruncate](log_items#notes-on-handling-copytruncate-log-file-rotation) notes,  
_mtime-reread_ \- non-unique records, reread if modification time or size changes (default),  
_mtime-noreread_ \- non-unique records, reread only if the size changes (ignore modification time change).  

  * **persistent dir** (only in zabbix_agentd on Unix systems; not supported in Zabbix agent 2) - the absolute pathname of directory where to store persistent files. See also additional notes on [persistent files](log_items#notes-on-persistent-files-for-log-items).

Comments:

  * The item must be configured as an [active check](/documentation/current/en/manual/appendix/items/activepassive#active-checks);
  * Log rotation is based on the last modification time of files;
  * Note that logrt is designed to work with one currently active log file, with several other matching inactive files rotated. If, for example, a directory has many active log files, a separate logrt item should be created for each one. Otherwise if one logrt item picks up too many files it may lead to exhausted memory and a crash of monitoring.
  * If `output` is left empty - the whole line containing the matched text is returned. Note that all global regular expression types except 'Result is TRUE' always return the whole matched line and the `output` parameter is ignored.
  * Content extraction using the `output` parameter takes place on the agent.
  * In the `file regexp` parameter, the log directory path and log file regular expression must be separated by the correct directory separator: 
    * on Windows, the separator must be a backslash (\\); forward slashes may be tolerated at other positions, except the one that separates the log directory path and the log file regular expression (see examples below).
    * on other systems, it must be a forward slash (/).

Examples for Windows:
    
    
    logrt["c:/dir1/dir2/dir3\filename.*\.log","pattern_to_match"] #this item will collect data from log files in "c:/dir1/dir2/dir3" where the file name starts with "filename" and ends with any extension matching ".log".
           logrt["//example.com/share/dir1/dir2/dir3\filename.*\.log","pattern_to_match"] #this item will collect data from log files in the network share "//example.com/share/dir1/dir2/dir3" where the file name starts with "filename" and ends with any extension matching ".log".

Copy

✔ Copied

Examples for other systems:
    
    
    logrt["/home/zabbix/logs/^logfile[0-9]{1,3}$",,,100] #this item will match a file like "logfile1" (will not match ".logfile1").
           logrt["/home/user/^logfile_.*_[0-9]{1,3}$","pattern_to_match","UTF-8",100] #this item will collect data from files such as "logfile_abc_1" or "logfile__001".

Copy

✔ Copied

Example of using the `output` parameter for extracting a number from log record:
    
    
    logrt[/app1/^test.*log$,"task run [0-9.]+ sec, processed ([0-9]+) records, [0-9]+ errors",,,,\1] #this item will match a log record "2015-11-13 10:08:26 task run 6.08 sec, processed 6080 records, 0 errors" and send only '6080' to server. Because a numeric value is being sent, the "Type of information" for this item can be set to "Numeric (unsigned)" and the value can be used in graphs, triggers etc.

Copy

✔ Copied

Example of using the `output` parameter for rewriting a log record before sending to server:
    
    
    logrt[/app1/^test.*log$,"([0-9 :-]+) task run ([0-9.]+) sec, processed ([0-9]+) records, ([0-9]+) errors",,,,"\1 RECORDS: \3, ERRORS: \4, DURATION: \2"] #this item will match a log record "2015-11-13 10:08:26 task run 6.08 sec, processed 6080 records, 0 errors" and send a modified record "2015-11-13 10:08:26 RECORDS: 6080, ERRORS: 0, DURATION: 6.08" to server.

Copy

✔ Copied

##### logrt.count[file regexp,<regexp>,<encoding>,<maxproclines>,<mode>,<maxdelay>,<options>,<persistent dir>]

  
The count of matched lines in a monitored log file that is rotated.  
Return value: _Integer_.  
See supported platforms.

Parameters:

  * **file regexp** \- the absolute path to file, with the file name specified using a regular [expression](/documentation/current/en/manual/regular_expressions). Note that the regular expression applies only to the file name and does not need to match the entire name (e.g., /path/to/agent will match zabbix_agentd.log).  

  * **regexp** \- a regular [expression](/documentation/current/en/manual/regular_expressions#overview) describing the required pattern.  

  * **encoding** \- the code page [identifier](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#encoding-settings).  

  * **maxproclines** \- the maximum number of new lines per second the agent will analyze (cannot exceed 10000). The default value is 10*'MaxLinesPerSecond' in [zabbix_agentd.conf](/documentation/current/en/manual/appendix/config/zabbix_agentd).  

  * **mode** \- possible values: _all_ (default) or _skip_ \- skip processing of older data (affects only newly created items).  

  * **maxdelay** \- the maximum delay in seconds. Type: float. Values: 0 - (default) never ignore log file lines; > 0.0 - ignore older lines in order to get the most recent lines analyzed within "maxdelay" seconds. Read the [maxdelay](log_items#using-maxdelay-parameter) notes before using it!  

  * **options** \- the type of log file rotation and other options. Possible values:  
_rotate_ (default),  
_copytruncate_ \- note that _copytruncate_ cannot be used together with _maxdelay_. In this case _maxdelay_ must be 0 or not specified; see [copytruncate](log_items#notes-on-handling-copytruncate-log-file-rotation) notes,  
_mtime-reread_ \- non-unique records, reread if modification time or size changes (default),  
_mtime-noreread_ \- non-unique records, reread only if the size changes (ignore modification time change).  

  * **persistent dir** (only in zabbix_agentd on Unix systems; not supported in Zabbix agent 2) - the absolute pathname of directory where to store persistent files. See also additional notes on [persistent files](log_items#notes-on-persistent-files-for-log-items).

Comments:

  * The item must be configured as an [active check](/documentation/current/en/manual/appendix/items/activepassive#active-checks);
  * Matching lines are counted in the new lines since the last log check by the agent, and thus depend on the item update interval;
  * Log rotation is based on the last modification time of files;
  * In the `file regexp` parameter, the log directory path and log file regular expression must be separated by the correct directory separator: 
    * on Windows, the separator must be a backslash (\\); forward slashes may be tolerated at other positions, except the one that separates the log directory path and the log file regular expression (see examples below).
    * on other systems, it must be a forward slash (/).

Examples for Windows:
    
    
    logrt.count["c:/dir1/dir2/dir3\filename.*\.log","pattern_to_match"] #this item will count the number of matches for the pattern "pattern_to_match" in log files located in "c:/dir1/dir2/dir3".
           logrt.count["//example.com/share/dir1/dir2/dir3\filename.*\.log","pattern_to_match"] #this item will count the number of matches for the pattern "pattern_to_match" in log files on the network share "//example.com/share/dir1/dir2/dir3".

Copy

✔ Copied

Examples for other systems:
    
    
    logrt.count["/home/zabbix/logs/^logfile[0-9]{1,3}$",,,100] #this item will count the number of matches for the pattern "^logfile[0-9]{1,3}$" in log files in the "/home/zabbix/logs" directory.
           logrt.count["/home/user/^logfile_.*_[0-9]{1,3}$","pattern_to_match","UTF-8",100] #this item will count the number of occurrences of the pattern "pattern_to_match" in log files located in "/home/user".

Copy

✔ Copied

##### modbus.get[endpoint,<slave id>,<function>,<address>,<count>,<type>,<endianness>,<offset>]

  
Reads Modbus data.  
Return value: _JSON string_.  
Supported platforms: Linux.

Parameters:

  * **endpoint** \- the endpoint defined as `protocol://connection_string`;  

  * **slave id** \- the slave ID;  

  * **function** \- the Modbus function;  

  * **address** \- the address of first registry, coil or input;  

  * **count** \- the number of records to read;  

  * **type** \- the type of data;  

  * **endianness** \- the endianness configuration;  

  * **offset** \- the number of registers, starting from 'address', the results of which will be discarded.

See a [detailed description](/documentation/current/en/manual/appendix/items/modbus) of parameters.

##### net.dns[<ip>,name,<type>,<timeout>,<count>,<protocol>]

  
Checks the status of a DNS service.  
Return values: 0 - DNS resolution failed (DNS server did not respond or returned an error); 1 - DNS resolution succeeded.  
See supported platforms.

Parameters:

  * **ip** (ignored on Windows unless using Zabbix agent 2) - the IP address of DNS server (leave empty for the default DNS server);
  * **name** \- the DNS name to query;
  * **type** \- the record type to be queried (default is _SOA_);
  * **timeout** (ignored on Windows unless using Zabbix agent 2) - the timeout for the request in seconds (default is 1 second);
  * **count** (ignored on Windows unless using Zabbix agent 2) - the number of tries for the request (default is 2);
  * **protocol** \- the protocol used to perform DNS queries: _udp_ (default) or _tcp_.

Comments:

  * The possible values for `type` are: _ANY_ , _A_ , _NS_ , _CNAME_ , _MB_ , _MG_ , _MR_ , _PTR_ , _MD_ , _MF_ , _MX_ , _SOA_ , _NULL_ , _WKS_ (not supported for Zabbix agent on Windows, Zabbix agent 2 on all OS), _HINFO_ , _MINFO_ , _TXT_ , _SRV_
  * For reverse DNS lookups (when `type` is set to _PTR_), you can provide the DNS name in both reversed and non-reversed format (see examples below). Note that when PTR record is requested, the DNS name is actually an IP address.
  * Internationalized domain names are not supported, please use IDNA encoded names instead.

Examples:
    
    
    net.dns[198.51.100.1,example.com,MX,2,1]
           
           net.dns[,198.51.100.1,PTR]
           net.dns[,1.100.51.198.in-addr.arpa,PTR]
           
           net.dns[,2a00:1450:400f:800::200e,PTR]
           net.dns[,e.0.0.2.0.0.0.0.0.0.0.0.0.0.0.0.0.0.8.0.f.0.0.4.0.5.4.1.0.0.a.2.ip6.arpa,PTR]

Copy

✔ Copied

##### net.dns.perf[<ip>,name,<type>,<timeout>,<count>,<protocol>]

  
Checks the performance of a DNS service.  
Return value: _Float_ (0 - service is down; seconds - the number of seconds spent waiting for a response from the service).  
See supported platforms.

Parameters:

  * **ip** (ignored on Windows unless using Zabbix agent 2) - the IP address of DNS server (leave empty for the default DNS server);
  * **name** \- the DNS name to query;
  * **type** \- the record type to be queried (default is _SOA_);
  * **timeout** (ignored on Windows unless using Zabbix agent 2) - the timeout for the request in seconds (default is 1 second);
  * **count** (ignored on Windows unless using Zabbix agent 2) - the number of tries for the request (default is 2);
  * **protocol** \- the protocol used to perform DNS queries: _udp_ (default) or _tcp_.

Comments:

  * The possible values for `type` are:  
_ANY_ , _A_ , _NS_ , _CNAME_ , _MB_ , _MG_ , _MR_ , _PTR_ , _MD_ , _MF_ , _MX_ , _SOA_ , _NULL_ , _WKS_ (not supported for Zabbix agent on Windows, Zabbix agent 2 on all OS), _HINFO_ , _MINFO_ , _TXT_ , _SRV_
  * For reverse DNS lookups (when `type` is set to _PTR_), you can provide the DNS name in both reversed and non-reversed format (see examples below). Note that when PTR record is requested, the DNS name is actually an IP address.
  * Internationalized domain names are not supported, please use IDNA encoded names instead.
  * The item returns a response time instead of `0` when the DNS server responds with an error code (for example, `NXDOMAIN` or `SERVFAIL`).

Examples:
    
    
    net.dns.perf[198.51.100.1,example.com,MX,2,1]
           
           net.dns.perf[,198.51.100.1,PTR]
           net.dns.perf[,1.100.51.198.in-addr.arpa,PTR]
           
           net.dns.perf[,2a00:1450:400f:800::200e,PTR]
           net.dns.perf[,e.0.0.2.0.0.0.0.0.0.0.0.0.0.0.0.0.0.8.0.f.0.0.4.0.5.4.1.0.0.a.2.ip6.arpa,PTR]

Copy

✔ Copied

##### net.dns.record[<ip>,name,<type>,<timeout>,<count>,<protocol>]

  
Performs a DNS query.  

Zabbix agent 2 also provides [net.dns.get](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent/zabbix_agent2#net.dns.get), which offers additional features such as more record types and greater control over DNS monitoring. Return value: a character string with the required type of information.  
See supported platforms.

Parameters:

  * **ip** (ignored on Windows unless using Zabbix agent 2) - the IP address of DNS server (leave empty for the default DNS server);
  * **name** \- the DNS name to query;
  * **type** \- the record type to be queried (default is _SOA_);
  * **timeout** (ignored on Windows unless using Zabbix agent 2) - the timeout for the request in seconds (default is 1 second);
  * **count** (ignored on Windows unless using Zabbix agent 2) - the number of tries for the request (default is 2);
  * **protocol** \- the protocol used to perform DNS queries: _udp_ (default) or _tcp_.

Comments:

  * The possible values for `type` are:  
_ANY_ , _A_ , _NS_ , _CNAME_ , _MB_ , _MG_ , _MR_ , _PTR_ , _MD_ , _MF_ , _MX_ , _SOA_ , _NULL_ , _WKS_ (not supported for Zabbix agent on Windows, Zabbix agent 2 on all OS), _HINFO_ , _MINFO_ , _TXT_ , _SRV_
  * For reverse DNS lookups (when `type` is set to _PTR_), you can provide the DNS name in reversed or non-reversed format (see examples below). Note that when PTR record is requested, the DNS name is actually an IP address.
  * Internationalized domain names are not supported, please use IDNA encoded names instead.

Examples:
    
    
    net.dns.record[198.51.100.1,example.com,MX,2,1]
           
           net.dns.record[,198.51.100.1,PTR]
           net.dns.record[,1.100.51.198.in-addr.arpa,PTR]
           
           net.dns.record[,2a00:1450:400f:800::200e,PTR]
           net.dns.record[,e.0.0.2.0.0.0.0.0.0.0.0.0.0.0.0.0.0.8.0.f.0.0.4.0.5.4.1.0.0.a.2.ip6.arpa,PTR]

Copy

✔ Copied

##### net.if.collisions[if]

  
The number of out-of-window collisions.  
Return value: _Integer_.  
Supported platforms: Linux, FreeBSD, Solaris, AIX, MacOS X, OpenBSD, NetBSD. Root privileges are required on NetBSD.

Parameter:

  * **if** \- network interface name

##### net.if.discovery

  
The list of network interfaces. Used for low-level discovery.  
Return value: _JSON string_.  
Supported platforms: Linux, FreeBSD, Solaris, HP-UX, AIX, OpenBSD, NetBSD.

##### net.if.in[if,<mode>]

  
The incoming traffic statistics on a network interface.  
Return value: _Integer_.  
Supported platforms: Linux, FreeBSD, Solaris**5** , HP-UX, AIX, MacOS X, OpenBSD, NetBSD. Root privileges are required on NetBSD.

Parameters:

  * **if** \- network interface name (Unix); network interface full description or IPv4 address; or, if in braces, network interface GUID (Windows);
  * **mode** \- possible values:  
_bytes_ \- number of bytes (default)  
_packets_ \- number of packets  
 _errors_ \- number of errors  
 _dropped_ \- number of dropped packets  
 _overruns (fifo)_ \- the number of FIFO buffer errors  
 _frame_ \- the number of packet framing errors  
 _compressed_ \- the number of compressed packets received by the device driver  
 _multicast_ \- the number of multicast frames received by the device driver

Comments:

  * You may use this key with the _Change per second_ preprocessing step in order to get the bytes-per-second statistics;
  * The _dropped_ mode is supported only on Linux, FreeBSD, HP-UX, MacOS X, OpenBSD, NetBSD;
  * The _overruns_ , _frame_ , _compressed_ , _multicast_ modes are supported only on Linux;
  * On HP-UX this item does not provide details on loopback interfaces (e.g. lo0).

Examples:
    
    
    net.if.in[eth0]
           net.if.in[eth0,errors]

Copy

✔ Copied

##### net.if.out[if,<mode>]

  
The outgoing traffic statistics on a network interface.  
Return value: _Integer_.  
Supported platforms: Linux, FreeBSD, Solaris**5** , HP-UX, AIX, MacOS X, OpenBSD, NetBSD. Root privileges are required on NetBSD.

Parameters:

  * **if** \- network interface name (Unix); network interface full description or IPv4 address; or, if in braces, network interface GUID (Windows);
  * **mode** \- possible values:  
_bytes_ \- number of bytes (default)  
_packets_ \- number of packets  
 _errors_ \- number of errors  
 _dropped_ \- number of dropped packets  
 _overruns (fifo)_ \- the number of FIFO buffer errors  
 _collisions (colls)_ \- the number of collisions detected on the interface  
 _carrier_ \- the number of carrier losses detected by the device driver  
 _compressed_ \- the number of compressed packets transmitted by the device driver

Comments:

  * You may use this key with the _Change per second_ preprocessing step in order to get the bytes-per-second statistics;
  * The _dropped_ mode is supported only on Linux, HP-UX;
  * The _overruns_ , _collision_ , _carrier_ , _compressed_ modes are supported only on Linux;
  * On HP-UX this item does not provide details on loopback interfaces (e.g. lo0).

Examples:
    
    
    net.if.out[eth0]
           net.if.out[eth0,errors]

Copy

✔ Copied

##### net.if.total[if,<mode>]

  
The sum of incoming and outgoing traffic statistics on a network interface.  
Return value: _Integer_.  
Supported platforms: Linux, FreeBSD, Solaris**5** , HP-UX, AIX, MacOS X, OpenBSD, NetBSD. Root privileges are required on NetBSD.

Parameters:

  * **if** \- network interface name (Unix); network interface full description or IPv4 address; or, if in braces, network interface GUID (Windows);
  * **mode** \- possible values:  
_bytes_ \- number of bytes (default)  
_packets_ \- number of packets  
 _errors_ \- number of errors  
 _dropped_ \- number of dropped packets  
 _overruns (fifo)_ \- the number of FIFO buffer errors  
 _collisions (colls)_ \- the number of collisions detected on the interface  
 _compressed_ \- the number of compressed packets transmitted or received by the device driver

Comments:

  * You may use this key with the _Change per second_ preprocessing step in order to get the bytes-per-second statistics;
  * The _dropped_ mode is supported only on Linux, HP-UX. Dropped packets are supported only if both `net.if.in` and `net.if.out` work for dropped packets on your platform.
  * The _overruns_ , _collision_ , _compressed_ modes are supported only on Linux;
  * On HP-UX this item does not provide details on loopback interfaces (e.g. lo0).

Examples:
    
    
    net.if.total[eth0]
           net.if.total[eth0,errors]

Copy

✔ Copied

##### net.tcp.listen[port]

  
Checks if this TCP port is in LISTEN state.  
Return values: 0 - it is not in LISTEN state; 1 - it is in LISTEN state.  
Supported platforms: Linux, FreeBSD, Solaris, MacOS X.

Parameter:

  * **port** \- TCP port number

On Linux kernels 2.6.14 and above, the information about listening TCP sockets is obtained from the kernel's NETLINK interface, if possible. Otherwise, the information is retrieved from /proc/net/tcp and /roc/net/tcp6 files.

Example:
    
    
    net.tcp.listen[80]

Copy

✔ Copied

##### net.tcp.port[<ip>,port]

  
Checks if it is possible to make a TCP connection to the specified port.  
Return values: 0 - cannot connect; 1 - can connect.  
See supported platforms.

Parameters:

  * **ip** \- the IP address or DNS name (default is 127.0.0.1);
  * **port** \- the port number.

Comments:

  * For simple TCP performance testing use `net.tcp.service.perf[tcp,<ip>,<port>]`;
  * These checks may result in additional messages in system daemon logfiles (SMTP and SSH sessions being logged usually).

Example:
    
    
    net.tcp.port[,80] #this item can be used to test the web server availability running on port 80

Copy

✔ Copied

##### net.tcp.service[service,<ip>,<port>]

  
Checks if a service is running and accepting TCP connections.  
Return values: 0 - service is down; 1 - service is running.  
See supported platforms.

Parameters:

  * **service** \- _ssh_ , _ldap_ , _smtp_ , _ftp_ , _http_ , _pop_ , _nntp_ , _imap_ , _tcp_ , _https_ , or _telnet_ (see [details](/documentation/current/en/manual/appendix/items/service_check_details));
  * **ip** \- the IP address or DNS name (default is 127.0.0.1);
  * **port** \- the port number (by default the standard service port number is used).

Comments:

  * These checks may result in additional messages in system daemon logfiles (SMTP and SSH sessions being logged usually);
  * Checking of encrypted protocols (like IMAP on port 993 or POP on port 995) is currently not supported. As a workaround, please use `net.tcp.port[]` for checks like these.
  * Checking of LDAP and HTTPS on Windows is only supported by Zabbix agent 2;
  * The telnet check looks for a login prompt (':' at the end).

Example:
    
    
    net.tcp.service[ftp,,45] #this item can be used to test the availability of FTP server on TCP port 45

Copy

✔ Copied

##### net.tcp.service.perf[service,<ip>,<port>]

  
Checks the performance of a TCP service.  
Return values: _Float_ (0 - service is down; seconds - the number of seconds spent waiting for a response from the service).  
See supported platforms.

Parameters:

  * **service** \- _ssh_ , _ldap_ , _smtp_ , _ftp_ , _http_ , _pop_ , _nntp_ , _imap_ , _tcp_ , _https_ , or _telnet_ (see [details](/documentation/current/en/manual/appendix/items/service_check_details));
  * **ip** \- the IP address or DNS name (default is 127.0.0.1);
  * **port** \- the port number (by default the standard service port number is used).

Comments:

  * Checking of encrypted protocols (like IMAP on port 993 or POP on port 995) is currently not supported. As a workaround, please use `net.tcp.service.perf[tcp,<ip>,<port>]` for checks like these.
  * The telnet check looks for a login prompt (':' at the end).

Example:
    
    
    net.tcp.service.perf[ssh] #this item can be used to test the speed of initial response from the SSH server

Copy

✔ Copied

##### net.tcp.socket.count[<laddr>,<lport>,<raddr>,<rport>,<state>]

  
Returns the number of TCP sockets that match parameters.  
Return value: _Integer_.  
Supported platforms: Linux.

Parameters:

  * **laddr** \- the local IPv4/6 address or CIDR subnet;
  * **lport** \- the local port number or service name;
  * **raddr** \- the remote IPv4/6 address or CIDR subnet;
  * **rport** \- the remote port number or service name;
  * **state** \- the connection state (_established_ , _syn_sent_ , _syn_recv_ , _fin_wait1_ , _fin_wait2_ , _time_wait_ , _close_ , _close_wait_ , _last_ack_ , _listen_ , _closing_).

Example:
    
    
    net.tcp.socket.count[,80,,,established] #the number of connections to local TCP port 80 in the established state

Copy

✔ Copied

##### net.udp.listen[port]

  
Checks if this UDP port is in LISTEN state.  
Return values: 0 - it is not in LISTEN state; 1 - it is in LISTEN state.  
Supported platforms: Linux, FreeBSD, Solaris, MacOS X.

Parameter:

  * **port** \- UDP port number

Example:
    
    
    net.udp.listen[68]

Copy

✔ Copied

##### net.udp.service[service,<ip>,<port>]

  
Checks if a service is running and responding to UDP requests.  
Return values: 0 - service is down; 1 - service is running.  
See supported platforms.

Parameters:

  * **service** \- _ntp_ (see [details](/documentation/current/en/manual/appendix/items/service_check_details));
  * **ip** \- the IP address or DNS name (default is 127.0.0.1);
  * **port** \- the port number (by default the standard service port number is used).

Example:
    
    
    net.udp.service[ntp,,45] #this item can be used to test the availability of NTP service on UDP port 45

Copy

✔ Copied

##### net.udp.service.perf[service,<ip>,<port>]

  
Checks the performance of a UDP service.  
Return values: _Float_ (0 - service is down; seconds - the number of seconds spent waiting for a response from the service).  
See supported platforms.

Parameters:

  * **service** \- _ntp_ (see [details](/documentation/current/en/manual/appendix/items/service_check_details));
  * **ip** \- the IP address or DNS name (default is 127.0.0.1);
  * **port** \- the port number (by default the standard service port number is used).

Example:
    
    
    net.udp.service.perf[ntp] #this item can be used to test response time from NTP service

Copy

✔ Copied

##### net.udp.socket.count[<laddr>,<lport>,<raddr>,<rport>,<state>]

  
Returns the number of UDP sockets that match parameters.  
Return value: _Integer_.  
Supported platforms: Linux.

Parameters:

  * **laddr** \- the local IPv4/6 address or CIDR subnet;
  * **lport** \- the local port number or service name;
  * **raddr** \- the remote IPv4/6 address or CIDR subnet;
  * **rport** \- the remote port number or service name;
  * **state** \- the connection state (_established_ , _unconn_).

Example:
    
    
    net.udp.socket.count[,,,,established] #returns the number of UDP sockets in the connected state

Copy

✔ Copied

##### proc.cpu.util[<name>,<user>,<type>,<cmdline>,<mode>,<zone>]

  
The process CPU utilization percentage.  
Return value: _Float_.  
Supported platforms: Linux, Solaris**6**.

Parameters:

  * **name** \- the process name (default is _all processes_);
  * **user** \- the user name (default is _all users_);
  * **type** \- the CPU utilization type: _total_ (default), _user_ , or _system_ ;
  * **cmdline** \- filter by command line (it is a regular [expression](/documentation/current/en/manual/regular_expressions#overview));
  * **mode** \- the data gathering mode: _avg1_ (default), _avg5_ , or _avg15_ ;
  * **zone** \- the target zone: _current_ (default) or _all_. This parameter is supported on Solaris only.

Comments:

  * The returned value is based on a single CPU core utilization percentage. For example, the CPU utilization of a process fully using two cores is 200%.
  * The process CPU utilization data is gathered by a collector which supports the maximum of 1024 unique (by name, user and command line) queries. Queries not accessed during the last 24 hours are removed from the collector.
  * When setting the `zone` parameter to _current_ (or default) in case the agent has been compiled on a Solaris without zone support, but running on a newer Solaris where zones are supported, then the agent will return NOTSUPPORTED (the agent cannot limit results to only the current zone). However, _all_ is supported in this case.

Examples:
    
    
    proc.cpu.util[,root] #CPU utilization of all processes running under the "root" user
           proc.cpu.util[zabbix_server,zabbix] #CPU utilization of all zabbix_server processes running under the zabbix user

Copy

✔ Copied

##### proc.get[<name>,<user>,<cmdline>,<mode>]

  
The list of OS processes and their parameters. Can be used for low-level discovery.  
Return value: _JSON string_.  
Supported platforms: Linux, FreeBSD, Windows, OpenBSD, NetBSD.

Parameters:

  * **name** \- the process name (default _all processes_);
  * **user** \- the user name (default _all users_);
  * **cmdline** \- filter by command line (it is a regular [expression](/documentation/current/en/manual/regular_expressions#overview)). This parameter is not supported for Windows; on other platforms it is not supported if mode is set to 'summary'.
  * **mode** \- possible values:  
_process_ (default), _thread_ (not supported for NetBSD), _summary_. See a list of [process parameters](/documentation/current/en/manual/appendix/items/proc_get) returned for each mode and OS.

Comments:

  * If a value cannot be retrieved, for example, because of an error (process already died, lack of permissions, system call failure), `-1` will be returned;
  * See [notes](/documentation/current/en/manual/appendix/items/proc_mem_num_notes) on selecting processes with `name` and `cmdline` parameters (Linux-specific).

Examples:
    
    
    proc.get[zabbix_server,zabbix,,process] #list of all zabbix_server processes running under the zabbix user, returns one entry per PID
           proc.get[java,,,thread] #list of all Java processes, returns one entry per thread
           proc.get[,zabbix,,summary] #combined data for processes of each type running under the zabbix user, returns one entry per process name

Copy

✔ Copied

##### proc.mem[<name>,<user>,<mode>,<cmdline>,<memtype>]

  
The memory used by the process in bytes.  
Return value: _Integer_ \- with `mode` as _max_ , _min_ , _sum_ ; _Float_ \- with `mode` as _avg_  
Supported platforms: Linux, FreeBSD, Solaris, AIX, OpenBSD, NetBSD.

Parameters:

  * **name** \- the process name (default is _all processes_);
  * **user** \- the user name (default is _all users_);
  * **mode** \- possible values: _avg_ , _max_ , _min_ , or _sum_ (default);
  * **cmdline** \- filter by command line (it is a regular [expression](/documentation/current/en/manual/regular_expressions#overview));
  * **memtype** \- the [type of memory](/documentation/current/en/manual/appendix/items/proc_mem_notes) used by process

Comments:

  * The `memtype` parameter is supported only on Linux, FreeBSD, Solaris**6** , AIX;
  * When several processes use shared memory, the sum of memory used by processes may result in large, unrealistic values.  
  
See [notes](/documentation/current/en/manual/appendix/items/proc_mem_num_notes) on selecting processes with `name` and `cmdline` parameters (Linux-specific).  
  
When this item is invoked from the command line and contains a command line parameter (e.g. using the agent test mode: `zabbix_agentd -t proc.mem[,,,apache2]`), one extra process will be counted, as the agent will count itself.

Examples:
    
    
    proc.mem[,root] #the memory used by all processes running under the "root" user
           proc.mem[zabbix_server,zabbix] #the memory used by all zabbix_server processes running under the zabbix user
           proc.mem[,oracle,max,oracleZABBIX] #the memory used by the most memory-hungry process running under Oracle having oracleZABBIX in its command line

Copy

✔ Copied

##### proc.num[<name>,<user>,<state>,<cmdline>,<zone>]

  
The number of processes.  
Return value: _Integer_.  
Supported platforms: Linux, FreeBSD, Solaris**6** , HP-UX, AIX, OpenBSD, NetBSD.

Parameters:

  * **name** \- the process name (default is _all processes_);
  * **user** \- the user name (default is _all users_);
  * **state** \- possible values:  
_all_ (default),  
_disk_ \- uninterruptible sleep,  
_run_ \- running,  
_sleep_ \- interruptible sleep,  
_trace_ \- stopped,  
_zomb_ \- zombie;
  * **cmdline** \- filter by command line (it is a regular [expression](/documentation/current/en/manual/regular_expressions#overview));
  * **zone** \- the target zone: _current_ (default), or _all_. This parameter is supported on Solaris only.

Comments:

  * The _disk_ and _trace_ state parameters are supported only on Linux, FreeBSD, OpenBSD, NetBSD;
  * When this item is invoked from the command line and contains a command line parameter (e.g. using the agent test mode: `zabbix_agentd -t proc.num[,,,apache2]`), one extra process will be counted, as the agent will count itself;
  * When setting the `zone` parameter to _current_ (or default) in case the agent has been compiled on a Solaris without zone support, but running on a newer Solaris where zones are supported, then the agent will return NOTSUPPORTED (the agent cannot limit results to only the current zone). However, _all_ is supported in this case.
  * See [notes](/documentation/current/en/manual/appendix/items/proc_mem_num_notes) on selecting processes with `name` and `cmdline` parameters (Linux-specific).

Examples:
    
    
    proc.num[,mysql] #the number of processes running under the mysql user
           proc.num[apache2,www-data] #the number of apache2 processes running under the www-data user
           proc.num[,oracle,sleep,oracleZABBIX] #the number of processes in sleep state running under Oracle having oracleZABBIX in its command line

Copy

✔ Copied

##### sensor[device,sensor,<mode>]

  
Hardware sensor reading.  
Return value: _Float_.  
Supported platforms: Linux, OpenBSD.

Parameters:

  * **device** \- the device name, can be a regular expression if mode is omitted;
  * **sensor** \- the sensor name, can be a regular expression if mode is omitted;
  * **mode** \- possible values: _avg_ , _max_ , or _min_ (if this parameter is omitted, device and sensor are treated verbatim).

Comments:

  * Reads /proc/sys/dev/sensors on Linux 2.4;
  * Reads /sys/class/hwmon on Linux 2.6+. See a more detailed description of [sensor](/documentation/current/en/manual/appendix/items/sensor) item on Linux.
  * Reads the _hw.sensors_ MIB on OpenBSD.

Examples:
    
    
    sensor[w83781d-i2c-0-2d,temp1]
           sensor[cpu0,temp0] #the temperature of one CPU
           sensor["cpu[0-2]$",temp,avg] #the average temperature of the first three CPUs

Copy

✔ Copied

##### system.boottime

  
The system boot time.  
Return value: _Integer (Unix timestamp)_.  
Supported platforms: Linux, FreeBSD, Solaris, MacOS X, OpenBSD, NetBSD.

##### system.cpu.discovery

  
The list of detected CPUs/CPU cores. Used for low-level discovery.  
Return value: _JSON string_.  
See supported platforms.

##### system.cpu.intr

  
The device interrupts.  
Return value: _Integer_.  
Supported platforms: Linux, FreeBSD, Solaris, AIX, OpenBSD, NetBSD.

##### system.cpu.load[<cpu>,<mode>]

  
The [CPU load](http://en.wikipedia.org/wiki/Load_\(computing\)).  
Return value: _Float_.  
See supported platforms.

Parameters:

  * **cpu** \- possible values: _all_ (default) or _percpu_ (the total load divided by online CPU count);
  * **mode** \- possible values: _avg1_ (one-minute average, default), _avg5_ , or _avg15_.

Example:
    
    
    system.cpu.load[,avg5]

Copy

✔ Copied

##### system.cpu.num[<type>]

  
The number of CPUs.  
Return value: _Integer_.  
Supported platforms: Linux, FreeBSD, Solaris, HP-UX, AIX, MacOS X, OpenBSD, NetBSD.

Parameter:

  * **type** \- possible values: _online_ (default) or _max_

The _max_ type parameter is supported only on Linux, FreeBSD, Solaris, MacOS X.

Example:
    
    
    system.cpu.num

Copy

✔ Copied

##### system.cpu.switches

  
The count of context switches.  
Return value: _Integer_.  
Supported platforms: Linux, FreeBSD, Solaris, AIX, OpenBSD, NetBSD.

##### system.cpu.util[<cpu>,<type>,<mode>,<logical or physical>]

  
The CPU utilization percentage.  
Return value: _Float_.  
Supported platforms: Linux, FreeBSD, Solaris, HP-UX, AIX, OpenBSD, NetBSD.

Parameters:

  * **cpu** \- _< CPU number>_ or _all_ (default);
  * **type** \- possible values: _user_ (default), _idle_ , _nice_ , _system_ , _iowait_ , _interrupt_ , _softirq_ , _steal_ , _spin_ (on OpenBSD), _guest_ (on Linux kernels 2.6.24 and above), or _guest_nice_ (on Linux kernels 2.6.33 and above);
  * **mode** \- possible values: _avg1_ (one-minute average, default), _avg5_ , or _avg15_ ;
  * **logical or physical** \- possible values: _logical_ (default) or _physical_. This parameter is supported on AIX only.

Comments:

  * The _nice_ type parameter is supported only on Linux, FreeBSD, HP-UX, OpenBSD, NetBSD.
  * The _iowait_ type parameter is supported only on Linux 2.6 and later, Solaris, AIX.
  * The _interrupt_ type parameter is supported only on Linux 2.6 and later, FreeBSD, OpenBSD.
  * The _softirq_ , _steal_ , _guest_ , _guest_nice_ type parameters are supported only on Linux 2.6 and later.
  * The _avg5_ and _avg15_ mode parameters are supported on Linux, FreeBSD, Solaris, HP-UX, AIX, OpenBSD, NetBSD.

Example:
    
    
    system.cpu.util[0,user,avg5]

Copy

✔ Copied

##### system.hostname[<type>,<transform>]

  
The system host name.  
Return value: _String_.  
See supported platforms.

Parameters:

  * **type** \- possible values: _netbios_ (default on Windows), _host_ (default on Linux), _shorthost_ (returns part of the hostname before the first dot, a full string for names without dots), _fqdn_ (returns Fully Qualified Domain Name);
  * **transform** \- possible values: _none_ (default) or _lower_ (convert to lowercase).

The value is acquired by taking `nodename` from the uname() system API output.

Examples of returned values:
    
    
    system.hostname → linux-w7x1
           system.hostname → example.com
           system.hostname[shorthost] → example
           system.hostname → WIN-SERV2008-I6
           system.hostname[host] → Win-Serv2008-I6LonG
           system.hostname[host,lower] → win-serv2008-i6long
           system.hostname[fqdn,lower] → blog.zabbix.com

Copy

✔ Copied

##### system.hw.chassis[<info>]

  
The chassis information.  
Return value: _String_.  
Supported platforms: Linux.

Parameter:

  * **info** \- possible values: _full_ (default), _model_ , _serial_ , _type_ , or _vendor_

Comments:

  * This item key depends on the availability of the [SMBIOS](http://en.wikipedia.org/wiki/System_Management_BIOS) table;
  * It will try to read the DMI table from sysfs, if sysfs access fails then try reading directly from memory;
  * **Root permissions** are required because the value is acquired by reading from sysfs or memory.

Example:
    
    
    system.hw.chassis[full] → Hewlett-Packard HP Pro 3010 Small Form Factor PC CZXXXXXXXX Desktop

Copy

✔ Copied

##### system.hw.cpu[<cpu>,<info>]

  
The CPU information.  
Return value: _String_ or _Integer_.  
Supported platforms: Linux.

Parameters:

  * **cpu** \- _< CPU number>_ or _all_ (default);
  * **info** \- possible values: _full_ (default), _curfreq_ , _maxfreq_ , _model_ or _vendor_.

Comments:

  * Gathers info from `/proc/cpuinfo` and `/sys/devices/system/cpu/[cpunum]/cpufreq/cpuinfo_max_freq`;
  * If a CPU number and _curfreq_ or _maxfreq_ is specified, a numeric value is returned (Hz).

Example:
    
    
    system.hw.cpu[0,vendor] → AuthenticAMD

Copy

✔ Copied

##### system.hw.devices[<type>]

  
The listing of PCI or USB devices.  
Return value: _Text_.  
Supported platforms: Linux.

Parameter:

  * **type** \- _pci_ (default) or _usb_

Returns the output of either the lspci or lsusb utility (executed without any parameters).

Example:
    
    
    system.hw.devices → 00:00.0 Host bridge: Advanced Micro Devices [AMD] RS780 Host Bridge

Copy

✔ Copied

##### system.hw.macaddr[<interface>,<format>]

  
The listing of MAC addresses.  
Return value: _String_.  
Supported platforms: Linux.

Parameters:

  * **interface** \- _all_ (default) or a regular [expression](/documentation/current/en/manual/regular_expressions#overview);
  * **format** \- _full_ (default) or _short_

Comments:

  * Lists MAC addresses of the interfaces whose name matches the given `interface` regular [expression](/documentation/current/en/manual/regular_expressions#overview) (_all_ lists for all interfaces);
  * If `format` is specified as _short_ , interface names and identical MAC addresses are not listed.

Example:
    
    
    system.hw.macaddr["eth0$",full] → [eth0] 00:11:22:33:44:55

Copy

✔ Copied

##### system.localtime[<type>]

  
The system time.  
Return value: _Integer_ \- with `type` as _utc_ ; _String_ \- with `type` as _local_.  
See supported platforms.

Parameters:

  * **type** \- possible values: _utc_ \- (default) the time since the Epoch (00:00:00 UTC, January 1, 1970), measured in seconds or _local_ \- the time in the 'yyyy-mm-dd,hh:mm:ss.nnn,+hh:mm' format

Must be used as a [passive check](/documentation/current/en/manual/appendix/items/activepassive#passive-checks) only.

Example:
    
    
    system.localtime[local] #create an item using this key and then use it to display the host time in the *Clock* dashboard widget.

Copy

✔ Copied

##### system.run[command,<mode>]

  
Run the specified command on the host.  
Return value: _Text_ result of the command or 1 - with `mode` as _nowait_ (regardless of the command result).  
See supported platforms.

Parameters:

  * **command** \- command for execution;  

  * **mode** \- possible values: _wait_ \- wait end of execution (default) or _nowait_ \- do not wait.

Comments:

  * This item is disabled by default. Learn how to [enable them](/documentation/current/en/manual/config/items/restrict_checks);
  * The return value of the item is a standard output together with a standard error produced by the command. [Exit code checking](/documentation/current/en/manual/appendix/command_execution#exit-code-checking) is not performed;
  * To be processed correctly, the return value of the command must be of `text` data type. An empty result is also allowed;
  * The return value is limited to 16MB (including trailing whitespace that is truncated); [database limits](/documentation/current/en/manual/config/items/item#text-data-limits) also apply;
  * See also: [Command execution](/documentation/current/en/manual/appendix/command_execution).

Example:
    
    
    system.run[ls -l /] #return a detailed file list of the root directory

Copy

✔ Copied

##### system.stat[resource,<type>]

  
The system statistics.  
Return value: _Integer_ or _float_.  
Supported platforms: AIX.

Parameters:

  * **ent** \- the number of processor units this partition is entitled to receive (float);
  * **kthr, <type>** \- information about kernel thread states:  
_r_ \- average number of runnable kernel threads (float)  
_b_ \- average number of kernel threads placed in the Virtual Memory Manager wait queue (float)
  * **memory, <type>** \- information about the usage of virtual and real memory:  
_avm_ \- active virtual pages (integer)  
_fre_ \- size of the free list (integer)
  * **page, <type>** \- information about page faults and paging activity:  
_fi_ \- file page-ins per second (float)  
_fo_ \- file page-outs per second (float)  
_pi_ \- pages paged in from paging space (float)  
_po_ \- pages paged out to paging space (float)  
_fr_ \- pages freed (page replacement) (float)  
_sr_ \- pages scanned by page-replacement algorithm (float)
  * **faults, <type>** \- trap and interrupt rate:  
_in_ \- device interrupts (float)  
_sy_ \- system calls (float)  
_cs_ \- kernel thread context switches (float)
  * **cpu, <type>** \- breakdown of percentage usage of processor time:  
_us_ \- user time (float)  
_sy_ \- system time (float)  
_id_ \- idle time (float)  
_wa_ \- idle time during which the system had outstanding disk/NFS I/O request(s) (float)  
_pc_ \- number of physical processors consumed (float)  
_ec_ \- the percentage of entitled capacity consumed (float)  
_lbusy_ \- indicates the percentage of logical processor(s) utilization that occurred while executing at the user and system level (float)  
_app_ \- indicates the available physical processors in the shared pool (float)
  * **disk, <type>** \- disk statistics:  
_bps_ \- indicates the amount of data transferred (read or written) to the drive in bytes per second (integer)  
_tps_ \- indicates the number of transfers per second that were issued to the physical disk/tape (float)

Comments:

  * Take note of the following limitations in these items:  
`system.stat[cpu,app]` \- supported only on AIX LPAR of type "Shared"  
`system.stat[cpu,ec]` \- supported on AIX LPAR of type "Shared" and "Dedicated" ("Dedicated" always returns 100 (percent))  
`system.stat[cpu,lbusy]` \- supported only on AIX LPAR of type "Shared"  
`system.stat[cpu,pc]` \- supported on AIX LPAR of type "Shared" and "Dedicated"  
`system.stat[ent]` \- supported on AIX LPAR of type "Shared" and "Dedicated"

##### system.sw.arch

  
The software architecture information.  
Return value: _String_.  
See supported platforms.

The info is acquired from the `uname()` function.

Example:
    
    
    system.sw.arch → i686

Copy

✔ Copied

##### system.sw.os[<info>]

  
The operating system information.  
Return value: _String_.  
Supported platforms: Linux, Windows.

Parameter:

  * **info** \- possible values: _full_ (default), _short_ , or _name_

The info is acquired from (note that not all files and options are present in all distributions):

  * `/proc/version` (_full_) on Linux;
  * `/proc/version_signature` (_short_) on Linux;
  * the PRETTY_NAME parameter from `/etc/os-release` on Linux-systems supporting it or `/etc/issue.net` (_name_);
  * the `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion` registry key on Windows.

Examples:
    
    
    system.sw.os[short] → Ubuntu 2.6.35-28.50-generic 2.6.35.11
           system.sw.os[full] → [s|Windows 10 Enterprise 22621.1.asd64fre.ni_release.220506-1250 Build 22621.963]

Copy

✔ Copied

##### system.sw.os.get

  
Detailed information about the operating system (version, type, distribution name, minor and major version, etc).  
Return value: _JSON string_.  
Supported platforms: Linux, Windows.

##### system.sw.packages[<regexp>,<manager>,<format>]

  
The listing of installed packages.  
Return value: _Text_.  
Supported platforms: Linux.

Parameters:

  * **regexp** \- _all_ (default) or a regular [expression](/documentation/current/en/manual/regular_expressions#overview);
  * **manager** \- _all_ (default) or a package manager;
  * **format** \- _full_ (default) or _short_.

Comments:

  * Lists (alphabetically) installed packages whose name matches the given regular [expression](/documentation/current/en/manual/regular_expressions#overview) (_all_ lists them all);
  * Supported package managers (executed command):  
dpkg (dpkg --get-selections)  
pkgtool (ls /var/log/packages)  
rpm (rpm -qa)  
pacman (pacman -Q)  
portage
  * If `format` is specified as _full_ , packages are grouped by package managers (each manager on a separate line beginning with its name in square brackets);
  * If `format` is specified as _short_ , packages are not grouped and are listed on a single line.

Example:
    
    
    system.sw.packages[mini,dpkg,short] → python-minimal, python2.6-minimal, ubuntu-minimal

Copy

✔ Copied

##### system.sw.packages.get[<regexp>,<manager>]

  
A detailed listing of installed packages.  
Return value: _JSON string_.  
Supported platforms: Linux.

Parameters:

  * **regexp** \- _all_ (default) or a regular [expression](/documentation/current/en/manual/regular_expressions#overview);
  * **manager** \- _all_ (default) or a package manager (possible values: _rpm_ , _dpkg_ , _pkgtool_ , _pacman_ , or _portage_).

Comments:

  * Returns unformatted JSON with the installed packages whose name matches the given regular expression;
  * The output is an array of objects each containing the following keys: name, manager, version, size, architecture, buildtime and installtime (see [more details](/documentation/current/en/manual/appendix/items/return_values_system_sw_packages_get)).

##### system.swap.in[<device>,<type>]

  
The swap-in (from device into memory) statistics.  
Return value: _Integer_.  
Supported platforms: Linux, FreeBSD, OpenBSD.

Parameters:

  * **device** \- specify the device used for swapping (Linux only) or _all_ (default);
  * **type** \- possible values: _count_ (number of swapins, default on non-Linux platforms), _sectors_ (sectors swapped in), or _pages_ (pages swapped in, default on Linux).

Comments:

  * The source of this information is:  
/proc/swaps, /proc/partitions, /proc/stat (Linux 2.4)  
/proc/swaps, /proc/diskstats, /proc/vmstat (Linux 2.6)
  * Note that _pages_ will only work if device was not specified;
  * The _sectors_ type parameter is supported only on Linux.

Example:
    
    
    system.swap.in[,pages]

Copy

✔ Copied

##### system.swap.out[<device>,<type>]

  
The swap-out (from memory onto device) statistics.  
Return value: _Integer_.  
Supported platforms: Linux, FreeBSD, OpenBSD.

Parameters:

  * **device** \- specify the device used for swapping (Linux only) or _all_ (default);
  * **type** \- possible values: _count_ (number of swapouts, default on non-Linux platforms), _sectors_ (sectors swapped out), or _pages_ (pages swapped out, default on Linux).

Comments:

  * The source of this information is:  
`/proc/swaps`, `/proc/partitions`, `/proc/stat` (Linux 2.4)  
`/proc/swaps`, `/proc/diskstats`, `/proc/vmstat` (Linux 2.6)
  * Note that _pages_ will only work if device was not specified;
  * The _sectors_ type parameter is supported only on Linux.

Example:
    
    
    system.swap.out[,pages]

Copy

✔ Copied

##### system.swap.size[<device>,<type>]

  
The swap space size in bytes or in percentage from total.  
Return value: _Integer_ \- for bytes; _Float_ \- for percentage.  
Supported platforms: Linux, FreeBSD, Solaris, AIX, OpenBSD.

Parameters:

  * **device** \- specify the device used for swapping (FreeBSD only) or _all_ (default);
  * **type** \- possible values: _free_ (free swap space, default), _pfree_ (free swap space, in percent), _pused_ (used swap space, in percent), _total_ (total swap space), or _used_ (used swap space).

Comments:

  * Note that _pfree_ , _pused_ are not supported on Windows if swap size is 0;
  * If device is not specified Zabbix agent will only take into account swap devices (files), the physical memory will be ignored. For example, on Solaris systems the `swap -s` command includes a portion of physical memory and swap devices (unlike `swap -l`).

Example:
    
    
    system.swap.size[,pfree] → free swap space percentage

Copy

✔ Copied

##### system.uname

  
Identification of the system.  
Return value: _String_.  
See supported platforms.

Comments:

  * On UNIX the value for this item is obtained with the uname() system call;
  * On Windows the item returns the OS architecture, whereas on UNIX it returns the CPU architecture.

Examples:
    
    
    system.uname → FreeBSD localhost 4.2-RELEASE FreeBSD 4.2-RELEASE #0: Mon Nov i386
           system.uname → Windows ZABBIX-WIN 6.0.6001 Microsoft® Windows Server® 2008 Standard Service Pack 1 x86

Copy

✔ Copied

##### system.uptime

  
The system uptime in seconds.  
Return value: _Integer_.  
Supported platforms: Linux, FreeBSD, Solaris, AIX, MacOS X, OpenBSD, NetBSD.

In [item configuration](/documentation/current/en/manual/config/items/item#configuration), use **s** or **uptime** units to get readable values.

##### system.users.num

  
The number of users logged in.  
Return value: _Integer_.  
See supported platforms.

The **who** command is used on the agent side to obtain the value.

##### vfs.dev.discovery

  
The list of block devices and their type. Used for low-level discovery.  
Return value: _JSON string_.  
Supported platforms: Linux.

##### vfs.dev.read[<device>,<type>,<mode>]

  
The disk read statistics.  
Return value: _Integer_ \- with `type` in _sectors_ , _operations_ , _bytes_ ; _Float_ \- with `type` in _sps_ , _ops_ , _bps_.  
Supported platforms: Linux, FreeBSD, Solaris, AIX, OpenBSD.

Parameters:

  * **device** \- disk device (default is _all_ **3**);
  * **type** \- possible values: _sectors_ , _operations_ , _bytes_ , _sps_ , _ops_ , or _bps_ (_sps_ , _ops_ , _bps_ stand for: sectors, operations, bytes per second, respectively);
  * **mode** \- possible values: _avg1_ (one-minute average, default), _avg5_ , or _avg15_. This parameter is supported only with `type` in: sps, ops, bps.

Comments:

  * If using an update interval of three hours or more**2** , this item will always return '0';
  * The _sectors_ and _sps_ type parameters are supported only on Linux;
  * The _ops_ type parameter is supported only on Linux and FreeBSD;
  * The _bps_ type parameter is supported only on FreeBSD;
  * The _bytes_ type parameter is supported only on FreeBSD, Solaris, AIX, OpenBSD;
  * The `mode` parameter is supported only on Linux, FreeBSD;
  * You may use relative device names (for example, `sda`) as well as an optional /dev/ prefix (for example, `/dev/sda`);
  * LVM logical volumes are supported;
  * The default values of 'type' parameter for different OSes:  
_AIX_ \- operations  
 _FreeBSD_ \- bps  
 _Linux_ \- sps  
 _OpenBSD_ \- operations  
 _Solaris_ \- bytes
  * _sps_ , _ops_ and _bps_ on supported platforms is limited to 1024 devices (1023 individual and one for _all_).

Example:
    
    
    vfs.dev.read[,operations]

Copy

✔ Copied

##### vfs.dev.write[<device>,<type>,<mode>]

  
The disk write statistics.  
Return value: _Integer_ \- with `type` in _sectors_ , _operations_ , _bytes_ ; _Float_ \- with `type` in _sps_ , _ops_ , _bps_.  
Supported platforms: Linux, FreeBSD, Solaris, AIX, OpenBSD.

Parameters:

  * **device** \- disk device (default is _all_ **3**);
  * **type** \- possible values: _sectors_ , _operations_ , _bytes_ , _sps_ , _ops_ , or _bps_ (_sps_ , _ops_ , _bps_ stand for: sectors, operations, bytes per second, respectively);
  * **mode** \- possible values: _avg1_ (one-minute average, default), _avg5_ , or _avg15_. This parameter is supported only with `type` in: sps, ops, bps.

Comments:

  * If using an update interval of three hours or more**2** , this item will always return '0';
  * The _sectors_ and _sps_ type parameters are supported only on Linux;
  * The _ops_ type parameter is supported only on Linux and FreeBSD;
  * The _bps_ type parameter is supported only on FreeBSD;
  * The _bytes_ type parameter is supported only on FreeBSD, Solaris, AIX, OpenBSD;
  * The `mode` parameter is supported only on Linux, FreeBSD;
  * You may use relative device names (for example, `sda`) as well as an optional /dev/ prefix (for example, `/dev/sda`);
  * LVM logical volumes are supported;
  * The default values of 'type' parameter for different OSes:  
_AIX_ \- operations  
 _FreeBSD_ \- bps  
 _Linux_ \- sps  
 _OpenBSD_ \- operations  
 _Solaris_ \- bytes
  * _sps_ , _ops_ and _bps_ on supported platforms is limited to 1024 devices (1023 individual and one for _all_).

Example:
    
    
    vfs.dev.write[,operations]

Copy

✔ Copied

##### vfs.dir.count[dir,<regex incl>,<regex excl>,<types incl>,<types excl>,<max depth>,<min size>,<max size>,<min age>,<max age>,<regex excl dir>]

  
The directory entry count.  
Return value: _Integer_.  
See supported platforms.

Parameters:

  * **dir** \- the absolute path to directory;
  * **regex incl** \- a regular [expression](/documentation/current/en/manual/regular_expressions#overview) describing the name pattern of the entity (file, directory, symbolic link) to include; include all if empty (default value);
  * **regex excl** \- a regular [expression](/documentation/current/en/manual/regular_expressions#overview) describing the name pattern of the entity (file, directory, symbolic link) to exclude; don't exclude any if empty (default value);
  * **types incl** \- directory entry types to count, possible values: _file_ \- regular file, _dir_ \- subdirectory, _sym_ \- symbolic link, _sock_ \- socket, _bdev_ \- block device, _cdev_ \- character device, _fifo_ \- FIFO, _dev_ \- synonymous with "bdev,cdev", _all_ \- all types (default), i.e. "file,dir,sym,sock,bdev,cdev,fifo". Multiple types must be separated with comma and quoted.
  * **types excl** \- directory entry types (see `types incl`) to NOT count. If some entry type is in both `types incl` and `types excl`, directory entries of this type are NOT counted.
  * **max depth** \- the maximum depth of subdirectories to traverse:  
**-1** (default) - unlimited,  
**0** \- no descending into subdirectories.
  * **min size** \- the minimum size (in bytes) for file to be counted. Smaller files will not be counted. [Memory suffixes](/documentation/current/en/manual/appendix/suffixes#memory-size-suffixes) can be used.
  * **max size** \- the maximum size (in bytes) for file to be counted. Larger files will not be counted. [Memory suffixes](/documentation/current/en/manual/appendix/suffixes#memory-size-suffixes) can be used.
  * **min age** \- the minimum age (in seconds) of directory entry to be counted. More recent entries will not be counted. [Time suffixes](/documentation/current/en/manual/appendix/suffixes#time-suffixes) can be used.
  * **max age** \- the maximum age (in seconds) of directory entry to be counted. Entries so old and older will not be counted (modification time). [Time suffixes](/documentation/current/en/manual/appendix/suffixes#time-suffixes) can be used.
  * **regex excl dir** \- a regular [expression](/documentation/current/en/manual/regular_expressions#overview) describing the name pattern of the directory to exclude. All content of the directory will be excluded (in contrast to regex_excl)

Comments:

  * Environment variables, e.g. %APP_HOME%, $HOME and %TEMP% are not supported;
  * Pseudo-directories "." and ".." are never counted;
  * Symbolic links are never followed for directory traversal;
  * Both `regex incl` and `regex excl` are being applied to files and directories when calculating the entry count, but are ignored when picking subdirectories to traverse (if `regex incl` is “(?i)^.+\\.zip$” and `max depth` is not set, then all subdirectories will be traversed, but only the files of type zip will be counted).
  * The execution time is limited by the timeout value in agent [configuration](/documentation/current/en/manual/appendix/config/zabbix_agentd#timeout) (3 sec). Since large directory traversal may take longer than that, no data will be returned and the item will turn unsupported. Partial count will not be returned.
  * When filtering by size, only regular files have meaningful sizes. Under Linux and BSD, directories also have non-zero sizes (a few Kb typically). Devices have zero sizes, e.g. the size of **/dev/sda1** does not reflect the respective partition size. Therefore, when using `<min_size>` and `<max_size>`, it is recommended to specify `<types_incl>` as "_file_ ", to avoid surprises.

Examples:
    
    
    vfs.dir.count[/dev] #monitors the number of devices in /dev (Linux)
           vfs.dir.count["C:\Users\ADMINI~1\AppData\Local\Temp"] #monitors the number of files in a temporary directory

Copy

✔ Copied

##### vfs.dir.get[dir,<regex incl>,<regex excl>,<types incl>,<types excl>,<max depth>,<min size>,<max size>,<min age>,<max age>,<regex excl dir>]

  
The directory entry list.  
Return value: _JSON string_.  
See supported platforms.

Parameters:

  * **dir** \- the absolute path to directory;
  * **regex incl** \- a regular [expression](/documentation/current/en/manual/regular_expressions#overview) describing the name pattern of the entity (file, directory, symbolic link) to include; include all if empty (default value);
  * **regex excl** \- a regular [expression](/documentation/current/en/manual/regular_expressions#overview) describing the name pattern of the entity (file, directory, symbolic link) to exclude; don't exclude any if empty (default value);
  * **types incl** \- directory entry types to list, possible values: _file_ \- regular file, _dir_ \- subdirectory, _sym_ \- symbolic link, _sock_ \- socket, _bdev_ \- block device, _cdev_ \- character device, _fifo_ \- FIFO, _dev_ \- synonymous with "bdev,cdev", _all_ \- all types (default), i.e. "file,dir,sym,sock,bdev,cdev,fifo". Multiple types must be separated with comma and quoted.
  * **types excl** \- directory entry types (see `types incl`) to NOT list. If some entry type is in both `types incl` and `types excl`, directory entries of this type are NOT listed.
  * **max depth** \- the maximum depth of subdirectories to traverse:  
**-1** (default) - unlimited,  
**0** \- no descending into subdirectories.
  * **min size** \- the minimum size (in bytes) for file to be listed. Smaller files will not be listed. [Memory suffixes](/documentation/current/en/manual/appendix/suffixes#memory-size-suffixes) can be used.
  * **max size** \- the maximum size (in bytes) for file to be listed. Larger files will not be listed. [Memory suffixes](/documentation/current/en/manual/appendix/suffixes#memory-size-suffixes) can be used.
  * **min age** \- the minimum age (in seconds) of directory entry to be listed. More recent entries will not be listed. [Time suffixes](/documentation/current/en/manual/appendix/suffixes#time-suffixes) can be used.
  * **max age** \- the maximum age (in seconds) of directory entry to be listed. Entries so old and older will not be listed (modification time). [Time suffixes](/documentation/current/en/manual/appendix/suffixes#time-suffixes) can be used.
  * **regex excl dir** \- a regular [expression](/documentation/current/en/manual/regular_expressions#overview) describing the name pattern of the directory to exclude. All content of the directory will be excluded (in contrast to `regex excl`)

Comments:

  * Environment variables, e.g. %APP_HOME%, $HOME and %TEMP% are not supported;
  * Pseudo-directories "." and ".." are never listed;
  * Symbolic links are never followed for directory traversal;
  * Both `regex incl` and `regex excl` are being applied to files and directories when generating the entry list, but are ignored when picking subdirectories to traverse (if `regex incl` is “(?i)^.+\\.zip$” and `max depth` is not set, then all subdirectories will be traversed, but only the files of type zip will be counted).
  * The execution time is limited by the timeout value in agent [configuration](/documentation/current/en/manual/appendix/config/zabbix_agentd#timeout). Since large directory traversal may take longer than that, no data will be returned and the item will turn unsupported. Partial list will not be returned.
  * When filtering by size, only regular files have meaningful sizes. Under Linux and BSD, directories also have non-zero sizes (a few Kb typically). Devices have zero sizes, e.g. the size of **/dev/sda1** does not reflect the respective partition size. Therefore, when using `min size` and `max size`, it is recommended to specify `types incl` as "_file_ ", to avoid surprises.

Examples:
    
    
    vfs.dir.get[/dev] #retrieves the device list in /dev (Linux)
           vfs.dir.get["C:\Users\ADMINI~1\AppData\Local\Temp"] #retrieves the file list in a temporary directory

Copy

✔ Copied

##### vfs.dir.size[dir,<regex incl>,<regex excl>,<mode>,<max depth>,<regex excl dir>]

  
The directory size (in bytes).  
Return value: _Integer_.  
Supported platforms: Linux, Windows. The item may work on other UNIX-like platforms.

Parameters:

  * **dir** \- the absolute path to directory;
  * **regex incl** \- a regular [expression](/documentation/current/en/manual/regular_expressions#overview) describing the name pattern of the entity (file, directory, symbolic link) to include; include all if empty (default value);
  * **regex excl** \- a regular [expression](/documentation/current/en/manual/regular_expressions#overview) describing the name pattern of the entity (file, directory, symbolic link) to exclude; don't exclude any if empty (default value);
  * **mode** \- possible values: _apparent_ (default) - gets apparent file sizes rather than disk usage (acts as `du -sb dir`), _disk_ \- gets disk usage (acts as `du -s -B1 dir`). Unlike the `du` command, the vfs.dir.size item takes hidden files in account when calculating the directory size (acts as `du -sb .[^.]* *` within dir).
  * **max depth** \- the maximum depth of subdirectories to traverse: **-1** (default) - unlimited, **0** \- no descending into subdirectories.
  * **regex excl dir** \- a regular [expression](/documentation/current/en/manual/regular_expressions#overview) describing the name pattern of the directory to exclude. All content of the directory will be excluded (in contrast to `regex excl`)

Comments:

  * Only directories with at least the read permission for _zabbix_ user are calculated. For directories with read permission only, the size of the directory itself is calculated. Directories with read & execute permissions are calculated including contents.
  * With large directories or slow drives this item may time out due to the Timeout setting in [agent](/documentation/current/en/manual/appendix/config/zabbix_agentd) and [server](/documentation/current/en/manual/appendix/config/zabbix_server)/[proxy](/documentation/current/en/manual/appendix/config/zabbix_proxy) configuration files. Increase the timeout values as necessary.
  * The file size limit depends on [large file support](/documentation/current/en/manual/appendix/items/large_file_support).

Examples:
    
    
    vfs.dir.size[/tmp,log] #calculates the size of all files in /tmp containing 'log' in their names
           vfs.dir.size[/tmp,log,^.+\.old$] #calculates the size of all files in /tmp containing 'log' in their names, excluding files with names ending with '.old'

Copy

✔ Copied

##### vfs.file.cksum[file,<mode>]

  
The file checksum, calculated by the UNIX cksum algorithm.  
Return value: _Integer_ \- with `mode` as _crc32_ , _String_ \- with `mode` as _md5_ , _sha256_.  
See supported platforms.

Parameters:

  * **file** \- the full path to file;
  * **mode** \- _crc32_ (default), _md5_ , or _sha256_.

The file size limit depends on [large file support](/documentation/current/en/manual/appendix/items/large_file_support).

Example:
    
    
    vfs.file.cksum[/etc/passwd]

Copy

✔ Copied

Examples of returned values (crc32/md5/sha256 respectively):
    
    
    675436101
           9845acf68b73991eb7fd7ee0ded23c44
           ae67546e4aac995e5c921042d0cf0f1f7147703aa42bfbfb65404b30f238f2dc

Copy

✔ Copied

##### vfs.file.contents[file,<encoding>]

  
Retrieving the contents of a file**7**.  
Return value: _Text_.  
See supported platforms.

Parameters:

  * **file** \- the full path to file;
  * **encoding** \- the code page [identifier](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#encoding-settings).

Comments:

  * The return value is limited to 16MB (including trailing whitespace that is truncated); [database limits](/documentation/current/en/manual/config/items/item#text-data-limits) also apply;
  * An empty string is returned if the file is empty or contains LF/CR characters only;
  * The byte order mark (BOM) is excluded from the output.

Example:
    
    
    vfs.file.contents[/etc/passwd]

Copy

✔ Copied

##### vfs.file.exists[file,<types incl>,<types excl>]

  
Checks if the file exists.  
Return value: 0 - not found; 1 - file of the specified type exists.  
See supported platforms.

Parameters:

  * **file** \- the full path to file;
  * **types incl** \- the list of file types to include, possible values: _file_ (regular file, default (if types_excl is not set)), _dir_ (directory), _sym_ (symbolic link), _sock_ (socket), _bdev_ (block device), _cdev_ (character device), _fifo_ (FIFO), _dev_ (synonymous with "bdev,cdev"), _all_ (all mentioned types, default if types_excl is set).
  * **types excl** \- the list of file types to exclude, see types_incl for possible values (by default no types are excluded)

Comments:

  * Multiple types must be separated with a comma and the entire set enclosed in quotes "";
  * If the same type is in both <types_incl> and <types_excl>, files of this type are excluded;
  * The file size limit depends on [large file support](/documentation/current/en/manual/appendix/items/large_file_support).

Examples:
    
    
    vfs.file.exists[/tmp/application.pid]
           vfs.file.exists[/tmp/application.pid,"file,dir,sym"]
           vfs.file.exists[/tmp/application_dir,dir]

Copy

✔ Copied

##### vfs.file.get[file]

  
Returns information about a file.  
Return value: _JSON string_.  
See supported platforms.

Parameter:

  * **file** \- the full path to file

Comments:

  * Supported file types on UNIX-like systems: regular file, directory, symbolic link, socket, block device, character device, FIFO.
  * The file size limit depends on [large file support](/documentation/current/en/manual/appendix/items/large_file_support).

Example:
    
    
    vfs.file.get[/etc/passwd] #return a JSON with information about the /etc/passwd file (type, user, permissions, SID, uid etc)

Copy

✔ Copied

##### vfs.file.md5sum[file]

  
The MD5 checksum of file.  
Return value: Character string (MD5 hash of the file).  
See supported platforms.

Parameter:

  * **file** \- the full path to file

The file size limit depends on [large file support](/documentation/current/en/manual/appendix/items/large_file_support).

Example:
    
    
    vfs.file.md5sum[/usr/local/etc/zabbix_agentd.conf]

Copy

✔ Copied

Example of returned value:
    
    
    b5052decb577e0fffd622d6ddc017e82

Copy

✔ Copied

##### vfs.file.owner[file,<ownertype>,<resulttype>]

  
Retrieves the owner of a file.  
Return value: _String_.  
See supported platforms.

Parameters:

  * **file** \- the full path to file;
  * **ownertype** \- _user_ (default) or _group_ (Unix only);
  * **resulttype** \- _name_ (default) or _id_ ; for id - return uid/gid on Unix, SID on Windows.

The file size limit depends on [large file support](/documentation/current/en/manual/appendix/items/large_file_support).

Examples:
    
    
    vfs.file.owner[/tmp/zabbix_server.log] #return the file owner of /tmp/zabbix_server.log
           vfs.file.owner[/tmp/zabbix_server.log,,id] #return the file owner ID of /tmp/zabbix_server.log

Copy

✔ Copied

##### vfs.file.permissions[file]

  
Return a 4-digit string containing the octal number with UNIX permissions.  
Return value: _String_.  
Supported platforms: Linux. The item may work on other UNIX-like platforms.

Parameters:

  * **file** \- the full path to file

The file size limit depends on [large file support](/documentation/current/en/manual/appendix/items/large_file_support).

Example:
    
    
    vfs.file.permissions[/etc/passwd] #return permissions of /etc/passwd, for example, '0644'

Copy

✔ Copied

##### vfs.file.regexp[file,regexp,<encoding>,<start line>,<end line>,<output>]

  
Retrieve a string in the file**7**.  
Return value: The line containing the matched string, or as specified by the optional `output` parameter.  
See supported platforms.

Parameters:

  * **file** \- the full path to file;
  * **regexp** \- a regular [expression](/documentation/current/en/manual/regular_expressions#overview) describing the required pattern;
  * **encoding** \- the code page [identifier](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#encoding-settings);
  * **start line** \- the number of the first line to search (first line of file by default);
  * **end line** \- the number of the last line to search (last line of file by default);
  * **output** \- an optional output formatting template. The **\0** escape sequence is replaced with the matched part of text (from the first character where match begins until the character where match ends) while an **\N** (where N=1...9) escape sequence is replaced with Nth matched group (or an empty string if the N exceeds the number of captured groups).

Comments:

  * The file size limit depends on [large file support](/documentation/current/en/manual/appendix/items/large_file_support).
  * Only the first matching line is returned;
  * An empty string is returned if no line matched the expression;
  * The byte order mark (BOM) is excluded from the output;
  * Content extraction using the `output` parameter takes place on the agent.

Examples:
    
    
    vfs.file.regexp[/etc/passwd,zabbix]
           vfs.file.regexp[/path/to/some/file,"([0-9]+)$",,3,5,\1]
           vfs.file.regexp[/etc/passwd,"^zabbix:.:([0-9]+)",,,,\1] → getting the ID of user *zabbix*

Copy

✔ Copied

##### vfs.file.regmatch[file,regexp,<encoding>,<start line>,<end line>]

  
Find a string in the file**7**.  
Return values: 0 - match not found; 1 - found.  
See supported platforms.

Parameters:

  * **file** \- the full path to file;
  * **regexp** \- a regular [expression](/documentation/current/en/manual/regular_expressions#overview) describing the required pattern;
  * **encoding** \- the code page [identifier](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#encoding-settings);
  * **start line** \- the number of the first line to search (first line of file by default);
  * **end line** \- the number of the last line to search (last line of file by default).

Comments:

  * The file size limit depends on [large file support](/documentation/current/en/manual/appendix/items/large_file_support).
  * The byte order mark (BOM) is ignored.

Example:
    
    
    vfs.file.regmatch[/var/log/app.log,error]

Copy

✔ Copied

##### vfs.file.size[file,<mode>]

  
The file size (in bytes).  
Return value: _Integer_.  
See supported platforms.

Parameters:

  * **file** \- the full path to file;
  * **mode** \- possible values: _bytes_ (default) or _lines_ (empty lines are counted, too).

Comments:

  * The file must have read permissions for user _zabbix_ ;
  * The file size limit depends on [large file support](/documentation/current/en/manual/appendix/items/large_file_support).

Example:
    
    
    vfs.file.size[/var/log/syslog]

Copy

✔ Copied

##### vfs.file.time[file,<mode>]

  
The file time information.  
Return value: _Integer_ (Unix timestamp).  
See supported platforms.

Parameters:

  * **file** \- the full path to file;
  * **mode** \- possible values:  
_modify_ (default) - the last time of modifying file content,  
_access_ \- the last time of reading file,  
_change_ \- the last time of changing file properties

The file size limit depends on [large file support](/documentation/current/en/manual/appendix/items/large_file_support).

Example:
    
    
    vfs.file.time[/etc/passwd,modify]

Copy

✔ Copied

##### vfs.fs.discovery

  
The list of mounted filesystems with their type and mount options. Used for low-level discovery.  
Return value: _JSON string_.  
Supported platforms: Linux, FreeBSD, Solaris, HP-UX, AIX, MacOS X, OpenBSD, NetBSD.

##### vfs.fs.get

  
The list of mounted filesystems with their type, available disk space, inode statistics and mount options. Can be used for low-level discovery.  
Return value: _JSON string_.  
Supported platforms: Linux, FreeBSD, Solaris, HP-UX, AIX, MacOS X, OpenBSD, NetBSD.

Comments:

  * File systems with the inode count equal to zero, which can be the case for file systems with dynamic inodes (e.g. btrfs), are also reported;
  * See also: [Discovery of mounted filesystems](/documentation/current/en/manual/discovery/low_level_discovery/examples/mounted_filesystems).

##### vfs.fs.inode[fs,<mode>]

  
The number or percentage of inodes.  
Return value: _Integer_ \- for number; _Float_ \- for percentage.  
See supported platforms.

Parameters:

  * **fs** \- the filesystem;
  * **mode** \- possible values: _total_ (default), _free_ , _used_ , _pfree_ (free, percentage), or _pused_ (used, percentage).

If the inode count equals zero, which can be the case for file systems with dynamic inodes (e.g. btrfs), the pfree/pused values will be reported as "100" and "0" respectively.

Example:
    
    
    vfs.fs.inode[/,pfree]

Copy

✔ Copied

##### vfs.fs.size[fs,<mode>]

  
The disk space in bytes or in percentage from total.  
Return value: _Integer_ \- for bytes; _Float_ \- for percentage.  
See supported platforms.

Parameters:

  * **fs** \- the filesystem;
  * **mode** \- possible values: _total_ (default), _free_ , _used_ , _pfree_ (free, percentage), or _pused_ (used, percentage).

Comments:

  * If the filesystem is not mounted, returns the size of a local filesystem where the mount point is located;
  * The reserved space of a file system is taken into account and not included when using the _free_ mode.

Example:
    
    
    vfs.fs.size[/tmp,free]

Copy

✔ Copied

##### vm.memory.size[<mode>]

  
The memory size in bytes or in percentage from total.  
Return value: _Integer_ \- for bytes; _Float_ \- for percentage.  
See supported platforms.

Parameter:

  * **mode** \- possible values: _total_ (default), _active_ , _anon_ , _buffers_ , _cached_ , _exec_ , _file_ , _free_ , _inactive_ , _pinned_ , _shared_ , _slab_ , _wired_ , _used_ , _pused_ (used, percentage), _available_ , or _pavailable_ (available, percentage).

Comments:

  * This item accepts three categories of parameters:  
1) _total_ \- total amount of memory  
2) platform-specific memory types: _active_ , _anon_ , _buffers_ , _cached_ , _exec_ , _file_ , _free_ , _inactive_ , _pinned_ , _shared_ , _slab_ , _wired_  
3) user-level estimates on how much memory is used and available: _used_ , _pused_ , _available_ , _pavailable_
  * The _active_ mode parameter is supported only on FreeBSD, HP-UX, MacOS X, OpenBSD, NetBSD;
  * The _anon_ , _exec_ , _file_ mode parameters are supported only on NetBSD;
  * The _buffers_ mode parameter is supported only on Linux, FreeBSD, OpenBSD, NetBSD;
  * The _cached_ mode parameter is supported only on Linux, FreeBSD, AIX, OpenBSD, NetBSD;
  * The _inactive_ , _wired_ mode parameters are supported only on FreeBSD, MacOS X, OpenBSD, NetBSD;
  * The _pinned_ mode parameter is supported only on AIX;
  * The _shared_ mode parameter is supported only on Linux 2.4, FreeBSD, OpenBSD, NetBSD;
  * See also [additional details](/documentation/current/en/manual/appendix/items/vm.memory.size_params) for this item.

Example:
    
    
    vm.memory.size[pavailable]

Copy

✔ Copied

##### web.page.get[host,<path>,<port>]

  
Get the content of a web page.  
Return value: Web page source as text (including headers).  
See supported platforms.

Parameters:

  * **host** \- the hostname or URL (as `scheme://host:port/path`, where only _host_ is mandatory). Allowed URL schemes: _http_ , _https_**4**. A missing scheme will be treated as _http_. If a URL is specified `path` and `port` must be empty. Specifying user name/password when connecting to servers that require authentication, for example: `http://user:password@www.example.com` is only possible with cURL support **4**. [Punycode](https://en.wikipedia.org/wiki/Punycode) is supported in hostnames.
  * **path** \- the path to an HTML document (default is /);
  * **port** \- the port number (default is 80 for HTTP)

Comments:

  * This item turns unsupported if the resource specified in `host` does not exist or is unavailable;
  * `host` can be a hostname, domain name, IPv4 or IPv6 address. But for IPv6 address Zabbix agent must be compiled with IPv6 support enabled.

Examples:
    
    
    web.page.get[www.example.com,index.php,80]
           web.page.get[https://www.example.com]
           web.page.get[https://blog.example.com/?s=zabbix]
           web.page.get[localhost:80]
           web.page.get["[::1]/server-status"]

Copy

✔ Copied

##### web.page.perf[host,<path>,<port>]

  
The loading time of a full web page (in seconds).  
Return value: _Float_.  
See supported platforms.

Parameters:

  * **host** \- the hostname or URL (as `scheme://host:port/path`, where only _host_ is mandatory). Allowed URL schemes: _http_ , _https_**4**. A missing scheme will be treated as _http_. If a URL is specified `path` and `port` must be empty. Specifying user name/password when connecting to servers that require authentication, for example: `http://user:password@www.example.com` is only possible with cURL support **4**. Punycode is supported in hostnames.
  * **path** \- the path to an HTML document (default is /);
  * **port** \- the port number (default is 80 for HTTP)

Comments:

  * This item turns unsupported if the resource specified in `host` does not exist or is unavailable;
  * `host` can be a hostname, domain name, IPv4 or IPv6 address. But for IPv6 address Zabbix agent must be compiled with IPv6 support enabled.

Examples:
    
    
    web.page.perf[www.example.com,index.php,80]
           web.page.perf[https://www.example.com]

Copy

✔ Copied

##### web.page.regexp[host,<path>,<port>,regexp,<length>,<output>]

  
Find a string on the web page.  
Return value: The matched string, or as specified by the optional `output` parameter.  
See supported platforms.

Parameters:

  * **host** \- the hostname or URL (as `scheme://host:port/path`, where only _host_ is mandatory). Allowed URL schemes: _http_ , _https_**4**. A missing scheme will be treated as _http_. If a URL is specified `path` and `port` must be empty. Specifying user name/password when connecting to servers that require authentication, for example: `http://user:password@www.example.com` is only possible with cURL support **4**. Punycode is supported in hostnames.
  * **path** \- the path to an HTML document (default is /);
  * **port** \- the port number (default is 80 for HTTP)
  * **regexp** \- a regular [expression](/documentation/current/en/manual/regular_expressions#overview) describing the required pattern;
  * **length** \- the maximum number of characters to return;
  * **output** \- an optional output formatting template. The **\0** escape sequence is replaced with the matched part of text (from the first character where match begins until the character where match ends) while an **\N** (where N=1...9) escape sequence is replaced with Nth matched group (or an empty string if the N exceeds the number of captured groups).

Comments:

  * This item turns unsupported if the resource specified in `host` does not exist or is unavailable;
  * `host` can be a hostname, domain name, IPv4 or IPv6 address. But for IPv6 address Zabbix agent must be compiled with IPv6 support enabled.
  * Content extraction using the `output` parameter takes place on the agent.

Examples:
    
    
    web.page.regexp[www.example.com,index.php,80,OK,2]
           web.page.regexp[https://www.example.com,,,OK,2]

Copy

✔ Copied

##### agent.hostmetadata

  
The agent host metadata.  
Return value: _String_.  
See supported platforms.

Returns the value of [HostMetadata](/documentation/current/en/manual/appendix/config/zabbix_agentd#hostmetadata) or [HostMetadataItem](/documentation/current/en/manual/appendix/config/zabbix_agentd#hostmetadataitem) parameters, or empty string if none are defined.

##### agent.hostname

  
The agent host name.  
Return value: _String_.  
See supported platforms.

Returns:

  * As passive check - the name of the first host listed in the [Hostname](/documentation/current/en/manual/appendix/config/zabbix_agentd#hostname) parameter of the agent configuration file;
  * As active check - the name of the current hostname.

##### agent.ping

  
The agent availability check.  
Return value: Nothing - unavailable; 1 - available.  
See supported platforms.

Use the **nodata()** trigger function to check for host unavailability.

##### agent.variant

  
The variant of Zabbix agent (Zabbix agent or Zabbix agent 2).  
Return value: 1 - Zabbix agent; 2 - Zabbix agent 2.  
See supported platforms.

##### agent.version

  
The version of Zabbix agent.  
Return value: _String_.  
See supported platforms.

Example of returned value:
    
    
    6.0.3

Copy

✔ Copied

##### zabbix.stats[<ip>,<port>]

  
Returns a set of Zabbix server or proxy internal metrics remotely.  
Return value: _JSON string_.  
See supported platforms.

Parameters:

  * **ip** \- the IP/DNS/network mask list of servers/proxies to be remotely queried (default is 127.0.0.1);
  * **port** \- the port of server/proxy to be remotely queried (default is 10051)

Comments:

  * A selected set of internal metrics is returned by this item. For details, see [Remote monitoring of Zabbix stats](/documentation/current/en/manual/appendix/items/remote_stats#exposed-metrics);
  * Note that the stats request will only be accepted from the addresses listed in the 'StatsAllowedIP' [server](/documentation/current/en/manual/appendix/config/zabbix_server)/[proxy](/documentation/current/en/manual/appendix/config/zabbix_proxy) parameter on the target instance.

##### zabbix.stats[<ip>,<port>,queue,<from>,<to>]

  
Returns the number of monitored items in the queue which are delayed on Zabbix server or proxy remotely.  
Return value: _JSON string_.  
See supported platforms.

Parameters:

  * **ip** \- the IP/DNS/network mask list of servers/proxies to be remotely queried (default is 127.0.0.1);
  * **port** \- the port of server/proxy to be remotely queried (default is 10051)
  * **queue** \- constant (to be used as is)
  * **from** \- delayed by at least (default is 6 seconds)
  * **to** \- delayed by at most (default is infinity)

Note that the stats request will only be accepted from the addresses listed in the 'StatsAllowedIP' [server](/documentation/current/en/manual/appendix/config/zabbix_server)/[proxy](/documentation/current/en/manual/appendix/config/zabbix_proxy) parameter on the target instance.

#### Footnotes

**1** A Linux-specific note. Zabbix agent must have read-only access to filesystem _/proc_. Kernel patches from www.grsecurity.org limit access rights of non-privileged users.

**2** `vfs.dev.read[]`, `vfs.dev.write[]`: Zabbix agent will terminate "stale" device connections if the item values are not accessed for more than 3 hours. This may happen if a system has devices with dynamically changing paths or if a device gets manually removed. Note also that these items, if using an update interval of 3 hours or more, will always return '0'.

**3** `vfs.dev.read[]`, `vfs.dev.write[]`: If default _all_ is used for the first parameter then the key will return summary statistics, including all block devices like sda, sdb, and their partitions (sda1, sda2, sdb3...) and multiple devices (MD raid) based on those block devices/partitions and logical volumes (LVM) based on those block devices/partitions. In such cases returned values should be considered only as relative value (dynamic in time) but not as absolute values.

**4** SSL (HTTPS) is supported only if agent is compiled with cURL support. Otherwise the item will turn unsupported.

**5** The `bytes` and `errors` values are not supported for loopback interfaces on Solaris systems up to and including Solaris 10 6/06 as byte, error and utilization statistics are not stored and/or reported by the kernel. However, if you're monitoring a Solaris system via net-snmp, values may be returned as net-snmp carries legacy code from the cmu-snmp dated as old as 1997 that, upon failing to read byte values from the interface statistics returns the packet counter (which does exist on loopback interfaces) multiplied by an arbitrary value of 308. This makes the assumption that the average length of a packet is 308 octets, which is a very rough estimation as the MTU limit on Solaris systems for loopback interfaces is 8892 bytes. These values should not be assumed to be correct or even closely accurate. They are guestimates. Zabbix agent does not do any guess work, but net-snmp will return a value for these fields.

**6** The command line on Solaris, obtained from /proc/pid/psinfo, is limited to 80 bytes and contains the command line as it was when the process was started.

**7** `vfs.file.contents[]`, `vfs.file.regexp[]`, `vfs.file.regmatch[]` items can be used for retrieving file contents. If you want to restrict access to specific files with sensitive information, run Zabbix agent under a user that has no access permissions to viewing these files.

### Usage with command-line utilities

Note that when testing or using item keys with zabbix_agentd or zabbix_get from the command line you should consider shell syntax too.

For example, if a certain parameter of the key has to be enclosed in double quotes you have to explicitly escape double quotes, otherwise they will be trimmed by the shell as special characters and will not be passed to the Zabbix utility.

Examples:
    
    
    zabbix_agentd -t 'vfs.dir.count[/var/log,,,"file,dir",,0]'
           
           zabbix_agentd -t vfs.dir.count[/var/log,,,\"file,dir\",,0]

Copy

✔ Copied

### Encoding settings

To make sure that the acquired data are not corrupted you may specify the correct encoding for processing the check (e.g. 'vfs.file.contents') in the `encoding` parameter. The list of supported encodings (code page identifiers) may be found in documentation for [libiconv](http://www.gnu.org/software/libiconv/) (GNU Project) or in Microsoft Windows SDK documentation for ["Code Page Identifiers"](https://learn.microsoft.com/en-us/windows/win32/intl/code-page-identifiers). Note that Microsoft sometimes marks some code pages as "available only to managed applications" — i.e. exposed only via the .NET runtime and not available through the native Win32 APIs. Zabbix agent implements its own encoding-conversion logic, therefore those code pages are supported by Zabbix agent even when the native Windows functions do not provide them.

If no encoding is specified in the `encoding` parameter the following resolution strategies are applied:

  * If encoding is not specified (or is an empty string) it is assumed to be UTF-8, the data is processed "as-is";
  * BOM analysis - applicable for items 'vfs.file.contents', 'vfs.file.regexp', 'vfs.file.regmatch'. An attempt is made to determine the correct encoding by using the byte order mark (BOM) at the beginning of the file. If BOM is not present - standard resolution (see above) is applied instead.

### Troubleshooting agent items

In case of passive checks, to prevent that item does not get any value because the server request to the agent times out first, the following should be noted:

  * Where agent version is older than server version, the _Timeout_ value in the [item configuration](/documentation/current/en/manual/config/items/item#configuration) (or [global timeout](/documentation/current/en/manual/web_interface/frontend_sections/administration/general#timeouts)) may need to be higher than the `Timeout` value in the agent [configuration file](/documentation/current/en/manual/appendix/config/zabbix_agentd#timeout).
  * Where agent version is newer than server version, the `Timeout` value in the server [configuration file](/documentation/current/en/manual/appendix/config/zabbix_server#timeout) may need to be higher than the `Timeout` value in the agent [configuration file](/documentation/current/en/manual/appendix/config/zabbix_agentd#timeout).