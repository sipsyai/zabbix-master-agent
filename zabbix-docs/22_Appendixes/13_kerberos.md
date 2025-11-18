---
title: Configuring Kerberos with Zabbix
source: https://www.zabbix.com/documentation/current/en/manual/appendix/items/kerberos
downloaded: 2025-11-14 10:47:31
---

# 13 Configuring Kerberos with Zabbix

#### Overview

Kerberos authentication can be used in web monitoring and HTTP items in Zabbix.

This section describes an example of configuring Kerberos with Zabbix server to perform web monitoring of `www.example.com` with user 'zabbix'.

#### Steps

##### Step 1

Install Kerberos package.

For Debian/Ubuntu:
    
    
    apt install krb5-user

Copy

✔ Copied

For RHEL:
    
    
    dnf install krb5-workstation

Copy

✔ Copied

##### Step 2

Configure Kerberos configuration file (see MIT documentation for details)
    
    
    cat /etc/krb5.conf 
           [libdefaults]
               default_realm = EXAMPLE.COM
           
           # The following krb5.conf variables are only for MIT Kerberos.
               kdc_timesync = 1
               ccache_type = 4
               forwardable = true
               proxiable = true
           
           [realms]
               EXAMPLE.COM = {
               }
           
           [domain_realm]
               .example.com=EXAMPLE.COM
               example.com=EXAMPLE.COM

Copy

✔ Copied

##### Step 3

Create a Kerberos ticket for user _zabbix_. Run the following command as user _zabbix_ :
    
    
    kinit zabbix

Copy

✔ Copied

It is important to run the above command as user _zabbix_. If you run it as _root_ the authentication will not work.

##### Step 4

Create a web scenario or HTTP agent item with Kerberos authentication type.

Optionally can be tested with the following curl command:
    
    
    curl -v --negotiate -u : http://example.com

Copy

✔ Copied

Note that for lengthy web monitoring it is necessary to take care of renewing the Kerberos ticket. Default time of ticket expiration is 10h.