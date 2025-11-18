---
title: Setup from sources
source: https://www.zabbix.com/documentation/current/en/manual/concepts/java/from_sources
downloaded: 2025-11-14 10:33:54
---

# 1 Setup from sources

#### Overview

If [installed](/documentation/current/en/manual/installation/install#installing-java-gateway) from sources, the following information will help you in setting up Zabbix [Java gateway](/documentation/current/en/manual/concepts/java).

#### Overview of files

If you obtained Java gateway from sources, you should have ended up with a collection of shell scripts, JAR and configuration files under $PREFIX/sbin/zabbix_java. The role of these files is summarized below.
    
    
    bin/zabbix-java-gateway-$VERSION.jar

Copy

✔ Copied

Java gateway JAR file itself.
    
    
    lib/logback-core-1.5.16.jar
           lib/logback-classic-1.5.16.jar
           lib/slf4j-api-2.0.16.jar
           lib/android-json-4.3_r3.1.jar

Copy

✔ Copied

Dependencies of Java gateway: [Logback](http://logback.qos.ch/), [SLF4J](http://www.slf4j.org/), and [Android JSON](https://android.googlesource.com/platform/libcore/+/master/json) library.
    
    
    lib/logback.xml  
           lib/logback-console.xml

Copy

✔ Copied

Configuration files for Logback.
    
    
    shutdown.sh  
           startup.sh

Copy

✔ Copied

Convenience scripts for starting and stopping Java gateway.
    
    
    settings.sh

Copy

✔ Copied

Configuration file that is sourced by startup and shutdown scripts above.

#### Configuring and running Java gateway

By default, Java gateway listens on port 10052. If you plan on running Java gateway on a different port, you can specify that in settings.sh script. See the description of [Java gateway configuration file](/documentation/current/en/manual/appendix/config/zabbix_java) for how to specify this and other options.

Port 10052 is not [IANA registered](http://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.txt).

Once you are comfortable with the settings, you can start Java gateway by running the startup script:
    
    
    ./startup.sh

Copy

✔ Copied

Likewise, once you no longer need Java gateway, run the shutdown script to stop it:
    
    
    ./shutdown.sh

Copy

✔ Copied

Note that unlike server or proxy, Java gateway is lightweight and does not need a database.

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

In case there are any problems with Java gateway or an error message that you see about an item in the frontend is not descriptive enough, you might wish to take a look at Java gateway log file.

By default, Java gateway logs its activities into /tmp/zabbix_java.log file with log level "info". Sometimes that information is not enough and there is a need for information at log level "debug". In order to increase logging level, modify file lib/logback.xml and change the level attribute of <root> tag to "debug":
    
    
    <root level="debug">
             <appender-ref ref="FILE" />
           </root>

Copy

✔ Copied

Note that unlike Zabbix server or Zabbix proxy, there is no need to restart Zabbix Java gateway after changing logback.xml file - changes in logback.xml will be picked up automatically. When you are done with debugging, you can return the logging level to "info".

If you wish to log to a different file or a completely different medium like database, adjust logback.xml file to meet your needs. See [Logback Manual](http://logback.qos.ch/manual/) for more details.

Sometimes for debugging purposes it is useful to start Java gateway as a console application rather than a daemon. To do that, comment out PID_FILE variable in settings.sh. If PID_FILE is omitted, startup.sh script starts Java gateway as a console application and makes Logback use lib/logback-console.xml file instead, which not only logs to console, but has logging level "debug" enabled as well.

Finally, note that since Java gateway uses SLF4J for logging, you can replace Logback with the framework of your choice by placing an appropriate JAR file in lib directory. See [SLF4J Manual](http://www.slf4j.org/manual.html) for more details.

#### JMX monitoring

See [JMX monitoring](/documentation/current/en/manual/config/items/itemtypes/jmx_monitoring) page for more details.