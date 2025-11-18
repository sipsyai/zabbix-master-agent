---
title: Agent 2
source: https://www.zabbix.com/documentation/current/en/manual/concepts/agent2
downloaded: 2025-11-14 10:33:51
---

# 3 Agent 2

#### Overview

Zabbix agent 2 is a new generation of [Zabbix agent](/documentation/current/en/manual/concepts/agent), written in Go (with some C code reused from Zabbix agent). It is designed to:

  * Reduce the number of TCP connections.
  * Provide improved concurrency of checks.
  * Be easily extendable with [plugins](/documentation/current/en/manual/extensions/plugins), which provide simple checks with minimal code and support complex checks consisting of long-running scripts and standalone data gathering with periodic reporting.
  * Function as a replacement for Zabbix agent, supporting all previous features.

##### Passive and active checks

Zabbix agent 2 supports [passive and active checks](/documentation/current/en/manual/concepts/agent#passive-and-active-checks), similarly to Zabbix agent. Additionally, Zabbix agent 2 active checks support [flexible/scheduling intervals](/documentation/current/en/manual/config/items/item/custom_intervals) and check concurrency within one active server.

By default, after a restart, Zabbix agent 2 will schedule the first data collection for active checks at a conditionally random time within the item's update interval to prevent spikes in resource usage. To perform active checks that do not have _Scheduling_ [update interval](/documentation/current/en/manual/config/items/item/custom_intervals#scheduling-intervals) immediately after the agent restart, set `ForceActiveChecksOnStart` parameter (global-level) or `Plugins.<Plugin name>.System.ForceActiveChecksOnStart` (affects only specific plugin checks) in the [configuration file](/documentation/current/en/manual/appendix/config/zabbix_agent2). Plugin-level parameter, if set, will override the global parameter.

##### Check concurrency

Checks from different plugins can be executed concurrently. The number of concurrent checks within one plugin is limited by the plugin capacity setting. Each plugin may have a hardcoded capacity setting (1000 being default) that can be lowered using the `Plugins.<PluginName>.System.Capacity=N` setting in the _Plugins_ configuration parameter.

#### Supported platforms

For supported platforms, refer to the [Requirements](/documentation/current/en/manual/installation/requirements#supported-platforms) page.

#### Agent 2 on UNIX-like systems

Zabbix agent 2 on UNIX-like systems is run on the host being monitored.

##### Installation

Zabbix agent 2 can be installed on Linux-based systems using one of the following methods:

  * [Zabbix packages](https://www.zabbix.com/download?zabbix=7.4) \- select the Agent 2 component (after selecting your Zabbix version, OS distribution, and OS version) and follow the provided instructions.
  * [Zabbix sources](https://www.zabbix.com/download_sources) \- download the source files and compile Zabbix agent by [configuring the sources](/documentation/current/en/manual/installation/install) with the `--enable-agent2` option. Note that a configured Go environment with a [supported Go version](/documentation/current/en/manual/installation/requirements#agent-2) is required for building Zabbix agent 2.

##### If installed as package

Zabbix agent 2 runs as a foreground process and relies on an external service manager (e.g., systemd) for background execution; Zabbix agent 2 does not have built-in daemonization support on Linux.

The agent can be started by executing:
    
    
    systemctl start zabbix-agent2

Copy

✔ Copied

To stop, restart, or check the status of Zabbix agent 2, use the following commands:
    
    
    systemctl stop zabbix-agent2
           systemctl restart zabbix-agent2
           systemctl status zabbix-agent2

Copy

✔ Copied

##### Start up manually

You can start Zabbix agent by locating the zabbix_agent2 binary and running it directly; for example:
    
    
    zabbix_agent2

Copy

✔ Copied

#### Agent 2 on Windows systems

Zabbix agent 2 runs as a standalone process; however, it can also be run as a Windows service.

##### Installation

Zabbix agent 2 can be installed on Windows using one of the following methods:

  * [Pre-compiled Zabbix agent binaries](https://www.zabbix.com/download_agents?version=7.4) \- download the Zabbix agent MSI installer package and follow the instructions on the [Windows agent installation from MSI](/documentation/current/en/manual/installation/install_from_packages/win_msi) page.
  * [Zabbix sources](https://www.zabbix.com/download_sources) \- download the source files and follow the instructions on the [Building Zabbix agent 2 on Windows](/documentation/current/en/manual/installation/install/building_zabbix_agent_2_on_windows) page. Note that a configured Go environment with a [supported Go version](/documentation/current/en/manual/installation/requirements#agent-2) is required for building Zabbix agent 2.

Zabbix agent 2 monitoring capabilities can be extended with plugins. While built-in plugins are available out-of-the-box, loadable plugins on Windows must be installed separately. For more information, see [Loadable plugins](/documentation/current/en/manual/extensions/plugins#loadable).

See the [Zabbix agent on Microsoft Windows](/documentation/current/en/manual/appendix/install/windows_agent#installing-agent-as-windows-service) page for additional details on installing Zabbix agent 2 (from a ZIP archive) as a Windows service.

#### Options

The following command-line parameters can be used with Zabbix agent 2:

**UNIX and Windows agent**  
---  
-c --config <config-file> | Path to the configuration file.  
You may use this option to specify a configuration file that is not the default one.  
On UNIX, default is /usr/local/etc/zabbix_agent2.conf or as set by [compile-time](/documentation/current/en/manual/installation/install#installing-zabbix-daemons) variables _\--sysconfdir_ or _\--prefix_  
On Windows, default is C:\Program Files\Zabbix Agent 2\zabbix_agent2.conf  
-f --foreground | Run Zabbix agent in foreground (default: true).  
-p --print | Print known items and exit.  
_Note_ : To return [user parameter](/documentation/current/en/manual/config/items/userparameters) results as well, you must specify the configuration file (if it is not in the default location).  
-t --test <item key> | Test specified item and exit.  
_Note_ : To return [user parameter](/documentation/current/en/manual/config/items/userparameters) results as well, you must specify the configuration file (if it is not in the default location).  
-T --test-config | Validate configuration file and exit.  
-h --help | Print help information and exit.  
-v --verbose | Print debugging information. Use this option with -p and -t options.  
-V --version | Print agent version and license information.  
-R --runtime-control <option> | Perform administrative functions. See [runtime control](/documentation/current/en/manual/concepts/agent2#runtime-control).  
**Windows agent only**  
-m --multiple-agents | Use multiple agent instances (with -i, -d, -s, -x options).  
To distinguish service names of instances, each service name will include the Hostname value from the specified configuration file.  
-S --startup-type <value> | Set the startup type of the Zabbix Windows agent service. Allowed values:  
`automatic` \- _(default)_ start the service automatically at Windows startup;  
`delayed` \- delay starting the service after the automatically started services have completed startup;  
`manual` \- start the service manually (by a user or application);  
`disabled` \- disable the service, so that it cannot be started by a user or application.  
You may use this option together with the -i option, or separately to modify the startup type of an already installed service.  
-i --install | Install Zabbix Windows agent as service.  
-d --uninstall | Uninstall Zabbix Windows agent service.  
-s --start | Start Zabbix Windows agent service.  
-x --stop | Stop Zabbix Windows agent service.  
  
Specific **examples** of using command-line parameters:

  * print all built-in agent items with values
  * test a user parameter with "mysql.ping" key defined in the specified configuration file
  * installing a "Zabbix Agent" service for Windows using the default path to configuration file C:\Program Files\Zabbix Agent 2\zabbix_agent2.conf
  * modifying the startup type of an installed "Zabbix Agent" service for Windows using the configuration file zabbix_agent2.conf located in the same folder as agent executable

    
    
    zabbix_agent2 --print
           zabbix_agent2 -t "mysql.ping" -c /etc/zabbix/zabbix_agentd.conf
           zabbix_agent2.exe -i
           zabbix_agent2.exe -c zabbix_agent2.conf -S delayed

Copy

✔ Copied

##### Runtime control

Runtime control provides some options for remote control.

log_level_increase | Increase log level.  
---|---  
log_level_decrease | Decrease log level.  
metrics | List available metrics.  
version | Display agent version.  
userparameter_reload | Reload values of the _UserParameter_ and _Include_ options from the current configuration file.  
help | Display help information on runtime control.  
  
Examples:

  * increasing log level for agent 2
  * print runtime control options

    
    
    zabbix_agent2 -R log_level_increase
           zabbix_agent2 -R help

Copy

✔ Copied

Since Zabbix 7.4.1, agent 2 runtime control commands write output to `stdout` (standard output) instead of `stderr` (standard error).

#### Configuration file

The configuration parameters of agent 2 are mostly compatible with Zabbix agent with some exceptions.

_ControlSocket_ | The runtime control socket path. Agent 2 uses a control socket for runtime commands.  
---|---  
_EnablePersistentBuffer_ ,  
_PersistentBufferFile_ ,  
_PersistentBufferPeriod_ | These parameters are used to configure persistent storage on agent 2 for active items.  
_ForceActiveChecksOnStart_ | Determines whether the agent should perform active checks immediately after restart or spread evenly over time.  
_Plugins_ | Plugins may have their own parameters, in the format `Plugins.<Plugin name>.<Parameter>=<value>`. A common plugin parameter is _System.Capacity_ , setting the limit of checks that can be executed at the same time.  
_StatusPort_ | The port agent 2 will be listening on for HTTP status request and display of a list of configured plugins and some internal parameters  
**Dropped parameters** | **Description**  
_AllowRoot_ , _User_ | Not supported because daemonization is not supported.  
_LoadModule_ , _LoadModulePath_ | Loadable modules are not supported.  
_StartAgents_ | This parameter was used in Zabbix agent to increase passive check concurrency or disable them. In Agent 2, the concurrency is configured at a plugin level and can be limited by a capacity setting. Whereas disabling passive checks is not currently supported.  
_HostInterface_ , _HostInterfaceItem_ | Not yet supported.  
  
For more details see the configuration file options for [zabbix_agent2](/documentation/current/en/manual/appendix/config/zabbix_agent2).

#### Exit codes

Zabbix agent 2 can also be compiled with older OpenSSL versions (1.0.1, 1.0.2).

In this case Zabbix provides mutexes for locking in OpenSSL. If a mutex lock or unlock fails then an error message is printed to the standard error stream (STDERR) and Agent 2 exits with return code 2 or 3, respectively.