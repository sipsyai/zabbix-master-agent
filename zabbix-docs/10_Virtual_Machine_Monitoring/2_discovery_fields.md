---
title: Virtual machine discovery key fields
source: https://www.zabbix.com/documentation/current/en/manual/vm_monitoring/discovery_fields
downloaded: 2025-11-14 10:36:58
---

# 2 Virtual machine discovery key fields

The following table lists fields returned by virtual machine related discovery keys.

**Description** | **Field** | **Retrieved content**  
---|---|---  
**vmware.cluster.discovery**  
Performs cluster discovery. | {#CLUSTER.ID} | Cluster identifier.  
{#CLUSTER.NAME} | Cluster name.  
"resource_pool" | An array containing resource pool data, including resource group ID, tags array, resource pool path, number of virtual machines.  
  
Array structure:  
`[{`  
`"rpid":"resource group id",`  
`"tags":[{}],`  
`"rpath":"resource group path",`  
`"vm_count":0`  
`}]`  
  
For `"tags"` array structure, see the "tags" field.  
"tags" | An array containing tags with tag name, description and category.  
  
Array structure:  
`[{`  
`"tag":"tag name",`  
`"tag_description":"tag description",`  
`"category":"tag category"`  
`}]`  
**vmware.datastore.discovery**  
Performs datastore discovery. | {#DATASTORE} | Datastore name.  
{#DATASTORE.EXTENT} | An array containing datastore extent partition ID and instance name.  
  
Array structure:  
`[{`  
`"partitionid":1,`  
`"instance":"name"`  
`}]`  
{#DATASTORE.TYPE} | Datastore type.  
  
Value examples: `VMFS`, `NFS`, `vsan`, etc.  
{#DATASTORE.UUID} | Datastore identifier.  
"tags" | An array containing tags with tag name, description and category.  
  
Array structure:  
`[{`  
`"tag":"tag name",`  
`"tag_description":"tag description",`  
`"category":"tag category"`  
`}]`  
**vmware.dc.discovery**  
Performs datacenter discovery. | {#DATACENTER} | Datacenter name.  
{#DATACENTERID} | Datacenter identifier.  
"tags" | An array containing tags with tag name, description and category.  
  
Array structure:  
`[{`  
`"tag":"tag name",`  
`"tag_description":"tag description",`  
`"category":"tag category"`  
`}]`  
**vmware.dvswitch.discovery**  
Performs vSphere distributed switches discovery. | {#DVS.NAME} | Switch name.  
{#DVS.UUID} | Switch identifier.  
**vmware.hv.discovery**  
Performs hypervisor discovery. | {#HV.UUID} | Unique hypervisor identifier.  
{#HV.ID} | Hypervisor identifier (HostSystem managed object name).  
{#HV.NAME} | Hypervisor name.  
{#HV.NETNAME} | Hypervisor network host name.  
{#HV.IP} | Hypervisor IP address, might be empty.  
  
In case of an HA configuration with multiple net interfaces, the following selection priority for interface is observed:  
\- prefer the IP which shares the IP-subnet with the vCenter IP;  
\- prefer the IP from IP-subnet with default gateway;  
\- prefer the IP from interface with the lowest ID.  
{#CLUSTER.NAME} | Cluster name, might be empty.  
{#DATACENTER.NAME} | Datacenter name.  
{#PARENT.NAME} | Name of container that stores the hypervisor.  
{#PARENT.TYPE} | Type of container in which the hypervisor is stored. The values could be `Datacenter`, `Folder`, `ClusterComputeResource`, `VMware`, where "VMware" stands for unknown container type.  
"resource_pool" | An array containing resource pool data, including resource group ID, tags array, resource pool path, number of virtual machines.  
  
Array structure:  
`[{`  
`"rpid":"resource group id",`  
`"tags":[{}],`  
`"rpath":"resource group path",`  
`"vm_count":0`  
`}]`  
  
For `"tags"` array structure, see the "tags" field.  
"tags" | An array containing tags with tag name, description and category.  
  
Array structure:  
`[{`  
`"tag":"tag name",`  
`"tag_description":"tag description",`  
`"category":"tag category"`  
`}]`  
**vmware.hv.datastore.discovery**  
Performs hypervisor datastore discovery. Note that multiple hypervisors can use the same datastore. | {#DATASTORE} | Datastore name.  
{#DATASTORE.TYPE} | Datastore type.  
  
Value examples: `VMFS`, `NFS`, `vsan`, etc.  
{#DATASTORE.UUID} | Datastore identifier.  
{#MULTIPATH.COUNT} | Registered number of datastore paths.  
{#MULTIPATH.PARTITION.COUNT} | Number of available disk partitions.  
"datastore_extent" | An array containing datastore extent instance name and partition ID.  
  
Array structure:  
`[{`  
`"partitionid":1,`  
`"instance":"name"`  
`}]`  
"tags" | An array containing tags with tag name, description and category.  
  
Array structure:  
`[{`  
`"tag":"tag name",`  
`"tag_description":"tag description",`  
`"category":"tag category"`  
`}]`  
**vmware.hv.net.if.discovery**  
Performs hypervisor network interfaces discovery. | {#IFNAME} | Interface name.  
{#IFDRIVER} | Interface driver.  
{#IFDUPLEX} | Interface duplex settings.  
{#IFSPEED} | Interface speed.  
{#IFMAC} | Interface mac address.  
**vmware.vm.discovery**  
Performs virtual machine discovery. | {#VM.UUID} | Unique virtual machine identifier.  
{#VM.ID} | Virtual machine identifier (VirtualMachine managed object name).  
{#VM.NAME} | Virtual machine name.  
{#HV.NAME} | Hypervisor name.  
{#HV.UUID} | Unique hypervisor identifier.  
{#HV.ID} | Hypervisor identifier (HostSystem managed object name).  
{#CLUSTER.NAME} | Cluster name, might be empty.  
{#DATACENTER.NAME} | Datacenter name.  
{#DATASTORE.NAME} | Datastore name.  
{#DATASTORE.UUID} | Datastore identifier.  
{#VM.IP} | Virtual machine IP address, might be empty.  
{#VM.DNS} | Virtual machine DNS name, might be empty.  
{#VM.GUESTFAMILY} | Guest virtual machine OS family, might be empty.  
{#VM.GUESTFULLNAME} | Full guest virtual machine OS name, might be empty.  
{#VM.FOLDER} | The chain of virtual machine parent folders, can be used as value for nested groups; folder names are combined with "/". Might be empty.  
{#VM.TOOLS.STATUS} | VMware virtual machine tools state.  
{#VM.POWERSTATE} | VMware virtual machine power state (`poweredOff`, `poweredOn`, or `suspended`).  
{#VM.RPOOL.ID} | Resource pool identifier.  
{#VM.RPOOL.PATH} | Full resource pool path excluding the "root" name "Resources". Folder names are combined with "/".  
{#VM.SNAPSHOT.COUNT} | Number of VM snapshots.  
"tags" | An array containing tags with tag name, description and category.  
  
Array structure:  
`[{`  
`"tag":"tag name",`  
`"tag_description":"tag description",`  
`"category":"tag category"`  
`}]`  
"vm_customattribute" | An array of virtual machine custom attributes (if defined).  
  
Array structure:  
`[{`  
`"name":"custom field name",`  
`"value":"custom field value"`  
`}]`  
"net_if" | An array of virtual machine network interfaces.  
  
Array structure:  
`[{`  
`"ifname": "interface name",`  
`"ifdesc": "interface description",`  
`"ifmac": "00:00:00:00:00:00",`  
`"ifconnected": true,`  
`"iftype": "interface type",`  
`"ifbackingdevice": "interface backing device",`  
`"ifdvswitch_uuid": "interface switch uuid",`  
`"ifdvswitch_portgroup": "interface switch port group",`  
`"ifdvswitch_port": "interface switch port",`  
`"ifip": ["interface ip addresses"]`  
`}]`  
  
For the description of returned data, see the "vmware.vm.net.if.discovery" item key.  
**vmware.vm.net.if.discovery**  
Performs virtual machine network interface discovery. | {#IFNAME} | Network interface name.  
{#IFDESC} | Interface description.  
{#IFMAC} | Interface mac address.  
{#IFCONNECTED} | Interface connection status (`false` \- disconnected; `true` \- connected).  
{#IFTYPE} | Interface type.  
{#IFBACKINGDEVICE} | Name of the backing device.  
{#IFDVSWITCH.UUID} | Unique vSphere Distributed Switch identifier.  
{#IFDVSWITCH.PORTGROUP} | Distributed port group.  
{#IFDVSWITCH.PORT} | vSphere Distributed Switch port.  
"ifip" | An array of interface addresses.  
**vmware.vm.vfs.dev.discovery**  
Performs virtual machine disk device discovery. | {#DISKNAME} | Disk device name.  
**vmware.vm.vfs.fs.discovery**  
Performs virtual machine file system discovery. | {#FSNAME} | File system name.