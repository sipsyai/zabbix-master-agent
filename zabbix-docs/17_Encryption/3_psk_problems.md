---
title: PSK problems
source: https://www.zabbix.com/documentation/current/en/manual/encryption/troubleshooting/psk_problems
downloaded: 2025-11-14 10:37:51
---

# 3 PSK problems

#### PSK contains an odd number of hex-digits

Proxy or agent does not start, message in the proxy or agent log:
    
    
    invalid PSK in file "/home/zabbix/zabbix_proxy.psk"

Copy

✔ Copied

#### PSK identity string longer than 128 bytes is passed to GnuTLS

In TLS client side log:
    
    
    gnutls_handshake() failed: -110 The TLS connection was non-properly terminated.

Copy

✔ Copied

In TLS server side log.
    
    
    gnutls_handshake() failed: -90 The SRP username supplied is illegal.

Copy

✔ Copied

#### Too long PSK value used with OpenSSL 1.1.1

In connecting-side log:
    
    
    ...OpenSSL library (version OpenSSL 1.1.1  11 Sep 2018) initialized
           ...
           ...In zbx_tls_connect(): psk_identity:"PSK 1"
           ...zbx_psk_client_cb() requested PSK identity "PSK 1"
           ...End of zbx_tls_connect():FAIL error:'SSL_connect() set result code to SSL_ERROR_SSL: file ssl\statem\extensions_clnt.c line 801: error:14212044:SSL routines:tls_construct_ctos_early_data:internal error: TLS write fatal alert "internal error"'

Copy

✔ Copied

In accepting-side log:
    
    
    ...Message from 123.123.123.123 is missing header. Message ignored.

Copy

✔ Copied

This problem typically arises when upgrading OpenSSL from 1.0.x or 1.1.0 to 1.1.1 and if the PSK value is longer than 512-bit (64-byte PSK, entered as 128 hexadecimal digits).

See also: [Value size limits](/documentation/current/en/manual/encryption/using_pre_shared_keys#size-limits)