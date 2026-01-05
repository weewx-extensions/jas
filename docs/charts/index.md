---
title: Charts
nav_order: 2
---

[Apache ECharts](https://echarts.apache.org/en/index.html) is the charting engine.
 WeeWX-JAS comes with many predefined charts.
A few examples are below.

This chart shows multiple data series in a single chart.
![Outside Temperature](/images/outTemp.png)

Here is a chart with multiple y-axis charting data with lines and a scatter plot.
![Outside Humidity](/images/outHumidity.png)

WeeWX-JAS also has the ability to chart historical data.
This charts visualizes data across years.
![Year to Year](/images/yearToYear.png)

To see the  predefined charts, browse the `[[chart_definitions]]` section of
[skin.conf](https://github.com/bellrichm/weewx-jas/blob/master/skins/jas/skin.conf).
Each section under `[[[chart_definitions]]` is a separate chart.

In addition to the predefined charts, it is ‘easy’ to [define additional charts](https://github.com/bellrichm/weewx-jas/wiki/Defining-New-Charts)

To display a chart it needs to be added to a [page](https://github.com/bellrichm/weewx-jas/wiki/Pages#the-pages-section).

The following chart options ate configured in the `[[[[pages]]][[[[[page-name]]][[[[[[chart-name]]]]]] section.

## chart_modal =

Overrides the [chart_modal](https://github.com/bellrichm/weewx-jas/wiki/Miscellaneous-Options#chart_modal-) for this specific `chart`.

## series_type =

When set to `mqtt` the chart will be updated when a new MQTT message is received.
The setting `mqtt` is mutually exclusive with setting `chart_modal = True`.
**Experimental - maybe removed in the future.**
