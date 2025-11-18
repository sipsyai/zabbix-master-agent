---
title: Agent
source: https://www.zabbix.com/documentation/current/en/manual/concepts/agent
downloaded: 2025-11-14 10:33:50
---

# 2 Agent

#### Overview

Zabbix agent is deployed on a monitoring target to actively monitor local resources and applications (hard drives, memory, processor statistics, etc.).

The agent gathers operational information locally and reports data to Zabbix server for further processing. In case of failures (such as a hard disk running full or a crashed service process), Zabbix server can actively alert the administrators of the particular machine that reported the failure.

Zabbix agents are highly efficient because of the use of native system calls for gathering statistical information.

##### Passive and active checks

Zabbix agents can perform passive and active checks:

  * [Passive checks](/documentation/current/en/manual/appendix/items/activepassive#passive-checks) \- Zabbix agent responds to a request from Zabbix server (or proxy). For example, the server requests data (e.g., CPU load), and the agent returns the result.
  * [Active checks](/documentation/current/en/manual/appendix/items/activepassive#active-checks) \- Zabbix agent collects and sends data without waiting for a request from Zabbix server (or proxy). First, it retrieves a list of monitoring items from server (CPU load, available memory, etc.), then collects the required data and periodically sends new values back to it.

The agent check type is configured by selecting the respective monitoring [item type](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent). Zabbix agent processes items of type "Zabbix agent" or "Zabbix agent (active)".

#### Supported platforms

For supported platforms, refer to the [Requirements](/documentation/current/en/manual/installation/requirements#supported-platforms) page.

#### Agent on UNIX-like systems

Zabbix agent on UNIX-like systems is run on the host being monitored.

##### Installation

Zabbix agent can be installed on Linux-based systems using one of the following methods:

  * [Zabbix packages](https://www.zabbix.com/download?zabbix=7.4) \- select the Agent component (after selecting your Zabbix version, OS distribution, and OS version) and follow the provided instructions.
  * [Zabbix sources](https://www.zabbix.com/download_sources) \- download the source files and compile Zabbix agent by [configuring the sources](/documentation/current/en/manual/installation/install) with the `--enable-agent` option.

In general, 32-bit Zabbix agents will work on 64-bit systems, but may fail in some cases.

Pre-compiled Zabbix agent binaries are available for [download](https://www.zabbix.com/download_agents?version=7.4&os=macOS) for macOS, IBM AIX, FreeBSD, OpenBSD, and Solaris. Legacy binaries, compatible with current Zabbix server/proxy version, are available for [NetBSD](https://www.zabbix.com/download_agents?os=NetBSD&show_legacy=1) and [HP-UX](https://www.zabbix.com/download_agents?os=HPUX&show_legacy=1).

##### If installed as package

Zabbix agent runs as a daemon process. The agent can be started by executing:
    
    
    systemctl start zabbix-agent

Copy

✔ Copied

This will work on most of GNU/Linux systems. On other systems you may need to run:
    
    
    /etc/init.d/zabbix-agent start

Copy

✔ Copied

To stop, restart, or check the status of Zabbix agent, use the following commands:
    
    
    systemctl stop zabbix-agent
           systemctl restart zabbix-agent
           systemctl status zabbix-agent

Copy

✔ Copied

##### Start up manually

You can start Zabbix agent by locating the zabbix_agentd binary and running it directly; for example:
    
    
    zabbix_agentd

Copy

✔ Copied

#### Agent on Windows systems

Zabbix agent on Windows runs as a Windows service.

##### Installation

Zabbix agent can be installed on Windows using one of the following methods:

  * [Pre-compiled Zabbix agent binaries](https://www.zabbix.com/download_agents?version=7.4) \- download the Zabbix agent MSI installer package and follow the instructions on the [Windows agent installation from MSI](/documentation/current/en/manual/installation/install_from_packages/win_msi) page.
  * [Zabbix sources](https://www.zabbix.com/download_sources) \- download the source files and follow the instructions on the [Building Zabbix agent on Windows](/documentation/current/en/manual/installation/install/win_agent) page.

See the [Zabbix agent on Microsoft Windows](/documentation/current/en/manual/appendix/install/windows_agent#installing-agent-as-windows-service) page for additional details on installing Zabbix agent (from a ZIP archive) as a Windows service.

#### Options

It is possible to run multiple instances of the agent on a host. A single instance can use the default configuration file or a configuration file specified in the command line. In case of multiple instances each agent instance must have its own configuration file (one of the instances can use the default configuration file).

The following command-line parameters can be used with Zabbix agent:

**UNIX and Windows agent**  
---  
-c --config <config-file> | Path to the configuration file.  
You may use this option to specify a configuration file that is not the default one.  
On UNIX, default is /usr/local/etc/zabbix_agentd.conf or as set by [compile-time](/documentation/current/en/manual/installation/install#installing-zabbix-daemons) variables _\--sysconfdir_ or _\--prefix_  
On Windows, default is C:\Program Files\Zabbix Agent\zabbix_agentd.conf  
-f --foreground | Run Zabbix agent in foreground (default: true).  
-p --print | Print known items and exit.  
_Note_ : To return [user parameter](/documentation/current/en/manual/config/items/userparameters) results as well, you must specify the configuration file (if it is not in the default location).  
-t --test <item key> | Test specified item and exit.  
_Note_ : To return [user parameter](/documentation/current/en/manual/config/items/userparameters) results as well, you must specify the configuration file (if it is not in the default location).  
-T --test-config | Validate configuration file and exit.  
-h --help | Display help information.  
-V --version | Display version number.  
**UNIX agent only**  
-R --runtime-control <option> | Perform administrative functions. See [runtime control](/documentation/current/en/manual/concepts/agent#runtime-control).  
**Windows agent only**  
-m --multiple-agents | Use multiple agent instances (with -i, -d, -s, -x options).  
To distinguish service names of instances, each service name will include the Hostname value from the specified configuration file.  
-S --startup-type <value> | Set the startup type of the Zabbix Windows agent service. Allowed values:  
`automatic` \- _(default)_ start the service automatically at Windows startup;  
`delayed` \- delay starting the service after the automatically started services have completed startup (available on Windows Server 2008/Vista and later versions);  
`manual` \- start the service manually (by a user or application);  
`disabled` \- disable the service, so that it cannot be started by a user or application.  
You may use this option together with the -i option, or separately to modify the startup type of an already installed service.  
-i --install | Install Zabbix Windows agent as service.  
-d --uninstall | Uninstall Zabbix Windows agent service.  
-s --start | Start Zabbix Windows agent service.  
-x --stop | Stop Zabbix Windows agent service.  
  
Specific **examples** of using command-line parameters:

  * printing all built-in agent items with values
  * testing a user parameter with "mysql.ping" key defined in the specified configuration file
  * installing a "Zabbix Agent" service for Windows using the default path to configuration file C:\Program Files\Zabbix Agent\zabbix_agentd.conf
  * installing a "Zabbix Agent [Hostname]" service for Windows using the configuration file zabbix_agentd.conf located in the same folder as agent executable and making the service name unique by extending it by Hostname value from the config file
  * modifying the startup type of an installed "Zabbix Agent" service for Windows using the configuration file zabbix_agentd.conf located in the same folder as agent executable

    
    
    zabbix_agentd --print
           zabbix_agentd -t "mysql.ping" -c /etc/zabbix/zabbix_agentd.conf
           zabbix_agentd.exe -i
           zabbix_agentd.exe -i -m -c zabbix_agentd.conf
           zabbix_agentd.exe -c zabbix_agentd.conf -S delayed

Copy

✔ Copied

##### Runtime control

With runtime control options you may change the log level of agent processes.

log_level_increase[=<target>] | Increase log level.  
If target is not specified, all processes are affected. | Target can be specified as:  
**process type** \- all processes of specified type (e.g., listener)  
See all agent process types.  
**process type,N** \- process type and number (e.g., listener,3)  
**pid** \- process identifier (1 to 65535). For larger values specify target as 'process-type,N'.  
---|---|---  
log_level_decrease[=<target>] | Decrease log level.  
If target is not specified, all processes are affected.  
userparameter_reload | Reload values of the _UserParameter_ and _Include_ options from the current configuration file. |   
  
Examples:

  * increasing log level of all processes
  * increasing log level of the third listener process
  * increasing log level of process with PID 1234
  * decreasing log level of all active check processes

    
    
    zabbix_agentd -R log_level_increase
           zabbix_agentd -R log_level_increase=listener,3
           zabbix_agentd -R log_level_increase=1234
           zabbix_agentd -R log_level_decrease="active checks"

Copy

✔ Copied

Runtime control is not supported on OpenBSD, NetBSD and Windows.

#### Agent process types

  * `active checks` \- process for performing active checks
  * `collector` \- process for data collection
  * `listener` \- process for listening to passive checks

The agent log file can be used to observe these process types.

#### Process user

Zabbix agent on UNIX is designed to run as a non-root user. It will run as whatever non-root user it is started as. So you can run agent as any non-root user without any issues.

If you will try to run it as 'root', it will switch to a hardcoded 'zabbix' user, which must be present on your system. You can only run agent as 'root' if you modify the 'AllowRoot' parameter in the agent configuration file accordingly.

#### Configuration file

For details on configuring Zabbix agent see the configuration file options for [zabbix_agentd](/documentation/current/en/manual/appendix/config/zabbix_agentd) or [Windows agent](/documentation/current/en/manual/appendix/config/zabbix_agentd_win).

#### Locale

Note that the agent requires a UTF-8 locale so that some textual agent items can return the expected content. Most modern Unix-like systems have a UTF-8 locale as default, however, there are some systems where that may need to be set specifically.

#### Exit code

Zabbix agent returns 0 in case of successful exit and 1 in case of failure.