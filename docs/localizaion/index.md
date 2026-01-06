---
title: Localization
nav_order: 8
---

## Text

Because WeeWX-JAS allows the end user to select the language, it does not leverage WeeWX's translation infrastructure.
As much as possible, WeeWX-JAS does use the same constructs as outline in the [customization guide](https://weewx.com/docs/latest/customizing.htm#localization).
The base internationalization is in the appropriate `lang` files.

Because charts can be added to a WeeWX-JAS installation, additional text might need to be translated. This could be additional titles, labels, etc.
These additional translations could be added to the `lang` files, but then they would be overwritten when the skin is updated.
To get around this, WeeWX-JAS defines a location in weewx.conf to put these translations, `[[[[lang]]]]` in the `[[[Extras]]]` section.

If a new chart named, `memoryUsage` is defined that displays 3 series of data, `mem_size`, `mem_rss`, and `mem_shared`;
the `lang` section for English would look like the following.

```
    [[jas]]
        [[[Extras]]]
            [[[[lang]]]]
                [[[[[en]]]]]
                    [[[[[[Labels]]]]]]
                        [[[[[[[Generic]]]]]]]
                            # The chart displays 3 data series, mem_size, mem_rss, and mem_share
                            mem_size = Memory Size
                            mem_rss = Memory RSS
                            mem_share = Memory Share
                    [[[[[[Texts]]]]]]
                            # The title of the memoryUsage chart
                            memoryUsage_title = Usage
```

## Dates and Times

Formatting of dates and times are also done using javascript.
The [momentjs library](https://momentjs.com/) is used.
Because of this the [format](https://momentjs.com/docs/#/displaying/format/) to designate the layout of dates and times is different.

WeeWX-JAS also allows for the format of dates and times to be dependent on the context it is being displayed in.
For example the date shown as an x-axis label might be different than what is shown in the tooltip.
This results in date and time formats also being defined in the 'lang.conf' file under the `[Texts]` section.
If one wishes to change the format but does not want or need to translate the skin, the weewx.conf can be updated to accomplish this.
It would look something like this.

```
[StdReport]
.
.
.
    [[jas]]
        skin = jas
.
.
.
        [[[Texts]]]
            [[[[aggregate_interval_none]]]]
                tooltip_x              = HH:mm
                xaxis_label            = HH:mm    
                label                  = HH:mm 
```

Or one could put it in the [[[Extras]]][[[[lang]]]] section of weewx.conf as defined above.
