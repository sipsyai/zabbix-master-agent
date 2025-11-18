---
title: Installation from containers
source: https://www.zabbix.com/documentation/current/en/manual/installation/containers
downloaded: 2025-11-14 10:34:11
---

# 5 Installation from containers

### Overview

This section describes how to deploy Zabbix with Docker or Docker Compose.

Zabbix officially provides:

  * Separate Docker images for each Zabbix component to run as portable and self-sufficient containers.
  * Compose files for defining and running multi-container Zabbix components in Docker.

Since Zabbix 6.0, deterministic triggers need to be created during the installation. If binary logging is enabled for MySQL/MariaDB, this requires superuser privileges or setting the variable/configuration parameter _log_bin_trust_function_creators = 1_. See [Database creation scripts](/documentation/current/en/manual/appendix/install/db_scripts#mysqlmariadb) for instructions how to set the variable.  
Note that if executing from a console, the variable will only be set temporarily and will be dropped when a Docker is restarted. In this case, keep your SQL service running, only stop zabbix-server service by running 'docker compose down zabbix-server' and then 'docker compose up -d zabbix-server'.  
Alternatively, you can set this variable in the configuration file.

#### Source files

Docker file sources are stored in the Zabbix [official repository](https://github.com/zabbix/zabbix-docker) on GitHub, where you can follow latest file changes or fork the project to make your own images.

### Docker

Zabbix provides images based on a variety of OS base images. To get the list of supported base operating system images for a specific Zabbix component, see the component's description in [Docker Hub](https://hub.docker.com/u/zabbix). All Zabbix images are configured to rebuild latest images if base images are updated.

#### Installation

To get Zabbix component image, run:
    
    
    docker pull zabbix/zabbix-server-mysql

Copy

✔ Copied

Replace `zabbix/zabbix-server-mysql` with the name of the required docker repository.

This command will pull the latest stable Zabbix component version based on the Alpine Linux OS. You can append tags to the repository name to get an image based on another operating system or of the specific Zabbix major or minor version.

The following repositories are available in Docker Hub:

_Zabbix agent_ | [zabbix/zabbix-agent](https://hub.docker.com/r/zabbix/zabbix-agent/)  
---|---  
_Zabbix server_  
| with MySQL support | [zabbix/zabbix-server-mysql](https://hub.docker.com/r/zabbix/zabbix-server-mysql/)  
with PostgreSQL support | [zabbix/zabbix-server-pgsql](https://hub.docker.com/r/zabbix/zabbix-server-pgsql/)  
_Zabbix web interface_  
| based on Apache2 web server with MySQL support | [zabbix/zabbix-web-apache-mysql](https://hub.docker.com/r/zabbix/zabbix-web-apache-mysql/)  
based on Apache2 web server with PostgreSQL support | [zabbix/zabbix-web-apache-pgsql](https://hub.docker.com/r/zabbix/zabbix-web-apache-pgsql/)  
based on Nginx web server with MySQL support | [zabbix/zabbix-web-nginx-mysql](https://hub.docker.com/r/zabbix/zabbix-web-nginx-mysql/)  
based on Nginx web server with PostgreSQL support | [zabbix/zabbix-web-nginx-pgsql](https://hub.docker.com/r/zabbix/zabbix-web-nginx-pgsql/)  
_Zabbix proxy_  
| with SQLite3 support | [zabbix/zabbix-proxy-sqlite3](https://hub.docker.com/r/zabbix/zabbix-proxy-sqlite3/)  
with MySQL support | [zabbix/zabbix-proxy-mysql](https://hub.docker.com/r/zabbix/zabbix-proxy-mysql/)  
_Zabbix Java gateway_ | [zabbix/zabbix-java-gateway](https://hub.docker.com/r/zabbix/zabbix-java-gateway/)  
  
SNMP trap support is provided in a separate repository [zabbix/zabbix-snmptraps](https://hub.docker.com/r/zabbix/zabbix-snmptraps/). It can be linked with Zabbix server and Zabbix proxy.

#### Tags

Official Zabbix component images may contain the following tags:

latest | The latest stable version of a Zabbix component based on Alpine Linux image. | zabbix-agent:latest  
---|---|---  
<OS>-trunk | The latest nightly build of the Zabbix version that is currently being developed on a specific operating system.   
  
**< OS>** \- the base operating system. Supported values:   
_alpine_ \- Alpine Linux;   
_ltsc2019_ \- Windows 10 LTSC 2019 (agent only);   
_ol_ \- Oracle Linux;   
_ltsc2022_ \- Windows 11 LTSC 2022 (agent only);   
_ubuntu_ \- Ubuntu | zabbix-agent:ubuntu-trunk  
<OS>-latest | The latest stable version of a Zabbix component on a specific operating system.   
  
**< OS>** \- the base operating system. Supported values:   
_alpine_ \- Alpine Linux;   
_ltsc2019_ \- Windows 10 LTSC 2019 (agent only);   
_ol_ \- Oracle Linux;   
_ltsc2022_ \- Windows 11 LTSC 2022 (agent only);   
_ubuntu_ \- Ubuntu | zabbix-agent:ol-latest  
<OS>-X.X-latest | The latest minor version of a Zabbix component of a specific major version and operating system.   
  
**< OS>** \- the base operating system. Supported values:   
_alpine_ \- Alpine Linux;   
_ltsc2019_ \- Windows 10 LTSC 2019 (agent only);   
_ol_ \- Oracle Linux;   
_ltsc2022_ \- Windows 11 LTSC 2022 (agent only);   
_ubuntu_ \- Ubuntu  
  
**X.X** \- the major Zabbix version (i.e. _6.0_ , _7.0_ , _7.4_). | zabbix-agent:alpine-7.4-latest  
<OS>-X.X.* | The latest minor version of a Zabbix component of a specific major version and operating system.   
  
**< OS>** \- the base operating system. Supported values:   
_alpine_ \- Alpine Linux;   
_ltsc2019_ \- Windows 10 LTSC 2019 (agent only);   
_ol_ \- Oracle Linux;   
_ltsc2022_ \- Windows 11 LTSC 2022 (agent only);   
_ubuntu_ \- Ubuntu  
  
**X.X** \- the major Zabbix version (i.e. _6.0_ , _7.0_ , _7.4_).   
  
***** \- the Zabbix minor version | zabbix-agent:alpine-7.4.1  
  
#### Initial configuration

After downloading the images, start the containers by executing `docker run` command followed by additional arguments to specify required environment variables and/or mount points. Some configuration examples are provided below.

To enable communication between Zabbix components, some ports, such as 10051/TCP for Zabbix server (trapper), 10050/TCP for Zabbix agent, 162/UDP for SNMP traps and 80/TCP for Zabbix web interface will be exposed to a host machine. Full list of default ports used by Zabbix components is available on the [Requirements](/documentation/current/en/manual/installation/requirements#default-port-numbers) page. For Zabbix server and agent the default port can be changed by setting ZBX_LISTENPORT environment variable.

##### Environment variables

All Zabbix component images provide environment variables to control configuration. Supported environment variables are listed in the component repository.

These environment variables are options from Zabbix configuration files, but with different naming method. For example, `ZBX_LOGSLOWQUERIES` is equal to `LogSlowQueries` from Zabbix [server](/documentation/current/en/manual/appendix/config/zabbix_server#logslowqueries) or Zabbix [proxy](/documentation/current/en/manual/appendix/config/zabbix_proxy#logslowqueries) configuration files.

Some configuration options (e.g., `PIDFile` and `LogType`) cannot be changed.

The following environment variables are specific to Docker components and do not exist in Zabbix configuration files:

`DB_SERVER_HOST` | Server  
Proxy  
Web interface | `mysql-server` for MYSQL   
`postgres-server` for PostgreSQL | IP or DNS name of MySQL or PostgreSQL server.  
---|---|---|---  
`DB_SERVER_PORT` | Server  
Proxy  
Web interface | `3306` for MYSQL   
`5432` for PostgreSQL | Port of MySQL or PostgreSQL server.  
`MYSQL_USER` | Server  
Proxy  
Web-interface | `zabbix` | MySQL database user.  
`MYSQL_PASSWORD` | Server  
Proxy  
Web interface | `zabbix` | MySQL database password.  
`MYSQL_DATABASE` | Server  
Proxy  
Web interface | `zabbix` for Zabbix server   
`zabbix_proxy` for Zabbix proxy | Zabbix database name.  
`POSTGRES_USER` | Server  
Web interface | `zabbix` | PostgreSQL database user.  
`POSTGRES_PASSWORD` | Server  
Web interface | `zabbix` | PostgreSQL database password.  
`POSTGRES_DB` | Server  
Web interface | `zabbix` for Zabbix server   
`zabbix_proxy` for Zabbix proxy | Zabbix database name.  
`PHP_TZ` | Web-interface | `Europe/Riga` | Timezone in PHP format. Full list of supported timezones is available on [php.net](http://php.net/manual/en/timezones.php).  
`ZBX_SERVER_NAME` | Web interface | `Zabbix Docker` | Visible Zabbix installation name in upper-right corner of the web interface.  
`ZBX_JAVAGATEWAY_ENABLE` | Server  
Proxy | `false` | Enables communication with Zabbix Java gateway to collect Java related checks.  
`ZBX_ENABLE_SNMP_TRAPS` | Server  
Proxy | `false` | Enables SNMP trap feature. It requires **zabbix-snmptraps** instance and shared volume _/var/lib/zabbix/snmptraps_ to Zabbix server or Zabbix proxy.  
  
##### Volumes

The images allow to mount volumes using the following mount points:

**Zabbix agent**  
---  
| _/etc/zabbix/zabbix_agentd.d_ | The volume allows to include _*.conf_ files and extend Zabbix agent using the `UserParameter` feature  
_/var/lib/zabbix/modules_ | The volume allows to load additional modules and extend Zabbix agent using the [LoadModule](/documentation/current/en/manual/extensions/loadablemodules) feature  
_/var/lib/zabbix/enc_ | The volume is used to store TLS-related files. These file names are specified using `ZBX_TLSCAFILE`, `ZBX_TLSCRLFILE`, `ZBX_TLSKEY_FILE` and `ZBX_TLSPSKFILE` environment variables  
**Zabbix server**  
| _/usr/lib/zabbix/alertscripts_ | The volume is used for custom alert scripts. It is the `AlertScriptsPath` parameter in [zabbix_server.conf](/documentation/current/en/manual/appendix/config/zabbix_server)  
_/usr/lib/zabbix/externalscripts_ | The volume is used by [external checks](/documentation/current/en/manual/config/items/itemtypes/external). It is the `ExternalScripts` parameter in [zabbix_server.conf](/documentation/current/en/manual/appendix/config/zabbix_server)  
_/var/lib/zabbix/modules_ | The volume allows to load additional modules and extend Zabbix server using the [LoadModule](/documentation/current/en/manual/extensions/loadablemodules) feature  
_/var/lib/zabbix/enc_ | The volume is used to store TLS related files. These file names are specified using `ZBX_TLSCAFILE`, `ZBX_TLSCRLFILE`, `ZBX_TLSKEY_FILE` and `ZBX_TLSPSKFILE` environment variables  
_/var/lib/zabbix/ssl/certs_ | The volume is used as location of SSL client certificate files for client authentication. It is the `SSLCertLocation` parameter in zabbix_server.conf  
_/var/lib/zabbix/ssl/keys_ | The volume is used as location of SSL private key files for client authentication. It is the `SSLKeyLocation` parameter in [zabbix_server.conf](/documentation/current/en/manual/appendix/config/zabbix_server)  
_/var/lib/zabbix/ssl/ssl_ca_ | The volume is used as location of certificate authority (CA) files for SSL server certificate verification. It is the `SSLCALocation` parameter in [zabbix_server.conf](/documentation/current/en/manual/appendix/config/zabbix_server)  
_/var/lib/zabbix/snmptraps_ | The volume is used as location of snmptraps.log file. It could be shared by zabbix-snmptraps container and inherited using the volumes_from Docker option while creating a new instance of Zabbix server. SNMP trap processing feature could be enabled by using shared volume and switching the `ZBX_ENABLE_SNMP_TRAPS` environment variable to 'true'  
_/var/lib/zabbix/mibs_ | The volume allows to add new MIB files. It does not support subdirectories, all MIBs must be placed in `/var/lib/zabbix/mibs`  
**Zabbix proxy**  
| _/usr/lib/zabbix/externalscripts_ | The volume is used by [external checks](/documentation/current/en/manual/config/items/itemtypes/external). It is the `ExternalScripts` parameter in [zabbix_proxy.conf](/documentation/current/en/manual/appendix/config/zabbix_proxy)  
_/var/lib/zabbix/db_data/_ | The volume allows to store database files on external devices. Supported only for Zabbix proxy with SQLite3  
_/var/lib/zabbix/modules_ | The volume allows to load additional modules and extend Zabbix server using the [LoadModule](/documentation/current/en/manual/extensions/loadablemodules) feature  
_/var/lib/zabbix/enc_ | The volume is used to store TLS related files. These file names are specified using `ZBX_TLSCAFILE`, `ZBX_TLSCRLFILE`, `ZBX_TLSKEY_FILE` and `ZBX_TLSPSKFILE` environment variables  
_/var/lib/zabbix/ssl/certs_ | The volume is used as location of SSL client certificate files for client authentication. It is the `SSLCertLocation` parameter in [zabbix_proxy.conf](/documentation/current/en/manual/appendix/config/zabbix_proxy)  
_/var/lib/zabbix/ssl/keys_ | The volume is used as location of SSL private key files for client authentication. It is the `SSLKeyLocation` parameter in [zabbix_proxy.conf](/documentation/current/en/manual/appendix/config/zabbix_proxy)  
_/var/lib/zabbix/ssl/ssl_ca_ | The volume is used as location of certificate authority (CA) files for SSL server certificate verification. It is the `SSLCALocation` parameter in [zabbix_proxy.conf](/documentation/current/en/manual/appendix/config/zabbix_proxy)  
_/var/lib/zabbix/snmptraps_ | The volume is used as location of snmptraps.log file. It could be shared by the zabbix-snmptraps container and inherited using the volumes_from Docker option while creating a new instance of Zabbix server. SNMP trap processing feature could be enabled by using shared volume and switching the `ZBX_ENABLE_SNMP_TRAPS` environment variable to 'true'  
_/var/lib/zabbix/mibs_ | The volume allows to add new MIB files. It does not support subdirectories, all MIBs must be placed in `/var/lib/zabbix/mibs`  
**Zabbix web interface based on Apache2 web server**  
| _/etc/ssl/apache2_ | The volume allows to enable HTTPS for Zabbix web interface. The volume must contain the two `ssl.crt` and `ssl.key` files prepared for Apache2 SSL connections  
**Zabbix web interface based on Nginx web server**  
| _/etc/ssl/nginx_ | The volume allows to enable HTTPS for Zabbix web interface. The volume must contain the two `ssl.crt`, `ssl.key` files and `dhparam.pem` prepared for Nginx SSL connections  
**Zabbix snmptraps**  
| _/var/lib/zabbix/snmptraps_ | The volume contains the `snmptraps.log` log file named with received SNMP traps  
_/var/lib/zabbix/mibs_ | The volume allows to add new MIB files. It does not support subdirectories, all MIBs must be placed in `/var/lib/zabbix/mibs`  
  
For additional information, see Zabbix official repositories in Docker Hub.

##### Examples

**Example 1**

The example demonstrates how to run Zabbix server with MySQL database support, Zabbix web interface based on the Nginx web server and Zabbix Java gateway.

1\. Create network dedicated for Zabbix component containers:
    
    
    docker network create --subnet 172.20.0.0/16 --ip-range 172.20.240.0/20 zabbix-net

Copy

✔ Copied

2\. Start empty MySQL server instance:

For MySQL versions 8.4+, `caching_sha2_password` should be used instead of `mysql_native_password`.
    
    
    docker run --name mysql-server -t \
                 -e MYSQL_DATABASE="zabbix" \
                 -e MYSQL_USER="zabbix" \
                 -e MYSQL_PASSWORD="zabbix_pwd" \
                 -e MYSQL_ROOT_PASSWORD="root_pwd" \
                 --network=zabbix-net \
                 --restart unless-stopped \
                 -d mysql:8.0-oracle \
                 --character-set-server=utf8 --collation-server=utf8_bin \
                 --default-authentication-plugin=mysql_native_password

Copy

✔ Copied

3\. Start Zabbix Java gateway instance:
    
    
    docker run --name zabbix-java-gateway -t \
                 --network=zabbix-net \
                 --restart unless-stopped \
                 -d zabbix/zabbix-java-gateway:alpine-7.4-latest

Copy

✔ Copied

4\. Start Zabbix server instance and link the instance with created MySQL server instance:
    
    
    docker run --name zabbix-server-mysql -t \
                 -e DB_SERVER_HOST="mysql-server" \
                 -e MYSQL_DATABASE="zabbix" \
                 -e MYSQL_USER="zabbix" \
                 -e MYSQL_PASSWORD="zabbix_pwd" \
                 -e MYSQL_ROOT_PASSWORD="root_pwd" \
                 -e ZBX_JAVAGATEWAY="zabbix-java-gateway" \
                 --network=zabbix-net \
                 -p 10051:10051 \
                 --restart unless-stopped \
                 -d zabbix/zabbix-server-mysql:alpine-7.4-latest

Copy

✔ Copied

5\. Start Zabbix web interface and link the instance with created MySQL server and Zabbix server instances:
    
    
    docker run --name zabbix-web-nginx-mysql -t \
                 -e ZBX_SERVER_HOST="zabbix-server-mysql" \
                 -e DB_SERVER_HOST="mysql-server" \
                 -e MYSQL_DATABASE="zabbix" \
                 -e MYSQL_USER="zabbix" \
                 -e MYSQL_PASSWORD="zabbix_pwd" \
                 -e MYSQL_ROOT_PASSWORD="root_pwd" \
                 --network=zabbix-net \
                 -p 80:8080 \
                 --restart unless-stopped \
                 -d zabbix/zabbix-web-nginx-mysql:alpine-7.4-latest

Copy

✔ Copied

**Example 2**

The example demonstrates how to run Zabbix server with PostgreSQL database support, Zabbix web interface based on the Nginx web server and SNMP trap feature.

1\. Create network dedicated for Zabbix component containers:
    
    
    docker network create --subnet 172.20.0.0/16 --ip-range 172.20.240.0/20 zabbix-net

Copy

✔ Copied

2\. Start empty PostgreSQL server instance:
    
    
    docker run --name postgres-server -t \
                 -e POSTGRES_USER="zabbix" \
                 -e POSTGRES_PASSWORD="zabbix_pwd" \
                 -e POSTGRES_DB="zabbix" \
                 --network=zabbix-net \
                 --restart unless-stopped \
                 -d postgres:latest

Copy

✔ Copied

3\. Start Zabbix snmptraps instance:
    
    
    docker run --name zabbix-snmptraps -t \
                 -v /zbx_instance/snmptraps:/var/lib/zabbix/snmptraps:rw \
                 -v /var/lib/zabbix/mibs:/usr/share/snmp/mibs:ro \
                 --network=zabbix-net \
                 -p 162:1162/udp \
                 --restart unless-stopped \
                 -d zabbix/zabbix-snmptraps:alpine-7.4-latest

Copy

✔ Copied

4\. Start Zabbix server instance and link the instance with created PostgreSQL server instance:
    
    
    docker run --name zabbix-server-pgsql -t \
                 -e DB_SERVER_HOST="postgres-server" \
                 -e POSTGRES_USER="zabbix" \
                 -e POSTGRES_PASSWORD="zabbix_pwd" \
                 -e POSTGRES_DB="zabbix" \
                 -e ZBX_ENABLE_SNMP_TRAPS="true" \
                 --network=zabbix-net \
                 -p 10051:10051 \
                 --volumes-from zabbix-snmptraps \
                 --restart unless-stopped \
                 -d zabbix/zabbix-server-pgsql:alpine-7.4-latest

Copy

✔ Copied

5\. Start Zabbix web interface and link the instance with created PostgreSQL server and Zabbix server instances:
    
    
    docker run --name zabbix-web-nginx-pgsql -t \
                 -e ZBX_SERVER_HOST="zabbix-server-pgsql" \
                 -e DB_SERVER_HOST="postgres-server" \
                 -e POSTGRES_USER="zabbix" \
                 -e POSTGRES_PASSWORD="zabbix_pwd" \
                 -e POSTGRES_DB="zabbix" \
                 --network=zabbix-net \
                 -p 443:8443 \
                 -p 80:8080 \
                 -v /etc/ssl/nginx:/etc/ssl/nginx:ro \
                 --restart unless-stopped \
                 -d zabbix/zabbix-web-nginx-pgsql:alpine-7.4-latest

Copy

✔ Copied

**Example 3**

The example demonstrates how to run Zabbix server with MySQL database support, Zabbix web interface based on the Nginx web server and Zabbix Java gateway using `podman` on Red Hat 8.

1\. Create new pod with name `zabbix` and exposed ports (web-interface, Zabbix server trapper):
    
    
    podman pod create --name zabbix -p 80:8080 -p 10051:10051

Copy

✔ Copied

2\. (optional) Start Zabbix agent container in `zabbix` pod location:
    
    
    podman run --name zabbix-agent \
               -e ZBX_SERVER_HOST="127.0.0.1,localhost" \
               --restart=always \
               --pod=zabbix \
               -d registry.connect.redhat.com/zabbix/zabbix-agent-70:latest

Copy

✔ Copied

3\. Create `./mysql/` directory on host and start Oracle MySQL server 8.0:

For MySQL versions 8.4+, `caching_sha2_password` should be used instead of `mysql_native_password`.
    
    
    podman run --name mysql-server -t \
                 -e MYSQL_DATABASE="zabbix" \
                 -e MYSQL_USER="zabbix" \
                 -e MYSQL_PASSWORD="zabbix_pwd" \
                 -e MYSQL_ROOT_PASSWORD="root_pwd" \
                 -v ./mysql/:/var/lib/mysql/:Z \
                 --restart=always \
                 --pod=zabbix \
                 -d mysql:8.0 \
                 --character-set-server=utf8 --collation-server=utf8_bin \
                 --default-authentication-plugin=mysql_native_password

Copy

✔ Copied

4\. Start Zabbix server container:
    
    
    podman run --name zabbix-server-mysql -t \
                             -e DB_SERVER_HOST="127.0.0.1" \
                             -e MYSQL_DATABASE="zabbix" \
                             -e MYSQL_USER="zabbix" \
                             -e MYSQL_PASSWORD="zabbix_pwd" \
                             -e MYSQL_ROOT_PASSWORD="root_pwd" \
                             -e ZBX_JAVAGATEWAY="127.0.0.1" \
                             --restart=always \
                             --pod=zabbix \
                             -d registry.connect.redhat.com/zabbix/zabbix-server-mysql-70

Copy

✔ Copied

5\. Start Zabbix Java Gateway container:
    
    
    podman run --name zabbix-java-gateway -t \
                 --restart=always \
                 --pod=zabbix \
                 -d registry.connect.redhat.com/zabbix/zabbix-java-gateway-70

Copy

✔ Copied

6\. Start Zabbix web-interface container:
    
    
    podman run --name zabbix-web-mysql -t \
                             -e ZBX_SERVER_HOST="127.0.0.1" \
                             -e DB_SERVER_HOST="127.0.0.1" \
                             -e MYSQL_DATABASE="zabbix" \
                             -e MYSQL_USER="zabbix" \
                             -e MYSQL_PASSWORD="zabbix_pwd" \
                             -e MYSQL_ROOT_PASSWORD="root_pwd" \
                             --restart=always \
                             --pod=zabbix \
                             -d registry.connect.redhat.com/zabbix/zabbix-web-mysql-70

Copy

✔ Copied

Pod `zabbix` exposes 80/TCP port (HTTP) to host machine from 8080/TCP of `zabbix-web-mysql` container.

### Docker Compose

Alternatively, Zabbix can be installed using Docker Compose plugin. Compose files for defining and running multi-container Zabbix components are available in the official [Zabbix Docker repository](https://github.com/zabbix/zabbix-docker) on GitHub.

Official Zabbix compose files support version 3 of Docker Compose.

These compose files are added as examples; they are overloaded. For example, they contain proxies with both MySQL and SQLite3 support.

To obtain Docker compose files provided by Zabbix, clone the repository:
    
    
    git clone https://github.com/zabbix/zabbix-docker.git

Copy

✔ Copied

Switch to the required version:
    
    
    git checkout 7.4

Copy

✔ Copied

Compose configuration files and create and start containers:
    
    
    docker compose -f ./docker-compose_v3_alpine_mysql_latest.yaml up

Copy

✔ Copied

Replace `docker-compose_v3_alpine_mysql_latest.yaml` in the command above with the required configuration file.

The following options are available:

`docker-compose_v3_alpine_mysql_latest.yaml` | The compose file runs the latest version of Zabbix 7.4 components on Alpine Linux with MySQL database support.  
---|---  
`docker-compose_v3_alpine_mysql_local.yaml` | The compose file locally builds the latest version of Zabbix 7.4 and runs Zabbix components on Alpine Linux with MySQL database support.  
`docker-compose_v3_alpine_pgsql_latest.yaml` | The compose file runs the latest version of Zabbix 7.4 components on Alpine Linux with PostgreSQL database support.  
`docker-compose_v3_alpine_pgsql_local.yaml` | The compose file locally builds the latest version of Zabbix 7.4 and runs Zabbix components on Alpine Linux with PostgreSQL database support.  
`docker-compose_v3_ol_mysql_latest.yaml` | The compose file runs the latest version of Zabbix 7.4 components on Oracle Linux with MySQL database support.  
`docker-compose_v3_ol_mysql_local.yaml` | The compose file locally builds the latest version of Zabbix 7.4 and runs Zabbix components on Oracle Linux with MySQL database support.  
`docker-compose_v3_ol_pgsql_latest.yaml` | The compose file runs the latest version of Zabbix 7.4 components on Oracle Linux with PostgreSQL database support.  
`docker-compose_v3_ol_pgsql_local.yaml` | The compose file locally builds the latest version of Zabbix 7.4 and runs Zabbix components on Oracle Linux with PostgreSQL database support.  
`docker-compose_v3_ubuntu_mysql_latest.yaml` | The compose file runs the latest version of Zabbix 7.4 components on Ubuntu 22.04 with MySQL database support.  
`docker-compose_v3_ubuntu_mysql_local.yaml` | The compose file locally builds the latest version of Zabbix 7.4 and runs Zabbix components on Ubuntu 22.04 with MySQL database support.  
`docker-compose_v3_ubuntu_pgsql_latest.yaml` | The compose file runs the latest version of Zabbix 7.4 components on Ubuntu 22.04 with PostgreSQL database support.  
`docker-compose_v3_ubuntu_pgsql_local.yaml` | The compose file locally builds the latest version of Zabbix 7.4 and runs Zabbix components on Ubuntu 22.04 with PostgreSQL database support.  
  
#### Storage

Compose files are configured to support local storage on a host machine. Docker Compose will create a `zbx_env` directory in the folder with the compose file when you run Zabbix components using the compose file. The directory will contain the same structure as described in the Volumes section and directory for database storage.

There are also volumes in read-only mode for `/etc/localtime` and `/etc/timezone` files.

#### Environment variables

The variable files have the following naming structure: `.env_<type of component>` and are located in the _env_vars_ [directory](https://github.com/zabbix/zabbix-docker/tree/trunk/env_vars). See environment variables for details about variable naming and available selection.

#### Examples

**Example 1**
    
    
    git checkout 7.4
           docker compose -f ./docker-compose_v3_alpine_mysql_latest.yaml up -d

Copy

✔ Copied

The command will download the latest Zabbix 7.4 images for each Zabbix component and run them in detach mode.

Do not forget to download `.env_<type of component>` files from github.com official Zabbix repository with compose files.

**Example 2**
    
    
    git checkout 7.4
           docker compose -f ./docker-compose_v3_ubuntu_mysql_local.yaml up -d

Copy

✔ Copied

The command will download base image Ubuntu 24.04 (noble), then build Zabbix 7.4 components locally and run them in detach mode.