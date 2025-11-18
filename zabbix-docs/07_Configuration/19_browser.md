---
title: Browser items
source: https://www.zabbix.com/documentation/current/en/manual/config/items/itemtypes/browser
downloaded: 2025-11-14 10:35:20
---

# 19 Browser items

#### Overview

Browser items allow monitoring complex websites and web applications using a browser.

The support of Browser items is currently experimental.

Browser items collect data by executing a user-defined JavaScript code and retrieving data over HTTP/HTTPS. This item can simulate such browser-related actions as clicking, entering text, navigating through web pages, and other user interactions with websites or web applications.

In addition to the script, an optional list of parameters (pairs of name and value) and timeout can be specified.

The item partially implements the [W3C WebDriver standard](https://www.w3.org/TR/webdriver2/) with either Selenium Server or a plain WebDriver (for example, ChromeDriver) as a web testing endpoint. For the item to work, set the endpoint in the Zabbix [server](/documentation/current/en/manual/appendix/config/zabbix_server#webdriverurl)/[proxy](/documentation/current/en/manual/appendix/config/zabbix_proxy#webdriverurl) configuration file `WebDriverURL` parameter (if using ChromeDriver, see [Security Considerations](https://developer.chrome.com/docs/chromedriver/security-considerations)). For better performance, consider using a dedicated server for the web testing environment.

Browser item checks are executed and processed by Zabbix server or proxy browser pollers. If necessary, you can adjust the number of pre-forked instances of browser pollers in the Zabbix [server](/documentation/current/en/manual/appendix/config/zabbix_server#startbrowserpollers)/[proxy](/documentation/current/en/manual/appendix/config/zabbix_proxy#startbrowserpollers) configuration file `StartBrowserPollers` parameter.

For monitoring complex websites and web applications, the [Website by Browser](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/app/website_browser?at=refs%2Fheads%2Frelease%2F7.4) template is available as an [out-of-the-box template](/documentation/current/en/manual/config/templates_out_of_the_box).

#### Configuration

In the _Type_ field of [item configuration form](/documentation/current/en/manual/config/items/item), select Browser and then fill out the required fields.

![](/documentation/current/assets/en/manual/config/items/itemtypes/browser_item.png)

All mandatory input fields are marked with a red asterisk.

The fields that require specific information for Browser items are:

_Key_ | Enter a unique key that will be used to identify the item.  
---|---  
_Parameters_ | Specify the variables to be passed to the script as the attribute and value pairs.  
[User macros](/documentation/current/en/manual/config/macros/user_macros) are supported. To see which built-in macros are supported, do a search for "Browser-type item" in the [supported macro](/documentation/current/en/manual/appendix/macros/supported_by_location) table.  
_Script_ | Enter JavaScript code in the modal editor that opens when clicking in the parameter field or on the pencil icon next to it. This code must provide the logic for returning the metric value.  
The code has access to all parameters, all [additional JavaScript objects](/documentation/current/en/manual/config/items/preprocessing/javascript/javascript_objects) and [Browser item JavaScript objects](/documentation/current/en/manual/config/items/preprocessing/javascript/browser_item_javascript_objects) added by Zabbix.  
See also: [JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide).  
_Timeout_ | JavaScript execution timeout (1-600s; exceeding it will return an error).  
Note that depending on the script, it might take longer for the timeout to trigger.  
For more information on the _Timeout_ parameter, see [general item attributes](/documentation/current/en/manual/config/items/item#configuration).  
  
#### Examples

For an example of how to set up Zabbix for monitoring websites using the _Website by Browser_ template, see [Monitor websites with Browser items](/documentation/current/en/manual/guides/monitor_browser).

##### Default script

The following script:

  1. Initializes a browser session.
  2. Navigates to a specified URL.
  3. Collects performance entries and session statistics, and returns them as a JSON string.

In the _Script_ field, enter:
    
    
    var browser = new Browser(Browser.chromeOptions());
           
           try {
               browser.navigate("http://example.com");
               browser.collectPerfEntries();
           }
           finally {
               return JSON.stringify(browser.getResult());
           }

Copy

✔ Copied

##### Initialize browser with custom capabilities

The following script:

  1. Initializes a browser session for the available browser based on the first matching browser in the order specified within the script.
  2. Defines browser capabilities, including page load strategy and options specific to each browser, such as the headless mode for Chrome, Firefox, and Microsoft Edge browsers.

In the _Script_ field, enter:
    
    
    var browser = new Browser({
               "capabilities":{
                   "firstMatch":[
                       {
                           "browserName":"chrome",
                           "pageLoadStrategy":"normal",
                           "goog:chromeOptions":{
                               "args":[
                                   "--headless=new"
                               ]
                           }
                       },
                       {
                           "browserName":"firefox",
                           "pageLoadStrategy":"normal",
                           "moz:firefoxOptions":{
                               "args":[
                                   "--headless"
                               ]
                           }
                       },
                       {
                           "browserName":"MicrosoftEdge",
                           "pageLoadStrategy":"normal",
                           "ms:edgeOptions":{
                               "args":[
                                   "--headless=new"
                               ]
                           }
                       },
                       {
                           "browserName":"safari",
                           "pageLoadStrategy":"normal"
                       }
                   ]
               }
           });

Copy

✔ Copied

##### Initialize browser with GUI

By default, browser sessions (excluding Safari) are initialized in headless mode, meaning the browser's graphical user interface (GUI) is not displayed.

The following script initializes a browser session with the GUI enabled.

Note that if the WebDriver cannot locate the browser binary, you can specify the path manually.
    
    
    var opts = Browser.chromeOptions();
           opts.capabilities.alwaysMatch['goog:chromeOptions'].args = [];
           
           // To initialize a Firefox session with GUI, uncomment the following lines:
           // var opts = Browser.firefoxOptions();
           // opts.capabilities.alwaysMatch['moz:firefoxOptions'].binary = 'usr/bin/firefox';
           // opts.capabilities.alwaysMatch['moz:firefoxOptions'].args = [];
           
           // To initialize a Microsoft Edge session with GUI, uncomment the following lines:
           // var opts = Browser.edgeOptions();
           // opts.capabilities.alwaysMatch['ms:edgeOptions'].binary = 'usr/bin/microsoft-edge';
           // opts.capabilities.alwaysMatch['ms:edgeOptions'].args = [];
           
           var browser = new Browser(opts);

Copy

✔ Copied

If your tests are running on a remote server or in a container, you can use a Virtual Network Computing (VNC) client to connect to the machine's VNC server. This lets you view and interact with the browser's GUI remotely.

##### Take screenshots

The following script:

  1. Initializes a browser session.
  2. Sets the browser's viewport size to determine the screenshot size (specified as parameters, see below).
  3. Navigates to a URL (specified as a parameter, see below).
  4. Collects session statistics, captures a screenshot, and adds it to the collected statistics.
  5. Handles errors by capturing error messages and a screenshot.
  6. Returns the collected results as a JSON string.

The script also uses parameters from the item configuration form:

  * webURL - http://example.com
  * width - 1920
  * height - 1080

In the _Script_ field, enter:
    
    
    var browser, result;
           
           var browser = new Browser(Browser.chromeOptions());
           
           try {
               var params = JSON.parse(value); // Parse the JSON string containing parameters passed from Zabbix.
           
               browser.setScreenSize(Number(params.width), Number(params.height))
           
               browser.navigate(params.webURL);
           
               result = browser.getResult();
               result.screenshot = browser.getScreenshot();
           }
           catch (err) {
               if (!(err instanceof BrowserError)) {
                   browser.setError(err.message);
               }
               result = browser.getResult();
               result.error.screenshot = browser.getScreenshot();
           }
           finally {
               return JSON.stringify(result);
           }

Copy

✔ Copied

##### Check Zabbix login

The following script:

  1. Initializes a browser session.
  2. Navigates to a page (specified as a parameter, see below).
  3. Enters the username and password (specified as parameters, see below).
  4. Finds and clicks the login button.
  5. Finds and clicks the logout button.
  6. Collects performance data before and after login, as well as after logout.
  7. Handles errors by capturing error messages and a screenshot.
  8. Returns the collected results as a JSON string.

The script also uses parameters from the item configuration form:

  * webURL - http://{HOST.CONN}/index.php
  * username - {$USERNAME}
  * password - {$PASSWORD}

In the _Script_ field, enter:
    
    
    var browser, result;
           
           browser = new Browser(Browser.chromeOptions());
           
           try {
               var params = JSON.parse(value); // Parse the JSON string containing parameters passed from Zabbix.
           
               browser.navigate(params.webURL);
               browser.collectPerfEntries("open page");
           
               var el = browser.findElement("xpath", "//input[@id='name']");
               if (el === null) {
                   throw Error("cannot find name input field");
               }
               el.sendKeys(params.username);
           
               el = browser.findElement("xpath", "//input[@id='password']");
               if (el === null) {
                   throw Error("cannot find password input field");
               }
               el.sendKeys(params.password);
           
               el = browser.findElement("xpath", "//button[@id='enter']");
               if (el === null) {
                   throw Error("cannot find login button");
               }
               el.click();
           
               browser.collectPerfEntries("login");
           
               el = browser.findElement("link text", "Sign out");
               if (el === null) {
                   throw Error("cannot find logout button");
               }
               el.click();
           
               browser.collectPerfEntries("logout");
           
               result = browser.getResult();
           }
           catch (err) {
               if (!(err instanceof BrowserError)) {
                   browser.setError(err.message);
               }
               result = browser.getResult();
               result.error.screenshot = browser.getScreenshot();
           }
           finally {
               return JSON.stringify(result);
           }

Copy

✔ Copied

##### Find links

The following script:

  1. Initializes a browser session.
  2. Defines a function for removing duplicate elements from an array (see step 5).
  3. Navigates to a page (specified as parameters, see below).
  4. Finds links on the page.
  5. Removes duplicate links to ensure they are unique.
  6. Extracts only the links that start with "http".
  7. Formats the extracted links to a specific structure.
  8. Handles errors by capturing error messages and a screenshot.
  9. Returns the collected results as a JSON string.

The script also uses parameters from the item configuration form:

  * scheme - {$WEBSITE.SCHEME}
  * domain - {$WEBSITE.DOMAIN}
  * path - {$WEBSITE.PATH}

In the _Script_ field, enter:
    
    
    var browser, result;
           
           browser = new Browser(Browser.chromeOptions());
           
           try {
               var params = JSON.parse(value);  // Parse the JSON string containing parameters passed from Zabbix.
           
               function uniq(a) {
                   return a.sort().filter(function (item, pos, ary) {
                       return !pos || item != ary[pos - 1];
                   });
               }
           
               browser.navigate(params.scheme + '://' + params.domain + params.path);
           
               var el = browser.findElements("link text", "");
               var links = [];
               for (var n = 0; n < el.length; n++) {
                   links.push(el[n].getAttribute('href'));
               }
           
               links = uniq(links);
           
               result = [];
               for (i = 0; i < links.length; i++) {
                   if (links[i].match(/^http.*/)) {
                       var row = {};
                       row["{#URL}"] = links[i];
                       result.push(row);
                   }
               }
           }
           catch (err) {
               if (!(err instanceof BrowserError)) {
                   browser.setError(err.message);
               }
               result = browser.getResult();
               result.error.screenshot = browser.getScreenshot();
           }
           finally {
               return JSON.stringify(result);
           }

Copy

✔ Copied