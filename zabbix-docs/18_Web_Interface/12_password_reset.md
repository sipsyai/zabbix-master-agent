---
title: Resetting password
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/password_reset
downloaded: 2025-11-14 10:39:44
---

# 12 Resetting password

### Overview

This section describes the steps for resetting user passwords in Zabbix.

### Steps

Turn to your Zabbix administrator if you have forgotten your Zabbix password and cannot log in.

A Super administrator user can change passwords for all users in the user [configuration form](/documentation/current/en/manual/config/users_and_usergroups/user#general-attributes).

If a Super administrator has forgotten their password and cannot log in, the following SQL query must be run to apply the default password to the Super admin user (replace 'Admin' with the appropriate Super admin username):
    
    
    UPDATE users SET passwd = '$2a$10$ZXIvHAEP2ZM.dLXTm6uPHOMVlARXX7cqjbhM6Fn0cANzkCQBWpMrS' WHERE username = 'Admin';

Copy

✔ Copied

After running this query, the user password will be set to _zabbix_. Make sure to change the default password on the first login.