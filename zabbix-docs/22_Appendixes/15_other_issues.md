---
title: Other issues
source: https://www.zabbix.com/documentation/current/en/manual/appendix/other_issues
downloaded: 2025-11-14 10:47:59
---

# 15 Other issues

#### Login and systemd

We recommend [creating](/documentation/current/en/manual/installation/install#create-user-account) a _zabbix_ user as system user, that is, without ability to log in. Some users ignore this recommendation and use the same account to log in (e. g. using SSH) to host running Zabbix. This might crash Zabbix daemon on log out. In this case you will get something like the following in Zabbix server log:
    
    
    zabbix_server [27730]: [file:'selfmon.c',line:375] lock failed: [22] Invalid argument
           zabbix_server [27716]: [file:'dbconfig.c',line:5266] lock failed: [22] Invalid argument
           zabbix_server [27706]: [file:'log.c',line:238] lock failed: [22] Invalid argument

Copy

✔ Copied

and in Zabbix agent log:
    
    
    zabbix_agentd [27796]: [file:'log.c',line:238] lock failed: [22] Invalid argument

Copy

✔ Copied

This happens because of default systemd setting `RemoveIPC=yes` configured in `/etc/systemd/logind.conf`. When you log out of the system the semaphores created by Zabbix previously are removed which causes the crash.

A quote from systemd documentation:
    
    
    RemoveIPC=
           
           Controls whether System V and POSIX IPC objects belonging to the user shall be removed when the
           user fully logs out. Takes a boolean argument. If enabled, the user may not consume IPC resources
           after the last of the user's sessions terminated. This covers System V semaphores, shared memory
           and message queues, as well as POSIX shared memory and message queues. Note that IPC objects of the
           root user and other system users are excluded from the effect of this setting. Defaults to "yes".

Copy

✔ Copied

There are 2 solutions to this problem:

  1. (recommended) Stop using _zabbix_ account for anything else than Zabbix processes, create a dedicated account for other things.
  2. (not recommended) Set `RemoveIPC=no` in `/etc/systemd/logind.conf` and reboot the system. Note that `RemoveIPC` is a system-wide parameter, changing it will affect the whole system.

#### Using Zabbix frontend behind proxy

If Zabbix frontend runs behind proxy server, the cookie path in the proxy configuration file needs to be rewritten in order to match the reverse-proxied path. See examples below. If the cookie path is not rewritten, users may experience authorization issues, when trying to login to Zabbix frontend.

##### Example configuration for nginx
    
    
    # ..
           location / {
           # ..
           proxy_cookie_path /zabbix /;
           proxy_pass http://192.168.0.94/zabbix/;
           # ..

Copy

✔ Copied

##### Example configuration for Apache
    
    
    # ..
           ProxyPass "/" http://host/zabbix/
           ProxyPassReverse "/" http://host/zabbix/
           ProxyPassReverseCookiePath /zabbix /
           ProxyPassReverseCookieDomain host zabbix.example.com
           # ..

Copy

✔ Copied