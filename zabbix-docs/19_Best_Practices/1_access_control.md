---
title: Access control
source: https://www.zabbix.com/documentation/current/en/manual/best_practices/security/access_control
downloaded: 2025-11-14 10:39:48
---

# 1 Access control

#### Overview

This section contains best practices for setting up access control in a secure way.

#### Principle of least privilege

User accounts, at all times, should run with as few privileges as possible. This means that user accounts in Zabbix frontend, database users, or the user for Zabbix server/proxy/agent processes should only have the privileges that are essential for performing the intended functions.

Giving extra privileges to the 'zabbix' user will allow it to access configuration files and execute operations that can compromise the infrastructure security.

When configuring user account privileges, Zabbix [frontend user types](/documentation/current/en/manual/config/users_and_usergroups/permissions) should be considered. Note that although the _Admin_ user type has fewer privileges than the _Super Admin_ user type, it can still manage configuration and execute custom scripts.

Some information is available even for non-privileged users. For example, while _Alerts_ → _Scripts_ is available only for _Super Admin_ users, scripts can also be retrieved through Zabbix API. In this case, limiting script permissions and excluding sensitive information from scripts (for example, access credentials) can help avoid exposing sensitive information available in global scripts.

#### Secure user for Zabbix agent

By default, Zabbix server, proxy, and agent (or agent 2) processes share one `zabbix` user. To prevent Zabbix agent/agent 2 (running on the same machine as server/proxy) from accessing sensitive details in the server/proxy configuration (for example, database credentials), the agent should be run under a different user:

For Zabbix agent:

  1. Create a secure [group and user](/documentation/current/en/manual/installation/install#create-user-account) (e.g., `zabbix-agent`).
  2. Set this user in the agent configuration file [User](/documentation/current/en/manual/appendix/config/zabbix_agentd#user) parameter.
  3. [Restart agent](/documentation/current/en/manual/concepts/agent#if-installed-as-package) to drop privileges to the new user.

For Zabbix agent 2, the configuration must be applied at the [service](https://www.freedesktop.org/software/systemd/man/latest/systemd.exec.html) level, because the [agent 2 configuration file](/documentation/current/en/manual/appendix/config/zabbix_agent2) does not support the `User` parameter. For an example, see [ZBX-26442](https://support.zabbix.com/browse/ZBX-26442).

#### Revoke write access to SSL configuration (Windows)

If you have compiled Zabbix agent on Windows, with OpenSSL located in an unprotected directory (e.g., `C:\zabbix`, `c:\openssl-64bit`, `C:\OpenSSL-Win64-111-static`, or `C:\dev\openssl`), make sure to revoke write access from non-administrator users to this directory. Otherwise, the agent loads SSL settings from a path that can be modified by unprivileged users, resulting in a potential security vulnerability.

#### Hardening security of Zabbix components

Some functionality can be switched off to harden the security of Zabbix components:

  * global script execution on Zabbix server can be disabled by setting EnableGlobalScripts=0 in server configuration;
  * global script execution on Zabbix proxy is disabled by default (can be enabled by setting EnableRemoteCommands=1 in proxy configuration);
  * global script execution on Zabbix agents is disabled by default (can be enabled by adding an AllowKey=system.run[<command>,*] parameter for each allowed command in agent configuration);
  * user HTTP authentication can be disabled by setting `$ALLOW_HTTP_AUTH=false` in the frontend configuration file (zabbix.conf.php). Note that reinstalling the frontend (running setup.php) will remove this parameter.