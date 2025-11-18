---
title: Image object
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/image/object
downloaded: 2025-11-14 10:42:39
---

# Image object

The following objects are directly related to the `image` API.

### Image

The image object has the following properties.

imageid | ID | ID of the image.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
\- _required_ for update operations  
---|---|---  
name | string | Name of the image.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
imagetype | integer | Type of image.  
  
Possible values:  
1 - _(default)_ icon;  
2 - background image.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _constant_  
\- _required_ for create operations  
image | string | Base64 encoded image.  
The maximum size of the encoded image is 1 MB. Maximum size can be adjusted by changing `ZBX_MAX_IMAGE_SIZE` constant value.  
Supported image formats: PNG, JPEG, GIF.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations