---
title: regexp.update
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/regexp/update
downloaded: 2025-11-14 10:43:58
---

# regexp.update

### Description

`object regexp.update(object/array regularExpressions)`

This method allows to update existing global regular expressions.

This method is only available to _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` Regular expression properties to be updated.

The `regexpid` property must be defined for each object, all other properties are optional. Only the passed properties will be updated, all others will remain unchanged.

Additionally to the [standard properties](object#expressions), the method accepts the following parameters.

expressions | array | [Expressions](/documentation/current/en/manual/api/reference/regexp/object#expressions) options.  
---|---|---  
  
### Return values

`(object)` Returns an object containing the IDs of the updated regular expressions under the `regexpids` property.

### Examples

#### Updating global regular expression for file systems discovery.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "regexp.update",
               "params": {
                 "regexpid": "1",
                 "name": "File systems for discovery",
                 "test_string": "",
                 "expressions": [
                   {
                     "expression": "^(btrfs|ext2|ext3|ext4|reiser|xfs|ffs|ufs|jfs|jfs2|vxfs|hfs|apfs|refs|zfs)$",
                     "expression_type": "3",
                     "exp_delimiter": ",",
                     "case_sensitive": "0"
                   },
                   {
                     "expression": "^(ntfs|fat32|fat16)$",
                     "expression_type": "3",
                     "exp_delimiter": ",",
                     "case_sensitive": "0"
                   }
                 ]
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "regexpids": [
                       "1"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CRegexp::update() in _ui/include/classes/api/services/CRegexp.php_.