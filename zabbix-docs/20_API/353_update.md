---
title: userdirectory.update
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/userdirectory/update
downloaded: 2025-11-14 10:45:46
---

# userdirectory.update

### Description

`object userdirectory.update(object/array userDirectory)`

This method allows to update existing user directories.

This method is only available to _Super admin_ user type.

### Parameters

`(object/array)` [User directory properties](object#user-directory) to be updated.

The `userdirectoryid` property must be defined for each user directory, all other properties are optional. Only the passed properties will be updated, all others will remain unchanged.

### Return values

`(object)` Returns an object containing the IDs of the updated user directories under the `userdirectoryids` property.

### Examples

##### Update bind password for user directory

Set new bind password for a user directory.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "userdirectory.update",
               "params": {
                   "userdirectoryid": "3",
                   "bind_password": "newldappassword"
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "userdirectoryids": [
                       "3"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

##### Update mappings for user directory

Update provisioning groups mappings and media type mappings for user directory "2".

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "userdirectory.update",
               "params": {
                   "userdirectoryid": "2",
                   "provision_media": [
                           {
                               "userdirectory_mediaid": "2"
                           }
                       ],
                       "provision_groups": [
                           {
                               "name": "Zabbix administrators",
                               "roleid": "2",
                               "user_groups": [
                                   {
                                       "usrgrpid": "7"
                                   },
                                   {
                                       "usrgrpid": "8"
                                   },
                                   {
                                       "usrgrpid": "11"
                                   }
                               ]
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
                   "userdirectoryids": [
                       "2"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CUserDirectory::update() in _ui/include/classes/api/services/CUserDirectory.php_.