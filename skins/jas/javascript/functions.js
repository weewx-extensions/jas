// Copyright (c) 2026 Rich Bell <bellrichm@gmail.com>
// See the file LICENSE.txt for your rights.

// Update the min/max observations
function updateMinMax(startTimestamp, endTimestamp) {
    jasLogDebug("Min start: ", startTimestamp);
    jasLogDebug("Max start: ", endTimestamp);
    // ToDo: optimize to only get index once for all observations?
    minMaxObs.forEach(function (minMaxObsData) {
        startIndex = minMaxObsData.minDateTimeArray.findIndex(element => element == startTimestamp);
        endIndex = minMaxObsData.minDateTimeArray.findIndex(element => element == endTimestamp);
        if (startIndex < 0) {
            startIndex = 0;
        }
        if (endIndex < 0) {
            endIndex = minMaxObsData.minDateTimeArray.length - 1;
        }
        if (startIndex == endIndex) {
            minIndex = startIndex;
            maxIndex = endIndex;
        } else {
            minIndex = minMaxObsData.minDataArray.indexOf(Math.min(...minMaxObsData.minDataArray.slice(startIndex, endIndex + 1).filter(obs => obs != null)));
            maxIndex = minMaxObsData.maxDataArray.indexOf(Math.max(...minMaxObsData.maxDataArray.slice(startIndex, endIndex + 1)));
        }

        min = minMaxObsData.minDataArray[minIndex];
        max = minMaxObsData.maxDataArray[maxIndex];
        if (minMaxObsData.maxDecimals) {
            min = min.toFixed(minMaxObsData.maxDecimals);
            max = max.toFixed(minMaxObsData.maxDecimals);
        }
        min = Number(min).toLocaleString(lang);
        max = Number(max).toLocaleString(lang);
        min = min + minMaxObsData.label;
        max = max + minMaxObsData.label;

        minDate = moment.unix(minMaxObsData.minDateTimeArray[minIndex] / 1000).utcOffset(utcOffset).format(dateTimeFormat[lang].chart[minFormat].label);
        maxDate = moment.unix(minMaxObsData.maxDateTimeArray[maxIndex] / 1000).utcOffset(utcOffset).format(dateTimeFormat[lang].chart[maxFormat].label);

        observation_element = document.getElementById(minMaxObsData.minId);
        observation_element.innerHTML = min + "<br>" + minDate;
        observation_element = document.getElementById(minMaxObsData.maxId);
        observation_element.innerHTML = max + "<br>" + maxDate;
    });
}

function setupZoomDate() {
    zoomDateRangePicker = new DateRangePicker("zoomdatetimerange-input",
        {
            minDate: startMinMaxDate,
            maxDate: endMinMaxDate,
            startDate: startMinMaxDate,
            endDate: endMinMaxDate,
            locale: {
                format: dateTimeFormat[lang].datePicker,
                applyLabel: getText("datepicker_apply_label"),
                cancelLabel: getText("datepicker_cancel_label"),
            },
        },
        function (start, end, label) {
            // Update all charts with selected date/time and min/max values
            pageCharts.forEach(function (pageChart) {
                pageChart.chart.dispatchAction({ type: "dataZoom", startValue: start.unix() * 1000, endValue: end.unix() * 1000 });
            });

            updateMinMax(start.unix() * 1000, end.startOf("day").unix() * 1000);
        }
    );
}

function setupThisDate() {
    var thisDateRangePicker = new DateRangePicker("thisdatetimerange-input",
        {
            singleDatePicker: true,
            minDate: startMinMaxDate,
            maxDate: endMinMaxDate,
            locale: {
                format: dateTimeFormat[lang].datePicker,
                applyLabel: getText("datepicker_apply_label"),
                cancelLabel: getText("datepicker_cancel_label"),
            },
        },
        function (start, end, label) {
            updateThisDate(start.unix() * 1000);
        }
    );

    var lastDay = new Date(selectedYear, selectedMonth, 0).getDate();
    var selectedDay = new Date().getDate();
    if (selectedDay > lastDay) {
        selectedDay = lastDay;
    }

    var selectedDate = Date.UTC(selectedYear, selectedMonth - 1, selectedDay) / 1000 - (utcOffset * 60);

    thisDateRangePicker.setStartDate(moment.unix(selectedDate).utcOffset(utcOffset));
    thisDateRangePicker.setEndDate(moment.unix(selectedDate).utcOffset(utcOffset));
    updateThisDate(selectedDate * 1000);
}

