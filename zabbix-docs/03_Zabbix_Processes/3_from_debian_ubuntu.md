---
title: Setup from Debian/Ubuntu packages
source: https://www.zabbix.com/documentation/current/en/manual/concepts/java/from_debian_ubuntu
downloaded: 2025-11-14 10:33:55
---

# 3 Setup from Debian/Ubuntu packages

#### Overview

If [installed from packages](/documentation/current/en/manual/installation/install_from_packages), the following information will help you in setting up Zabbix [Java gateway](/documentation/current/en/manual/concepts/java).

#### Configuring and running Java gateway

Java gateway configuration may be tuned in the file:
    
    
    /etc/zabbix/zabbix_java_gateway.conf

Copy

✔ Copied

For more details, see Zabbix Java gateway configuration [parameters](/documentation/current/en/manual/appendix/config/zabbix_java).

To start Zabbix Java gateway:
    
    
    systemctl restart zabbix-java-gateway

Copy

✔ Copied

To automatically start Zabbix Java gateway on boot:
    
    
    systemctl enable zabbix-java-gateway

Copy

✔ Copied

#### Configuring server for use with Java gateway

With Java gateway up and running, you have to tell Zabbix server where to find Zabbix Java gateway. This is done by specifying JavaGateway and JavaGatewayPort parameters in the [server configuration file](/documentation/current/en/manual/appendix/config/zabbix_server). If the host on which JMX application is running is monitored by Zabbix proxy, then you specify the connection parameters in the [proxy configuration file](/documentation/current/en/manual/appendix/config/zabbix_proxy) instead.
    
    
    JavaGateway=192.168.3.14
           JavaGatewayPort=10052

Copy

✔ Copied

By default, server does not start any processes related to JMX monitoring. If you wish to use it, however, you have to specify the number of pre-forked instances of Java pollers. You do this in the same way you specify regular pollers and trappers.
    
    
    StartJavaPollers=5

Copy

✔ Copied

Do not forget to restart server or proxy, once you are done with configuring them.

#### Debugging Java gateway

Zabbix Java gateway log file is:
    
    
    /var/log/zabbix/zabbix_java_gateway.log

Copy

✔ Copied

If you like to increase the logging, edit the file:
    
    
    /etc/zabbix/zabbix_java_gateway_logback.xml

Copy

✔ Copied

and change `level="info"` to "debug" or even "trace" (for deep troubleshooting):
    
    
    <configuration scan="true" scanPeriod="15 seconds">
           [...]
                 <root level="info">
                         <appender-ref ref="FILE" />
                 </root>
           
           </configuration>

Copy

✔ Copied

#### JMX monitoring

See [JMX monitoring](/documentation/current/en/manual/config/items/itemtypes/jmx_monitoring) page for more details.