---
title: Get
source: https://www.zabbix.com/documentation/current/en/manual/concepts/get
downloaded: 2025-11-14 10:33:57
---

# 7 Get

#### Overview

Zabbix get is a command-line utility, which can be used to communicate with Zabbix agent and retrieve required information from the agent.

The utility is usually used for the troubleshooting of Zabbix agents.

See also [zabbix_utils](https://github.com/zabbix/python-zabbix-utils/blob/main/README.md) \- a Python library that has built-in functionality to act like Zabbix get.

#### Running Zabbix get

An example of running Zabbix get under UNIX to get the processor load value from the agent:
    
    
    cd bin
           ./zabbix_get -s 127.0.0.1 -p 10050 -k system.cpu.load[all,avg1]

Copy

✔ Copied

Another example of running Zabbix get for capturing a string from a website:
    
    
    cd bin
           ./zabbix_get -s 192.168.1.1 -p 10050 -k "web.page.regexp[www.example.com,,,\"USA: ([a-zA-Z0-9.-]+)\",,\1]"

Copy

✔ Copied

Note that the item key here contains a space so quotes are used to mark the item key to the shell. The quotes are not part of the item key; they will be trimmed by the shell and will not be passed to Zabbix agent.

If an item key is unsupported Zabbix get will return the exit code `1`.

Zabbix get accepts the following command line parameters:
    
    
    -s --host <host name or IP>             Specify host name or IP address of a host
           -p --port <port number>                 Specify port number of agent running on the host (default: 10050)
           -I --source-address <IP address>        Specify source IP address
           -t --timeout <seconds>                  Specify timeout. Valid range: 1-600 seconds (default: 30 seconds)
           -k --key <item key>                     Specify key of item to retrieve value for
           -P --protocol <value>                   Protocol used to communicate with agent. Values:
                                                       auto - connect using JSON protocol, fallback and retry with plaintext protocol (default)
                                                       json - connect using JSON protocol
                                                       plaintext - connect using plaintext protocol where just item key is sent (6.4.x and older releases)
           -h --help                               Display this help message
           -V --version                            Display version number
           
           --tls-connect <value>                   How to connect to agent. Values:
                                                       unencrypted - connect without encryption (default)
                                                       psk - connect using TLS and a pre-shared key
                                                       cert - connect using TLS and a certificate
           --tls-ca-file <CA file>                 Full pathname of a file containing the top-level CA(s) certificates for peer certificate verification
           --tls-crl-file <CRL file>               Full pathname of a file containing revoked certificates
           --tls-agent-cert-issuer <cert issuer>   Allowed agent certificate issuer
           --tls-agent-cert-subject <cert subject> Allowed agent certificate subject
           --tls-cert-file <cert file>             Full pathname of a file containing the certificate or certificate chain
           --tls-key-file <key file>               Full pathname of a file containing the private key
           --tls-psk-identity <PSK-identity>       Unique, case sensitive string used to identify the pre-shared key
           --tls-psk-file <PSK-file>               Full pathname of a file containing the pre-shared key
           --tls-cipher13 <cipher-string>          Cipher string for OpenSSL 1.1.1 or newer for TLS 1.3. Override the default ciphersuite selection criteria. This option is not available if OpenSSL version is less than 1.1.1
           --tls-cipher <cipher-string>            GnuTLS priority string (for TLS 1.2 and up) or OpenSSL cipher string (only for TLS 1.2). Override the default ciphersuite selection criteria

Copy

✔ Copied

See also [Zabbix get manpage](/documentation/current/en/manpages/zabbix_get) for more information.

Zabbix get on Windows can be run similarly:
    
    
    zabbix_get.exe [options]

Copy

✔ Copied