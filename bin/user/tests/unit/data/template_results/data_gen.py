#    Copyright (c) 2026 Rich Bell <bellrichm@gmail.com>
#
#    See the file LICENSE.txt for your full rights.
#

# pylint: disable=wrong-import-order
# pylint: disable=missing-module-docstring, missing-class-docstring, missing-function-docstring
# pylint: disable=invalid-name

# pylint: disable=line-too-long
# pylint: disable=too-many-lines

result_data_minimal_configuration = \
'''


/* jas foo3 foo4 */

foo6foo5 = {};

minMaxObs = [];
thisDateObsList = [];
var current = {};
var current_observation = null;
var current_aqi = null;
var current_alert =null;
var forecasts = [];

var foo6startDate;
var foo6endDate;
var foo6startTimestamp;
var foo6endTimestamp;
var startMinMaxTimestamp;
var endinMaxTimestamp;

var updateDate;

function getDatafoo6(pageDataString) {
    pageData = JSON.parse(pageDataString);




    forecasts = pageData.forecasts
    foo6startDate = moment(pageData.startDate);
    foo6endDate = moment(pageData.endDate);
    foo6startTimestamp = pageData.startTimestamp;
    foo6endTimestamp = pageData.endTimestamp;
    startMinMaxDate = moment(pageData.startDate);
    endMinMaxDate = moment(pageData.endDate);
    startMinMaxTimestamp = pageData.startTimestamp;
    endMinMaxTimestamp = pageData.endTimestamp;

    var foo6endTimestamp_bar1 =  pageData.endTimestamp_bar1;

    foo6data_binding.obs1_unit_name_foo7 = pageData.foo6data_binding.obs1_unit_name_foo7;
    foo6data_binding_obs1_unit_name_foo7_dateTime = [].concat(foo6data_binding.obs1_unit_name_foo7.map(arr => arr[0]));
    foo6data_binding_obs1_unit_name_foo7_data = [].concat(foo6data_binding.obs1_unit_name_foo7.map(arr => arr[1]));





    mqttData2 = {};
    mqttData = {};




}

  
'''

result_display_aeris_observation = \
'''


/* jas foo3 foo4 */

foo6foo5 = {};

minMaxObs = [];
thisDateObsList = [];
var current = {};
var current_observation = null;
var current_aqi = null;
var current_alert =null;
var forecasts = [];

var foo6startDate;
var foo6endDate;
var foo6startTimestamp;
var foo6endTimestamp;
var startMinMaxTimestamp;
var endinMaxTimestamp;

var updateDate;

function getDatafoo6(pageDataString) {
    pageData = JSON.parse(pageDataString);



if (pageData.alerts) {
        current_alert = getText(pageData.alerts[0].type);
        current_alert_detail = getText(pageData.alerts[0].bodyFull);
    }

    forecasts = pageData.forecasts
    foo6startDate = moment(pageData.startDate);
    foo6endDate = moment(pageData.endDate);
    foo6startTimestamp = pageData.startTimestamp;
    foo6endTimestamp = pageData.endTimestamp;
    startMinMaxDate = moment(pageData.startDate);
    endMinMaxDate = moment(pageData.endDate);
    startMinMaxTimestamp = pageData.startTimestamp;
    endMinMaxTimestamp = pageData.endTimestamp;

    var foo6endTimestamp_bar1 =  pageData.endTimestamp_bar1;

    foo6data_binding.obs1_unit_name_foo7 = pageData.foo6data_binding.obs1_unit_name_foo7;
    foo6data_binding_obs1_unit_name_foo7_dateTime = [].concat(foo6data_binding.obs1_unit_name_foo7.map(arr => arr[0]));
    foo6data_binding_obs1_unit_name_foo7_data = [].concat(foo6data_binding.obs1_unit_name_foo7.map(arr => arr[1]));




    var mqtt_enabled = false;
    updateDate = pageData.updateDate;


    current.observations = new Map();
    currentData = JSON.parse(pageData.currentData);


    mqttData2 = {};
    mqttData = {};




}

  
'''

result_display_aeris_alert = \
'''


/* jas foo3 foo4 */

foo6foo5 = {};

minMaxObs = [];
thisDateObsList = [];
var current = {};
var current_observation = null;
var current_aqi = null;
var current_alert =null;
var forecasts = [];

var foo6startDate;
var foo6endDate;
var foo6startTimestamp;
var foo6endTimestamp;
var startMinMaxTimestamp;
var endinMaxTimestamp;

var updateDate;

function getDatafoo6(pageDataString) {
    pageData = JSON.parse(pageDataString);



if (pageData.alerts) {
        current_alert = getText(pageData.alerts[0].type);
        current_alert_detail = getText(pageData.alerts[0].bodyFull);
    }

    forecasts = pageData.forecasts
    foo6startDate = moment(pageData.startDate);
    foo6endDate = moment(pageData.endDate);
    foo6startTimestamp = pageData.startTimestamp;
    foo6endTimestamp = pageData.endTimestamp;
    startMinMaxDate = moment(pageData.startDate);
    endMinMaxDate = moment(pageData.endDate);
    startMinMaxTimestamp = pageData.startTimestamp;
    endMinMaxTimestamp = pageData.endTimestamp;

    var foo6endTimestamp_bar1 =  pageData.endTimestamp_bar1;

    foo6data_binding.obs1_unit_name_foo7 = pageData.foo6data_binding.obs1_unit_name_foo7;
    foo6data_binding_obs1_unit_name_foo7_dateTime = [].concat(foo6data_binding.obs1_unit_name_foo7.map(arr => arr[0]));
    foo6data_binding_obs1_unit_name_foo7_data = [].concat(foo6data_binding.obs1_unit_name_foo7.map(arr => arr[1]));




    var mqtt_enabled = false;
    updateDate = pageData.updateDate;


    current.observations = new Map();
    currentData = JSON.parse(pageData.currentData);


    mqttData2 = {};
    mqttData = {};




}

  
'''

