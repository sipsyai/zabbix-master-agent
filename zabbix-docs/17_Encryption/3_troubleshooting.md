---
title: Troubleshooting
source: https://www.zabbix.com/documentation/current/en/manual/encryption/troubleshooting
downloaded: 2025-11-14 10:37:48
---

# 3 Troubleshooting

#### General recommendations

  * Start with understanding which component acts as a TLS client and which one acts as a TLS server in problem case.  
Zabbix server, proxies and agents, depending on interaction between them, all can work as TLS servers and clients.  
For example, Zabbix server connecting to agent for a passive check, acts as a TLS client. The agent is in role of TLS server.  
Zabbix agent, requesting a list of active checks from proxy, acts as a TLS client. The proxy is in role of TLS server.  
`zabbix_get` and `zabbix_sender` utilities always act as TLS clients.
  * Zabbix uses mutual authentication.  
Each side verifies its peer and may refuse connection.  
For example, Zabbix server connecting to agent can close connection immediately if agent's certificate is invalid. And vice versa - Zabbix agent accepting a connection from server can close connection if server is not trusted by agent.
  * Examine logfiles in both sides - in TLS client and TLS server.  
The side which refuses connection may log a precise reason why it was refused. Other side often reports rather general error (e.g. "Connection closed by peer", "connection was non-properly terminated").
  * Sometimes misconfigured encryption results in confusing error messages in no way pointing to real cause.  
In subsections below we try to provide a (far from exhaustive) collection of messages and possible causes which could help in troubleshooting.  
Please note that different crypto toolkits (OpenSSL, GnuTLS) often produce different error messages in same problem situations.  
Sometimes error messages depend even on particular combination of crypto toolkits on both sides.