function setupPageRefresh() {
    // Set a timer to reload the iframe/page.
    var currentDate = new Date();
    var futureDate = new Date();
    futureDate.setTime(futureDate.getTime() + millisecondsWait);
    var futureTimestamp = Math.floor(futureDate.getTime() / millisecondsWait) * millisecondsWait;
    var timeout = futureTimestamp - currentDate.getTime() + millisecondsDelay;
    setTimeout(function () { handleRefreshData(null); setupPageRefresh(); }, timeout);
}

// Handle reset button of zoom control
function resetRange() {
    zoomDateRangePicker.setStartDate(startMinMaxDate);
    zoomDateRangePicker.setEndDate(endMinMaxDate);
    pageCharts.forEach(function (pageChart) {
        pageChart.chart.dispatchAction({ type: "dataZoom", startValue: startMinMaxTimestamp, endValue: endMinMaxTimestamp });
    });
    updateMinMax(startMinMaxTimestamp, endMinMaxTimestamp);
}

// Handle event messages of type "mqtt".
var test_obj = null; // Not a great idea to be global, but makes remote debugging easier.
function updateCurrentMQTT(topic, test_obj) {
    fieldMap = topics.get(topic);
    // Handle the "header" section of current observations.
    header = JSON.parse(sessionStorage.getItem("header"));
    if (header) {
        observation = fieldMap.get(header.name);
        if (observation === undefined) {
            mqttValue = test_obj[header.name];
        }
        else {
            mqttValue = test_obj[observation];
        }

        if (mqttValue != undefined) {
            if (headerMaxDecimals) {
                mqttValue = Number(mqttValue).toFixed(headerMaxDecimals);
            }
            if (!isNaN(mqttValue)) {
                header.value = Number(mqttValue).toLocaleString(lang);
            }
        }

        if (test_obj[header.unit]) {
            header.unit = test_obj[header.unit];
        }
        sessionStorage.setItem("header", JSON.stringify(header));
        headerElem = document.getElementById(header.name);
        if (headerElem) {
            headerElem.innerHTML = header.value + header.unit;
        }
        headerModalElem = document.getElementById("currentModalTitle");
        if (headerModalElem) {
            headerModalElem.innerHTML = header.value + header.unit;
        }
    }

    // Process each observation in the "current" section.
    observations = [];
    if (sessionStorage.getItem("observations")) {
        observations = sessionStorage.getItem("observations").split(",");
    }

    observations.forEach(function (observation) {
        obs = fieldMap.get(observation);
        if (obs === undefined) {
            obs = observation;
        }

        observationInfo = current.observations.get(observation);
        if (observationInfo.mqtt && test_obj[obs]) {
            data = JSON.parse(sessionStorage.getItem(observation));
            data.value = Number(test_obj[obs]);
            if (observationInfo.maxDecimals != null) {
                data.value = data.value.toFixed(observationInfo.maxDecimals);
            }
            if (!isNaN(data.value)) {
                data.value = Number(data.value).toLocaleString(lang);
            }
            sessionStorage.setItem(observation, JSON.stringify(data));

            dataElem = document.getElementById(data.name + "_value");
            if (dataElem) {
                dataElem.innerHTML = data.value + data.unit;
            }
            if (data.modalLabel) {
                document.getElementById(data.modalLabel).innerHTML = data.value + data.unit;
            }
        }
    });

    // And the "current" section date/time.
    if (test_obj.dateTime) {
        sessionStorage.setItem("updateDate", test_obj.dateTime * 1000);
        timeElem = document.getElementById("updateDateDiv");
        if (timeElem) {
            timeElem.innerHTML = moment.unix(test_obj.dateTime).utcOffset(utcOffset).format(dateTimeFormat[lang].current);
        }
        timeModalElem = document.getElementById("updateModalDate");
        if (timeModalElem) {
            timeModalElem.innerHTML = moment.unix(test_obj.dateTime).utcOffset(utcOffset).format(dateTimeFormat[lang].current);
        }
    }
}

