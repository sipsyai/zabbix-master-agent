---
title: Requirements
source: https://www.zabbix.com/documentation/current/en/manual/installation/requirements
downloaded: 2025-11-14 10:34:02
---

# 2 Requirements

#### Hardware

**Memory**

Zabbix requires both physical and disk memory. The amount of required disk memory obviously depends on the number of hosts and parameters that are being monitored. If you're planning to keep a long history of monitored parameters, you should be thinking of at least a couple of gigabytes to have enough space to store the history in the database. Each Zabbix daemon process requires several connections to a database server. The amount of memory allocated for the connection depends on the configuration of the database engine.

The more physical memory you have, the faster the database (and therefore Zabbix) works.

**CPU**

Zabbix and especially Zabbix database may require significant CPU resources depending on number of monitored parameters and chosen database engine.

**Other hardware**

A serial communication port and a serial GSM modem are required for using SMS notification support in Zabbix. USB-to-serial converter will also work.

#### Examples of hardware configuration

The table provides examples of hardware configuration, assuming a **Linux/BSD/Unix** platform.

These are size and hardware configuration examples to start with. Each Zabbix installation is unique. Make sure to benchmark the performance of your Zabbix system in a staging or development environment, so that you can fully understand your requirements before deploying the Zabbix installation to its production environment.

Small | 1 000 | 2 | 8 | MySQL Server,  
Percona Server,  
MariaDB Server,  
PostgreSQL | m6i.large/m6g.large  
---|---|---|---|---|---  
Medium | 10 000 | 4 | 16 | MySQL Server,  
Percona Server,  
MariaDB Server,  
PostgreSQL | m6i.xlarge/m6g.xlarge  
Large | 100 000 | 16 | 64 | MySQL Server,  
Percona Server,  
MariaDB Server,  
PostgreSQL | m6i.4xlarge/m6g.4xlarge  
Very large | 1 000 000 | 32 | 96 | MySQL Server,  
Percona Server,  
MariaDB Server,  
PostgreSQL | m6i.8xlarge/m6g.8xlarge  
  
**1** 1 metric = 1 item + 1 trigger + 1 graph  
**2** Example with Amazon general purpose EC2 instances, using ARM64 or x86_64 architecture, a proper instance type like Compute/Memory/Storage optimised should be selected during Zabbix installation evaluation and testing before installing in its production environment.

Actual configuration depends on the number of active items and refresh rates very much (see database size section of this page for details). It is highly recommended to run the database on a separate server for large installations.

#### Supported platforms

Due to security requirements and the mission-critical nature of the monitoring server, UNIX is the only operating system that can consistently deliver the necessary performance, fault tolerance, and resilience. Zabbix operates on market-leading versions.

Zabbix components are available and tested for the following platforms:

Linux | x | x | x |   
---|---|---|---|---  
Windows | - | x | x | Zabbix agent is supported on all desktop and server versions since Windows XP (64-bit)/Server 2003.  
  
