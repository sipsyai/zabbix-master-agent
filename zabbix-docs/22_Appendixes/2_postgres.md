---
title: PostgreSQL encryption configuration
source: https://www.zabbix.com/documentation/current/en/manual/appendix/install/db_encrypt/postgres
downloaded: 2025-11-14 10:46:32
---

# 2 PostgreSQL encryption configuration

### Overview

This section provides several encryption configuration examples for CentOS 8.2 and PostgreSQL 13.

Connection between Zabbix frontend and PostgreSQL cannot be encrypted (parameters in GUI are disabled), if the value of _Database host_ field begins with a slash or the field is empty.

### Pre-requisites

Install the PostgreSQL database using the [official repository](https://www.postgresql.org/download/linux/redhat/).

PostgreSQL is not configured to accept TLS connections out-of-the-box. Please follow instructions from PostgreSQL documentation for [certificate preparation with postgresql.conf](https://www.postgresql.org/docs/13/ssl-tcp.html) and also for [user access control](https://www.postgresql.org/docs/13/auth-pg-hba-conf.html) through ph_hba.conf.

By default, the PostgreSQL socket is bound to the localhost, for the network remote connections to allow listening on the real network interface.

PostgreSQL settings for all [modes](/documentation/current/en/manual/appendix/install/db_encrypt#terminology) can look like this:

**/var/lib/pgsql/13/data/postgresql.conf:**
    
    
    ...
           ssl = on
           ssl_ca_file = 'root.crt'
           ssl_cert_file = 'server.crt'
           ssl_key_file = 'server.key'
           ssl_ciphers = 'HIGH:MEDIUM:+3DES:!aNULL'
           ssl_prefer_server_ciphers = on
           ssl_min_protocol_version = 'TLSv1.3'
           ...

Copy

✔ Copied

For access control adjust _/var/lib/pgsql/13/data/pg_hba.conf_ :
    
    
    ...
           ### require
           hostssl all all 0.0.0.0/0 md5
           
           ### verify CA
           hostssl all all 0.0.0.0/0 md5 clientcert=verify-ca
           
           ### verify full
           hostssl all all 0.0.0.0/0 md5 clientcert=verify-full
           ...

Copy

✔ Copied

### Transport-only encryption

#### Frontend

To enable transport-only encryption for connections between Zabbix frontend and the database:

  * Check _Database TLS encryption_
  * Leave _Verify database certificate_ unchecked

![](/documentation/current/assets/en/manual/appendix/install/encrypt_db_transport2.png)

#### Server

To enable transport-only encryption for connections between server and the database, configure _/etc/zabbix/zabbix_server.conf_ :
    
    
    ...
           DBHost=10.211.55.9
           DBName=zabbix
           DBUser=zbx_srv
           DBPassword=<strong_password>
           DBTLSConnect=required
           ...

Copy

✔ Copied

### Encryption with certificate authority verification

#### Frontend

To enable encryption with certificate authority verification for connections between Zabbix frontend and the database:

  * Check _Database TLS encryption_ and _Verify database certificate_
  * Specify path to _Database TLS CA file_

![](/documentation/current/assets/en/manual/appendix/install/encrypt_db_verify_ca2.png)

Alternatively, this can be set in _/etc/zabbix/web/zabbix.conf.php:_
    
    
    ...
           $DB['ENCRYPTION'] = true;
           $DB['KEY_FILE'] = '';
           $DB['CERT_FILE'] = '';
           $DB['CA_FILE'] = '/etc/ssl/pgsql/root.crt';
           $DB['VERIFY_HOST'] = false;
           $DB['CIPHER_LIST'] = '';
           ...

Copy

✔ Copied

#### Server

To enable encryption with certificate verification for connections between Zabbix server and the database, configure _/etc/zabbix/zabbix_server.conf:_
    
    
    ...
           DBHost=10.211.55.9
           DBName=zabbix
           DBUser=zbx_srv
           DBPassword=<strong_password>
           DBTLSConnect=verify_ca
           DBTLSCAFile=/etc/ssl/pgsql/root.crt
           ...

Copy

✔ Copied

### Encryption with full verification

#### Frontend

To enable encryption with certificate and database host identity verification for connections between Zabbix frontend and the database:

  * Check _Database TLS encryption_ and _Verify database certificate_
  * Specify path to _Database TLS key file_
  * Specify path to _Database TLS CA file_
  * Specify path to _Database TLS certificate file_
  * Check _Database host verification_

![](/documentation/current/assets/en/manual/appendix/install/encrypt_db_verify_full2.png)

Alternatively, this can be set in _/etc/zabbix/web/zabbix.conf.php:_
    
    
    $DB['ENCRYPTION'] = true;
           $DB['KEY_FILE'] = '';
           $DB['CERT_FILE'] = '';
           $DB['CA_FILE'] = '/etc/ssl/pgsql/root.crt';
           $DB['VERIFY_HOST'] = true;
           $DB['CIPHER_LIST'] = '';
           ...

Copy

✔ Copied

#### Server

To enable encryption with certificate and database host identity verification for connections between Zabbix server and the database, configure _/etc/zabbix/zabbix_server.conf_ :
    
    
    ...
           DBHost=10.211.55.9
           DBName=zabbix
           DBUser=zbx_srv
           DBPassword=<strong_password>
           DBTLSConnect=verify_full
           DBTLSCAFile=/etc/ssl/pgsql/root.crt
           DBTLSCertFile=/etc/ssl/pgsql/client.crt
           DBTLSKeyFile=/etc/ssl/pgsql/client.key
           ...

Copy

✔ Copied