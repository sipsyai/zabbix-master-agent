---
title: JMX template operation
source: https://www.zabbix.com/documentation/current/en/manual/config/templates_out_of_the_box/jmx
downloaded: 2025-11-14 10:36:06
---

# 5 JMX template operation

Steps to ensure correct operation of templates that collect metrics by [JMX](/documentation/current/en/manual/config/items/itemtypes/jmx_monitoring):

1\. Make sure that Zabbix [Java gateway](/documentation/current/en/manual/concepts/java#getting-java-gateway) is installed and set up properly.  
2\. [Link](/documentation/current/en/manual/config/templates/linking#linking-a-template) the template to the target host. The host should have the JMX interface set up.  
If the template is not available in your Zabbix installation, you may need to [import](/documentation/current/en/manual/config/templates_out_of_the_box#template-upgrade) the template first.  
3\. If necessary, adjust the values of template macros.  
4\. Configure the instance being monitored to allow data sharing with Zabbix.

A detailed description of a template, including the full list of macros, items, and triggers, is available in the template's README file (accessible by clicking on a template name).

The following templates are available:

  * [Apache ActiveMQ by JMX](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/app/activemq_jmx/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [Apache Cassandra by JMX](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/db/cassandra_jmx/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [Apache Kafka by JMX](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/app/kafka_jmx/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [Apache Tomcat by JMX](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/app/tomcat_jmx/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [GridGain by JMX](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/db/gridgain_jmx/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [Ignite by JMX](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/db/ignite_jmx/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [Jira Data Center by JMX](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/app/jira_datacenter_jmx/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [WildFly Domain by JMX](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/app/wildfly_domain_jmx/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [WildFly Server by JMX](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/app/wildfly_server_jmx/README.md?at=refs%2Fheads%2Frelease%2F7.4)