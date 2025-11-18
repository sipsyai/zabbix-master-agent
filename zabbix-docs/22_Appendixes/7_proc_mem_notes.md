---
title: Notes on memtype parameter in proc.mem items
source: https://www.zabbix.com/documentation/current/en/manual/appendix/items/proc_mem_notes
downloaded: 2025-11-14 10:47:25
---

# 7 Notes on memtype parameter in proc.mem items

#### Overview

The **memtype** parameter is supported on Linux, AIX, FreeBSD, and Solaris platforms.

Three common values of 'memtype' are supported on all of these platforms: `pmem`, `rss` and `vsize`. Additionally, platform-specific 'memtype' values are supported on some platforms.

#### AIX

See values supported for 'memtype' parameter on AIX in the table.

vsize [1](proc_mem_notes#footnotes) | Virtual memory size | pi_size |   
---|---|---|---  
pmem | Percentage of real memory | pi_prm | ps -o pmem  
rss | Resident set size | pi_trss + pi_drss | ps -o rssize  
size | Size of process (code + data) | pi_dvm | "ps gvw" SIZE column  
dsize | Data size | pi_dsize  
tsize | Text (code) size | pi_tsize | "ps gvw" TSIZ column  
sdsize | Data size from shared library | pi_sdsize  
drss | Data resident set size | pi_drss |   
trss | Text resident set size | pi_trss |   
  
Notes for AIX:

  1. When choosing parameters for proc.mem[] item key on AIX, try to specify narrow process selection criteria. Otherwise there is a risk of getting unwanted processes counted into proc.mem[] result.

Example:
    
    
    $ zabbix_agentd -t proc.mem[,,,NonExistingProcess,rss]
           proc.mem[,,,NonExistingProcess,rss]           [u|2879488]

This example shows how specifying only command line (regular expression to match) parameter results in Zabbix agent self-accounting - probably not what you want.

  2. Do not use "ps -ef" to browse processes - it shows only non-kernel processes. Use "ps -Af" to see all processes which will be seen by Zabbix agent.

  3. Let's go through example of 'topasrec' how Zabbix agent proc.mem[] selects processes.

    
    
    $ ps -Af | grep topasrec
           root 10747984        1   0   Mar 16      -  0:00 /usr/bin/topasrec  -L -s 300 -R 1 -r 6 -o /var/perf daily/ -ypersistent=1 -O type=bin -ystart_time=04:08:54,Mar16,2023

proc.mem[] has arguments:
    
    
    proc.mem[<name>,<user>,<mode>,<cmdline>,<memtype>]

The 1st criterion is a process name (argument <name>). In our example Zabbix agent will see it as 'topasrec'. In order to match, you need to either specify 'topasrec' or to leave it empty. The 2nd criterion is a user name (argument <user>). To match, you need to either specify 'root' or to leave it empty. The 3rd criterion used in process selection is an argument <cmdline>. Zabbix agent will see its value as '/usr/bin/topasrec -L -s 300 -R 1 -r 6 -o /var/perf/daily/ -ypersistent=1 -O type=bin -ystart_time=04:08:54,Mar16,2023'. To match, you need to either specify a regular expression which matches this string or to leave it empty.

Arguments <mode> and <memtype> are applied after using the three criteria mentioned above.

#### FreeBSD

See values supported for 'memtype' parameter on FreeBSD in the table.

vsize | Virtual memory size | kp_eproc.e_vm.vm_map.size or ki_size | ps -o vsz  
---|---|---|---  
pmem | Percentage of real memory | calculated from rss | ps -o pmem  
rss | Resident set size | kp_eproc.e_vm.vm_rssize or ki_rssize | ps -o rss  
size [1](proc_mem_notes#footnotes) | Size of process (code + data + stack) | tsize + dsize + ssize |   
tsize | Text (code) size | kp_eproc.e_vm.vm_tsize or ki_tsize | ps -o tsiz  
dsize | Data size | kp_eproc.e_vm.vm_dsize or ki_dsize | ps -o dsiz  
ssize | Stack size | kp_eproc.e_vm.vm_ssize or ki_ssize | ps -o ssiz  
  
#### Linux

See values supported for 'memtype' parameter on Linux in the table.

vsize [1](proc_mem_notes#footnotes) | Virtual memory size | VmSize  
---|---|---  
pmem | Percentage of real memory | (VmRSS/total_memory) * 100  
rss | Resident set size | VmRSS  
data | Size of data segment | VmData  
exe | Size of code segment | VmExe  
hwm | Peak resident set size | VmHWM  
lck | Size of locked memory | VmLck  
lib | Size of shared libraries | VmLib  
peak | Peak virtual memory size | VmPeak  
pin | Size of pinned pages | VmPin  
pte | Size of page table entries | VmPTE  
size | Size of process code + data + stack segments | VmExe + VmData + VmStk  
stk | Size of stack segment | VmStk  
swap | Size of swap space used | VmSwap  
  
Notes for Linux:

  1. Not all 'memtype' values are supported by older Linux kernels. For example, Linux 2.4 kernels do not support `hwm`, `pin`, `peak`, `pte` and `swap` values.
  2. We have noticed that self-monitoring of the Zabbix agent active check process with `proc.mem[...,...,...,...,data]` shows a value that is 4 kB larger than reported by `VmData` line in the agent's /proc/<pid>/status file. At the time of self-measurement the agent's data segment increases by 4 kB and then returns to the previous size.

#### Solaris

See values supported for 'memtype' parameter on Solaris in the table.

vsize [1](proc_mem_notes#footnotes) | Size of process image | pr_size | ps -o vsz  
---|---|---|---  
pmem | Percentage of real memory | pr_pctmem | ps -o pmem  
rss | Resident set size  
It may be underestimated - see rss description in "man ps". | pr_rssize | ps -o rss  
  
##### Footnotes

**1** Default value.