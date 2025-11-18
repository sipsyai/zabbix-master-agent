---
title: Windows agent installation from MSI
source: https://www.zabbix.com/documentation/current/en/manual/installation/install_from_packages/win_msi
downloaded: 2025-11-14 10:34:08
---

# 1 Windows agent installation from MSI

#### Overview

Zabbix agent can be installed on Windows using 32-bit or 64-bit MSI installer packages, available for [download](https://www.zabbix.com/download_agents?os=Windows).

Minimum OS requirements for MSI installation are:

  * **For Zabbix agent:** Windows XP (64-bit) or Windows Server 2003
  * **For Zabbix agent 2:** Windows 10 (32-bit) or Windows Server 2016

32-bit packages cannot be installed on 64-bit systems.

Packages include:

  * TLS support (TLS configuration is optional)
  * [Zabbix get](/documentation/current/en/manual/concepts/get) and [Zabbix sender](/documentation/current/en/manual/concepts/sender) utilities (can be installed alongside Zabbix agent/agent 2 or separately)

Zabbix agent 2 packages do not include loadable plugins (MongoDB, PostgreSQL, MSSQL), which need to be downloaded and installed separately.

Installation can be done using the Setup Wizard or the command line.

Although installation using MSI packages is fully supported, installing at least [Microsoft .NET Framework 2](https://dotnet.microsoft.com/en-us/download/dotnet-framework) is recommended for proper error handling.

It is recommended to use the default installation location provided by the installer. Using a custom location without the necessary permissions may compromise the security of the installation.

#### Installation from Setup Wizard

The following installation steps apply to both Zabbix agent and Zabbix agent 2.

1\. Double-click the downloaded MSI file to start the installation:

![](/documentation/current/assets/en/manual/installation/install_from_packages/msi0_b.png)

2\. Accept the End-User License Agreement:

![](/documentation/current/assets/en/manual/installation/install_from_packages/msi0_c.png)

3\. Select the Zabbix components ([Agent daemon](/documentation/current/en/manual/concepts/agent), [Zabbix sender](/documentation/current/en/manual/concepts/sender), [Zabbix get](/documentation/current/en/manual/concepts/get)) to be installed:

It is recommended to use the default installation location provided by the installer. Using a custom location without the necessary permissions may compromise the security of the installation.

![](/documentation/current/assets/en/manual/installation/install_from_packages/msi0_f.png)

4\. Configure the following parameters. Their values will be set in the Zabbix agent configuration file:

_Host name_ | The host name of the machine where Zabbix agent is being installed. Sets the [Hostname](/documentation/current/en/manual/appendix/config/zabbix_agentd_win#hostname) parameter.  
---|---  
_Zabbix server IP/DNS_ | A list of comma-delimited IP addresses, optionally in CIDR notation, or DNS names of Zabbix servers or Zabbix proxies. This parameter is **mandatory**. Sets the [Server](/documentation/current/en/manual/appendix/config/zabbix_agentd_win#server) parameter.  
_Agent listen port_ | The agent will listen on this port for connections from the server. Sets the [ListenPort](/documentation/current/en/manual/appendix/config/zabbix_agentd_win#listenport) parameter.  
_Server or Proxy for active checks_ | The Zabbix server/proxy address or cluster configuration to get [active checks](/documentation/current/en/manual/appendix/items/activepassive) from. The server/proxy address is an IP address or DNS name and optional port separated by colon. Sets the [ServerActive](/documentation/current/en/manual/appendix/config/zabbix_agentd_win#serveractive) parameter.  
_Enable PSK_ | Mark the checkbox to enable TLS support [using pre-shared keys](/documentation/current/en/manual/encryption/using_pre_shared_keys). Sets the [TLSConnect](/documentation/current/en/manual/appendix/config/zabbix_agentd_win#tlsconnect) and [TLSAccept](/documentation/current/en/manual/appendix/config/zabbix_agentd_win#tlsaccept) parameters to `psk`.  
_Add agent location to the PATH_ | Mark the checkbox to add Zabbix agent location to the system PATH variable.  
  
If an existing Zabbix agent is detected, the parameter values from its configuration file will be displayed. Additionally the existing configuration file will be renamed during installation, and a new configuration file will be created.

![](/documentation/current/assets/en/manual/installation/install_from_packages/msi0_d.png)

5\. Configure PSK parameters if you marked the _Enable PSK_ checkbox in the previous step. These parameters will also be set in the Zabbix agent configuration file:

_Pre-shared key identity_ | The pre-shared key identity string. Sets the [TLSPSKIdentity](/documentation/current/en/manual/appendix/config/zabbix_agentd_win#tlspskidentity) parameter.  
---|---  
_Pre-shared key value_ | The pre-shared key string value. Creates the psk.key file containing the key and sets the [TLSPSKFile](/documentation/current/en/manual/appendix/config/zabbix_agentd_win#tlspskfile) parameter to the key location (default: `C:\Program Files\Zabbix Agent\psk.key`). It is **recommended** to restrict access to the pre-shared key file by adjusting the file's security settings so that only Zabbix agent (or the user running the agent) can read it.  
  
![](/documentation/current/assets/en/manual/installation/install_from_packages/msi0_e.png)

6\. Click _Install_ to begin the installation.

All selected Zabbix components and the Zabbix agent configuration file will be installed in your specified location (default: `C:\Program Files\Zabbix Agent`). The same applies to Zabbix agent 2, except additional configuration files for its [built-in plugins](/documentation/current/en/manual/extensions/plugins#built-in) will be installed in the `zabbix_agent2.d\plugins.d` subfolder.

Additionally, zabbix_agentd.exe (or zabbix_agent2.exe) will be set up as a Windows service with delayed automatic startup (or automatic startup on Windows versions before Windows Vista/Server 2008).

If a different version of Zabbix agent is running during installation, you will be prompted to choose either to close the application and try restarting it or leave it open, in which case a reboot will be required.

![](/documentation/current/assets/en/manual/installation/install_from_packages/msi0_g.png)

7\. Click the _Finish_ button to exit the Setup Wizard.

![](/documentation/current/assets/en/manual/installation/install_from_packages/msi0_h.png)

#### Installation from command line

Zabbix agent can be installed from the command line by running the MSI installer with [msiexec](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/msiexec). For example:
    
    
    msiexec.exe /l*v "C:\package.log" /i "C:\zabbix_agent-7.4.0-windows-amd64-openssl.msi" /qn+ SERVER=192.0.2.0

Copy

✔ Copied

This method allows for unattended installations and custom configurations using parameters.

##### Supported parameters

Zabbix agent MSI installer packages support the following parameters for both Zabbix agent and Zabbix agent 2.

Zabbix agent/agent2 parameters are set in the configuration file during installation. Click a parameter name to view its detailed description and configuration examples on the [Zabbix agent (Windows)](/documentation/current/en/manual/appendix/config/zabbix_agentd_win) page. For Zabbix agent 2, refer to the [Zabbix agent 2 (Windows)](/documentation/current/en/manual/appendix/config/zabbix_agent2_win) page.

ADDDEFAULT | A list of comma-delimited components to install in their default configuration. For more information, see [ADDDEFAULT property](https://learn.microsoft.com/en-us/windows/win32/msi/adddefault).  
Possible values: `AgentProgram`, `GetProgram`, `SenderProgram`, `ALL`  
Example: `ADDDEFAULT=AgentProgram,GetProgram`  
---|---  
ADDLOCAL | A list of comma-delimited components to install locally. For more information, see [ADDLOCAL property](https://learn.microsoft.com/en-us/windows/win32/msi/addlocal).  
Possible values: `AgentProgram`, `GetProgram`, `SenderProgram`, `ALL`  
Example: `ADDLOCAL=AgentProgram,SenderProgram`  
ALLOWDENYKEY | A list of semicolon-delimited AllowKey or DenyKey parameters to [restrict Zabbix agent checks](/documentation/current/en/manual/config/items/restrict_checks). If necessary, use a backslash to escape the delimiter (`\;`). Sets the [AllowKey](/documentation/current/en/manual/appendix/config/zabbix_agentd#allowkey) and [DenyKey](/documentation/current/en/manual/appendix/config/zabbix_agentd#denykey) parameters in the agent configuration file.  
Example: `ALLOWDENYKEY="AllowKey=system.run[type C:\Windows\System32\drivers\etc\hosts];DenyKey=system.run[*]"`  
CONF | The full pathname to a template configuration file for Zabbix agent. During installation, this file will become the agent configuration file. The file must contain at least the [Server](/documentation/current/en/manual/appendix/config/zabbix_agentd#server) and [LogFile](/documentation/current/en/manual/appendix/config/zabbix_agentd#logfile) parameters.  
Example: `CONF="C:\full\path\to\example.conf"`  
ENABLEPATH | Use `ENABLEPATH=1` to add Zabbix agent location to the system PATH variable.  
[ENABLEPERSISTENTBUFFER](/documentation/current/en/manual/appendix/config/zabbix_agent2_win#enablepersistentbuffer) | Zabbix agent 2 only. Enable the usage of local persistent storage for active items.  
[HOSTINTERFACE](/documentation/current/en/manual/appendix/config/zabbix_agentd_win#hostinterface) | An optional parameter that defines the host interface.  
[HOSTMETADATA](/documentation/current/en/manual/appendix/config/zabbix_agentd_win#hostmetadata) | An optional parameter that defines the host metadata.  
[HOSTMETADATAITEM](/documentation/current/en/manual/appendix/config/zabbix_agentd_win#hostmetadataitem) | An optional parameter that defines an item used for getting the host metadata.  
[HOSTNAME](/documentation/current/en/manual/appendix/config/zabbix_agentd_win#hostname) | An optional parameter that defines the hostname.  
[INCLUDE](/documentation/current/en/manual/appendix/config/zabbix_agentd_win#include) | A list of semicolon-delimited individual files or all files in a directory to include in the Zabbix agent configuration file.  
INSTALLFOLDER | The full pathname to a folder where Zabbix components and the Zabbix agent configuration file will be installed. For Zabbix agent 2, additional configuration files for [built-in plugins](/documentation/current/en/manual/extensions/plugins#built-in) will be installed in the `zabbix_agent2.d\plugins.d` subfolder.  
Example: `INSTALLFOLDER="C:\Program Files\Zabbix Agent"`  
[LISTENIP](/documentation/current/en/manual/appendix/config/zabbix_agentd_win#listenip) | A list of comma-delimited IP addresses that the agent should listen on.  
[LISTENPORT](/documentation/current/en/manual/appendix/config/zabbix_agentd_win#listenport) | The agent will listen on this port for connections from the server.  
[LOGFILE](/documentation/current/en/manual/appendix/config/zabbix_agentd_win#logfile) | The name of the Zabbix agent log file.  
[LOGTYPE](/documentation/current/en/manual/appendix/config/zabbix_agentd_win#logtype) | The type of the log output.  
NONMSICONFNAME | The full pathname to a custom configuration file for Zabbix agent. During installation, any valid agent configuration parameters present in this file (limited to those listed in this table) will be written in the newly created agent configuration file. The file must contain at least the [Server](/documentation/current/en/manual/appendix/config/zabbix_agentd#server) parameter.  
Example: `NONMSICONFNAME="C:\full\path\to\example.conf"`  
[PERSISTENTBUFFERFILE](/documentation/current/en/manual/appendix/config/zabbix_agent2_win#persistentbufferfile) | Zabbix agent 2 only. The file where Zabbix agent 2 should keep the SQLite database.  
[PERSISTENTBUFFERPERIOD](/documentation/current/en/manual/appendix/config/zabbix_agent2_win#persistentbufferperiod) | Zabbix agent 2 only. The time period for which data should be stored when there is no connection to the server or proxy.  
[SERVER](/documentation/current/en/manual/appendix/config/zabbix_agentd_win#server) | A list of comma-delimited IP addresses, optionally in CIDR notation, or DNS names of Zabbix servers or Zabbix proxies. This parameter is **mandatory**.  
[SERVERACTIVE](/documentation/current/en/manual/appendix/config/zabbix_agentd_win#serveractive) | The Zabbix server/proxy address or cluster configuration to get active checks from.  
SKIP | Use `SKIP=fw` to prevent the MSI installer from adding a Windows Firewall exception rule for Zabbix agent.  
STARTUPTYPE | Startup type of the Zabbix agent service. Possible values:  
**automatic** \- start the service automatically at Windows startup;  
**delayed** \- _(default)_ delay starting the service after the automatically started services have completed startup (available on Windows Vista/Server 2008 and later versions);  
**manual** \- start the service manually (by a user or application);  
**disabled** \- disable the service so that it cannot be started by a user or application.  
Example: `STARTUPTYPE=disabled`  
[STATUSPORT](/documentation/current/en/manual/appendix/config/zabbix_agent2_win#statusport) | Zabbix agent 2 only. If set, the agent will listen on this port for HTTP status requests (http://localhost:<port>/status).  
[TIMEOUT](/documentation/current/en/manual/appendix/config/zabbix_agentd_win#timeout) | Specifies how long to wait (in seconds) for establishing connection and exchanging data with Zabbix proxy or server.  
[TLSACCEPT](/documentation/current/en/manual/appendix/config/zabbix_agentd_win#tlsaccept) | The incoming connections to accept (used for passive checks). If set to `psk`, then TLSCONNECT will also be set to `psk` (unless specified otherwise).  
[TLSCAFILE](/documentation/current/en/manual/appendix/config/zabbix_agentd_win#tlscafile) | The full pathname of a file containing the top-level CA(s) certificates for peer certificate verification.  
[TLSCERTFILE](/documentation/current/en/manual/appendix/config/zabbix_agentd_win#tlscertfile) | The full pathname of a file containing the agent certificate or certificate chain.  
[TLSCONNECT](/documentation/current/en/manual/appendix/config/zabbix_agentd_win#tlsconnect) | How the agent should connect to Zabbix server or proxy (used for active checks). If set to `psk`, then TLSACCEPT will also be set to `psk` (unless specified otherwise).  
[TLSCRLFILE](/documentation/current/en/manual/appendix/config/zabbix_agentd_win#tlscrlfile) | The full pathname of a file containing revoked certificates.  
[TLSKEYFILE](/documentation/current/en/manual/appendix/config/zabbix_agentd_win#tlskeyfile) | The full pathname of a file containing the Zabbix agent private key.  
[TLSPSKFILE](/documentation/current/en/manual/appendix/config/zabbix_agentd_win#tlspskfile) | The full pathname of a file containing the Zabbix agent pre-shared key. If both TLSPSKFILE and TLSPSKVALUE are set, the value of TLSPSKVALUE will be written into the file specified in TLSPSKFILE. It is **recommended** to restrict access to the pre-shared key file by adjusting the file's security settings so that only Zabbix agent (or the user running the agent) can read it.  
[TLSPSKIDENTITY](/documentation/current/en/manual/appendix/config/zabbix_agentd_win#tlspskidentity) | The pre-shared key identity string.  
TLSPSKVALUE | The pre-shared key string value. If both TLSPSKFILE and TLSPSKVALUE are set, the value of TLSPSKVALUE will be written into the file specified in TLSPSKFILE.  
Example: `TLSPSKVALUE=1f87b595725ac58dd977beef14b97461a7c1045b9a1c963065002c5473194952`  
[TLSSERVERCERTISSUER](/documentation/current/en/manual/appendix/config/zabbix_agentd_win#tlsservercertissuer) | The allowed server (proxy) certificate issuer.  
[TLSSERVERCERTSUBJECT](/documentation/current/en/manual/appendix/config/zabbix_agentd_win#tlsservercertsubject) | The allowed server (proxy) certificate subject.  
  
##### Examples

The following example installs Zabbix agent with custom configuration. It also enables TLS support [using pre-shared keys](/documentation/current/en/manual/encryption/using_pre_shared_keys).
    
    
    mkdir "C:\Program Files\Zabbix Agent" 2>nul
           msiexec.exe /l*v "C:\package.log" /i "C:\zabbix_agent-7.4.0-windows-amd64-openssl.msi" /qn+^
            SERVER=192.0.2.0^
            INSTALLFOLDER="C:\Program Files\Zabbix Agent"^
            HOSTNAME=LAPTOP-IKP7S51S^
            TLSACCEPT=psk^
            TLSCONNECT=psk^
            TLSPSKIDENTITY="PSK 001"^
            TLSPSKFILE="C:\Program Files\Zabbix Agent\psk.key"^
            TLSPSKVALUE=1f87b595725ac58dd977beef14b97461a7c1045b9a1c963065002c5473194952^
            ENABLEPATH=1^
            ALLOWDENYKEY="AllowKey=system.run[type C:\Windows\System32\drivers\etc\hosts];DenyKey=system.run[*]"

Copy

✔ Copied

The next example installs a newer version of Zabbix agent and uses a **template configuration file** (`CONF="C:\agent-template.conf"`). During installation, this file will become the agent configuration file. To inherit parameters from the old configuration file, use parameter placeholders (e.g., `[AllowDenyKey]`).
    
    
    msiexec.exe /l*v "C:\package.log" /i "C:\zabbix_agent-7.4.1-windows-amd64-openssl.msi" /qn+ NONMSICONFNAME="C:\agent.conf"
           
           # agent-template.conf example:
           LogFile=[LogFile]
           [AllowDenyKey]
           Server=192.0.2.8
           Hostname=DESKTOP-X9F4A2B
           [Include]
           [TLSConnect]
           [TLSAccept]
           [TLSPSKIdentity]
           [TLSPSKFile]

Copy

✔ Copied

Alternatively, you can use a **custom configuration file** (`NONMSICONFNAME="C:\agent-custom.conf"`). During installation, any valid agent configuration parameters present in this file (limited to those listed in the table above) will be written in the newly created agent configuration file. To keep existing agent configuration, define parameters to be preserved.
    
    
    msiexec.exe /l*v "C:\package.log" /i "C:\zabbix_agent-7.4.1-windows-amd64-openssl.msi" /qn+ NONMSICONFNAME="C:\agent-custom.conf"
           
           # agent-custom.conf example:
           Server=192.0.2.8
           Hostname=DESKTOP-X9F4A2B

Copy

✔ Copied

#### Zabbix agent 2 loadable plugins

Zabbix agent 2 [loadable plugins](/documentation/current/en/manual/extensions/plugins#loadable) can be installed on Windows using 64-bit MSI installer packages, available for [download](https://www.zabbix.com/download_agents?version=7.4&os=Windows&encryption=No+encryption).

Minimum OS requirements for MSI installation are Windows 10 (64-bit) or Windows Server 2016.

Packages include:

  * [MongoDB plugin](/documentation/current/en/manual/appendix/config/zabbix_agent2_plugins/mongodb_plugin)
  * [PostgreSQL plugin](/documentation/current/en/manual/appendix/config/zabbix_agent2_plugins/postgresql_plugin)
  * [MSSQL plugin](/documentation/current/en/manual/appendix/config/zabbix_agent2_plugins/mssql_plugin)

Packages do not include the [Ember+ plugin](/documentation/current/en/manual/appendix/config/zabbix_agent2_plugins/ember_plus_plugin), which is currently only available to be built from source (for both Unix and Windows).

Before installing a plugin, check its README file. It may contain additional requirements and installation instructions specific to the plugin.

Similarly to Zabbix agent/agent2, loadable plugins can be installed using the Setup Wizard or the command line.

##### Installation from Setup Wizard

1\. Double-click the downloaded MSI file to start the installation.

2\. Accept the End-User License Agreement.

3\. Select the Zabbix agent 2 loadable plugins ([MongoDB plugin](/documentation/current/en/manual/appendix/config/zabbix_agent2_plugins/mongodb_plugin), [PostgreSQL plugin](/documentation/current/en/manual/appendix/config/zabbix_agent2_plugins/postgresql_plugin), [MSSQL plugin](/documentation/current/en/manual/appendix/config/zabbix_agent2_plugins/mssql_plugin)) to be installed.

It is recommended to use the default installation location provided by the installer. Using a custom location without the necessary permissions may compromise the security of the installation.

4\. Click _Install_ to begin the installation.

All selected Zabbix agent 2 loadable plugins will be installed in your specified location (default: `C:\Program Files\Zabbix Agent 2`), with their configuration files installed in the `zabbix_agent2.d` subfolder.

5\. Click the _Finish_ button to exit the Setup Wizard.

##### Installation from command line

Zabbix agent 2 loadable plugins can be installed from the command line by running the MSI installer with [msiexec](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/msiexec). For example:
    
    
    msiexec.exe /l*v "C:\package.log" /i "C:\zabbix_agent2_plugins-7.4.0-windows-amd64.msi" /qn+

Copy

✔ Copied

Zabbix agent 2 loadable plugin MSI installer packages support the following parameters.

ADDDEFAULT | A list of comma-delimited components to install in their default configuration. For more information, see [ADDDEFAULT property](https://learn.microsoft.com/en-us/windows/win32/msi/adddefault).  
Possible values: `MongodbPlugin`, `PostgresqlPlugin`, `MssqlPlugin`, `ALL`  
Example: `ADDDEFAULT=MongodbPlugin,PostgresqlPlugin`  
---|---  
ADDLOCAL | A list of comma-delimited components to install locally. For more information, see [ADDLOCAL property](https://learn.microsoft.com/en-us/windows/win32/msi/addlocal).  
Possible values: `MongodbPlugin`, `PostgresqlPlugin`, `MssqlPlugin`, `ALL`  
Example: `ADDLOCAL=MongodbPlugin,MssqlPlugin`  
INSTALLFOLDER | The full pathname to a folder where Zabbix components will be installed, with their configuration files installed in the `zabbix_agent2.d` subfolder.  
Example: `INSTALLFOLDER="C:\Program Files\Zabbix Agent 2"`