Zabbix agent 2 is supported on all desktop and server versions since Windows 10 (32-bit)/Server 2016, as it is compiled only with a [supported Go version](/documentation/current/en/manual/installation/requirements#agent-2) to prevent critical security vulnerabilities. Since Go 1.21, the [minimum required Windows versions](https://go.dev/wiki/MinimumRequirements#windowswindows) are raised, making Windows 10/Server 2016 the minimum version for Zabbix agent 2.  
macOS | x | x | - |   
IBM AIX | x | x | - | Zabbix agent does not work on AIX platforms below versions 6.1 TL07 / 7.1 TL01.  
FreeBSD | x | x | - |   
OpenBSD | x | x | - |   
Solaris | x | x | - |   
NetBSD | x | x | - |   
HP-UX | x | x | - |   
  
Zabbix server/agent may work on other Unix-like operating systems.

Zabbix disables core dumps if compiled with encryption and does not start if the system does not allow disabling of core dumps.

#### Required software

Zabbix is built around modern web servers, leading database engines, and PHP scripting language.

##### Third-party external surrounding software

If stated as mandatory, the required software/library is strictly necessary. Optional ones are needed for supporting some specific function.

_MySQL/Percona_ | One of | 8.0.30-9.0.X | Required if MySQL (or Percona) is used as Zabbix backend database. InnoDB engine is required.  
  
We recommend using the [C API (libmysqlclient)](https://dev.mysql.com/downloads/c-api/) library for building server/proxy.  
---|---|---|---  
_MariaDB_ | 10.5.00-12.0.X | InnoDB engine is required.  
  
The recommended version is 11.4.  
  
We recommend using the [MariaDB Connector/C](https://downloads.mariadb.org/connector-c/) library for building server/proxy.  
  
Added support for MariaDB versions:  
\- 12.0.X since Zabbix 7.4.3.  
  
See also: [Possible deadlocks with MariaDB](/documentation/current/en/manual/installation/known_issues#possible-deadlocks-with-mysqlmariadb) and [Access to UI elements with MariaDB 10.5.1–10.5.9](/documentation/current/en/manual/installation/known_issues#access-to-ui-elements-with-mariadb-10.5.110.5.9).  
_PostgreSQL_ | 13.0-18.X | Required if PostgreSQL is used as Zabbix backend database.  
Depending on the installation size, it might be required to increase PostgreSQL _work_mem_ configuration property (4MB being the default value), so that the amount of memory used by the database for particular operation is sufficient and query execution does not take too much time.  
  
Added support for PostgreSQL versions:  
\- 18.X since Zabbix 7.4.4.  
_TimescaleDB_ for PostgreSQL | 2.13.0-2.22.X | Required if TimescaleDB is used as a PostgreSQL database extension. Make sure to install TimescaleDB Community Edition, which supports compression.  
  
Note that PostgreSQL 15 is supported since TimescaleDB 2.10.  
You may also refer to [TimescaleDB documentation](https://docs.tigerdata.com/self-hosted/latest/upgrades/upgrade-pg/) for details regarding PostgreSQL and TimescaleDB version compatibility.  
  
Added support for TimescaleDB versions:  
\- 2.20.X, 2.21.X since Zabbix 7.4.1;  
\- 2.22.X since Zabbix 7.4.4.  
_SQLite_ | Optional | 3.3.5-3.34.X | SQLite is only supported with Zabbix proxies. Required if SQLite is used as Zabbix proxy database.  
_smartmontools_ | 7.1 or later | Required for Zabbix agent 2.  
_who_ |  | Required for the user count plugin.  
_dpkg_ |  | Required for the system.sw.packages plugin.  
_pkgtool_ |  | Required for the system.sw.packages plugin.  
_rpm_ |  | Required for the system.sw.packages plugin.  
_pacman_ |  | Required for the system.sw.packages plugin.  
_q applets_ |  | `qlist` and `qsize`, as part of [q applets](https://wiki.gentoo.org/wiki/Q_applets), are required for the system.sw.packages plugin on Gentoo Linux.  
  
Although Zabbix can work with databases available in the operating systems, for the best experience, we recommend using databases installed from the official database developer repositories.

##### Frontend

The minimum supported screen width for Zabbix frontend is 1200px.

If stated as mandatory, the required software/library is strictly necessary. Optional ones are needed for supporting some specific function.

_PHP_ | Yes | 8.0.0 - 8.4.X |   
---|---|---|---  
_Apache_ | One of | 2.4 or later |   
_Nginx_ | 1.20 or later |   
_MySQL_ | One of | See [Third-party external surrounding software](/documentation/current/en/manual/installation/requirements#third-party-external-surrounding-software) |   
_PostgreSQL_ |   
**_PHP extensions_**  
_mysqli_ | Yes |  | Required if MySQL is used as Zabbix backend database.  
_pgsql_ |  | Required if PostgreSQL is used as Zabbix backend database.  
_bcmath_ |  | php-bcmath (_\--enable-bcmath_)  
_mbstring_ |  | php-mbstring (_\--enable-mbstring_)  
_sockets_ |  | php-net-socket (_\--enable-sockets_); required for user script support.  
_gd_ | 2.0.28 or later | php-gd (if provided as a separate package by the distributor); PHP GD extension must support PNG images (_\--with-png-dir_), JPEG images (_\--with-jpeg-dir_), and FreeType 2 (_\--with-freetype-dir_). Version 2.3.0 or later may be required to avoid possible [text overlapping in graphs](/documentation/current/en/manual/installation/known_issues#text-overlapping) for some frontend languages.  
_libxml_ | 2.6.15 or later | php-xml (if provided as a separate package by the distributor)  
_xmlwriter_ |  | php-xmlwriter (if provided as a separate package by the distributor)  
_xmlreader_ |  | php-xmlreader (if provided as a separate package by the distributor)  
_ctype_ |  | php-ctype (_\--enable-ctype_)  
_session_ |  | php-session (if provided as a separate package by the distributor)  
_ldap_ | No |  | php-ldap; required for LDAP authentication.  
_openssl_ |  | php-openssl; required for SAML authentication.  
_gettext_ |  | php-gettext (_\--with-gettext_); required for translations.  
_cURL_ | 7.19.4 or later | php-curl; required for Duo Universal Prompt [MFA](/documentation/current/en/manual/web_interface/frontend_sections/users/authentication/mfa), and [SMTP authentication](/documentation/current/en/manual/config/notifications/media/email#configuration).  
  
Third-party frontend libraries that are supplied with Zabbix:

[jQuery JavaScript Library](https://jquery.com/) | Yes | 3.6.0 | JavaScript library that simplifies the process of cross-browser development.  
---|---|---|---  
[jQuery UI](https://jqueryui.com/) | 1.12.1 | A set of user interface interactions, effects, widgets, and themes built on top of jQuery.  
[SAML PHP Toolkit](https://github.com/onelogin/php-saml) | 4.0.0 | A PHP toolkit that adds SAML 2.0 authentication support to be able to sign in to Zabbix.  
[Symfony Yaml Component](https://symfony.com/doc/current/components/yaml.html) | 5.1.0 | Adds support to export and import Zabbix configuration elements in the YAML format.  
  
Zabbix may work on previous versions of Apache, MySQL, and PostgreSQL as well.

For other fonts than the default DejaVu, PHP function [imagerotate](http://php.net/manual/en/function.imagerotate.php) might be required. If it is missing, these fonts might be rendered incorrectly when a graph is displayed. This function is only available if PHP is compiled with bundled GD, which is not the case in Debian and other distributions.

Third-party libraries used for writing and debugging Zabbix frontend code:

[Composer](https://getcomposer.org/) | No | 2.4.1 | An application-level package manager for PHP that provides a standard format for managing dependencies of PHP software and required libraries.  
---|---|---|---  
[PHPUnit](https://phpunit.de/) | 8.5.29 | A PHP unit testing framework for testing Zabbix frontend.  
[SASS](https://sass-lang.com/) | 3.4.22 | A preprocessor scripting language that is interpreted and compiled into Cascading Style Sheets (CSS).  
  
##### Web browser on client side

Cookies and JavaScript must be enabled.

The latest stable versions of Google Chrome, Mozilla Firefox, Microsoft Edge, Apple Safari, and Opera are supported.

The same-origin policy for IFrames is implemented, which means that Zabbix cannot be placed in frames on a different domain.  
  
Still, pages placed into a Zabbix frame will have access to Zabbix frontend (through JavaScript) if the page that is placed in the frame and Zabbix frontend are on the same domain. A page like `http://secure-zabbix.com/cms/page.html`, if placed into dashboards on `http://secure-zabbix.com/zabbix/`, will have full JS access to Zabbix.

##### Server/proxy

If stated as mandatory, the required software/library is strictly necessary. Optional ones are needed for supporting some specific function.

_libpcre2_ | Yes | PCRE2 library is required for [Perl Compatible Regular Expression](https://en.wikipedia.org/wiki/Perl_Compatible_Regular_Expressions) (PCRE) support.  
PCRE2 v10.x is supported.  
---|---|---  
_libevent_ | Required for inter-process communication. Version 2.0.10 or higher.  
_libevent-pthreads_ | Required for inter-process communication.  
_libpthread_ | Required for mutex and read-write lock support (could be part of libc).  
_libresolv_ | Required for DNS resolution (could be part of libc).  
_libiconv_ | Required for text encoding/format conversion (could be part of libc). Mandatory for Zabbix server on Linux.  
_libz_ | Required for compression support.  
_libm_ | Math library. Required by Zabbix server only.  
_libmysqlclient_ | One of | Required if MySQL is used.  
_libmariadb_ | Required if MariaDB is used.  
_libpq5_ | Required if PostgreSQL is used; _libpq5_ version must match or be higher than the version of the PostgreSQL database used.  
_libsqlite3_ | Required if SQLite is used. Required for Zabbix proxy only.  
_libOpenIPMI_ | No | Required for IPMI support. Required for Zabbix server only.  
_libssh2_ or _libssh_ | Required for [SSH checks](/documentation/current/en/manual/config/items/itemtypes/ssh_checks#overview). Version 1.8.0 or higher (libssh2); 0.9.0 or higher (libssh).  
_libcurl_ | Required for the following features:  
\- [Web monitoring](/documentation/current/en/manual/web_monitoring), [VMware monitoring](/documentation/current/en/manual/vm_monitoring), and [HTTP agent](/documentation/current/en/manual/config/items/itemtypes/http) items (for all: version 7.19.1 or higher);  
\- Zabbix agent [web.page.*](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#web.page.get) items (version 7.19.1 or higher; see also agent requirements);  
\- [SMTP authentication](/documentation/current/en/manual/config/notifications/media/email#configuration) (Basic: version 7.20.0 or higher; OAuth: version 7.33 or higher; see also frontend requirements);  
\- [Elasticsearch](/documentation/current/en/manual/appendix/install/elastic_search_setup) (version 7.28.0 or higher).  
Version 7.28.0 or higher for all features is recommended.  
To use upgraded cURL features for `web.page.*` items, restart Zabbix server/proxy.  
For SMTP authentication, use the `libcurl-full` package at runtime.  
_libxml2_ | Required for [VMware monitoring](/documentation/current/en/manual/vm_monitoring) and XML XPath preprocessing.  
_net-snmp_ | Required for SNMP support. Version 5.3.0 or higher.  
Support of strong encryption protocols (AES192/AES192C, AES256/AES256C) is available starting with net-snmp library 5.8; on RHEL 8+ based systems it is recommended to use net-snmp 5.8.15 or later.  
_libunixodbc_ | Required for [database monitoring](/documentation/current/en/manual/config/items/itemtypes/odbc_checks).  
_libgnutls_ or _libopenssl_ | Required when using [encryption](/documentation/current/en/manual/encryption#compiling-zabbix-with-encryption-support).  
Minimum versions: _libgnutls_ \- 3.1.18, _libopenssl_ \- 1.0.1  
_libldap_ | Required for LDAP support.  
_fping_ | Required for [ICMP ping items](/documentation/current/en/manual/config/items/itemtypes/simple_checks#icmp-pings).  
_c-ares_ | Required for asynchronous DNS resolution if Zabbix is configured with `--with-ares` option. Otherwise, _libevent_ will be used.  
Minimum version: 1.16.0  
  
##### Agent

_libpcre2_ | Yes | PCRE2 library is required for [Perl Compatible Regular Expression](https://en.wikipedia.org/wiki/Perl_Compatible_Regular_Expressions) (PCRE) support.  
PCRE2 v10.x is supported.  
Required for log monitoring. Also required on Windows.  
---|---|---  
_libpthread_ | Required for mutex and read-write lock support (could be part of libc). Not required on Windows.  
_libresolv_ | Required for DNS resolution (could be part of libc). Not required on Windows.  
_libiconv_ | Required for text encoding/format conversion to UTF-8 in log items, file content, file regex and regmatch items (could be part of libc). Not required on Windows.  
_libgnutls_ or _libopenssl_ | No | Required if using [encryption](/documentation/current/en/manual/encryption#compiling-zabbix-with-encryption-support).  
Minimum versions: _libgnutls_ \- 3.1.18, _libopenssl_ \- 1.0.1  
On Microsoft Windows OpenSSL 1.1.1 or later is required.  
_libldap_ | Required if LDAP is used. Not supported on Windows.  
_libcurl_ | Required for extended support of Zabbix agent [web.page.*](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#web.page.get) items.  
Without libcurl, basic functionality is available (e.g., web.page.get[http://example.com]). With libcurl, the agent supports additional features, such as HTTP URLs with credentials (e.g., http://user:password@example.com) and HTTPS URLs.  
Version 7.19.1 or higher is required (7.28.0 or higher is recommended).  
To use upgraded cURL features, restart Zabbix agent.  
_libmodbus_ | Only required if Modbus monitoring is used.  
Version 3.0 or higher.  
  
##### Agent 2

_Go_ | Yes | Required to build Zabbix agent 2 and its plugins from source.  
Go 1.23 or later is supported. See [go.dev](https://go.dev/doc/install) for installation instructions.  
Go libraries used by Zabbix agent 2 and its plugins are listed in the Zabbix Git repository (libraries marked as `indirect` in the repository are dependencies of other required libraries):  
\- [Zabbix agent 2](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/src/go/go.mod?at=refs%2Fheads%2Frelease%2F7.4)  
\- [Plugin support](https://git.zabbix.com/projects/AP/repos/plugin-support/browse/go.mod?at=refs%2Fheads%2Frelease%2F7.4)  
\- [PostgreSQL](https://git.zabbix.com/projects/AP/repos/postgresql/browse/go.mod?at=refs%2Fheads%2Frelease%2F7.4)  
\- [MongoDB](https://git.zabbix.com/projects/AP/repos/mongodb/browse/go.mod?at=refs%2Fheads%2Frelease%2F7.4)  
\- [MSSQL](https://git.zabbix.com/projects/AP/repos/mssql/browse/go.mod?at=refs%2Fheads%2Frelease%2F7.4)  
\- [Ember+](https://git.zabbix.com/projects/AP/repos/ember-plus/browse/go.mod?at=refs%2Fheads%2Frelease%2F7.4)  
\- [NVIDIA GPU](https://git.zabbix.com/projects/AP/repos/nvidia-gpu/browse/go.mod?at=refs%2Fheads%2Frelease%2F7.4)  
\- [Example plugin](https://git.zabbix.com/projects/AP/repos/example/browse/go.mod?at=refs%2Fheads%2Frelease%2F7.4)  
---|---|---  
_libpcre2_ | Yes | PCRE2 library is required for [Perl Compatible Regular Expression](https://en.wikipedia.org/wiki/Perl_Compatible_Regular_Expressions) (PCRE) support.  
PCRE2 v10.x is supported.  
Required for log monitoring. Also required on Windows.  
_libopenssl_ | No | Required when using encryption.  
OpenSSL 1.0.1 or later is required on UNIX platforms.  
The OpenSSL library must have PSK support enabled. LibreSSL is not supported.  
On Microsoft Windows systems OpenSSL 1.1.1 or later is required.  
  
##### Web service

The latest stable version of Google Chrome is supported for generating scheduled reports using the Zabbix web service.

The required Go version for building the web service matches the one used for Zabbix agent 2.

##### Java gateway

If you obtained Zabbix from the source repository or an archive, then the necessary dependencies are already included in the source tree.

If you obtained Zabbix from your distribution's package, then the necessary dependencies are already provided by the packaging system.

In both cases above, the software is ready to be used and no additional downloads are necessary.

If, however, you wish to provide your versions of these dependencies (for instance, if you are preparing a package for some Linux distribution), below is the list of library versions that Java gateway is known to work with. Zabbix may work with other versions of these libraries, too.

The following table lists JAR files that are currently bundled with Java gateway in the original code:

[android-json](https://mvnrepository.com/artifact/com.vaadin.external.google/android-json) | Yes | 4.3r1 | JSON (JavaScript Object Notation) is a lightweight data-interchange format. This is the org.json compatible Android implementation extracted from the Android SDK.  
---|---|---|---  
[logback-classic](https://mvnrepository.com/artifact/ch.qos.logback/logback-classic) | 1.5.16 |   
[logback-core](https://mvnrepository.com/artifact/ch.qos.logback/logback-core) | 1.5.16 |   
[slf4j-api](https://mvnrepository.com/artifact/org.slf4j/slf4j-api) | 2.0.16 |   
  
Java gateway can be built using either Oracle Java or open source OpenJDK (version 1.6 or newer). Packages provided by Zabbix are compiled using OpenJDK. The following table lists OpenJDK packages used for building Zabbix packages by distribution:

AlmaLinux 9 | `java-11-openjdk-devel` (amd64: 11.0.19.0.7-4; arm64: 11.0.20.0.8-3)  
---|---  
AlmaLinux 8 | `java-1.8.0-openjdk-devel` (amd64: 1.8.0.332.b09-2; arm64: 1.8.0.382.b05-2)  
Amazon Linux 2023 | `java-22-amazon-corretto-devel` (amd64, arm64: 22.0.2+9-1)  
CentOS Stream 9 | `java-11-openjdk-devel` (amd64, arm64: 11.0.18.0.10-3)  
CentOS Stream 8 | `java-1.8.0-openjdk-devel` (amd64, arm64: 1.8.0.362.b08-3)  
CentOS 7 | `java-1.8.0-openjdk-devel` (amd64: 1.8.0.282.b08-1)  
Debian 12 | `default-jdk-headless` (amd64, arm64: 2:1.17-74)  
Debian 11 | `default-jdk-headless` (amd64: 2:1.11-72)  
OpenSUSE Leap 15 | `java-17-openjdk-devel` (amd64: 17.0.5.0-150400.3.9.3; arm64: 17.0.8.0-150400.3.27.1)  
Oracle Linux 9 | `java-11-openjdk-devel` (amd64: 11.0.19.0.7-4.0.1; arm64: 11.0.20.0.8-2.0.1)  
Oracle Linux 8 | `java-1.8.0-openjdk-devel` (amd64: 1.8.0.372.b07-4.0.1); `java-11-openjdk-devel` (arm64: 11.0.20.0.8-3.0.1)  
Oracle Linux 7 | `java-1.8.0-openjdk-devel` (amd64: 1.8.0.282.b08-1)  
Raspberry Pi OS 12 | `default-jdk-headless` (arm64, armhf: 2:1.17-74)  
Raspberry Pi OS 11 | `default-jdk-headless` (arm64: 2:1.11-72; armhf: 2:1.11-72+b4)  
RHEL 9 | `java-11-openjdk-devel` (amd64: 11.0.19.0.7-4; arm64: 11.0.20.0.8-3)  
RHEL 8 | `java-1.8.0-openjdk-devel` (amd64: 1.8.0.372.b07-4; arm64: 1.8.0.382.b05-2)  
RHEL 7 | `java-1.8.0-openjdk-devel` (amd64: 1.8.0.282.b08-1)  
Rocky Linux 9 | `java-11-openjdk-devel` (amd64: 11.0.19.0.7-4; arm64: 11.0.20.0.8-3)  
Rocky Linux 8 | `java-1.8.0-openjdk-devel` (amd64: 1.8.0.372.b07-4; arm64: 1.8.0.382.b05-2)  
SLES 15 | `java-17-openjdk-devel` (amd64: 17.0.5.0-150400.3.9.3; arm64: 17.0.8.0-150400.3.27.1)  
Ubuntu 24.04 | `default-jdk-headless` (amd64, arm64: 2:1.21-75+exp1)  
Ubuntu 22.04 | `default-jdk-headless` (amd64, arm64: 2:1.11-72build2)  
Ubuntu 20.04 | `default-jdk-headless` (amd64, arm64: 2:1.11-72)  
  
#### Default port numbers

The following list of open ports per component is applicable for default configuration:

Zabbix agent | 10050 | TCP | on demand  
---|---|---|---  
Zabbix agent 2 | 10050 | TCP | on demand  
Zabbix server | 10051 | TCP | on demand  
Zabbix proxy | 10051 | TCP | on demand  
Zabbix Java gateway | 10052 | TCP | on demand  
Zabbix web service | 10053 | TCP | on demand  
Zabbix frontend | 80 | HTTP | on demand  
443 | HTTPS | on demand  
Zabbix trapper | 10051 | TCP | on demand  
  
The port numbers should be open in firewall to enable Zabbix communications. Outgoing TCP connections usually do not require explicit firewall settings.

#### Database size

Zabbix configuration data require a fixed amount of disk space and do not grow much.

Zabbix database size mainly depends on these variables, which define the amount of stored historical data:

  * Number of processed values per second

This is the average number of new values Zabbix server receives every second. For example, if we have 3000 items for monitoring with a refresh rate of 60 seconds, the number of values per second is calculated as 3000/60 = **50**.

It means that 50 new values are added to Zabbix database every second.

  * Housekeeper settings for history

Zabbix keeps values for a fixed period of time, normally several weeks or months. Each new value requires a certain amount of disk space for data and index.

So, if we would like to keep 30 days of history and we receive 50 values per second, the total number of values will be around (**30** *24*3600)* **50** = 129.600.000, or about 130M of values.

Depending on the database engine used, type of received values (floats, integers, strings, log files, etc), the disk space for keeping a single value may vary from 40 bytes to hundreds of bytes. Normally it is around 90 bytes per value for numeric items**2**. In our case, it means that 130M of values will require 130M * 90 bytes = **10.9GB** of disk space.

The size of text/log item values is impossible to predict exactly, but you may expect around 500 bytes per value.

  * Housekeeper setting for trends

Zabbix keeps a 1-hour max/min/avg/count set of values for each item in the table **trends**. The data is used for trending and long period graphs. The one hour period can not be customized.

Zabbix database, depending on the database type, requires about 90 bytes per each total. Suppose we would like to keep trend data for 5 years. Values for 3000 items will require 3000*24*365* **90** = **2.2GB** per year, or **11GB** for 5 years.

  * Housekeeper settings for events

Each Zabbix event requires approximately 250 bytes of disk space**1**. It is hard to estimate the number of events generated by Zabbix daily. In the worst-case scenario, we may assume that Zabbix generates one event per second.

For each recovered event, an event_recovery record is created. Normally most of the events will be recovered so we can assume one event_recovery record per event. That means additional 80 bytes per event.

Optionally events can have tags, each tag record requiring approximately 100 bytes of disk space**1**. The number of tags per event (#tags) depends on configuration. So each will need an additional #tags * 100 bytes of disk space.

It means that if we want to keep 3 years of events, this would require 3*365*24*3600* (250+80+#tags*100) = **~30GB** +#tags*100B disk space**2**.

**1** More when having non-ASCII event names, tags and values.  
**2** The size approximations are based on MySQL and might be different for other databases.

The table contains formulas that can be used to calculate the disk space required for Zabbix system:

_Zabbix configuration_ | Fixed size. Normally 10MB or less.  
---|---  
_History_ | days*(items/refresh rate)*24*3600*bytes  
items : number of items  
days : number of days to keep history  
refresh rate : average refresh rate of items  
bytes : number of bytes required to keep single value, depends on database engine, normally ~90 bytes.  
_Trends_ | days*(items/3600)*24*3600*bytes  
items : number of items  
days : number of days to keep history  
bytes : number of bytes required to keep single trend, depends on the database engine, normally ~90 bytes.  
_Events_ | days*events*24*3600*bytes  
events : number of event per second. One (1) event per second in worst-case scenario.  
days : number of days to keep history  
bytes : number of bytes required to keep single event, depends on the database engine, normally ~330 + average number of tags per event * 100 bytes.  
  
So, the total required disk space can be calculated as:

**Configuration + History + Trends + Events**

The disk space will NOT be used immediately after Zabbix installation. Database size will grow then it will stop growing at some point, which depends on housekeeper settings.

#### Time synchronization

It is very important to have precise system time on the server with Zabbix running. [ntpd](http://www.ntp.org/) is the most popular daemon that synchronizes the host's time with the time of other machines. It's strongly recommended to maintain synchronized system time on all systems Zabbix components are running on.

#### Network requirements

A following list of open ports per component is applicable for default configuration.

Frontend | http on 80, https on 443  
---|---  
Server | 10051 (for use with active proxy/agents)  
Active Proxy | 10051  
Passive Proxy | 10051  
Agent2 | 10050  
Trapper |   
JavaGateway | 10052  
WebService | 10053  
  
The port numbers should be opened in the firewall to enable external communications with Zabbix. Outgoing TCP connections usually do not require explicit firewall settings.