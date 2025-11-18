---
title: Installation from packages
source: https://www.zabbix.com/documentation/current/en/manual/installation/install_from_packages
downloaded: 2025-11-14 10:34:07
---

# 4 Installation from packages

#### Overview

Official Zabbix 7.4 packages are available on the [Zabbix website](https://www.zabbix.com/download), where you can select your operating system and Zabbix component to generate installation instructions suitable for your environment. See also the package installation notes on this page for important additional information.

Packages are available for the following Linux distributions:

  * Red Hat Enterprise Linux and its derivatives: AlmaLinux, Amazon Linux 2023, CentOS Stream, CentOS 7, Oracle Linux, Rocky Linux
  * Debian, Ubuntu, Raspberry Pi OS, Raspbian
  * SUSE Linux Enterprise Server, openSUSE Leap

Some OS distributions (in particular, Debian-based distributions) provide their own Zabbix packages. These packages are **not** supported by Zabbix and may be outdated or missing the latest features and bug fixes. It is recommended to use only official packages from the [Zabbix Official Repository](https://repo.zabbix.com/). If you previously installed Zabbix from your operating system's repository, see the steps for [upgrading Zabbix packages from OS repositories](/documentation/current/en/manual/installation/upgrade/packages#zabbix-packages-from-os-repositories).

Packages support MySQL/PostgreSQL database and Apache/Nginx web server. Note that Zabbix server and proxy cannot share the same database; use different database names if both are installed on the same host.

If necessary, separate packages for Zabbix agent/agent 2, Zabbix get, and Zabbix sender are available at the [Zabbix Official Repository](https://repo.zabbix.com/zabbix/7.4/stable).

Zabbix also provides Zabbix agent pre-compiled binaries for non-Linux operating systems; see:

  * [Windows agent installation from MSI](/documentation/current/en/manual/installation/install_from_packages/win_msi)
  * [macOS agent installation from PKG](/documentation/current/en/manual/installation/install_from_packages/mac_pkg)
  * [Legacy binaries](https://www.zabbix.com/download_agents?version=2.4&os=HPUX&show_legacy=1) (for older/less common systems, such as HP-UX, NetBSD, Tru64, and older versions of SLES)

#### Package installation notes

The following notes apply to all systems:

  * If using PostgreSQL, `DBHost=localhost` (or an IP address) in Zabbix [server](/documentation/current/en/manual/appendix/config/zabbix_server)/[proxy](/documentation/current/en/manual/appendix/config/zabbix_proxy#dbhost) configuration makes PostgreSQL use a network socket instead of a local UNIX socket; see SELinux configuration for related setup instructions.
  * If using TimescaleDB, see additional [TimescaleDB setup](/documentation/current/en/manual/appendix/install/timescaledb).
  * If installing Zabbix [Java gateway](/documentation/current/en/manual/concepts/java) (for monitoring JMX applications), see additional setup instructions for [RHEL-based systems](/documentation/current/en/manual/concepts/java/from_rhel) and [Debian-based systems](/documentation/current/en/manual/concepts/java/from_debian_ubuntu).
  * For running Zabbix agent as root, see [Running agent as root](/documentation/current/en/manual/appendix/install/run_agent_as_root).

The following notes apply to RHEL and its derivatives:

  * If you've enabled the EPEL repository for EL9, which also provides Zabbix packages, it must be excluded from package resolution before installing official Zabbix packages; see [Accidental installation of EPEL Zabbix packages](/documentation/current/en/manual/installation/known_issues#accidental-installation-of-epel-zabbix-packages).
  * For installing Zabbix packages on Red Hat UBI environments, see [Zabbix packages for RHEL on Red Hat UBI environments](/documentation/current/en/manual/installation/known_issues#zabbix-packages-for-rhel-on-red-hat-ubi-environments).
  * For using [ICMP ping items](/documentation/current/en/manual/config/items/itemtypes/simple_checks), packages for `fping` are also available at the [Zabbix Official Repository](https://repo.zabbix.com/third-party).

#### SELinux configuration

Zabbix uses socket-based inter-process communication. On systems where Security-Enhanced Linux (SELinux) is enabled, you may need to add SELinux rules to allow Zabbix create/use UNIX domain sockets in the SocketDir directory. Socket files are used by Zabbix server (alerter, preprocessing, IPMI) and Zabbix proxy (IPMI), and they're present while the process is running.

Having SELinux enabled in enforcing mode, execute the following commands to enable communication between Zabbix frontend and server:

For RHEL 7 (and later), AlmaLinux, CentOS Stream, Oracle Linux, Rocky Linux 8 (and later):
    
    
    setsebool -P httpd_can_connect_zabbix on

Copy

✔ Copied

If the database is accessed over the network (including `localhost` for PostgreSQL), also allow Zabbix frontend to connect to the database:
    
    
    setsebool -P httpd_can_network_connect_db on

Copy

✔ Copied

For RHEL prior to 7:
    
    
    setsebool -P httpd_can_network_connect on
           setsebool -P zabbix_can_network on

Copy

✔ Copied

After applying SELinux settings, restart Apache:
    
    
    systemctl restart httpd

Copy

✔ Copied

Optionally, you can install a pre-defined `zabbix-selinux-policy` package from The [Zabbix Official Repository](https://repo.zabbix.com/zabbix/7.4/stable). This package is provided for all supported OS versions to simplify Zabbix deployment and prevent users from turning off SELinux because of the configuration complexity.

For maximum security, it is recommended to set custom SELinux settings.

The `zabbix-selinux-policy` package contains a basic SELinux policy, allowing Zabbix to create and use sockets and enabling HTTPd connection to PostgreSQL (used by frontend).

The source `zabbix_policy.te` file contains the following rules:
    
    
    module zabbix_policy 1.2;
           
           require {
               type zabbix_t;
               type zabbix_port_t;
               type zabbix_var_run_t;
               type postgresql_port_t;
               type httpd_t;
               class tcp_socket name_connect;
               class sock_file { create unlink };
               class unix_stream_socket connectto;
           }
           
           #============= zabbix_t ==============
           allow zabbix_t self:unix_stream_socket connectto;
           allow zabbix_t zabbix_port_t:tcp_socket name_connect;
           allow zabbix_t zabbix_var_run_t:sock_file create;
           allow zabbix_t zabbix_var_run_t:sock_file unlink;
           allow httpd_t zabbix_port_t:tcp_socket name_connect;
           
           #============= httpd_t ==============
           allow httpd_t postgresql_port_t:tcp_socket name_connect;

Copy

✔ Copied

#### Debuginfo packages

Debuginfo packages contain debugging symbols for Zabbix binaries. They are not required for normal installation or operation but are useful for advanced troubleshooting.

To enable the `zabbix-debuginfo` repository:

  * On RHEL 7, edit `/etc/yum.repos.d/zabbix.repo` and set `enabled=1` for the `zabbix-debuginfo` section:

    
    
    [zabbix-debuginfo]
           name=Zabbix Official Repository debuginfo - $basearch
           baseurl=http://repo.zabbix.com/zabbix/7.4/stable/rhel/7/$basearch/debuginfo/
           enabled=1
           gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-ZABBIX-A14FE591
           gpgcheck=1

Copy

✔ Copied

  * On SUSE, edit `/etc/zypp/repos.d/zabbix.repo` and set `enabled=1` for the `zabbix-debuginfo` section:

    
    
    [zabbix-debuginfo]
           name=Zabbix Official Repository debuginfo
           type=rpm-md
           baseurl=https://repo.zabbix.com/zabbix/7.4/stable/sles/15/x86_64/debuginfo/
           gpgcheck=1
           gpgkey=https://repo.zabbix.com/zabbix/7.4/stable/sles/15/x86_64/debuginfo/repodata/repomd.xml.key
           enabled=0
           update=1

Copy

✔ Copied

Once enabled, install the packages:

  * On RHEL, install a single package with debug information for all Zabbix components:

    
    
    dnf install zabbix-debuginfo

Copy

✔ Copied

  * On SUSE, install component-specific debuginfo packages:

    
    
    zypper install zabbix-<component>-debuginfo

Copy

✔ Copied