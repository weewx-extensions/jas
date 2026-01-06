---
title: Miscellaneous Options
nav_order: 10
---

## allow_user_language_selection =

When `true`, the user can select the language to use.
**Experimental**

## bootstrap_version =

The version of the bootstrap library to use. Normally this should not be changed.

## bootstrap_icons_version =

The version of the bootstrap icons library to use. Normally this should not be changed.

## chart_modal =

When `True`, clicking on the chart title will display rhe chart in a modal window.

## css_override =

The name of a cheetah include file that contains user specified CSS.

**Note: Due to the way Cheetah compiles templates, do *not* dynamically generate this file.**

## data_binding =

The default WeeWX database binding for WeeWX-JAS to use.

## date_picker_version =

The version of the vanilla-datetimerange-picker library to use. Normally this should not be changed.

## echarts_version =

The version of the ECharts library to use. Normally this should not be changed.

## grid_cols =

The WeeWX-JAS skin uses [Bootstrap](https://getbootstrap.com) to control the layout.
A key feature of Bootstrap is its [grid system](https://getbootstrap.com/docs/5.0/layout/grid/
).
It is a twelve column system and [tiered breakpoints](https://getbootstrap.com/docs/5.0/layout/breakpoints/
).
WeeWX-JAS allows control over this via the `grid_cols` configuration option.
This option is used to specify the classes for a given column of data.
The  default value is `col-12 col-xl-6 mb-4`.
The `col-12` says that the data too be rendered will take all twelve of Bootstrap's columns.
Said a different way, the data will be in one column.  
The `col-xl-6` says that for [breakpoints](https://getbootstrap.com/docs/5.0/layout/breakpoints/) the data will take six of Bootstrap's twelve columns.
Said a different way, the data will be rendered in two columns.
The `mb-4` is specifying the [bottom margin](https://getbootstrap.com/docs/5.0/utilities/spacing/).
This is one way to add space between the displayed data.

## jas_debug_level =

Controls logging to the browser’s console.

1. debug/verbose and higher
2. info and higher
3. warn and higher (default)
4. error and higher

## landing_page =

The name of the ‘page’ to display when WeeWX-JAS is first displayed.
If not set or set to an invalid page, the ‘first’ page in the navbar is used.

## momentjs_version =

The version of the momentjs library to use. Normally this should not be changed.

## paho_mqtt_version =

The version of the mqtt library to use. Normally this should not be changed.

## popperjs_core_version =

The version of the popper library to use. Normally this should not be changed>

## use_browser_language_preference =

When `true`, WeeWX-JAS uses the browser’s language preferences to determine the language to use.
For more information see, [https://www.w3.org/International/questions/qa-lang-priorities#changing](https://www.w3.org/International/questions/qa-lang-priorities#changing)
**Experimental**

## themes =

Valid values are, `light` or `dark`. This designates the default theme.
