---
title: Connection type or permission problems
source: https://www.zabbix.com/documentation/current/en/manual/encryption/troubleshooting/connection_permission_problems
downloaded: 2025-11-14 10:37:49
---

# 1 Connection type or permission problems

#### Server is configured to connect with PSK to agent but agent accepts only unencrypted connections

In server or proxy log (with _GnuTLS_ 3.3.16)
    
    
    Get value from agent failed: zbx_tls_connect(): gnutls_handshake() failed: \
               -110 The TLS connection was non-properly terminated.

Copy

✔ Copied

In server or proxy log (with _OpenSSL_ 1.0.2c)
    
    
    Get value from agent failed: TCP connection successful, cannot establish TLS to [[127.0.0.1]:10050]: \
               Connection closed by peer. Check allowed connection types and access rights

Copy

✔ Copied

#### One side connects with certificate but other side accepts only PSK or vice versa

In any log (with _GnuTLS_):
    
    
    failed to accept an incoming connection: from 127.0.0.1: zbx_tls_accept(): gnutls_handshake() failed:\
               -21 Could not negotiate a supported cipher suite.

Copy

✔ Copied

In any log (with _OpenSSL_ 1.0.2c):
    
    
    failed to accept an incoming connection: from 127.0.0.1: TLS handshake returned error code 1:\
               file .\ssl\s3_srvr.c line 1411: error:1408A0C1:SSL routines:ssl3_get_client_hello:no shared cipher:\
               TLS write fatal alert "handshake failure"

Copy

✔ Copied

#### Attempting to use Zabbix sender compiled with TLS support to send data to Zabbix server/proxy compiled without TLS

##### In connecting-side log:

Linux:
    
    
    ...In zbx_tls_init_child()
           ...OpenSSL library (version OpenSSL 1.1.1  11 Sep 2018) initialized
           ...
           ...In zbx_tls_connect(): psk_identity:"PSK test sender"
           ...End of zbx_tls_connect():FAIL error:'connection closed by peer'
           ...send value error: TCP successful, cannot establish TLS to [[localhost]:10051]: connection closed by peer

Copy

✔ Copied

Windows:
    
    
    ...OpenSSL library (version OpenSSL 1.1.1a  20 Nov 2018) initialized
           ...
           ...In zbx_tls_connect(): psk_identity:"PSK test sender"
           ...zbx_psk_client_cb() requested PSK identity "PSK test sender"
           ...End of zbx_tls_connect():FAIL error:'SSL_connect() I/O error: [0x00000000] The operation completed successfully.'
           ...send value error: TCP successful, cannot establish TLS to [[192.168.1.2]:10051]: SSL_connect() I/O error: [0x00000000] The operation completed successfully.

Copy

✔ Copied

##### In accepting-side log:
    
    
    ...failed to accept an incoming connection: from 127.0.0.1: support for TLS was not compiled in

Copy

✔ Copied

#### One side connects with PSK but other side uses LibreSSL or has been compiled without encryption support

LibreSSL does not support PSK.

In connecting-side log:
    
    
    ...TCP successful, cannot establish TLS to [[192.168.1.2]:10050]: SSL_connect() I/O error: [0] Success

Copy

✔ Copied

In accepting-side log:
    
    
    ...failed to accept an incoming connection: from 192.168.1.2: support for PSK was not compiled in

Copy

✔ Copied

In Zabbix frontend:
    
    
    Get value from agent failed: TCP successful, cannot establish TLS to [[192.168.1.2]:10050]: SSL_connect() I/O error: [0] Success

Copy

✔ Copied

#### One side connects with PSK but other side uses OpenSSL with PSK support disabled

In connecting-side log:
    
    
    ...TCP successful, cannot establish TLS to [[192.168.1.2]:10050]: SSL_connect() set result code to SSL_ERROR_SSL: file ../ssl/record/rec_layer_s3.c line 1536: error:14094410:SSL routines:ssl3_read_bytes:sslv3 alert handshake failure: SSL alert number 40: TLS read fatal alert "handshake failure"

Copy

✔ Copied

In accepting-side log:
    
    
    ...failed to accept an incoming connection: from 192.168.1.2: TLS handshake set result code to 1: file ssl/statem/statem_srvr.c line 1422: error:1417A0C1:SSL routines:tls_post_process_client_hello:no shared cipher: TLS write fatal alert "handshake failure"

Copy

✔ Copied