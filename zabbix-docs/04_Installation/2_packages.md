---
title: Upgrade from packages
source: https://www.zabbix.com/documentation/current/en/manual/installation/upgrade/packages
downloaded: 2025-11-14 10:34:15
---

# 2 Upgrade from packages

#### Overview

This section provides the steps required for a successful [upgrade](/documentation/current/en/manual/installation/upgrade) using official RPM and DEB packages provided by Zabbix for:

  * [Red Hat Enterprise Linux](/documentation/current/en/manual/installation/upgrade/packages/rhel)
  * [Debian/Ubuntu](/documentation/current/en/manual/installation/upgrade/packages/debian_ubuntu)

##### Zabbix packages from OS repositories

Some OS distributions (in particular, Debian-based distributions) provide their own Zabbix packages. These packages **are not supported by Zabbix** and may be outdated or missing the latest features and bug fixes. It is recommended to use only official packages from the [Zabbix Official Repository](https://repo.zabbix.com/).

If you are upgrading from packages provided by OS distributions (or had them installed at some point), follow this procedure to switch to official Zabbix packages:

  1. Uninstall the old packages.
  2. Check for and remove any leftover files from the old installation.
  3. Install the official Zabbix packages following [installation instructions](https://www.zabbix.com/download) provided by Zabbix.

Do not perform a direct upgrade, as this may result in a broken installation.