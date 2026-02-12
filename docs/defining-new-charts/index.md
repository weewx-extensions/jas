---
title: Defining New Charts
nav_order: 5
---

WeeWX uses [Apache ECharts](https://echarts.apache.org/en/index.html) to generate the charts.
A very complete set of [reference documentation](https://echarts.apache.org/handbook/en/get-started) exists.
WeeWX-JAS also contains some basic charts.
To see the  predefined charts, browse the `[[chart_definitions]]` section of
[skin.conf](https://github.com/bellrichm/weewx-jas/blob/master/skins/jas/skin.conf).
Each section under `[[[chart_definitions]]` is a separate chart.

With the exception of `series` and `weewx`, options map directly to [EChart configuration options](https://echarts.apache.org/en/option.html).
Specifically, objects `{}` in the EChart configuration map to sections `[]` in the weewx.conf.
So if you wanted to configure the title for the chart, the EChart configuration would look like this.

```
var option = {
  title: {
    left: 'center',
    text: 'Inside Temperature',
  }}
  ```

  And the weewx.conf would look like this.

  ```
  [[[[chart_definitions]]]]
      [[[[[inTempChart]]]]]
          [[[[[[title]]]]]]
              left = "'center'"
              text = "'Inside Temperature'"
```


## `[[[[chart_definitions]]]]`
{: .no_toc}

This section is used to define the additional charts.

- Table of Contents
{:toc}

### `[[[[[chart-name]]]]]`

Each  additional `chart` gets it is own section.
The section is the name of the chart.
The additional charts can then be included on any [page](https://weewx-extensions.github.io/jas/pages).

#### _EChart Options_

Any valid [EChart option and sub-option(s)](https://echarts.apache.org/en/option.html#yAxis).

#### `[[[[[[weewx]]]]]]`

The `weewx` section is for options that are used by WeeWX-JAS.

##### data_binding =

Sets the WeeWX data_binding for this chart.

##### title =

Sets the title for this chart.
If not set, the variable `’chart-name’_title` in the `lang` files can be used to set the title.

##### `[[[[[[[yAxis]]]]]]]`

Used to specify optons specific to the y-axis.

Any valid [yAxis option and sub-option(s)](https://echarts.apache.org/en/option.html#yAxis).

#### `[[[[[[series]]]]]]`

The `[[[[[[series]]]]]]` option can have `N` subsections.
Each subsection is a WeeWX observation to be plotted.
WeeWX-JAS will create the `name` and `data` options for each series.

#### `[[[[[[[observation-name]]]]]]]`

##### _EChart Options_ =

Any valid [series option and sub-option(s)](https://echarts.apache.org/en/option.html#series).

##### `[[[[[[[[weewx]]]]]]]]`

The `weewx` section is for options that are used by WeeWX-JAS.

##### data_binding =

Sets the WeeWX data_binding for this observation .

##### aggregate_type =

Sets the WeeWX aggregate_type for this observation.

##### unit =

Sets the WeeWX unit for this observation.

Putting it all together, the WeeWX configuration would look like this.

```
[StdReport]
    [[jas]]
        [[[Extras]]]
            [[[[chart_definitions]]]]
                [[[[[outHumidity]]]]]
                    [[[[[[title]]]]]]
                        left = "'center'"
                        text = "'Outside Humidity'"
                [[[[[[weewx]]]]]]
                    data_binding = wx_view 
                [[[[[[series]]]]]]
                    [[[[[[[dewpoint]]]]]]]
                        yAxisIndex = 0
                        type = "'line'"
                        smooth = true
                        symbol = "'none'"                    
                        [[[[[[[[label]]]]]]]]
                            show = true
                            fontSize = 20
                        [[[[[[[[weewx]]]]]]]]
                            data_binding = data_binding02    
                    [[[[[[[outHumidity]]]]]]]
                        yAxisIndex = 1
                        type = "'scatter'"
                        symbolSize = 5
                        [[[[[[[[label]]]]]]]]
                            show = true
                            fontSize = 20
```

Or using WeeWX-JAS defaults, a simple line chart of `inTemp` and `outTemp` would like lthis.

```
[StdReport]
    [[jas]]
        [[[Extras]]]
            [[[chart_definitions]]]]
                [[[[[TempChart]]]]]
                    [[[[[[series]]]]]]
                        [[[[[[[inTemp]]]]]]]
                        [[[[[[[outTemp]]]]]]]

```
