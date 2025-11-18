---
title: Zabbix agent on Microsoft Windows
source: https://www.zabbix.com/documentation/current/en/manual/appendix/install/windows_agent
downloaded: 2025-11-14 10:46:38
---

# 11 Zabbix agent on Microsoft Windows

#### Configuring agent

Both generations of Zabbix agents run as a Windows service. For Zabbix agent 2, replace _agentd_ with _agent2_ in the instructions below.

You can run a single instance of Zabbix agent or multiple instances of the agent on a Microsoft Windows host. A single instance may use either:

  * the default configuration file, located in the same directory as the agent binary;
  * a configuration file specified in the command line.

In case of multiple instances each agent instance must have its own configuration file (one of the instances can use the default configuration file).

An example configuration file is available in the Zabbix source archive as:

  * `conf/zabbix_agentd.conf` for Zabbix agent;
  * `conf/zabbix_agent2.conf` for Zabbix agent2.

If you want to install Zabbix agent/agent 2 for Windows as a service from an [archive](https://www.zabbix.com/download_agents) without specifying the configuration file explicitly, then, before installing the agent:

  * `conf/zabbix_agentd.conf` should be copied manually to the directory where zabbix_agentd.exe will be installed;
  * `conf/zabbix_agent2.conf` and the `conf/zabbix_agent2.d` directory should be copied manually to the directory where zabbix_agent2.exe will be installed.

See the [configuration file](/documentation/current/en/manual/appendix/config/zabbix_agentd_win) options for details on configuring Zabbix Windows agent.

##### Hostname parameter

To perform [active checks](/documentation/current/en/manual/appendix/items/activepassive#active-checks) on a host Zabbix agent needs to have the hostname defined. Moreover, the hostname value set on the agent side should exactly match the "[Host name](/documentation/current/en/manual/config/hosts/host)" configured for the host in the frontend.

The hostname value on the agent side can be defined by either the **Hostname** or **HostnameItem** parameter in the agent [configuration file](/documentation/current/en/manual/appendix/config/zabbix_agentd_win) \- or the default values are used if any of these parameters are not specified.

The default value for **HostnameItem** parameter is the value returned by the "system.hostname" agent key. For Windows, it returns result of the gethostname() function, which queries namespace providers to determine the local host name. If no namespace provider responds, the NetBIOS name is returned.

The default value for **Hostname** is the value returned by the HostnameItem parameter. So, in effect, if both these parameters are unspecified, the actual hostname will be the host NetBIOS name; Zabbix agent will use NetBIOS host name to retrieve the list of active checks from Zabbix server and send results to it.

The "system.hostname" key supports two optional parameters - _type_ and _transform_.

_Type_ determines the type of the name the item should return:

  * _netbios_ (default) - returns the NetBIOS host name which is limited to 15 symbols and is in the UPPERCASE only;
  * _host_ \- case-sensitive, returns the full, real Windows host name (without a domain);
  * _shorthost_ \- returns part of the hostname before the first dot. It will return a full string if the name does not contain a dot.
  * _fqdn_ \- returns Fully Qualified Domain Name (without the trailing dot).

_Transform_ allows to specify additional transformation rule for the hostname:

  * _none_ (default) - use the original letter case;
  * _lower_ \- convert the text into lowercase.

So, to simplify the configuration of zabbix_agentd.conf file and make it unified, three different approaches can be used:

  1. Leave **Hostname** or **HostnameItem** parameters undefined and Zabbix agent will use NetBIOS host name as the hostname.
  2. Leave **Hostname** parameter undefined and define **HostnameItem** like this:  
**HostnameItem=system.hostname[host]** \- for Zabbix agent to use the full, real (case-sensitive) Windows host name as the hostname  
**HostnameItem=system.hostname[shorthost,lower]** \- for Zabbix agent to use only part of the hostname before the first dot, converted into lowercase.  
**HostnameItem=system.hostname[fqdn]** \- for Zabbix agent to use the Fully Qualified Domain Name as the hostname.

Host name is also used as part of Windows service name which is used for installing, starting, stopping and uninstalling the Windows service. For example, if Zabbix agent configuration file specifies `Hostname=Windows_db_server`, then the agent will be installed as a Windows service "`Zabbix Agent [Windows_db_server]`". Therefore, to have a different Windows service name for each Zabbix agent instance, each instance must use a different host name.

#### Installing agent as Windows service

Before installing the agent, copy `conf/zabbix_agentd.conf` manually to the directory where zabbix_agentd.exe will be installed.

To install a single instance of Zabbix agent with the default configuration file:
    
    
    zabbix_agentd.exe --install

Copy

✔ Copied

On a 64-bit system, a 64-bit Zabbix agent version is required for all checks related to running 64-bit processes to work correctly.

If you wish to use a configuration file other than the default one, you should use the following command for service installation:
    
    
    zabbix_agentd.exe --config <your_configuration_file> --install

Copy

✔ Copied

A full path to the configuration file should be specified.

Multiple instances of Zabbix agent can be installed as services like this:
    
    
      zabbix_agentd.exe --config <configuration_file_for_instance_1> --install --multiple-agents
             zabbix_agentd.exe --config <configuration_file_for_instance_2> --install --multiple-agents
             ...
             zabbix_agentd.exe --config <configuration_file_for_instance_N> --install --multiple-agents

Copy

✔ Copied

The installed service should now be visible in Control Panel.

#### Starting agent

To start the agent service, you can use Control Panel or do it from command line.

To start a single instance of Zabbix agent with the default configuration file:
    
    
     zabbix_agentd.exe --start

Copy

✔ Copied

To start a single instance of Zabbix agent with another configuration file:
    
    
     zabbix_agentd.exe --config <your_configuration_file> --start

Copy

✔ Copied

To start one of multiple instances of Zabbix agent:
    
    
     zabbix_agentd.exe --config <configuration_file_for_this_instance> --start --multiple-agents

Copy

✔ Copied

#### Stopping agent

To stop the agent service, you can use Control Panel or do it from command line.

To stop a single instance of Zabbix agent started with the default configuration file:
    
    
     zabbix_agentd.exe --stop

Copy

✔ Copied

To stop a single instance of Zabbix agent started with another configuration file:
    
    
     zabbix_agentd.exe --config <your_configuration_file> --stop

Copy

✔ Copied

To stop one of multiple instances of Zabbix agent:
    
    
     zabbix_agentd.exe --config <configuration_file_for_this_instance> --stop --multiple-agents

Copy

✔ Copied

#### Uninstalling agent Windows service

To uninstall a single instance of Zabbix agent using the default configuration file:
    
    
       zabbix_agentd.exe --uninstall

Copy

✔ Copied

To uninstall a single instance of Zabbix agent using a non-default configuration file:
    
    
       zabbix_agentd.exe --config <your_configuration_file> --uninstall

Copy

✔ Copied

To uninstall multiple instances of Zabbix agent from Windows services:
    
    
      zabbix_agentd.exe --config <configuration_file_for_instance_1> --uninstall --multiple-agents
             zabbix_agentd.exe --config <configuration_file_for_instance_2> --uninstall --multiple-agents
             ...
             zabbix_agentd.exe --config <configuration_file_for_instance_N> --uninstall --multiple-agents

Copy

✔ Copied

#### Limitations

Zabbix agent for Windows does not support non-standard Windows configurations where CPUs are distributed non-uniformly across NUMA nodes. If logical CPUs are distributed non-uniformly, then CPU performance metrics may not be available for some CPUs. For example, if there are 72 logical CPUs with 2 NUMA nodes, both nodes must have 36 CPUs each.