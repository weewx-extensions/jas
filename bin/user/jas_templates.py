#    Copyright (c) 2026 Rich Bell <bellrichm@gmail.com>
#
#    See the file LICENSE.txt for your full rights.
#

'''
Data templates used by JAS skin.
'''

data_aqi_template = \
'''
  pageData.aqi.value = {data_aqi_value};
  pageData.aqi.timestamp = {data_aqi_timestamp};
  pageData.aqi.category = "{data_aqi_category}";
  pageData.aqi.color = "{data_aqi_color}";
  pageData.aqi.method = "{data_aqi_method}";
  pageData.aqi.dominant = "{data_aqi_dominant}";
'''

data_alert_template = \
'''
  alert = {{}};
  alert.type = "alert_type_{alert_type}";
  alert.name = "{alert_name}";
  alert.loc = "{alert_loc}";
  alert.emergency = {alert_emergency};
  alert.priority = {alert_priority};
  alert.color = "{alert_color}";
  alert.cat = "{alert_cat}";
  alert.body = `{alert_body}`;
  alert.bodyFull = `{alert_body_full}`;
  pageData.alerts.push(alert);
'''

data_forecast_tempate = \
'''
  forecast = {{}};
  forecast.timestamp = {forecast_timestamp};
  forecast.observation_codes = [{forecast_observation_codes}];
  forecast.day_code = {forecast_day_code};
  forecast.temp_min = {forecast_temp_min};
  forecast.temp_max = {forecast_temp_max};
  forecast.temp_unit = "{forecast_temp_unit}";
  forecast.rain = {forecast_rain};
  forecast.wind_min = {forecast_wind_min};
  forecast.wind_max = {forecast_wind_max};
  forecast.wind_unit = "{forecast_wind_unit}";
  pageData.forecasts.push(forecast);
'''

data_load_template = \
'''<!doctype html>
<html>
  <head>
    <meta name="generator" content="jas {VERSION} {gen_time}">
    <script src="https://cdn.jsdelivr.net/npm/moment@{momentjs_version}/moment{momentjs_minified}.js"></script>
{script_string}    <script>
      window.addEventListener("load", function (event) {{
      console.debug(Date.now().toString() + " iframe start");
{dataload_string}        message = {{}};
        message.kind = "dataLoaded";
        message.message = JSON.stringify(pageData);
        window.parent.postMessage(message, "*");
        console.debug(Date.now().toString() + " iframe end");
      }})
    </script>
  </head>
</html>
'''

data_load_template2 =\
'''// the start
'''

data_load_template2 +=\
'''/* jas {VERSION} {gen_time} */
pageData = {{}};
function {interval_long_name}dataLoad() {{
  traceStart = Date.now();
  console.debug(Date.now().toString() + " dataLoad start");
'''
