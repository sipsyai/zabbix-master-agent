---
title: Distribution-specific notes on setting up Nginx for Zabbix
source: https://www.zabbix.com/documentation/current/en/manual/appendix/install/nginx
downloaded: 2025-11-14 10:46:36
---

# 9 Distribution-specific notes on setting up Nginx for Zabbix

#### RHEL

Nginx is available only in EPEL:
    
    
    dnf -y install epel-release

Copy

✔ Copied

#### SLES 15

In SUSE Linux Enterprise Server 15 you need to configure `php-fpm` (the path to configuration file may vary slightly depending on the service pack):
    
    
    cp /etc/php8/fpm/php-fpm.conf{.default,}
           cp /etc/php8/fpm/php-fpm.d/www.conf{.default,}
           sed -i 's/user = nobody/user = wwwrun/; s/group = nobody/group = www/' /etc/php8/fpm/php-fpm.d/www.conf

Copy

✔ Copied