---
title: Customizing
nav_order: 3
---

A primary goal of WeeWX-JAS is for it to be highly customizable. It has the following structure.

## Pages

[Pages](https://github.com/bellrichm/WeeWX-jas/wiki/Pages) have the following attributes.

- They contain [sections](https://github.com/bellrichm/WeeWX-jas/wiki/Sections) and [charts](https://github.com/bellrichm/WeeWX-jas/wiki/Charts).
- A page contains data for a predefined interval of time, like a day or week.
- The pages to be displayed is fully customizabele.
- The sections and charts that are on a page is fully customizable.

## Sections

[Sections](https://github.com/bellrichm/WeeWX-jas/wiki/Sections) have the following attributes.

- Can either display certain data such as current conditions, minimums/maximums.
- The content, temperature, rain, wind, etc., is very customizable.
- Uses the [page's](https://github.com/bellrichm/WeeWX-jas/wiki/Pages) interval for the minimums/maximums, charts, etc.

## Charts

[Charts](https://github.com/bellrichm/WeeWX-jas/wiki/Charts) have the following attributes.

- Uses [Apache Echarts](https://echarts.apache.org/en/index.html)
- In theory, all Apache Echarts [options](https://echarts.apache.org/en/option.html#title) are supported.
- WeeWX aggregation, average, sum, minimums, maximums, use the [page's](https://github.com/bellrichm/WeeWX-jas/wiki/Pages) interval.
