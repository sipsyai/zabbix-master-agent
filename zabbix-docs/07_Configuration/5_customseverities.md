---
title: Customizing trigger severities
source: https://www.zabbix.com/documentation/current/en/manual/config/triggers/customseverities
downloaded: 2025-11-14 10:35:36
---

# 5 Customizing trigger severities

Trigger severity names and colors for severity related GUI elements can be configured in _Administration → General → Trigger displaying options_. Colors are shared among all GUI themes.

#### Translating customized severity names

If Zabbix frontend translations are used, custom severity names will override translated names by default.

Default trigger severity names are available for translation in all locales. If a severity name is changed, a custom name is used in all locales and additional manual translation is needed.

Custom severity name translation procedure:

  * set required custom severity name, for example, 'Important'
  * edit <frontend_dir>/locale/<required_locale>/LC_MESSAGES/frontend.po
  * add 2 lines:

    
    
    msgid "Important"
           msgstr "<translation string>"

Copy

✔ Copied

and save file.

  * create .mo files as described in <frontend_dir>/locale/README

Here **msgid** should match the new custom severity name and **msgstr** should be the translation for it in the specific language.

This procedure should be performed after each severity name change.