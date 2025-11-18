---
title: Security best practices
source: https://www.zabbix.com/documentation/current/en/manual/best_practices/security
downloaded: 2025-11-14 10:39:47
---

# 1 Security best practices

#### Overview

This section contains best practices for setting up Zabbix in a secure way.

The practices in this section are not required for the functioning of Zabbix but are recommended for better system security.

#### UTF-8 encoding

UTF-8 is the only encoding supported by Zabbix. It is known to work without any security flaws. Users should be aware that there are known security issues if using some of the other encodings.

#### Windows installer paths

When using Windows installers, it is recommended to use the default paths provided by the installer. Using custom paths without proper permissions could compromise the security of the installation.

#### Zabbix Security Advisories and CVE database

See [_Zabbix Security Advisories and CVE database_](https://www.zabbix.com/security_advisories).