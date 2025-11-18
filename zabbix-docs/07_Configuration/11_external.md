---
title: External checks
source: https://www.zabbix.com/documentation/current/en/manual/config/items/itemtypes/external
downloaded: 2025-11-14 10:35:12
---

# 11 External checks

#### Overview

External check is a check executed by Zabbix server by [running a shell script](/documentation/current/en/manual/appendix/command_execution) or a binary. However, when hosts are monitored by a Zabbix proxy, the external checks are executed by the proxy.

External checks do not require any agent running on a host being monitored.

The syntax of the item key is:
    
    
    script[<parameter1>,<parameter2>,...]

Copy

✔ Copied

Where:

**script** | Name of a shell script or a binary.  
---|---  
**parameter(s)** | Optional command line parameters.  
  
If you don't want to pass any parameters to the script you may use:
    
    
    script[] or
           script

Copy

✔ Copied

Zabbix server or proxy will search the directory specified for external scripts and execute the command (see `ExternalScripts` parameter in Zabbix [server](/documentation/current/en/manual/appendix/config/zabbix_server#externalscripts)/[proxy](/documentation/current/en/manual/appendix/config/zabbix_proxy#externalscripts) configuration file). The command will be executed under the same user as Zabbix server/proxy, so any access permissions or environment variables should be handled in a wrapper script, if necessary. Permissions on the command should also allow that user to execute it. Only commands in the specified directory are available for execution.

Do not overuse external checks, as each script requires starting a fork process by Zabbix server/proxy, and running many scripts can significantly decrease Zabbix performance.

#### Usage example

Executing the script **check_oracle.sh** with the first parameters '-h'. The second parameter will be replaced by IP address or DNS name, depending on the selection in the host properties.
    
    
    check_oracle.sh["-h","{HOST.CONN}"]

Copy

✔ Copied

Assuming host is configured to use IP address, Zabbix server/proxy will execute:
    
    
    check_oracle.sh '-h' '192.168.1.4'

Copy

✔ Copied

#### External check result

The return value of an external check is a standard output together with a standard error produced by the check.

An item that returns text (character, log, or text type of information) will not become unsupported in case of a standard error output.

The return value is limited to 16MB (including trailing whitespace that is truncated); [database limits](/documentation/current/en/manual/config/items/item#text-data-limits) also apply.

If the requested script is not found or Zabbix server/proxy has no permissions to execute it, the item will become unsupported and a corresponding error message will be displayed.

In case of a timeout, the item will become unsupported, a corresponding error message will be displayed, and the process forked for the script will be terminated.