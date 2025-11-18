---
title: userdirectory.delete
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/userdirectory/delete
downloaded: 2025-11-14 10:45:43
---

# userdirectory.delete

### Description

`object userdirectory.delete(array userDirectoryIds)`

This method allows to delete user directories. User directory cannot be deleted when it is directly used for at least one user group.  
Default LDAP user directory cannot be deleted when `authentication.ldap_configured` is set to 1 or when there are more user directories left.

This method is only available to _Super admin_ user type.

### Parameters

`(array)` IDs of the user directories to delete.

### Return values

`(object)` Returns an object containing the IDs of the deleted user directories under the `userdirectoryids` property.

### Examples

#### Deleting multiple user directories

Delete two user directories.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "userdirectory.delete",
               "params": [
                   "2",
                   "12"
               ],
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "userdirectoryids": [
                       "2",
                       "12"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CUserDirectory::delete() in _ui/include/classes/api/services/CUserDirectory.php_.