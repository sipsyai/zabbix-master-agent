---
title: Installation from sources
source: https://www.zabbix.com/documentation/current/en/manual/installation/install
downloaded: 2025-11-14 10:34:03
---

# 3 Installation from sources

You can get the very latest version of Zabbix by compiling it from the sources.

A step-by-step tutorial for installing Zabbix from the sources is provided here.

#### 1 Installing Zabbix daemons

##### 1 Download the source archive

Go to the [Zabbix download page](http://www.zabbix.com/download_sources) and download the source archive. Once downloaded, extract the sources, by running:
    
    
    tar -zxvf zabbix-7.4.0.tar.gz

Copy

✔ Copied

Enter the correct Zabbix version in the command. It must match the name of the downloaded archive.

##### 2 Create user account

All Zabbix daemon processes run under unprivileged system users. If a Zabbix daemon is started from an unprivileged user account, it will continue running as that user.

In the default configuration, if a daemon is started as `root`, it will switch to the `zabbix` user account, which must be present. To create a `zabbix` system user and group, run the commands listed below.

RedHat-based system:
    
    
    groupadd --system zabbix
           useradd --system -g zabbix -d /usr/lib/zabbix -s /sbin/nologin -c "Zabbix Monitoring System" zabbix

Copy

✔ Copied

Debian-based system:
    
    
    addgroup --system --quiet zabbix
           adduser --quiet --system --disabled-login --ingroup zabbix --home /var/lib/zabbix --no-create-home zabbix

Copy

✔ Copied

There is no need to create a separate user account for Zabbix frontend.

###### Security recommendation

If the Zabbix [server](/documentation/current/en/manual/concepts/server) and [agent](/documentation/current/en/manual/concepts/agent) run on the same machine, it is recommended to run them under **separate user accounts**. Running both as the same user allows the agent to access the server's configuration file, which could expose sensitive information—such as the database password—to any Admin-level user in Zabbix.

Running Zabbix as `root`, `bin`, or any other account with special rights is a security risk.

###### Home directory (optional)

Zabbix processes do not require a home directory, so creating one is generally not recommended. However, if you need functionality that requires a home directory (for example, storing MySQL credentials in $HOME/.my.cnf), you can create it using the commands listed below.

On RedHat-based systems, run:
    
    
    mkdir -m u=rwx,g=rwx,o= -p /usr/lib/zabbix
           chown zabbix:zabbix /usr/lib/zabbix

Copy

✔ Copied

On Debian-based systems, run:
    
    
    mkdir -m u=rwx,g=rwx,o= -p /var/lib/zabbix
           chown zabbix:zabbix /var/lib/zabbix

Copy

✔ Copied

##### 3 Create Zabbix database

For Zabbix [server](/documentation/current/en/manual/concepts/server) and [proxy](/documentation/current/en/manual/concepts/proxy) daemons, as well as Zabbix frontend, a database is required. It is not needed to run Zabbix [agent](/documentation/current/en/manual/concepts/agent).

SQL [scripts are provided](/documentation/current/en/manual/appendix/install/db_scripts) for creating database schema and inserting the dataset. Zabbix proxy database needs only the schema while Zabbix server database requires also the dataset on top of the schema.

Having created a Zabbix database, proceed to the following steps of compiling Zabbix.

##### 4 Configure the sources

C99 with GNU extensions is required for building Zabbix server, Zabbix proxy or Zabbix agent. This version can be explicitly specified by setting CFLAGS="-std=gnu99":
    
    
    export CFLAGS="-std=gnu99"

Copy

✔ Copied

If installing from [Zabbix Git repository](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse?at=refs%2Fheads%2Frelease%2F7.4), it is required to run first:  

`./bootstrap.sh`

When configuring the sources for a Zabbix server or proxy, you must specify the database type to be used. Only one database type can be compiled with a server or proxy process at a time.

To see all of the supported configuration options, inside the extracted Zabbix source directory run:
    
    
    ./configure --help

Copy

✔ Copied

To configure the sources for a Zabbix server and agent, you may run something like:
    
    
    ./configure --enable-server --enable-agent --with-mysql --enable-ipv6 --with-net-snmp --with-libcurl --with-libxml2 --with-openipmi --with-ares

Copy

✔ Copied

To configure the sources for a Zabbix server (with PostgreSQL etc.), you may run:
    
    
    ./configure --enable-server --with-postgresql --with-net-snmp

Copy

✔ Copied

To configure the sources for a Zabbix proxy (with SQLite etc.), you may run:
    
    
    ./configure --prefix=/usr --enable-proxy --with-net-snmp --with-sqlite3 --with-ssh2

Copy

✔ Copied

To configure the sources for a Zabbix agent, you may run:
    
    
    ./configure --enable-agent

Copy

✔ Copied

or, for Zabbix agent 2:
    
    
    ./configure --enable-agent2

Copy

✔ Copied

A configured Go environment with a [supported Go version](/documentation/current/en/manual/installation/requirements#agent-2) is required for building Zabbix agent 2.

Notes on compilation options:

  * `--enable-agent` \- compiles Zabbix agent, as well as [Zabbix get](/documentation/current/en/manual/concepts/get) and [Zabbix sender](/documentation/current/en/manual/concepts/sender) command-line utilities.
  * `--with-libcurl` \- required for virtual machine monitoring, SMTP authentication, and `web.page.*` [Zabbix agent items](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent). See also: [Requirements](/documentation/current/en/manual/installation/requirements#serverproxy) (libcurl).
  * `--with-libxml2` \- required for virtual machine monitoring.
  * `--with-libpcre2[=DIR]` \- Zabbix always compiles with the PCRE2 library; this option only allows to specify a custom PCRE2 installation path.
  * `--with-mysql=/path/to/mysql_config` \- specifies the path to a particular MySQL client library configuration. Useful when multiple versions of MySQL or MariaDB are installed.
  * `--enable-static` \- statically links libraries (not supported on [Solaris](https://docs.oracle.com/cd/E18659_01/html/821-1383/bkajp.html)). Use this if you plan to distribute compiled binaries to systems without the required libraries. Not recommended when building Zabbix server. To build the server statically, a static version of every external library is required. The configure script does not check for this automatically.
  * `--with-stacksize=<value>` \- sets the per-thread stack size in kilobytes (e.g., `--with-stacksize=512`). You can increase this value if Zabbix crashes or freezes due to stack overflows (e.g., during [preprocessing](/documentation/current/en/manual/config/items/preprocessing) on systems with low default thread stack limits).

If `./configure` fails due to missing libraries or other issues, please check the `config.log` file for detailed error information.

For example, if `libssl` is missing, the immediate error message may be misleading:
    
    
    checking for main in -lmysqlclient... no
           configure: error: Not found mysqlclient library

Copy

✔ Copied

In this case, `config.log` reveals the actual cause:
    
    
    /usr/bin/ld: cannot find -lssl
           /usr/bin/ld: cannot find -lcrypto

Copy

✔ Copied

See also:

  * [Compiling Zabbix with encryption support](/documentation/current/en/manual/encryption#compiling-zabbix-with-encryption-support)
  * Known [compilation issues](/documentation/current/en/manual/installation/known_issues/compilation_issues)

##### 5 Make and install everything

If installing from [Zabbix Git repository](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse?at=refs%2Fheads%2Frelease%2F7.4), it is required to run first:  

`$ make dbschema`
    
    
    make install

Copy

✔ Copied

This step should be run as a user with sufficient permissions (commonly 'root', or by using `sudo`).

Running `make install` will by default install the daemon binaries (zabbix_server, zabbix_agentd, zabbix_proxy) in /usr/local/sbin and the client binaries (zabbix_get, zabbix_sender) in /usr/local/bin.

To specify a different location than /usr/local, use a --prefix key in the previous step of configuring sources, for example --prefix=/home/zabbix. In this case daemon binaries will be installed under <prefix>/sbin, while utilities under <prefix>/bin. Man pages will be installed under <prefix>/share.

##### 6 Review and edit configuration files

  * edit the Zabbix agent configuration file **/usr/local/etc/zabbix_agentd.conf**

You need to configure this file for every host with zabbix_agentd installed.

You must specify the Zabbix server **IP address** in the file. Connections from other hosts will be denied.

  * edit the Zabbix server configuration file **/usr/local/etc/zabbix_server.conf**

You must specify the database name, user and password (if using any).

The rest of the parameters will suit you with their defaults if you have a small installation (up to ten monitored hosts). You should change the default parameters if you want to maximize the performance of Zabbix server (or proxy) though.

  * if you have installed a Zabbix proxy, edit the proxy configuration file **/usr/local/etc/zabbix_proxy.conf**

You must specify the server IP address and proxy hostname (must be known to the server), as well as the database name, user and password (if using any).

With SQLite the full path to database file must be specified; DB user and password are not required.

##### 7 Start up the daemons

Run zabbix_server on the server side.
    
    
    zabbix_server

Copy

✔ Copied

Make sure that your system allows allocation of 36MB (or a bit more) of shared memory, otherwise the server may not start and you will see "Cannot allocate shared memory for <type of cache>." in the server log file. This may happen on FreeBSD, Solaris 8.  

Run zabbix_agentd on all the monitored machines.
    
    
    zabbix_agentd

Copy

✔ Copied

Make sure that your system allows allocation of 2MB of shared memory, otherwise the agent may not start and you will see "Cannot allocate shared memory for collector." in the agent log file. This may happen on Solaris 8.

If you have installed Zabbix proxy, run zabbix_proxy.
    
    
    zabbix_proxy

Copy

✔ Copied

#### 2 Installing Zabbix web interface

##### Copying PHP files

Zabbix frontend is written in PHP, so to run it a PHP supported webserver is needed. Installation is done by simply copying the PHP files from the ui directory to the webserver HTML documents directory.

Common locations of HTML documents directories for Apache web servers include:

  * /usr/local/apache2/htdocs (default directory when installing Apache from source)
  * /srv/www/htdocs (OpenSUSE, SLES)
  * /var/www/html (Debian, Ubuntu, Fedora, RHEL)

It is recommended to use a subdirectory instead of the HTML root. To create a subdirectory and copy Zabbix frontend files into it, execute the following commands, replacing the <htdocs> with actual directory:
    
    
    mkdir <htdocs>/zabbix
           cd ui
           cp -a . <htdocs>/zabbix

Copy

✔ Copied

If planning to use any other language than English, see [Installation of additional frontend languages](/documentation/current/en/manual/appendix/install/locales) for instructions.

##### Installing frontend

Please see [Web interface installation](/documentation/current/en/manual/installation/frontend) page for information about Zabbix frontend installation wizard.

#### 3 Installing Java gateway

It is required to install Java gateway only if you want to monitor JMX applications. Java gateway is lightweight and does not require a database.

To install from sources, first [download](/documentation/current/en/manual/installation/install#download-the-source-archive) and extract the source archive.

To compile Java gateway, run the `./configure` script with `--enable-java` option. It is recommended that you specify the `--prefix` option to request installation path other than the default /usr/local, because installing Java gateway will create a whole directory tree, not just a single executable.
    
    
    ./configure --enable-java --prefix=$PREFIX

Copy

✔ Copied

To compile and package Java gateway into a JAR file, run `make`. Note that for this step you will need `javac` and `jar` executables in your path.
    
    
    make

Copy

✔ Copied

Now you have a zabbix-java-gateway-$VERSION.jar file in src/zabbix_java/bin. If you are comfortable with running Java gateway from src/zabbix_java in the distribution directory, then you can proceed to instructions for configuring and running [Java gateway](/documentation/current/en/manual/java/from_sources#overview-of-files). Otherwise, make sure you have enough privileges and run `make install`.
    
    
    make install

Copy

✔ Copied

Proceed to [setup](/documentation/current/en/manual/concepts/java/from_sources) for more details on configuring and running Java gateway.

#### 4 Installing Zabbix web service

Installing Zabbix web service is only required if you want to use [scheduled reports](/documentation/current/en/manual/web_interface/frontend_sections/reports/scheduled).

To install from sources, first [download](/documentation/current/en/manual/installation/install#download-the-source-archive) and extract the source archive.

To compile Zabbix web service, run the `./configure` script with `--enable-webservice` option.

A configured Go environment with a [supported Go version](/documentation/current/en/manual/installation/requirements#agent-2) is required for building Zabbix web service.

Run zabbix_web_service on the machine, where the web service is installed:
    
    
    zabbix_web_service

Copy

✔ Copied

Proceed to [setup](/documentation/current/en/manual/appendix/install/web_service) for more details on configuring Scheduled reports generation.