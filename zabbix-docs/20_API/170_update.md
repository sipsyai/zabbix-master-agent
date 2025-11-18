---
title: image.update
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/image/update
downloaded: 2025-11-14 10:42:43
---

# image.update

### Description

`object image.update(object/array images)`

This method allows to update existing images.

This method is only available to _Super admin_ user type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` Image properties to be updated.

The `imageid` property must be defined for each image, all other properties are optional. Only the passed properties will be updated, all others will remain unchanged.

The method accepts images with the [standard image properties](object#image).

### Return values

`(object)` Returns an object containing the IDs of the updated images under the `imageids` property.

### Examples

#### Rename image

Rename image to "Cloud icon".

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "image.update",
               "params": {
                   "imageid": "2",
                   "name": "Cloud icon"
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "imageids": [
                       "2"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CImage::update() in _ui/include/classes/api/services/CImage.php_.