function updateCurrentObservations() {
    if (jasOptions.currentHeader) {
        //ToDo: switch to allow non mqtt header data? similar to the observation section
        if (sessionStorage.getItem("header") === null || !jasOptions.MQTTConfig) {
            sessionStorage.setItem("header", JSON.stringify(current.header));
        }
        header = JSON.parse(sessionStorage.getItem("header"));
        document.getElementById(jasOptions.currentHeader).innerHTML = header.value + header.unit;
    }

    if (jasOptions.displayAerisObservation) {
        document.getElementById("currentObservation").innerHTML = current_observation;
    }

    if (jasOptions.displayAerisAQI) {
        document.getElementById("currentAQI").innerHTML = current_aqi;
    }

    if (jasOptions.displayAerisAlert) {
        document.getElementById("currentAlert").innerHTML = current_alert;
    }

    // ToDo: cleanup, perhaps put observation data into an array and store that
    // ToDo: do a bit more in cheetah?
    observations = [];
    for (var [observation, data] of current.observations) {
        observations.push(observation);
        if (sessionStorage.getItem(observation) === null || !jasOptions.MQTTConfig || !data.mqtt) {
            sessionStorage.setItem(observation, JSON.stringify(data));
        }
        obs = JSON.parse(sessionStorage.getItem(observation));

        document.getElementById(obs.name + "_value").innerHTML = obs.value + obs.unit;
    }
    sessionStorage.setItem("observations", observations.join(","));

    if (sessionStorage.getItem("updateDate") === null || !jasOptions.MQTTConfig) {
        sessionStorage.setItem("updateDate", updateDate);
    }
    document.getElementById("updateDateDiv").innerHTML = moment.unix(sessionStorage.getItem("updateDate") / 1000).utcOffset(utcOffset).format(dateTimeFormat[lang].current);
}

document.addEventListener("DOMContentLoaded", function (event) {
    console.debug(Date.now().toString() + " DOMContentLoaded start");
    setupPage();
    console.debug(Date.now().toString() + " setupPage done");
    if (pageName != "about") {
        setupCharts();
    }
    console.debug(Date.now().toString() + " setupCharts done");
    DOMLoaded = true;
    console.debug(Date.now().toString() + " DOMContentLoaded end");
});

function updateData() {
    console.debug(Date.now().toString() + " updateData start");
    if (jasOptions.minmax) {
        updateMinMax(startMinMaxTimestamp, endMinMaxTimestamp);
    }

    // Set up the date/time picker
    if (jasOptions.zoomcontrol) {
        setupZoomDate();
    }

    if (jasOptions.thisdate) {
        setupThisDate();
    }

    if (jasOptions.current) {
        updateCurrentObservations();
    }
    console.debug(Date.now().toString() + " updateCurrentObservations done");
    if (jasOptions.forecast) {
        updateForecasts();
    }
    console.debug(Date.now().toString() + " updateForecasts done");
    updateChartData();
    console.debug(Date.now().toString() + " updateChartData done");
    console.debug(Date.now().toString() + " updateData end");

}

function setupPage(pageDataString) {
    console.debug(Date.now().toString() + " setupPage start");
    theme = sessionStorage.getItem("theme");
    if (!theme) {
        theme = defaultTheme;
    }
    console.debug(Date.now().toString() + " getTheme done");
    setTheme(theme);
    console.debug(Date.now().toString() + " setTheme done");
    updateTexts();
    console.debug(Date.now().toString() + " updateTexts done");
    updateLabels();
    console.debug(Date.now().toString() + " updateLabels done");

    if (jasOptions.refresh) {
        setupPageRefresh();
    }

    console.debug(Date.now().toString() + " setupPage end");
};

