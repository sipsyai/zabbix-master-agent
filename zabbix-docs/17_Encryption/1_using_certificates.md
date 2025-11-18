---
title: Using certificates
source: https://www.zabbix.com/documentation/current/en/manual/encryption/using_certificates
downloaded: 2025-11-14 10:37:46
---

# 1 Using certificates

#### Overview

Zabbix can use RSA certificates in PEM format, signed by a public or an in-house certificate authority (CA).

Certificate verification is performed against a pre-configured CA certificate. Optionally, Certificate Revocation Lists (CRL) can be used.

Each Zabbix component can have only one certificate configured.

For more information on setting up and operating an internal CA, generating and signing certificate requests, and revoking certificates, refer to tutorials such as the [OpenSSL PKI Tutorial v2.0](http://pki-tutorial.readthedocs.org/en/latest/).

Carefully consider and test your certificate extensions. For more details, see Limitations on using X.509 v3 certificate extensions.

#### Certificate configuration parameters

The following configuration parameters are supported for setting up certificates on Zabbix components.

_TLSCAFile_ | yes | Full pathname of a file containing the top-level CA(s) certificates for peer certificate verification.  
If using a certificate chain with multiple members, order the certificates with lower level CA(s) certificates first, followed by higher level CA(s) certificates.  
Certificates from multiple CAs can be included in a single file.  
---|---|---  
_TLSCRLFile_ | no | Full pathname of a file containing Certificate Revocation Lists (CRL).  
_TLSCertFile_ | yes | Full pathname of a file containing the certificate.  
If using a certificate chain with multiple members, order the certificates with the server, proxy, or agent certificate first, followed by lower level CA(s) certificates, and concluded by higher level CA(s) certificates.  
_TLSKeyFile_ | yes | Full pathname of a file containing the private key.  
Ensure that this file is readable only by the [Zabbix user](/documentation/current/en/manual/installation/install#create-user-account) by setting appropriate access rights.  
_TLSServerCertIssuer_ | no | Allowed server certificate issuer.  
_TLSServerCertSubject_ | no | Allowed server certificate subject.  
  
#### Configuration examples

After setting up the necessary certificates, configure Zabbix components to use certificate-based encryption.

Below are detailed steps for configuring:

  * Zabbix server
  * Zabbix proxy
  * Zabbix agent

##### Zabbix server

1\. Prepare the CA certificate file.

In order to verify peer certificates, Zabbix server must have access to the file containing the top-level, self-signed root CA certificates. For example, if certificates from two independent root CAs are needed, place them into a file at `/home/zabbix/zabbix_ca_file.crt`:
    
    
    Certificate:
               Data:
                   Version: 3 (0x2)
                   Serial Number: 1 (0x1)
               Signature Algorithm: sha1WithRSAEncryption
                   Issuer: DC=com, DC=zabbix, O=Zabbix SIA, OU=Development group, CN=Root1 CA
                       ...
                   Subject: DC=com, DC=zabbix, O=Zabbix SIA, OU=Development group, CN=Root1 CA
                   Subject Public Key Info:
                       Public Key Algorithm: rsaEncryption
                           Public-Key: (2048 bit)
                       ...
                   X509v3 extensions:
                       X509v3 Key Usage: critical
                           Certificate Sign, CRL Sign
                       X509v3 Basic Constraints: critical
                           CA:TRUE
                       ...
           -----BEGIN CERTIFICATE-----
           MIID2jCCAsKgAwIBAgIBATANBgkqhkiG9w0BAQUFADB+MRMwEQYKCZImiZPyLGQB
           ....
           9wEzdN8uTrqoyU78gi12npLj08LegRKjb5hFTVmO
           -----END CERTIFICATE-----
           Certificate:
               Data:
                   Version: 3 (0x2)
                   Serial Number: 1 (0x1)
               Signature Algorithm: sha1WithRSAEncryption
                   Issuer: DC=com, DC=zabbix, O=Zabbix SIA, OU=Development group, CN=Root2 CA
                       ...
                   Subject: DC=com, DC=zabbix, O=Zabbix SIA, OU=Development group, CN=Root2 CA
                   Subject Public Key Info:
                       Public Key Algorithm: rsaEncryption
                           Public-Key: (2048 bit)
                       ....
                   X509v3 extensions:
                       X509v3 Key Usage: critical
                           Certificate Sign, CRL Sign
                       X509v3 Basic Constraints: critical
                           CA:TRUE
                       ....       
           -----BEGIN CERTIFICATE-----
           MIID3DCCAsSgAwIBAgIBATANBgkqhkiG9w0BAQUFADB/MRMwEQYKCZImiZPyLGQB
           ...
           vdGNYoSfvu41GQAR5Vj5FnRJRzv5XQOZ3B6894GY1zY=
           -----END CERTIFICATE-----

Copy

✔ Copied

2\. Place the Zabbix server certificate/certificate chain into a file, for example, at `/home/zabbix/zabbix_server.crt`. The first certificate is the Zabbix server certificate, followed by the intermediate CA certificate:
    
    
    Certificate:
               Data:
                   Version: 3 (0x2)
                   Serial Number: 1 (0x1)
               Signature Algorithm: sha1WithRSAEncryption
                   Issuer: DC=com, DC=zabbix, O=Zabbix SIA, OU=Development group, CN=Signing CA
                   ...
                   Subject: DC=com, DC=zabbix, O=Zabbix SIA, OU=Development group, CN=Zabbix server
                   Subject Public Key Info:
                       Public Key Algorithm: rsaEncryption
                           Public-Key: (2048 bit)
                           ...
                   X509v3 extensions:
                       X509v3 Key Usage: critical
                           Digital Signature, Key Encipherment
                       X509v3 Basic Constraints: 
                           CA:FALSE
                       ...
           -----BEGIN CERTIFICATE-----
           MIIECDCCAvCgAwIBAgIBATANBgkqhkiG9w0BAQUFADCBgTETMBEGCgmSJomT8ixk
           ...
           h02u1GHiy46GI+xfR3LsPwFKlkTaaLaL/6aaoQ==
           -----END CERTIFICATE-----
           Certificate:
               Data:
                   Version: 3 (0x2)
                   Serial Number: 2 (0x2)
               Signature Algorithm: sha1WithRSAEncryption
                   Issuer: DC=com, DC=zabbix, O=Zabbix SIA, OU=Development group, CN=Root1 CA
                   ...
                   Subject: DC=com, DC=zabbix, O=Zabbix SIA, OU=Development group, CN=Signing CA
                   Subject Public Key Info:
                       Public Key Algorithm: rsaEncryption
                           Public-Key: (2048 bit)
                       ...
                   X509v3 extensions:
                       X509v3 Key Usage: critical
                           Certificate Sign, CRL Sign
                       X509v3 Basic Constraints: critical
                           CA:TRUE, pathlen:0
                   ...
           -----BEGIN CERTIFICATE-----
           MIID4TCCAsmgAwIBAgIBAjANBgkqhkiG9w0BAQUFADB+MRMwEQYKCZImiZPyLGQB
           ...
           dyCeWnvL7u5sd6ffo8iRny0QzbHKmQt/wUtcVIvWXdMIFJM0Hw==
           -----END CERTIFICATE-----

Copy

✔ Copied

Use only the attributes mentioned above for both client and server certificates to avoid affecting the certificate verification process. For example, OpenSSL might fail to establish an encrypted connection if _X509v3 Subject Alternative Name_ or _Netscape Cert Type_ extensions are used. For more information, see Limitations on using X.509 v3 certificate extensions.

3\. Place the Zabbix server private key into a file, for example, at `/home/zabbix/zabbix_server.key`:
    
    
    -----BEGIN PRIVATE KEY-----
           MIIEwAIBADANBgkqhkiG9w0BAQEFAASCBKowggSmAgEAAoIBAQC9tIXIJoVnNXDl
           ...
           IJLkhbybBYEf47MLhffWa7XvZTY=
           -----END PRIVATE KEY-----

Copy

✔ Copied

4\. Edit the TLS configuration parameters in the [Zabbix server configuration file](/documentation/current/en/manual/appendix/config/zabbix_server):
    
    
    TLSCAFile=/home/zabbix/zabbix_ca_file.crt
           TLSCertFile=/home/zabbix/zabbix_server.crt
           TLSKeyFile=/home/zabbix/zabbix_server.key

Copy

✔ Copied

##### Zabbix proxy

1\. Prepare files with the top-level CA certificates, the Zabbix proxy certificate/certificate chain, and the private key as described in the Zabbix server section. Then, edit the `TLSCAFile`, `TLSCertFile`, and `TLSKeyFile` parameters in the [Zabbix proxy configuration file](/documentation/current/en/manual/appendix/config/zabbix_proxy) accordingly.

2\. Edit additional TLS parameters in the [Zabbix proxy configuration file](/documentation/current/en/manual/appendix/config/zabbix_proxy):

  * For active proxy: `TLSConnect=cert`
  * For passive proxy: `TLSAccept=cert`

To improve proxy security, you can also set the `TLSServerCertIssuer` and `TLSServerCertSubject` parameters. For more information, see Restricting allowed certificate issuer and subject.

TLS parameters in the final proxy configuration file may look as follows:
    
    
    TLSConnect=cert
           TLSAccept=cert
           TLSCAFile=/home/zabbix/zabbix_ca_file.crt
           TLSServerCertIssuer=CN=Signing CA,OU=Development group,O=Zabbix SIA,DC=zabbix,DC=com
           TLSServerCertSubject=CN=Zabbix server,OU=Development group,O=Zabbix SIA,DC=zabbix,DC=com
           TLSCertFile=/home/zabbix/zabbix_proxy.crt
           TLSKeyFile=/home/zabbix/zabbix_proxy.key

Copy

✔ Copied

3\. Configure encryption for this proxy in Zabbix frontend:

  * Go to: _Administration → Proxies_.
  * Select the proxy and click the _Encryption_ tab.

In the examples below, the _Issuer_ and _Subject_ fields are filled in. For more information on why and how to use these fields, see Restricting allowed certificate issuer and subject.

For active proxy:

![](/documentation/current/assets/en/manual/encryption/proxy_active_cert.png)

For passive proxy:

![](/documentation/current/assets/en/manual/encryption/proxy_passive_cert.png)

##### Zabbix agent

1\. Prepare files with the top-level CA certificates, the Zabbix agent certificate/certificate chain, and the private key as described in the Zabbix server section. Then, edit the `TLSCAFile`, `TLSCertFile`, and `TLSKeyFile` parameters in the [Zabbix agent configuration file](/documentation/current/en/manual/appendix/config/zabbix_agentd) accordingly.

2\. Edit additional TLS parameters in the [Zabbix agent configuration file](/documentation/current/en/manual/appendix/config/zabbix_agentd):

  * For active agent: `TLSConnect=cert`
  * For passive agent: `TLSAccept=cert`

To improve agent security, you can set the `TLSServerCertIssuer` and `TLSServerCertSubject` parameters. For more information, see Restricting allowed certificate issuer and subject.

The TLS parameters in the final agent configuration file may look as follows. Note that the example assumes that the host is monitored by a proxy, hence it is specified as the certificate Subject:
    
    
    TLSConnect=cert
           TLSAccept=cert
           TLSCAFile=/home/zabbix/zabbix_ca_file.crt
           TLSServerCertIssuer=CN=Signing CA,OU=Development group,O=Zabbix SIA,DC=zabbix,DC=com
           TLSServerCertSubject=CN=Zabbix proxy,OU=Development group,O=Zabbix SIA,DC=zabbix,DC=com
           TLSCertFile=/home/zabbix/zabbix_agentd.crt
           TLSKeyFile=/home/zabbix/zabbix_agentd.key

Copy

✔ Copied

3\. Configure encryption in Zabbix frontend for the host monitored by this agent.

  * Go to: _Data collection → Hosts_.
  * Select the host and click the _Encryption_ tab.

In the example below, the _Issuer_ and _Subject_ fields are filled in. For more information on why and how to use these fields, see Restricting allowed certificate issuer and subject.

![](/documentation/current/assets/en/manual/encryption/agent_config.png)

##### Zabbix web service

1\. Prepare files with the top-level CA certificates, the Zabbix web service certificate/certificate chain, and the private key as described in the Zabbix server section. Then, edit the `TLSCAFile`, `TLSCertFile`, and `TLSKeyFile` parameters in the [Zabbix web service configuration file](/documentation/current/en/manual/appendix/config/zabbix_web_service) accordingly.

2\. Edit an additional TLS parameter in the [Zabbix web service configuration file](/documentation/current/en/manual/appendix/config/zabbix_web_service): `TLSAccept=cert`

TLS parameters in the final web service configuration file may look as follows:
    
    
    TLSAccept=cert
           TLSCAFile=/home/zabbix/zabbix_ca_file.crt
           TLSCertFile=/home/zabbix/zabbix_web_service.crt
           TLSKeyFile=/home/zabbix/zabbix_web_service.key

Copy

✔ Copied

3\. Configure Zabbix server to connect to the TLS-configured Zabbix web service by editing the `WebServiceURL` parameter in the [Zabbix server configuration file](/documentation/current/en/manual/appendix/config/zabbix_server):
    
    
    WebServiceURL=https://example.com:443/report

Copy

✔ Copied

#### Restricting allowed certificate issuer and subject

When two Zabbix components (for example, server and agent) establish a TLS connection, they validate each other's certificates. If a peer certificate is signed by a trusted CA (with a pre-configured top-level certificate in `TLSCAFile`), is valid, has not expired, and passes other checks, then the communication between components can proceed. In this simplest case, the certificate issuer and subject are not verified.

However, this presents a risk: anyone with a valid certificate can impersonate anyone else (for example, a host certificate could be used to impersonate a server). While this may be acceptable in small environments where certificates are signed by a dedicated in-house CA and the risk of impersonation is low, it may not be sufficient in larger or more security-sensitive environments.

If your top-level CA issues certificates that should not be accepted by Zabbix or if you want to reduce the risk of impersonation, you can restrict allowed certificates by specifying their issuer and subject.

For example, in the Zabbix proxy configuration file, you could specify:
    
    
    TLSServerCertIssuer=CN=Signing CA,OU=Development group,O=Zabbix SIA,DC=zabbix,DC=com
           TLSServerCertSubject=CN=Zabbix server,OU=Development group,O=Zabbix SIA,DC=zabbix,DC=com

Copy

✔ Copied

With these settings, an active proxy will not communicate with a Zabbix server whose certificate has a different issuer or subject. Similarly, a passive proxy will not accept requests from such a server.

##### Rules for matching `Issuer` and `Subject` strings

The rules for matching `Issuer` and `Subject` strings are as follows:

  * `Issuer` and `Subject` strings are checked independently. Both are optional.
  * An unspecified string means that any string is accepted.
  * Strings are compared _as is_ and must match exactly.
  * UTF-8 characters are supported. However, wildcards (`*`) or regular expressions are not supported.
  * The following [RFC 4514](http://tools.ietf.org/html/rfc4514) requirements are implemented - characters that require escaping (with a '`\`' backslash, U+005C): 
    * anywhere in the string: '`"`' (U+0022), '`+`' (U+002B), '`,`' (U+002C), '`;`' (U+003B), '`<`' (U+003C), '`>`' (U+003E), '`\\`' (U+005C);
    * at the beginning of the string: space (' ', U+0020) or number sign ('`#`', U+0023);
    * at the end of the string: space (' ', U+0020).
  * Null characters (U+0000) are not supported. If a null character is encountered, the matching will fail.
  * [RFC 4517](http://tools.ietf.org/html/rfc4517) and [RFC 4518](http://tools.ietf.org/html/rfc4518) standards are not supported.

For example, if `Issuer` and `Subject` organization (`O`) strings contain trailing spaces and the `Subject` organizational unit (`OU`) string contains double quotes, these characters must be escaped:
    
    
    TLSServerCertIssuer=CN=Signing CA,OU=Development head,O=\ Example SIA\ ,DC=example,DC=com
           TLSServerCertSubject=CN=Zabbix server,OU=Development group \"5\",O=\ Example SIA\ ,DC=example,DC=com

Copy

✔ Copied

##### Field order and formatting

Zabbix follows the recommendations of [RFC 4514](http://tools.ietf.org/html/rfc4514), which specifies a "reverse" order for these fields, starting with the lowest-level fields (`CN`), proceeding to the mid-level fields (`OU`, `O`), and concluding with the highest-level fields (`DC`).
    
    
    TLSServerCertIssuer=CN=Signing CA,OU=Development group,O=Zabbix SIA,DC=zabbix,DC=com
           TLSServerCertSubject=CN=Zabbix proxy,OU=Development group,O=Zabbix SIA,DC=zabbix,DC=com

Copy

✔ Copied

In contrast, OpenSSL by default displays the `Issuer` and `Subject` strings in top-level to low-level order. In the following example, `Issuer` and `Subject` fields start with the top-level (`DC`) and end with the low-level (`CN`) field. The formatting with spaces and field separators also varies based on the options used, and thus will not match the format required by Zabbix.
    
    
    $ openssl x509 -noout -in /home/zabbix/zabbix_proxy.crt -issuer -subject
           issuer= /DC=com/DC=zabbix/O=Zabbix SIA/OU=Development group/CN=Signing CA
           subject= /DC=com/DC=zabbix/O=Zabbix SIA/OU=Development group/CN=Zabbix proxy
           
           $ openssl x509 -noout -text -in /home/zabbix/zabbix_proxy.crt
           Certificate:
               ...
                   Issuer: DC=com, DC=zabbix, O=Zabbix SIA, OU=Development group, CN=Signing CA
                   ...
                   Subject: DC=com, DC=zabbix, O=Zabbix SIA, OU=Development group, CN=Zabbix proxy

Copy

✔ Copied

To format _Issuer_ and _Subject_ strings correctly for Zabbix, invoke OpenSSL with the following options:
    
    
    $ openssl x509 -noout -issuer -subject \
               -nameopt esc_2253,esc_ctrl,utf8,dump_nostr,dump_unknown,dump_der,sep_comma_plus,dn_rev,sname\
               -in /home/zabbix/zabbix_proxy.crt

Copy

✔ Copied

The output will then be in reverse order, comma-separated, and usable in Zabbix configuration files and frontend:
    
    
    issuer= CN=Signing CA,OU=Development group,O=Zabbix SIA,DC=zabbix,DC=com
           subject= CN=Zabbix proxy,OU=Development group,O=Zabbix SIA,DC=zabbix,DC=com

Copy

✔ Copied

#### Limitations on using X.509 v3 certificate extensions

When implementing X.509 v3 certificates within Zabbix, certain extensions may not be fully supported or could result in inconsistent behavior.

**Subject Alternative Name extension**

Zabbix does not support the _Subject Alternative Name_ extension, which is used to specify alternative DNS names such as IP addresses or email addresses. Zabbix can only validate the value in the _Subject_ field of the certificate (see Restricting Allowed Certificate Issuer and Subject). If certificates include the `subjectAltName` field, the outcome of certificate validation may vary depending on the specific crypto toolkits used to compile Zabbix components. As a result, Zabbix may either accept or reject certificates based on these combinations.

**Extended Key Usage extension**

Zabbix supports the _Extended Key Usage_ extension. However, if used, it is generally required that both _clientAuth_ (for TLS WWW client authentication) and _serverAuth_ (for TLS WWW server authentication) attributes are specified. For example:

  * In passive checks, where Zabbix agent operates as a TLS server, the _serverAuth_ attribute must be included in the agent's certificate.
  * For active checks, where the agent operates as a TLS client, the _clientAuth_ attribute must be included in the agent's certificate.

While GnuTLS may issue a warning for key usage violations, it typically allows communication to proceed despite these warnings.

**Name Constraints extension**

Support for the _Name Constraints_ extension varies among crypto toolkits. Ensure that your chosen toolkit supports this extension. This extension may restrict Zabbix from loading CA certificates if this section is marked as critical, depending on the specific toolkit in use.

#### Certificate Revocation Lists (CRL)

If a certificate is compromised, the Certificate Authority (CA) can revoke it by including the certificate in a Certificate Revocation List (CRL). CRLs are managed through configuration files and can be specified using the `TLSCRLFile` parameter in server, proxy, and agent configuration files. For example:
    
    
    TLSCRLFile=/home/zabbix/zabbix_crl_file.crt

Copy

✔ Copied

In this case, `zabbix_crl_file.crt` may contain CRLs from multiple CAs, and could look like this:
    
    
    -----BEGIN X509 CRL-----
           MIIB/DCB5QIBATANBgkqhkiG9w0BAQUFADCBgTETMBEGCgmSJomT8ixkARkWA2Nv
           ...
           treZeUPjb7LSmZ3K2hpbZN7SoOZcAoHQ3GWd9npuctg=
           -----END X509 CRL-----
           -----BEGIN X509 CRL-----
           MIIB+TCB4gIBATANBgkqhkiG9w0BAQUFADB/MRMwEQYKCZImiZPyLGQBGRYDY29t
           ...
           CAEebS2CND3ShBedZ8YSil59O6JvaDP61lR5lNs=
           -----END X509 CRL-----

Copy

✔ Copied

The CRL file is loaded only when Zabbix starts. To update the CRL, restart Zabbix.

If Zabbix components are compiled with OpenSSL and CRLs are used, ensure that each top-level and intermediate CA in the certificate chains has a corresponding CRL (even if it is empty) included in the `TLSCRLFile`.