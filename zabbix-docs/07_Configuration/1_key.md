---
title: Item key format
source: https://www.zabbix.com/documentation/current/en/manual/config/items/item/key
downloaded: 2025-11-14 10:34:42
---

# 1 Item key format

Item key format, including key parameters, must follow syntax rules. The following illustrations depict the supported syntax. Allowed elements and characters at each point can be determined by following the arrows - if some block can be reached through the line, it is allowed, if not - it is not allowed.

![](/documentation/current/assets/en/manual/config/item_key_2.png)

To construct a valid item key, one starts with specifying the key name, then there's a choice to either have parameters or not - as depicted by the two lines that could be followed.

#### Key name

The key name itself has a limited range of allowed characters, which just follow each other. Allowed characters are:
    
    
    0-9a-zA-Z_-.

Copy

✔ Copied

Which means:

  * all numbers;
  * all lowercase letters;
  * all uppercase letters;
  * underscore;
  * dash;
  * dot.

![](/documentation/current/assets/en/manual/config/key_name.png)

#### Key parameters

An item key can have multiple parameters that are comma separated.

![](/documentation/current/assets/en/manual/config/key_parameters.png)

Each key parameter can be either a quoted string, an unquoted string or an array.

![](/documentation/current/assets/en/manual/config/item_parameter.png)

The parameter can also be left empty, thus using the default value. In that case, the appropriate number of commas must be added if any further parameters are specified. For example, item key **icmpping[,,200,,500]** would specify that the interval between individual pings is 200 milliseconds, timeout - 500 milliseconds, and all other parameters are left at their defaults.

It is possible to include macros in the parameters. Those can be [user macros](/documentation/current/en/manual/appendix/macros/supported_by_location_user#items-item-prototypes) or some of the built-in macros. To see what particular built-in macros are supported in item key parameters, search the page [Supported macros](/documentation/current/en/manual/appendix/macros/supported_by_location) for "item key parameters".

#### Parameter - quoted string

If the key parameter is a quoted string, any Unicode character is allowed. If the key parameter string contains a quotation mark, this parameter has to be quoted, and each quotation mark which is a part of the parameter string has to be escaped with a backslash (`\`) character. If the key parameter string contains comma, this parameter has to be quoted.

![](/documentation/current/assets/en/manual/config/key_param_quoted_string.png)

To quote item key parameters, use double quotes only. Single quotes are not supported.

Multi-level parameter arrays, e.g. `[a,[b,[c,d]],e]`, are not allowed.

#### Parameter - unquoted string

If the key parameter is an unquoted string, any Unicode character is allowed except comma and right square bracket (]). Unquoted parameter cannot start with left square bracket ([).

![](/documentation/current/assets/en/manual/config/key_param_unquoted_string.png)

#### Parameter - array

If the key parameter is an array, it is again enclosed in square brackets, where individual parameters come in line with the rules and syntax of specifying multiple parameters.

![](/documentation/current/assets/en/manual/config/key_param_array.png)