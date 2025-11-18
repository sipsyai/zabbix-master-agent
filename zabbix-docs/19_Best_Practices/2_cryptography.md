---
title: Cryptography
source: https://www.zabbix.com/documentation/current/en/manual/best_practices/security/cryptography
downloaded: 2025-11-14 10:39:51
---

# 2 Cryptography

#### Overview

This section contains best practices for setting up cryptography in a secure way.

#### Setting up SSL for Zabbix frontend

On RHEL-based systems, install the `mod_ssl` package:
    
    
    dnf install mod_ssl

Copy

✔ Copied

Create a directory for SSL keys:
    
    
    mkdir -p /etc/httpd/ssl/private
           chmod 700 /etc/httpd/ssl/private

Copy

✔ Copied

Create the SSL certificate:
    
    
    openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/httpd/ssl/private/apache-selfsigned.key -out /etc/httpd/ssl/apache-selfsigned.crt

Copy

✔ Copied

Fill out the prompts appropriately. The most important line is the one that requests the `Common Name`. You must enter the domain name you want to be associated with your server. You can enter the public IP address instead if you do not have a domain name.
    
    
    Country Name (2 letter code) [XX]:
           State or Province Name (full name) []:
           Locality Name (eg, city) [Default City]:
           Organization Name (eg, company) [Default Company Ltd]:
           Organizational Unit Name (eg, section) []:
           Common Name (eg, your name or your server's hostname) []:example.com
           Email Address []:

Copy

✔ Copied

Edit the Apache SSL configuration file (`/etc/httpd/conf.d/ssl.conf`):
    
    
    DocumentRoot "/usr/share/zabbix"
           ServerName example.com:443
           SSLCertificateFile /etc/httpd/ssl/apache-selfsigned.crt
           SSLCertificateKeyFile /etc/httpd/ssl/private/apache-selfsigned.key

Copy

✔ Copied

Restart the Apache service to apply the changes:
    
    
    systemctl restart httpd.service

Copy

✔ Copied