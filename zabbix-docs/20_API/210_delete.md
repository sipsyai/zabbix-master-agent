---
title: mediatype.delete
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/mediatype/delete
downloaded: 2025-11-14 10:43:24
---

# mediatype.delete

### Description

`object mediatype.delete(array mediaTypeIds)`

This method allows to delete media types.

This method is only available to _Super admin_ user type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(array)` IDs of the media types to delete.

### Return values

`(object)` Returns an object containing the IDs of the deleted media types under the `mediatypeids` property.

### Examples

#### Deleting multiple media types

Delete two media types.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "mediatype.delete",
               "params": [
                   "3",
                   "5"
               ],
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "mediatypeids": [
                       "3",
                       "5"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CMediaType::delete() in _ui/include/classes/api/services/CMediaType.php_.