result_data_thisdate_no_aggregate = \
'''


/* jas foo3 foo4 */

foo6foo5 = {};

minMaxObs = [];
thisDateObsList = [];
var current = {};
var current_observation = null;
var current_aqi = null;
var current_alert =null;
var forecasts = [];

var foo6startDate;
var foo6endDate;
var foo6startTimestamp;
var foo6endTimestamp;
var startMinMaxTimestamp;
var endinMaxTimestamp;

var updateDate;

function getDatafoo6(pageDataString) {
    pageData = JSON.parse(pageDataString);




    forecasts = pageData.forecasts
    foo6startDate = moment(pageData.startDate);
    foo6endDate = moment(pageData.endDate);
    foo6startTimestamp = pageData.startTimestamp;
    foo6endTimestamp = pageData.endTimestamp;
    startMinMaxDate = moment(pageData.startDate);
    endMinMaxDate = moment(pageData.endDate);
    startMinMaxTimestamp = pageData.startTimestamp;
    endMinMaxTimestamp = pageData.endTimestamp;

    var foo6endTimestamp_bar1 =  pageData.endTimestamp_bar1;

    foo6data_binding.obs1_unit_name_foo7 = pageData.foo6data_binding.obs1_unit_name_foo7;
    foo6data_binding_obs1_unit_name_foo7_dateTime = [].concat(foo6data_binding.obs1_unit_name_foo7.map(arr => arr[0]));
    foo6data_binding_obs1_unit_name_foo7_data = [].concat(foo6data_binding.obs1_unit_name_foo7.map(arr => arr[1]));



    thisDateObs = [];
    maxDecimals = null;

    thisDateObsDetail = {};
    thisDateObsDetail.label = "obs-label";
    thisDateObsDetail.maxDecimals = maxDecimals;
    thisDateObsDetail.dataArray = foo6min.obs1_foo1;
    thisDateObsDetail.id = "obs1_thisdate_min";
    thisDateObs.push(thisDateObsDetail);

    thisDateObsDetail = {};
    thisDateObsDetail.label = "obs-label";
    thisDateObsDetail.maxDecimals = maxDecimals;
    thisDateObsDetail.dataArray = foo6max.obs1_foo1;
    thisDateObsDetail.id = "obs1_thisdate_max";
    thisDateObs.push(thisDateObsDetail);


    thisDateObsList.push(thisDateObs);



    mqttData2 = {};
    mqttData = {};




}

  
'''

result_data_thisdate_has_aggregate = \
'''


/* jas foo3 foo4 */

foo6foo5 = {};

minMaxObs = [];
thisDateObsList = [];
var current = {};
var current_observation = null;
var current_aqi = null;
var current_alert =null;
var forecasts = [];

var foo6startDate;
var foo6endDate;
var foo6startTimestamp;
var foo6endTimestamp;
var startMinMaxTimestamp;
var endinMaxTimestamp;

var updateDate;

function getDatafoo6(pageDataString) {
    pageData = JSON.parse(pageDataString);




    forecasts = pageData.forecasts
    foo6startDate = moment(pageData.startDate);
    foo6endDate = moment(pageData.endDate);
    foo6startTimestamp = pageData.startTimestamp;
    foo6endTimestamp = pageData.endTimestamp;
    startMinMaxDate = moment(pageData.startDate);
    endMinMaxDate = moment(pageData.endDate);
    startMinMaxTimestamp = pageData.startTimestamp;
    endMinMaxTimestamp = pageData.endTimestamp;

    var foo6endTimestamp_bar1 =  pageData.endTimestamp_bar1;

    foo6data_binding.obs1_unit_name_foo7 = pageData.foo6data_binding.obs1_unit_name_foo7;
    foo6data_binding_obs1_unit_name_foo7_dateTime = [].concat(foo6data_binding.obs1_unit_name_foo7.map(arr => arr[0]));
    foo6data_binding_obs1_unit_name_foo7_data = [].concat(foo6data_binding.obs1_unit_name_foo7.map(arr => arr[1]));



    thisDateObs = [];
    maxDecimals = null;

    thisDateObsDetail = {};
    thisDateObsDetail.label = "obs-label";
    thisDateObsDetail.maxDecimals = maxDecimals;
    thisDateObsDetail.dataArray = foo6type-1.obs1_foo1;
    thisDateObsDetail.id = "obs1_thisdate_type-1";
    thisDateObs.push(thisDateObsDetail);

    thisDateObsList.push(thisDateObs);



    mqttData2 = {};
    mqttData = {};




}

  
'''
