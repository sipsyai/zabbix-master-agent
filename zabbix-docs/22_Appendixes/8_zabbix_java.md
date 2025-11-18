---
title: Zabbix Java gateway
source: https://www.zabbix.com/documentation/current/en/manual/appendix/config/zabbix_java
downloaded: 2025-11-14 10:47:06
---

# 8 Zabbix Java gateway

If you use `startup.sh` and `shutdown.sh` scripts for starting [Zabbix Java gateway](/documentation/current/en/manual/concepts/java), then you can specify the necessary configuration parameters in the `settings.sh` file. The startup and shutdown scripts source the settings file and take care of converting shell variables (listed in the first column) to Java properties (listed in the second column).

If you start Zabbix Java gateway manually by running `java` directly, then you specify the corresponding Java properties on the command line.

LISTEN_IP | zabbix.listenIP | no |  | 0.0.0.0 | IP address to listen on.  
---|---|---|---|---|---  
LISTEN_PORT | zabbix.listenPort | no | 1024-32767 | 10052 | Port to listen on.  
PID_FILE | zabbix.pidFile | no |  | /tmp/zabbix_java.pid | Name of PID file. If omitted, Zabbix Java Gateway is started as a console application.  
PROPERTIES_FILE | zabbix.propertiesFile | no |  |  | Name of properties file. Can be used to set additional properties using a key-value format in such a way that they are not visible on a command line or to overwrite existing ones.  
For example: "javax.net.ssl.trustStorePassword=<password>"  
START_POLLERS | zabbix.startPollers | no | 1-1000 | 5 | Number of worker threads to start.  
TIMEOUT | zabbix.timeout | no | 1-30 | 3 | How long to wait for network operations.  
  
Port 10052 is not [IANA registered](http://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.txt).