window.addEventListener("load", function (event) {
    console.debug(Date.now().toString() + " onLoad start");
    setIframeSrc();
    if (dataLoaded) {
        pageLoaded = true;
        updateData();
    }

    modalChart = null;
    var chartModal = document.getElementById("chartModal");

    chartModal.addEventListener("shown.bs.modal", function (event) {
        var titleElem = document.getElementById("chartModalTitle");
        titleElem.innerText = getText(event.relatedTarget.getAttribute("data-bs-title"));
        var divelem = document.getElementById("chartModalBody");
        modalChart = echarts.init(divelem);

        var chartId = event.relatedTarget.getAttribute("data-bs-chart");
        index = pageIndex[chartId];
        option = pageCharts[index]["def"];
        modalChart.setOption(option);
        modalChart.setOption(pageCharts[index]["option"]);
        resizeChart(modalChart, elemHeight = divelem.getAttribute("jasHeight") -
            4 * document.getElementById("chartModalHeader").clientHeight -
            document.getElementById("chartModalFooter").clientHeight);
    })

    chartModal.addEventListener("hidden.bs.modal", function (event) {
        modalChart.dispose();
        modalChart = null;

        bootstrap.Modal.getInstance(document.getElementById("chartModal")).dispose();
    })

    if (jasOptions.current) {
        var currentModal = document.getElementById("currentModal");
        currentModal.addEventListener("shown.bs.modal", function (event) {
            headerModalElem = document.getElementById("currentModalTitle");
            if (headerModalElem) {
                headerModalElem.innerHTML = header.value + header.unit;
            }

            if (jasOptions.displayAerisObservation) {
                document.getElementById("currentObservationModal").innerHTML = current_observation;
            }
            if (jasOptions.displayAerisAQI) {
                document.getElementById("currentAQIModal").innerHTML = current_aqi;
            }
            if (jasOptions.displayAerisAlert) {
                document.getElementById("currentAlertModal").innerHTML = current_alert;
            }
            // Process each observation in the "current" section.
            observations = [];
            if (sessionStorage.getItem("observations")) {
                observations = sessionStorage.getItem("observations").split(",");
            }

            observations.forEach(function (observation) {
                obs = JSON.parse(sessionStorage.getItem(observation));
                if (obs.modalLabel) {
                    document.getElementById(obs.modalLabel).innerHTML = obs.value + obs.unit;
                }
            });

            var updateDate = sessionStorage.getItem("updateDate") / 1000;
            timeElem = document.getElementById("updateModalDate");
            if (timeElem) {
                timeElem.innerHTML = moment.unix(updateDate).utcOffset(utcOffset).format(dateTimeFormat[lang].current);
            }
        })

        currentModal.addEventListener("hidden.bs.modal", function (event) {
            bootstrap.Modal.getInstance(document.getElementById("currentModal")).dispose();
        })

        if (jasOptions.displayAerisAlert) {
            var alertModal = document.getElementById("alertModal");
            alertModal.addEventListener("shown.bs.modal", function (event) {
                document.getElementById("alertDetailModal").innerHTML = current_alert_detail;
            })

            alertModal.addEventListener("hidden.bs.modal", function (event) {
                bootstrap.Modal.getInstance(document.getElementById("alertModal")).dispose();
            })
        }
    }

    // Todo: create functions for code in the if statements
    // Tell the parent page the iframe size
    message = {};
    message.kind = "resize";
    message.message = {};
    message.message = { height: document.body.scrollHeight, width: document.body.scrollWidth };
    // window.top refers to parent window
    window.top.postMessage(message, "*");

    // When the iframe size changes, let the parent page know
    const myObserver = new ResizeObserver(entries => {
        entries.forEach(entry => {
            message = {};
            message.kind = "resize";
            message.message = {};
            message.message = { height: document.body.scrollHeight, width: document.body.scrollWidth };
            // window.top refers to parent window
            window.top.postMessage(message, "*");
        });
    });
    myObserver.observe(document.body);

    message = {};
    message.kind = "loaded";
    message.message = {};
    // window.top refers to parent window
    window.top.postMessage(message, "*");
    console.debug(Date.now().toString() + " onLoad End");
});

function setIframeSrc() {
    url = "../dataload/" + pageName2 + ".html";
    if (bustCache) {
        url = url + "?ts=" + Date.now();
    }

    document.getElementById("data-iframe").src = url;
}

function jasShow(data) {
    return window[data]
}

function updatelogLevel(logLevel) {
    jasLogDebug = () => { };
    jasLogInfo = () => { };
    jasLogWarn = () => { };
    jasLogError = () => { };

    switch (logLevel) {
        case "1":
            jasLogDebug = (prefix, info) => { console.debug(prefix + JSON.stringify(info)); };
        case "2":
            jasLogInfo = (prefix, info) => { console.info(prefix + JSON.stringify(info)); };
        case "3":
            jasLogWarn = (prefix, info) => { console.warn(prefix + JSON.stringify(info)); };
        case "4":
            jasLogError = (prefix, info) => { console.error(prefix + JSON.stringify(info)); };
    }
}

