---
title: Red Hat Enterprise Linux
source: https://www.zabbix.com/documentation/current/en/manual/installation/upgrade/packages/rhel
downloaded: 2025-11-14 10:34:16
---

# 1 Red Hat Enterprise Linux

#### Overview

This section provides instructions on upgrading from Zabbix **7.2.x** to the latest version of Zabbix **7.4.x** using official Zabbix packages for Red Hat Enterprise Linux or its derivatives - AlmaLinux, CentOS Stream, Oracle Linux, and Rocky Linux.

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
           cp /etc/httpd/conf.d/zabbix.conf  /opt/zabbix-backup/

Copy

✔ Copied

For PHP files and Zabbix binaries, run:
    
    
    cp -R /usr/share/zabbix/ /opt/zabbix-backup/
           cp -R /usr/share/zabbix-* /opt/zabbix-backup/

Copy

✔ Copied

##### 4 Update repository configuration package

Before proceeding with the upgrade, update your current repository package to the latest version to ensure compatibility with the newest packages and to include any recent security patches or bug fixes.

On **RHEL 10** , run:
    
    
    rpm -Uvh https://repo.zabbix.com/zabbix/7.4/release/rhel/10/noarch/zabbix-release-latest.el10.noarch.rpm

Copy

✔ Copied

On **RHEL 9** , run:
    
    
    rpm -Uvh https://repo.zabbix.com/zabbix/7.4/release/rhel/9/noarch/zabbix-release-latest.el9.noarch.rpm

Copy

✔ Copied

For older RHEL versions or its derivatives, replace the link above with the correct one from the [Zabbix repository](https://repo.zabbix.com/zabbix/7.4/release/). Note, however, that packages for these versions may not include all Zabbix components, and to upgrade those components from packages, consider upgrading your OS. For a list of components included, see [Zabbix packages](https://www.zabbix.com/download?zabbix=7.4&os_distribution=red_hat_enterprise_linux&os_version=7&components=agent&db=&ws=).

Then, clean up the `dnf` package manager's cache (including headers, metadata, and package files downloaded during previous installations or updates):
    
    
    dnf clean all

Copy

✔ Copied

On the next `dnf` operation, `dnf` will download fresh metadata from the repositories since the old metadata is cleared.

See also: [Known issues](/documentation/current/en/manual/installation/known_issues#expired-signing-key-for-rhel-packages) for updating the repository configuration package on RHEL.

##### 5 Upgrade Zabbix components

To upgrade Zabbix components, run:
    
    
    dnf install zabbix-server-mysql zabbix-web-mysql zabbix-agent

Copy

✔ Copied

  * If using PostgreSQL, replace `mysql` with `pgsql` in the command.
  * If upgrading the proxy, replace `server` with `proxy` in the command.
  * If upgrading the agent 2, replace `zabbix-agent` with `zabbix-agent2 zabbix-agent2-plugin-*` in the command.

Upgrading Zabbix agent 2 with the `dnf install zabbix-agent2` command could lead to an error. For more information, see [_Known issues_](/documentation/current/en/manual/installation/known_issues#upgrading-zabbix-agent-2-6.0.5-or-older).

Then, to upgrade Zabbix frontend with Apache and restart Apache, run:
    
    
    dnf install zabbix-apache-conf
           systemctl restart httpd

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

To upgrade all Zabbix components, run:
    
    
    dnf upgrade 'zabbix-*'

Copy

✔ Copied

  * To upgrade Zabbix server only, replace `'zabbix-*'` with `'zabbix-server-*'` in the command.
  * To upgrade Zabbix proxy only, replace `'zabbix-*'` with `'zabbix-proxy-*'` in the command.
  * To upgrade Zabbix agent only, replace `'zabbix-*'` with `'zabbix-agent-*'` in the command.
  * To upgrade Zabbix agent 2 only, replace `'zabbix-*'` with `'zabbix-agent2-*'` in the command.