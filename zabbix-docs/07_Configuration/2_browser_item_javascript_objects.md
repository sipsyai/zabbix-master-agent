---
title: Browser item JavaScript objects
source: https://www.zabbix.com/documentation/current/en/manual/config/items/preprocessing/javascript/browser_item_javascript_objects
downloaded: 2025-11-14 10:34:52
---

# 2 Browser item JavaScript objects

#### Overview

This section describes Zabbix additions to the JavaScript language implemented with Duktape for use in the [Browser item](/documentation/current/en/manual/config/items/itemtypes/browser) script. These additions supplement the JavaScript objects described on the [Additional JavaScript objects](/documentation/current/en/manual/config/items/preprocessing/javascript/javascript_objects) page.

#### Browser

The `Browser` object manages WebDriver sessions, initializing a session upon creation and terminating it upon destruction. A single script can support up to four `Browser` objects.

To construct a `Browser` object, use the `new Browser(options)` syntax. The `options` (_JSON object_) parameter specifies browser options, usually the WebDriver options method result (for example, `Browser.chromeOptions()`).

The following methods are supported with the `Browser` object.

`navigate(url)` | Navigate to the specified URL.  
  
Parameters:  
`url` \- (string) URL to navigate to.  
---|---  
`getUrl()` | Return a string of the opened page URL.  
`getPageSource()` | Return a string of the opened page source.  
`findElement(strategy, selector)` | Return an `Element` object with one element in the opened page (or return `null` if no elements match `strategy` and `selector`).  
  
