---
title: image.delete
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/image/delete
downloaded: 2025-11-14 10:42:41
---

# image.delete

### Description

`object image.delete(array imageIds)`

This method allows to delete images.

This method is only available to _Super admin_ user type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(array)` IDs of the images to delete.

### Return values

`(object)` Returns an object containing the IDs of the deleted images under the `imageids` property.

### Examples

#### Delete multiple images

Delete two images.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "image.delete",
               "params": [
                   "188",
                   "192"
               ],
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "imageids": [
                       "188",
                       "192"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CImage::delete() in _ui/include/classes/api/services/CImage.php_.