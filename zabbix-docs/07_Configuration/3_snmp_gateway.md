---
title: SNMP gateway
source: https://www.zabbix.com/documentation/current/en/manual/config/export/snmp_gateway
downloaded: 2025-11-14 10:36:46
---

# 3 SNMP gateway

#### Overview

Zabbix SNMP gateway is an AgentX-extension for snmpd supporting both SNMP polling and trapping.

With Zabbix SNMP gateway it is possible to use the SNMP protocol to retrieve:

  * trigger data;
  * problem trigger data;
  * host group status (count of triggers by trigger status per group)

The data is retrieved by the OID, which is a combination of a common base and a specific suffix. The common **base** is set in the configuration file of SNMP gateway, for example:

  * `BaseOID=1.3.6.1.4.1.3043.7.55` \- for any trigger data;
  * `ProblemBaseOID=1.3.6.1.4.1.3047.7.55` \- for problem trigger data;
  * `BaseOID=1.3.6.1.4.1.3046.7.55` \- for host group status.

The OID **suffix** is set in the configuration on host triggers as a **tag** (for example, `OIDSuffix:3`) in the frontend.

In this case all information for the trigger will be available under `OID=1.3.6.1.4.1.3043.7.55.X.3`. "X" here will be the number of trigger data fields (i.e. 1 - suffix, 2 - ID, 3 - expression, 4 - description, etc.).

For a more detailed description and the configuration file example, see the [SNMP gateway readme file](https://git.zabbix.com/projects/ZT/repos/snmp-gateway/browse/README.md).

#### Installation and setup

See the [readme](https://git.zabbix.com/projects/ZT/repos/snmp-gateway/browse/README.md) file of SNMP gateway for instructions on:

  * installing and configuring snmpd;
  * enabling AgentX support;
  * configuring Zabbix SNMP gateway;
  * configuring SNMP traps for trigger state changes.

#### Retrieving data

With everything set up properly, you may use `snmpwalk` and `snmpget` commands to retrieve data:
    
    
    [user@localhost ~]# snmpget -v2c -c public 127.0.0.1 1.3.6.1.4.1.3043.7.55.2.3
           SNMPv2-SMI::enterprises.3043.7.55.2.3 = INTEGER: 15247
    
    
    [user@localhost ~]# snmpwalk -v2c -c public 127.0.0.1 1.3.6.1.4.1.3043.7.55
           SNMPv2-SMI::enterprises.3043.7.55.1.1 = INTEGER: 1
           SNMPv2-SMI::enterprises.3043.7.55.1.3 = INTEGER: 3
           SNMPv2-SMI::enterprises.3043.7.55.1.4 = INTEGER: 4
           SNMPv2-SMI::enterprises.3043.7.55.1.5 = INTEGER: 5
           SNMPv2-SMI::enterprises.3043.7.55.1.6 = INTEGER: 6
           SNMPv2-SMI::enterprises.3043.7.55.1.10 = INTEGER: 10
           SNMPv2-SMI::enterprises.3043.7.55.2.1 = INTEGER: 15367
           SNMPv2-SMI::enterprises.3043.7.55.2.3 = INTEGER: 15247
           SNMPv2-SMI::enterprises.3043.7.55.2.4 = INTEGER: 15365
           SNMPv2-SMI::enterprises.3043.7.55.2.5 = INTEGER: 15366
           SNMPv2-SMI::enterprises.3043.7.55.2.6 = INTEGER: 13493
           SNMPv2-SMI::enterprises.3043.7.55.2.10 = INTEGER: 13503
           ...

##### Filtering options

You may limit the problem trigger information in SNMP gateway configuration:

  * by severity (by default `ProblemMinSeverity=-1`)
  * by hiding acknowledged problems (by default `ProblemHideAck=false`)

You may limit the problem count per host group in SNMP gateway configuration:

  * by unknown state triggers (by default `CountUnknown=-false`)
  * by triggers with acknowledged/unacknowledged/all problems (by default `CountAcknowledgeStatus=all`)