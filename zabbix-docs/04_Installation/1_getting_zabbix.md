---
title: Getting Zabbix
source: https://www.zabbix.com/documentation/current/en/manual/installation/getting_zabbix
downloaded: 2025-11-14 10:34:01
---

# 1 Getting Zabbix

#### Overview

There are four ways of getting Zabbix:

  * Install it from the [distribution packages](/documentation/current/en/manual/installation/install_from_packages)
  * Download the latest source archive and [compile it yourself](/documentation/current/en/manual/installation/install)
  * Install it from the [containers](/documentation/current/en/manual/installation/containers)
  * Download the [virtual appliance](/documentation/current/en/manual/appliance)

To download the latest distribution packages, pre-compiled sources or the virtual appliance, go to the [Zabbix download page](https://www.zabbix.com/download), where direct links to latest versions are provided.

#### Getting Zabbix source code

There are several ways of getting Zabbix source code:

  * You can [download](https://www.zabbix.com/download_sources) the released stable versions from the official Zabbix website
  * You can [download](https://www.zabbix.com/developers) nightly builds from the official Zabbix website developer page
  * You can get the latest development version from the Git source code repository system: 
    * The primary location of the full repository is at <https://git.zabbix.com/scm/zbx/zabbix.git>
    * Master and supported releases are also mirrored to Github at <https://github.com/zabbix/zabbix>

A Git client must be installed to clone the repository. The official commandline Git client package is commonly called **git** in distributions. To install, for example, on Debian/Ubuntu, run:
    
    
    sudo apt-get update
           sudo apt-get install git

Copy

✔ Copied

To grab all Zabbix source, change to the directory you want to place the code in and execute:
    
    
    git clone https://git.zabbix.com/scm/zbx/zabbix.git

Copy

✔ Copied