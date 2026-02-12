---
title: The pages section
nav_order: 12
---

Pages are the base building block to display data.
Pages consist of [sections](https://weewx-extensions.github.io/jas/sections) and [charts](https://weewx-extensions.github.io/jas/charts).
WeeWX-JAS has the following pages.

| Name          | Time period                  | Data ('no' aggregation) | Sum (chart)    | Sum (current)     | Min/Max        |
|---------------|------------------------------|-------------------------|----------------|-------------------|----------------|
| about         | N/A                          | N/A                     | N/A            | N/A               | N/A            |
| day           | Current day                  | Archive period          | Archive period | Current day       | Archive period |
| last24hours   | Last 24 hours                | Archive period          | Archive period | Last 24 hours     | Archive period |
| yesterday     | Previous day                 | Archive period          | Archive period | Previous day      | Archive period |
| week          | Current week                 | Hour average            | Hour           | Current week      | Hour           |
| last7days     | Previous 7 days              | Hour average            | Hour           | Previous 7 days   | Hour           |
| month         | Current month                | Day average             | Day            | Current month     | Day            |
| last31days    | Previous 31 days             | Day average             | Day            | Previous 31 days  | Day            |
| year          | Current year                 | Day average             | Day            | Current year      | Day            |
| last366days   | Previous 366 days            | Day average             | Day            | Previous 366 days | Day            |
| month-archive | Historical month             | Hour average            | Day            | Display month     | Day            |
| year-archive  | Historical year              | Day average             | Day            | Display year      | Day            |
| yeartoyear    | Comparing data between years | Day average             | Day            | N/A               | Day            |
| multiyear     | Multiple years in the x-axis | Day average             | Day            | N/A               | Day            |

- Time period: The period of time from which the data is displayed.
- Data ('no' aggregation): The data displayed (usually in a chart) when no aggregation is specified.
- The year-archive and month-archive are more like a template that will generate a page for every
year and every year/month in the database. Theses pages must have [navbar = primary](https://weewx-extensions.github.io/jas/pages#navbar-).

## filename =

The name of a cheetah include file that will be used to generate the ‘about’ page. Note, this is only valid in the about page section.

**Note: Due to the way Cheetah compiles templates, do *not* dynamically generate this file.**

## layout =

The name of a cheetah include file that will change the layout of all pages except the ‘about’ page.

**Note: Due to the way Cheetah compiles templates, do *not* dynamically generate this file.**

## query_string_on

Provides the ability to add a query string to requests for the page's [HTML component](https://weewx-extensions.github.io/jas/getting-started#html)
or
requests for the page’s [data component](https://weewx-extensions.github.io/jas/getting-started#data).
This allows the serving infrastructure to use the query string as part of the cache key.
The  pages' [data component](https://weewx-extensions.github.io/jas/getting-started#data) is made up of
the [data loader sub-component](https://weewx-extensions.github.io/jas/getting-started#data-loader) and
the [data helper sub-component](https://weewx-extensions.github.io/jas/getting-started#data-helper).

When `query_string_on` contains the value `data`:

- The query string on request for the javascript portion of the [data loader sub-component](https://weewx-extensions.github.io/jas/getting-started#data-loader)
is the timestamp that the data was generated.
- The query string on request for the HTML portion of the [data loader sub-component](https://weewx-extensions.github.io/jas/getting-started#data-loader)
is the current timestamp.
This ensures the HTML is never cached and it will be updated with the new javascript query string.
This makes it easy to ‘break’ the cache when new data has been generated.

When `query_string_on` contains the value `page`:

- The query string on the request for the [HTML](https://weewx-extensions.github.io/jas/getting-started#html)
is the current timestamp. This value is deprecated and will be removed.

Valid values are any combination of `page` and `data`.
For example, `query_string_on = page, data` or `query_string_on = page` or `query_string_on = data`, etc.
The default value is `not set`.

## The `[[[[[page-name]]]]]` stanza

The pages to display are configured by including a [[[[[*page-name*]]]]] subsection for the desired named page.
The order of the [[[[[*page-name*]]]]] sections is the order the pages will be displayed in the navigation menu.
It is one of the values listed in the [above table](https://weewx-extensions.github.io/jas/pages#the-pages-section).

### chart_modal =

Overrides the [chart_modal](https://weewx-extensions.github.io/jas/miscellaneous-options#chart_modal) at the page level.

### delay_seconds =

The time to wait after the interval has reached before reloading the page.
This gives WeeWX time to generate the data.
The default is `60`.

### enable =

When set to `false`, the page will not be displayed

### end =

For charts that display multiple years of data, controls the ending year to display.

### grid_cols =

Override the default [grid_cols](https://weewx-extensions.github.io/jas/miscellaneous-options#grid_cols-) at the page level.

### navbar =

Valid values are, `primary` or `secondary`.
When set to `primary`, the page is placed directly in the navbar.
When set to `secondary`, the page is placed in a `more` dropdown in the navbar.

### mqtt =

Controls if page sections are updated with MQTT data.

### query_string_on

Overrides the [query_string on](https://weewx-extensions.github.io/jas/pages#query_string_on) at the page level.

### reload =

When true, adds code to automatically reload the page.
The default is `false`.

### start =

For charts that display multiple years of data, controls the starting year to display.

### wait_seconds =

The interval to reload the page.
A setting of 300 means the page will reload on the hour, five minutes after, 10 minutes after, etc.
The default is `300`.

### zoomControl =

Adds a date range picker to limit the data displayed.
This does not change the aggregate interval.

### The `[[[[[[section-name]]]]]]` stanza

Used to include either [sections](https://weewx-extensions.github.io/jas/sections) or
[charts](https://weewx-extensions.github.io/jas/charts).
Each section and chart has its own stanza that is the name of the defined section or chart.

#### layout =

This option is only valid in the `forecast` subsection.
It should be set to `row`

#### series_type =

This option is only valid for `charts`.
The only valid value is `mqtt`
When set to `mqtt`, the chart updates with mqtt data.

## Putting it all together

The following will create a website with a `day` and `year` pages.
The `day` page will automatically reload.
The `year` page will have a date range picker.
This can be used to ‘zoom in’ the date range.

```
[StdReport]
    [[jas]]
        [[[Extras]]]
            [[[[pages]]]]
                [[[[[day]]]]]
                    reload = True
                [[[[[year]]]]]
                    zoomControl = True
                ```
