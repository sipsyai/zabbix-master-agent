---
title: Unstable releases
source: https://www.zabbix.com/documentation/current/en/manual/installation/install_from_packages/unstable
downloaded: 2025-11-14 10:34:10
---

# 3 Unstable releases

### Overview

The instructions below are for enabling unstable Zabbix release repositories (disabled by default) used for minor Zabbix version release candidates.

First, install or update to the latest zabbix-release package. To enable rc packages on your system do the following:

### Red Hat Enterprise Linux

Open the `/etc/yum.repos.d/zabbix.repo` file and set enabled=1 for the `zabbix-unstable` repo.
    
    
    [zabbix-unstable]
           name=Zabbix Official Repository (unstable) - $basearch
           baseurl=https://repo.zabbix.com/zabbix/7.4/unstable/rhel/8/$basearch/
           enabled=1
           gpgcheck=1
           gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-ZABBIX-A14FE591

Copy

✔ Copied

### Debian/Ubuntu

Open the `/etc/apt/sources.list.d/zabbix.list` and uncomment "Zabbix unstable repository".
    
    
    # Zabbix unstable repository
           deb https://repo.zabbix.com/zabbix/7.4/unstable/debian bullseye main
           deb-src https://repo.zabbix.com/zabbix/7.4/unstable/debian bullseye main

Copy

✔ Copied

### SUSE

Open the `/etc/zypp/repos.d/zabbix.repo` file and set enable=1 for the `zabbix-unstable` repo.
    
    
    [zabbix-unstable]
           name=Zabbix Official Repository
           type=rpm-md
           baseurl=https://repo.zabbix.com/zabbix/7.4/unstable/sles/15/x86_64/
           gpgcheck=1
           gpgkey=https://repo.zabbix.com/zabbix/7.4/unstable/sles/15/x86_64/repodata/repomd.xml.key
           enabled=1
           update=1

Copy

✔ Copied