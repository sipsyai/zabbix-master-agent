---
title: Minimum permission level for Windows agent items
source: https://www.zabbix.com/documentation/current/en/manual/appendix/items/win_permissions
downloaded: 2025-11-14 10:47:21
---

# 3 Minimum permission level for Windows agent items

#### Overview

When monitoring systems using an agent, a good practice is to obtain metrics from the host on which the agent is installed. To use the principle of least privilege, it is necessary to determine what metrics are obtained from the agent.

The table in this document allows you to select the minimum rights for guaranteed correct operation of Zabbix agent.

If a different user is selected for the agent to work, rather than 'LocalSystem', then for the operation of agent as a Windows service, the new user must have the rights "Log on as a service" from "Local Policy→User Rights Assignment" and the right to create, write and delete the Zabbix agent log file. An Active Directory user must be added to the _Performance Monitor Users_ group.

When working with the rights of an agent based on the "minimum technically acceptable" group, prior provision of rights to objects for monitoring is required.

#### Common agent items supported on Windows

| Recommended | Minimum technically acceptable (functionality is limited)  
---|---|---  
agent.hostname | Guests | Guests  
agent.ping | Guests | Guests  
agent.variant | Guests | Guests  
agent.version | Guests | Guests  
log | Administrators | Guests  
log.count | Administrators | Guests  
logrt | Administrators | Guests  
logrt.count | Administrators | Guests  
net.dns | Guests | Guests  
net.dns.perf | Guests | Guests  
net.dns.record | Guests | Guests  
net.if.discovery | Guests | Guests  
net.if.in | Guests | Guests  
net.if.out | Guests | Guests  
net.if.total | Guests | Guests  
net.tcp.listen | Guests | Guests  
net.tcp.port | Guests | Guests  
net.tcp.service | Guests | Guests  
net.tcp.service.perf | Guests | Guests  
net.udp.service | Guests | Guests  
net.udp.service.perf | Guests | Guests  
proc.num | Administrators | Guests  
system.cpu.discovery | Performance Monitor Users | Performance Monitor Users  
system.cpu.load | Performance Monitor Users | Performance Monitor Users  
system.cpu.num | Guests | Guests  
system.cpu.util | Performance Monitor Users | Performance Monitor Users  
system.hostname | Guests | Guests  
system.localtime | Guests | Guests  
system.run | Administrators | Guests  
system.sw.arch | Guests | Guests  
system.swap.size | Guests | Guests  
system.uname | Guests | Guests  
system.uptime | Performance Monitor Users | Performance Monitor Users  
vfs.dir.count | Administrators | Guests  
vfs.dir.get | Administrators | Guests  
vfs.dir.size | Administrators | Guests  
vfs.file.cksum | Administrators | Guests  
vfs.file.contents | Administrators | Guests  
vfs.file.exists | Administrators | Guests  
vfs.file.md5sum | Administrators | Guests  
vfs.file.regexp | Administrators | Guests  
vfs.file.regmatch | Administrators | Guests  
vfs.file.size | Administrators | Guests  
vfs.file.time | Administrators | Guests  
vfs.fs.discovery | Administrators | Guests  
vfs.fs.size | Administrators | Guests  
vfs.fs.get | Administrators | Guests  
vm.memory.size | Guests | Guests  
web.page.get | Guests | Guests  
web.page.perf | Guests | Guests  
web.page.regexp | Guests | Guests  
zabbix.stats | Guests | Guests  
  
#### Windows-specific item keys

| Recommended | Minimum technically acceptable (functionality is limited)  
---|---|---  
eventlog | Event Log Readers | Guests  
net.if.list | Guests | Guests  
perf_counter | Performance Monitor Users | Performance Monitor Users  
proc_info | Administrators | Guests  
service.discovery | Guests | Guests  
service.info | Guests | Guests  
services | Guests | Guests  
wmi.get | Administrators | Guests  
vm.vmemory.size | Guests | Guests