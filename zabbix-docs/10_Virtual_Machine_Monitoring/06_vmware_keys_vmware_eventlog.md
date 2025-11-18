---
title: vmware.eventlog
source: https://www.zabbix.com/documentation/current/en/manual/vm_monitoring/vmware_keys#vmware.eventlog
downloaded: 2025-11-14 10:37:02
---

# 1 VMware monitoring item keys

### Overview

This page provides details on the simple checks that can be used to monitor [VMware environments](/documentation/current/en/manual/vm_monitoring). The metrics are grouped by the monitoring target.

### Supported item keys

The item keys are listed without parameters and additional information. Click on the item key to see the full details.

vmware.eventlog | The VMware event log. | General service  
---|---|---  
vmware.fullname | The VMware service full name.  
vmware.version | The VMware service version.  
vmware.cl.perfcounter | The VMware cluster performance counter metrics. | Cluster  
vmware.cluster.alarms.get | The VMware cluster alarms data.  
vmware.cluster.discovery | The discovery of VMware clusters.  
vmware.cluster.property | The VMware cluster property.  
vmware.cluster.status | The VMware cluster status.  
vmware.cluster.tags.get | The VMware cluster tags array.  
vmware.datastore.alarms.get | The VMware datastore alarms data. | Datastore  
vmware.datastore.discovery | The discovery of VMware datastores.  
vmware.datastore.hv.list | The list of datastore hypervisors.  
vmware.datastore.perfcounter | The VMware datastore performance counter value.  
vmware.datastore.property | The VMware datastore property.  
vmware.datastore.read | The amount of time for a read operation from the datastore.  
vmware.datastore.size | The VMware datastore space in bytes or in percentage from total.  
vmware.datastore.tags.get | The VMware datastore tags array.  
vmware.datastore.write | The amount of time for a write operation to the datastore.  
vmware.dc.alarms.get | The VMware datacenter alarms data. | Datacenter  
vmware.dc.discovery | The discovery of VMware datacenters.  
vmware.dc.tags.get | The VMware datacenter tags array.  
vmware.dvswitch.discovery | The discovery of VMware vSphere Distributed Switches. | vSphere Distributed Switch  
vmware.dvswitch.fetchports.get | The VMware vSphere Distributed Switch ports data.  
vmware.hv.alarms.get | The VMware hypervisor alarms data. | Hypervisor  
vmware.hv.cluster.name | The VMware hypervisor cluster name.  
vmware.hv.connectionstate | The VMware hypervisor connection state.  
vmware.hv.cpu.usage | The VMware hypervisor processor usage (Hz).  
vmware.hv.cpu.usage.perf | The VMware hypervisor processor usage as a percentage during the interval.  
vmware.hv.cpu.utilization | The VMware hypervisor processor usage as a percentage during the interval, depends on power management or HT.  
vmware.hv.datacenter.name | The VMware hypervisor datacenter name.  
vmware.hv.datastore.discovery | The discovery of VMware hypervisor datastores.  
vmware.hv.datastore.list | The list of VMware hypervisor datastores.  
vmware.hv.datastore.multipath | The number of available datastore paths.  
vmware.hv.datastore.read | The average amount of time for a read operation from the datastore.  
vmware.hv.datastore.size | The VMware datastore space in bytes or in percentage from total.  
vmware.hv.datastore.write | The average amount of time for a write operation to the datastore.  
vmware.hv.discovery | The discovery of VMware hypervisors.  
vmware.hv.diskinfo.get | The VMware hypervisor disk data.  
vmware.hv.fullname | The VMware hypervisor name.  
vmware.hv.hw.cpu.freq | The VMware hypervisor processor frequency.  
vmware.hv.hw.cpu.model | The VMware hypervisor processor model.  
vmware.hv.hw.cpu.num | The number of processor cores on VMware hypervisor.  
vmware.hv.hw.cpu.threads | The number of processor threads on VMware hypervisor.  
vmware.hv.hw.memory | The VMware hypervisor total memory size.  
vmware.hv.hw.model | The VMware hypervisor model.  
vmware.hv.hw.sensors.get | The VMware hypervisor hardware sensors value.  
vmware.hv.hw.serialnumber | The VMware hypervisor serial number.  
vmware.hv.hw.uuid | The VMware hypervisor BIOS UUID.  
vmware.hv.hw.vendor | The VMware hypervisor vendor name.  
vmware.hv.maintenance | The VMware hypervisor maintenance status.  
vmware.hv.memory.size.ballooned | The VMware hypervisor ballooned memory size.  
vmware.hv.memory.used | The VMware hypervisor used memory size.  
vmware.hv.net.if.discovery | The discovery of VMware hypervisor network interfaces.  
vmware.hv.network.in | The VMware hypervisor network input statistics.  
vmware.hv.network.linkspeed | The VMware hypervisor network interface speed.  
vmware.hv.network.out | The VMware hypervisor network output statistics.  
vmware.hv.perfcounter | The VMware hypervisor performance counter value.  
vmware.hv.property | The VMware hypervisor property.  
vmware.hv.power | The VMware hypervisor power usage.  
vmware.hv.sensor.health.state | The VMware hypervisor health state rollup sensor.  
vmware.hv.sensors.get | The VMware hypervisor HW vendor state sensors.  
vmware.hv.status | The VMware hypervisor status.  
vmware.hv.tags.get | The VMware hypervisor tags array.  
vmware.hv.uptime | The VMware hypervisor uptime.  
vmware.hv.version | The VMware hypervisor version.  
vmware.hv.vm.num | The number of virtual machines on the VMware hypervisor.  
vmware.rp.cpu.usage | The CPU usage in hertz during the interval on VMware Resource Pool. | Resource pool  
vmware.rp.memory | The memory metrics of VMware resource pool.  
vmware.alarms.get | The VMware virtual center alarms data. | Virtual center  
vmware.vm.alarms.get | The VMware virtual machine alarms data. | Virtual machine  
vmware.vm.attribute | The VMware virtual machine custom attribute value.  
vmware.vm.cluster.name | The VMware virtual machine name.  
vmware.vm.consolidationneeded | The VMware virtual machine disk requires consolidation.  
vmware.vm.cpu.latency | The percentage of time the virtual machine is unable to run because it is contending for access to the physical CPU(s).  
vmware.vm.cpu.num | The number of processors on VMware virtual machine.  
vmware.vm.cpu.readiness | The percentage of time that the virtual machine was ready, but could not get scheduled to run on the physical CPU.  
vmware.vm.cpu.ready | The time that the virtual machine was ready, but could not get scheduled to run on the physical CPU.  
vmware.vm.cpu.swapwait | The percentage of CPU time spent waiting for swap-in.  
vmware.vm.cpu.usage | The VMware virtual machine processor usage (Hz).  
vmware.vm.cpu.usage.perf | The VMware virtual machine processor usage as a percentage during the interval.  
vmware.vm.datacenter.name | The VMware virtual machine datacenter name.  
vmware.vm.discovery | The discovery of VMware virtual machines.  
vmware.vm.guest.memory.size.swapped | The amount of guest physical memory that is swapped out to the swap space.  
vmware.vm.guest.osuptime | The total time elapsed since the last operating system boot-up.  
vmware.vm.hv.maintenance | The VMware virtual machine hypervisor maintenance status.  
vmware.vm.hv.name | The VMware virtual machine hypervisor name.  
vmware.vm.memory.size | The VMware virtual machine total memory size.  
vmware.vm.memory.size.ballooned | The VMware virtual machine ballooned memory size.  
vmware.vm.memory.size.compressed | The VMware virtual machine compressed memory size.  
vmware.vm.memory.size.consumed | The amount of host physical memory consumed for backing up guest physical memory pages.  
vmware.vm.memory.size.private | The VMware virtual machine private memory size.  
vmware.vm.memory.size.shared | The VMware virtual machine shared memory size.  
vmware.vm.memory.size.swapped | The VMware virtual machine swapped memory size.  
vmware.vm.memory.size.usage.guest | The VMware virtual machine guest memory usage.  
vmware.vm.memory.size.usage.host | The VMware virtual machine host memory usage.  
vmware.vm.memory.usage | The percentage of host physical memory that has been consumed.  
vmware.vm.net.if.discovery | The discovery of VMware virtual machine network interfaces.  
vmware.vm.net.if.in | The VMware virtual machine network interface input statistics.  
vmware.vm.net.if.out | The VMware virtual machine network interface output statistics.  
vmware.vm.net.if.usage | The VMware virtual machine network utilization during the interval.  
vmware.vm.perfcounter | The VMware virtual machine performance counter value.  
vmware.vm.powerstate | The VMware virtual machine power state.  
vmware.vm.property | The VMware virtual machine property.  
vmware.vm.snapshot.get | The VMware virtual machine snapshot state.  
vmware.vm.state | The VMware virtual machine state.  
vmware.vm.storage.committed | The VMware virtual machine committed storage space.  
vmware.vm.storage.readoio | The average number of outstanding read requests to the virtual disk during the collection interval.  
vmware.vm.storage.totalreadlatency | The average time a read from the virtual disk takes.  
vmware.vm.storage.totalwritelatency | The average time a write to the virtual disk takes.  
vmware.vm.storage.uncommitted | The VMware virtual machine uncommitted storage space.  
vmware.vm.storage.unshared | The VMware virtual machine unshared storage space.  
vmware.vm.storage.writeoio | The average number of outstanding write requests to the virtual disk during the collection interval.  
vmware.vm.tags.get | The VMware virtual machine tags array.  
vmware.vm.tools | The VMware virtual machine guest tools state or version.  
vmware.vm.uptime | The VMware virtual machine uptime.  
vmware.vm.vfs.dev.discovery | The discovery of VMware virtual machine disk devices.  
vmware.vm.vfs.dev.read | The VMware virtual machine disk device read statistics.  
vmware.vm.vfs.dev.write | The VMware virtual machine disk device write statistics.  
vmware.vm.vfs.fs.discovery | The discovery of VMware virtual machine file systems.  
vmware.vm.vfs.fs.size | The VMware virtual machine file system statistics.  
  
