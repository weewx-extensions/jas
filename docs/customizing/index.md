---
title: Customizing
nav_order: 3
---

A primary goal of WeeWX-JAS is for it to be highly customizable. It has the following structure.

## Pages

[Pages](https://weewx-extensions.github.io/jas/pages) have the following attributes.

- They contain [sections](https://weewx-extensions.github.io/jas/sections) and [charts](https://weewx-extensions.github.io/jas/charts).
- A page contains data for a predefined interval of time, like a day or week.
- The pages to be displayed is fully customizabele.
- The sections and charts that are on a page is fully customizable.

## Sections

[Sections](https://weewx-extensions.github.io/jas/sections) have the following attributes.

- Can either display certain data such as current conditions, minimums/maximums.
- The content, temperature, rain, wind, etc., is very customizable.
- Uses the [page's](https://weewx-extensions.github.io/jas/pages) interval for the minimums/maximums, charts, etc.

## Charts

[Charts](https://weewx-extensions.github.io/jas/charts) have the following attributes.

- Uses [Apache Echarts](https://echarts.apache.org/en/index.html)
- In theory, all Apache Echarts [options](https://echarts.apache.org/en/option.html#title) are supported.
- WeeWX aggregation, average, sum, minimums, maximums, use the [page's](https://weewx-extensions.github.io/jas/pages) interval.
