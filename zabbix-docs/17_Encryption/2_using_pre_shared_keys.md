---
title: Using pre-shared keys
source: https://www.zabbix.com/documentation/current/en/manual/encryption/using_pre_shared_keys
downloaded: 2025-11-14 10:37:47
---

# 2 Using pre-shared keys

#### Overview

Each pre-shared key (PSK) in Zabbix actually is a pair of:

  * non-secret PSK identity string,
  * secret PSK string value.

PSK identity string is a non-empty UTF-8 string. For example, "PSK ID 001 Zabbix agentd". It is a unique name by which this specific PSK is referred to by Zabbix components. Do not put sensitive information in PSK identity string - it is transmitted over the network unencrypted.

PSK value is a hard to guess string of hexadecimal digits, for example, "e560cb0d918d26d31b4f642181f5f570ad89a390931102e5391d08327ba434e9".

#### Size limits

There are size limits for PSK identity and value in Zabbix, in some cases a crypto library can have lower limit:

_Zabbix_ | 128 UTF-8 characters | 128-bit (16-byte PSK, entered as 32 hexadecimal digits) | 2048-bit (256-byte PSK, entered as 512 hexadecimal digits)  
---|---|---|---  
_GnuTLS_ | 128 bytes (may include UTF-8 characters) | - | 2048-bit (256-byte PSK, entered as 512 hexadecimal digits)  
_OpenSSL 1.0.x, 1.1.0_ | 127 bytes (may include UTF-8 characters) | - | 2048-bit (256-byte PSK, entered as 512 hexadecimal digits)  
_OpenSSL 1.1.1_ | 127 bytes (may include UTF-8 characters) | - | 512-bit (64-byte PSK, entered as 128 hexadecimal digits)  
_OpenSSL 1.1.1a and later_ | 127 bytes (may include UTF-8 characters) | - | 2048-bit (256-byte PSK, entered as 512 hexadecimal digits)  
  
Zabbix frontend allows configuring up to 128-character long PSK identity string and 2048-bit long PSK regardless of crypto libraries used.  
If some Zabbix components support lower limits, it is the user's responsibility to configure PSK identity and value with allowed length for these components.  
Exceeding length limits results in communication failures between Zabbix components.

Before Zabbix server connects to agent using PSK, the server looks up the PSK identity and PSK value configured for that agent in database (actually in configuration cache). Upon receiving a connection the agent uses PSK identity and PSK value from its configuration file. If both parties have the same PSK identity string and PSK value the connection may succeed.

Each PSK identity must be paired with only one value. It is the user's responsibility to ensure that there are no two PSKs with the same identity string but different values. Failing to do so may lead to unpredictable errors or disruptions of communication between Zabbix components using PSKs with this PSK identity string.

#### Generating PSK

For example, a 256-bit (32 bytes) PSK can be generated using the following commands:

  * with _OpenSSL_ :

    
    
      $ openssl rand -hex 32
             af8ced32dfe8714e548694e2d29e1a14ba6fa13f216cb35c19d0feb1084b0429

Copy

✔ Copied

  * with _GnuTLS_ :

    
    
      $ psktool -u psk_identity -p database.psk -s 32
             Generating a random key for user 'psk_identity'
             Key stored to database.psk
             
             $ cat database.psk 
             psk_identity:9b8eafedfaae00cece62e85d5f4792c7d9c9bcc851b23216a1d300311cc4f7cb

Copy

✔ Copied

Note that "psktool" above generates a database file with a PSK identity and its associated PSK. Zabbix expects just a PSK in the PSK file, so the identity string and colon (':') should be removed from the file.

#### Configuring PSK for server-agent communication (example)

On the agent host, write the PSK value into a file, for example, `/home/zabbix/zabbix_agentd.psk`. The file must contain PSK in the first text string, for example:
    
    
    1f87b595725ac58dd977beef14b97461a7c1045b9a1c963065002c5473194952

Copy

✔ Copied

Set access rights to PSK file - it must be readable only by Zabbix user.

Edit TLS parameters in agent configuration file `zabbix_agentd.conf`, for example, set:
    
    
    TLSConnect=psk
           TLSAccept=psk
           TLSPSKFile=/home/zabbix/zabbix_agentd.psk
           TLSPSKIdentity=PSK 001

Copy

✔ Copied

The agent will connect to server (active checks) and accept from server and `zabbix_get` only connections using PSK. PSK identity will be "PSK 001".

Restart the agent. Now you can test the connection using `zabbix_get`, for example:
    
    
    zabbix_get -s 127.0.0.1 -k "system.cpu.load[all,avg1]" --tls-connect=psk --tls-psk-identity="PSK 001" --tls-psk-file=/home/zabbix/zabbix_agentd.psk

Copy

✔ Copied

(To minimize downtime see how to change connection type in [Connection encryption management](/documentation/current/en/manual/encryption?&#connection-encryption-management)).

Configure PSK encryption for this agent in Zabbix frontend:

  * Go to: _Data collection → Hosts_
  * Select host and click on **Encryption** tab

Example:

![psk_config.png](/documentation/current/assets/en/manual/encryption/psk_config.png)

All mandatory input fields are marked with a red asterisk.

When configuration cache is synchronized with database the new connections will use PSK. Check server and agent logfiles for error messages.

#### Configuring PSK for server - active proxy communication (example)

On the proxy, write the PSK value into a file, for example, `/home/zabbix/zabbix_proxy.psk`. The file must contain PSK in the first text string, for example:
    
    
    e560cb0d918d26d31b4f642181f5f570ad89a390931102e5391d08327ba434e9

Copy

✔ Copied

Set access rights to PSK file - it must be readable only by Zabbix user.

Edit TLS parameters in proxy configuration file `zabbix_proxy.conf`, for example, set:
    
    
    TLSConnect=psk
           TLSPSKFile=/home/zabbix/zabbix_proxy.psk
           TLSPSKIdentity=PSK 002

Copy

✔ Copied

The proxy will connect to server using PSK. PSK identity will be "PSK 002".

(To minimize downtime see how to change connection type in [Connection encryption management](/documentation/current/en/manual/encryption#connection-encryption-management)).

Configure PSK for this proxy in Zabbix frontend. Go to _Administration→Proxies_ , select the proxy, go to "Encryption" tab. In "Connections from proxy" mark `PSK`. Paste into "PSK identity" field "PSK 002" and "e560cb0d918d26d31b4f642181f5f570ad89a390931102e5391d08327ba434e9" into "PSK" field. Click "Update".

Restart proxy. It will start using PSK-based encrypted connections to server. Check server and proxy logfiles for error messages.

For a passive proxy the procedure is very similar. The only difference - set `TLSAccept=psk` in proxy configuration file and set "Connections to proxy" in Zabbix frontend to `PSK`.