Parameters:  
`strategy` \- (string, CSS selector/link text/partial link text/tag name/Xpath) [Location strategy](https://www.selenium.dev/documentation/webdriver/elements/locators/);  
`selector` \- (string) Element selector using the specified location strategy.  
`findElements(strategy, target)` | Return an array of `Element` objects with multiple elements in the opened page (or return an empty array if no elements match location strategy and target).  
  
Parameters:  
`strategy` \- (string, CSS selector/link text/partial link text/tag name/Xpath) [Location strategy](https://www.selenium.dev/documentation/webdriver/elements/locators/);  
`target` \- (string) Element selector using the specified location strategy.  
`getCookies()` | Return an array of `Cookie` objects.  
`addCookie(cookie)` | Set cookies.  
  
Parameters:  
`cookie` \- (`Cookie` object) Cookie to set.  
`getScreenshot()` | Return a base64 encoded string representing an image of the browser's viewport.  
`setScreenSize(x,y)` | Set the browser's viewport size.  
  
Parameters:  
`x` \- (string) Height in pixels;  
`y` \- (string) Width in pixels.  
`setScriptTimeout(timeout)` | Set script loading timeout.  
  
Parameters:  
`timeout` \- (integer) Timeout value in milliseconds.  
`setSessionTimeout(timeout)` | Set session (page load) timeout.  
  
Parameters:  
`timeout` \- (integer) Timeout value in milliseconds.  
`setElementWaitTimeout(timeout)` | Set element location strategy (implicit) timeout.  
  
Parameters:  
`timeout` \- (integer) Timeout value in milliseconds.  
`collectPerfEntries(mark)` | Collect performance entries to retrieve with the `getResult()` method.  
  
Parameters:  
`mark` \- (string, optional) performance snapshot mark.  
`getRawPerfEntries()` | Return an array of performance entry objects.  
`getResult()` | Return a `Result` object with browser session statistics (error information, performance snapshots, etc.).  
`getError()` | Return a `BrowserError` object with browser errors (or return `null` if there are no browser errors).  
`setError(message)` | Set a custom error message to be included in the `Result` object.  
  
Parameters:  
`message` \- (string) Error message.  
`discardError()` | Discard the error to be returned in the `Result` object.  
`getAlert()` | Return an `Alert` object with browser alerts (or return `null` if there are no browser alerts).  
`chromeOptions()` | Return a `chromeOptions` object with predefined Chrome browser options.  
`firefoxOptions()` | Return a `firefoxOptions` object with predefined Firefox browser options.  
`safariOptions()` | Return a `safariOptions` object with predefined Safari browser options.  
`edgeOptions()` | Return an `edgeOptions` object with predefined Edge browser options.  
`switchFrame(target)` | Switch to the specified frame.   
  
Parameters:  
`target` \- (browser element or integer, optional) Target frame. To select a frame by element, pass the element. To select a frame by index, pass the number. If left empty, will switch to the top-level browsing context.  
  
All Browser methods can throw the following errors:

  * `BrowserError` \- derived from the `Error` object that is thrown if the `Browser` constructor fails; contains an additional `browser` property with a `Browser` object that threw this `BrowserError`.
  * `WebdriverError` \- derived from `BrowserError`; contains the same properties as the `BrowserError` object, which indicate if the error was generated in response to an error in the WebDriver response.

#### Element

The `Element` object is returned by the `Browser` object `findElement()`/`findElements()` methods and cannot be constructed directly.

The `Element` object represents an element in the web page and provides methods to interact with it.

The following methods are supported with the `Element` object.

`getAttribute(name)` | Return an attribute value string of the element attribute (or return `null` if the specified attribute was not found).  
  
Parameters:  
`name` \- (string) Attribute name.  
---|---  
`getProperty(name)` | Return a property value string of the element property (or return `null` if the specified property was not found).  
  
Parameters:  
`name` \- (string) Property name.  
`getText()` | Return a text value string of the element text.  
`click()` | Click on an element.  
`clear()` | Clear the content of an editable element.  
`sendKeys(keys)` | Send keys.  
  
Parameters:  
`keys` \- (string) Keys to send.  
  
#### Cookie

The `Cookie` object is returned by the `Browser` object `getCookies()` method and passed to the `addCookie()` method.

While the `Cookie` object does not have any methods, it can contain the following properties:

name | string | Name of the cookie.  
---|---|---  
value | string | Value of the cookie.  
path | string | Path for which the cookie is valid.  
Defaults to `"/"` if omitted when adding a cookie.  
domain | string | Domain to which the cookie is visible.  
Defaults to the URL domain of the session's current browsing context's active document if omitted when adding a cookie.  
secure | boolean | Indicates whether the cookie is secure.  
Defaults to `false` if omitted when adding a cookie.  
httpOnly | boolean | Indicates whether the cookie is HTTP-only.  
Defaults to `false` if omitted when adding a cookie.  
expiry | integer | Expiration time of the cookie (in seconds since the Unix Epoch). Must not be set if omitted when adding a cookie.  
sameSite | string | The `sameSite` attribute of the cookie, which controls whether the cookie should be restricted to a first-party or same-site context.  
Can be set to either `"Lax"` or `"Strict"`.  
Defaults to `"None"` if omitted when adding a cookie.  
  
#### Alert

The `Alert` object represents a web page alert, is returned by `Browser` object `getAlert()` method, and cannot be constructed directly.

The `Alert` object contains the `text` property with the alert text (or `null` if there are no alerts).

The following methods are supported with the `Alert` object.

`accept()` | Accept the alert.  
---|---  
`dismiss()` | Dismiss the alert.  
  
#### Result

The `Result` object contains session statistics and is returned by the `Browser` object `getResult()` method.

Typically, the `Result` object is stringified and returned from the script, and then parsed into dependent item values through preprocessing.

While the `Result` object does not have any methods, it can contain the following properties.

duration | string | Session duration from session creation to result retrieval.  
---|---|---  
error | object | Error information.  
| http_status | integer | HTTP status returned by the WebDriver (or 0 if there are no WebDriver errors).  
error_code | string | Error returned by the WebDriver (or empty string if there are no WebDriver errors).  
message | string | WebDriver error message (or empty string if there are no WebDriver errors).  
performance_data | object | Performance statistics.  
| summary | object | Performance summary.  
| navigation | object | Navigation summary.  
resource | object | Resource summary.  
| details | array of objects | Performance statistics after each operation that could have resulted in navigation.  
| mark | string | _(optional)_ Performance snapshot mark specified with the `collectPerfEntries()` method.  
navigation | object | Navigation statistics.  
resource | object | Resource summary for this step.  
user | array of objects | Array of mark/measure type statistics.  
| marks | array of objects | Marked performance snapshot indexes.  
| name | string | Performance snapshot mark name.  
index | integer | Performance snapshot index in details array.