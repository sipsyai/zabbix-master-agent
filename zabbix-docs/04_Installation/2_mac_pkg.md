---
title: macOS agent installation from PKG
source: https://www.zabbix.com/documentation/current/en/manual/installation/install_from_packages/mac_pkg
downloaded: 2025-11-14 10:34:09
---

# 2 macOS agent installation from PKG  
  
#### Overview

Zabbix agent can be installed on macOS using PKG installer packages, available for [download](https://www.zabbix.com/download_agents?os=macOS).

Zabbix agent packages are available with or without [encryption](/documentation/current/en/manual/encryption).

#### Installing agent

The agent can be installed using the graphical user interface or from the command line, for example:
    
    
    sudo installer -pkg zabbix_agent-7.4.0-macos-arm64-openssl.pkg -target /

Copy

✔ Copied

Make sure to use the correct Zabbix package version in the command. It must match the name of the downloaded package.

#### Running agent

The agent will start automatically after installation or restart.

You may edit the configuration file at `/usr/local/etc/zabbix/zabbix_agentd.conf` if necessary.

To start the agent manually, you may run:
    
    
    sudo launchctl start com.zabbix.zabbix_agentd

Copy

✔ Copied

To stop the agent manually:
    
    
    sudo launchctl stop com.zabbix.zabbix_agentd

Copy

✔ Copied

During upgrade, the existing configuration file is not overwritten. Instead a new `zabbix_agentd.conf.NEW` file is created to be used for reviewing and updating the existing configuration file, if necessary. Remember to restart the agent after manual changes to the configuration file.

#### Troubleshooting and removing agent

This section lists some useful commands that can be used for troubleshooting and removing Zabbix agent installation.

See if Zabbix agent is running:
    
    
    ps aux | grep zabbix_agentd

Copy

✔ Copied

See if Zabbix agent has been installed from packages:
    
    
    pkgutil --pkgs | grep zabbix 
           com.zabbix.pkg.ZabbixAgent

Copy

✔ Copied

See the files that were installed from the installer package (note that the initial `/` is not displayed in this view):
    
    
    pkgutil --only-files --files com.zabbix.pkg.ZabbixAgent
           Library/LaunchDaemons/com.zabbix.zabbix_agentd.plist                                                                                                                                                                                                                           
           usr/local/bin/zabbix_get                                                                                                                                                                                                                                                       
           usr/local/bin/zabbix_sender                                                                                                                                                                                                                                                    
           usr/local/etc/zabbix/zabbix_agentd/userparameter_examples.conf.NEW                                                                                                                                                                                                             
           usr/local/etc/zabbix/zabbix_agentd/userparameter_mysql.conf.NEW                                                                                                                                                                                                                
           usr/local/etc/zabbix/zabbix_agentd.conf.NEW                                                                                                                                                                                                                                    
           usr/local/sbin/zabbix_agentd

Copy

✔ Copied

Stop Zabbix agent if it was launched with `launchctl`:
    
    
    sudo launchctl unload /Library/LaunchDaemons/com.zabbix.zabbix_agentd.plist

Copy

✔ Copied

Remove files (including configuration and logs) that were installed with installer package:
    
    
    sudo rm -f /Library/LaunchDaemons/com.zabbix.zabbix_agentd.plist
           sudo rm -f /usr/local/sbin/zabbix_agentd
           sudo rm -f /usr/local/bin/zabbix_get
           sudo rm -f /usr/local/bin/zabbix_sender
           sudo rm -rf /usr/local/etc/zabbix
           sudo rm -rf /var/log/zabbix

Copy

✔ Copied

Forget that Zabbix agent has been installed:
    
    
    sudo pkgutil --forget com.zabbix.pkg.ZabbixAgent

Copy

✔ Copied