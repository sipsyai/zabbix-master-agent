---
title: MySQL encryption configuration
source: https://www.zabbix.com/documentation/current/en/manual/appendix/install/db_encrypt/mysql
downloaded: 2025-11-14 10:46:31
---

# 1 MySQL encryption configuration  
  
### Overview

This section provides several encryption configuration examples for CentOS 8.2 and MySQL 8.0.30 and can be used as a quickstart guide for encrypting the connection to the database. 

If MySQL host is set to localhost, encryption options will not be available. In this case a connection between Zabbix frontend and the database uses a socket file (on Unix) or shared memory (on Windows) and cannot be encrypted.

List of encryption combinations is not limited to the ones listed on this page. There are a lot more combinations available.

### Pre-requisites

Install MySQL database from the [official repository](https://dev.mysql.com/downloads/repo/yum/).

See [MySQL documentation](https://dev.mysql.com/doc/mysql-yum-repo-quick-guide/en/) for details on how to use MySQL repo.

MySQL server is ready to accept secure connections using a self-signed certificate.

To see which users are using an encrypted connection, run the following query (Performance Schema should be turned ON):
    
    
    SELECT sbt.variable_value AS tls_version, t2.variable_value AS cipher, processlist_user AS user, processlist_host AS host 
           FROM performance_schema.status_by_thread  AS sbt
           JOIN performance_schema.threads AS t ON t.thread_id = sbt.thread_id
           JOIN performance_schema.status_by_thread AS t2 ON t2.thread_id = t.thread_id
           WHERE sbt.variable_name = 'Ssl_version' and t2.variable_name = 'Ssl_cipher'
           ORDER BY tls_version;

Copy

✔ Copied

### Transport-only encryption

#### MySQL configuration

Modern versions of the database are ready out-of-the-box for `required` [encryption mode](/documentation/current/en/manual/appendix/install/db_encrypt#terminology). A server-side certificate will be created after initial setup and launch.

Create users and roles for the main components:

For MySQL versions 8.4+, `caching_sha2_password` should be used instead of `mysql_native_password`.
    
    
    mysql> CREATE USER   
            'zbx_srv'@'%' IDENTIFIED WITH mysql_native_password BY '<strong_password>',   
            'zbx_web'@'%' IDENTIFIED WITH mysql_native_password BY '<strong_password>'
            REQUIRE SSL   
            PASSWORD HISTORY 5; 
           
           mysql> CREATE ROLE 'zbx_srv_role', 'zbx_web_role'; 
           
           mysql> GRANT SELECT, UPDATE, DELETE, INSERT, CREATE, DROP, ALTER, INDEX, REFERENCES ON zabbix.* TO 'zbx_srv_role'; 
           mysql> GRANT SELECT, UPDATE, DELETE, INSERT ON zabbix.* TO 'zbx_web_role'; 
           
           mysql> GRANT 'zbx_srv_role' TO 'zbx_srv'@'%'; 
           mysql> GRANT 'zbx_web_role' TO 'zbx_web'@'%'; 
           
           mysql> SET DEFAULT ROLE 'zbx_srv_role' TO 'zbx_srv'@'%'; 
           mysql> SET DEFAULT ROLE 'zbx_web_role' TO 'zbx_web'@'%';

Copy

✔ Copied

Note that the X.509 protocol is not used to check identity, but the user is configured to use only encrypted connections. See [MySQL documentation](https://dev.mysql.com/doc/refman/8.0/en/create-user.html#create-user-tls) for more details about configuring users.

Run to check connection (socket connection cannot be used to test secure connections):
    
    
    mysql -u zbx_srv -p -h 10.211.55.9 --ssl-mode=REQUIRED

Copy

✔ Copied

Check current status and available cipher suites:
    
    
    mysql> status
           --------------
           mysql Ver 8.0.21 for Linux on x86_64 (MySQL Community Server - GPL)
           
           Connection id: 62
           Current database:
           Current user: zbx_srv@bfdb.local
           SSL: Cipher in use is TLS_AES_256_GCM_SHA384
           
           
           mysql> SHOW SESSION STATUS LIKE 'Ssl_cipher_list'\G;
           *************************** 1. row ***************************
           Variable_name: Ssl_cipher_list
           Value: TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_128_GCM_SHA256:TLS_AES_128_CCM_SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-DSS-AES128-GCM-SHA256:DHE-RSA-AES128-SHA256:DHE-DSS-AES128-SHA256:DHE-DSS-AES256-GCM-SHA384:DHE-RSA-AES256-SHA256:DHE-DSS-AES256-SHA256:DHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:DHE-DSS-AES128-SHA:DHE-RSA-AES128-SHA:DHE-DSS-AES256-SHA:DHE-RSA-AES256-SHA:AES256-SHA:CAMELLIA256-SHA:CAMELLIA128-SHA:AES128-GCM-SHA256:AES256-GCM-SHA384:AES128-SHA256:AES256-SHA256:AES128-SHA
           1 row in set (0.00 sec)
           
           ERROR:
           No query specified

Copy

✔ Copied

#### Frontend

To enable transport-only encryption for connections between Zabbix frontend and the database:

  * Check _Database TLS encryption_
  * Leave _Verify database certificate_ unchecked

![](/documentation/current/assets/en/manual/appendix/install/encrypt_db_transport.png)

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

Copy required MySQL CA to the Zabbix frontend server, assign proper permissions to allow the webserver to read this file.

This mode doesn't work on RHEL 7 due to older MySQL libraries.

#### Frontend

To enable encryption with certificate verification for connections between Zabbix frontend and the database:

  * Check _Database TLS encryption_ and _Verify database certificate_
  * Specify path to Database TLS CA file

![](/documentation/current/assets/en/manual/appendix/install/encrypt_db_verify_ca.png)

Alternatively, this can be set in _/etc/zabbix/web/zabbix.conf.php_ :
    
    
    ...
           $DB['ENCRYPTION'] = true;
           $DB['KEY_FILE'] = '';
           $DB['CERT_FILE'] = '';
           $DB['CA_FILE'] = '/etc/ssl/mysql/ca.pem';
           $DB['VERIFY_HOST'] = false;
           $DB['CIPHER_LIST'] = '';
           ...

Copy

✔ Copied

Troubleshoot user using command-line tool to check if connection is possible for required user:
    
    
        mysql -u zbx_web -p -h 10.211.55.9 --ssl-mode=REQUIRED --ssl-ca=/var/lib/mysql/ca.pem

Copy

✔ Copied

#### Server

To enable encryption with certificate verification for connections between Zabbix server and the database, configure _/etc/zabbix/zabbix_server.conf_ :
    
    
    ...
           DBHost=10.211.55.9
           DBName=zabbix
           DBUser=zbx_srv
           DBPassword=<strong_password>
           DBTLSConnect=verify_ca
           DBTLSCAFile=/etc/ssl/mysql/ca.pem
           ...

Copy

✔ Copied

### Encryption with full verification

#### MySQL configuration

Set MySQL CE server configuration option (_/etc/my.cnf.d/server-tls.cnf_) to:
    
    
    [mysqld]
           ...
           # in this examples keys are located in the MySQL CE datadir directory
           ssl_ca=ca.pem
           ssl_cert=server-cert.pem
           ssl_key=server-key.pem
           
           require_secure_transport=ON
           tls_version=TLSv1.3
           ...

Copy

✔ Copied

Keys for the MySQL CE server and client (Zabbix frontend) should be created manually according to the MySQL CE documentation: [Creating SSL and RSA certificates and keys using MySQL](https://dev.mysql.com/doc/refman/8.0/en/creating-ssl-rsa-files-using-mysql.html) or[Creating SSL certificates and keys using openssl](https://dev.mysql.com/doc/refman/8.0/en/creating-ssl-files-using-openssl.html)

MySQL server certificate should contain the Common Name field set to the FQDN name as Zabbix frontend will use the DNS name to communicate with the database or IP address of the database host.

Create MySQL user:

For MySQL versions 8.4+, `caching_sha2_password` should be used instead of `mysql_native_password`.
    
    
    mysql> CREATE USER
             'zbx_srv'@'%' IDENTIFIED WITH mysql_native_password BY '<strong_password>',
             'zbx_web'@'%' IDENTIFIED WITH mysql_native_password BY '<strong_password>'
             REQUIRE X509
             PASSWORD HISTORY 5;

Copy

✔ Copied

Check if it is possible to log in with that user:
    
    
    mysql -u zbx_web -p -h 10.211.55.9 --ssl-mode=VERIFY_IDENTITY --ssl-ca=/var/lib/mysql/ca.pem --ssl-cert=/var/lib/mysql/client-cert.pem --ssl-key=/var/lib/mysql/client-key.pem

Copy

✔ Copied

#### Frontend

To enable encryption with full verification for connections between Zabbix frontend and the database:

  * Check _Database TLS encryption_ and _Verify database certificate_
  * Specify path to _Database TLS key file_
  * Specify path to _Database TLS CA file_
  * Specify path to _Database TLS certificate file_

Note that _Database host verification_ is checked and grayed out - this step cannot be skipped for MySQL.

If _Database TLS cipher list_ field is left empty, the common ciphers permitted by both frontend (client) and server will be enabled. Alternatively, the ciphers can be set explicitly, in conformance with the [cipher configuration requirements](https://dev.mysql.com/doc/refman/8.0/en/encrypted-connection-protocols-ciphers.html#encrypted-connection-cipher-configuration).

![](/documentation/current/assets/en/manual/appendix/install/encrypt_db_verify_full1.png)

Alternatively, this can be set in _/etc/zabbix/web/zabbix.conf.php_ :
    
    
    ...
           // Used for TLS connection with strictly defined Cipher list.
           $DB['ENCRYPTION'] = true;
           $DB['KEY_FILE'] = '/etc/ssl/mysql/client-key.pem';
           $DB['CERT_FILE'] = '/etc/ssl/mysql/client-cert.pem';
           $DB['CA_FILE'] = '/etc/ssl/mysql/ca.pem';
           $DB['VERIFY_HOST'] = true;
           $DB['CIPHER_LIST'] = 'TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_128_GCM_SHA256:TLS_AES_128_CCM_SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA256:ECDHE-RSA-AES256-GC';
           ...
           // or
           ...
           // Used for TLS connection without Cipher list defined - selected by MySQL server
           $DB['ENCRYPTION'] = true;
           $DB['KEY_FILE'] = '/etc/ssl/mysql/client-key.pem';
           $DB['CERT_FILE'] = '/etc/ssl/mysql/client-cert.pem';
           $DB['CA_FILE'] = '/etc/ssl/mysql/ca.pem';
           $DB['VERIFY_HOST'] = true;
           $DB['CIPHER_LIST'] = '';
           ...

Copy

✔ Copied

#### Server

To enable encryption with full verification for connections between Zabbix server and the database, configure _/etc/zabbix/zabbix_server.conf_ :
    
    
    ...
           DBHost=10.211.55.9
           DBName=zabbix
           DBUser=zbx_srv
           DBPassword=<strong_password>
           DBTLSConnect=verify_full
           DBTLSCAFile=/etc/ssl/mysql/ca.pem
           DBTLSCertFile=/etc/ssl/mysql/client-cert.pem
           DBTLSKeyFile=/etc/ssl/mysql/client-key.pem
           ...

Copy

✔ Copied