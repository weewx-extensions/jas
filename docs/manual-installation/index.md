---
title: Manual Installation
nav_order: 9
---

Why? Just use [wee_extension](https://github.com/bellrichm/weewx-jas#installation). But if you must, read on.

## Installation notes

Because there are [multiple methods to install WeeWX](http://weewx.com/docs/usersguide.htm#installation_methods), location of files can vary.
See [where to find things](http://weewx.com/docs/usersguide.htm#Where_to_find_things)
in the WeeWX [User's Guide](http://weewx.com/docs/usersguide.htm") for the definitive information.
The following symbolic names are used to define the various locations:

* *$DOWNLOAD_ROOT* - The directory containing the downloaded *WeeWX-JAS* extension.
* *$BIN_ROOT* - The directory where WeeWX executables are located.
* *$SKIN_ROOT* - The directory wehere WeeWX skins are located.
* *$CONFIG_ROOT* - The directory where the configuration (typically, weewx.conf) is located.

The notation vX.Y.Z designates the version being installed.
X.Y.Z is the release.

Prior to making any updates/changes, always make a backup.

## Preqrequisites

|WeeWX version   |Python version                               |
|----------------|---------------------------------------------|
|4.6.0 or greater|Python 3.6 or greater                        |

## Instructions

1. Download WeeWX-JAS

    ```
    wget -P $DOWNLOAD_ROOT https://github.com/bellrichm/weewx-jas/archive/vX.Y.Z.tar.gz
    ```

    All of the releases can be found [here](https://github.com/bellrichm/weewx-jas/releases) and this is the [latest](https://github.com/bellrichm/weewx-jas/releases/latest).

2. Unpack WeeWX-JAS

    ```
    tar xvfz vX.Y.Z.tar.gz
    ```

3. Copy the files

    ```
    cp $DOWNLOAD_ROOT/vX.Y.X/bin/user/jas.py $BIN_ROOT/user
    cp $DOWNLOAD_ROOT/vX.Y.X/skins/* $SKIN_ROOT
    ```

4. Configure

     ```
    [StdReport]
        [[jas]]
            skin = jas
            lang = en
            HTML_ROOT = jas
            [[[Extras]]]
                [[[[chart_definitions]]]]
                    [[[[[outTempChart]]]]]
                        [[[[[[series]]]]]]
                            [[[[[[[outTemp]]]]]]]
                [[[[pages]]]]
                    [[[[[day]]]]]
                        [[[[[[outTemp]]]]]]
    ```

    This will configure WeeWX-JAS to create a line chart of the outTemp observation and display it on the day page.
    For additional information read [Customizing](https://github.com/bellrichm/weewx-jas/wiki/  ).

5. Restart WeeWX

    ```
    sudo /etc/init.d/weewx restart
    ```

    or

    ```
    sudo sudo service restart weewx
    ```

    or

    ```
    sudo systemctl restart weewx
    ```
