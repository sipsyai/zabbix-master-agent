---
title: Secure connection to the database
source: https://www.zabbix.com/documentation/current/en/manual/appendix/install/db_encrypt
downloaded: 2025-11-14 10:46:30
---

# 5 Secure connection to the database

#### Overview

This section provides Zabbix setup steps and configuration examples for secure TLS connections between:

MySQL | Zabbix frontend, Zabbix server, Zabbix proxy  
---|---  
PostgreSQL | Zabbix frontend, Zabbix server, Zabbix proxy  
  
To set up connection encryption within the DBMS, see official vendor documentation for details:

  * [MySQL](https://dev.mysql.com/doc/refman/8.0/en/replication-encrypted-connections.html): source and replica replication database servers.
  * [MySQL](https://dev.mysql.com/doc/refman/8.0/en/group-replication-security.html): group replication, etc. database servers.
  * [PostgreSQL](https://www.postgresql.org/docs/current/encryption-options.html) encryption options.

All examples are based on the GA releases of MySQL CE (8.0) and PgSQL (13) available through official repositories using CentOS 8.

##### Requirements

The following is required to set up encryption:

  * Developer-supported operating system with OpenSSL >=1.1.X or alternative.

It is recommended to avoid OS in the end-of-life status, especially in the case of new installations

  * Database engine (RDBMS) installed and maintained from the official repository provided by developer. Operating systems often shipped with outdated database software versions for which encryption support is not implemented, for example RHEL 7 based systems and PostgreSQL 9.2, MariaDB 5.5 without encryption support. 

##### Terminology

Setting this option enforces to use TLS connection to database from Zabbix server/proxy and frontend to database:

  * `required` \- connect using TLS as transport mode without identity checks
  * `verify_ca` \- connect using TLS and verify certificate
  * `verify_full` \- connect using TLS, verify certificate and verify that database identity (CN) specified by DBHost matches its certificate

#### Zabbix configuration

##### Frontend to the database

A secure connection to the database can be configured during frontend installation:

  * Mark the _Database TLS encryption_ checkbox in the [Configure DB connection](/documentation/current/en/manual/installation/frontend#configure-db-connection) step to enable transport encryption.
  * Mark the _Verify database certificate_ checkbox that appears when _TLS encryption_ field is checked to enable encryption with certificates.

For MySQL, the _Database TLS encryption_ checkbox is disabled, if _Database host_ is set to localhost, because connection that uses a socket file (on Unix) or shared memory (on Windows) cannot be encrypted.  
For PostgreSQL, the _TLS encryption_ checkbox is disabled, if the value of the _Database host_ field begins with a slash or the field is empty.

The following parameters become available in the TLS encryption in certificates mode (if both checkboxes are marked):

_Database TLS CA file_ | Specify the full path to a valid TLS certificate authority (CA) file.  
---|---  
_Database TLS key file_ | Specify the full path to a valid TLS key file.  
_Database TLS certificate file_ | Specify the full path to a valid TLS certificate file.  
_Database host verification_ | Mark this checkbox to activate host verification.  
Disabled for MYSQL, because PHP MySQL library does not allow to skip the peer certificate validation step.  
_Database TLS cipher list_ | Specify a custom list of valid ciphers. The format of the cipher list must conform to the OpenSSL standard.  
Available for MySQL only.  
  
TLS parameters must point to valid files. If they point to non-existent or invalid files, it will lead to the authorization error.  
If certificate files are writable, the frontend generates a warning in the [System information](/documentation/current/en/manual/web_interface/frontend_sections/reports/status_of_zabbix) report that "TLS certificate files must be read-only." (displayed only if the PHP user is the owner of the certificate).  
  
Certificates protected by passwords are not supported.

##### Use cases

Zabbix frontend uses GUI interface to define possible options: `required`, `verify_ca`, `verify_full`. Specify required options in the installation wizard step _Configure DB connections_. These options are mapped to the configuration file (zabbix.conf.php) in the following manner:

![](/documentation/current/assets/en/manual/appendix/install/encrypt_db_transport.png) | ...  
// Used for TLS connection.  
$DB['ENCRYPTION'] = true;  
$DB['KEY_FILE'] = '';  
$DB['CERT_FILE'] = '';  
$DB['CA_FILE'] = '';  
$DB['VERIFY_HOST'] = false;  
$DB['CIPHER_LIST'] = '';  
... | Check _Database TLS encryption_  
Leave _Verify database certificate_ unchecked | Enable `required` mode.  
---|---|---|---  
![](/documentation/current/assets/en/manual/appendix/install/encrypt_db_verify_ca.png) | ...  
$DB['ENCRYPTION'] = true;  
$DB['KEY_FILE'] = '';  
$DB['CERT_FILE'] = '';  
$DB['CA_FILE'] = '/etc/ssl/mysql/ca.pem';  
$DB['VERIFY_HOST'] = false;  
$DB['CIPHER_LIST'] = '';  
... | 1\. Check _Database TLS encryption_ and _Verify database certificate_  
2\. Specify path to _Database TLS CA file_ | Enable `verify_ca` mode.  
![](/documentation/current/assets/en/manual/appendix/install/encrypt_db_verify_full1.png) | ...  
// Used for TLS connection with strictly defined Cipher list.  
$DB['ENCRYPTION'] = true;  
$DB['KEY_FILE'] = '<key_file_path>';  
$DB['CERT_FILE'] = '<key_file_path>';  
$DB['CA_FILE'] = '<key_file_path>';  
$DB['VERIFY_HOST'] = true;  
$DB['CIPHER_LIST'] = '<cipher_list>';  
...  
  
Or:  
  
...  
// Used for TLS connection without Cipher list defined - selected by MySQL server  
$DB['ENCRYPTION'] = true;  
$DB['KEY_FILE'] = '<key_file_path>';  
$DB['CERT_FILE'] = '<key_file_path>';  
$DB['CA_FILE'] = '<key_file_path>';  
$DB['VERIFY_HOST'] = true;  
$DB['CIPHER_LIST'] = '';  
... | 1\. Check _Database TLS encryption_ and _Verify database certificate_  
2\. Specify path to _Database TLS key file_  
3\. Specify path to _Database TLS CA file_  
4\. Specify path to _Database TLS certificate file_  
5\. Specify _Database TLS cipher list_ (optional) | Enable `verify_full` mode for MySQL.  
![](/documentation/current/assets/en/manual/appendix/install/encrypt_db_verify_full2.png) | ...  
$DB['ENCRYPTION'] = true;  
$DB['KEY_FILE'] = '<key_file_path>';  
$DB['CERT_FILE'] = '<key_file_path>';  
$DB['CA_FILE'] = '<key_file_path>';  
$DB['VERIFY_HOST'] = true;  
$DB['CIPHER_LIST'] = ' ';  
...  
| 1\. Check _Database TLS encryption_ and _Verify database certificate_  
2\. Specify path to _Database TLS key file_  
3\. Specify path to _Database TLS CA file_  
4\. Specify path to _Database TLS certificate file_  
5\. Check _Database host verification_ | Enable `verify_full` mode for PostgreSQL.  
  
**See also:** [Encryption configuration examples for MySQL](/documentation/current/en/manual/appendix/install/db_encrypt/mysql), [Encryption configuration examples for PostgreSQL](/documentation/current/en/manual/appendix/install/db_encrypt/postgres).

#### Zabbix server/proxy configuration

Secure connections to the database can be configured with the respective parameters in the Zabbix [server](/documentation/current/en/manual/appendix/config/zabbix_server) and/or [proxy](/documentation/current/en/manual/appendix/config/zabbix_proxy) configuration file.

None | Connection to the database without encryption.  
---|---  
1\. Set `DBTLSConnect=required` | Server/proxy make a TLS connection to the database. An unencrypted connection is not allowed.  
1\. Set `DBTLSConnect=verify_ca`  
2\. Set `DBTLSCAFile` \- specify the TLS certificate authority file | Server/proxy make a TLS connection to the database after verifying the database certificate.  
1\. Set `DBTLSConnect=verify_full`  
2\. Set `DBTLSCAFile` \- specify TLS certificate authority file | Server/proxy make a TLS connection to the database after verifying the database certificate and the database host identity.  
1\. Set `DBTLSCAFile` \- specify TLS certificate authority file  
2\. Set `DBTLSCertFile` \- specify the client public key certificate file  
3\. Set `DBTLSKeyFile` \- specify the client private key file | Server/proxy provide a client certificate while connecting to the database.  
1\. Set `DBTLSCipher` \- the list of encryption ciphers that the client permits for connections using TLS protocols up to TLS 1.2  
  
or `DBTLSCipher13` \- the list of encryption ciphers that the client permits for connections using TLS 1.3 protocol | (MySQL) TLS connection is made using a cipher from the provided list.  
(PostgreSQL) Setting this option will be considered as an error.