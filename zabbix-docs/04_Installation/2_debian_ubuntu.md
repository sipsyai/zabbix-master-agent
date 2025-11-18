---
title: Debian/Ubuntu
source: https://www.zabbix.com/documentation/current/en/manual/installation/upgrade/packages/debian_ubuntu
downloaded: 2025-11-14 10:34:17
---

# 2 Debian/Ubuntu

#### Overview

This section provides instructions on upgrading from Zabbix **7.2.x** to the latest version of Zabbix **7.4.x** using official Zabbix packages for Debian/Ubuntu.

Before upgrading, please review the relevant [upgrade notes](/documentation/current/en/manual/installation/upgrade) and ensure that your system meets the [requirements](/documentation/current/en/manual/installation/requirements) for Zabbix 7.4.

Consider running two parallel SSH sessions during the upgrade: one for executing the upgrade steps and another for monitoring server/proxy logs. For example, run `tail -f zabbix_server.log` or `tail -f zabbix_proxy.log` in the second session to view the latest log entries and possible errors in real time. This can be critical for production instances.

For instructions on upgrading between Zabbix 7.4.x minor versions (for example, from 7.4.1 to 7.4.3), see Upgrade between minor versions.

#### Upgrade procedure

##### 1 Stop Zabbix processes

Stop Zabbix server to make sure that no new data is inserted into database:
    
    
    systemctl stop zabbix-server

Copy

✔ Copied

If upgrading Zabbix proxy, agent, or agent 2, stop these components too:
    
    
    systemctl stop zabbix-proxy
           systemctl stop zabbix-agent
           systemctl stop zabbix-agent2

Copy

✔ Copied

##### 2 Back up Zabbix database

Back up your existing Zabbix database to safeguard against upgrade failures (for example, disk space issues, power loss, or unexpected problems).

##### 3 Back up Zabbix configuration files, PHP files, and Zabbix binaries

Back up existing Zabbix configuration files, PHP files, and Zabbix binaries.

For configuration files, run:
    
    
    mkdir /opt/zabbix-backup/
           cp /etc/zabbix/zabbix_server.conf /opt/zabbix-backup/
           cp /etc/apache2/conf-enabled/zabbix.conf /opt/zabbix-backup/

Copy

✔ Copied

For PHP files and Zabbix binaries, run:
    
    
    cp -R /usr/share/zabbix/ /opt/zabbix-backup/
           cp -R /usr/share/zabbix-* /opt/zabbix-backup/

Copy

✔ Copied

##### 4 Update repository configuration package

Before proceeding with the upgrade, uninstall your current Zabbix repository package:
    
    
    rm -Rf /etc/apt/sources.list.d/zabbix.list

Copy

✔ Copied

You may also need to manually remove any old Zabbix packages from your working directory (e.g., `rm zabbix-release_latest+debian12_all.deb`) before downloading the new one to prevent the package manager from reusing an outdated version during the upgrade process.

Then, install the latest repository configuration package to ensure compatibility with the newest packages and to include any recent security patches or bug fixes.

On **Debian 12** , run:
    
    
    wget https://repo.zabbix.com/zabbix/7.4/release/debian/pool/main/z/zabbix-release/zabbix-release_latest+debian12_all.deb
           dpkg -i zabbix-release_latest+debian12_all.deb

Copy

✔ Copied

