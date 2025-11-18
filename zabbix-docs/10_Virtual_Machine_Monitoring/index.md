---
title: Virtual machine monitoring
source: https://www.zabbix.com/documentation/current/en/manual/vm_monitoring
downloaded: 2025-11-14 10:36:56
---

# 10 Virtual machine monitoring

#### Overview

Zabbix can use [low-level discovery](/documentation/current/en/manual/discovery/low_level_discovery) rules to automatically discover VMware hypervisors and virtual machines, and create hosts to monitor them based on pre-defined [host prototypes](/documentation/current/en/manual/discovery/low_level_discovery/host_prototypes).

Zabbix also includes [ready-to-use templates](/documentation/current/en/manual/config/templates_out_of_the_box/vmware) for monitoring VMware vCenter or ESXi hypervisors.

The minimum required VMware vCenter or vSphere version is 5.1.

#### Data collection

Virtual machine monitoring consists of two steps:

  1. Zabbix _vmware collector_ processes collect virtual machine data - the processes obtain necessary information from VMware web services over the SOAP protocol, pre-process it, and store it in Zabbix server shared memory.

  2. Zabbix _poller_ processes retrieve data using Zabbix simple check [VMware monitoring item keys](/documentation/current/en/manual/vm_monitoring/vmware_keys).

Zabbix divides collected data into VMware configuration data and VMware performance counter data. Both types of data are collected independently by the _vmware collector_ processes.

The following statistics are available based on the VMware performance counter information:

  * Datastore
  * Disk device
  * CPU
  * Power
  * Network interface
  * Custom performance counter items

For the complete list of items that obtain data from VMware performance counters, see [_VMware monitoring item keys_](/documentation/current/en/manual/vm_monitoring/vmware_keys#footnotes).

Note that the frequency of VMware event retrieval depends on the polling interval of [vmware.eventlog](/documentation/current/en/manual/vm_monitoring/vmware_keys#vmware.eventlog), but cannot be less then 5 seconds.

#### Configuration

If Zabbix server is compiled from [sources](/documentation/current/en/manual/installation/install#configure-the-sources), it must be compiled with the `--with-libcurl --with-libxml2` configuration options to enable virtual machine monitoring. Zabbix packages are compiled with these options already enabled.

The following Zabbix server configuration file parameters can be modified for virtual machine monitoring:

  * [`StartVMwareCollectors`](/documentation/current/en/manual/appendix/config/zabbix_server#startvmwarecollectors)

It is recommended to enable more collectors than the number of monitored VMware services; otherwise, the retrieval of VMware performance counter statistics might be delayed by the retrieval of VMware configuration data (which takes a while for large installations).   
  
Generally, the value of `StartVMwareCollectors` should not dip below `2` and should not exceed twice the amount of monitored VMware services: Amount of services < `StartVMwareCollectors` < (Amount of services * 2). For example, when monitoring one VMware service, set `StartVMwareCollectors` to `2`; when monitoring three services, set `StartVMwareCollectors` to `5`.   
  
Note that the required number of collectors also depends on the scope of the VMware environment, and the `VMwareFrequency` and `VMwarePerfFrequency` configuration parameters.

  * [`VMwareCacheSize`](/documentation/current/en/manual/appendix/config/zabbix_server#vmwarecachesize)
  * [`VMwareFrequency`](/documentation/current/en/manual/appendix/config/zabbix_server#vmwarefrequency)
  * [`VMwarePerfFrequency`](/documentation/current/en/manual/appendix/config/zabbix_server#vmwareperffrequency)
  * [`VMwareTimeout`](/documentation/current/en/manual/appendix/config/zabbix_server#vmwaretimeout)

To support datastore capacity metrics, ensure that the value of the VMware `vpxd.stats.maxQueryMetrics` key is set to at least `64`. For more information, see the [_VMware Knowledge Base_ article](https://kb.vmware.com/s/article/2107096).

##### Discovery

Zabbix can use low-level discovery rules (for example, _vmware.hv.discovery[{$VMWARE.URL}]_) to automatically discover VMware hypervisors and virtual machines. Moreover, Zabbix can use host prototypes to automatically generate real hosts for the discovered entities. For more information, see [_Host prototypes_](/documentation/current/en/manual/discovery/low_level_discovery/host_prototypes).

##### Configuration examples

For a basic example of how to set up Zabbix for monitoring VMware using the _VMware FQDN_ template, see [_Monitor VMware with Zabbix_](/documentation/current/en/manual/guides/monitor_vmware).

For a more detailed example of how to create a host, a low-level discovery rule, and a host prototype for monitoring VMware, see [_Setup example_](/documentation/current/en/manual/vm_monitoring/example).

#### Extended logging

The data collected by the _vmware collector_ processes can be logged for detailed debugging using debug level 5. The debug level can be configured in the [server](/documentation/current/en/manual/appendix/config/zabbix_server#debuglevel) and [proxy](/documentation/current/en/manual/appendix/config/zabbix_proxy#debuglevel) configuration files or using the runtime control option `-R log_level_increase="vmware collector,N"`, where "N" is the process number.

For example, to increase the debug level from 4 to 5 for all _vmware collector_ processes, run the following command:
    
    
    zabbix_server -R log_level_increase="vmware collector"

Copy

✔ Copied

To increase the debug level from 4 to 5 for the second _vmware collector_ process, run the following command:
    
    
    zabbix_server -R log_level_increase="vmware collector,2"

Copy

✔ Copied

When extended logging of VMware collector data is no longer required, it is recommended to decrease the debug level to default (3) by running the `-R log_level_decrease` command.

#### Troubleshooting

  * In case of unavailable metrics, please ensure that they are not made unavailable or turned off by default in recent VMware vSphere versions, or if some limits are not placed on performance-metric database queries. For more information, see [ZBX-12094](https://support.zabbix.com/browse/ZBX-12094).
  * If `config.vpxd.stats.maxQueryMetrics` is invalid or exceeds the maximum number of characters permitted error, add a `config.vpxd.stats.maxQueryMetrics` parameter to the vCenter Server settings. The value of this parameter should be the same as the value of `maxQuerysize` in VMware's _web.xml_ file. For more information, see [_VMware Knowledge Base_ article](https://kb.vmware.com/s/article/2107096).
  * If you suspect your Zabbix installation is using too much memory, see [Profiling excessive memory usage with tcmalloc](/documentation/current/en/manual/installation/known_issues#profiling-excessive-memory-usage-with-tcmalloc).