---
title: Debugging
nav_order: 4
---

There are two places that WeeWX-JAS may encounter problems, generating the web content and running the web content.

## Debugging content generation

This requires the 'traditional' information, the weewx.conf and a good log file to debug.
See [Help! Posting to WeeWX user group](https://github.com/weewx/weewx/wiki/Help!-Posting-to-weewx-user) for information on capturing the log.

## Debugging display issues

The easiest way is to provide the url to WeeWX-JAS. The next easiest way is to provide the web content. This is easily done by following these steps

1. Navigate to the 'page' that has the problem.
2. Right click on the page and select, "Save as"

Note: It does matter what content of page is clicked on. Usually a blank portion of the navbar works.
![Save as](/images/saveStart.png)

3. Ensure that "Webpage, complete" is selected.
![Save as](/images/saveType.png)
4. A file and and a directory of files will be downloaded. For convenience, zip these into a single file.
![Save as](/images/saveFiles.png)

Once the necessary information is gathered,
[open an issue](https://github.com/weewx-extensions/jas/issues/new),
[start a discussion in github](https://github.com/weewx-extensions/jas/discussions/new),
or [post on WeeWX google group](https://groups.google.com/g/weewx-user).