updatelogLevel(logLevel);

// ToDo: make a dictionary of dictionaries
var pageCharts = [];
var pageIndex = {};

// Ensure that the height of charts is consistent ratio of the width.
function refreshSizes() {
    radarElem = document.getElementById("radar");
    if (radarElem) {
        // Match the height of charts 
        height = radarElem.offsetWidth / 1.618;
        height = height + "px";
        radarElem.style.height = height;
    }

    for (var index in pageCharts) {
        resizeChart(pageCharts[index].chart);
    }
}

function resizeChart(chart, elemHeight = null) {
    chartElem = chart.getDom();
    if (!elemHeight) {
        height = chartElem.offsetWidth / 1.618;
    }
    else {
        height = Math.min(height = chartElem.offsetWidth / 1.618, elemHeight);
    }
    width = Math.max(document.documentElement.clientWidth, window.innerWidth || 0);
    // width/100 is like the css variable vw
    fontSize = width / 100 * 1.5;
    // Max is 18px and min is 10px
    document.getElementsByTagName("html")[0].style.fontSize = Math.min(18, Math.max(10, fontSize)) + "px";
    height = height + "px";
    chart.resize({ width: null, height: height });
    options = chart.getOption();
    updatedOptions = {};
    if (chartElem.offsetWidth > 505) {
        percent = 1;
        legendTextStyleWidth = 70;
        legendIcon = 'roundRect';
    }
    else if (chartElem.offsetWidth > 350) {
        percent = 2 / 3;
        legendTextStyleWidth = 70;
        legendIcon = 'roundRect';
    }
    else if (chartElem.offsetWidth > 300) {
        percent = 1 / 2;
        legendTextStyleWidth = 70;
        legendIcon = 'roundRect';
    }
    else {
        percent = 1 / 2;
        legendTextStyleWidth = 20;
        legendIcon = 'none';
    }

    updatedOptions.toolbox = {};
    updatedOptions.toolbox.itemSize = Math.round(15 * percent);
    updatedOptions.toolbox.showTitle = false
    updatedOptions.tooltip = {};
    updatedOptions.tooltip.textStyle = {};
    updatedOptions.tooltip.textStyle.fontSize = Math.round(14 * percent);
    updatedOptions.axisPointer = {};
    updatedOptions.axisPointer.label = {};
    updatedOptions.axisPointer.label.fontSize = Math.round(12 * percent);
    updatedOptions.legend = {};
    updatedOptions.legend.itemHeight = Math.round(14 * percent);
    updatedOptions.legend.itemWidth = Math.round(25 * percent);
    updatedOptions.legend.textStyle = {};
    updatedOptions.legend.textStyle.fontSize = Math.round(12 * percent);
    if (options.legend[0].type == 'scroll') {
        updatedOptions.legend.pageIconSize = Math.round(15 * percent);
        updatedOptions.legend.pageTextStyle = {};
        updatedOptions.legend.pageTextStyle.fontSize = Math.round(12 * percent);
    }
    if ('xAxis' in options) {
        updatedOptions.xAxis = {};
        updatedOptions.xAxis.axisLabel = {};
        updatedOptions.xAxis.axisLabel.fontSize = Math.round(12 * percent);
        updatedOptions.yAxis = [];
        for (let i = 0; i < options.yAxis.length; i++) {
            updatedOptions.yAxis[i] = {};
            updatedOptions.yAxis[i].axisLabel = {};
            updatedOptions.yAxis[i].axisLabel.fontSize = Math.round(12 * percent);
            updatedOptions.yAxis[i].nameTextStyle = {};
            updatedOptions.yAxis[i].nameTextStyle.fontSize = Math.round(12 * percent);
        }
    }
    if ('angleAxis' in options) {
        updatedOptions.legend.textStyle.width = legendTextStyleWidth;
        updatedOptions.legend.icon = legendIcon;
        updatedOptions.angleAxis = {};
        updatedOptions.angleAxis.axisLabel = {};
        updatedOptions.angleAxis.axisLabel.fontSize = Math.round(12 * percent);
    }

    chart.setOption(updatedOptions);
}

