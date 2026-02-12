---
title: Getting Started
nav_order: 7
---

## Prerequisites

A basic understanding of [WeeWX](https://weewx.com) is required.
When creating new charts, an understanding of [Apache ECharts](https://echarts.apache.org/en/index.html) is necessary.
To change the layout, [Bootstrap](https://getbootstrap.com/) knowledge is required.
If MQTT is being used, some knowledge of [MQTT](https://www.eclipse.org/paho/index.php?page=clients/js/index.php) is required.

## Installation

Follow the [instructions](https://github.com/bellrichm/weewx-jas#installation) to install WeeWX-JAS.

## Customizing

See [Customizing](https://weewx-extensions.github.io/jas/customizing)

## Overview

Like many skins, when displaying data, WeeWX-JAS does not interact directly with the database.
It uses WeeWX utilities to extract the data.
These utilities run at the end of the WeeWX archive period.
Some skins, like Standard and Seasons, create images and html that can be directly displayed.
Others, like WeeWX-JAS, extract the data and use Javascript libraries to create charts.

### WeeWX-JAS Components

WeeWX-JAS is made up of [pages](https://weewx-extensions.github.io/jas/pages).
Each page is made up of four components, data, HTML, chartd, and Javascript code.

#### Data

This is what will be displayed in either [charts](https://weewx-extensions.github.io/jas/charts)
or as [section](https://weewx-extensions.github.io/jas/sections), like a table.
The data component is made up of the following two sub-components.

##### Data Loader

This is the code that loads the WeeWX json formatted data into WeeWX-JAS.
When displaying observations for time periods such as current conditions, this year, today, etc.;
the data that is loaded will change every archive period as more recent observations are gathered.
Assuming no changes to WeeWX-JAS nor any configuration changes, for historical time periods, such as a past month or past year, the data will not change.

##### Data Helper

This is the code manipulates the json formatted data into the format that WeeWX-JAS uses.
For example, it takes the json formatted data of observations for a given time period and finds the minimum value.
Assuming no changes to WeeWX-JAS nor any configuration changes, these will never change.

#### HTML

This is the layout of a given a page in WeeWX-JAS.
Assuming no changes to WeeWX-JAS nor any configuration changes, these will never change.

#### Charts

This is the Javascript that creates the charts from the data.
Assuming no changes to WeeWX-JAS nor any configuration changes, these will never change.

#### Javascript Code

This ‘glues’ the user interface together.
It does such things as formatting date/times, formatting numerical data, displaying text in the correct language, etc.
Assuming no changes to WeeWX-JAS nor any configuration changes, these will never change.

### Generating WeeWX-JAS Components

#### Data Loader

##### Historical Time Period

When WeeWX kicks of the report generation, it checks to see if the data has been generated.
It only generates the data if it is ‘missing’.

The historical data aggregates data by day. For example, the minimum temperature is the minimum for a day.
Historical data is also displayed for the current year and month.
Because 'current' historical data changes on the day boundary, this data is only generated once per day.

current year and month special case

##### Current Time Period

###### day and last24hours

'day' and 'last24hours' time periods have no aggregation and therefore are generated every aggregation period.

###### week and last7days

'week' and 'last7days' time periods are aggregated on the hour and therefore are generated once per hour.

###### month and last31days

'month' and 'last31days' time periods are aggregated on the day and therefore are generated once per day.

###### year and last366days

'year' and 'last366days' time periods are aggregated on the day and therefore are generated once per day.

###### yesterday

'yesterday' has no aggregation but only changes once per day and therefore are generated once per day.

#### Data Helper

##### Historical Time Period

When WeeWX kicks of the report generation, it checks to see if the Javascript  has been generated.
It only generates the Javascript if it is ‘missing’.

##### Current Time Period

The Javascript is generated once, at the end of the first archive period.

#### HTML

##### Historical Time Period

When WeeWX kicks of the report generation, it checks to see if the HTML has been generated.
It only generates the HTML if it is ‘missing’.

##### Current Time Period

The HTML is generated once, at the end of the first archive period.

#### Charts

##### Historical Time Period

When WeeWX kicks of the report generation, it checks to see if the chart has been generated.
It only generates the charts if it is ‘missing’.

##### Current Time Period

The charts are generated once, at the end of the first archive period.

#### Javascript

##### Historical Time Period

When WeeWX kicks of the report generation, it checks to see if the Javascript  has been generated.
It only generates the Javascript if it is ‘missing’.

##### Current Time Period

The Javascript is generated once, at the end of the first archive period.

## Ask for Help

Feel free to [open an issue](https://github.com/bellrichm/weewx-jas/issues/new),
[start a discussion in github](https://github.com/bellrichm/weewx-jas/discussions/new),
or [post on WeeWX google group](https://groups.google.com/g/weewx-user).
Because WeeWX-JAS uses javascript to create the charts, a `weewx.log` is not always useful.
But it never hurts to include one.
When doing so, see [Help! Posting to WeeWX user](https://github.com/weewx/weewx/wiki/Help!-Posting-to-weewx-user)
for information on capturing the log.
Often times seeing what is in the browser console is useful.
The console can be found in the browser's `developer tools`.
This is a brief introduction to [developer tools](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_are_browser_developer_tools)
