---
title: Secure connection to the frontend
source: https://www.zabbix.com/documentation/current/en/manual/appendix/install/frontend_encrypt
downloaded: 2025-11-14 10:46:33
---

# 6 Secure connection to the frontend

#### Overview

This section provides Zabbix setup steps and configuration examples for secure TLS connections between Zabbix frontend and Zabbix server.

#### Configuration

By default, communication between Zabbix frontend and Zabbix server is unencrypted. For better security, enable TLS on both sides. Below is an example of the simplest way to do this.

1\. Generate certificates and keys.

Create a working directory:
    
    
    sudo mkdir -p /etc/zabbix/ssl && cd /etc/zabbix/ssl

Copy

✔ Copied

Create a CA certificate (adjust the `MyZabbixCA` value to match the actual common name):
    
    
    sudo openssl genrsa -out ca.key 4096
           sudo openssl req -new -x509 -days 3650 -key ca.key -out ca.crt -subj "/CN=MyZabbixCA/"

Copy

✔ Copied

Generate a private key and certificate for Zabbix server (adjust the `zabbix-server.example.com` value to match the actual common name):
    
    
    sudo openssl genrsa -out server.key 2048
           sudo openssl req -new -key server.key -out server.csr -subj "/CN=zabbix-server.example.com/"
           sudo openssl x509 -req -days 365 -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -sha256 -out server.crt

Copy

✔ Copied

Generate a private key and certificate for Zabbix frontend (adjust the `zabbix-frontend-node` value to match the actual common name):
    
    
    sudo openssl genrsa -out frontend.key 2048
           sudo openssl req -new -key frontend.key -out frontend.csr -subj "/CN=zabbix-frontend-node/"
           sudo openssl x509 -req -days 365 -in frontend.csr -CA ca.crt -CAkey ca.key -CAcreateserial -sha256 -out frontend.crt

Copy

✔ Copied

2\. Set proper permissions.

For Zabbix server (adjust ownership/group according to your distribution's Zabbix server daemon user):
    
    
    sudo chown root:zabbix /etc/zabbix/ssl/server.{crt,key} /etc/zabbix/ssl/ca.crt
           sudo chmod 640 /etc/zabbix/ssl/server.key
           sudo chmod 644 /etc/zabbix/ssl/server.crt /etc/zabbix/ssl/ca.crt

Copy

✔ Copied

For frontend (adjust ownership/group according to your distribution's webserver user):
    
    
    sudo chown root:www-data /etc/zabbix/ssl/frontend.{crt,key}
           sudo chmod 640 /etc/zabbix/ssl/frontend.key
           sudo chmod 644 /etc/zabbix/ssl/frontend.crt

Copy

✔ Copied

3\. Configure Zabbix server.

In `zabbix_server.conf` add:
    
    
    TLSFrontendAccept=cert
           TLSCertFile=/etc/zabbix/ssl/server.crt
           TLSKeyFile=/etc/zabbix/ssl/server.key
           TLSCAFile=/etc/zabbix/ssl/ca.crt
           # Optionally:
           # TLSFrontendCertIssuer=/CN=MyZabbixCA/
           # TLSFrontendCertSubject=/CN=zabbix-frontend-node/

Copy

✔ Copied

Then restart the server:
    
    
    sudo systemctl restart zabbix-server

Copy

✔ Copied

4\. Configure Zabbix frontend.

During [web interface installation](/documentation/current/en/manual/installation/frontend), enable the _Encrypt connections from Web interface_ option (and _Verify server certificate issuer and subject_ option, if necessary) and fill in the _TLS CA file_ , _TLS key file_ , _TLS certificate file_ fields (and _Server TLS certificate issuer_ and _Server TLS certificate subject_ fields, if necessary):

![](/documentation/current/assets/en/manual/appendix/install/frontend_encrypt.png)

_TLS CA file_ | Specify the full path to the Certificate Authority (CA) certificate file used to verify the server’s certificate.  
---|---  
_TLS key file_ | Specify the full path to the client private key file corresponding to the client certificate.  
_TLS certificate file_ | Specify the full path to the client certificate file if mutual TLS authentication is required.  
_Server TLS certificate issuer_ | Specify a distinguished Name (DN) of the issuer to match against the server’s certificate.  
_Server TLS certificate subject_ | Specify a distinguished Name (DN) of the subject to match against the server’s certificate.  
  
On existing installations, edit the following fields in `zabbix.conf.php`:
    
    
    $ZBX_SERVER_TLS['ACTIVE'] = '1';
           $ZBX_SERVER_TLS['CA_FILE'] = '/etc/zabbix/ssl/ca.crt';
           $ZBX_SERVER_TLS['KEY_FILE'] = '/etc/zabbix/ssl/frontend.key';
           $ZBX_SERVER_TLS['CERT_FILE'] = '/etc/zabbix/ssl/frontend.crt';
           // Optionally:
           // $ZBX_SERVER_TLS['CERTIFICATE_ISSUER']  = '/CN=MyZabbixCA/';
           // $ZBX_SERVER_TLS['CERTIFICATE_SUBJECT'] = '/CN=zabbix-server.example.com/';

Copy

✔ Copied

5\. Verify encryption by confirming there are no error messages in Zabbix frontend or Zabbix server log file:
    
    
    tail -f /var/log/zabbix/zabbix_server.log

Copy

✔ Copied