function getLogLevel() {
    return "Sub-page log level: " + sessionStorage.getItem("logLevel")
}

function setLogLevel(logLevel) {
    sessionStorage.setItem("logLevel", logLevel);
    updatelogLevel(logLevel.toString());
    return "Sub-page log level: " + sessionStorage.getItem("logLevel")
}

// Handle event messages of type "setTheme".
function setTheme(theme) {
    buttons = document.getElementsByClassName("btn");
    if (theme == 'dark') {
        for (var i = 0; i < buttons.length; i++) {
            buttons[i].classList.remove("btn-dark");
            buttons[i].classList.add("btn-light");
        }
    }
    else {
        for (var i = 0; i < buttons.length; i++) {
            buttons[i].classList.remove("btn-light");
            buttons[i].classList.add("btn-dark");
        }
    }

    if (document.documentElement.getAttribute('data-bs-theme') == theme) {
        return;
    }
    document.documentElement.setAttribute('data-bs-theme', theme);
    const style = getComputedStyle(document.body);
    bsBodyColor = style.getPropertyValue("--bs-body-color");

    textColor = {
        textStyle: {
            color: bsBodyColor
        }
    }
    toolboxColor = {
        toolbox: {
            iconStyle: {
                borderColor: bsBodyColor
            }
        }
    }
    xAxisColor = {
        xAxis: {
            axisLine: {
                lineStyle: {
                    color: bsBodyColor
                }
            }
        }
    }
    angleAxisColor = {
        angleAxis: {
            axisLine: {
                lineStyle: {
                    color: bsBodyColor
                }
            }
        }
    }

    for (var index in pageCharts) {
        options = pageCharts[index].chart.getOption();
        pageCharts[index].chart.setOption(textColor);
        pageCharts[index].chart.setOption(toolboxColor);
        if ('xAxis' in options) {
            pageCharts[index].chart.setOption(xAxisColor);
        }
        if ('angleAxis' in options) {
            pageCharts[index].chart.setOption(angleAxisColor);
        }
    }

}

// Handle event messages of type "lang".
function handleLang(lang) {
    sessionStorage.setItem("currentLanguage", lang);
    window.location.reload(true);
}

// Handle event messages of type "resize".
function handleResize(message) {
    var divelem = document.getElementById('chartModalBody');
    divelem.setAttribute('jasHeight', message.height)
    if (modalChart) {
        resizeChart(modalChart, elemHeight = message.height -
            4 * document.getElementById('chartModalHeader').clientHeight -
            document.getElementById('chartModalFooter').clientHeight)
    }
}

// Handle event messages of type "log".
function handleLog(message) {
    var logDisplayElem = document.getElementById("logDisplay");
    if (logDisplayElem) {
        logDisplayElem.innerHTML = message + "\\n<br>" + logDisplayElem.innerHTML;
    }
}

// Handle event messages of type "refreshData".
function handleRefreshData(message) {
    setIframeSrc();
}

// Handle event messages of type "scroll".
function handleScroll(message) {
    document.getElementById('chartModal').style.top = message.currentScroll + 'px';
}

// Handle event messages of type "dataLoaded".
function handleDataLoaded(message) {
    console.debug(Date.now().toString() + " handleDataLoaded start");

    getDataFunction(message);
    console.debug(Date.now().toString() + " getData done");
    dataLoaded = true;
    if (DOMLoaded) {
        pageLoaded = true;
        updateData();
    }
    console.debug(Date.now().toString() + " handleDataLoaded end");
}

function handleMQTT(message) {
    test_obj = JSON.parse(message.payload);

    jasLogDebug("test_obj: ", test_obj);
    jasLogDebug("sessionStorage: ", sessionStorage);
    // ToDo - there seems to be a timing issue and somtimes topics is not set before this call
    if (typeof topics === 'undefined') {
        return;
    }
    //jasLogDebug("topics: ", Object.fromEntries(topics));
    // ToDo - only exists on pages with "current" section
    //jasLogDebug("current.observations: ", Object.fromEntries(current.observations));

    if (jasOptions.current && jasOptions.pageMQTT) {
        updateCurrentMQTT(message.topic, test_obj);
    }

    // Proof of concept, charting MQTT data
    for (obs in test_obj) {
        if (obs in mqttData2) {
            if (mqttData2[obs].length >= 1800) {
                mqttData2[obs].shift;
            }
            mqttData2[obs].push([parseInt(test_obj.dateTime) * 1000, parseFloat(test_obj[obs])]);
        }
    }

    pageCharts.forEach(function (pageChart) {
        if (pageChart.option === null) {
            echartSeries = [];
            pageChart.series.forEach(function (series) {
                seriesData = {};
                seriesData.data = mqttData2[series.obs];
                seriesData.name = series.name;
                if (seriesData.name == null) {
                    seriesData.name = getLabel(series.obs);
                }
                echartSeries.push(seriesData);
            });
            pageChart.chart.setOption({ series: echartSeries });
        }
    });
}

