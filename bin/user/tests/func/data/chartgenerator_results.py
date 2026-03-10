#    Copyright (c) 2026 Rich Bell <bellrichm@gmail.com>
#
#    See the file LICENSE.txt for your full rights.
#

# pylint: disable=wrong-import-order
# pylint: disable=missing-module-docstring, missing-class-docstring, missing-function-docstring
# pylint: disable=invalid-name

# pylint: disable=line-too-long
# pylint: disable=too-many-lines

result1 =\
'''
/* jas 1.2.0-rc03 {now} */
utc_offset = {utc_offset};
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
  windRangeLegend = ['<1  mph', '1-4  mph', '4-8  mph', '8-13  mph', '13-19  mph', '19-25  mph', '25-32  mph', '>32  mph'];

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
      name:'  mph',
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
      name: windRangeLegend[0],
      barCategoryGap: 0,
      type: 'bar',
      coordinateSystem: 'polar',
      stack: 'a',
    }},
    {{
      name: windRangeLegend[1],
      barCategoryGap: 0,
      type: 'bar',
      coordinateSystem: 'polar',
      stack: 'a',
    }},
    {{
      name: windRangeLegend[2],
      barCategoryGap: 0,
      type: 'bar',
      coordinateSystem: 'polar',
      stack: 'a',
    }},
    {{
      name: windRangeLegend[3],
      barCategoryGap: 0,
      type: 'bar',
      coordinateSystem: 'polar',
      stack: 'a',
    }},
    {{
      name: windRangeLegend[4],
      barCategoryGap: 0,
      type: 'bar',
      coordinateSystem: 'polar',
      stack: 'a',
    }},
    {{
      name: windRangeLegend[5],
      barCategoryGap: 0,
      type: 'bar',
      coordinateSystem: 'polar',
      stack: 'a',
    }},
    {{
      name: windRangeLegend[6],
      barCategoryGap: 0,
      type: 'bar',
      coordinateSystem: 'polar',
      stack: 'a',
    }},
    ],
    tooltip: {{
      trigger: 'item',
      className: 'echarts-tooltip',
      textStyle: {{
        color: 'var(--bs-body-color)',
      }},
    }},
    angleAxis: {{
      type: 'category',
      data: ordinateNames,
      boundaryGap: false,
      axisTick: {{
        show: false,
      }},
      splitLine: {{
        show: true,
      }},
    }},
    radiusAxis: {{
      show: false,
    }},
    polar: {{
    }},
    legend: {{
      data: windRangeLegend,
      orient: 'vertical',
      right: 0,
      type: 'scroll',
      icon: 'roundRect',
      textStyle: {{
        width: 70,
        color: 'color',
        overflow: 'break',
      }},
    }},
  }};

  pageIndex['windRoseday'] = Object.keys(pageIndex).length;
  var telem = document.getElementById('windRoseday');
  var windRosechart = echarts.init(document.getElementById('windRoseday'));
  windRosechart.setOption(option);
  pageChart = {{}};
  pageChart.def = option;
  pageChart.chart = windRosechart;
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
      {{name: windRangeLegend[0],
       data: day_avg.windCompassRange0_wx_binding}},
      {{name: windRangeLegend[1],
       data: day_avg.windCompassRange1_wx_binding}},
      {{name: windRangeLegend[2],
       data: day_avg.windCompassRange2_wx_binding}},
      {{name: windRangeLegend[3],
       data: day_avg.windCompassRange3_wx_binding}},
      {{name: windRangeLegend[4],
       data: day_avg.windCompassRange4_wx_binding}},
      {{name: windRangeLegend[5],
       data: day_avg.windCompassRange5_wx_binding}},
      {{name: windRangeLegend[6],
       data: day_avg.windCompassRange6_wx_binding}},
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

result2 =\
'''
/* jas 1.2.0-rc03 {now} */
utc_offset = {utc_offset};
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

  var option = {{
    series: [
     {{
    name: '2026',
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
      textStyle: {{
        color: 'var(--bs-body-color)',
      }},
    }},
    xAxis: {{
      type: 'category',
      data: monthDays[lang],
      axisLabel: {{
        hideOverlap: true,
      }},
      axisLine: {{
        onZero: false,
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

  pageIndex['outTempMaxyeartoyear'] = Object.keys(pageIndex).length;
  var telem = document.getElementById('outTempMaxyeartoyear');
  var outTempMaxchart = echarts.init(document.getElementById('outTempMaxyeartoyear'));
  outTempMaxchart.setOption(option);
  pageChart = {{}};
pageChart.def = option;
  pageChart.chart = outTempMaxchart;
  pageCharts.push(pageChart);

  var option = {{
    series: [
     {{
    name: '2026',
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
      textStyle: {{
        color: 'var(--bs-body-color)',
      }},
    }},
    xAxis: {{
      type: 'category',
      data: monthDays[lang],
      axisLabel: {{
        hideOverlap: true,
      }},
      axisLine: {{
        onZero: false,
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

  pageIndex['outTempMinyeartoyear'] = Object.keys(pageIndex).length;
  var telem = document.getElementById('outTempMinyeartoyear');
  var outTempMinchart = echarts.init(document.getElementById('outTempMinyeartoyear'));
  outTempMinchart.setOption(option);
  pageChart = {{}};
pageChart.def = option;
  pageChart.chart = outTempMinchart;
  pageCharts.push(pageChart);

  var option = {{
    series: [
     {{
    name: '2026',
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
      textStyle: {{
        color: 'var(--bs-body-color)',
      }},
    }},
    xAxis: {{
      type: 'category',
      data: monthDays[lang],
      axisLabel: {{
        hideOverlap: true,
      }},
      axisLine: {{
        onZero: false,
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

  pageIndex['windchillMinyeartoyear'] = Object.keys(pageIndex).length;
  var telem = document.getElementById('windchillMinyeartoyear');
  var windchillMinchart = echarts.init(document.getElementById('windchillMinyeartoyear'));
  windchillMinchart.setOption(option);
  pageChart = {{}};
pageChart.def = option;
  pageChart.chart = windchillMinchart;
  pageCharts.push(pageChart);

  var option = {{
    series: [
     {{
    name: '2026',
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
      textStyle: {{
        color: 'var(--bs-body-color)',
      }},
    }},
    xAxis: {{
      type: 'category',
      data: monthDays[lang],
      axisLabel: {{
        hideOverlap: true,
      }},
      axisLine: {{
        onZero: false,
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

  pageIndex['heatindexMaxyeartoyear'] = Object.keys(pageIndex).length;
  var telem = document.getElementById('heatindexMaxyeartoyear');
  var heatindexMaxchart = echarts.init(document.getElementById('heatindexMaxyeartoyear'));
  heatindexMaxchart.setOption(option);
  pageChart = {{}};
pageChart.def = option;
  pageChart.chart = heatindexMaxchart;
  pageCharts.push(pageChart);

  var option = {{
    series: [
     {{
    name: '2026',
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
      textStyle: {{
        color: 'var(--bs-body-color)',
      }},
    }},
    xAxis: {{
      type: 'category',
      data: monthDays[lang],
      axisLabel: {{
        hideOverlap: true,
      }},
      axisLine: {{
        onZero: false,
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

  pageIndex['barometeryeartoyear'] = Object.keys(pageIndex).length;
  var telem = document.getElementById('barometeryeartoyear');
  var barometerchart = echarts.init(document.getElementById('barometeryeartoyear'));
  barometerchart.setOption(option);
  pageChart = {{}};
pageChart.def = option;
  pageChart.chart = barometerchart;
  pageCharts.push(pageChart);

  var option = {{
    series: [
     {{
    name: '2026',
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
      textStyle: {{
        color: 'var(--bs-body-color)',
      }},
    }},
    xAxis: {{
      type: 'category',
      data: monthDays[lang],
      axisLabel: {{
        hideOverlap: true,
      }},
      axisLine: {{
        onZero: false,
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

  pageIndex['dewpointMaxyeartoyear'] = Object.keys(pageIndex).length;
  var telem = document.getElementById('dewpointMaxyeartoyear');
  var dewpointMaxchart = echarts.init(document.getElementById('dewpointMaxyeartoyear'));
  dewpointMaxchart.setOption(option);
  pageChart = {{}};
pageChart.def = option;
  pageChart.chart = dewpointMaxchart;
  pageCharts.push(pageChart);

  var option = {{
    series: [
     {{
    name: '2026',
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
      textStyle: {{
        color: 'var(--bs-body-color)',
      }},
    }},
    xAxis: {{
      type: 'category',
      data: monthDays[lang],
      axisLabel: {{
        hideOverlap: true,
      }},
      axisLine: {{
        onZero: false,
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

  pageIndex['dewpointMinyeartoyear'] = Object.keys(pageIndex).length;
  var telem = document.getElementById('dewpointMinyeartoyear');
  var dewpointMinchart = echarts.init(document.getElementById('dewpointMinyeartoyear'));
  dewpointMinchart.setOption(option);
  pageChart = {{}};
pageChart.def = option;
  pageChart.chart = dewpointMinchart;
  pageCharts.push(pageChart);

  var option = {{
    series: [
     {{
    name: '2026',
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
      textStyle: {{
        color: 'var(--bs-body-color)',
      }},
    }},
    xAxis: {{
      type: 'category',
      data: monthDays[lang],
      axisLabel: {{
        hideOverlap: true,
      }},
      axisLine: {{
        onZero: false,
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

  pageIndex['outHumidityMaxyeartoyear'] = Object.keys(pageIndex).length;
  var telem = document.getElementById('outHumidityMaxyeartoyear');
  var outHumidityMaxchart = echarts.init(document.getElementById('outHumidityMaxyeartoyear'));
  outHumidityMaxchart.setOption(option);
  pageChart = {{}};
pageChart.def = option;
  pageChart.chart = outHumidityMaxchart;
  pageCharts.push(pageChart);

  var option = {{
    series: [
     {{
    name: '2026',
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
      textStyle: {{
        color: 'var(--bs-body-color)',
      }},
    }},
    xAxis: {{
      type: 'category',
      data: monthDays[lang],
      axisLabel: {{
        hideOverlap: true,
      }},
      axisLine: {{
        onZero: false,
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

  pageIndex['outHumidityMinyeartoyear'] = Object.keys(pageIndex).length;
  var telem = document.getElementById('outHumidityMinyeartoyear');
  var outHumidityMinchart = echarts.init(document.getElementById('outHumidityMinyeartoyear'));
  outHumidityMinchart.setOption(option);
  pageChart = {{}};
pageChart.def = option;
  pageChart.chart = outHumidityMinchart;
  pageCharts.push(pageChart);

  var option = {{
    series: [
     {{
    name: '2026',
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
      textStyle: {{
        color: 'var(--bs-body-color)',
      }},
    }},
    xAxis: {{
      type: 'category',
      data: monthDays[lang],
      axisLabel: {{
        hideOverlap: true,
      }},
      axisLine: {{
        onZero: false,
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

  pageIndex['rainOnlyyeartoyear'] = Object.keys(pageIndex).length;
  var telem = document.getElementById('rainOnlyyeartoyear');
  var rainOnlychart = echarts.init(document.getElementById('rainOnlyyeartoyear'));
  rainOnlychart.setOption(option);
  pageChart = {{}};
pageChart.def = option;
  pageChart.chart = rainOnlychart;
  pageCharts.push(pageChart);

  var option = {{
    series: [
     {{
    name: '2026',
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
      textStyle: {{
        color: 'var(--bs-body-color)',
      }},
    }},
    xAxis: {{
      type: 'category',
      data: monthDays[lang],
      axisLabel: {{
        hideOverlap: true,
      }},
      axisLine: {{
        onZero: false,
      }},
    }},
    yAxis: [
    {{
      name:'  mph',
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

  pageIndex['windGustOnlyyeartoyear'] = Object.keys(pageIndex).length;
  var telem = document.getElementById('windGustOnlyyeartoyear');
  var windGustOnlychart = echarts.init(document.getElementById('windGustOnlyyeartoyear'));
  windGustOnlychart.setOption(option);
  pageChart = {{}};
pageChart.def = option;
  pageChart.chart = windGustOnlychart;
  pageCharts.push(pageChart);

  var option = {{
    series: [
     {{
    name: '2026',
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
      textStyle: {{
        color: 'var(--bs-body-color)',
      }},
    }},
    xAxis: {{
      type: 'category',
      data: monthDays[lang],
      axisLabel: {{
        hideOverlap: true,
      }},
      axisLine: {{
        onZero: false,
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

  pageIndex['ETyeartoyear'] = Object.keys(pageIndex).length;
  var telem = document.getElementById('ETyeartoyear');
  var ETchart = echarts.init(document.getElementById('ETyeartoyear'));
  ETchart.setOption(option);
  pageChart = {{}};
pageChart.def = option;
  pageChart.chart = ETchart;
  pageCharts.push(pageChart);

  var option = {{
    series: [
     {{
    name: '2026',
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
      textStyle: {{
        color: 'var(--bs-body-color)',
      }},
    }},
    xAxis: {{
      type: 'category',
      data: monthDays[lang],
      axisLabel: {{
        hideOverlap: true,
      }},
      axisLine: {{
        onZero: false,
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

  pageIndex['UVMaxyeartoyear'] = Object.keys(pageIndex).length;
  var telem = document.getElementById('UVMaxyeartoyear');
  var UVMaxchart = echarts.init(document.getElementById('UVMaxyeartoyear'));
  UVMaxchart.setOption(option);
  pageChart = {{}};
pageChart.def = option;
  pageChart.chart = UVMaxchart;
  pageCharts.push(pageChart);

  var option = {{
    series: [
     {{
    name: '2026',
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
      textStyle: {{
        color: 'var(--bs-body-color)',
      }},
    }},
    xAxis: {{
      type: 'category',
      data: monthDays[lang],
      axisLabel: {{
        hideOverlap: true,
      }},
      axisLine: {{
        onZero: false,
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

  pageIndex['radiationMaxyeartoyear'] = Object.keys(pageIndex).length;
  var telem = document.getElementById('radiationMaxyeartoyear');
  var radiationMaxchart = echarts.init(document.getElementById('radiationMaxyeartoyear'));
  radiationMaxchart.setOption(option);
  pageChart = {{}};
pageChart.def = option;
  pageChart.chart = radiationMaxchart;
  pageCharts.push(pageChart);

}}
function updateChartData() {{
  index = 0;
  series_option = {{
    series: [
      {{name: '2026',
       data: year2026_max.outTemp_wx_binding.map(arr => [moment.unix(arr[0] / 1000).utcOffset({utc_offset}).format(dateTimeFormat[lang].chart.yearToYearXaxis), arr[1]])}},
  ]}};
  pageCharts[index].chart.setOption(series_option);
  pageCharts[index].option = series_option;
  index += 1;
  series_option = {{
    series: [
      {{name: '2026',
       data: year2026_min.outTemp_wx_binding.map(arr => [moment.unix(arr[0] / 1000).utcOffset({utc_offset}).format(dateTimeFormat[lang].chart.yearToYearXaxis), arr[1]])}},
  ]}};
  pageCharts[index].chart.setOption(series_option);
  pageCharts[index].option = series_option;
  index += 1;
  series_option = {{
    series: [
      {{name: '2026',
       data: year2026_min.windchill_wx_binding.map(arr => [moment.unix(arr[0] / 1000).utcOffset({utc_offset}).format(dateTimeFormat[lang].chart.yearToYearXaxis), arr[1]])}},
  ]}};
  pageCharts[index].chart.setOption(series_option);
  pageCharts[index].option = series_option;
  index += 1;
  series_option = {{
    series: [
      {{name: '2026',
       data: year2026_max.heatindex_wx_binding.map(arr => [moment.unix(arr[0] / 1000).utcOffset({utc_offset}).format(dateTimeFormat[lang].chart.yearToYearXaxis), arr[1]])}},
  ]}};
  pageCharts[index].chart.setOption(series_option);
  pageCharts[index].option = series_option;
  index += 1;
  series_option = {{
    series: [
      {{name: '2026',
       data: year2026_avg.barometer_wx_binding.map(arr => [moment.unix(arr[0] / 1000).utcOffset({utc_offset}).format(dateTimeFormat[lang].chart.yearToYearXaxis), arr[1]])}},
  ]}};
  pageCharts[index].chart.setOption(series_option);
  pageCharts[index].option = series_option;
  index += 1;
  series_option = {{
    series: [
      {{name: '2026',
       data: year2026_max.dewpoint_wx_binding.map(arr => [moment.unix(arr[0] / 1000).utcOffset({utc_offset}).format(dateTimeFormat[lang].chart.yearToYearXaxis), arr[1]])}},
  ]}};
  pageCharts[index].chart.setOption(series_option);
  pageCharts[index].option = series_option;
  index += 1;
  series_option = {{
    series: [
      {{name: '2026',
       data: year2026_min.dewpoint_wx_binding.map(arr => [moment.unix(arr[0] / 1000).utcOffset({utc_offset}).format(dateTimeFormat[lang].chart.yearToYearXaxis), arr[1]])}},
  ]}};
  pageCharts[index].chart.setOption(series_option);
  pageCharts[index].option = series_option;
  index += 1;
  series_option = {{
    series: [
      {{name: '2026',
       data: year2026_max.outHumidity_wx_binding.map(arr => [moment.unix(arr[0] / 1000).utcOffset({utc_offset}).format(dateTimeFormat[lang].chart.yearToYearXaxis), arr[1]])}},
  ]}};
  pageCharts[index].chart.setOption(series_option);
  pageCharts[index].option = series_option;
  index += 1;
  series_option = {{
    series: [
      {{name: '2026',
       data: year2026_min.outHumidity_wx_binding.map(arr => [moment.unix(arr[0] / 1000).utcOffset({utc_offset}).format(dateTimeFormat[lang].chart.yearToYearXaxis), arr[1]])}},
  ]}};
  pageCharts[index].chart.setOption(series_option);
  pageCharts[index].option = series_option;
  index += 1;
  series_option = {{
    series: [
      {{name: '2026',
       data: year2026_sum.rain_wx_binding.map(arr => [moment.unix(arr[0] / 1000).utcOffset({utc_offset}).format(dateTimeFormat[lang].chart.yearToYearXaxis), arr[1]])}},
  ]}};
  pageCharts[index].chart.setOption(series_option);
  pageCharts[index].option = series_option;
  index += 1;
  series_option = {{
    series: [
      {{name: '2026',
       data: year2026_max.windGust_wx_binding.map(arr => [moment.unix(arr[0] / 1000).utcOffset({utc_offset}).format(dateTimeFormat[lang].chart.yearToYearXaxis), arr[1]])}},
  ]}};
  pageCharts[index].chart.setOption(series_option);
  pageCharts[index].option = series_option;
  index += 1;
  series_option = {{
    series: [
      {{name: '2026',
       data: year2026_sum.ET_wx_binding.map(arr => [moment.unix(arr[0] / 1000).utcOffset({utc_offset}).format(dateTimeFormat[lang].chart.yearToYearXaxis), arr[1]])}},
  ]}};
  pageCharts[index].chart.setOption(series_option);
  pageCharts[index].option = series_option;
  index += 1;
  series_option = {{
    series: [
      {{name: '2026',
       data: year2026_max.UV_wx_binding.map(arr => [moment.unix(arr[0] / 1000).utcOffset({utc_offset}).format(dateTimeFormat[lang].chart.yearToYearXaxis), arr[1]])}},
  ]}};
  pageCharts[index].chart.setOption(series_option);
  pageCharts[index].option = series_option;
  index += 1;
  series_option = {{
    series: [
      {{name: '2026',
       data: year2026_max.radiation_wx_binding.map(arr => [moment.unix(arr[0] / 1000).utcOffset({utc_offset}).format(dateTimeFormat[lang].chart.yearToYearXaxis), arr[1]])}},
  ]}};
  pageCharts[index].chart.setOption(series_option);
  pageCharts[index].option = series_option;
  index += 1;
}}
'''

result3 =\
'''
/* jas 1.2.0-rc03 {now} */
utc_offset = {utc_offset};
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

  aggregate_interval = 'multiyear'
  var option = {{
    series: [
    {{
      z: 100,
      type: 'line',
      smooth: true,
      symbol: 'none',
    }},
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

  pageIndex['outTempMinMaxmultiyear'] = Object.keys(pageIndex).length;
  var telem = document.getElementById('outTempMinMaxmultiyear');
  var outTempMinMaxchart = echarts.init(document.getElementById('outTempMinMaxmultiyear'));
  outTempMinMaxchart.setOption(option);
  pageChart = {{}};
pageChart.def = option;
  pageChart.chart = outTempMinMaxchart;
  pageCharts.push(pageChart);

  aggregate_interval = 'multiyear'
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

  pageIndex['barometermultiyear'] = Object.keys(pageIndex).length;
  var telem = document.getElementById('barometermultiyear');
  var barometerchart = echarts.init(document.getElementById('barometermultiyear'));
  barometerchart.setOption(option);
  pageChart = {{}};
pageChart.def = option;
  pageChart.chart = barometerchart;
  pageCharts.push(pageChart);

  aggregate_interval = 'multiyear'
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
      symbolSize: 5,
    }},
    {{
      type: 'scatter',
      symbolSize: 5,
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

  pageIndex['outHumidityMinMaxmultiyear'] = Object.keys(pageIndex).length;
  var telem = document.getElementById('outHumidityMinMaxmultiyear');
  var outHumidityMinMaxchart = echarts.init(document.getElementById('outHumidityMinMaxmultiyear'));
  outHumidityMinMaxchart.setOption(option);
  pageChart = {{}};
pageChart.def = option;
  pageChart.chart = outHumidityMinMaxchart;
  pageCharts.push(pageChart);

  aggregate_interval = 'multiyear'
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

  pageIndex['rainmultiyear'] = Object.keys(pageIndex).length;
  var telem = document.getElementById('rainmultiyear');
  var rainchart = echarts.init(document.getElementById('rainmultiyear'));
  rainchart.setOption(option);
  pageChart = {{}};
pageChart.def = option;
  pageChart.chart = rainchart;
  pageCharts.push(pageChart);

  aggregate_interval = 'multiyear'
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
      name:'  mph',
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

  pageIndex['windmultiyear'] = Object.keys(pageIndex).length;
  var telem = document.getElementById('windmultiyear');
  var windchart = echarts.init(document.getElementById('windmultiyear'));
  windchart.setOption(option);
  pageChart = {{}};
pageChart.def = option;
  pageChart.chart = windchart;
  pageCharts.push(pageChart);

  aggregate_interval = 'multiyear'
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

  pageIndex['ETmultiyear'] = Object.keys(pageIndex).length;
  var telem = document.getElementById('ETmultiyear');
  var ETchart = echarts.init(document.getElementById('ETmultiyear'));
  ETchart.setOption(option);
  pageChart = {{}};
pageChart.def = option;
  pageChart.chart = ETchart;
  pageCharts.push(pageChart);

  aggregate_interval = 'multiyear'
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

  pageIndex['UVMaxmultiyear'] = Object.keys(pageIndex).length;
  var telem = document.getElementById('UVMaxmultiyear');
  var UVMaxchart = echarts.init(document.getElementById('UVMaxmultiyear'));
  UVMaxchart.setOption(option);
  pageChart = {{}};
pageChart.def = option;
  pageChart.chart = UVMaxchart;
  pageCharts.push(pageChart);

  aggregate_interval = 'multiyear'
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

  pageIndex['radiationMaxmultiyear'] = Object.keys(pageIndex).length;
  var telem = document.getElementById('radiationMaxmultiyear');
  var radiationMaxchart = echarts.init(document.getElementById('radiationMaxmultiyear'));
  radiationMaxchart.setOption(option);
  pageChart = {{}};
pageChart.def = option;
  pageChart.chart = radiationMaxchart;
  pageCharts.push(pageChart);

}}
function updateChartData() {{
  index = 0;
  series_option = {{
    series: [
      {{name: getLabel('outTempMin'),
       data: [
               ...year2026_min.outTemp_wx_binding,
             ]}},
      {{name: getLabel('outTempMax'),
       data: [
               ...year2026_max.outTemp_wx_binding,
             ]}},
      {{name: getLabel('windchillMin'),
       data: [
               ...year2026_min.windchill_wx_binding,
             ]}},
      {{name: getLabel('heatindexMax'),
       data: [
               ...year2026_max.heatindex_wx_binding,
             ]}},
  ]}};
  pageCharts[index].chart.setOption(series_option);
  pageCharts[index].option = series_option;
  index += 1;
  series_option = {{
    series: [
      {{name: getLabel('barometer'),
       data: [
               ...year2026_avg.barometer_wx_binding,
             ]}},
  ]}};
  pageCharts[index].chart.setOption(series_option);
  pageCharts[index].option = series_option;
  index += 1;
  series_option = {{
    series: [
      {{name: getLabel('dewpointMin'),
       data: [
               ...year2026_min.dewpoint_wx_binding,
             ]}},
      {{name: getLabel('dewpointMax'),
       data: [
               ...year2026_max.dewpoint_wx_binding,
             ]}},
      {{name: getLabel('outHumidityMin'),
       data: [
               ...year2026_min.outHumidity_wx_binding,
             ]}},
      {{name: getLabel('outHumidityMax'),
       data: [
               ...year2026_max.outHumidity_wx_binding,
             ]}},
  ]}};
  pageCharts[index].chart.setOption(series_option);
  pageCharts[index].option = series_option;
  index += 1;
  series_option = {{
    series: [
      {{name: getLabel('rainRate'),
       data: [
               ...year2026_max.rainRate_wx_binding,
             ]}},
      {{name: getLabel('rain'),
       data: [
               ...year2026_sum.rain_wx_binding,
             ]}},
  ]}};
  pageCharts[index].chart.setOption(series_option);
  pageCharts[index].option = series_option;
  index += 1;
  series_option = {{
    series: [
      {{name: getLabel('windSpeed'),
       data: [
               ...year2026_avg.windSpeed_wx_binding,
             ]}},
      {{name: getLabel('windGust'),
       data: [
               ...year2026_max.windGust_wx_binding,
             ]}},
      {{name: getLabel('windDir'),
       data: [
               ...year2026_avg.windDir_wx_binding,
             ]}},
  ]}};
  pageCharts[index].chart.setOption(series_option);
  pageCharts[index].option = series_option;
  index += 1;
  series_option = {{
    series: [
      {{name: getLabel('ET'),
       data: [
               ...year2026_sum.ET_wx_binding,
             ]}},
  ]}};
  pageCharts[index].chart.setOption(series_option);
  pageCharts[index].option = series_option;
  index += 1;
  series_option = {{
    series: [
      {{name: getLabel('UV'),
       data: [
               ...year2026_max.UV_wx_binding,
             ]}},
  ]}};
  pageCharts[index].chart.setOption(series_option);
  pageCharts[index].option = series_option;
  index += 1;
  series_option = {{
    series: [
      {{name: getLabel('radiation'),
       data: [
               ...year2026_max.radiation_wx_binding,
             ]}},
  ]}};
  pageCharts[index].chart.setOption(series_option);
  pageCharts[index].option = series_option;
  index += 1;
}}
'''

result4 =\
'''
/* jas 1.2.0-rc03 {now} */
utc_offset = {utc_offset};
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

  aggregate_interval = 'mqtt'
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

  pageIndex['outTempdebug'] = Object.keys(pageIndex).length;
  var telem = document.getElementById('outTempdebug');
  var outTempchart = echarts.init(document.getElementById('outTempdebug'));
  outTempchart.setOption(option);
  pageChart = {{}};
pageChart.option = null;
pageChart.series = [];
seriesData = {{}};
seriesData.obs = "outTemp_celsius";
seriesData.name = null;
pageChart.series.push(seriesData);
seriesData = {{}};
seriesData.obs = "windchill";
seriesData.name = null;
pageChart.series.push(seriesData);
seriesData = {{}};
seriesData.obs = "heatindex";
seriesData.name = null;
pageChart.series.push(seriesData);
  pageChart.chart = outTempchart;
  pageCharts.push(pageChart);

  aggregate_interval = 'mqtt'
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

  pageIndex['outHumiditydebug'] = Object.keys(pageIndex).length;
  var telem = document.getElementById('outHumiditydebug');
  var outHumiditychart = echarts.init(document.getElementById('outHumiditydebug'));
  outHumiditychart.setOption(option);
  pageChart = {{}};
pageChart.option = null;
pageChart.series = [];
seriesData = {{}};
seriesData.obs = "dewpoint";
seriesData.name = null;
pageChart.series.push(seriesData);
seriesData = {{}};
seriesData.obs = "outHumidity";
seriesData.name = null;
pageChart.series.push(seriesData);
seriesData = {{}};
seriesData.obs = "outTemp";
seriesData.name = null;
pageChart.series.push(seriesData);
  pageChart.chart = outHumiditychart;
  pageCharts.push(pageChart);

  aggregate_interval = 'mqtt'
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

  pageIndex['barometerdebug'] = Object.keys(pageIndex).length;
  var telem = document.getElementById('barometerdebug');
  var barometerchart = echarts.init(document.getElementById('barometerdebug'));
  barometerchart.setOption(option);
  pageChart = {{}};
pageChart.option = null;
pageChart.series = [];
seriesData = {{}};
seriesData.obs = "barometer";
seriesData.name = null;
pageChart.series.push(seriesData);
  pageChart.chart = barometerchart;
  pageCharts.push(pageChart);

  aggregate_interval = 'mqtt'
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

  pageIndex['raindebug'] = Object.keys(pageIndex).length;
  var telem = document.getElementById('raindebug');
  var rainchart = echarts.init(document.getElementById('raindebug'));
  rainchart.setOption(option);
  pageChart = {{}};
pageChart.option = null;
pageChart.series = [];
seriesData = {{}};
seriesData.obs = "rainRate";
seriesData.name = null;
pageChart.series.push(seriesData);
seriesData = {{}};
seriesData.obs = "rain";
seriesData.name = null;
pageChart.series.push(seriesData);
  pageChart.chart = rainchart;
  pageCharts.push(pageChart);

  aggregate_interval = 'mqtt'
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
      name:'  mph',
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

  pageIndex['winddebug'] = Object.keys(pageIndex).length;
  var telem = document.getElementById('winddebug');
  var windchart = echarts.init(document.getElementById('winddebug'));
  windchart.setOption(option);
  pageChart = {{}};
pageChart.option = null;
pageChart.series = [];
seriesData = {{}};
seriesData.obs = "windSpeed";
seriesData.name = null;
pageChart.series.push(seriesData);
seriesData = {{}};
seriesData.obs = "windGust";
seriesData.name = null;
pageChart.series.push(seriesData);
seriesData = {{}};
seriesData.obs = "windDir";
seriesData.name = null;
pageChart.series.push(seriesData);
  pageChart.chart = windchart;
  pageCharts.push(pageChart);

  aggregate_interval = 'mqtt'
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

  pageIndex['ETdebug'] = Object.keys(pageIndex).length;
  var telem = document.getElementById('ETdebug');
  var ETchart = echarts.init(document.getElementById('ETdebug'));
  ETchart.setOption(option);
  pageChart = {{}};
pageChart.option = null;
pageChart.series = [];
seriesData = {{}};
seriesData.obs = "ET";
seriesData.name = null;
pageChart.series.push(seriesData);
  pageChart.chart = ETchart;
  pageCharts.push(pageChart);

  aggregate_interval = 'mqtt'
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

  pageIndex['UVdebug'] = Object.keys(pageIndex).length;
  var telem = document.getElementById('UVdebug');
  var UVchart = echarts.init(document.getElementById('UVdebug'));
  UVchart.setOption(option);
  pageChart = {{}};
pageChart.option = null;
pageChart.series = [];
seriesData = {{}};
seriesData.obs = "UV";
seriesData.name = null;
pageChart.series.push(seriesData);
  pageChart.chart = UVchart;
  pageCharts.push(pageChart);

  aggregate_interval = 'mqtt'
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

  pageIndex['radiationdebug'] = Object.keys(pageIndex).length;
  var telem = document.getElementById('radiationdebug');
  var radiationchart = echarts.init(document.getElementById('radiationdebug'));
  radiationchart.setOption(option);
  pageChart = {{}};
pageChart.option = null;
pageChart.series = [];
seriesData = {{}};
seriesData.obs = "radiation";
seriesData.name = null;
pageChart.series.push(seriesData);
  pageChart.chart = radiationchart;
  pageCharts.push(pageChart);

}}
function updateChartData() {{
}}
'''
