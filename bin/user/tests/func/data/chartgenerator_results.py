#    Copyright (c) 2026 Rich Bell <bellrichm@gmail.com>
#
#    See the file LICENSE.txt for your full rights.
#

# pylint: disable=wrong-import-order
# pylint: disable=missing-module-docstring, missing-class-docstring, missing-function-docstring
# pylint: disable=invalid-name

# pylint: disable=line-too-long

result1 =\
'''
/* jas 1.2.0-rc03 {now} */
utc_offset = -300.0;
function simpleTooltipFormatter(args) {{
  dateTime = moment.unix(args[0].axisValue/1000).utcOffset(utc_offset).format(dateTimeFormat[lang].chart[aggregate_interval].toolTipX);
  let tooltip = `<div>${{dateTime}}</div> `;

  args.forEach(({{ color, seriesName, value }}) => {{
    value = value[1] ? Number(value[1]).toLocaleString(lang) : value[1];
    if (value != null) {{tooltip += `<div style="color: ${{color}};">${{seriesName}} ${{value}}</div>`}};
  }});
  return tooltip;
}}

function setupCharts() {{
  ordinateNames = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW'];

  aggregate_interval = 'none'
  aggregate_interval = 'none'
  aggregate_interval = 'none'
  var option = {{
    series: [
    {{
      z: 100,
      type: 'line',
      smooth: true,
      symbol: 'none',
    }},
    {{
      type: 'line',
      smooth: true,
      symbol: 'none',
    }},
    {{
      type: 'line',
      smooth: true,
      symbol: 'none',
    }},
    ],
    title: {{
      left: 'center',
    }},
    toolbox: {{
      feature: {{
        dataZoom: {{
          yAxisIndex: 'none',
          restore: {{
          }},
          saveAsImage: {{
          }},
        }},
      }},
    }},
    legend: {{
      orient: 'horizontal',
      bottom: 0,
      textStyle: {{
        color: 'color',
      }},
    }},
    tooltip: {{
      trigger: 'axis',
      className: 'echarts-tooltip',
      formatter: simpleTooltipFormatter,
      textStyle: {{
        color: 'var(--bs-body-color)',
      }},
      axisPointer: {{
        label: {{
        }},
      }},
    }},
    xAxis: {{
      type: 'time',
      boundaryGap: false,
      axisLine: {{
        onZero: false,
      }},
      axisLabel: {{
        hideOverlap: true,
        formatter: function (value) {{ return moment.unix(value/1000).utcOffset(utc_offset).format(dateTimeFormat[lang].chart[aggregate_interval].xAxisLabel); }},
      }},
    }},
    yAxis: [
    {{
      name:' ',
      type: 'value',
      boundaryGap: [0, '100%'],
      min: function (value) {{return Math.floor(value.min);}},
      max: function (value) {{return Math.ceil(value.max);}},
      axisLabel: {{
        formatter: function (value) {{return(value ? value.toLocaleString(lang) : value);}},
      }},
    }},
  ],
  }};

  pageIndex['outTempday'] = Object.keys(pageIndex).length;
  var telem = document.getElementById('outTempday');
  var outTempchart = echarts.init(document.getElementById('outTempday'));
  outTempchart.setOption(option);
  pageChart = {{}};
  pageChart.def = option;
  pageChart.chart = outTempchart;
  pageCharts.push(pageChart);

  aggregate_interval = 'none'
  aggregate_interval = 'none'
  aggregate_interval = 'none'
  var option = {{
    series: [
    {{
      yAxisIndex: 0,
      type: 'line',
      smooth: true,
      symbol: 'none',
    }},
    {{
      yAxisIndex: 1,
      type: 'scatter',
      symbolSize: 5,
    }},
    {{
      type: 'line',
      smooth: true,
      symbol: 'none',
    }},
    ],
    title: {{
      left: 'center',
    }},
    toolbox: {{
      feature: {{
        dataZoom: {{
          yAxisIndex: 'none',
          restore: {{
          }},
          saveAsImage: {{
          }},
        }},
      }},
    }},
    legend: {{
      orient: 'horizontal',
      bottom: 0,
      textStyle: {{
        color: 'color',
      }},
    }},
    tooltip: {{
      trigger: 'axis',
      className: 'echarts-tooltip',
      formatter: simpleTooltipFormatter,
      textStyle: {{
        color: 'var(--bs-body-color)',
      }},
      axisPointer: {{
        label: {{
        }},
      }},
    }},
    xAxis: {{
      type: 'time',
      boundaryGap: false,
      axisLine: {{
        onZero: false,
      }},
      axisLabel: {{
        hideOverlap: true,
        formatter: function (value) {{ return moment.unix(value/1000).utcOffset(utc_offset).format(dateTimeFormat[lang].chart[aggregate_interval].xAxisLabel); }},
      }},
    }},
    yAxis: [
    {{
      name:' ',
      type: 'value',
      boundaryGap: [0, '100%'],
      min: function (value) {{return Math.floor(value.min);}},
      max: function (value) {{return Math.ceil(value.max);}},
      axisLabel: {{
        formatter: function (value) {{return(value ? value.toLocaleString(lang) : value);}},
      }},
    }},
    {{
      name:' ',
      type: 'value',
      boundaryGap: [0, '100%'],
      min: function (value) {{return Math.floor(value.min);}},
      max: function (value) {{return Math.ceil(value.max);}},
      axisLabel: {{
        formatter: function (value) {{return(value ? value.toLocaleString(lang) : value);}},
      }},
    }},
  ],
  }};

  pageIndex['outHumidityday'] = Object.keys(pageIndex).length;
  var telem = document.getElementById('outHumidityday');
  var outHumiditychart = echarts.init(document.getElementById('outHumidityday'));
  outHumiditychart.setOption(option);
  pageChart = {{}};
  pageChart.def = option;
  pageChart.chart = outHumiditychart;
  pageCharts.push(pageChart);

  aggregate_interval = 'none'
  var option = {{
    series: [
    {{
      type: 'line',
      smooth: true,
      symbol: 'none',
    }},
    ],
    title: {{
      left: 'center',
    }},
    toolbox: {{
      feature: {{
        dataZoom: {{
          yAxisIndex: 'none',
          restore: {{
          }},
          saveAsImage: {{
          }},
        }},
      }},
    }},
    legend: {{
      orient: 'horizontal',
      bottom: 0,
      textStyle: {{
        color: 'color',
      }},
    }},
    tooltip: {{
      trigger: 'axis',
      className: 'echarts-tooltip',
      formatter: simpleTooltipFormatter,
      textStyle: {{
        color: 'var(--bs-body-color)',
      }},
      axisPointer: {{
        label: {{
        }},
      }},
    }},
    xAxis: {{
      type: 'time',
      boundaryGap: false,
      axisLine: {{
        onZero: false,
      }},
      axisLabel: {{
        hideOverlap: true,
        formatter: function (value) {{ return moment.unix(value/1000).utcOffset(utc_offset).format(dateTimeFormat[lang].chart[aggregate_interval].xAxisLabel); }},
      }},
    }},
    yAxis: [
    {{
      name:' ',
      type: 'value',
      boundaryGap: [0, '100%'],
      min: function (value) {{return Math.floor(value.min);}},
      max: function (value) {{return Math.ceil(value.max);}},
      axisLabel: {{
        formatter: function (value) {{return(value ? value.toLocaleString(lang) : value);}},
      }},
    }},
  ],
  }};

  pageIndex['barometerday'] = Object.keys(pageIndex).length;
  var telem = document.getElementById('barometerday');
  var barometerchart = echarts.init(document.getElementById('barometerday'));
  barometerchart.setOption(option);
  pageChart = {{}};
  pageChart.def = option;
  pageChart.chart = barometerchart;
  pageCharts.push(pageChart);

  aggregate_interval = 'none'
  aggregate_interval = 'none'
  var option = {{
    series: [
    {{
      yAxisIndex: 1,
      type: 'line',
      smooth: true,
      symbol: 'none',
    }},
    {{
      yAxisIndex: 0,
      type: 'bar',
    }},
    ],
    title: {{
      left: 'center',
    }},
    toolbox: {{
      feature: {{
        dataZoom: {{
          yAxisIndex: 'none',
          restore: {{
          }},
          saveAsImage: {{
          }},
        }},
      }},
    }},
    legend: {{
      orient: 'horizontal',
      bottom: 0,
      textStyle: {{
        color: 'color',
      }},
    }},
    tooltip: {{
      trigger: 'axis',
      className: 'echarts-tooltip',
      formatter: simpleTooltipFormatter,
      textStyle: {{
        color: 'var(--bs-body-color)',
      }},
      axisPointer: {{
        label: {{
        }},
      }},
    }},
    xAxis: {{
      type: 'time',
      boundaryGap: false,
      axisLine: {{
        onZero: false,
      }},
      axisLabel: {{
        hideOverlap: true,
        formatter: function (value) {{ return moment.unix(value/1000).utcOffset(utc_offset).format(dateTimeFormat[lang].chart[aggregate_interval].xAxisLabel); }},
      }},
    }},
    yAxis: [
    {{
      name:' ',
      type: 'value',
      boundaryGap: [0, '100%'],
      min: function (value) {{return Math.floor(value.min);}},
      max: function (value) {{return Math.ceil(value.max);}},
      axisLabel: {{
        formatter: function (value) {{return(value ? value.toLocaleString(lang) : value);}},
      }},
    }},
    {{
      name:' ',
      type: 'value',
      boundaryGap: [0, '100%'],
      min: function (value) {{return Math.floor(value.min);}},
      max: function (value) {{return Math.ceil(value.max);}},
      axisLabel: {{
        formatter: function (value) {{return(value ? value.toLocaleString(lang) : value);}},
      }},
    }},
  ],
  }};

  pageIndex['rainday'] = Object.keys(pageIndex).length;
  var telem = document.getElementById('rainday');
  var rainchart = echarts.init(document.getElementById('rainday'));
  rainchart.setOption(option);
  pageChart = {{}};
  pageChart.def = option;
  pageChart.chart = rainchart;
  pageCharts.push(pageChart);

  aggregate_interval = 'none'
  aggregate_interval = 'none'
  aggregate_interval = 'none'
  var option = {{
    series: [
    {{
      yAxisIndex: 0,
      type: 'line',
      smooth: true,
      symbol: 'none',
    }},
    {{
      type: 'line',
      smooth: true,
      symbol: 'none',
    }},
    {{
      yAxisIndex: 1,
      type: 'scatter',
    }},
    ],
    title: {{
      left: 'center',
    }},
    toolbox: {{
      feature: {{
        dataZoom: {{
          yAxisIndex: 'none',
          restore: {{
          }},
          saveAsImage: {{
          }},
        }},
      }},
    }},
    legend: {{
      orient: 'horizontal',
      bottom: 0,
      textStyle: {{
        color: 'color',
      }},
    }},
    tooltip: {{
      trigger: 'axis',
      className: 'echarts-tooltip',
      formatter: simpleTooltipFormatter,
      textStyle: {{
        color: 'var(--bs-body-color)',
      }},
      axisPointer: {{
        label: {{
        }},
      }},
    }},
    xAxis: {{
      type: 'time',
      boundaryGap: false,
      axisLine: {{
        onZero: false,
      }},
      axisLabel: {{
        hideOverlap: true,
        formatter: function (value) {{ return moment.unix(value/1000).utcOffset(utc_offset).format(dateTimeFormat[lang].chart[aggregate_interval].xAxisLabel); }},
      }},
    }},
    yAxis: [
    {{
      name:' ',
      type: 'value',
      boundaryGap: [0, '100%'],
      min: function (value) {{return Math.floor(value.min);}},
      max: function (value) {{return Math.ceil(value.max);}},
      axisLabel: {{
        formatter: function (value) {{return(value ? value.toLocaleString(lang) : value);}},
      }},
    }},
    {{
      name:' ',
      type: 'value',
      boundaryGap: [0, '100%'],
      min: function (value) {{return Math.floor(value.min);}},
      max: function (value) {{return Math.ceil(value.max);}},
      axisLabel: {{
        formatter: function (value) {{return(value ? value.toLocaleString(lang) : value);}},
      }},
    }},
  ],
  }};

  pageIndex['windday'] = Object.keys(pageIndex).length;
  var telem = document.getElementById('windday');
  var windchart = echarts.init(document.getElementById('windday'));
  windchart.setOption(option);
  pageChart = {{}};
  pageChart.def = option;
  pageChart.chart = windchart;
  pageCharts.push(pageChart);

  aggregate_interval = 'none'
  var option = {{
    series: [
    {{
      type: 'bar',
    }},
    ],
    title: {{
      left: 'center',
    }},
    toolbox: {{
      feature: {{
        dataZoom: {{
          yAxisIndex: 'none',
          restore: {{
          }},
          saveAsImage: {{
          }},
        }},
      }},
    }},
    legend: {{
      orient: 'horizontal',
      bottom: 0,
      textStyle: {{
        color: 'color',
      }},
    }},
    tooltip: {{
      trigger: 'axis',
      className: 'echarts-tooltip',
      formatter: simpleTooltipFormatter,
      textStyle: {{
        color: 'var(--bs-body-color)',
      }},
      axisPointer: {{
        label: {{
        }},
      }},
    }},
    xAxis: {{
      type: 'time',
      boundaryGap: false,
      axisLine: {{
        onZero: false,
      }},
      axisLabel: {{
        hideOverlap: true,
        formatter: function (value) {{ return moment.unix(value/1000).utcOffset(utc_offset).format(dateTimeFormat[lang].chart[aggregate_interval].xAxisLabel); }},
      }},
    }},
    yAxis: [
    {{
      name:' ',
      type: 'value',
      boundaryGap: [0, '100%'],
      min: function (value) {{return Math.floor(value.min);}},
      max: function (value) {{return Math.ceil(value.max);}},
      axisLabel: {{
        formatter: function (value) {{return(value ? value.toLocaleString(lang) : value);}},
      }},
    }},
  ],
  }};

  pageIndex['ETday'] = Object.keys(pageIndex).length;
  var telem = document.getElementById('ETday');
  var ETchart = echarts.init(document.getElementById('ETday'));
  ETchart.setOption(option);
  pageChart = {{}};
  pageChart.def = option;
  pageChart.chart = ETchart;
  pageCharts.push(pageChart);

  aggregate_interval = 'none'
  var option = {{
    series: [
    {{
      type: 'line',
      smooth: true,
      symbol: 'none',
    }},
    ],
    title: {{
      left: 'center',
    }},
    toolbox: {{
      feature: {{
        dataZoom: {{
          yAxisIndex: 'none',
          restore: {{
          }},
          saveAsImage: {{
          }},
        }},
      }},
    }},
    legend: {{
      orient: 'horizontal',
      bottom: 0,
      textStyle: {{
        color: 'color',
      }},
    }},
    tooltip: {{
      trigger: 'axis',
      className: 'echarts-tooltip',
      formatter: simpleTooltipFormatter,
      textStyle: {{
        color: 'var(--bs-body-color)',
      }},
      axisPointer: {{
        label: {{
        }},
      }},
    }},
    xAxis: {{
      type: 'time',
      boundaryGap: false,
      axisLine: {{
        onZero: false,
      }},
      axisLabel: {{
        hideOverlap: true,
        formatter: function (value) {{ return moment.unix(value/1000).utcOffset(utc_offset).format(dateTimeFormat[lang].chart[aggregate_interval].xAxisLabel); }},
      }},
    }},
    yAxis: [
    {{
      name:' ',
      type: 'value',
      boundaryGap: [0, '100%'],
      min: function (value) {{return Math.floor(value.min);}},
      max: function (value) {{return Math.ceil(value.max);}},
      axisLabel: {{
        formatter: function (value) {{return(value ? value.toLocaleString(lang) : value);}},
      }},
    }},
  ],
  }};

  pageIndex['UVday'] = Object.keys(pageIndex).length;
  var telem = document.getElementById('UVday');
  var UVchart = echarts.init(document.getElementById('UVday'));
  UVchart.setOption(option);
  pageChart = {{}};
  pageChart.def = option;
  pageChart.chart = UVchart;
  pageCharts.push(pageChart);

  aggregate_interval = 'none'
  var option = {{
    series: [
    {{
      type: 'line',
      smooth: true,
      symbol: 'none',
    }},
    ],
    title: {{
      left: 'center',
    }},
    toolbox: {{
      feature: {{
        dataZoom: {{
          yAxisIndex: 'none',
          restore: {{
          }},
          saveAsImage: {{
          }},
        }},
      }},
    }},
    legend: {{
      orient: 'horizontal',
      bottom: 0,
      textStyle: {{
        color: 'color',
      }},
    }},
    tooltip: {{
      trigger: 'axis',
      className: 'echarts-tooltip',
      formatter: simpleTooltipFormatter,
      textStyle: {{
        color: 'var(--bs-body-color)',
      }},
      axisPointer: {{
        label: {{
        }},
      }},
    }},
    xAxis: {{
      type: 'time',
      boundaryGap: false,
      axisLine: {{
        onZero: false,
      }},
      axisLabel: {{
        hideOverlap: true,
        formatter: function (value) {{ return moment.unix(value/1000).utcOffset(utc_offset).format(dateTimeFormat[lang].chart[aggregate_interval].xAxisLabel); }},
      }},
    }},
    yAxis: [
    {{
      name:' ',
      type: 'value',
      boundaryGap: [0, '100%'],
      min: function (value) {{return Math.floor(value.min);}},
      max: function (value) {{return Math.ceil(value.max);}},
      axisLabel: {{
        formatter: function (value) {{return(value ? value.toLocaleString(lang) : value);}},
      }},
    }},
  ],
  }};

  pageIndex['radiationday'] = Object.keys(pageIndex).length;
  var telem = document.getElementById('radiationday');
  var radiationchart = echarts.init(document.getElementById('radiationday'));
  radiationchart.setOption(option);
  pageChart = {{}};
  pageChart.def = option;
  pageChart.chart = radiationchart;
  pageCharts.push(pageChart);

}}
function updateChartData() {{
  index = 0;
  series_option = {{
    series: [
      {{name: getLabel('outTemp_celsius'),
       data: day_avg.outTemp_binding2_degree_C}},
      {{name: getLabel('windchill'),
       data: day_avg.windchill_wx_binding}},
      {{name: getLabel('heatindex'),
       data: day_avg.heatindex_wx_binding}},
  ]}};
  pageCharts[index].chart.setOption(series_option);
  pageCharts[index].option = series_option;
  index += 1;
  series_option = {{
    series: [
      {{name: getLabel('dewpoint'),
       data: day_avg.dewpoint_wx_binding}},
      {{name: getLabel('outHumidity'),
       data: day_avg.outHumidity_wx_binding}},
      {{name: getLabel('outTemp'),
       data: day_avg.outTemp_wx_binding}},
  ]}};
  pageCharts[index].chart.setOption(series_option);
  pageCharts[index].option = series_option;
  index += 1;
  series_option = {{
    series: [
      {{name: getLabel('barometer'),
       data: day_avg.barometer_wx_binding}},
  ]}};
  pageCharts[index].chart.setOption(series_option);
  pageCharts[index].option = series_option;
  index += 1;
  series_option = {{
    series: [
      {{name: getLabel('rainRate'),
       data: day_max.rainRate_wx_binding}},
      {{name: getLabel('rain'),
       data: day_sum.rain_wx_binding}},
  ]}};
  pageCharts[index].chart.setOption(series_option);
  pageCharts[index].option = series_option;
  index += 1;
  series_option = {{
    series: [
      {{name: getLabel('windSpeed'),
       data: day_avg.windSpeed_wx_binding}},
      {{name: getLabel('windGust'),
       data: day_max.windGust_wx_binding}},
      {{name: getLabel('windDir'),
       data: day_avg.windDir_wx_binding}},
  ]}};
  pageCharts[index].chart.setOption(series_option);
  pageCharts[index].option = series_option;
  index += 1;
  series_option = {{
    series: [
      {{name: getLabel('ET'),
       data: day_sum.ET_wx_binding}},
  ]}};
  pageCharts[index].chart.setOption(series_option);
  pageCharts[index].option = series_option;
  index += 1;
  series_option = {{
    series: [
      {{name: getLabel('UV'),
       data: day_avg.UV_wx_binding}},
  ]}};
  pageCharts[index].chart.setOption(series_option);
  pageCharts[index].option = series_option;
  index += 1;
  series_option = {{
    series: [
      {{name: getLabel('radiation'),
       data: day_avg.radiation_wx_binding}},
  ]}};
  pageCharts[index].chart.setOption(series_option);
  pageCharts[index].option = series_option;
  index += 1;
}}
'''
