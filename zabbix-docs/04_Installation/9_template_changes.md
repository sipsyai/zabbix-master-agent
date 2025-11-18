---
title: Template changes
source: https://www.zabbix.com/documentation/current/en/manual/installation/template_changes
downloaded: 2025-11-14 10:34:22
---

# 9 Template changes

This page lists all changes to the stock templates that are shipped with Zabbix.

Upgrading to the latest Zabbix version will not automatically upgrade the templates used. It is recommended to modify the templates in existing installations by downloading the latest templates from the [Zabbix Git repository](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates?at=refs%2Fheads%2Frelease%2F7.4) and [importing](/documentation/current/en/manual/xml_export_import/templates#importing) them manually into Zabbix.

If templates with the same names already exist, the _Delete missing_ options should be checked when importing to achieve a clean import. This way, the old items that are no longer in the updated template will be removed (note that it will mean losing history of these old items).

Please be informed that since Zabbix 6.0, all templates follow an updated format, which may impact the import of pre-6.0 templates. For more information, see [Template changes in 6.0](https://www.zabbix.com/documentation/6.0/en/manual/installation/template_changes#updated-template-format).

## Changes in 7.4.1

#### New templates

  * [Cisco Secure Firewall Threat Defense by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/net/cisco/cisco_secure_ftd_http?at=refs%2Fheads%2Frelease%2F7.4), a template providing monitoring capabilities for Cisco Secure Firewall Threat Defense devices using REST API.

#### Updated templates

  * The template _VMware Guest_ within the [VMware](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/app/vmware?at=refs%2Fheads%2Frelease%2F7.4) and [VMware FQDN](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/app/vmware_fqdn?at=refs%2Fheads%2Frelease%2F7.4) template sets has been updated with a new item _Boot time_. This item now replaces _Uptime of guest OS_ in the trigger _VM has been restarted_ to avoid false positives after virtual machine migrations, such as vMotion.

## Changes in 7.4.2

#### New templates

  * The [AWS by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/cloud/AWS/aws_http?at=refs%2Fheads%2Frelease%2F7.4) template set has been supplemented with the template _AWS Backup Vault by HTTP_.

## Changes in 7.4.3

#### New templates

  * [Aruba CX 8300s by SNMP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/net/aruba/aruba_cx8300s_snmp/README.md?at=refs%2Fheads%2Frelease%2F7.4), a template providing SNMP-based monitoring for the Aruba CX 8300 switch series.
  * [Ciena 3906 by SNMP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/net/ciena/README.md?at=refs%2Fheads%2Frelease%2F7.4), a template for monitoring Ciena 3906 devices.
  * [Vyatta Virtual Router by SNMP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/net/vyatta_virtual_router?at=refs%2Fheads%2Frelease%2F7.4), a template for monitoring the Vyatta 1908e virtual router.

#### Updated templates

  * [Huawei OceanStor Dorado by SNMP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/san/huawei_dorado_snmp?at=refs%2Fheads%2Frelease%2F7.4) has been updated with details on device coverage.
  * The template sets [Zabbix server health](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/app/zabbix_server?at=refs%2Fheads%2Frelease%2F7.4) and [Zabbix proxy health](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/app/zabbix_proxy?at=refs%2Fheads%2Frelease%2F7.4) have been updated with extended preprocessor throughput monitoring capabilities.

## Changes in 7.4.4

#### New templates

  * [Stormshield SNS by SNMP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/net/stormshield_sns/README.md?at=refs%2Fheads%2Frelease%2F7.4), a template for monitoring Stormshield Network Security (SNS) devices via SNMP.

## Changes in 7.4.6

#### Updated templates

  * [MySQL by Zabbix agent](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/db/mysql_agent/README.md?at=refs%2Fheads%2Frelease%2F7.4), [MySQL by Zabbix agent 2](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/db/mysql_agent2/README.md?at=refs%2Fheads%2Frelease%2F7.4), [MySQL by Zabbix agent active](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/db/mysql_agent_active/README.md?at=refs%2Fheads%2Frelease%2F7.4), [MySQL by Zabbix agent 2 active](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/db/mysql_agent2_active/README.md?at=refs%2Fheads%2Frelease%2F7.4), and [MySQL by ODBC](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/db/mysql_odbc/README.md?at=refs%2Fheads%2Frelease%2F7.4) have been updated to support both `SHOW SLAVE STATUS` (old syntax) and `SHOW REPLICA STATUS` (new syntax).