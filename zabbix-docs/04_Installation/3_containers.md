---
title: Upgrade from containers
source: https://www.zabbix.com/documentation/current/en/manual/installation/upgrade/containers
downloaded: 2025-11-14 10:34:18
---

# 3 Upgrade from containers

### Overview

This section describes steps required for a successful [upgrade](/documentation/current/en/manual/installation/upgrade) to Zabbix **7.4**.x containers.

Separate sets of instructions are available for upgrading individual Zabbix component images and Docker compose files.

Before the upgrade make sure to read the relevant [**upgrade notes**](/documentation/current/en/manual/installation/upgrade)!

Before starting the upgrade, verify that users have the necessary permissions to the database for upgrading purposes.  

For upgrades from Zabbix 6.0 or older, deterministic triggers will need to be created during the upgrade. If binary logging is enabled for MySQL/MariaDB, this requires superuser privileges or setting the variable/configuration parameter _log_bin_trust_function_creators = 1_. See [Database creation scripts](/documentation/current/en/manual/appendix/install/db_scripts#mysqlmariadb) for instructions how to set the variable.  
Note that if executing from a console, the variable will only be set temporarily and will be dropped when a Docker is restarted. In this case, keep your SQL service running, only stop zabbix-server service by running 'docker compose down zabbix-server' and then 'docker compose up -d zabbix-server'.  
Alternatively, you can set this variable in the configuration file.

Depending on the size of a database upgrade to version 7.4 may take quite a long time.

### Zabbix image upgrade

The steps listed below can be used to upgrade any Zabbix component. Replace `zabbix-server-mysql` with the required component image name.

1\. Check current image version:
    
    
    docker inspect -f '{{ .Config.Image }}' zabbix-server-mysql

Copy

✔ Copied

2\. Pull desired image version, for example:
    
    
    docker pull zabbix/zabbix-server-mysql:alpine-7.4-latest

Copy

✔ Copied

`zabbix/zabbix-server-mysql:alpine-7.4-latest` will pull the latest released minor version of Zabbix server 7.4 with MySQL support based on Alpine Linux. Replace it with the name of the Docker repository and tags combination you need. See [Installation from containers](/documentation/current/en/manual/installation/containers#docker) for a list of available options.

3\. Stop the container:
    
    
    docker stop zabbix-server-mysql

Copy

✔ Copied

4\. Remove the container:
    
    
    docker rm zabbix-server-mysql

Copy

✔ Copied

5\. Launch the updated container by executing `docker run` command followed by additional arguments to specify required [environment variables](/documentation/current/en/manual/installation/containers#environment-variables) and/or [mount points](/documentation/current/en/manual/installation/containers#volumes).

**Configuration examples**

Zabbix server with MySQL:
    
    
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

Zabbix server with PostgreSQL:
    
    
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

More configuration examples, including examples for other Zabbix components, are available on the [Installation from containers](/documentation/current/en/manual/installation/containers#examples) page.

6\. Verify the update:
    
    
    docker logs -f zabbix-server-mysql

Copy

✔ Copied

### Compose files

Follow upgrade instructions in this section, if you installed Zabbix using [compose file](/documentation/current/en/manual/installation/containers#docker-compose).

1\. Check current image version:
    
    
    docker inspect -f '{{ .Config.Image }}' zabbix-server-mysql

Copy

✔ Copied

2\. Pull the latest updates from the GitHub [repository](https://github.com/zabbix/zabbix-docker) and switch to the required branch:
    
    
    git pull
           git checkout 7.4

Copy

✔ Copied

3\. Start Zabbix components using new compose file:
    
    
    docker-compose -f ./docker-compose_v3_alpine_mysql_latest.yaml up -d

Copy

✔ Copied

4\. Verify the update:
    
    
    docker logs -f zabbix-server-mysql

Copy

✔ Copied

See [Installation from containers](/documentation/current/en/manual/installation/containers#docker-compose) for more details, including lists of supported environment variables and volume mount points.