---
title: Creating your own theme
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/theming
downloaded: 2025-11-14 10:39:40
---

# 8 Creating your own theme

#### Overview

By default, Zabbix provides a number of predefined themes. You may follow the step-by-step procedure provided here in order to create your own. Feel free to share the result of your work with Zabbix community if you created something nice.

##### Step 1

To define your own theme you'll need to create a CSS file and save it in the `assets/styles/` folder (for example, _custom-theme.css_). You can either copy the files from a different theme and create your theme based on it or start from scratch.

##### Step 2

Add your theme to the list of themes returned by the APP::getThemes() method. You can do this by overriding the ZBase::getThemes() method in the APP class. This can be done by adding the following code before the closing brace in _include/classes/core/APP.php_ :
    
    
      public static function getThemes() {
                 return array_merge(parent::getThemes(), [
                     'custom-theme' => _('Custom theme')
                 ]);
             }

Copy

✔ Copied

Note that the name you specify within the first pair of quotes must match the name of the theme file without extension.

To add multiple themes, just list them under the first theme, for example:
    
    
      public static function getThemes() {
                 return array_merge(parent::getThemes(), [
                     'custom-theme' => _('Custom theme'),
                     'anothertheme' => _('Another theme'),
                     'onemoretheme' => _('One more theme')
                 ]);
             }

Copy

✔ Copied

Note that every theme except the last one must have a trailing comma.

To change graph colors, the entry must be added in the _graph_theme_ database table.

##### Step 3

Activate the new theme.

In Zabbix frontend, you may either set this theme to be the default one or change your theme in the user profile.

Enjoy the new look and feel!