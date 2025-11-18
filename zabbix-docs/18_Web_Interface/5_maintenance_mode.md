---
title: Frontend maintenance mode
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/maintenance_mode
downloaded: 2025-11-14 10:39:37
---

# 5 Frontend maintenance mode

#### Overview

It is possible to temporarily disable Zabbix frontend to restrict access. This is useful for protecting Zabbix database from user-initiated changes, preserving its integrity.

While Zabbix frontend is in maintenance mode, you can safely stop the database and perform maintenance tasks.

Users from defined IP addresses will be able to interact with the frontend normally during maintenance mode.

#### Configuration

To enable maintenance mode, open the `maintenance.inc.php` file (located in `/conf` of the Zabbix HTML document directory on the web server) and uncomment the following lines:
    
    
    // Maintenance mode.
           define('ZBX_DENY_GUI_ACCESS', 1);
           
           // Array of IP addresses, which are allowed to connect to frontend (optional).
           $ZBX_GUI_ACCESS_IP_RANGE = array('127.0.0.1');
           
           // Message shown on warning screen (optional).
           $ZBX_GUI_ACCESS_MESSAGE = 'We are upgrading MySQL database till 15:00. Stay tuned...';

Copy

✔ Copied

In most cases, the `maintenance.inc.php` file is located in `/conf` of the Zabbix HTML document directory on the web server. However, some operating systems and web servers may use a different location.

For example, the location for:

  * SUSE and RedHat is `/etc/zabbix/web/maintenance.inc.php`.
  * Debian-based systems is `/usr/share/zabbix/conf/`.

See also [Copying PHP files](/documentation/current/en/manual/installation/install#copying-php-files).

**ZBX_DENY_GUI_ACCESS** | If defined with any value, maintenance mode will be enabled.   
To disable maintenance mode, comment out or delete.  
---|---  
**ZBX_GUI_ACCESS_IP_RANGE** | Array of IP addresses, which are allowed to connect to the frontend (optional).  
For example:  
`array('192.168.1.1', '192.168.1.2')`  
**ZBX_GUI_ACCESS_MESSAGE** | A message to inform users about the maintenance (optional).   
If undefined, the default message _'Zabbix is under maintenance'_ will be used.  
  
#### Display

Users will see the following screen when trying to access Zabbix frontend while in maintenance mode. The screen is refreshed every 30 seconds in order to return to a normal state without user intervention when the maintenance is over.

![](/documentation/current/assets/en/manual/web_interface/frontend_maintenance.png)

IP addresses defined in _ZBX_GUI_ACCESS_IP_RANGE_ will be able to access the frontend as usual.