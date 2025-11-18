---
title: Running agent as root
source: https://www.zabbix.com/documentation/current/en/manual/appendix/install/run_agent_as_root
downloaded: 2025-11-14 10:46:37
---

# 10 Running agent as root

Since Zabbix **5.0.0** , the systemd service file for Zabbix agent in [official packages](https://www.zabbix.com/download) explicitly includes directives for `User` and `Group`. Both are set to `zabbix`.

It is no longer possible to configure which user Zabbix agent runs as via `zabbix_agentd.conf` file, because the agent will bypass this configuration and run as the user specified in the systemd service file. To run Zabbix agent as root you need to make the modifications described below.

### Zabbix agent

To override the default user and group for Zabbix agent, run:
    
    
    systemctl edit zabbix-agent

Copy

✔ Copied

Then, add the following content:
    
    
    [Service]
           User=root
           Group=root

Copy

✔ Copied

Reload daemons and restart the zabbix-agent service:
    
    
    systemctl daemon-reload
           systemctl restart zabbix-agent

Copy

✔ Copied

For **Zabbix agent** this re-enables the functionality of configuring user in the `zabbix_agentd.conf` file. Now you need to set `User=root` and `AllowRoot=1` configuration parameters in the agent [configuration file](/documentation/current/en/manual/appendix/config/zabbix_agentd).

### Zabbix agent 2

To override the default user and group for Zabbix agent 2, run:
    
    
    systemctl edit zabbix-agent2

Copy

✔ Copied

Then, add the following content:
    
    
    [Service]
           User=root
           Group=root

Copy

✔ Copied

Reload daemons and restart the zabbix-agent2 service:
    
    
    systemctl daemon-reload
           systemctl restart zabbix-agent2

Copy

✔ Copied

For **Zabbix agent2** this completely determines the user that it runs as. No additional modifications are required.