// Get the observation for timeSramp
function getObservation(timeStamp, observations) {
    var array_result = observations.filter(function (v, i) { return v[0] === timeStamp; });
    if (array_result.length > 0) {
        return array_result[0][1];
    }

    if (observations[0]) {
        return observations[0][1];
    }

    return null;
}

// Update the "on this date" observations with observations at timeStamp
function updateThisDate(timeStamp) {
    thisDateObsList.forEach(function (thisDateObs) {
        thisDateObs.forEach(function (thisDateObsDetail) {
            obs = getObservation(timeStamp, thisDateObsDetail.dataArray);
            if (obs && thisDateObsDetail.maxDecimals) {
                obs = obs.toFixed(thisDateObsDetail.maxDecimals);
            }

            // ToDo: Note, the value 'null, returns '0'. Not sure if this is desired, of some other value should be displayed
            obsValue = Number(obs).toLocaleString(lang);
            observation = document.getElementById(thisDateObsDetail.id);
            observation.innerHTML = obsValue + thisDateObsDetail.label;
        });
    });
}

function updateForecasts() {
    i = 0;
    forecasts.forEach(function (forecast) {
        observation = '';
        forecast.observation_codes.forEach(function (observationCode) {
            observation += getText(observationCode) + ' '
        });
        date = moment.unix(forecast["timestamp"]).utcOffset(utcOffset).format(dateTimeFormat[lang].forecast);
        observationId = "forecastObservation" + i;
        document.getElementById("forecastDate" + i).innerHTML = getText(forecast["day_code"]) + " " + date;
        document.getElementById("forecastObservation" + i).innerHTML = observation;
        document.getElementById("forecastTemp" + i).innerHTML = forecast["temp_min"] + " | " + forecast["temp_max"];
        document.getElementById("forecastRain" + i).innerHTML = '<i class="bi bi-droplet"></i>' + ' ' + forecast['rain'] + '%';
        document.getElementById('forecastWind' + i).innerHTML = '<i class="bi bi-wind"></i>' + ' ' + forecast['wind_min'] + ' | ' + forecast['wind_max'] + ' ' + forecast['wind_unit'];
        i += 1;
    });
}

window.addEventListener("onresize", function () {
    message = {};
    message.kind = "resize";
    message.message = {};
    message.message = { height: document.body.scrollHeight, width: document.body.scrollWidth };

    // window.top refers to parent window
    window.top.postMessage(message, "*");
});

window.addEventListener("message",
    function (e) {
        // Running directly from the file system has some strangeness
        if (window.location.origin != "file://" && e.origin !== window.location.origin)
            return;

        message = e.data;
        if (message.kind == undefined) {
            return;
        }
        if (message.kind == "jasShow") {
            console.log(jasShow(message.message));
        }
        if (message.kind == "getLogLevel") {
            console.log(getLogLevel());
        }
        if (message.kind == "setLogLevel") {
            console.log(setLogLevel(message.message.logLevel));
        }
        if (message.kind == "lang") {
            handleLang(message.message);
        }
        if (message.kind == "dataLoaded") {
            handleDataLoaded(message.message);
        }
        if (message.kind == "mqtt") {
            handleMQTT(message.message);
        }
        if (message.kind == "setTheme") {
            setTheme(message.message);
        }
        if (message.kind == "refreshData") {
            handleRefreshData(message.message);
        }
        if (message.kind == "resize") {
            handleResize(message.message);
        }
        if (message.kind == "scroll") {
            handleScroll(message.message);
        }
        if (message.kind == "log") {
            handleLog(message.message);
        }
    },
    false
);