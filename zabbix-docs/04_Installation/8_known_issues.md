---
title: Known issues
source: https://www.zabbix.com/documentation/current/en/manual/installation/known_issues
downloaded: 2025-11-14 10:34:19
---

# 8 Known issues

See also: [Compilation issues](/documentation/current/en/manual/installation/known_issues/compilation_issues).

#### Known issues in 7.4.4

It is not recommended to upgrade to this version due to:

  * sudden CPU spike issue if you are using the Zabbix agent 2 MySQL plugin (see [ZBX-27156](https://support.zabbix.com/browse/ZBX-27156))
  * graph for Zabbix active agent items showing an "Undefined array key" warning due to an undefined index error (see [ZBX-27153](https://support.zabbix.com/browse/ZBX-27153))

#### Upgrade

##### SQL mode setting for successful upgrade

The `sql_mode` setting in MySQL/MariaDB must have the "STRICT_TRANS_TABLES" mode set. If it is absent, the Zabbix database upgrade will fail (see also [ZBX-19435](https://support.zabbix.com/browse/ZBX-19435)).

##### Upgrade with MariaDB 10.2.1 and before

Upgrading Zabbix may fail if database tables were created with MariaDB 10.2.1 and before, because in those versions the default row format is compact. This can be fixed by changing the row format to dynamic (see also [ZBX-17690](https://support.zabbix.com/browse/ZBX-17690)).

#### Templates

##### Template compatibility in dual-stack (IPv4/IPv6) environments

In dual-stack environments (systems configured to support both IPv4 and IPv6), the hostname `localhost` typically resolves to both IPv4 and IPv6 addresses. Due to the common prioritization of IPv6 over IPv4 by many operating systems and DNS resolvers, Zabbix templates may fail to work correctly if the service being monitored is configured to listen only on IPv4.

Services that are not configured to listen on IPv6 addresses may become inaccessible, leading to monitoring failures. Users might configure access correctly for IPv4 but still face connectivity issues due to the default behavior of prioritizing IPv6.

A workaround for this is to ensure that the services (Nginx, Apache, PostgreSQL, etc.) are configured to listen on both IPv4 and IPv6 addresses, and Zabbix server/agent is allowed access via IPv6. Additionally, in Zabbix templates and configurations, use `localhost` explicitly instead of `127.0.0.1` to ensure compatibility with both IPv4 and IPv6.

**For example** , when monitoring PostgreSQL with the [PostgreSQL by Zabbix agent 2](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/db/postgresql_agent2?at=refs%2Fheads%2Frelease%2F7.4) template, you may need to edit the `pg_hba.conf` file to allow connections for the `zbx_monitor` user. If the dual-stack environment prioritizes IPv6 (system resolves localhost to `::1`) and you configure `localhost` but only add an IPv4 entry (`127.0.0.1/32`), the connection will fail because there is no matching IPv6 entry.

The following `pg_hba.conf` file example ensures that the `zbx_monitor` user can connect to any database from the local machine using both IPv4 and IPv6 addresses with different authentication methods:
    
    
    # TYPE     DATABASE     USER            ADDRESS          METHOD
             host     all          zbx_monitor     localhost        trust
             host     all          zbx_monitor     127.0.0.1/32     md5
             host     all          zbx_monitor     ::1/128          scram-sha-256

Copy

✔ Copied

If necessary, you can also use the IPv4 address (`127.0.0.1`) directly when configuring the [PostgreSQL by Zabbix agent 2](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/db/postgresql_agent2?at=refs%2Fheads%2Frelease%2F7.4) template macro for the connection string.

#### Accidental installation of EPEL Zabbix packages

If the EPEL repository is installed and enabled, installing Zabbix packages may pull EPEL versions instead of the official Zabbix packages. To resolve this:

1\. Remove any Zabbix packages installed from EPEL:
    
    
    dnf remove zabbix-server-mysql

Copy

✔ Copied

2\. Exclude Zabbix packages from EPEL by adding the following line to `/etc/yum.conf` file:
    
    
    [epel]
           ...
           excludepkgs=zabbix*

Copy

✔ Copied

3\. Reinstall the official Zabbix server package:
    
    
    dnf install zabbix-server-mysql

Copy

✔ Copied

During installation, official Zabbix packages include the word `release` in their version string (e.g., `7.0.0-release1.el8`), distinguishing them from EPEL packages.

#### Zabbix packages for RHEL on Red Hat UBI environments

When installing Zabbix from Red Hat Enterprise Linux packages on [Red Hat Universal Base Image](https://catalog.redhat.com/software/base-images) environments, ensure access to required repositories and dependencies. Zabbix packages depend on `libOpenIPMI.so` and `libOpenIPMIposix.so` libraries, which are not provided by any package in the default package manager repositories enabled on UBI systems and will result in installation failures.

The `libOpenIPMI.so` and `libOpenIPMIposix.so` libraries are available in the `OpenIPMI-libs` package, which is provided by the `redhat-#-for-<arch>-appstream-rpms` repository. Access to this repository is curated by subscriptions, which, in the case of UBI environments, get propagated by mounting repository configuration and secrets directories of the RHEL host into the container file-system namespace.

For more information, see [ZBX-24291](https://support.zabbix.com/browse/ZBX-24291).

#### Expired signing key for RHEL packages

When upgrading Zabbix on [Red Hat Enterprise Linux](/documentation/current/en/manual/installation/upgrade/packages/rhel#update-repository-configuration-package) or its derivatives, you may encounter an expired signing key issue for packages on [Zabbix repository](https://repo.zabbix.com/zabbix/7.4/). When a signing key expires, attempts to verify package signatures will result in an error indicating that the certificate or key is no longer valid. For example:
    
    
    error: Verifying a signature using certificate D9AA84C2B617479C6E4FCF4D19F2475308EFA7DD (Zabbix LLC (Jul 2022) <packager@zabbix.com>):
             1. Certificate 19F2475308EFA7DD invalid: certificate is not alive
                 because: The primary key is not live
                 because: Expired on 2024-07-04T11:41:23Z
             2. Key 19F2475308EFA7DD invalid: key is not alive
                 because: The primary key is not live
                 because: Expired on 2024-07-04T11:41:23Z

Copy

✔ Copied

To resolve such issues, manually reinstall the latest `zabbix-release` package for your specific variant of RHEL (replace the link below with the correct one from [Zabbix repository](https://repo.zabbix.com/zabbix/7.4/release/rhel/)).

For example, on **RHEL 9** , run:
    
    
    rpm -Uvh https://repo.zabbix.com/zabbix/7.4/release/rhel/9/noarch/zabbix-release-latest.el9.noarch.rpm

Copy

✔ Copied

Then, update the repository information:
    
    
    dnf update

Copy

✔ Copied

For more information, see [ZBX-24761](https://support.zabbix.com/browse/ZBX-24761).

#### Timescale DB: high memory usage with large number of partitions

PostgreSQL versions 9.6-12 use too much memory when updating tables with a large number of partitions. This issue manifests itself when Zabbix updates trends on systems with TimescaleDB if trends are split into relatively small (e.g. 1 day) chunks. This leads to hundreds of chunks present in the trends tables with default housekeeping settings - the condition where PostgreSQL is likely to run out of memory.

The issue has been resolved since Zabbix 5.0.1 for new installations with TimescaleDB, but if TimescaleDB was set up with Zabbix before that,please see [ZBX-16347](https://support.zabbix.com/browse/ZBX-16347?focusedCommentId=430816&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-430816) for the migration notes.

#### Timescale DB 2.5.0: compression policy can fail on tables that contain integers

This issue manifests when TimescaleDB 2.5.0/2.5.1 is used. It has been resolved since TimescaleDB 2.5.2.

For more information, please see [TimescaleDB Issue #3773](https://github.com/timescale/timescaledb/issues/3773).

#### Database TLS connection with MariaDB

Database TLS connection is not supported with the 'verify_ca' option for the DBTLSConnect [parameter](/documentation/current/en/manual/appendix/config/zabbix_server) if MariaDB is used.

#### Possible deadlocks with MySQL/MariaDB

When running under high load, and with more than one LLD worker involved, it is possible to run into a deadlock caused by an InnoDB error related to the row-locking strategy (see [upstream bug](https://github.com/mysql/mysql-server/commit/7037a0bdc83196755a3bf3e935cfb3c0127715d5)). The error has been fixed in MySQL since 8.0.29, but not in MariaDB. For more details, see [ZBX-21506](https://support.zabbix.com/browse/ZBX-21506).

#### Global event correlation

Events may not get correlated correctly if the time interval between the first and second event is very small, i.e. half a second and less.

#### Numeric (float) data type range with PostgreSQL 11 and earlier

PostgreSQL 11 and earlier versions only support floating point value range of approximately -1.34E-154 to 1.34E+154.

#### NetBSD 8.0 and newer

Various Zabbix processes may randomly crash on startup on the NetBSD versions 8.X and 9.X. That is due to the too small default stack size (4MB), which must be increased by running:
    
    
    ulimit -s 10240

Copy

✔ Copied

For more information, please see the related problem report: [ZBX-18275](https://support.zabbix.com/browse/ZBX-18275).

#### Regular expression limitations in Zabbix agent 2

Zabbix agent 2 does not support lookaheads and lookbehinds in regular expressions due to the standard Go regexp library limitations.

#### IPMI checks

IPMI checks will not work with the standard OpenIPMI library package on Debian prior to 9 (stretch) and Ubuntu prior to 16.04 (xenial). To fix that, recompile OpenIPMI library with OpenSSL enabled as discussed in [ZBX-6139](https://support.zabbix.com/browse/ZBX-6139).

#### IPMI — untrusted hosts may crash OpenIPMI

There is a bug in the OpenIPMI library used by Zabbix for polling IPMI data that can be triggered by specially crafted responses from an untrusted device.  
An untrusted IPMI device may send crafted data that causes the OpenIPMI library to crash, which in turn can cause Zabbix server process that performs IPMI polling to terminate.

#### SSH checks

  * Some Linux distributions like Debian, Ubuntu do not support encrypted private keys (with passphrase) if the libssh2 library is installed from packages. Please see [ZBX-4850](https://support.zabbix.com/browse/ZBX-4850) for more details.
  * When using libssh 0.9.x on some Linux distributions with OpenSSH 8, SSH checks may occasionally report "Cannot read data from SSH server". This is caused by a libssh [issue](https://gitlab.com/libssh/libssh-mirror/-/merge_requests/101) ([more detailed report](https://bugs.libssh.org/T231)). The error is expected to have been fixed by a stable libssh 0.9.5 release. See also [ZBX-17756](https://support.zabbix.com/browse/ZBX-17756) for details.
  * Using the pipe "|" in the SSH script may lead to a "Cannot read data from SSH server" error. In this case it is recommended to upgrade the libssh library version. See also [ZBX-21337](https://support.zabbix.com/browse/ZBX-21337) for details.

#### ODBC checks

  * MySQL unixODBC driver should not be used with Zabbix server or Zabbix proxy compiled against MariaDB connector library and vice versa, if possible it is also better to avoid using the same connector as the driver due to an [upstream bug](https://bugs.mysql.com/bug.php?id=73709). Recommended setup:

PostgreSQL, SQLite or Oracle connector → MariaDB or MySQL unixODBC driver MariaDB connector → MariaDB unixODBC driver MySQL connector → MySQL unixODBC driver

See [ZBX-7665](https://support.zabbix.com/browse/ZBX-7665) for more information and available workarounds.

  * XML data queried from Microsoft SQL Server may get truncated in various ways on Linux and UNIX systems.

  * It has been observed that using ODBC checks for monitoring Oracle databases using various versions of Oracle Instant Client for Linux causes Zabbix server to crash. See also: [ZBX-18402](https://support.zabbix.com/browse/ZBX-18402), [ZBX-20803](https://support.zabbix.com/browse/ZBX-20803).

  * If using FreeTDS UnixODBC driver, you need to prepend a 'SET NOCOUNT ON' statement to an SQL query (for example, `SET NOCOUNT ON DECLARE @strsql NVARCHAR(max) SET @strsql = ....`). Otherwise, database monitor item in Zabbix will fail to retrieve the information with an error "SQL query returned empty result".  
See [ZBX-19917](https://support.zabbix.com/browse/ZBX-19917) for more information.

#### Incorrect request method parameter in items

The request method parameter, used only in HTTP checks, may be incorrectly set to '1', a non-default value for all items as a result of upgrade from a pre-4.0 Zabbix version. For details on how to fix this situation, see [ZBX-19308](https://support.zabbix.com/browse/ZBX-19308).

#### Web monitoring and HTTP agent

Zabbix server leaks memory on some Linux distributions due to an [upstream bug](https://bugzilla.redhat.com/show_bug.cgi?id=1057388) when "SSL verify peer" is enabled in web scenarios or HTTP agent. Please see [ZBX-10486](https://support.zabbix.com/browse/ZBX-10486) for more information and available workarounds.

#### Simple checks

There is a bug in **fping** versions earlier than v3.10 that mishandles duplicate echo replay packets. This may cause unexpected results for `icmpping`, `icmppingloss`, `icmppingsec` items. It is recommended to use the latest version of **fping**. Please see [ZBX-11726](https://support.zabbix.com/browse/ZBX-11726) for more details.

#### Errors with fping execution in rootless containers

When containers are running in rootless mode or in a specific-restrictions environment, you may face errors related to fping execution when performing ICMP checks, such as `fping: Operation not permitted` or all packets to all resources lost.

To fix this problem add `--cap-add=net_raw` to "docker run" or "podman run" commands.

Additionally fping execution in non-root environments may require sysctl modification, i.e.:
    
    
    sudo sysctl -w "net.ipv4.ping_group_range=0 1995"

Copy

✔ Copied

where "1995" is the zabbix GID. For more details, see [ZBX-22833](https://support.zabbix.com/browse/ZBX-22833).

#### SNMP checks

If the OpenBSD operating system is used, a use-after-free bug in the Net-SNMP library up to the 5.7.3 version can cause a crash of Zabbix server if the SourceIP parameter is set in the Zabbix server configuration file. As a workaround, please do not set the SourceIP parameter. The same problem applies also for Linux, but it does not cause Zabbix server to stop working. A local patch for the net-snmp package on OpenBSD was applied and will be released with OpenBSD 6.3.

#### SNMP data spikes

Spikes in SNMP data have been observed that may be related to certain physical factors like voltage spikes in the mains. See [ZBX-14318](https://support.zabbix.com/browse/ZBX-14318) more details.

#### SNMP traps

The "net-snmp-perl" package, needed for SNMP traps, has been removed in RHEL 8.0-8.2; re-added in RHEL 8.3.

So if you are using RHEL 8.0-8.2, the best solution is to upgrade to RHEL 8.3.

Please also see [ZBX-17192](https://support.zabbix.com/browse/ZBX-17192) for more information.

#### Alerter process crash in RHEL 7

Instances of a Zabbix server alerter process crash have been encountered in RHEL 7. Please see [ZBX-10461](https://support.zabbix.com/browse/ZBX-10461) for details.

#### Upgrading Zabbix agent 2 (6.0.5 or older)

When upgrading Zabbix agent 2 (version 6.0.5 or older) from packages, a plugin-related file conflict error may occur. To fix the error, back up your agent 2 configuration (if necessary), uninstall agent 2 and install it anew.

On RHEL-based systems, run:
    
    
    dnf remove zabbix-agent2
           dnf install zabbix-agent2

Copy

✔ Copied

On Debian-based systems, run:
    
    
    apt remove zabbix-agent2
           apt install zabbix-agent2

Copy

✔ Copied

For more information, see [ZBX-23250](https://support.zabbix.com/browse/ZBX-23250).

#### Flipping frontend locales

It has been observed that frontend locales may flip without apparent logic, i. e. some pages (or parts of pages) are displayed in one language while other pages (or parts of pages) in a different language. Typically the problem may appear when there are several users, some of whom use one locale, while others use another.

A known workaround to this is to disable multithreading in PHP and Apache.

The problem is related to how setting the locale works [in PHP](https://www.php.net/manual/en/function.setlocale): locale information is maintained per process, not per thread. So in a multi-thread environment, when there are several projects run by same Apache process, it is possible that the locale gets changed in another thread and that changes how data can be processed in the Zabbix thread.

For more information, please see related problem reports:

  * [ZBX-10911](https://support.zabbix.com/browse/ZBX-10911) (Problem with flipping frontend locales)
  * [ZBX-16297](https://support.zabbix.com/browse/ZBX-16297) (Problem with number processing in graphs using the `bcdiv` function of BC Math functions)

#### Graphs

##### Daylight Saving Time

Changes to Daylight Saving Time (DST) result in irregularities when displaying X axis labels (date duplication, date missing, etc).

##### Sum aggregation

When using [sum aggregation](/documentation/current/en/manual/config/visualization/graphs/aggregate#configuration) in a graph for period that is less than one hour, graphs display incorrect (multiplied) values when data come from trends.

##### Text overlapping

For some frontend languages (e.g., Japanese), local fonts can cause text overlapping in graph legend. To avoid this, use version 2.3.0 (or later) of PHP GD extension.

#### Log file monitoring

`log[]` and `logrt[]` items repeatedly reread log file from the beginning if file system is 100% full and the log file is being appended (see [ZBX-10884](https://support.zabbix.com/browse/ZBX-10884) for more information).

#### Slow MySQL queries

Zabbix server generates slow `SELECT` queries in case of non-existing values for items. This [issue](https://bugs.mysql.com/bug.php?id=74602) is known to occur in MySQL 5.6/5.7 versions (for an extended discussion, see [ZBX-10652](https://support.zabbix.com/browse/ZBX-10652)), and, in specific cases, may also occur in later MySQL versions. A workaround to this is disabling the [`index_condition_pushdown`](https://dev.mysql.com/doc/refman/8.0/en/switchable-optimizations.html#optflag_index-condition-pushdown) or [`prefer_ordering_index`](https://dev.mysql.com/doc/refman/8.0/en/switchable-optimizations.html#optflag_prefer-ordering-index) optimizer in MySQL. Note, however, that this workaround may not fix all issues related to slow queries.

#### Persistent filter settings from links

When opening a link to Zabbix frontend page that contains filter settings, including the time selector, the filter is automatically saved in the database for the user, replacing the previously saved filter and/or time selector settings for that page. These settings remain active until the user manually updates or resets them.

#### IPv6 address issue in SNMPv3 traps

Due to a net-snmp bug, IPv6 address may not be correctly displayed when using SNMPv3 in SNMP traps. For more details and a possible workaround, see [ZBX-14541](https://support.zabbix.com/browse/ZBX-14541).

#### Trimmed long IPv6 IP address in failed login information

A failed login attempt message will display only the first 39 characters of a stored IP address as that's the character limit in the database field. That means that IPv6 IP addresses longer than 39 characters will be shown incompletely.

#### Zabbix agent checks on Windows

Non-existing DNS entries in a `Server` parameter of Zabbix agent configuration file (zabbix_agentd.conf) may increase Zabbix agent response time on Windows. This happens because Windows DNS caching daemon doesn't cache negative responses for IPv4 addresses. However, for IPv6 addresses negative responses are cached, so a possible workaround to this is disabling IPv4 on the host.

#### YAML export/import

There are some known issues with YAML [export/import](/documentation/current/en/manual/xml_export_import):

  * Error messages are not translatable;
  * Valid JSON with a .yaml file extension sometimes cannot be imported;
  * Unquoted human-readable dates are automatically converted to Unix timestamps.

#### Setup wizard on SUSE with NGINX and php-fpm

Frontend setup wizard cannot save configuration file on SUSE with NGINX + php-fpm. This is caused by a setting in /usr/lib/systemd/system/php-fpm.service unit, which prevents Zabbix from writing to /etc. (introduced in [PHP 7.4](https://bugs.php.net/bug.php?id=72510)).

There are two workaround options available:

  * Set the [ProtectSystem](https://www.freedesktop.org/software/systemd/man/systemd.exec.html#ProtectSystem=) option to 'true' instead of 'full' in the php-fpm systemd unit.
  * Manually save /etc/zabbix/web/zabbix.conf.php file.

#### Authorization header forwarding

In some cases, Apache or NGINX may prevent the Authorization header in API requests from reaching Zabbix. This can cause authentication issues when using Zabbix API or single sign-on (SSO) services, such as SAML with Okta.

To address this, update your web server's configuration.

For **Apache** , if you are using it as a reverse proxy (non-CGI setup), add the following directive to `/etc/httpd/conf/httpd.conf` (on RHEL-based systems) or `/etc/apache2/apache2.conf` (on Debian/Ubuntu):
    
    
    SetEnvIfNoCase ^Authorization$ "(.+)" HTTP_AUTHORIZATION=$1

Copy

✔ Copied

If Apache directly executes scripts to handle requests (e.g., by using mod_cgi), add the following directive instead:
    
    
    CGIPassAuth On

Copy

✔ Copied

In contrast, **NGINX** handles the Authorization header automatically. However, if NGINX is acting as a reverse proxy, you may explicitly forward the Authorization header by adding the following directives to `/etc/nginx/nginx.conf` (for your Zabbix frontend location):
    
    
    ...
           location / {
           ...
               proxy_set_header Authorization $http_authorization;
               proxy_pass http://backend_server;
           ...
           }

Copy

✔ Copied

After updating the configuration, restart you web server.

For more details, see:

  * [ZBX-22952](https://support.zabbix.com/browse/ZBX-22952)
  * [Apache 2.4 + PHP-FPM and Authorization headers](https://stackoverflow.com/questions/17018586/apache-2-4-php-fpm-and-authorization-headers)
  * [SetEnvIfNoCase](https://httpd.apache.org/docs/2.4/mod/mod_setenvif.html#setenvifnocase) and [CGIPassAuth](https://httpd.apache.org/docs/2.4/mod/core.html#CGIPassAuth) directives
  * [NGINX Reverse Proxy](https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/)

#### Chromium for Zabbix web service on Ubuntu 20

Though in most cases, Zabbix web service can run with Chromium, on Ubuntu 20.04 using Chromium causes the following error:
    
    
    Cannot fetch data: chrome failed to start:cmd_run.go:994:
           WARNING: cannot create user data directory: cannot create 
           "/var/lib/zabbix/snap/chromium/1564": mkdir /var/lib/zabbix: permission denied
           Sorry, home directories outside of /home are not currently supported. See https://forum.snapcraft.io/t/11209 for details.

Copy

✔ Copied

This error occurs because `/var/lib/zabbix` is used as a home directory of user 'zabbix'.

#### MySQL custom error codes

When Zabbix detects that the backend database is inaccessible, it sends a notification and continues attempting to connect. For certain database engines, specific error codes are recognized. In MySQL, these recognized error codes include:

  * CR_CONN_HOST_ERROR
  * CR_SERVER_GONE_ERROR
  * CR_CONNECTION_ERROR
  * CR_SERVER_LOST
  * CR_UNKNOWN_HOST
  * ER_SERVER_SHUTDOWN
  * ER_ACCESS_DENIED_ERROR
  * ER_ILLEGAL_GRANT_FOR_TABLE
  * ER_TABLEACCESS_DENIED_ERROR
  * ER_UNKNOWN_ERROR

Additionally, when using Zabbix with a MySQL installation on Azure, the generic error message _[9002] Some errors occurred_ may appear in Zabbix logs. This message is sent by the database to the Zabbix server or proxy. To determine the cause of the error, please consult the Azure logs.

#### Invalid regular expressions after switching to PCRE2

In Zabbix 6.0 support for PCRE2 has been added. Even though PCRE is still supported, Zabbix installation packages for RHEL 7 and newer, SLES (all versions), Debian 9 and newer, Ubuntu 16.04 and newer have been updated to use PCRE2. While providing many benefits, switching to PCRE2 may cause certain existing PCRE regexp patterns becoming invalid or behaving differently. In particular, this affects the pattern _^[\w-\\.]_. In order to make this regexp valid again without affecting semantics, change the expression to _^[-\w\\.]_ . This happens due to the fact that PCRE2 treats the dash sign as a delimiter, creating a range inside a character class.

#### Geomap widget error

The maps in the Geomap widget may not load correctly, if you have upgraded from an older Zabbix version with NGINX and didn't switch to the new NGINX configuration file during the upgrade.

To fix the issue, you can discard the old configuration file, use the configuration file from the current version package and reconfigure it as described in the [download instructions](https://www.zabbix.com/download?zabbix=6.0&os_distribution=red_hat_enterprise_linux&os_version=8&db=mysql&ws=nginx) in section _e. Configure PHP for Zabbix frontend_.

Alternatively, you can manually edit an existing NGINX configuration file (typically, _/etc/zabbix/nginx.conf_). To do so, open the file and locate the following block:
    
    
    location ~ /(api\/|conf[^\.]|include|locale|vendor) {
                   deny            all;
                   return          404;
           }

Copy

✔ Copied

Then, replace this block with:
    
    
    location ~ /(api\/|conf[^\.]|include|locale) {
                   deny            all;
                   return          404;
           }
           
           location /vendor {
                   deny            all;
                   return          404;
           }

Copy

✔ Copied

#### Preprocessing — global variables are unsafe

Preprocessing JavaScript runs per request, but assignments to undeclared identifiers (for example `secret = value`) create implicit globals that may persist beyond the current execution. Storing sensitive data (tokens, passwords, etc.) in implicit globals increases risk of accidental exposure or reuse by subsequent preprocessing runs or other integrations executing in the same environment.

Do not rely on implicit globals. Always declare variables with `var` or `const`, and avoid attaching secrets to global objects (for example `globalThis` or `window`). There is no supported way to override built-in global objects from within preprocessing.

Secure example:
    
    
    var apiToken = payload.token;
           var count = 1;
           return JSON.stringify({ token: apiToken, calls: count });

Copy

✔ Copied

#### Processor groups on Windows

Microsoft documentation states that systems with fewer than 64 logical processors always have a single processor group, Group 0. However, Zabbix users have reported a rare bug [ZBX-20260](https://support.zabbix.com/browse/ZBX-20260), when there are two processor groups on systems with 64 or less logical processors. This resulted in having the "(n)" performance counters for only one processor group out of two. The actual root cause of this bug is not known. However, a similar case was described at [stackoverflow.com](https://stackoverflow.com/questions/28098082/unable-to-use-more-than-one-processor-group-for-my-threads-in-a-c-sharp-app), and the root cause there was in interoperation between BIOS and Windows.

#### Limits of filtering with utf8mb4 collations

Filters (e.g., in _Data collection_ > [_Maintenance_](/documentation/current/en/manual/web_interface/frontend_sections/data_collection/maintenance#using-filter)) may not function correctly when applied to entities containing certain Unicode characters (e.g., ȼ, ɇ). This issue arises due to how the default utf8mb4_bin collation for MySQL or MariaDB databases handles sorting and comparison of Unicode characters.

To address this limitation, users can change the collation of database columns to alternatives such as utf8mb4_0900_bin, utf8mb4_0900_ai_ci, or utf8mb4_unicode_520_ci. Note, however, that changing the collation may cause unexpected behavior in the handling of empty spaces, as well as sorting and filtering for other characters.

For more information on changing collations, see [MySQL documentation](https://dev.mysql.com/doc/refman/8.4/en/alter-table.html#alter-table-character-set) or [MariaDB documentation](https://mariadb.com/kb/en/alter-database/). For details on collation differences, see [Unicode Character Sets](https://dev.mysql.com/doc/refman/8.4/en/charset-unicode-sets.html) in MySQL documentation.

#### Access to UI elements with MariaDB 10.5.1–10.5.9

Accessing the Zabbix web frontend with a role other than Super Admin may result in the message: "System error occurred. Please contact Zabbix administrator.". This issue affects installations using [MariaDB versions](/documentation/current/en/manual/installation/requirements#third-party-external-surrounding-software) 10.5.1 through 10.5.9.

To avoid this issue, update MariaDB to a version later than 10.5.9. For more details, see [ZBX-25746](https://support.zabbix.com/browse/ZBX-25746).

#### Profiling excessive memory usage with tcmalloc

If you suspect your Zabbix installation is using too much memory, you can use [tcmalloc's](https://github.com/google/tcmalloc) memory profiling feature to investigate Zabbix server/proxy memory consumption.

1\. When installing Zabbix [from sources](/documentation/current/en/manual/installation/install#configure-the-sources), configure additional flags:
    
    
    export CFLAGS="-std=gnu99 -g -O0"

Copy

✔ Copied

The `-std=gnu99` flag is required for building Zabbix server, Zabbix proxy, or Zabbix agent. The `-g` flag adds extra debugging information, while `-O0` disables optimizations, which can interfere with tcmalloc's profiling.

2\. Set the following environment variables before starting the Zabbix server. These variables tell tcmalloc how to track and report memory usage:
    
    
    LD_PRELOAD="/usr/lib/aarch64-linux-gnu/libtcmalloc.so" \
           HEAPPROFILE=./heap_profile \
           HEAP_PROFILE_ALLOCATION_INTERVAL=0 \
           HEAP_PROFILE_INUSE_INTERVAL=4294967296 \
           HEAPPROFILESIGNAL=5 \
           MALLOCSTATS=1 \
           ./sbin/zabbix_server -f -c /etc/zabbix/zabbix_server.conf

Copy

✔ Copied

3\. Trigger a profile dump by sending signal 5 to the target process. Replace 1234 with the actual process ID (PID):
    
    
    kill -5 1234

Copy

✔ Copied

4\. Print the generated profile:
    
    
    pprof-symbolize -text ./sbin/zabbix_server ./heap_profile.0001.heap
           
           Using local file ./sbin/zabbix_server.
           Using local file ./heap_profile.0001.heap.
           Total: 1078.1 MB
             1076.8  99.9%  99.9%   1076.8  99.9% zbx_malloc2
                1.0   0.1% 100.0%      1.0   0.1% __GI___strdup
                0.2   0.0% 100.0%      0.2   0.0% CRYPTO_zalloc@@OPENSSL_3.0.0
                0.1   0.0% 100.0%      0.1   0.0% OPENSSL_LH_insert@@OPENSSL_3.0.0
                0.0   0.0% 100.0%      0.0   0.0% zbx_realloc2
                0.0   0.0% 100.0%      0.1   0.0% PKCS7_decrypt@@OPENSSL_3.0.0
                0.0   0.0% 100.0%      0.0   0.0% find_best_tree_node
                0.0   0.0% 100.0%      0.0   0.0% CRYPTO_strndup@@OPENSSL_3.0.0
                ...
                0.0   0.0% 100.0%      0.0   0.0% preprocessing_flush_value
                0.0   0.0% 100.0%   1074.0  99.6% preprocessor_add_request

Copy

✔ Copied

In this example, zbx_malloc2 is responsible for almost all memory allocations.

See also:

  * [ZBX-25050](https://support.zabbix.com/browse/ZBX-25050) and [ZBX-25584](https://support.zabbix.com/browse/ZBX-25584) for the related problem reports.
  * [GCC Option Summary](https://gcc.gnu.org/onlinedocs/gcc-14.2.0/gcc/Option-Summary.html) on compiling options (`-std=gnu99`, `-g`, `-O0`, etc.).
  * [Gperftools Heap Profiler](https://gperftools.github.io/gperftools/heapprofile.html) documentation on environment variables for tcmalloc profiling.

#### MySQL 8.0 Group Replication in multi‐primary mode

When using MySQL 8.0 Group Replication in multi‐primary mode, you may encounter an error during transaction commits similar to the following:
    
    
    1531697:20250128:064734.697 query [txnlev:1] [update alerts set status=1,retries=0,error='' where alertid=154618;
           1531697:20250128:064734.713 query [txnlev:1] [commit;]
           1531697:20250128:064734.753 [Z3005] query failed: [3101] Plugin instructed the server to rollback the current transaction. [commit;]

Copy

✔ Copied

This error appears to be triggered by issues with rollback operations involving foreign key constraints.

See also:

  * [ZBX-26060](https://support.zabbix.com/browse/ZBX-26060) for the related problem report.
  * [MySQL Bug #96758 "Rollbacks with Foreign Keys on single node"](https://bugs.mysql.com/bug.php?id=96758) for the upstream issue.