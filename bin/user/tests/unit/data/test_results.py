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
'''// start
selectedYear = '2026';
selectedMonth = '3';
minFormat = 'none';
maxFormat = 'none';
pageName = '{page_name}';
pageName2 = 'None';
utcOffset = {utc_offset};
defaultTheme = 'light';
bustCache = false;
pageLoaded = false;
DOMLoaded = false;
dataLoaded = false;
traceStart = Date.now();
console.debug(Date.now().toString() + ' starting');
millisecondsWait = 300000;
millisecondsDelay = 60000;
headerMaxDecimals = null;
logLevel = sessionStorage.getItem('logLevel');
if (!logLevel) {{
    logLevel = '3';
    sessionStorage.setItem('logLevel', logLevel);
}}

console.debug(Date.now().toString() + ' ending');
// end
'''

result2 = \
'''/* jas 1.2.0-rc03 {now} */
jasOptions = {{}};
jasOptions.pageMQTT = true;
jasOptions.displayAerisObservation = -false;
jasOptions.displayAerisAQI = -false;
jasOptions.displayAerisAlert = -false;
jasOptions.refresh = false;
jasOptions.zoomcontrol = false;
jasOptions.currentHeader = null;
jasOptions.current = false;
jasOptions.forecast = false;
jasOptions.minmax = false;
jasOptions.thisdate = false;
jasOptions.MQTTConfig = false;

'''
