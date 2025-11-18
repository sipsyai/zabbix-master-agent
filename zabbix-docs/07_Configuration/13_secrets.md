---
title: Storage of secrets
source: https://www.zabbix.com/documentation/current/en/manual/config/secrets
downloaded: 2025-11-14 10:36:39
---

# 13 Storage of secrets

#### Overview

Zabbix can be configured to retrieve sensitive information from a secure vault. The following secret management services are supported: HashiCorp Vault KV Secrets Engine - Version 2, CyberArk Vault CV12.

Secrets can be used for retrieving:

  * [user macro values](/documentation/current/en/manual/config/macros/secret_macros#vault-secret)
  * database access credentials

Zabbix provides read-only access to the secrets in a vault, assuming that secrets are managed by someone else.

For information about specific vault provider configuration, see:

  * [HashiCorp configuration](/documentation/current/en/manual/config/secrets/hashicorp)
  * [CyberArk configuration](/documentation/current/en/manual/config/secrets/cyberark)

#### Caching of secret values

By default, vault secret macro values are retrieved by Zabbix server on every refresh of configuration data and then stored in the configuration cache. Zabbix proxy receives values of vault secret macros from Zabbix server on each configuration sync and stores them in its own configuration cache.

Encryption must be enabled between Zabbix server and proxy; otherwise a server warning message is logged.

It is also possible to [configure](/documentation/current/en/manual/web_interface/frontend_sections/administration/general#other) that macro values are retrieved by Zabbix server and Zabbix proxy independently.

To manually trigger refresh of cached secret values from a vault, use the 'secrets_reload' command-line [option](/documentation/current/en/manual/concepts/server#runtime-control).

For Zabbix frontend database credentials caching is disabled by default, but can be enabled by setting the option `$DB['VAULT_CACHE'] = true` in zabbix.conf.php. The credentials will be stored in a local cache using the filesystem temporary file directory. The web server must allow writing in a private temporary folder (for example, for Apache the configuration option `PrivateTmp=True` must be set). To control how often the data cache is refreshed/invalidated, use the ZBX_DATA_CACHE_TTL [constant](/documentation/current/en/manual/web_interface/definitions) .

#### TLS configuration

To configure TLS for communication between Zabbix components and the vault, add a certificate signed by a certificate authority (CA) to the system-wide default CA store. To use another location, specify the directory in the SSLCALocation Zabbix [server](/documentation/current/en/manual/appendix/config/zabbix_server)/[proxy](/documentation/current/en/manual/appendix/config/zabbix_proxy) configuration parameter, place the certificate file inside that directory, then run the CLI [command](https://www.openssl.org/docs/manmaster/man1/c_rehash.html):
    
    
    c_rehash .

Copy

✔ Copied