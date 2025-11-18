---
title: Zabbix agent 2 template operation
source: https://www.zabbix.com/documentation/current/en/manual/config/templates_out_of_the_box/zabbix_agent2
downloaded: 2025-11-14 10:36:03
---

# 2 Zabbix agent 2 template operation

Steps to ensure correct operation of templates that collect metrics with [Zabbix agent 2](/documentation/current/en/manual/concepts/agent2):

1\. Make sure that the agent 2 is installed on the host, and that the installed version contains the required plugin. In some cases, you may need to [upgrade](/documentation/current/en/manual/installation/upgrade) the agent 2 first.  
2\. [Link](/documentation/current/en/manual/config/templates/linking#linking-a-template) the template to a target host (if the template is not available in your Zabbix installation, you may need to [import](/documentation/current/en/manual/config/templates_out_of_the_box#template-upgrade) the template first).  
3\. If necessary, adjust the values of template macros. Note that user macros can be used to override configuration parameters.  
4\. Configure the instance being monitored to allow data sharing with Zabbix.

Zabbix agent 2 templates work in conjunction with the plugins. While the basic configuration can be done by simply adjusting user macros, the deeper customization can be achieved by [configuring the plugin](/documentation/current/en/manual/extensions/plugins#named-sessions) itself. For example, if a plugin supports named sessions, it is possible to monitor several entities of the same kind (e.g. MySQL1 and MySQL2) by specifying named session with own URI, username and password for each entity in the configuration file.

A detailed description of a template, including the full list of macros, items, and triggers, is available in the template's README file (accessible by clicking on a template name).

The following templates are available:

  * [Ceph by Zabbix agent 2](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/app/ceph_agent2/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [Docker](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/app/docker/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [Memcached](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/app/memcached/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [MongoDB cluster by Zabbix agent 2](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/db/mongodb_cluster/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [MongoDB node by Zabbix agent 2](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/db/mongodb/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [MySQL by Zabbix agent 2](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/db/mysql_agent2/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [MySQL by Zabbix agent 2 active](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/db/mysql_agent2_active/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [Oracle by Zabbix agent 2](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/db/oracle_agent2/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [PostgreSQL by Zabbix agent 2](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/db/postgresql_agent2/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [PostgreSQL by Zabbix agent 2 active](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/db/postgresql_agent2_active/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [Redis](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/db/redis/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [SMART by Zabbix agent 2](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/server/smart_agent2/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [SMART by Zabbix agent 2 active](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/server/smart_agent2_active/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [Systemd by Zabbix agent 2](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/app/systemd/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [Website certificate by Zabbix agent 2](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/app/certificate_agent2/README.md?at=refs%2Fheads%2Frelease%2F7.4)