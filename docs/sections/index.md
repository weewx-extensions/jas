---
title: Sections
nav_order: 13
---

A WeeWX-JAS [page](https://github.com/bellrichm/weewx-jas/wiki/Pages) consists of [charts](https://github.com/bellrichm/weewx-jas/wiki/Charts) and sections.
Sections display information other than charts and can be included on any [page](https://github.com/bellrichm/weewx-jas/wiki/Pages).

## The `[[[[current]]]]` section

### grid_cols

Override the default and page `grid_cols` setting.
For more information see, [grid_cols](https://github.com/bellrichm/weewx-jas/wiki/Miscellaneous-Options#grid_cols-) at the page level.

This section is used to display the current value of WeeWX observations.

### header_max_decimals =

The maximum number of decimals to display for the 'header' observation.
The default is not set.

### observation =

An observation can be displayed more promimently in the current section's 'header' by setting `observation =` to the desired observation.

### The `[[[[[observations]]]]]` section

#### The `[[[[[[observation-name]]]]]]` section

Each section is the name of a WeeWX observation to be displayed.
The order of the `observation-name` sections controls the order are the observations are displayed.

##### display =

Controls if this observation is displayed in the page and/or modal.
Default value is `page, modal` which results in the observation being displayed on the page and modal window.

##### max_decimals =

The maximum number of decimals to display for this observation.
The default is not set.

##### mqtt =

When set to false the observation will not be updated from the MQTT message.
This is useful for observations that are 'summed', like rain and ET.
The default is `True`.

##### type =

The WeeWX `aggregate_type`.
The default is not having it set.

##### unit =

A WeeWX `unit`.
This observation will be converted to this unit.

A configured `current` section would look something like this.

```
[StdReport]
    [[jas]]
        [[[Extras]]]
            [[[[current]]]]
                observation = outTemp
                max_decimals = 2
                [[[[[observations]]]]]
                    [[[[[[rain]]]]]]
                        mqtt = false
                        type = sum
                    [[[[[[heatindex]]]]]]
                        max_decimals = 2
                        unit = degree_C
                    [[[[[[windchill]]]]]]
                    [[[[[[dewpoint]]]]]]
                    [[[[[[outHumidity]]]]]] 
```

## The `[[[[forecast]]]]` section

WeeWX-JAS uses [Aeris](https://www.aerisweather.com) for its forecast information.
The `client_id =` and `client_secret =` must be set.

### enable = True

Enables/Disables the forecast section.

```
[StdReport]
    [[jas]]
        [[[Extras]]]
            client_id = REPLACE_ME
            client_secret = REPLACE_ME
```

## The `[[[[minmax]]]]` section

This section is used to display the min/max value of WeeWX observations.
Each observation to be displayed is a section within the `[[[[minmax]]]][[[[[observations]]]]]` setting.

### data_binding =

The WeeWX data_binding for the `minmax` section.

### The `[[[[[observations]]]]]` section

#### The `[[[[[[observation-name]]]]]]` section

Each section is the name of a WeeWX observation to be displayed.
The order of the `observation-name` sections controls the order are the observations are displayed.

##### data_binding =

The WeeWX data_binding for this observation.

#### max_decimals =

The maximum number of decimals to display for this observation.
The default is not set.

##### unit =

A WeeWX `unit`.
This observation will be converted to this unit.

A configured `minmax` section would look something like this.

```
[StdReport]
    [[jas]]
        [[[Extras]]]
            [[[[minmax]]]]
                data_binding = alternate_binding_one
                [[[[[observations]]]]]
                    [[[[[[outTemp]]]]]]
                        data_binding = alternate_binding_two
                        max_decimals = 2
                        unit = degree_C
                    [[[[[[heatindex]]]]]]
                    [[[[[[windchill]]]]]]
                    [[[[[[dewpoint]]]]]]
                    [[[[[[outHumidity]]]]]]  
```

## The `[[[[radar]]]]` section

No configuration of the `radar` section is required.
It just needs to be included on a [page](https://github.com/bellrichm/weewx-jas/wiki/Pages).

## The `[[[[thisdate]]]]` section

This section is used to display the value of the observation on the current date but in the time period of the page.
For example, if the current date is January 1, 2020 and the page being displayed is the data for the year 1999;
the `thisdate` section will show data for January 1, 1999.
Each observation to be displayed is a section within the `[[[[this]]]][[[[[observations]]]]]` setting.

### data_binding =

The WeeWX data_binding for `thisdate` section.

### The `[[[[[observations]]]]]` section

#### The `[[[[[[observation-name]]]]]]` section

Each section is the name of a WeeWX observation to be displayed.
The order of the `observation-name` sections controls the order are the observations are displayed.

##### data_binding =

The WeeWX data_binding for this observation.

##### type =

The WeeWX `aggregate_type`.
The default is not having it set.

##### unit =

A WeeWX `unit`.
This observation will be converted to this unit.

A configured `thisdate` section would look something like this.

```
[StdReport]
    [[jas]]
        [[[Extras]]]
            [[[[thisdate]]]]
                data_binding = alternate_binding_one
                [[[[[observations]]]]]
                    [[[[[[outTemp]]]]]]
                        data_binding = alternate_binding_two
                        max_decimals = 2
                        unit = degree_C
                    [[[[[[heatindex]]]]]]
                    [[[[[[windchill]]]]]]
                    [[[[[[dewpoint]]]]]]
                    [[[[[[outHumidity]]]]]]  
```
