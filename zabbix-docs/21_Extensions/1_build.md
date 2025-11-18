---
title: Building loadable plugins
source: https://www.zabbix.com/documentation/current/en/manual/extensions/plugins/build
downloaded: 2025-11-14 10:46:20
---

# 1 Building loadable plugins

### Overview

This page provides the steps required to build a loadable plugin binary from the sources.

If the source tarball is downloaded, it is possible to build the plugin offline, i.e. without the internet connection.

The PostgreSQL plugin is used as an example. Other loadable plugins can be built in a similar way.

### Steps

**1**. Download the plugin sources from [Zabbix Cloud Images and Appliances](https://cdn.zabbix.com/zabbix-agent2-plugins/sources/). The official download page will be available soon.

**2**. Transfer the archive to the machine where you are going to build the plugin.

**3**. Unarchive the tarball, e.g.:
    
    
    tar xvf zabbix-agent2-plugin-postgresql-1.0.0.tar.gz

Copy

✔ Copied

Make sure to replace "zabbix-agent2-plugin-postgresql-1.0.0.tar.gz" with the name of the downloaded archive.

**4**. Enter the extracted directory:
    
    
    cd <path to directory>

Copy

✔ Copied

**5**. Run:
    
    
    make

Copy

✔ Copied

**6**. The plugin executable may be placed anywhere as long as it is loadable by Zabbix agent 2. Specify the path to the plugin binary in the plugin configuration file, e.g. in postgresql.conf for the PostgreSQL plugin:
    
    
    Plugins.PostgreSQL.System.Path=/path/to/executable/zabbix-agent2-plugin-postgresql

Copy

✔ Copied

**7**. Path to the plugin configuration file must be specified in the Include parameter of the Zabbix agent 2 configuration file:
    
    
    Include=/path/to/plugin/configuration/file/postgresql.conf

Copy

✔ Copied

### Makefile targets

Loadable plugins provided by Zabbix have simple makefiles with the following targets:

make | Build plugin.  
---|---  
make clean | Delete all files that are normally created by building the plugin.  
make check | Perform self-tests. A real PostgreSQL database is required.  
make style | Check Go code style with 'golangci-lint'.  
make format | Format Go code with 'go fmt'.  
make dist | Create an archive containing the plugin sources and sources of all packages needed to build the plugin and its self-tests.