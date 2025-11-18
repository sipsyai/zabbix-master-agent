---
title: HashiCorp configuration
source: https://www.zabbix.com/documentation/current/en/manual/config/secrets/hashicorp
downloaded: 2025-11-14 10:36:41
---

# 2 HashiCorp configuration

#### Overview

This section explains how to configure Zabbix for retrieving secrets from HashiCorp Vault KV Secrets Engine - Version 2.

The vault should be deployed and configured as described in the official [HashiCorp documentation](https://www.vaultproject.io/docs/secrets/kv/kv-v2).

To learn about configuring TLS in Zabbix, see [_Storage of secrets_](/documentation/current/en/manual/config/secrets#configuring-tls).

#### Retrieving database credentials

To retrieve a secret with database credentials successfully, it is required to configure both:

  * Zabbix server/proxy
  * Zabbix frontend

##### Server/proxy

To configure Zabbix [server](/documentation/current/en/manual/appendix/config/zabbix_server) or [proxy](/documentation/current/en/manual/appendix/config/zabbix_proxy), specify the following configuration parameters in the configuration file:

  * `Vault` \- which vault provider should be used;
  * `VaultToken` \- vault authentication token (see Zabbix server/proxy configuration file for details);
  * `VaultURL` \- vault server HTTP[S] URL;
  * `VaultDBPath` \- path to the vault secret containing database credentials (this option can only be used if DBUser and DBPassword are not specified); Zabbix server or proxy will retrieve the credentials by keys "password" and "username";
  * `VaultPrefix` \- custom prefix for the vault path or query, depending on the vault; if not specified, the most suitable default will be used.

`Vault`, `VaultToken`, `VaultURL`, and `VaultPrefix` configuration parameters are also used for vault authentication when processing secret vault macros by Zabbix server (and Zabbix proxy, if [configured](/documentation/current/en/manual/web_interface/frontend_sections/administration/general#other)). Zabbix server and proxies will not open vault secret macros that contain DB credentials from VaultDBPath.  
  
Using different tokens for different proxies is strongly recommended.

Zabbix server and Zabbix proxy read the vault-related configuration parameters from _zabbix_server.conf_ and _zabbix_proxy.conf_ upon startup. Additionally, Zabbix server and Zabbix proxy will read the `VAULT_TOKEN` environment variable once during startup and will unset it so that it would not be available through forked scripts; it is an error if both `VaultToken` and `VAULT_TOKEN` parameters contain a value.

**Example**

  1. In _zabbix_server.conf_ , specify the following parameters:

    
    
    Vault=HashiCorp
           VaultToken=YOUR_VAULT_TOKEN_HERE
           VaultURL=https://127.0.0.1:8200
           VaultDBPath=database
           VaultPrefix=/v1/secret/data/zabbix/

Copy

✔ Copied

  2. Run the following CLI commands to create the required secret in the vault:

    
    
    # Enable "secret/" mount point if not already enabled; note that "kv-v2" must be used.
           vault secrets enable -path=secret/ kv-v2
           
           # Put new secrets with keys username and password under mount point "secret/" and path "zabbix/database".
           vault kv put -mount=secret zabbix/database username=zabbix password=<password>
           
           # Test that secret is successfully added.
           vault kv get secret/zabbix/database
           
           # Finally test with Curl; note that "data" need to be manually added after mount point and "/v1" before the mount point, also see --capath parameter.
           curl --header "X-Vault-Token: <VaultToken>" https://127.0.0.1:8200/v1/secret/data/zabbix/database

Copy

✔ Copied

  3. As a result, Zabbix server will retrieve the following credentials for database authentication:

  * Username: zabbix
  * Password: <password>

##### Frontend

Zabbix frontend can be configured to retrieve database credentials from the vault either during frontend [installation](/documentation/current/en/manual/installation/frontend) or by updating the frontend configuration file (`zabbix.conf.php`).

If vault credentials have been changed since the previous frontend installation, rerun the frontend installation or update `zabbix.conf.php`. See also: Updating existing configuration.

During **frontend installation** the configuration parameters must be specified at the _Configure DB Connection_ step:

![](/documentation/current/assets/en/manual/config/hashicorp_setup.png)

  * Set the _Store credentials in_ parameter to "HashiCorp Vault".
  * Specify the connection parameters:

_Vault API endpoint_ | yes | https://localhost:8200 | Specify the URL for connecting to the vault in the format `scheme://host:port`  
---|---|---|---  
_Vault prefix_ | no | /v1/secret/data/ | Provide a custom prefix for the vault path or query. If not specified, the default is used.  
Example: `/v1/secret/data/zabbix/`  
_Vault secret path_ | no |  | A path to the secret from where credentials for the database shall be retrieved by the keys "password" and "username".  
Example: `database`  
_Vault authentication token_ | no |  | Provide an authentication token for read-only access to the secret path.  
See [HashiCorp documentation](https://learn.hashicorp.com/tutorials/vault/tokens) for information about creating tokens and vault policies.  
  
#### Retrieving user macro values

To use HashiCorp Vault for storing _Vault secret_ user macro values, make sure that:

  * Zabbix server/proxy is [configured](/documentation/current/en/manual/config/secrets/hashicorp#serverproxy) to work with HashiCorp Vault;
  * the _Vault provider_ parameter in [_Administration → General → Other_](/documentation/current/en/manual/web_interface/frontend_sections/administration/general#other) is set to "HashiCorp Vault" (default);

![](/documentation/current/assets/en/manual/config/provider_hashicorp.png)

Zabbix server (and Zabbix proxy, if [configured](/documentation/current/en/manual/web_interface/frontend_sections/administration/general#other)) require access to _Vault secret_ macro values from the vault. Zabbix frontend does not need such access.

The macro value should contain a reference path (as `path:key`, for example, `macros:password`). The authentication token specified during Zabbix server/proxy configuration (by the `VaultToken` parameter) must provide read-only access to this path.

See [_Vault secret macros_](/documentation/current/en/manual/config/macros/secret_macros#vault-secret) for detailed information on macro value processing by Zabbix.

**Path syntax**

The symbols forward slash ("/") and colon (":") are reserved.

A forward slash can only be used to separate a mount point from a path (e.g., _secret/zabbix_ where the mount point is "secret" and the path is "zabbix"). In the case of Vault macros, a colon can only be used to separate a path/query from a key.

It is possible to URL-encode the forward slash and colon symbols if there is a need to create a mount point with the name that is separated by a forward slash (e.g., _foo/bar/zabbix_ , where the mount point is "foo/bar" and the path is "zabbix", can be encoded as "foo%2Fbar/zabbix") and if a mount point name or path need to contain a colon.

**Example**

  1. In Zabbix, add a user macro {$PASSWORD} of type "Vault secret" and with the value `macros:password`

![](/documentation/current/assets/en/manual/config/hashi_macro.png)

  2. Run the following CLI commands to create required secret in the vault:

    
    
    # Enable "secret/" mount point if not already enabled; note that "kv-v2" must be used.
           vault secrets enable -path=secret/ kv-v2
           
           # Put new secret with key "password" under mount point "secret/" and path "zabbix/macros".
           vault kv put -mount=secret zabbix/macros password=<password>
           
           # Test that secret is successfully added.
           vault kv get secret/zabbix/macros
           
           # Finally test with Curl; note that "data" need to be manually added after mount point and "/v1" before the mount point, also see --capath parameter.
           curl --header "X-Vault-Token: <VaultToken>" https://127.0.0.1:8200/v1/secret/data/zabbix/macros

Copy

✔ Copied

  3. As a result, Zabbix will resolve the macro {$PASSWORD} to the value: <password>

#### Updating existing configuration

To update an existing configuration for retrieving secrets from a HashiCorp Vault:

  1. Update the Zabbix server or proxy configuration file parameters as described in the _Database credentials_ section.

  2. Update the DB connection settings by reconfiguring Zabbix frontend and specifying the required parameters as described in the _Frontend_ section. To reconfigure Zabbix frontend, open the frontend setup URL in the browser:

  * for Apache: http://<server_ip_or_name>/zabbix/setup.php
  * for Nginx: http://<server_ip_or_name>/setup.php

Alternatively, these parameters can be set in the [frontend configuration file](/documentation/current/en/manual/installation/frontend#install) (_zabbix.conf.php_):
    
    
    $DB['VAULT']                    = 'HashiCorp';
           $DB['VAULT_URL']                = 'https://localhost:8200';
           $DB['VAULT_DB_PATH']            = 'database';
           $DB['VAULT_TOKEN']              = '<mytoken>';
           $DB['VAULT_CERT_FILE']          = '';
           $DB['VAULT_KEY_FILE']           = '';
           $DB['VAULT_PREFIX']             = '/v1/secret/data/zabbix/';

Copy

✔ Copied

  3. Configure user macros as described in the _User macro values_ section, if necessary.

To update an existing configuration for retrieving secrets from a CyberArk Vault, see [_CyberArk configuration_](/documentation/current/en/manual/config/secrets/cyberark#update-existing-configuration).