---
title: mediatype.update
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/mediatype/update
downloaded: 2025-11-14 10:43:26
---

# mediatype.update

### Description

`object mediatype.update(object/array mediaTypes)`

This method allows to update existing media types.

This method is only available to _Super admin_ user type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` Media type properties to be updated.

The `mediatypeid` property must be defined for each media type, all other properties are optional. Only the passed properties will be updated, all others will remain unchanged.

Additionally to the [standard media type properties](object#media-type), the method accepts the following parameters.

message_templates | array | [Message templates](object#message-template) to replace the current message templates.  
---|---|---  
  
### Return values

`(object)` Returns an object containing the IDs of the updated media types under the `mediatypeids` property.

### Examples

#### Enabling a media type

Enable a media type, that is, set its status to "0".

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "mediatype.update",
               "params": {
                   "mediatypeid": "6",
                   "status": "0"
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "mediatypeids": [
                       "6"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CMediaType::update() in _ui/include/classes/api/services/CMediaType.php_.