### Item key details

Parameters without angle brackets are mandatory. Parameters marked with angle brackets **<** **>** are optional.

##### vmware.eventlog[url,<mode>,<severity>]

  
The VMware event log.  
Return value: _Log_.

Parameters:

  * **url** \- the VMware service URL;
  * **mode** \- _all_ (default) or _skip_ \- skip the processing of older data;
  * **severity** \- filter by severity: _error_ , _warning_ , _info_ or _user_. This parameter must be quoted if more than one severity is specified in a comma-delimited list (e.g.`"error,warning,info,user"`). Disabled by default.

Comments:

  * There must be only one `vmware.eventlog` item key per URL;
  * See also [example of filtering](/documentation/current/en/manual/config/items/preprocessing/examples#filtering-vmware-event-log-records) VMware event log records.

##### vmware.fullname[url]

  
The VMware service full name.  
Return value: _String_.

Parameters:

  * **url** \- the VMware service URL.

##### vmware.version[url]

  
The VMware service version.  
Return value: _String_.

Parameters:

  * **url** \- the VMware service URL.

##### vmware.cl.perfcounter[url,id,path,<instance>]

  
The VMware cluster performance counter metrics.  
Return value: _Integer_.

Parameters:

  * **url** \- the VMware service URL;
  * **id** \- the VMware cluster ID. `id` can be received from `vmware.cluster.discovery[]` as {#CLUSTER.ID}.
  * **path** \- the performance counter path**[1](vmware_keys#footnotes)** ;
  * **instance** \- the performance counter instance.

##### vmware.cluster.alarms.get[url,id]

  
The VMware cluster alarms data.  
Return value: [JSON object](/documentation/current/en/manual/vm_monitoring/vmware_json#vmware..alarms.get).

Parameters:

  * **url** \- the VMware service URL;
  * **id** \- the VMware cluster ID.

##### vmware.cluster.discovery[url]

  
The discovery of VMware clusters.  
Return value: [JSON object](/documentation/current/en/manual/vm_monitoring/discovery_fields).

Parameters:

  * **url** \- the VMware service URL.

##### vmware.cluster.property[url,id,prop]

  
The VMware cluster property.  
Return value: _String_.

Parameters:

  * **url** \- the VMware service URL;
  * **id** \- the VMware cluster ID;
  * **prop** \- the property path which is the name of a property of the VM object as defined in the [VMware SDK](https://vdc-repo.vmware.com/vmwb-repository/dcr-public/1ef6c336-7bef-477d-b9bb-caa1767d7e30/82521f49-9d9a-42b7-b19b-9e6cd9b30db1/vim.VirtualMachine.html).

Examples:
    
    
    vmware.vm.property[{$VMWARE.URL},{$VMWARE.VM.UUID},overallStatus]
           vmware.vm.property[{$VMWARE.URL},{$VMWARE.VM.UUID},runtime.powerState]

Copy

✔ Copied

##### vmware.cluster.status[url,name]

  
The VMware cluster status.  
Return value: _0_ \- gray; _1_ \- green; _2_ \- yellow; _3_ \- red.

Parameters:

  * **url** \- the VMware service URL;
  * **name** \- the VMware cluster name.

##### vmware.cluster.tags.get[url,id]

  
The VMware cluster tags array.  
Return value: [JSON object](/documentation/current/en/manual/vm_monitoring/vmware_json#vmware..tags.get).

Parameters:

  * **url** \- the VMware service URL;
  * **id** \- the VMware cluster ID.

This item works with vSphere 6.5 and newer.

##### vmware.datastore.alarms.get[url,uuid]

  
The VMware datastore alarms data.  
Return value: [JSON object](/documentation/current/en/manual/vm_monitoring/vmware_json#vmware..alarms.get).

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware datastore global unique identifier.

##### vmware.datastore.discovery[url,<filter_uuid>]

  
The discovery of VMware datastores.  
Return value: [JSON object](/documentation/current/en/manual/vm_monitoring/discovery_fields).

Parameters:

  * **url** \- the VMware service URL;
  * **filter_uuid** \- a single HV or VM unique identifier (default: empty). If specified, only linked datastores will be discovered.

##### vmware.datastore.hv.list[url,datastore]

  
The list of datastore hypervisors.  
Return value: _String_.

Parameters:

  * **url** \- the VMware service URL;
  * **datastore** \- the datastore UUID or name.

Output example:
    
    
    esx7-01-host.zabbix.sandbox
           esx7-02-host.zabbix.sandbox

Copy

✔ Copied

##### vmware.datastore.perfcounter[url,uuid,path,<instance>]

  
The VMware datastore performance counter value.  
Return value: _Integer_ **[2](vmware_keys#footnotes)**.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware datastore global unique identifier;
  * **path** \- the performance counter path**[1](vmware_keys#footnotes)** ;
  * **instance** \- the performance counter instance. Use empty instance for aggregate values (default). `instance` can be received from `vmware.datastore.discovery[]` as part of the {#DATASTORE.EXTENT} array.

##### vmware.datastore.property[url,uuid,prop]

  
The VMware datastore property.  
Return value: _String_.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware datastore global unique identifier;
  * **prop** \- the property path.

##### vmware.datastore.read[url,datastore,<mode>]

  
The amount of time for a read operation from the datastore (milliseconds).  
Return value: _Integer_ **[2](vmware_keys#footnotes)**.

Parameters:

  * **url** \- the VMware service URL;
  * **datastore** \- the datastore UUID or name;
  * **mode** \- _latency_ (average value, default) or _maxlatency_ (maximum value).

##### vmware.datastore.size[url,datastore,<mode>]

  
The VMware datastore space in bytes or in percentage from total.  
Return value: _Integer_ \- for bytes; _Float_ \- for percentage.

Parameters:

  * **url** \- the VMware service URL;
  * **datastore** \- the datastore UUID or name;
  * **mode** \- possible values: _total_ (default), _free_ , _pfree_ (free percentage), _uncommitted_.

##### vmware.datastore.tags.get[url,uuid]

  
The VMware datastore tags array.  
Return value: [JSON object](/documentation/current/en/manual/vm_monitoring/vmware_json#vmware..tags.get).

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware datastore global unique identifier.

This item works with vSphere 6.5 and newer.

##### vmware.datastore.write[url,datastore,<mode>]

  
The amount of time for a write operation to the datastore (milliseconds).  
Return value: _Integer_ **[2](vmware_keys#footnotes)**.

Parameters:

  * **url** \- the VMware service URL;
  * **datastore** \- the datastore UUID or name;
  * **mode** \- _latency_ (average value, default) or _maxlatency_ (maximum value).

##### vmware.dc.alarms.get[url,id]

  
The VMware datacenter alarms data.  
Return value: [JSON object](/documentation/current/en/manual/vm_monitoring/vmware_json#vmware..alarms.get).

Parameters:

  * **url** \- the VMware service URL;
  * **id** \- the VMware datacenter ID.

##### vmware.dc.discovery[url]

  
The discovery of VMware datacenters.  
Return value: [JSON object](/documentation/current/en/manual/vm_monitoring/discovery_fields).

Parameters:

  * **url** \- the VMware service URL.

##### vmware.dc.tags.get[url,id]

  
The VMware datacenter tags array.  
Return value: [JSON object](/documentation/current/en/manual/vm_monitoring/vmware_json#vmware..tags.get).

Parameters:

  * **url** \- the VMware service URL;
  * **id** \- the VMware datacenter ID.

This item works with vSphere 6.5 and newer.

##### vmware.dvswitch.discovery[url]

  
The discovery of VMware vSphere Distributed Switches.  
Return value: [JSON object](/documentation/current/en/manual/vm_monitoring/discovery_fields).

Parameters:

  * **url** \- the VMware service URL.

##### vmware.dvswitch.fetchports.get[url,uuid,<filter>,<mode>]

  
The VMware vSphere Distributed Switch ports data.  
Return value: [JSON object](/documentation/current/en/manual/vm_monitoring/vmware_json#vmware.dvswitch.fetchports.get).

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware DVSwitch global unique identifier.
  * **filter** \- a single string with comma-separated criteria for selecting ports;
  * **mode** \- _state_ (all XML without "config" XML nodes, default) or _full_.

The **filter** parameter supports the [criteria](https://vdc-download.vmware.com/vmwb-repository/dcr-public/bf660c0a-f060-46e8-a94d-4b5e6ffc77ad/208bc706-e281-49b6-a0ce-b402ec19ef82/SDK/vsphere-ws/docs/ReferenceGuide/vim.dvs.PortCriteria.html) available in the VMware data object DistributedVirtualSwitchPortCriteria.

Example:
    
    
    vmware.dvswitch.fetchports.get[{$VMWARE.URL},{$VMWARE.DVS.UUID},"connected:true,active:true,uplinkPort:false,nsxPort:false,inside:true,host:host-1012",state]

Copy

✔ Copied

##### vmware.hv.alarms.get[url,uuid]

  
The VMware hypervisor alarms data.  
Return value: [JSON object](/documentation/current/en/manual/vm_monitoring/vmware_json#vmware..alarms.get).

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware hypervisor global unique identifier.

##### vmware.hv.cluster.name[url,uuid]

  
The VMware hypervisor cluster name.  
Return value: _String_.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware hypervisor global unique identifier.

##### vmware.hv.connectionstate[url,uuid]

  
The VMware hypervisor connection state.  
Return value: _String_ : _connected_ , _disconnected_ , or _notResponding_.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware hypervisor global unique identifier.

##### vmware.hv.cpu.usage[url,uuid]

  
The VMware hypervisor processor usage (Hz).  
Return value: _Integer_.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware hypervisor global unique identifier.

##### vmware.hv.cpu.usage.perf[url,uuid]

  
The VMware hypervisor processor usage as a percentage during the interval.  
Return value: _Float_.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware hypervisor global unique identifier.

##### vmware.hv.cpu.utilization[url,uuid]

  
The VMware hypervisor processor usage as a percentage during the interval, depends on power management or HT.  
Return value: _Float_.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware hypervisor global unique identifier.

##### vmware.hv.datacenter.name[url,uuid]

  
The VMware hypervisor datacenter name.  
Return value: _String_.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware hypervisor global unique identifier.

##### vmware.hv.datastore.discovery[url,uuid]

  
The discovery of VMware hypervisor datastores.  
Return value: [JSON object](/documentation/current/en/manual/vm_monitoring/discovery_fields).

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware hypervisor global unique identifier.

##### vmware.hv.datastore.list[url,uuid]

  
The list of VMware hypervisor datastores.  
Return value: _String_.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware hypervisor global unique identifier.

Output example:
    
    
    SSD-RAID1-VAULT1
           SSD-RAID1-VAULT2
           SSD-RAID10

Copy

✔ Copied

##### vmware.hv.datastore.multipath[url,uuid,<datastore>,<partitionid>]

  
The number of available datastore paths.  
Return value: _Integer_.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware hypervisor global unique identifier;
  * **datastore** \- the datastore UUID or name;
  * **partitionid** \- the internal ID of physical device from `vmware.hv.datastore.discovery`.

##### vmware.hv.datastore.read[url,uuid,datastore,<mode>]

  
The average amount of time for a read operation from the datastore (milliseconds).  
Return value: _Integer_ **[2](vmware_keys#footnotes)**.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware hypervisor global unique identifier;
  * **datastore** \- the datastore UUID or name;
  * **mode** \- _latency_ (default).

##### vmware.hv.datastore.size[url,uuid,datastore,<mode>]

  
The VMware datastore space in bytes or in percentage from total.  
Return value: _Integer_ \- for bytes; _Float_ \- for percentage.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware hypervisor global unique identifier;
  * **datastore** \- the datastore UUID or name;
  * **mode** \- possible values: _total_ (default), _free_ , _pfree_ (free percentage), _uncommitted_.

##### vmware.hv.datastore.write[url,uuid,datastore,<mode>]

  
The average amount of time for a write operation to the datastore (milliseconds).  
Return value: _Integer_ **[2](vmware_keys#footnotes)**.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware hypervisor global unique identifier;
  * **datastore** \- the datastore UUID or name;
  * **mode** \- _latency_ (default).

##### vmware.hv.discovery[url]

  
The discovery of VMware hypervisors.  
Return value: [JSON object](/documentation/current/en/manual/vm_monitoring/discovery_fields).

Parameters:

  * **url** \- the VMware service URL.

##### vmware.hv.diskinfo.get[url,uuid]

  
The VMware hypervisor disk data.  
Return value: [JSON object](/documentation/current/en/manual/vm_monitoring/vmware_json#vmware.hv.diskinfo.get).

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware hypervisor global unique identifier.

##### vmware.hv.fullname[url,uuid]

  
The VMware hypervisor name.  
Return value: _String_.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware hypervisor global unique identifier.

##### vmware.hv.hw.cpu.freq[url,uuid]

  
The VMware hypervisor processor frequency (Hz).  
Return value: _Integer_.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware hypervisor global unique identifier.

##### vmware.hv.hw.cpu.model[url,uuid]

  
The VMware hypervisor processor model.  
Return value: _String_.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware hypervisor global unique identifier.

##### vmware.hv.hw.cpu.num[url,uuid]

  
The number of processor cores on VMware hypervisor.  
Return value: _Integer_.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware hypervisor global unique identifier.

##### vmware.hv.hw.cpu.threads[url,uuid]

  
The number of processor threads on VMware hypervisor.  
Return value: _Integer_.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware hypervisor global unique identifier.

##### vmware.hv.hw.memory[url,uuid]

  
The VMware hypervisor total memory size (bytes).  
Return value: _Integer_.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware hypervisor global unique identifier.

##### vmware.hv.hw.model[url,uuid]

  
The VMware hypervisor model.  
Return value: _String_.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware hypervisor global unique identifier.

##### vmware.hv.hw.sensors.get[url,uuid]

  
The VMware hypervisor hardware sensors value.  
Return value: [JSON object](/documentation/current/en/manual/vm_monitoring/vmware_json#vmware.hv.hw.sensors.get).

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware hypervisor global unique identifier.

##### vmware.hv.hw.serialnumber[url,uuid]

  
The VMware hypervisor serial number.  
Return value: _String_.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware hypervisor global unique identifier.

This item works with vSphere API 6.7 and newer.

##### vmware.hv.hw.uuid[url,uuid]

  
The VMware hypervisor BIOS UUID.  
Return value: _String_.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware hypervisor global unique identifier.

This item works with vSphere API 6.7 and newer.

##### vmware.hv.hw.vendor[url,uuid]

  
The VMware hypervisor vendor name.  
Return value: _String_.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware hypervisor global unique identifier.

This item works with vSphere API 6.7 and newer.

##### vmware.hv.maintenance[url,uuid]

  
The VMware hypervisor maintenance status.  
Return value: _0_ \- not in maintenance; _1_ \- in maintenance.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware hypervisor global unique identifier.

##### vmware.hv.memory.size.ballooned[url,uuid]

  
The VMware hypervisor ballooned memory size (bytes).  
Return value: _Integer_.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware hypervisor global unique identifier.

##### vmware.hv.memory.used[url,uuid]

  
The VMware hypervisor used memory size (bytes).  
Return value: _Integer_.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware hypervisor global unique identifier.

##### vmware.hv.net.if.discovery[url,uuid]

  
The discovery of VMware hypervisor network interfaces.  
Return value: _JSON object_.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware hypervisor global unique identifier.

##### vmware.hv.network.in[url,uuid,<mode>]

  
The VMware hypervisor network input statistics (bytes per second).  
Return value: _Integer_ **[2](vmware_keys#footnotes)**.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware hypervisor global unique identifier;
  * **mode** \- _bps_ (default), _packets_ , _dropped_ , _errors_ , _broadcast_.

##### vmware.hv.network.linkspeed[url,uuid,ifname]

  
The VMware hypervisor network interface speed.  
Return value: _Integer_. Returns _0_ , if the network interface is down, otherwise the speed value of the interface.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware hypervisor global unique identifier;
  * **ifname** \- the interface name.

##### vmware.hv.network.out[url,uuid,<mode>]

  
The VMware hypervisor network output statistics (bytes per second).  
Return value: _Integer_ **[2](vmware_keys#footnotes)**.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware hypervisor global unique identifier;
  * **mode** \- _bps_ (default), _packets_ , _dropped_ , _errors_ , _broadcast_.

##### vmware.hv.perfcounter[url,uuid,path,<instance>]

  
The VMware hypervisor performance counter value.  
Return value: _Integer_ **[2](vmware_keys#footnotes)**.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware hypervisor global unique identifier;
  * **path** \- the performance counter path **[1](vmware_keys#footnotes)** ;
  * **instance** \- the performance counter instance. Use empty instance for aggregate values (default).

##### vmware.hv.property[url,uuid,prop]

  
The VMware hypervisor property.  
Return value: _String_.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware hypervisor global unique identifier;
  * **prop** \- the property path.

##### vmware.hv.power[url,uuid,<max>]

  
The VMware hypervisor power usage (W).  
Return value: _Integer_.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware hypervisor global unique identifier;
  * **max** \- the maximum allowed power usage.

##### vmware.hv.sensor.health.state[url,uuid]

  
The VMware hypervisor health state rollup sensor.  
Return value: _Integer_ : _0_ \- gray; _1_ \- green; _2_ \- yellow; _3_ \- red.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware hypervisor global unique identifier.

Note that the item might not work in VMware vSphere 6.5 and newer, because VMware has deprecated the _VMware Rollup Health State_ sensor.

##### vmware.hv.sensors.get[url,uuid]

  
The VMware hypervisor HW vendor state sensors.  
Return value: [JSON object](/documentation/current/en/manual/vm_monitoring/vmware_json#vmware.hv.sensors.get).

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware hypervisor global unique identifier.

##### vmware.hv.status[url,uuid]

  
The VMware hypervisor status.  
Return value: _Integer_ : _0_ \- gray; _1_ \- green; _2_ \- yellow; _3_ \- red.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware hypervisor global unique identifier.

This item uses the host system overall status property.

##### vmware.hv.tags.get[url,uuid]

  
The VMware hypervisor tags array.  
Return value: [JSON object](/documentation/current/en/manual/vm_monitoring/vmware_json#vmware..tags.get).

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware hypervisor global unique identifier.

This item works with vSphere 6.5 and newer.

##### vmware.hv.uptime[url,uuid]

  
The VMware hypervisor uptime (seconds).  
Return value: _Integer_.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware hypervisor global unique identifier.

This item uses the host system overall status property.

##### vmware.hv.version[url,uuid]

  
The VMware hypervisor version.  
Return value: _String_.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware hypervisor global unique identifier.

##### vmware.hv.vm.num[url,uuid]

  
The number of virtual machines on the VMware hypervisor.  
Return value: _Integer_.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware hypervisor global unique identifier.

##### vmware.rp.cpu.usage[url,rpid]

  
The CPU usage in hertz during the interval on VMware Resource Pool.  
Return value: _Integer_.

Parameters:

  * **url** \- the VMware service URL;
  * **rpid** \- the VMware resource pool ID.

##### vmware.rp.memory[url,rpid,<mode>]

  
The memory metrics of VMware resource pool.  
Return value: _Integer_.

Parameters:

  * **url** \- the VMware service URL;
  * **rpid** \- the VMware resource pool ID;
  * **mode** \- possible values:  
_consumed_ (default) - the amount of host physical memory consumed for backing up guest physical memory pages  
_ballooned_ \- the amount of guest physical memory reclaimed from the virtual machine by the balloon driver in the guest  
 _overhead_ \- the host physical memory consumed by ESXi data structures for running the virtual machines

##### vmware.alarms.get[url]

  
The VMware virtual center alarms data.  
Return value: [JSON object](/documentation/current/en/manual/vm_monitoring/vmware_json#vmware..alarms.get).

Parameters:

  * **url** \- the VMware service URL.

##### vmware.vm.alarms.get[url,uuid]

  
The VMware virtual machine alarms data.  
Return value: [JSON object](/documentation/current/en/manual/vm_monitoring/vmware_json#vmware..alarms.get).

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware virtual machine global unique identifier.

##### vmware.vm.attribute[url,uuid,name]

  
The VMware virtual machine custom attribute value.  
Return value: _String_.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware virtual machine global unique identifier;
  * **name** \- the custom attribute name.

##### vmware.vm.cluster.name[url,uuid]

  
The VMware virtual machine name.  
Return value: _String_.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware virtual machine global unique identifier;
  * **name** \- the custom attribute name.

##### vmware.vm.consolidationneeded[url,uuid]

  
The VMware virtual machine disk requires consolidation.  
Return value: _String_ : _true_ \- consolidation is needed; _false_ \- consolidation is not needed.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware virtual machine global unique identifier.

##### vmware.vm.cpu.latency[url,uuid]

  
The percentage of time the virtual machine is unable to run because it is contending for access to the physical CPU(s).  
Return value: _Float_.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware virtual machine global unique identifier.

##### vmware.vm.cpu.num[url,uuid]

  
The number of processors on VMware virtual machine.  
Return value: _Integer_.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware virtual machine global unique identifier.

##### vmware.vm.cpu.readiness[url,uuid,<instance>]

  
The percentage of time that the virtual machine was ready, but could not get scheduled to run on the physical CPU.  
Return value: _Float_.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware virtual machine global unique identifier;
  * **instance** \- the CPU instance.

##### vmware.vm.cpu.ready[url,uuid]

  
The time (in milliseconds) that the virtual machine was ready, but could not get scheduled to run on the physical CPU. CPU ready time is dependent on the number of virtual machines on the host and their CPU loads (%).  
Return value: _Integer_ **[2](vmware_keys#footnotes)**.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware virtual machine global unique identifier.

##### vmware.vm.cpu.swapwait[url,uuid,<instance>]

  
The percentage of CPU time spent waiting for swap-in.  
Return value: _Float_.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware virtual machine global unique identifier;
  * **instance** \- the CPU instance.

##### vmware.vm.cpu.usage[url,uuid]

  
The VMware virtual machine processor usage (Hz).  
Return value: _Integer_.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware virtual machine global unique identifier.

##### vmware.vm.cpu.usage.perf[url,uuid]

  
The VMware virtual machine processor usage as a percentage during the interval.  
Return value: _Float_.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware virtual machine global unique identifier.

##### vmware.vm.datacenter.name[url,uuid]

  
The VMware virtual machine datacenter name.  
Return value: _String_.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware virtual machine global unique identifier.

##### vmware.vm.discovery[url]

  
The discovery of VMware virtual machines.  
Return value: [JSON object](/documentation/current/en/manual/vm_monitoring/discovery_fields).

Parameters:

  * **url** \- the VMware service URL.

##### vmware.vm.guest.memory.size.swapped[url,uuid]

  
The amount of guest physical memory that is swapped out to the swap space (KB).  
Return value: _Integer_.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware virtual machine global unique identifier.

##### vmware.vm.guest.osuptime[url,uuid]

  
The total time elapsed since the last operating system boot-up (in seconds).  
Return value: _Integer_.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware virtual machine global unique identifier.

##### vmware.vm.hv.maintenance[url,uuid]

  
The VMware virtual machine hypervisor maintenance status.  
Return value: _0_ \- not in maintenance; _1_ \- in maintenance.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware virtual machine global unique identifier.

##### vmware.vm.hv.name[url,uuid]

  
The VMware virtual machine hypervisor name.  
Return value: _String_.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware virtual machine global unique identifier.

##### vmware.vm.memory.size[url,uuid]

  
The VMware virtual machine total memory size (bytes).  
Return value: _Integer_.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware virtual machine global unique identifier.

##### vmware.vm.memory.size.ballooned[url,uuid]

  
The VMware virtual machine ballooned memory size (bytes).  
Return value: _Integer_.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware virtual machine global unique identifier.

##### vmware.vm.memory.size.compressed[url,uuid]

  
The VMware virtual machine compressed memory size (bytes).  
Return value: _Integer_.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware virtual machine global unique identifier.

##### vmware.vm.memory.size.consumed[url,uuid]

  
The amount of host physical memory consumed for backing up guest physical memory pages (KB).  
Return value: _Integer_.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware virtual machine global unique identifier.

##### vmware.vm.memory.size.private[url,uuid]

  
The VMware virtual machine private memory size (bytes).  
Return value: _Integer_.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware virtual machine global unique identifier.

##### vmware.vm.memory.size.shared[url,uuid]

  
The VMware virtual machine shared memory size (bytes).  
Return value: _Integer_.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware virtual machine global unique identifier.

##### vmware.vm.memory.size.swapped[url,uuid]

  
The VMware virtual machine swapped memory size (bytes).  
Return value: _Integer_.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware virtual machine global unique identifier.

##### vmware.vm.memory.size.usage.guest[url,uuid]

  
The VMware virtual machine guest memory usage (bytes).  
Return value: _Integer_.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware virtual machine global unique identifier.

##### vmware.vm.memory.size.usage.host[url,uuid]

  
The VMware virtual machine host memory usage (bytes).  
Return value: _Integer_.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware virtual machine global unique identifier.

##### vmware.vm.memory.usage[url,uuid]

  
The percentage of host physical memory that has been consumed.  
Return value: _Float_.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware virtual machine global unique identifier.

##### vmware.vm.net.if.discovery[url,uuid]

  
The discovery of VMware virtual machine network interfaces.  
Return value: [JSON object](/documentation/current/en/manual/vm_monitoring/discovery_fields).

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware virtual machine global unique identifier.

##### vmware.vm.net.if.in[url,uuid,instance,<mode>]

  
The VMware virtual machine network interface input statistics (bytes/packets per second).  
Return value: _Integer_ **[2](vmware_keys#footnotes)**.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware virtual machine global unique identifier;
  * **instance** \- the network interface instance;
  * **mode** \- _bps_ (default) or _pps_ \- bytes or packets per second.

##### vmware.vm.net.if.out[url,uuid,instance,<mode>]

  
The VMware virtual machine network interface output statistics (bytes/packets per second).  
Return value: _Integer_ **[2](vmware_keys#footnotes)**.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware virtual machine global unique identifier;
  * **instance** \- the network interface instance;
  * **mode** \- _bps_ (default) or _pps_ \- bytes or packets per second.

##### vmware.vm.net.if.usage[url,uuid,<instance>]

  
The VMware virtual machine network utilization (combined transmit-rates and receive-rates) during the interval (KBps).  
Return value: _Integer_.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware virtual machine global unique identifier;
  * **instance** \- the network interface instance.

##### vmware.vm.perfcounter[url,uuid,path,<instance>]

  
The VMware virtual machine performance counter value.  
Return value: _Integer_ **[2](vmware_keys#footnotes)**.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware virtual machine global unique identifier;
  * **path** \- the performance counter path **[1](vmware_keys#footnotes)** ;
  * **instance** \- the performance counter instance. Use empty instance for aggregate values (default).

##### vmware.vm.powerstate[url,uuid]

  
The VMware virtual machine power state.  
Return value: _0_ \- poweredOff; _1_ \- poweredOn; _2_ \- suspended.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware virtual machine global unique identifier.

##### vmware.vm.property[url,uuid,prop]

  
The VMware virtual machine property.  
Return value: _String_.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware virtual machine global unique identifier;
  * **prop** \- the property path.

##### vmware.vm.snapshot.get[url,uuid]

  
The VMware virtual machine snapshot state.  
Return value: [JSON object](/documentation/current/en/manual/vm_monitoring/vmware_json#vmware.vm.snapshot.get).

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware virtual machine global unique identifier.

##### vmware.vm.state[url,uuid]

  
The VMware virtual machine state.  
Return value: _String_ : _notRunning_ , _resetting_ , _running_ , _shuttingDown_ , _standby_ , or _unknown_.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware virtual machine global unique identifier.

##### vmware.vm.storage.committed[url,uuid]

  
The VMware virtual machine committed storage space (bytes).  
Return value: _Integer_.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware virtual machine global unique identifier.

##### vmware.vm.storage.readoio[url,uuid,instance]

  
The average number of outstanding read requests to the virtual disk during the collection interval.  
Return value: _Integer_.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware virtual machine global unique identifier;
  * **instance** \- the disk device instance.

##### vmware.vm.storage.totalreadlatency[url,uuid,instance]

  
The average time a read from the virtual disk takes (milliseconds).  
Return value: _Integer_.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware virtual machine global unique identifier;
  * **instance** \- the disk device instance.

##### vmware.vm.storage.totalwritelatency[url,uuid,instance]

  
The average time a write to the virtual disk takes (milliseconds).  
Return value: _Integer_.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware virtual machine global unique identifier;
  * **instance** \- the disk device instance.

##### vmware.vm.storage.uncommitted[url,uuid]

  
The VMware virtual machine uncommitted storage space (bytes).  
Return value: _Integer_.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware virtual machine global unique identifier.

##### vmware.vm.storage.unshared[url,uuid]

  
The VMware virtual machine unshared storage space (bytes).  
Return value: _Integer_.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware virtual machine global unique identifier.

##### vmware.vm.storage.writeoio[url,uuid,instance]

  
The average number of outstanding write requests to the virtual disk during the collection interval.  
Return value: _Integer_.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware virtual machine global unique identifier;
  * **instance** \- the disk device instance.

##### vmware.vm.tags.get[url,uuid]

  
The VMware virtual machine tags array.  
Return value: [JSON object](/documentation/current/en/manual/vm_monitoring/vmware_json#vmware..tags.get).

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware virtual machine global unique identifier.

This item works with vSphere 6.5 and newer.

##### vmware.vm.tools[url,uuid,<mode>]

  
The VMware virtual machine guest tools state.  
Return value: _String_.   
In _status_ mode: _guestToolsExecutingScripts_ \- VMware Tools is starting; _guestToolsNotRunning_ \- VMware Tools is not running; _guestToolsRunning_ \- VMware Tools is running.  
In _version_ mode: version.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware virtual machine global unique identifier;
  * **mode** \- _version_ , _status_ (default).

##### vmware.vm.uptime[url,uuid]

  
The VMware virtual machine uptime (seconds).  
Return value: _Integer_.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware virtual machine global unique identifier.

##### vmware.vm.vfs.dev.discovery[url,uuid]

  
The discovery of VMware virtual machine disk devices.  
Return value: [JSON object](/documentation/current/en/manual/vm_monitoring/discovery_fields).

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware virtual machine global unique identifier.

##### vmware.vm.vfs.dev.read[url,uuid,instance,<mode>]

  
The VMware virtual machine disk device read statistics (bytes/operations per second).  
Return value: _Integer_ **[2](vmware_keys#footnotes)**.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware virtual machine global unique identifier;
  * **instance** \- the disk device instance;
  * **mode** \- _bps_ (default) or _ops_ \- bytes or operations per second.

##### vmware.vm.vfs.dev.write[url,uuid,instance,<mode>]

  
The VMware virtual machine disk device write statistics (bytes/operations per second).  
Return value: _Integer_ **[2](vmware_keys#footnotes)**.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware virtual machine global unique identifier;
  * **instance** \- the disk device instance;
  * **mode** \- _bps_ (default) or _ops_ \- bytes or operations per second.

##### vmware.vm.vfs.fs.discovery[url,uuid]

  
The discovery of VMware virtual machine file systems.  
Return value: [JSON object](/documentation/current/en/manual/vm_monitoring/discovery_fields).

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware virtual machine global unique identifier.

VMware Tools must be installed on the guest virtual machine for this item to work.

##### vmware.vm.vfs.fs.size[url,uuid,fsname,<mode>]

  
The VMware virtual machine file system statistics (bytes/percentages).  
Return value: _Integer_ \- for bytes; _Float_ \- for percentage.

Parameters:

  * **url** \- the VMware service URL;
  * **uuid** \- the VMware virtual machine global unique identifier;
  * **fsname** \- the file system name;
  * **mode** \- _total_ , _free_ , _used_ , _pfree_ , or _pused_.

VMware Tools must be installed on the guest virtual machine for this item to work.

##### Footnotes

**1** See [Creating custom performance counter names for VMware](/documentation/current/en/manual/appendix/items/perf_counters).

**2** The value of these items is obtained from VMware performance counters and the VMwarePerfFrequency [parameter](/documentation/current/en/manual/appendix/config/zabbix_server) is used to refresh their data in Zabbix VMware cache:

  * vmware.cl.perfcounter
  * vmware.hv.datastore.read
  * vmware.hv.datastore.write
  * vmware.hv.network.in
  * vmware.hv.network.out
  * vmware.hv.perfcounter
  * vmware.vm.cpu.ready
  * vmware.vm.net.if.in
  * vmware.vm.net.if.out
  * vmware.vm.perfcounter
  * vmware.vm.vfs.dev.read
  * vmware.vm.vfs.dev.write

#### More info

See [Virtual machine monitoring](/documentation/current/en/manual/vm_monitoring) for detailed information how to configure Zabbix to monitor VMware environments.