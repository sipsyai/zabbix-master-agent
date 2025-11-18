---
title: Additional frontend languages
source: https://www.zabbix.com/documentation/current/en/manual/appendix/install/locales
downloaded: 2025-11-14 10:46:43
---

# 16 Additional frontend languages

#### Overview

In order to use any other language than English in Zabbix web interface, its locale should be installed on the web server. Additionally, the PHP gettext extension is required for the translations to work.

#### Installing locales

To list all installed languages, run:
    
    
    locale -a

Copy

✔ Copied

If some languages that are needed are not listed, open the _/etc/locale.gen_ file and uncomment the required locales. Since Zabbix uses UTF-8 encoding, you need to select locales with UTF-8 charset.

Now run:
    
    
    locale-gen 

Copy

✔ Copied

Restart the web server.

The locales should now be installed. It may be required to reload Zabbix frontend page in browser using Ctrl + F5 for new languages to appear.

#### Installing Zabbix

If installing Zabbix directly from [Zabbix git repository](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse?at=refs%2Fheads%2Frelease%2F7.4), translation files should be generated manually. To generate translation files, run:
    
    
    make gettext
           locale/make_mo.sh

Copy

✔ Copied

This step is not needed when installing Zabbix from packages or source tar.gz files.

#### Selecting a language

There are several ways to select a language in Zabbix web interface:

  * When installing web interface - in the frontend [installation wizard](/documentation/current/en/manual/installation/frontend#welcome-screen). Selected language will be set as system default.
  * After the installation, system default language can be changed in the _Administration→General→GUI_ [menu section](/documentation/current/en/manual/web_interface/frontend_sections/administration/general#gui).
  * Language for a particular user can be changed in the [user profile](/documentation/current/en/manual/web_interface/user_profile#user-profile).

If a locale for a language is not installed on the machine, this language will be greyed out in Zabbix language selector. An orange icon is displayed next to the language selector if at least one locale is missing. Upon pressing on this icon the following message will be displayed: "You are not able to choose some of the languages, because locales for them are not installed on the web server."

![locale_warning.png](/documentation/current/assets/en/manual/appendix/install/locale_warning.png)