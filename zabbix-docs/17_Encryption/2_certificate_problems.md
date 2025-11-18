---
title: Certificate problems
source: https://www.zabbix.com/documentation/current/en/manual/encryption/troubleshooting/certificate_problems
downloaded: 2025-11-14 10:37:50
---

# 2 Certificate problems

#### OpenSSL used with CRLs and for some CA in the certificate chain its CRL is not included in `TLSCRLFile`

In TLS server log in case of _OpenSSL_ peer:
    
    
    failed to accept an incoming connection: from 127.0.0.1: TLS handshake with 127.0.0.1 returned error code 1: \
               file s3_srvr.c line 3251: error:14089086: SSL routines:ssl3_get_client_certificate:certificate verify failed: \
               TLS write fatal alert "unknown CA"

Copy

✔ Copied

In TLS server log in case of _GnuTLS_ peer:
    
    
    failed to accept an incoming connection: from 127.0.0.1: TLS handshake with 127.0.0.1 returned error code 1: \
               file rsa_pk1.c line 103: error:0407006A: rsa routines:RSA_padding_check_PKCS1_type_1:\
               block type is not 01 file rsa_eay.c line 705: error:04067072: rsa routines:RSA_EAY_PUBLIC_DECRYPT:paddin

Copy

✔ Copied

#### CRL expired or expires during server operation

_OpenSSL_ , in server log:

  * before expiration:

    
    
    cannot connect to proxy "proxy-openssl-1.0.1e": TCP successful, cannot establish TLS to [[127.0.0.1]:20004]:\
               SSL_connect() returned SSL_ERROR_SSL: file s3_clnt.c line 1253: error:14090086:\
               SSL routines:ssl3_get_server_certificate:certificate verify failed:\
               TLS write fatal alert "certificate revoked"

Copy

✔ Copied

  * after expiration:

    
    
    cannot connect to proxy "proxy-openssl-1.0.1e": TCP successful, cannot establish TLS to [[127.0.0.1]:20004]:\
               SSL_connect() returned SSL_ERROR_SSL: file s3_clnt.c line 1253: error:14090086:\
               SSL routines:ssl3_get_server_certificate:certificate verify failed:\
               TLS write fatal alert "certificate expired"

Copy

✔ Copied

The point here is that with valid CRL a revoked certificate is reported as "certificate revoked". When CRL expires the error message changes to "certificate expired" which is quite misleading.

_GnuTLS_ , in server log:

  * before and after expiration the same:

    
    
    cannot connect to proxy "proxy-openssl-1.0.1e": TCP successful, cannot establish TLS to [[127.0.0.1]:20004]:\
                 invalid peer certificate: The certificate is NOT trusted. The certificate chain is revoked.

Copy

✔ Copied

#### Self-signed certificate, unknown CA

_OpenSSL_ , in log:
    
    
    error:'self signed certificate: SSL_connect() set result code to SSL_ERROR_SSL: file ../ssl/statem/statem_clnt.c\
                 line 1924: error:1416F086:SSL routines:tls_process_server_certificate:certificate verify failed:\
                 TLS write fatal alert "unknown CA"'

Copy

✔ Copied

This was observed when server certificate by mistake had the same Issuer and Subject string, although it was signed by CA. Issuer and Subject are equal in top-level CA certificate, but they cannot be equal in server certificate. (The same applies to proxy and agent certificates.)

To check whether a certificate contains the same Issuer and Subject entries, run:
    
    
    openssl x509 -in <yourcertificate.crt> -noout -text

It is acceptable for the root (top-level) certificate to have identical values for Issuer and Subject.