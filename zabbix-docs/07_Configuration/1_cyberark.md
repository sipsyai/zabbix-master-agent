---
title: CyberArk configuration
source: https://www.zabbix.com/documentation/current/en/manual/config/secrets/cyberark
downloaded: 2025-11-14 10:36:40
---

# 1 CyberArk configuration

This section explains how to configure Zabbix to retrieve secrets from CyberArk Vault CV12.

The vault should be installed and configured as described in the official [CyberArk documentation](https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/12.1/en/Content/HomeTilesLPs/LP-Tile6.htm?tocpath=Installation%7C_____0).

To learn about configuring TLS in Zabbix, see [_Storage of secrets_](/documentation/current/en/manual/config/secrets#tls-configuration).

### Database credentials

Access to a secret with database credentials is configured for each Zabbix component separately.

#### Server and proxies

To obtain database credentials from the vault for Zabbix [server](/documentation/current/en/manual/appendix/config/zabbix_server) or [proxy](/documentation/current/en/manual/appendix/config/zabbix_proxy), specify the following configuration parameters in the configuration file:

  * `Vault` \- which vault provider should be used;
  * `VaultURL` \- vault server HTTP[S] URL;
  * `VaultDBPath` \- query to the vault secret containing database credentials which will be retrieved by keys "Content" and "UserName" (this option can only be used if DBUser and DBPassword are not specified);
  * `VaultTLSCertFile`, `VaultTLSKeyFile` \- SSL certificate and key file names; setting up these options is not mandatory, but highly recommended;
  * `VaultPrefix` \- custom prefix for the vault path or query, depending on the vault; if not specified, the most suitable default will be used.

`Vault`, `VaultURL`, `VaultTLSCertFile`, `VaultTLSKeyFile`, and `VaultPrefix` configuration parameters are also used for vault authentication when processing secret vault macros by Zabbix server (and Zabbix proxy, if [configured](/documentation/current/en/manual/web_interface/frontend_sections/administration/general#other)). Zabbix server and proxies will not open vault secret macros that contain DB credentials from VaultDBPath.

Zabbix server and Zabbix proxy read the vault-related configuration parameters from _zabbix_server.conf_ and _zabbix_proxy.conf_ files upon startup.

##### Example

  1. In _zabbix_server.conf_ , specify the following parameters:

    
    
    Vault=CyberArk
           VaultURL=https://127.0.0.1:1858
           VaultDBPath=AppID=zabbix_server&Query=Safe=passwordSafe;Object=zabbix_server_database
           VaultTLSCertFile=cert.pem
           VaultTLSKeyFile=key.pem
           VaultPrefix=/AIMWebService/api/Accounts?

Copy

✔ Copied

  2. Zabbix will send the following API request to the vault:

    
    
    curl \
           --header "Content-Type: application/json" \
           --cert cert.pem \
           --key key.pem \
           https://127.0.0.1:1858/AIMWebService/api/Accounts?AppID=zabbix_server&Query=Safe=passwordSafe;Object=zabbix_server_database

Copy

✔ Copied

  3. The vault response will contain the keys "Content" and "UserName":

    
    
    {
               "Content": <password>,
               "UserName": <username>,
               "Address": <address>,
               "Database": <Database>,
               "PasswordChangeInProcess":<PasswordChangeInProcess>
           }

Copy

✔ Copied

  4. As a result, Zabbix will use the following credentials for database authentication:

  * Username: <username>
  * Password: <password>

#### Frontend

To obtain database credentials from the vault for Zabbix frontend, specify the following parameters during frontend [installation](/documentation/current/en/manual/installation/frontend).

  1. At the _Configure DB Connection_ step, set the _Store credentials in_ parameter to "CyberArk Vault".

![](/documentation/current/assets/en/manual/config/cyberark_setup.png)

  2. Then, fill in the additional parameters:

Vault API endpoint | yes | https://localhost:1858 | Specify the URL for connecting to the vault in the format `scheme://host:port`  
---|---|---|---  
Vault prefix | no | /AIMWebService/api/Accounts? | Provide a custom prefix for the vault path or query. If not specified, the default is used.  
Vault secret query string | yes |  | A query, which specifies from where database credentials should be retrieved.  
Example: `AppID=foo&Query=Safe=bar;Object=buzz`  
Vault certificates | no |  | After marking the checkbox, additional parameters will appear allowing to configure client authentication. While this parameter is optional, it is highly recommended to enable it for communication with the CyberArk Vault.  
SSL certificate file | no | conf/certs/cyberark-cert.pem | Path to the SSL certificate file. The file must be in PEM format.  
If the certificate file also contains the private key, leave the SSL key file parameter empty.  
SSL key file | no | conf/certs/cyberark-key.pem | Name of the SSL private key file used for client authentication. The file must be in PEM format.  
  
### User macro values

To use CyberArk Vault for storing _Vault secret_ user macro values, make sure that:

  * Zabbix server is [configured](/documentation/current/en/manual/config/secrets/cyberark#server-and-proxies) to work with CyberArk Vault;
  * the _Vault provider_ parameter in [_Administration → General → Other_](/documentation/current/en/manual/web_interface/frontend_sections/administration/general#other) is set to "CyberArk Vault".

![](/documentation/current/assets/en/manual/config/provider_cyberark.png)

Zabbix server (and Zabbix proxy, if [configured](/documentation/current/en/manual/web_interface/frontend_sections/administration/general#other)) require access to _Vault secret_ macro values from the vault. Zabbix frontend does not need such access.

The macro value should contain a query (as `query:key`).

See [_Vault secret macros_](/documentation/current/en/manual/config/macros/secret_macros#vault-secret) for detailed information on macro value processing by Zabbix.

#### Query syntax

The colon symbol (":") is reserved for separating the query from the key.

If a query itself contains a forward slash or a colon, these symbols should be URL-encoded ("/" is encoded as "%2F", ":" is encoded as "%3A").

#### Example

  1. In Zabbix, add a user macro {$PASSWORD} of type _Vault secret_ and with the value `AppID=zabbix_server&Query=Safe=passwordSafe;Object=zabbix:Content`

![](/documentation/current/assets/en/manual/config/cyberark_macro.png)

  2. Zabbix will send the following API request to the vault:

    
    
    curl \
           --header "Content-Type: application/json" \
           --cert cert.pem \
           --key key.pem \
           https://127.0.0.1:1858/AIMWebService/api/Accounts?AppID=zabbix_server&Query=Safe=passwordSafe;Object=zabbix_server_database

Copy

✔ Copied

  3. The vault response will contain the key "Content":

    
    
    {
               "Content": <password>,
               "UserName": <username>,
               "Address": <address>,
               "Database" :<Database>,
               "PasswordChangeInProcess":<PasswordChangeInProcess>
           }

Copy

✔ Copied

  4. As a result, Zabbix will resolve the macro {$PASSWORD} to the value - <password>

### Update existing configuration

To update an existing configuration for retrieving secrets from a CyberArk Vault:

  1. Update the Zabbix server or proxy configuration file parameters as described in the _Database credentials_ section.

  2. Update the DB connection settings by reconfiguring Zabbix frontend and specifying the required parameters as described in the _Frontend_ section. To reconfigure Zabbix frontend, open the frontend setup URL in the browser:

  * for Apache: http://<server_ip_or_name>/zabbix/setup.php
  * for Nginx: http://<server_ip_or_name>/setup.php

Alternatively, these parameters can be set in the [frontend configuration file](/documentation/current/en/manual/installation/frontend#install) (_zabbix.conf.php_):
    
    
    $DB['VAULT']                    = 'CyberArk';
           $DB['VAULT_URL']                = 'https://127.0.0.1:1858';
           $DB['VAULT_DB_PATH']            = 'AppID=foo&Query=Safe=bar;Object=buzz';
           $DB['VAULT_TOKEN']              = '';
           $DB['VAULT_CERT_FILE']          = 'conf/certs/cyberark-cert.pem';
           $DB['VAULT_KEY_FILE']           = 'conf/certs/cyberark-key.pem';
           $DB['VAULT_PREFIX']             = '';

Copy

✔ Copied

  3. Configure user macros as described in the _User macro values_ section, if necessary.

To update an existing configuration for retrieving secrets from a HashiCorp Vault, see [_HashiCorp configuration_](/documentation/current/en/manual/config/secrets/hashicorp#update-existing-configuration).