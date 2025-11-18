---
title: Windows Zabbix agent
source: https://www.zabbix.com/documentation/current/en/manual/config/items/itemtypes/zabbix_agent/win_keys
downloaded: 2025-11-14 10:34:57
---

# 2 Windows Zabbix agent

### Overview

The Windows Zabbix agent items are presented in two lists:

  * Shared items \- the item keys that are shared with the UNIX Zabbix agent;
  * Windows-specific items \- the item keys that are supported **only** on Windows.

Note that all item keys supported by Zabbix agent on Windows are also supported by the new generation Zabbix agent 2. See the [additional item keys](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent/zabbix_agent2) that you can use with the agent 2 only.

See also: [Minimum permissions for Windows items](/documentation/current/en/manual/appendix/items/win_permissions)

### Shared items

The table below lists Zabbix agent items that are supported on Windows and are shared with the UNIX Zabbix agent:

  * The item key is a link to full details of the UNIX Zabbix agent item
  * Windows-relevant item comments are included

[log](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#log) | The monitoring of a log file. This item is not supported for Windows Event Log.  
The `persistent_dir` parameter is not supported on Windows. | [Log monitoring](/documentation/current/en/manual/config/items/itemtypes/log_items)  
---|---|---  
[log.count](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#log.count) | The count of matched lines in a monitored log file. This item is not supported for Windows Event Log.  
The `persistent_dir` parameter is not supported on Windows.  
[logrt](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#logrt) | The monitoring of a log file that is rotated. This item is not supported for Windows Event Log.  
The `persistent_dir` parameter is not supported on Windows.  
[logrt.count](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#logrt.count) | The count of matched lines in a monitored log file that is rotated. This item is not supported for Windows Event Log.  
The `persistent_dir` parameter is not supported on Windows.  
[modbus.get](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#modbus) | Reads Modbus data. | Modbus  
[net.dns](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#net.dns) | Checks if the DNS service is up.  
The `ip`, `timeout` and `count` parameters are ignored on Windows unless using Zabbix agent 2. | Network  
[net.dns.perf](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#net.dns.perf) | Checks the performance of a DNS service.  
The `ip`, `timeout` and `count` parameters are ignored on Windows unless using Zabbix agent 2.  
[net.dns.record](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#net.dns.record) | Performs a DNS query.  
The `ip`, `timeout` and `count` parameters are ignored on Windows unless using Zabbix agent 2.  
[net.if.discovery](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#net.if.discovery) | The list of network interfaces.  
Some Windows versions (for example, Server 2008) might require the latest updates installed to support non-ASCII characters in interface names.  
[net.if.in](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#net.if.in) | The incoming traffic statistics on a network interface.  
On Windows, the item gets values from 64-bit counters if available. 64-bit interface statistic counters were introduced in Windows Vista and Windows Server 2008. If 64-bit counters are not available, the agent uses 32-bit counters.  
Multi-byte interface names on Windows are supported.  
You may obtain network interface descriptions on Windows with net.if.discovery or net.if.list items.  
[net.if.out](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#net.if.out) | The outgoing traffic statistics on a network interface.  
On Windows, the item gets values from 64-bit counters if available. 64-bit interface statistic counters were introduced in Windows Vista and Windows Server 2008. If 64-bit counters are not available, the agent uses 32-bit counters.  
Multi-byte interface names on Windows are supported.  
You may obtain network interface descriptions on Windows with net.if.discovery or net.if.list items.  
[net.if.total](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#net.if.total) | The sum of incoming and outgoing traffic statistics on a network interface.  
On Windows, the item gets values from 64-bit counters if available. 64-bit interface statistic counters were introduced in Windows Vista and Windows Server 2008. If 64-bit counters are not available, the agent uses 32-bit counters.  
You may obtain network interface descriptions on Windows with net.if.discovery or net.if.list items.  
[net.tcp.listen](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#net.tcp.listen) | Checks if this TCP port is in LISTEN state.  
[net.tcp.port](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#net.tcp.port) | Checks if it is possible to make a TCP connection to the specified port.  
[net.tcp.service](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#net.tcp.service) | Checks if a service is running and accepting TCP connections.  
Checking of LDAP and HTTPS on Windows is only supported by Zabbix agent 2.  
[net.tcp.service.perf](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#net.tcp.service.perf) | Checks the performance of a TCP service.  
Checking of LDAP and HTTPS on Windows is only supported by Zabbix agent 2.  
[net.tcp.socket.count](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#net.tcp.socket.count) | Returns the number of TCP sockets that match parameters.  
This item is supported on Linux by Zabbix agent, but on Windows it is supported only by [Zabbix agent 2](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent/zabbix_agent2) on 64-bit Windows.  
[net.udp.service](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#net.udp.service) | Checks if a service is running and responding to UDP requests.  
[net.udp.service.perf](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#net.udp.service.perf) | Checks the performance of a UDP service.  
[net.udp.socket.count](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#net.udp.socket.count) | Returns the number of UDP sockets that match parameters.  
This item is supported on Linux by Zabbix agent, but on Windows it is supported only by [Zabbix agent 2](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent/zabbix_agent2) on 64-bit Windows.  
[proc.get](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#proc.get) | The list of OS processes and their parameters.  
The `cmdline` parameter is not supported on Windows. | Processes  
[proc.num](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#proc.num) | The number of processes.  
On Windows, only the `name` and `user` parameters are supported.  
[system.cpu.discovery](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#system.cpu.discovery) | The list of detected CPUs/CPU cores. | System  
[system.cpu.load](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#system.cpu.load) | The CPU load.  
When a collector process is started on Zabbix agent, the following performance counters are initialized and later used for this item: `\System\Processor Queue Length`  
[system.cpu.num](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#system.cpu.num) | The number of CPUs.  
[system.cpu.util](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#system.cpu.util) | The CPU utilization percentage.  
The value is acquired using the _Processor Time_ performance counter. Note that since Windows 8 its Task Manager shows CPU utilization based on the _Processor Utility_ performance counter, while in previous versions it was the _Processor Time_ counter (see [more details](/documentation/current/en/manual/appendix/items/system_cpu_util)).  
_system_ is the only `type` parameter supported on Windows.  
[system.hostname](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#system.hostname) | The system host name.  
The value is acquired by either GetComputerName() (for **netbios**), GetComputerNameExA() (for **fqdn**), or gethostname() (for **host**) functions on Windows.  
See also a [more detailed description](/documentation/current/en/manual/appendix/install/windows_agent#configuring-agent).  
[system.localtime](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#system.localtime) | The system time.  
[system.run](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#system.run) | Run the specified command on the host.  
[system.sw.arch](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#system.sw.arch) | The software architecture information.  
[system.swap.size](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#system.swap.size) | The swap space size in bytes or in percentage from total.  
The `pused` type parameter is supported on Linux by Zabbix agent, but on Windows it is supported only by [Zabbix agent 2](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent/zabbix_agent2).  
Note that this key might report incorrect swap space size/percentage on virtualized (VMware ESXi, VirtualBox) Windows platforms. In this case you may use the `perf_counter[\700(_Total)\702]` key to obtain correct swap space percentage.  
[system.uname](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#system.uname) | Identification of the system.  
On Windows the value for this item is obtained from Win32_OperatingSystem and Win32_Processor WMI classes. The OS name (including edition) might be translated to the user's display language. On some versions of Windows it contains trademark symbols and extra spaces.  
[system.uptime](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#system.uptime) | The system uptime in seconds.  
[vfs.dir.count](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#vfs.dir.count) | The directory entry count.  
On Windows, directory symlinks are skipped and hard links are counted only once. | Virtual file systems  
[vfs.dir.get](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#vfs.dir.get) | The directory entry list.  
On Windows, directory symlinks are skipped and hard links are counted only once.  
[vfs.dir.size](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#vfs.dir.size) | The directory size.  
On Windows any symlink is skipped and hard links are taken into account only once.  
[vfs.file.cksum](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#vfs.file.cksum) | The file checksum, calculated by the UNIX cksum algorithm.  
[vfs.file.contents](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#vfs.file.contents) | Retrieving the contents of a file.  
[vfs.file.exists](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#vfs.file.exists) | Checks if the file exists.  
On Windows the double quotes have to be backslash '\' escaped and the whole item key enclosed in double quotes when using the command line utility for calling zabbix_get.exe or agent2.  
Note that the item may turn unsupported on Windows if a directory is searched within a non-existing directory, e.g. `vfs.file.exists[C:\no\dir,dir]` (where 'no' does not exist).  
[vfs.file.get](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#vfs.file.get) | Returns information about a file.  
Supported file types on Windows: regular file, directory, symbolic link  
[vfs.file.md5sum](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#vfs.file.md5sum) | The MD5 checksum of file.  
[vfs.file.owner](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#vfs.file.owner) | Retrieves the owner of a file.  
[vfs.file.regexp](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#vfs.file.regexp) | Retrieve a string in the file.  
[vfs.file.regmatch](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#vfs.file.regmatch) | Find a string in the file.  
[vfs.file.size](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#vfs.file.sizefilemode) | The file size.  
[vfs.file.time](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#vfs.file.timefilemode) | The file time information.  
On Windows XP `vfs.file.time[file,change]` may be equal to `vfs.file.time[file,access]`.  
[vfs.fs.discovery](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#vfs.fs.discovery) | The list of mounted filesystems with their type and mount options.  
The {#FSLABEL} macro is supported on Windows.  
[vfs.fs.get](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#vfs.fs.get) | The list of mounted filesystems with their type, available disk space, inode statistics and mount options.  
The {#FSLABEL} macro is supported on Windows.  
[vfs.fs.size](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#vfs.fs.size) | The disk space in bytes or in percentage from total.  
[vm.memory.size](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#vm.memory.size) | The memory size in bytes or in percentage from total. | Virtual memory  
[web.page.get](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#web.page.get) | Get the content of a web page. | Web monitoring  
[web.page.perf](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#web.page.perf) | The loading time of a full web page.  
[web.page.regexp](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#web.page.regexp) | Find a string on the web page.  
[agent.hostmetadata](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#agent.hostmetadata) | The agent host metadata. | Zabbix  
[agent.hostname](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#agent.hostname) | The agent host name.  
[agent.ping](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#agent.ping) | The agent availability check.  
[agent.variant](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#agent.variant) | The variant of Zabbix agent (Zabbix agent or Zabbix agent 2).  
[agent.version](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#agent.version) | The version of Zabbix agent.  
[zabbix.stats](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#zabbix.stats) | Returns a set of Zabbix server or proxy internal metrics remotely.  
[zabbix.stats](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#zabbix.stats.two) | Returns the number of monitored items in the queue which are delayed on Zabbix server or proxy remotely.  
  
### Windows-specific items

The table provides details on the item keys that are supported **only** by the Windows Zabbix agent.

Windows-specific items sometimes are an approximate counterpart of a similar agent item, for example `proc_info`, supported on Windows, roughly corresponds to the `proc.mem` item, not supported on Windows.

The item key is a link to full item key details.

eventlog | The Windows event log monitoring. | Log monitoring  
---|---|---  
eventlog.count | The count of lines in the Windows event log.  
net.if.list | The network interface list (includes interface type, status, IPv4 address, description). | Network  
perf_counter | The value of any Windows performance counter. | Performance counters  
perf_counter_en | The value of any Windows performance counter in English.  
perf_instance.discovery | The list of object instances of Windows performance counters.  
perf_instance_en.discovery | The list of object instances of Windows performance counters, discovered using the object names in English.  
proc_info | Various information about specific process(es). | Processes  
registry.data | Return data for the specified value name in the Windows Registry key. | Registry  
registry.get | The list of Windows Registry values or keys located at given key.  
service.discovery | The list of Windows services. | Services  
service.info | Information about a service.  
services | The listing of services.  
vm.vmemory.size | The virtual memory size in bytes or in percentage from the total. | Virtual memory  
wmi.get | Execute a WMI query and return the first selected object. | WMI  
wmi.getall | Execute a WMI query and return the whole response.  
  
### Item key details

Parameters without angle brackets are mandatory. Parameters marked with angle brackets **<** **>** are optional.

##### eventlog[name,<regexp>,<severity>,<source>,<eventid>,<maxlines>,<mode>]

  
The event log monitoring.  
Return value: _Log_.

Parameters:

  * **name** \- the name of the event log channel (_Log Name_ in the Event Viewer GUI);  

  * **regexp** \- a regular [expression](/documentation/current/en/manual/regular_expressions#overview) describing the required pattern (case sensitive);  

  * **severity** \- a regular expression describing severity (case insensitive). This parameter accepts a regular expression based on the following values: "Information", "Warning", "Error", "Critical", "Verbose" (running on Windows Vista or newer).  

  * **source** \- a regular expression describing the source identifier (case insensitive);  

  * **eventid** \- a regular expression describing the event identifier(s) (case sensitive);  

  * **maxlines** \- the maximum number of new lines per second the agent will send to Zabbix server or proxy. This parameter overrides the value of 'MaxLinesPerSecond' in [zabbix_agentd.conf](/documentation/current/en/manual/appendix/config/zabbix_agentd_win).  

  * **mode** \- possible values: _all_ (default) or _skip_ \- skip the processing of older data (affects only newly created items).

Comments:

  * The item must be configured as an [active check](/documentation/current/en/manual/appendix/items/activepassive#active-checks);
  * The agent is unable to send in events from the "Forwarded events" log;
  * Windows Eventing 6.0 is supported;
  * Selecting a non-Log [type of information](/documentation/current/en/manual/config/items/item#configuration) for this item will lead to the loss of local timestamp, as well as log severity and source information;
  * See also additional information on [log monitoring](/documentation/current/en/manual/config/items/itemtypes/log_items).

Examples:
    
    
    eventlog[Application]
           eventlog[Microsoft-Windows-Application-Experience/Program-Compatibility-Assistant]
           eventlog[Security,,"Failure Audit",,^(529|680)$]
           eventlog[System,,"Warning|Error"]
           eventlog[System,,,,^1$]
           eventlog[Windows PowerShell,,,,,,skip]
           eventlog[System,,,,@TWOSHORT] #here a custom regular expression named `TWOSHORT` is referenced (defined as a *Result is TRUE* type, the expression itself being `^1$|^70$`).

Copy

✔ Copied

##### eventlog.count[name,<regexp>,<severity>,<source>,<eventid>,<maxproclines>,<mode>]

  
The count of lines in the Windows event log.  
Return value: _Integer_.

Parameters:

  * **name** \- the name of the event log channel (_Log Name_ in the Event Viewer GUI);  

  * **regexp** \- a regular [expression](/documentation/current/en/manual/regular_expressions#overview) describing the required pattern (case sensitive);  

  * **severity** \- a regular expression describing severity (case insensitive). This parameter accepts a regular expression based on the following values: "Information", "Warning", "Error", "Critical", "Verbose" (running on Windows Vista or newer).  

  * **source** \- a regular expression describing the source identifier (case insensitive);  

  * **eventid** \- a regular expression describing the event identifier(s) (case sensitive);  

  * **maxproclines** \- the maximum number of new lines per second the agent will analyze (cannot exceed 10000). The default value is 10*'MaxLinesPerSecond' in [zabbix_agentd.conf](/documentation/current/en/manual/appendix/config/zabbix_agentd_win).  

  * **mode** \- possible values: _all_ (default) or _skip_ \- skip the processing of older data (affects only newly created items).

Comments:

  * The item must be configured as an [active check](/documentation/current/en/manual/appendix/items/activepassive#active-checks);
  * The agent is unable to send in events from the "Forwarded events" log;
  * Windows Eventing 6.0 is supported;
  * Selecting a non-Log [type of information](/documentation/current/en/manual/config/items/item#configuration) for this item will lead to the loss of local timestamp, as well as log severity and source information;
  * See also additional information on [log monitoring](/documentation/current/en/manual/config/items/itemtypes/log_items).

Examples:
    
    
    eventlog.count[System,,"Warning|Error"]
           eventlog.count[Windows PowerShell,,,,,,skip]

Copy

✔ Copied

##### net.if.list

  
The network interface list (includes interface type, status, IPv4 address, description).  
Return value: _Text_.

Comments:

  * Multi-byte interface names supported;
  * Disabled interfaces are not listed;
  * Enabling/disabling some components may change their ordering in the Windows interface name;
  * Some Windows versions (for example, Server 2008) might require the latest updates installed to support non-ASCII characters in interface names.

##### perf_counter[counter,<interval>]

  
The value of any Windows performance counter.  
Return value: _Integer_ , _float_ , _string_ or _text_ (depending on the request).

Parameters:

  * **counter** \- the path to the counter;  

  * **interval** \- the last N seconds for storing the average value. The `interval` must be between 1 and 900 seconds (included) and the default value is 1.

Comments:

  * `interval` is used for counters that require more than one sample (like CPU utilization), so the check returns an average value for last "interval" seconds every time;
  * Performance Monitor can be used to obtain the list of available counters.
  * See also: [Windows performance counters](/documentation/current/en/manual/config/items/perfcounters).

##### perf_counter_en[counter,<interval>]

  
The value of any Windows performance counter in English.  
Return value: _Integer_ , _float_ , _string_ or _text_ (depending on the request).

Parameters:

  * **counter** \- the path to the counter in English;  

  * **interval** \- the last N seconds for storing the average value. The `interval` must be between 1 and 900 seconds (included) and the default value is 1.

Comments:

  * `interval` is used for counters that require more than one sample (like CPU utilization), so the check returns an average value for last "interval" seconds every time;
  * This item is only supported on **Windows Server 2008/Vista** and above;
  * You can find the list of English strings by viewing the following registry key: `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Perflib\009`.

##### perf_instance.discovery[object]

  
The list of object instances of Windows performance counters. Used for [low-level discovery](/documentation/current/en/manual/discovery/low_level_discovery/examples/windows_perf_instances).  
Return value: _JSON object_.

Parameter:

  * **object** \- the object name (localized).

##### perf_instance_en.discovery[object]

  
The list of object instances of Windows performance counters, discovered using the object names in English. Used for [low-level discovery](/documentation/current/en/manual/discovery/low_level_discovery/examples/windows_perf_instances).  
Return value: _JSON object_.

Parameter:

  * **object** \- the object name (in English).

##### proc_info[process,<attribute>,<type>]

  
Various information about specific process(es).  
Return value: _Float_.

Parameters:

  * **process** \- the process name;  

  * **attribute** \- the requested process attribute;  

  * **type** \- the representation type (meaningful when more than one process with the same name exists)

Comments:

  * The following `attributes` are supported:  
_vmsize_ (default) - size of process virtual memory in Kbytes  
 _wkset_ \- size of process working set (amount of physical memory used by process) in Kbytes  
 _pf_ \- number of page faults  
 _ktime_ \- process kernel time in milliseconds  
 _utime_ \- process user time in milliseconds  
 _io_read_b_ \- number of bytes read by process during I/O operations  
 _io_read_op_ \- number of read operation performed by process  
 _io_write_b_ \- number of bytes written by process during I/O operations  
 _io_write_op_ \- number of write operation performed by process  
 _io_other_b_ \- number of bytes transferred by process during operations other than read and write operations  
 _io_other_op_ \- number of I/O operations performed by process, other than read and write operations  
 _gdiobj_ \- number of GDI objects used by process  
 _userobj_ \- number of USER objects used by process;  

  * Valid `types` are:  
_avg_ (default) - average value for all processes named <process>  
_min_ \- minimum value among all processes named <process>  
_max_ \- maximum value among all processes named <process>  
_sum_ \- sum of values for all processes named <process>;
  * On a 64-bit system, a 64-bit Zabbix agent is required for this item to work correctly.  

Examples:
    
    
    proc_info[iexplore.exe,wkset,sum] #retrieve the amount of physical memory taken by all Internet Explorer processes
           proc_info[iexplore.exe,pf,avg] #retrieve the average number of page faults for Internet Explorer processes

Copy

✔ Copied

##### registry.data[key,<value name>]

  
Return data for the specified value name in the Windows Registry key.  
Return value: _Integer_ , _string_ or _text_ (depending on the value type)

Parameters:

  * **key** \- the registry key including the root key; root abbreviations (e.g. HKLM) are allowed;
  * **value name** \- the registry value name in the key (empty string "" by default). The default value is returned if the value name is not supplied.

Comments:

  * Supported root abbreviations:  
HKCR - HKEY_CLASSES_ROOT  
HKCC - HKEY_CURRENT_CONFIG  
HKCU - HKEY_CURRENT_USER  
HKCULS - HKEY_CURRENT_USER_LOCAL_SETTINGS  
HKLM - HKEY_LOCAL_MACHINE  
HKPD - HKEY_PERFORMANCE_DATA  
HKPN - HKEY_PERFORMANCE_NLSTEXT  
HKPT - HKEY_PERFORMANCE_TEXT  
HKU - HKEY_USERS  

  * Keys with spaces must be double-quoted.

Examples:
    
    
    registry.data["HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\Windows Error Reporting"] #return the data of the default value of this key
           registry.data["HKLM\SOFTWARE\Microsoft\Windows\Windows Error Reporting","EnableZip"] #return the data of the value named "Enable Zip" in this key

Copy

✔ Copied

##### registry.get[key,<mode>,<name regexp>]

  
The list of Windows Registry values or keys located at given key.  
Return value: _JSON object_.

Parameters:

  * **key** \- the registry key including the root key; root abbreviations (e.g. HKLM) are allowed (see comments for registry.data[] to see full list of abbreviations);  

  * **mode** \- possible values:  
_values_ (default) or _keys_ ;  

  * **name regexp** \- only discover values with names that match the regexp (default - discover all values). Allowed only with _values_ as `mode`.

Keys with spaces must be double-quoted.

Examples:
    
    
    registry.get[HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall,values,"^DisplayName|DisplayVersion$"] #return the data of the values named "DisplayName" or "DisplayValue" in this key.
           The JSON will include details of the key, last subkey, value name, value type and value data.
           registry.get[HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall,values] #return the data of the all values in this key.
           The JSON will include details of the key, last subkey, value name, value type and value data.
           registry.get[HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall,keys] #return all subkeys of this key.
           The JSON will include details of the key and last subkey.

Copy

✔ Copied

##### service.discovery

  
The list of Windows services. Used for [low-level discovery](/documentation/current/en/manual/discovery/low_level_discovery/examples/windows_services).  
Return value: _JSON object_.

##### service.info[service,<param>]

  
Information about a service.  
Return value: _Integer_ \- with `param` as _state_ , _startup_ ; _String_ \- with `param` as _displayname_ , _path_ , _user_ ; _Text_ \- with `param` as _description_  
Specifically for _state_ : 0 - running, 1 - paused, 2 - start pending, 3 - pause pending, 4 - continue pending, 5 - stop pending, 6 - stopped, 7 - unknown, 255 - no such service  
Specifically for _startup_ : 0 - automatic, 1 - automatic delayed, 2 - manual, 3 - disabled, 4 - unknown, 5 - automatic trigger start, 6 - automatic delayed trigger start, 7 - manual trigger start

Parameters:

  * **service** \- a real service name or its display name as seen in the MMC Services snap-in;
  * **param** \- _state_ (default), _displayname_ , _path_ , _user_ , _startup_ , or _description_.

Comments:

  * Items like `service.info[service,state]` and `service.info[service]` will return the same information;
  * Only with `param` as _state_ this item returns a value for non-existing services (255).

Examples:
    
    
    service.info[SNMPTRAP] - state of the SNMPTRAP service;
           service.info[SNMP Trap] - state of the same service, but with the display name specified;
           service.info[EventLog,startup] - the startup type of the EventLog service

Copy

✔ Copied

##### services[<type>,<state>,<exclude>]

  
The listing of services.  
Return value: _0_ \- if empty; _Text_ \- the list of services separated by a newline.

Parameters:

  * **type** \- _all_ (default), _automatic_ , _manual_ , or _disabled_ ;
  * **state** \- _all_ (default), _stopped_ , _started_ , _start_pending_ , _stop_pending_ , _running_ , _continue_pending_ , _pause_pending_ , or _paused_ ;
  * **exclude** \- the services to exclude from the result. Excluded services should be listed in double quotes, separated by comma, without spaces.

Examples:
    
    
    services[,started] #returns the list of started services;
           services[automatic, stopped] #returns the list of stopped services that should be running;
           services[automatic, stopped, "service1,service2,service3"] #returns the list of stopped services that should be running, excluding services named "service1", "service2" and "service3"

Copy

✔ Copied

##### vm.vmemory.size[<type>]

  
The virtual memory size in bytes or in percentage from the total.  
Return value: _Integer_ \- for bytes; _float_ \- for percentage.

Parameter:

  * **type** \- possible values: _available_ (available virtual memory), _pavailable_ (available virtual memory, in percent), _pused_ (used virtual memory, in percent), _total_ (total virtual memory, default), or _used_ (used virtual memory)

Comments:

  * The monitoring of virtual memory statistics is based on:  

    * Total virtual memory on Windows (total physical + page file size);  

    * The maximum amount of memory Zabbix agent can commit;  

    * The current committed memory limit for the system or Zabbix agent, whichever is smaller.

Example:
    
    
    vm.vmemory.size[pavailable] #return the available virtual memory, in percentage

Copy

✔ Copied

##### wmi.get[<namespace>,<query>]

  
Execute a WMI query and return the first selected object.  
Return value: _Integer_ , _float_ , _string_ or _text_ (depending on the request).

Parameters:

  * **namespace** \- the WMI namespace;  

  * **query** \- the WMI query returning a single object.

WMI queries are performed with [WQL](https://en.wikipedia.org/wiki/WQL).

Example:
    
    
    wmi.get[root\cimv2,select status from Win32_DiskDrive where Name like '%PHYSICALDRIVE0%'] #returns the status of the first physical disk

Copy

✔ Copied

##### wmi.getall[<namespace>,<query>]

  
Execute a WMI query and return the whole response. Can be used for [low-level discovery](/documentation/current/en/manual/discovery/low_level_discovery/examples/wmi).  
Return value: _JSON object_

Parameters:

  * **namespace** \- the WMI namespace;  

  * **query** \- the WMI query.

Comments:

  * WMI queries are performed with [WQL](https://en.wikipedia.org/wiki/WQL).
  * JSONPath [preprocessing](/documentation/current/en/manual/config/items/item#item-value-preprocessing) can be used to point to more specific values in the returned JSON.

Example:
    
    
    wmi.getall[root\cimv2,select * from Win32_DiskDrive where Name like '%PHYSICALDRIVE%'] #returns status information of physical disks

Copy

✔ Copied

### Monitoring Windows services

This tutorial provides step-by-step instructions for setting up the monitoring of Windows services. It is assumed that Zabbix server and agent are configured and operational.

##### Step 1

Get the service name.

You can get the service name by going to the MMC Services snap-in and bringing up the properties of the service. In the _General_ tab you should see a field called "Service name". The value that follows is the name you will use when setting up an item for monitoring. For example, if you wanted to monitor the "workstation" service, then your service might be: **lanmanworkstation**.

##### Step 2

[Configure an item](/documentation/current/en/manual/config/items/item) for monitoring the service.

The item `service.info[service,<param>]` retrieves information about a particular service. Depending on the information you need, specify the `param` option which accepts the following values: _displayname_ , _state_ , _path_ , _user_ , _startup_ or _description_. The default value is _state_ if `param` is not specified (`service.info[service]`).

The type of return value depends on chosen `param`: integer for _state_ and _startup_ ; character string for _displayname_ , _path_ and _user_ ; text for _description_.

Example:

  * _Key:_ `service.info[lanmanworkstation]`
  * _Type of information:_ Numeric (unsigned)

The item `service.info[lanmanworkstation]` will retrieve information about the state of the service as a numerical value. To map a numerical value to a text representation in the frontend ("0" as "Running", "1" as "Paused", etc.), you can configure [value mapping](/documentation/current/en/manual/config/items/mapping#configuration) on the host on which the item is configured. To do this, either [link the template](/documentation/current/en/manual/config/templates/linking#linking-a-template) _Windows services by Zabbix agent_ or _Windows services by Zabbix agent active_ to the host, or configure on the host a new value map that is based on the _Windows service state_ value map configured on the mentioned templates.

Note that both of the mentioned templates have a discovery rule configured that will discover services automatically. If you do not want this, you can [disable the discovery rule](/documentation/current/en/manual/web_interface/frontend_sections/data_collection/hosts/discovery) on the host level once the template has been linked to the host.

### Discovery of Windows services

[Low-level discovery](/documentation/current/en/manual/discovery/low_level_discovery) provides a way to automatically create items, triggers, and graphs for different entities on a computer. Zabbix can automatically start monitoring Windows services on your machine, without the need to know the exact name of a service or create items for each service manually. A filter can be used to generate real items, triggers, and graphs only for services of interest.