For older Debian versions, replace the link above with the correct one from the [Zabbix repository](https://repo.zabbix.com/zabbix/7.4/release/debian/pool/main/z/zabbix-release/). Note, however, that packages for these versions may not include all Zabbix components, and to upgrade those components from packages, consider upgrading your OS. For a list of components included, see [Zabbix packages](https://www.zabbix.com/download?zabbix=7.4&os_distribution=debian&os_version=11&components=agent&db=&ws=).

On **Ubuntu 24.04** , run:
    
    
    wget https://repo.zabbix.com/zabbix/7.4/release/ubuntu/pool/main/z/zabbix-release/zabbix-release_latest+ubuntu24.04_all.deb
           dpkg -i zabbix-release_latest+ubuntu24.04_all.deb

Copy

✔ Copied

On **Ubuntu 22.04** , run:
    
    
    wget https://repo.zabbix.com/zabbix/7.4/release/ubuntu/pool/main/z/zabbix-release/zabbix-release_latest+ubuntu22.04_all.deb
           dpkg -i zabbix-release_latest+ubuntu22.04_all.deb

Copy

✔ Copied

For older Ubuntu versions, replace the link above with the correct one from the [Zabbix repository](https://repo.zabbix.com/zabbix/7.4/release/ubuntu/pool/main/z/zabbix-release/). Note, however, that packages for these versions may not include all Zabbix components, and to upgrade those components from packages, consider upgrading your OS. For a list of components included, see [Zabbix packages](https://www.zabbix.com/download?zabbix=7.4&os_distribution=ubuntu&os_version=20.04&components=agent&db=&ws=).

You may see a prompt about the Zabbix repository configuration:
    
    
    Configuration file '/etc/apt/sources.list.d/zabbix.list'
           ==> Deleted (by you or by a script) since installation.
           ==> Package distributor has shipped an updated version.
           What would you like to do about it ?  Your options are:
           Y or I  : install the package maintainer's version
           N or O  : keep your currently-installed version
           D       : show the differences between the versions
           Z       : start a shell to examine the situation
           The default action is to keep your current version.
           *** zabbix.list (Y/I/N/O/D/Z) [default=N] ?

Copy

✔ Copied

Enter `Y` (or `I`) to install the package maintainer's version of the Zabbix repository configuration.

Then, update the repository information:
    
    
    apt update

Copy

✔ Copied

##### 5 Upgrade Zabbix components

To upgrade Zabbix components, run:
    
    
    apt install --only-upgrade zabbix-server-mysql zabbix-frontend-php zabbix-agent

Copy

✔ Copied

  * If using PostgreSQL, replace `mysql` with `pgsql` in the command.
  * If upgrading proxy, replace `server` with `proxy` in the command.
  * If upgrading Zabbix agent 2, replace `zabbix-agent` with `zabbix-agent2 zabbix-agent2-plugin-*` in the command.

Upgrading Zabbix agent 2 with the `apt install zabbix-agent2` command could lead to an error. For more information, see [_Known issues_](/documentation/current/en/manual/installation/known_issues#upgrading-zabbix-agent-2-6.0.5-or-older).

You may see a prompt about the Zabbix server (or proxy) configuration:
    
    
    Configuration file '/etc/zabbix/zabbix_server.conf'
           ==> Modified (by you or by a script) since installation.
           ==> Package distributor has shipped an updated version.
           What would you like to do about it ?  Your options are:
           Y or I  : install the package maintainer's version
           N or O  : keep your currently-installed version
           D       : show the differences between the versions
           Z       : start a shell to examine the situation
           The default action is to keep your current version.
           *** zabbix_server.conf (Y/I/N/O/D/Z) [default=N] ?

Copy

✔ Copied

Enter the option that best fits your situation. For example, enter `D` to compare the current and new configuration, then decide if you want to install the package maintainer's version (`Y` or `I`).

Then, to upgrade Zabbix frontend with Apache and restart Apache, run:
    
    
    apt install zabbix-apache-conf
           systemctl restart apache2

Copy

✔ Copied

##### 6 Review component configuration parameters

Review the relevant [upgrade notes](/documentation/current/en/manual/installation/upgrade_notes) to check if any changes in the configuration parameters are necessary.

For new optional parameters, see the [What's new](/documentation/current/en/manual/introduction/whatsnew) page.

##### 7 Start Zabbix processes

Start the upgraded Zabbix components:
    
    
    systemctl start zabbix-server
           systemctl start zabbix-proxy
           systemctl start zabbix-agent
           systemctl start zabbix-agent2

Copy

✔ Copied

##### 8 Clear web browser cookies and cache

After the upgrade, you may need to clear web browser cookies and web browser cache for the Zabbix web interface to work properly.

#### Upgrade between minor versions

It is possible to upgrade between Zabbix 7.4.x minor versions (for example, from 7.4.1 to 7.4.3).

First, update the repository information:
    
    
    apt update

Copy

✔ Copied

Then, to upgrade all Zabbix components, run:
    
    
    apt install --only-upgrade 'zabbix*'

Copy

✔ Copied

  * To upgrade Zabbix server only, replace `'zabbix*'` with `'zabbix-server*'` in the command.
  * To upgrade Zabbix proxy only, replace `'zabbix*'` with `'zabbix-proxy*'` in the command.
  * To upgrade Zabbix agent only, replace `'zabbix*'` with `'zabbix-agent*'` in the command.
  * To upgrade Zabbix agent 2 only, replace `'zabbix*'` with `'zabbix-agent2*'` in the command.