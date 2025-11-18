---
title: proc.get parameters
source: https://www.zabbix.com/documentation/current/en/manual/appendix/items/proc_get
downloaded: 2025-11-14 10:47:28
---

# 10 proc.get parameters

#### Overview

The item [**proc.get**[<name>,<user>,<cmdline>,<mode>]](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#proc.get) is supported on Linux, Windows, FreeBSD, OpenBSD, and NetBSD.

List of process parameters returned by the item varies depending on the operating system and 'mode' argument value.

#### Linux

The following process parameters are returned on Linux for each mode:

pid: PID | pid: PID | name: process name  
---|---|---  
ppid: parent PID | ppid: parent PID | processes: number of processes  
name: process name | name: process name | vsize: virtual memory size  
cmdline: command with arguments | user: user (real) the process runs under | pmem: percentage of real memory  
user: user (real) the process runs under | group: group (real) the process runs under | rss: resident set size  
group: group (real) the process runs under | uid: user ID | data: size of data segment  
uid: user ID | gid: ID of the group the process runs under | exe: size of code segment  
gid: ID of the group the process runs under | tid: thread ID | lib: size of shared libraries  
vsize: virtual memory size | tname: thread name | lck: size of locked memory  
pmem: percentage of real memory | cputime_user: total CPU seconds (user) | pin: size of pinned pages  
rss: resident set size | cputime_system: total CPU seconds (system) | pte: size of page table entries  
data: size of data segment | state: thread state | size: size of process code + data + stack segments  
exe: size of code segment | ctx_switches: number of context switches | stk: size of stack segment  
hwm: peak resident set size | page_faults: number of page faults | swap: size of swap space used  
lck: size of locked memory |  | cputime_user: total CPU seconds (user)  
lib: size of shared libraries |  | cputime_system: total CPU seconds (system)  
peak: peak virtual memory size |  | ctx_switches: number of context switches  
pin: size of pinned pages |  | threads: number of threads  
pte: size of page table entries |  | page_faults: number of page faults  
size: size of process code + data + stack segments |  | pss: proportional set size memory  
stk: size of stack segment |  |   
swap: size of swap space used |  |   
cputime_user: total CPU seconds (user) |  |   
cputime_system: total CPU seconds (system) |  |   
state: process state (transparently retrieved from procfs, long form) |  |   
ctx_switches: number of context switches |  |   
threads: number of threads |  |   
page_faults: number of page faults |  |   
pss: proportional set size memory |  |   
  
#### BSD-based OS

The following process parameters are returned on FreeBSD, OpenBSD, and NetBSD for each mode:

pid: PID | pid: PID | name: process name  
---|---|---  
ppid: parent PID | ppid: parent PID | processes: number of processes  
jid: ID of jail (FreeBSD only) | jid: ID of jail (FreeBSD only) | vsize: virtual memory size  
jname: name of jail (FreeBSD only) | jname: name of jail (FreeBSD only) | pmem: percentage of real memory (FreeBSD only)  
name: process name | name: process name | rss: resident set size  
cmdline: command with arguments | user: user (real) the process runs under | size: size of process (code + data + stack)  
user: user (real) the process runs under | group: group (real) the process runs under | tsize: text (code) size  
group: group (real) the process runs under | uid: user ID | dsize: data size  
uid: user ID | gid: ID of the group the process runs under | ssize: stack size  
gid: ID of the group the process runs under | tid: thread ID | cputime_user: total CPU seconds (user)  
vsize: virtual memory size | tname: thread name | cputime_system: total CPU seconds (system)  
pmem: percentage of real memory (FreeBSD only) | cputime_user: total CPU seconds (user) | ctx_switches: number of context switches  
rss: resident set size | cputime_system: total CPU seconds (system) | threads: number of threads (not supported for NetBSD)  
size: size of process (code + data + stack) | state: thread state | stk: size of stack segment  
tsize: text (code) size | ctx_switches: number of context switches | page_faults: number of page faults  
dsize: data size | io_read_op: number of times the system had to perform input | fds: number of file descriptors (OpenBSD only)  
ssize: stack size | io_write_op: number of times the system had to perform output | swap: size of swap space used  
cputime_user: total CPU seconds (user) |  | io_read_op: number of times the system had to perform input  
cputime_system: total CPU seconds (system) |  | io_write_op: number of times the system had to perform output  
state: process state (disk sleep/running/sleeping/tracing stop/zombie/other) |  |   
ctx_switches: number of context switches |  |   
threads: number of threads (not supported for NetBSD) |  |   
page_faults: number of page faults |  |   
fds: number of file descriptors (OpenBSD only) |  |   
swap: size of swap space used |  |   
io_read_op: number of times the system had to perform input |  |   
io_write_op: number of times the system had to perform output |  |   
  
#### Windows

The following process parameters are returned on Windows for each mode:

pid: PID | pid: PID | name: process name  
---|---|---  
ppid: parent PID | ppid: parent PID | processes: number of processes  
name: process name | name: process name | vmsize: virtual memory size  
user: user the process runs under | user: user the process runs under | wkset: size of process working set  
sid: user SID | sid: user SID | cputime_user: total CPU seconds (user)  
vmsize: virtual memory size | tid: thread ID | cputime_system: total CPU seconds (system)  
wkset: size of process working set |  | threads: number of threads  
cputime_user: total CPU seconds (user) |  | page_faults: number of page faults  
cputime_system: total CPU seconds (system) |  | handles: number of handles  
threads: number of threads |  | io_read_b: IO bytes read  
page_faults: number of page faults |  | io_write_b: IO bytes written  
handles: number of handles |  | io_read_op: IO read operations  
io_read_b: IO bytes read |  | io_write_op: IO write operations  
io_write_b: IO bytes written |  | io_other_b: IO bytes transferred, other than read and write operations  
io_read_op: IO read operations |  | io_other_op: IO operations, other than read and write operations  
io_write_op: IO write operations |  |   
io_other_b: IO bytes transferred, other than read and write operations |  |   
io_other_op: IO operations, other than read and write operations |  |