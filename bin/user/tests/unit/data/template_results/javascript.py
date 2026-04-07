#    Copyright (c) 2026 Rich Bell <bellrichm@gmail.com>
#
#    See the file LICENSE.txt for your full rights.
#

# pylint: disable=wrong-import-order
# pylint: disable=missing-module-docstring, missing-class-docstring, missing-function-docstring
# pylint: disable=invalid-name

# pylint: disable=line-too-long
# pylint: disable=too-many-lines

results_javascript_min_configuration = \
'''  


fullNavBarWidth = 0;

indexPageLogLevel = sessionStorage.getItem('indexPageLogLevel');
if (!indexPageLogLevel) {
    indexPageLogLevel = "3";
    sessionStorage.setItem('indexPageLogLevel', indexPageLogLevel);
}

function updatelogLevel(logLevel) {
    jasLogDebug = () => {};
    jasLogInfo = () => {};
    jasLogWarn= () => {};
    jasLogError = () => {};

    switch(logLevel) {
        case "1":
            jasLogDebug = (prefix, info) => {console.debug(prefix + JSON.stringify(info));};
        case "2":
            jasLogInfo = (prefix, info) => {console.info(prefix + JSON.stringify(info));};
        case "3":
            jasLogWarn = (prefix, info) => {console.warn(prefix + JSON.stringify(info));};
        case "4":
            jasLogError = (prefix, info) => {console.error(prefix + JSON.stringify(info));};
        }
}

updatelogLevel(indexPageLogLevel);

jasLogInfo("", navigator.userAgent);
jasLogInfo("WeeWX version: ", 'foo10');
jasLogInfo("weewx-jas version: ", 'foo11');
jasLogInfo("Language setting is: ", lang);
jasLogInfo("Log level: ", indexPageLogLevel);
jasLogInfo("", "host: foo3");
jasLogInfo("", "port: foo4");
jasLogInfo("", "timeout: foo5");
jasLogInfo("", "keepAliveInterval: foo6");
jasLogInfo("", "cleanSession: foo7");
jasLogInfo("", "useSSL: foo8");
jasLogInfo("", "reconnect: foo9");

function jasShow(data)
{
  message = {};
  message.kind = 'jasShow';
  message.message = data;
   
    // When running without a webserver, there is a lot of 'strangeness'
    if (window.location.protocol == "file:") {
        targetOrigin = "*";
    }
    else {
        targetOrigin = window.location.origin;
    }      

    if (document.getElementById('child-iframe')) {
      document.getElementById('child-iframe').contentWindow.postMessage(message, targetOrigin);
    }
    else {
      window.self.postMessage(message, targetOrigin);
    }
  return "Showing..."
}

function setLogLevel(logLevel)
{
    sessionStorage.setItem("indexPageLogLevel", logLevel);
    updatelogLevel(logLevel.toString());
    //return "Set to: " + logLevel

  // Send the logLevel to the sub-pages
  message = {};
  message.kind = 'setLogLevel';
  message.message = {};
  message.message.logLevel = logLevel;
   
    // When running without a webserver, there is a lot of 'strangeness'
    if (window.location.protocol == "file:") {
        targetOrigin = "*";
    }
    else {
        targetOrigin = window.location.origin;
    }      

    if (document.getElementById('child-iframe')) {
      document.getElementById('child-iframe').contentWindow.postMessage(message, targetOrigin);
    }
    else {
      window.self.postMessage(message, targetOrigin);
    }

  return "Index page log level: " + sessionStorage.getItem("indexPageLogLevel")
}

function getLogLevel() {

  // get sub-page log level
  message = {};
  message.kind = 'getLogLevel';
  message.message = {};
   
  // When running without a webserver, there is a lot of 'strangeness'
  if (window.location.protocol == "file:") {
      targetOrigin = "*";
  }
  else {
      targetOrigin = window.location.origin;
  }      

  if (document.getElementById('child-iframe')) {
    document.getElementById('child-iframe').contentWindow.postMessage(message, targetOrigin);
  }
  else {
    window.self.postMessage(message, targetOrigin);
  }

  return "Index page log level: " + sessionStorage.getItem("indexPageLogLevel")
}

function updateTheme(themeSelection) {
  if (themeSelection.checked) {
    setTheme("dark");
  } else {
    setTheme("light");
  }
}

function setTheme(theme) {
  sessionStorage.setItem('theme', theme);
  document.documentElement.setAttribute('data-bs-theme', theme);
  buttons = document.getElementsByClassName("btn");

  if (theme == 'dark') {
    document.getElementById("themeSelection").checked = true;
    for(var i = 0; i < buttons.length; i++)
    {
      buttons[i].classList.remove("btn-dark");
      buttons[i].classList.add("btn-light");
    }
  }
  else {
    document.getElementById("themeSelection").checked = false;
    for(var i = 0; i < buttons.length; i++)
    {
      buttons[i].classList.remove("btn-light");
      buttons[i].classList.add("btn-dark");
    }
  }

  message = {};
  message.kind = 'setTheme';
  message.message = theme;
   
  // When running without a webserver, there is a lot of 'strangeness'
  if (window.location.protocol == "file:") {
      targetOrigin = "*";
  }
  else {
      targetOrigin = window.location.origin;
  }      

  if (document.getElementById('child-iframe')) {
    document.getElementById('child-iframe').contentWindow.postMessage(message, targetOrigin);
  }
  else {
    window.self.postMessage(message, targetOrigin);
  }
}

function manageNavbar() {
  parentWidth = document.getElementById('navbar').parentElement.offsetWidth
  if (fullNavBarWidth >= parentWidth) {
    document.getElementById('navbar').classList.remove('navbar-expand')
  }
  else {
    document.getElementById('navbar').classList.add('navbar-expand')
  }
}

function refreshData() {
    message = {};
    message.kind = 'refreshData';
    message.message = {};
    
    // When running without a webserver, there is a lot of 'strangeness'
    if (window.location.protocol == "file:") {
        targetOrigin = "*";
    }
    else {
        targetOrigin = window.location.origin;
    }      

    if (document.getElementById('child-iframe')) {
      document.getElementById('child-iframe').contentWindow.postMessage(message, targetOrigin);
    }
    else {
      window.self.postMessage(message, targetOrigin);
    }
}

function setIframeSrc(id, url, addQueryString) {
  console.debug(Date.now().toString() + " setIframeSrc start");
  document.querySelector("#child-iframe").style.visibility = 'hidden';
  // Set current page as the active page.
  currentPage = sessionStorage.getItem('currentPage');
  if (currentPage != url) {
    currentPageId = document.getElementById(currentPage);
    if (currentPageId) {
      currentPageId.classList.remove("active");
    }
    sessionStorage.setItem('currentPage', url);
    sessionStorage.setItem('addQueryString', addQueryString);
  }
  document.getElementById(url).classList.add("active");
  // use query string so that iframe is not cached
  full_url = url;
  if (addQueryString) {
    full_url = full_url + "?ts=" + Date.now();
  }
  document.getElementById(id).src = full_url;

  // When on the debug iframe, add the connect/disconnect buttons to the header.
  // The need to be on the parent page because the MQTT connection is on the parent. 
  if (url == 'pages/debug.html') {
    document.getElementById('connectButton').classList.remove("d-none");
    document.getElementById('disconnectButton').classList.remove("d-none");
  }
  else {
    document.getElementById('connectButton').classList.add("d-none");
    document.getElementById('disconnectButton').classList.add("d-none");      
  }
  console.debug(Date.now().toString() + " setIframeSrc end");
}

function updateLang(language) {
      var currentLanguage = sessionStorage.getItem('currentLanguage');
      if (language != currentLanguage) {
          if (currentLanguage) {
              document.getElementById(currentLanguage).classList.remove("active");
          }
          document.getElementById(language).classList.add("active");
          sessionStorage.setItem('currentLanguage', language);
      }

    lang = language;
    updateTexts();

    message = {};
    message.kind = 'lang';
    message.message = language;
    
    // When running without a webserver, there is a lot of 'strangeness'
    if (window.location.protocol == "file:") {
        targetOrigin = "*";
    }
    else {
        targetOrigin = window.location.origin;
    }      

    if (document.getElementById('child-iframe')) {
      document.getElementById('child-iframe').contentWindow.postMessage(message, targetOrigin);
    }
    else {
      window.self.postMessage(message, targetOrigin);
    }
}

// Handle a year being selected
function setYear(year) {
  // Handle 'year' and 'month' click/selections
    var url = "pages/" + year + ".html";
    setIframeSrc('child-iframe', url, false)
}

function resizeModal() {
  width = Math.max(document.documentElement.clientWidth, window.innerWidth || 0);
  height = Math.max(document.documentElement.clientHeight, window.innerHeight || 0);

  message = {};
  message.kind = 'resize';
  message.message = {};
  message.message.width = width;
  message.message.height = height - document.getElementById('navbar').clientHeight;

  // When running without a webserver, there is a lot of 'strangeness'
  if (window.location.protocol == "file:") {
      targetOrigin = "*";
  }
  else {
      targetOrigin = window.location.origin;
  }      

  iframe = document.getElementById('child-iframe')
  if (iframe) {
    iframe.contentWindow.postMessage(message, targetOrigin);
  }
  else {
    window.self.postMessage(message, targetOrigin);
  }
}

window.addEventListener("load", function (event) {
  var themes = ['light'];
  theme = sessionStorage.getItem('theme');
  if (!theme) {
    if (window.matchMedia('(prefers-color-scheme: dark)').media === 'not all') {
      theme = themes[0];
    }
    else {
      theme = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'
    }
  }
  setTheme(theme);

  window.addEventListener('scroll', function(event){
    iframe = document.getElementById('child-iframe')
    topOffset = iframe.getBoundingClientRect().top + window.scrollY;
    currentScroll = document.scrollingElement.scrollTop;


    message = {};
    message.kind = 'scroll';
    message.message = {};
    message.message.topOffset = topOffset;
    message.message.currentScroll = currentScroll;
   
    // When running without a webserver, there is a lot of 'strangeness'
    if (window.location.protocol == "file:") {
        targetOrigin = "*";
    }
    else {
        targetOrigin = window.location.origin;
    }      

    if (iframe) {
      iframe.contentWindow.postMessage(message, targetOrigin);
    }
    else {
      window.self.postMessage(message, targetOrigin);
    }
});




  updateTexts();

  if (sessionStorage.getItem('currentPage') === null) {
      sessionStorage.setItem('currentPage', '');

      setIframeSrc('child-iframe', 'pages/.html', false);
  }
  else
  {
    if (sessionStorage.getItem('addQueryString') == 'true') {
      addQueryString = true;
    }
    else {
      addQueryString = false;
    }
      setIframeSrc('child-iframe', sessionStorage.getItem('currentPage'), addQueryString);  
  }

  
  // Get the actual navbar width and then reset the auto sizing of its width
  navContainer = document.getElementById('nav-container');
  fullNavBarWidth = navContainer.offsetWidth;
  navContainer.classList.remove('w-auto');

  manageNavbar();
  document.body.style.viewport = "visible";
});

addEventListener("resize", (event) => {
  manageNavbar();
  width = Math.max(document.documentElement.clientWidth, window.innerWidth || 0);
  // width/100 is like the css variable vw
  fontSize = width/100 * 1.5;
  // Max is 18px and min is 10px
  document.getElementsByTagName("html")[0].style.fontSize = Math.min(18, Math.max(10, fontSize)) + "px";

  resizeModal();
});

window.addEventListener("beforeunload", function (event) {
  if(sessionStorage.getItem("MQTTConnected")){
    MQTTDisconnect();
  }
});

window.addEventListener('message', 
                        function(e) {
                          // message that was passed from iframe page
                          var kind = e.data.kind;
                          if (kind == undefined) {
                            return;
                          }
                          var message = e.data.message;

                          if (kind == 'resize') {
                              var iframe = document.querySelector("#child-iframe");
                              iframe.style.height = message.height + 'px';
                              //iframe.style.width = message.width + 'px';
                          }
                          if (kind == 'loaded') {
                            document.querySelector("#child-iframe").style.visibility = 'visible';
                            resizeModal();
                          }
                          
                        }, 
                        false);       

    
'''

results_javascript_archive_pages_configuration = \
'''  


fullNavBarWidth = 0;

indexPageLogLevel = sessionStorage.getItem('indexPageLogLevel');
if (!indexPageLogLevel) {
    indexPageLogLevel = "3";
    sessionStorage.setItem('indexPageLogLevel', indexPageLogLevel);
}

function updatelogLevel(logLevel) {
    jasLogDebug = () => {};
    jasLogInfo = () => {};
    jasLogWarn= () => {};
    jasLogError = () => {};

    switch(logLevel) {
        case "1":
            jasLogDebug = (prefix, info) => {console.debug(prefix + JSON.stringify(info));};
        case "2":
            jasLogInfo = (prefix, info) => {console.info(prefix + JSON.stringify(info));};
        case "3":
            jasLogWarn = (prefix, info) => {console.warn(prefix + JSON.stringify(info));};
        case "4":
            jasLogError = (prefix, info) => {console.error(prefix + JSON.stringify(info));};
        }
}

updatelogLevel(indexPageLogLevel);

jasLogInfo("", navigator.userAgent);
jasLogInfo("WeeWX version: ", 'foo10');
jasLogInfo("weewx-jas version: ", 'foo11');
jasLogInfo("Language setting is: ", lang);
jasLogInfo("Log level: ", indexPageLogLevel);
jasLogInfo("", "host: foo3");
jasLogInfo("", "port: foo4");
jasLogInfo("", "timeout: foo5");
jasLogInfo("", "keepAliveInterval: foo6");
jasLogInfo("", "cleanSession: foo7");
jasLogInfo("", "useSSL: foo8");
jasLogInfo("", "reconnect: foo9");

function jasShow(data)
{
  message = {};
  message.kind = 'jasShow';
  message.message = data;
   
    // When running without a webserver, there is a lot of 'strangeness'
    if (window.location.protocol == "file:") {
        targetOrigin = "*";
    }
    else {
        targetOrigin = window.location.origin;
    }      

    if (document.getElementById('child-iframe')) {
      document.getElementById('child-iframe').contentWindow.postMessage(message, targetOrigin);
    }
    else {
      window.self.postMessage(message, targetOrigin);
    }
  return "Showing..."
}

function setLogLevel(logLevel)
{
    sessionStorage.setItem("indexPageLogLevel", logLevel);
    updatelogLevel(logLevel.toString());
    //return "Set to: " + logLevel

  // Send the logLevel to the sub-pages
  message = {};
  message.kind = 'setLogLevel';
  message.message = {};
  message.message.logLevel = logLevel;
   
    // When running without a webserver, there is a lot of 'strangeness'
    if (window.location.protocol == "file:") {
        targetOrigin = "*";
    }
    else {
        targetOrigin = window.location.origin;
    }      

    if (document.getElementById('child-iframe')) {
      document.getElementById('child-iframe').contentWindow.postMessage(message, targetOrigin);
    }
    else {
      window.self.postMessage(message, targetOrigin);
    }

  return "Index page log level: " + sessionStorage.getItem("indexPageLogLevel")
}

function getLogLevel() {

  // get sub-page log level
  message = {};
  message.kind = 'getLogLevel';
  message.message = {};
   
  // When running without a webserver, there is a lot of 'strangeness'
  if (window.location.protocol == "file:") {
      targetOrigin = "*";
  }
  else {
      targetOrigin = window.location.origin;
  }      

  if (document.getElementById('child-iframe')) {
    document.getElementById('child-iframe').contentWindow.postMessage(message, targetOrigin);
  }
  else {
    window.self.postMessage(message, targetOrigin);
  }

  return "Index page log level: " + sessionStorage.getItem("indexPageLogLevel")
}

function updateTheme(themeSelection) {
  if (themeSelection.checked) {
    setTheme("dark");
  } else {
    setTheme("light");
  }
}

function setTheme(theme) {
  sessionStorage.setItem('theme', theme);
  document.documentElement.setAttribute('data-bs-theme', theme);
  buttons = document.getElementsByClassName("btn");

  if (theme == 'dark') {
    document.getElementById("themeSelection").checked = true;
    for(var i = 0; i < buttons.length; i++)
    {
      buttons[i].classList.remove("btn-dark");
      buttons[i].classList.add("btn-light");
    }
  }
  else {
    document.getElementById("themeSelection").checked = false;
    for(var i = 0; i < buttons.length; i++)
    {
      buttons[i].classList.remove("btn-light");
      buttons[i].classList.add("btn-dark");
    }
  }

  message = {};
  message.kind = 'setTheme';
  message.message = theme;
   
  // When running without a webserver, there is a lot of 'strangeness'
  if (window.location.protocol == "file:") {
      targetOrigin = "*";
  }
  else {
      targetOrigin = window.location.origin;
  }      

  if (document.getElementById('child-iframe')) {
    document.getElementById('child-iframe').contentWindow.postMessage(message, targetOrigin);
  }
  else {
    window.self.postMessage(message, targetOrigin);
  }
}

function manageNavbar() {
  parentWidth = document.getElementById('navbar').parentElement.offsetWidth
  if (fullNavBarWidth >= parentWidth) {
    document.getElementById('navbar').classList.remove('navbar-expand')
  }
  else {
    document.getElementById('navbar').classList.add('navbar-expand')
  }
}

function refreshData() {
    message = {};
    message.kind = 'refreshData';
    message.message = {};
    
    // When running without a webserver, there is a lot of 'strangeness'
    if (window.location.protocol == "file:") {
        targetOrigin = "*";
    }
    else {
        targetOrigin = window.location.origin;
    }      

    if (document.getElementById('child-iframe')) {
      document.getElementById('child-iframe').contentWindow.postMessage(message, targetOrigin);
    }
    else {
      window.self.postMessage(message, targetOrigin);
    }
}

function setIframeSrc(id, url, addQueryString) {
  console.debug(Date.now().toString() + " setIframeSrc start");
  document.querySelector("#child-iframe").style.visibility = 'hidden';
  // Set current page as the active page.
  currentPage = sessionStorage.getItem('currentPage');
  if (currentPage != url) {
    currentPageId = document.getElementById(currentPage);
    if (currentPageId) {
      currentPageId.classList.remove("active");
    }
    sessionStorage.setItem('currentPage', url);
    sessionStorage.setItem('addQueryString', addQueryString);
  }
  document.getElementById(url).classList.add("active");
  // use query string so that iframe is not cached
  full_url = url;
  if (addQueryString) {
    full_url = full_url + "?ts=" + Date.now();
  }
  document.getElementById(id).src = full_url;

  // When on the debug iframe, add the connect/disconnect buttons to the header.
  // The need to be on the parent page because the MQTT connection is on the parent. 
  if (url == 'pages/debug.html') {
    document.getElementById('connectButton').classList.remove("d-none");
    document.getElementById('disconnectButton').classList.remove("d-none");
  }
  else {
    document.getElementById('connectButton').classList.add("d-none");
    document.getElementById('disconnectButton').classList.add("d-none");      
  }
  console.debug(Date.now().toString() + " setIframeSrc end");
}

function updateLang(language) {
      var currentLanguage = sessionStorage.getItem('currentLanguage');
      if (language != currentLanguage) {
          if (currentLanguage) {
              document.getElementById(currentLanguage).classList.remove("active");
          }
          document.getElementById(language).classList.add("active");
          sessionStorage.setItem('currentLanguage', language);
      }

    lang = language;
    updateTexts();

    message = {};
    message.kind = 'lang';
    message.message = language;
    
    // When running without a webserver, there is a lot of 'strangeness'
    if (window.location.protocol == "file:") {
        targetOrigin = "*";
    }
    else {
        targetOrigin = window.location.origin;
    }      

    if (document.getElementById('child-iframe')) {
      document.getElementById('child-iframe').contentWindow.postMessage(message, targetOrigin);
    }
    else {
      window.self.postMessage(message, targetOrigin);
    }
}

// Handle a year being selected
function setYear(year) {
  // Handle 'year' and 'month' click/selections
    var makeonClickHandler = function(url) {
            return function onClickHandler() {
                  setIframeSrc("child-iframe", url, false);
            };
    };

    var list = document.getElementById("dropdownYearMonthMenu");
    list.innerHTML = "";

    // Add the year to the top of the month dropdown.
      var li = document.createElement("li");
      var link = document.createElement("a"); 
      link.classList.add("dropdown-item");   
      var url = "pages/" + year + ".html";
      link.id = url;
      link.onclick = makeonClickHandler(url);
      link.setAttribute("data-bs-toggle", "collapse")
      link.setAttribute("data-bs-target", ".navbar-collapse.show")
      link.setAttribute("role", "button")

      var text = document.createTextNode(year);
      link.appendChild(text);
      li.appendChild(link);
      list.appendChild(li);

      // Add a divider between the year amd months.
      var divider = document.createElement("div");
      divider.classList.add("dropdown-divider");
      list.appendChild(divider);

    // Add each month to the drop down.
    for (var i = 0; i < yearMonth[year].length; i++) {
      li = document.createElement("li");
      link = document.createElement("a"); 
      link.classList.add("dropdown-item");
      url = "pages/" + yearMonth[year][i] + ".html";
      link.id = url;
      link.onclick = makeonClickHandler(url);

      link.setAttribute("data-bs-toggle", "collapse")
      link.setAttribute("data-bs-target", ".navbar-collapse.show")
      link.setAttribute("role", "button")

      var currentPage = sessionStorage.getItem('currentPage');
      if (currentPage && currentPage == url) {
        link.id = url;
      }
    
      text = document.createTextNode(yearMonth[year][i]);
      link.appendChild(text);
      li.appendChild(link);
      list.appendChild(li);
    }
}

function resizeModal() {
  width = Math.max(document.documentElement.clientWidth, window.innerWidth || 0);
  height = Math.max(document.documentElement.clientHeight, window.innerHeight || 0);

  message = {};
  message.kind = 'resize';
  message.message = {};
  message.message.width = width;
  message.message.height = height - document.getElementById('navbar').clientHeight;

  // When running without a webserver, there is a lot of 'strangeness'
  if (window.location.protocol == "file:") {
      targetOrigin = "*";
  }
  else {
      targetOrigin = window.location.origin;
  }      

  iframe = document.getElementById('child-iframe')
  if (iframe) {
    iframe.contentWindow.postMessage(message, targetOrigin);
  }
  else {
    window.self.postMessage(message, targetOrigin);
  }
}

window.addEventListener("load", function (event) {
  var themes = ['light'];
  theme = sessionStorage.getItem('theme');
  if (!theme) {
    if (window.matchMedia('(prefers-color-scheme: dark)').media === 'not all') {
      theme = themes[0];
    }
    else {
      theme = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'
    }
  }
  setTheme(theme);

  window.addEventListener('scroll', function(event){
    iframe = document.getElementById('child-iframe')
    topOffset = iframe.getBoundingClientRect().top + window.scrollY;
    currentScroll = document.scrollingElement.scrollTop;


    message = {};
    message.kind = 'scroll';
    message.message = {};
    message.message.topOffset = topOffset;
    message.message.currentScroll = currentScroll;
   
    // When running without a webserver, there is a lot of 'strangeness'
    if (window.location.protocol == "file:") {
        targetOrigin = "*";
    }
    else {
        targetOrigin = window.location.origin;
    }      

    if (iframe) {
      iframe.contentWindow.postMessage(message, targetOrigin);
    }
    else {
      window.self.postMessage(message, targetOrigin);
    }
});



    var list = document.getElementById("dropdownYearMenu");
    list.innerHTML = "";
    list.currentSelection = null;

    // Handle year selected/click
    var setActiveYear = function() {
      var list = document.getElementById("dropdownYearMenu");
      var currentSelection = sessionStorage.getItem('currentSelection');
      if (this.id != currentSelection) {
          if (currentSelection) {
              document.getElementById(currentSelection).classList.remove("active");
          }
          this.classList.add("active");
          sessionStorage.setItem('currentSelection', this.id);
      }
      setYear(this.innerHTML);
    };

    // build year drop down
    for (var year in yearMonth){
      var li = document.createElement("li");
      var link = document.createElement("a"); 
      link.classList.add("dropdown-item");
        link.id = year;

      var text = document.createTextNode(year);
      link.onclick = setActiveYear;
      link.appendChild(text);
      link.href = "#";
      li.appendChild(link);
      list.appendChild(li);
      var currentSelection = sessionStorage.getItem('currentSelection');
      if (currentSelection && currentSelection == year) {
        link.classList.add("active");
        sessionStorage.setItem('currentSelection', link.id);
        setYear(link.innerHTML);
      }
    }

  updateTexts();

  if (sessionStorage.getItem('currentPage') === null) {
      sessionStorage.setItem('currentPage', '');

      setIframeSrc('child-iframe', 'pages/archive-month.html', false);
  }
  else
  {
    if (sessionStorage.getItem('addQueryString') == 'true') {
      addQueryString = true;
    }
    else {
      addQueryString = false;
    }
      setIframeSrc('child-iframe', sessionStorage.getItem('currentPage'), addQueryString);  
  }

  
  // Get the actual navbar width and then reset the auto sizing of its width
  navContainer = document.getElementById('nav-container');
  fullNavBarWidth = navContainer.offsetWidth;
  navContainer.classList.remove('w-auto');

  manageNavbar();
  document.body.style.viewport = "visible";
});

addEventListener("resize", (event) => {
  manageNavbar();
  width = Math.max(document.documentElement.clientWidth, window.innerWidth || 0);
  // width/100 is like the css variable vw
  fontSize = width/100 * 1.5;
  // Max is 18px and min is 10px
  document.getElementsByTagName("html")[0].style.fontSize = Math.min(18, Math.max(10, fontSize)) + "px";

  resizeModal();
});

window.addEventListener("beforeunload", function (event) {
  if(sessionStorage.getItem("MQTTConnected")){
    MQTTDisconnect();
  }
});

window.addEventListener('message', 
                        function(e) {
                          // message that was passed from iframe page
                          var kind = e.data.kind;
                          if (kind == undefined) {
                            return;
                          }
                          var message = e.data.message;

                          if (kind == 'resize') {
                              var iframe = document.querySelector("#child-iframe");
                              iframe.style.height = message.height + 'px';
                              //iframe.style.width = message.width + 'px';
                          }
                          if (kind == 'loaded') {
                            document.querySelector("#child-iframe").style.visibility = 'visible';
                            resizeModal();
                          }
                          
                        }, 
                        false);       

    
'''

results_javascript_archive_pages_month_disabled_configuration = \
'''  


fullNavBarWidth = 0;

indexPageLogLevel = sessionStorage.getItem('indexPageLogLevel');
if (!indexPageLogLevel) {
    indexPageLogLevel = "3";
    sessionStorage.setItem('indexPageLogLevel', indexPageLogLevel);
}

function updatelogLevel(logLevel) {
    jasLogDebug = () => {};
    jasLogInfo = () => {};
    jasLogWarn= () => {};
    jasLogError = () => {};

    switch(logLevel) {
        case "1":
            jasLogDebug = (prefix, info) => {console.debug(prefix + JSON.stringify(info));};
        case "2":
            jasLogInfo = (prefix, info) => {console.info(prefix + JSON.stringify(info));};
        case "3":
            jasLogWarn = (prefix, info) => {console.warn(prefix + JSON.stringify(info));};
        case "4":
            jasLogError = (prefix, info) => {console.error(prefix + JSON.stringify(info));};
        }
}

updatelogLevel(indexPageLogLevel);

jasLogInfo("", navigator.userAgent);
jasLogInfo("WeeWX version: ", 'foo10');
jasLogInfo("weewx-jas version: ", 'foo11');
jasLogInfo("Language setting is: ", lang);
jasLogInfo("Log level: ", indexPageLogLevel);
jasLogInfo("", "host: foo3");
jasLogInfo("", "port: foo4");
jasLogInfo("", "timeout: foo5");
jasLogInfo("", "keepAliveInterval: foo6");
jasLogInfo("", "cleanSession: foo7");
jasLogInfo("", "useSSL: foo8");
jasLogInfo("", "reconnect: foo9");

function jasShow(data)
{
  message = {};
  message.kind = 'jasShow';
  message.message = data;
   
    // When running without a webserver, there is a lot of 'strangeness'
    if (window.location.protocol == "file:") {
        targetOrigin = "*";
    }
    else {
        targetOrigin = window.location.origin;
    }      

    if (document.getElementById('child-iframe')) {
      document.getElementById('child-iframe').contentWindow.postMessage(message, targetOrigin);
    }
    else {
      window.self.postMessage(message, targetOrigin);
    }
  return "Showing..."
}

function setLogLevel(logLevel)
{
    sessionStorage.setItem("indexPageLogLevel", logLevel);
    updatelogLevel(logLevel.toString());
    //return "Set to: " + logLevel

  // Send the logLevel to the sub-pages
  message = {};
  message.kind = 'setLogLevel';
  message.message = {};
  message.message.logLevel = logLevel;
   
    // When running without a webserver, there is a lot of 'strangeness'
    if (window.location.protocol == "file:") {
        targetOrigin = "*";
    }
    else {
        targetOrigin = window.location.origin;
    }      

    if (document.getElementById('child-iframe')) {
      document.getElementById('child-iframe').contentWindow.postMessage(message, targetOrigin);
    }
    else {
      window.self.postMessage(message, targetOrigin);
    }

  return "Index page log level: " + sessionStorage.getItem("indexPageLogLevel")
}

function getLogLevel() {

  // get sub-page log level
  message = {};
  message.kind = 'getLogLevel';
  message.message = {};
   
  // When running without a webserver, there is a lot of 'strangeness'
  if (window.location.protocol == "file:") {
      targetOrigin = "*";
  }
  else {
      targetOrigin = window.location.origin;
  }      

  if (document.getElementById('child-iframe')) {
    document.getElementById('child-iframe').contentWindow.postMessage(message, targetOrigin);
  }
  else {
    window.self.postMessage(message, targetOrigin);
  }

  return "Index page log level: " + sessionStorage.getItem("indexPageLogLevel")
}

function updateTheme(themeSelection) {
  if (themeSelection.checked) {
    setTheme("dark");
  } else {
    setTheme("light");
  }
}

function setTheme(theme) {
  sessionStorage.setItem('theme', theme);
  document.documentElement.setAttribute('data-bs-theme', theme);
  buttons = document.getElementsByClassName("btn");

  if (theme == 'dark') {
    document.getElementById("themeSelection").checked = true;
    for(var i = 0; i < buttons.length; i++)
    {
      buttons[i].classList.remove("btn-dark");
      buttons[i].classList.add("btn-light");
    }
  }
  else {
    document.getElementById("themeSelection").checked = false;
    for(var i = 0; i < buttons.length; i++)
    {
      buttons[i].classList.remove("btn-light");
      buttons[i].classList.add("btn-dark");
    }
  }

  message = {};
  message.kind = 'setTheme';
  message.message = theme;
   
  // When running without a webserver, there is a lot of 'strangeness'
  if (window.location.protocol == "file:") {
      targetOrigin = "*";
  }
  else {
      targetOrigin = window.location.origin;
  }      

  if (document.getElementById('child-iframe')) {
    document.getElementById('child-iframe').contentWindow.postMessage(message, targetOrigin);
  }
  else {
    window.self.postMessage(message, targetOrigin);
  }
}

function manageNavbar() {
  parentWidth = document.getElementById('navbar').parentElement.offsetWidth
  if (fullNavBarWidth >= parentWidth) {
    document.getElementById('navbar').classList.remove('navbar-expand')
  }
  else {
    document.getElementById('navbar').classList.add('navbar-expand')
  }
}

function refreshData() {
    message = {};
    message.kind = 'refreshData';
    message.message = {};
    
    // When running without a webserver, there is a lot of 'strangeness'
    if (window.location.protocol == "file:") {
        targetOrigin = "*";
    }
    else {
        targetOrigin = window.location.origin;
    }      

    if (document.getElementById('child-iframe')) {
      document.getElementById('child-iframe').contentWindow.postMessage(message, targetOrigin);
    }
    else {
      window.self.postMessage(message, targetOrigin);
    }
}

function setIframeSrc(id, url, addQueryString) {
  console.debug(Date.now().toString() + " setIframeSrc start");
  document.querySelector("#child-iframe").style.visibility = 'hidden';
  // Set current page as the active page.
  currentPage = sessionStorage.getItem('currentPage');
  if (currentPage != url) {
    currentPageId = document.getElementById(currentPage);
    if (currentPageId) {
      currentPageId.classList.remove("active");
    }
    sessionStorage.setItem('currentPage', url);
    sessionStorage.setItem('addQueryString', addQueryString);
  }
  document.getElementById(url).classList.add("active");
  // use query string so that iframe is not cached
  full_url = url;
  if (addQueryString) {
    full_url = full_url + "?ts=" + Date.now();
  }
  document.getElementById(id).src = full_url;

  // When on the debug iframe, add the connect/disconnect buttons to the header.
  // The need to be on the parent page because the MQTT connection is on the parent. 
  if (url == 'pages/debug.html') {
    document.getElementById('connectButton').classList.remove("d-none");
    document.getElementById('disconnectButton').classList.remove("d-none");
  }
  else {
    document.getElementById('connectButton').classList.add("d-none");
    document.getElementById('disconnectButton').classList.add("d-none");      
  }
  console.debug(Date.now().toString() + " setIframeSrc end");
}

function updateLang(language) {
      var currentLanguage = sessionStorage.getItem('currentLanguage');
      if (language != currentLanguage) {
          if (currentLanguage) {
              document.getElementById(currentLanguage).classList.remove("active");
          }
          document.getElementById(language).classList.add("active");
          sessionStorage.setItem('currentLanguage', language);
      }

    lang = language;
    updateTexts();

    message = {};
    message.kind = 'lang';
    message.message = language;
    
    // When running without a webserver, there is a lot of 'strangeness'
    if (window.location.protocol == "file:") {
        targetOrigin = "*";
    }
    else {
        targetOrigin = window.location.origin;
    }      

    if (document.getElementById('child-iframe')) {
      document.getElementById('child-iframe').contentWindow.postMessage(message, targetOrigin);
    }
    else {
      window.self.postMessage(message, targetOrigin);
    }
}

// Handle a year being selected
function setYear(year) {
  // Handle 'year' and 'month' click/selections
    var url = "pages/" + year + ".html";
    setIframeSrc('child-iframe', url, false)
}

function resizeModal() {
  width = Math.max(document.documentElement.clientWidth, window.innerWidth || 0);
  height = Math.max(document.documentElement.clientHeight, window.innerHeight || 0);

  message = {};
  message.kind = 'resize';
  message.message = {};
  message.message.width = width;
  message.message.height = height - document.getElementById('navbar').clientHeight;

  // When running without a webserver, there is a lot of 'strangeness'
  if (window.location.protocol == "file:") {
      targetOrigin = "*";
  }
  else {
      targetOrigin = window.location.origin;
  }      

  iframe = document.getElementById('child-iframe')
  if (iframe) {
    iframe.contentWindow.postMessage(message, targetOrigin);
  }
  else {
    window.self.postMessage(message, targetOrigin);
  }
}

window.addEventListener("load", function (event) {
  var themes = ['light'];
  theme = sessionStorage.getItem('theme');
  if (!theme) {
    if (window.matchMedia('(prefers-color-scheme: dark)').media === 'not all') {
      theme = themes[0];
    }
    else {
      theme = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'
    }
  }
  setTheme(theme);

  window.addEventListener('scroll', function(event){
    iframe = document.getElementById('child-iframe')
    topOffset = iframe.getBoundingClientRect().top + window.scrollY;
    currentScroll = document.scrollingElement.scrollTop;


    message = {};
    message.kind = 'scroll';
    message.message = {};
    message.message.topOffset = topOffset;
    message.message.currentScroll = currentScroll;
   
    // When running without a webserver, there is a lot of 'strangeness'
    if (window.location.protocol == "file:") {
        targetOrigin = "*";
    }
    else {
        targetOrigin = window.location.origin;
    }      

    if (iframe) {
      iframe.contentWindow.postMessage(message, targetOrigin);
    }
    else {
      window.self.postMessage(message, targetOrigin);
    }
});



    var list = document.getElementById("dropdownYearMenu");
    list.innerHTML = "";
    list.currentSelection = null;

    // Handle year selected/click
    var setActiveYear = function() {
      var list = document.getElementById("dropdownYearMenu");
      var currentSelection = sessionStorage.getItem('currentSelection');
      if (this.id != currentSelection) {
          if (currentSelection) {
              document.getElementById(currentSelection).classList.remove("active");
          }
          this.classList.add("active");
          sessionStorage.setItem('currentSelection', this.id);
      }
      setYear(this.innerHTML);
    };

    // build year drop down
    for (var year in yearMonth){
      var li = document.createElement("li");
      var link = document.createElement("a"); 
      link.classList.add("dropdown-item");
        link.id = 'pages/' + year + '.html'
        link.setAttribute("data-bs-toggle", "collapse")
        link.setAttribute("data-bs-target", ".navbar-collapse.show")

      var text = document.createTextNode(year);
      link.onclick = setActiveYear;
      link.appendChild(text);
      link.href = "#";
      li.appendChild(link);
      list.appendChild(li);
      var currentSelection = sessionStorage.getItem('currentSelection');
      if (currentSelection && currentSelection == year) {
        link.classList.add("active");
        sessionStorage.setItem('currentSelection', link.id);
        setYear(link.innerHTML);
      }
    }

  updateTexts();

  if (sessionStorage.getItem('currentPage') === null) {
      sessionStorage.setItem('currentPage', '');

      setIframeSrc('child-iframe', 'pages/archive-year.html', false);
  }
  else
  {
    if (sessionStorage.getItem('addQueryString') == 'true') {
      addQueryString = true;
    }
    else {
      addQueryString = false;
    }
      setIframeSrc('child-iframe', sessionStorage.getItem('currentPage'), addQueryString);  
  }

  
  // Get the actual navbar width and then reset the auto sizing of its width
  navContainer = document.getElementById('nav-container');
  fullNavBarWidth = navContainer.offsetWidth;
  navContainer.classList.remove('w-auto');

  manageNavbar();
  document.body.style.viewport = "visible";
});

addEventListener("resize", (event) => {
  manageNavbar();
  width = Math.max(document.documentElement.clientWidth, window.innerWidth || 0);
  // width/100 is like the css variable vw
  fontSize = width/100 * 1.5;
  // Max is 18px and min is 10px
  document.getElementsByTagName("html")[0].style.fontSize = Math.min(18, Math.max(10, fontSize)) + "px";

  resizeModal();
});

window.addEventListener("beforeunload", function (event) {
  if(sessionStorage.getItem("MQTTConnected")){
    MQTTDisconnect();
  }
});

window.addEventListener('message', 
                        function(e) {
                          // message that was passed from iframe page
                          var kind = e.data.kind;
                          if (kind == undefined) {
                            return;
                          }
                          var message = e.data.message;

                          if (kind == 'resize') {
                              var iframe = document.querySelector("#child-iframe");
                              iframe.style.height = message.height + 'px';
                              //iframe.style.width = message.width + 'px';
                          }
                          if (kind == 'loaded') {
                            document.querySelector("#child-iframe").style.visibility = 'visible';
                            resizeModal();
                          }
                          
                        }, 
                        false);       

    
'''

results_javascript_landing_page_configuration = \
'''  


fullNavBarWidth = 0;

indexPageLogLevel = sessionStorage.getItem('indexPageLogLevel');
if (!indexPageLogLevel) {
    indexPageLogLevel = "3";
    sessionStorage.setItem('indexPageLogLevel', indexPageLogLevel);
}

function updatelogLevel(logLevel) {
    jasLogDebug = () => {};
    jasLogInfo = () => {};
    jasLogWarn= () => {};
    jasLogError = () => {};

    switch(logLevel) {
        case "1":
            jasLogDebug = (prefix, info) => {console.debug(prefix + JSON.stringify(info));};
        case "2":
            jasLogInfo = (prefix, info) => {console.info(prefix + JSON.stringify(info));};
        case "3":
            jasLogWarn = (prefix, info) => {console.warn(prefix + JSON.stringify(info));};
        case "4":
            jasLogError = (prefix, info) => {console.error(prefix + JSON.stringify(info));};
        }
}

updatelogLevel(indexPageLogLevel);

jasLogInfo("", navigator.userAgent);
jasLogInfo("WeeWX version: ", 'foo10');
jasLogInfo("weewx-jas version: ", 'foo11');
jasLogInfo("Language setting is: ", lang);
jasLogInfo("Log level: ", indexPageLogLevel);
jasLogInfo("", "host: foo3");
jasLogInfo("", "port: foo4");
jasLogInfo("", "timeout: foo5");
jasLogInfo("", "keepAliveInterval: foo6");
jasLogInfo("", "cleanSession: foo7");
jasLogInfo("", "useSSL: foo8");
jasLogInfo("", "reconnect: foo9");

function jasShow(data)
{
  message = {};
  message.kind = 'jasShow';
  message.message = data;
   
    // When running without a webserver, there is a lot of 'strangeness'
    if (window.location.protocol == "file:") {
        targetOrigin = "*";
    }
    else {
        targetOrigin = window.location.origin;
    }      

    if (document.getElementById('child-iframe')) {
      document.getElementById('child-iframe').contentWindow.postMessage(message, targetOrigin);
    }
    else {
      window.self.postMessage(message, targetOrigin);
    }
  return "Showing..."
}

function setLogLevel(logLevel)
{
    sessionStorage.setItem("indexPageLogLevel", logLevel);
    updatelogLevel(logLevel.toString());
    //return "Set to: " + logLevel

  // Send the logLevel to the sub-pages
  message = {};
  message.kind = 'setLogLevel';
  message.message = {};
  message.message.logLevel = logLevel;
   
    // When running without a webserver, there is a lot of 'strangeness'
    if (window.location.protocol == "file:") {
        targetOrigin = "*";
    }
    else {
        targetOrigin = window.location.origin;
    }      

    if (document.getElementById('child-iframe')) {
      document.getElementById('child-iframe').contentWindow.postMessage(message, targetOrigin);
    }
    else {
      window.self.postMessage(message, targetOrigin);
    }

  return "Index page log level: " + sessionStorage.getItem("indexPageLogLevel")
}

function getLogLevel() {

  // get sub-page log level
  message = {};
  message.kind = 'getLogLevel';
  message.message = {};
   
  // When running without a webserver, there is a lot of 'strangeness'
  if (window.location.protocol == "file:") {
      targetOrigin = "*";
  }
  else {
      targetOrigin = window.location.origin;
  }      

  if (document.getElementById('child-iframe')) {
    document.getElementById('child-iframe').contentWindow.postMessage(message, targetOrigin);
  }
  else {
    window.self.postMessage(message, targetOrigin);
  }

  return "Index page log level: " + sessionStorage.getItem("indexPageLogLevel")
}

function updateTheme(themeSelection) {
  if (themeSelection.checked) {
    setTheme("dark");
  } else {
    setTheme("light");
  }
}

function setTheme(theme) {
  sessionStorage.setItem('theme', theme);
  document.documentElement.setAttribute('data-bs-theme', theme);
  buttons = document.getElementsByClassName("btn");

  if (theme == 'dark') {
    document.getElementById("themeSelection").checked = true;
    for(var i = 0; i < buttons.length; i++)
    {
      buttons[i].classList.remove("btn-dark");
      buttons[i].classList.add("btn-light");
    }
  }
  else {
    document.getElementById("themeSelection").checked = false;
    for(var i = 0; i < buttons.length; i++)
    {
      buttons[i].classList.remove("btn-light");
      buttons[i].classList.add("btn-dark");
    }
  }

  message = {};
  message.kind = 'setTheme';
  message.message = theme;
   
  // When running without a webserver, there is a lot of 'strangeness'
  if (window.location.protocol == "file:") {
      targetOrigin = "*";
  }
  else {
      targetOrigin = window.location.origin;
  }      

  if (document.getElementById('child-iframe')) {
    document.getElementById('child-iframe').contentWindow.postMessage(message, targetOrigin);
  }
  else {
    window.self.postMessage(message, targetOrigin);
  }
}

function manageNavbar() {
  parentWidth = document.getElementById('navbar').parentElement.offsetWidth
  if (fullNavBarWidth >= parentWidth) {
    document.getElementById('navbar').classList.remove('navbar-expand')
  }
  else {
    document.getElementById('navbar').classList.add('navbar-expand')
  }
}

function refreshData() {
    message = {};
    message.kind = 'refreshData';
    message.message = {};
    
    // When running without a webserver, there is a lot of 'strangeness'
    if (window.location.protocol == "file:") {
        targetOrigin = "*";
    }
    else {
        targetOrigin = window.location.origin;
    }      

    if (document.getElementById('child-iframe')) {
      document.getElementById('child-iframe').contentWindow.postMessage(message, targetOrigin);
    }
    else {
      window.self.postMessage(message, targetOrigin);
    }
}

function setIframeSrc(id, url, addQueryString) {
  console.debug(Date.now().toString() + " setIframeSrc start");
  document.querySelector("#child-iframe").style.visibility = 'hidden';
  // Set current page as the active page.
  currentPage = sessionStorage.getItem('currentPage');
  if (currentPage != url) {
    currentPageId = document.getElementById(currentPage);
    if (currentPageId) {
      currentPageId.classList.remove("active");
    }
    sessionStorage.setItem('currentPage', url);
    sessionStorage.setItem('addQueryString', addQueryString);
  }
  document.getElementById(url).classList.add("active");
  // use query string so that iframe is not cached
  full_url = url;
  if (addQueryString) {
    full_url = full_url + "?ts=" + Date.now();
  }
  document.getElementById(id).src = full_url;

  // When on the debug iframe, add the connect/disconnect buttons to the header.
  // The need to be on the parent page because the MQTT connection is on the parent. 
  if (url == 'pages/debug.html') {
    document.getElementById('connectButton').classList.remove("d-none");
    document.getElementById('disconnectButton').classList.remove("d-none");
  }
  else {
    document.getElementById('connectButton').classList.add("d-none");
    document.getElementById('disconnectButton').classList.add("d-none");      
  }
  console.debug(Date.now().toString() + " setIframeSrc end");
}

function updateLang(language) {
      var currentLanguage = sessionStorage.getItem('currentLanguage');
      if (language != currentLanguage) {
          if (currentLanguage) {
              document.getElementById(currentLanguage).classList.remove("active");
          }
          document.getElementById(language).classList.add("active");
          sessionStorage.setItem('currentLanguage', language);
      }

    lang = language;
    updateTexts();

    message = {};
    message.kind = 'lang';
    message.message = language;
    
    // When running without a webserver, there is a lot of 'strangeness'
    if (window.location.protocol == "file:") {
        targetOrigin = "*";
    }
    else {
        targetOrigin = window.location.origin;
    }      

    if (document.getElementById('child-iframe')) {
      document.getElementById('child-iframe').contentWindow.postMessage(message, targetOrigin);
    }
    else {
      window.self.postMessage(message, targetOrigin);
    }
}

// Handle a year being selected
function setYear(year) {
  // Handle 'year' and 'month' click/selections
    var url = "pages/" + year + ".html";
    setIframeSrc('child-iframe', url, false)
}

function resizeModal() {
  width = Math.max(document.documentElement.clientWidth, window.innerWidth || 0);
  height = Math.max(document.documentElement.clientHeight, window.innerHeight || 0);

  message = {};
  message.kind = 'resize';
  message.message = {};
  message.message.width = width;
  message.message.height = height - document.getElementById('navbar').clientHeight;

  // When running without a webserver, there is a lot of 'strangeness'
  if (window.location.protocol == "file:") {
      targetOrigin = "*";
  }
  else {
      targetOrigin = window.location.origin;
  }      

  iframe = document.getElementById('child-iframe')
  if (iframe) {
    iframe.contentWindow.postMessage(message, targetOrigin);
  }
  else {
    window.self.postMessage(message, targetOrigin);
  }
}

window.addEventListener("load", function (event) {
  var themes = ['light'];
  theme = sessionStorage.getItem('theme');
  if (!theme) {
    if (window.matchMedia('(prefers-color-scheme: dark)').media === 'not all') {
      theme = themes[0];
    }
    else {
      theme = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'
    }
  }
  setTheme(theme);

  window.addEventListener('scroll', function(event){
    iframe = document.getElementById('child-iframe')
    topOffset = iframe.getBoundingClientRect().top + window.scrollY;
    currentScroll = document.scrollingElement.scrollTop;


    message = {};
    message.kind = 'scroll';
    message.message = {};
    message.message.topOffset = topOffset;
    message.message.currentScroll = currentScroll;
   
    // When running without a webserver, there is a lot of 'strangeness'
    if (window.location.protocol == "file:") {
        targetOrigin = "*";
    }
    else {
        targetOrigin = window.location.origin;
    }      

    if (iframe) {
      iframe.contentWindow.postMessage(message, targetOrigin);
    }
    else {
      window.self.postMessage(message, targetOrigin);
    }
});




  updateTexts();

  if (sessionStorage.getItem('currentPage') === null) {
      sessionStorage.setItem('currentPage', '');

      setIframeSrc('child-iframe', 'pages/page-1.html', true);
  }
  else
  {
    if (sessionStorage.getItem('addQueryString') == 'true') {
      addQueryString = true;
    }
    else {
      addQueryString = false;
    }
      setIframeSrc('child-iframe', sessionStorage.getItem('currentPage'), addQueryString);  
  }

  
  // Get the actual navbar width and then reset the auto sizing of its width
  navContainer = document.getElementById('nav-container');
  fullNavBarWidth = navContainer.offsetWidth;
  navContainer.classList.remove('w-auto');

  manageNavbar();
  document.body.style.viewport = "visible";
});

addEventListener("resize", (event) => {
  manageNavbar();
  width = Math.max(document.documentElement.clientWidth, window.innerWidth || 0);
  // width/100 is like the css variable vw
  fontSize = width/100 * 1.5;
  // Max is 18px and min is 10px
  document.getElementsByTagName("html")[0].style.fontSize = Math.min(18, Math.max(10, fontSize)) + "px";

  resizeModal();
});

window.addEventListener("beforeunload", function (event) {
  if(sessionStorage.getItem("MQTTConnected")){
    MQTTDisconnect();
  }
});

window.addEventListener('message', 
                        function(e) {
                          // message that was passed from iframe page
                          var kind = e.data.kind;
                          if (kind == undefined) {
                            return;
                          }
                          var message = e.data.message;

                          if (kind == 'resize') {
                              var iframe = document.querySelector("#child-iframe");
                              iframe.style.height = message.height + 'px';
                              //iframe.style.width = message.width + 'px';
                          }
                          if (kind == 'loaded') {
                            document.querySelector("#child-iframe").style.visibility = 'visible';
                            resizeModal();
                          }
                          
                        }, 
                        false);       

    
'''

results_javascript_mqtt_configuration = \
'''  


fullNavBarWidth = 0;

indexPageLogLevel = sessionStorage.getItem('indexPageLogLevel');
if (!indexPageLogLevel) {
    indexPageLogLevel = "3";
    sessionStorage.setItem('indexPageLogLevel', indexPageLogLevel);
}

function updatelogLevel(logLevel) {
    jasLogDebug = () => {};
    jasLogInfo = () => {};
    jasLogWarn= () => {};
    jasLogError = () => {};

    switch(logLevel) {
        case "1":
            jasLogDebug = (prefix, info) => {console.debug(prefix + JSON.stringify(info));};
        case "2":
            jasLogInfo = (prefix, info) => {console.info(prefix + JSON.stringify(info));};
        case "3":
            jasLogWarn = (prefix, info) => {console.warn(prefix + JSON.stringify(info));};
        case "4":
            jasLogError = (prefix, info) => {console.error(prefix + JSON.stringify(info));};
        }
}

updatelogLevel(indexPageLogLevel);

jasLogInfo("", navigator.userAgent);
jasLogInfo("WeeWX version: ", 'foo10');
jasLogInfo("weewx-jas version: ", 'foo11');
jasLogInfo("Language setting is: ", lang);
jasLogInfo("Log level: ", indexPageLogLevel);
jasLogInfo("", "host: foo3");
jasLogInfo("", "port: foo4");
jasLogInfo("", "timeout: foo5");
jasLogInfo("", "keepAliveInterval: foo6");
jasLogInfo("", "cleanSession: foo7");
jasLogInfo("", "useSSL: foo8");
jasLogInfo("", "reconnect: foo9");

function jasShow(data)
{
  message = {};
  message.kind = 'jasShow';
  message.message = data;
   
    // When running without a webserver, there is a lot of 'strangeness'
    if (window.location.protocol == "file:") {
        targetOrigin = "*";
    }
    else {
        targetOrigin = window.location.origin;
    }      

    if (document.getElementById('child-iframe')) {
      document.getElementById('child-iframe').contentWindow.postMessage(message, targetOrigin);
    }
    else {
      window.self.postMessage(message, targetOrigin);
    }
  return "Showing..."
}

function setLogLevel(logLevel)
{
    sessionStorage.setItem("indexPageLogLevel", logLevel);
    updatelogLevel(logLevel.toString());
    //return "Set to: " + logLevel

  // Send the logLevel to the sub-pages
  message = {};
  message.kind = 'setLogLevel';
  message.message = {};
  message.message.logLevel = logLevel;
   
    // When running without a webserver, there is a lot of 'strangeness'
    if (window.location.protocol == "file:") {
        targetOrigin = "*";
    }
    else {
        targetOrigin = window.location.origin;
    }      

    if (document.getElementById('child-iframe')) {
      document.getElementById('child-iframe').contentWindow.postMessage(message, targetOrigin);
    }
    else {
      window.self.postMessage(message, targetOrigin);
    }

  return "Index page log level: " + sessionStorage.getItem("indexPageLogLevel")
}

function getLogLevel() {

  // get sub-page log level
  message = {};
  message.kind = 'getLogLevel';
  message.message = {};
   
  // When running without a webserver, there is a lot of 'strangeness'
  if (window.location.protocol == "file:") {
      targetOrigin = "*";
  }
  else {
      targetOrigin = window.location.origin;
  }      

  if (document.getElementById('child-iframe')) {
    document.getElementById('child-iframe').contentWindow.postMessage(message, targetOrigin);
  }
  else {
    window.self.postMessage(message, targetOrigin);
  }

  return "Index page log level: " + sessionStorage.getItem("indexPageLogLevel")
}

function updateTheme(themeSelection) {
  if (themeSelection.checked) {
    setTheme("dark");
  } else {
    setTheme("light");
  }
}

function setTheme(theme) {
  sessionStorage.setItem('theme', theme);
  document.documentElement.setAttribute('data-bs-theme', theme);
  buttons = document.getElementsByClassName("btn");

  if (theme == 'dark') {
    document.getElementById("themeSelection").checked = true;
    for(var i = 0; i < buttons.length; i++)
    {
      buttons[i].classList.remove("btn-dark");
      buttons[i].classList.add("btn-light");
    }
  }
  else {
    document.getElementById("themeSelection").checked = false;
    for(var i = 0; i < buttons.length; i++)
    {
      buttons[i].classList.remove("btn-light");
      buttons[i].classList.add("btn-dark");
    }
  }

  message = {};
  message.kind = 'setTheme';
  message.message = theme;
   
  // When running without a webserver, there is a lot of 'strangeness'
  if (window.location.protocol == "file:") {
      targetOrigin = "*";
  }
  else {
      targetOrigin = window.location.origin;
  }      

  if (document.getElementById('child-iframe')) {
    document.getElementById('child-iframe').contentWindow.postMessage(message, targetOrigin);
  }
  else {
    window.self.postMessage(message, targetOrigin);
  }
}

function manageNavbar() {
  parentWidth = document.getElementById('navbar').parentElement.offsetWidth
  if (fullNavBarWidth >= parentWidth) {
    document.getElementById('navbar').classList.remove('navbar-expand')
  }
  else {
    document.getElementById('navbar').classList.add('navbar-expand')
  }
}

function refreshData() {
    message = {};
    message.kind = 'refreshData';
    message.message = {};
    
    // When running without a webserver, there is a lot of 'strangeness'
    if (window.location.protocol == "file:") {
        targetOrigin = "*";
    }
    else {
        targetOrigin = window.location.origin;
    }      

    if (document.getElementById('child-iframe')) {
      document.getElementById('child-iframe').contentWindow.postMessage(message, targetOrigin);
    }
    else {
      window.self.postMessage(message, targetOrigin);
    }
}

function setIframeSrc(id, url, addQueryString) {
  console.debug(Date.now().toString() + " setIframeSrc start");
  document.querySelector("#child-iframe").style.visibility = 'hidden';
  // Set current page as the active page.
  currentPage = sessionStorage.getItem('currentPage');
  if (currentPage != url) {
    currentPageId = document.getElementById(currentPage);
    if (currentPageId) {
      currentPageId.classList.remove("active");
    }
    sessionStorage.setItem('currentPage', url);
    sessionStorage.setItem('addQueryString', addQueryString);
  }
  document.getElementById(url).classList.add("active");
  // use query string so that iframe is not cached
  full_url = url;
  if (addQueryString) {
    full_url = full_url + "?ts=" + Date.now();
  }
  document.getElementById(id).src = full_url;

  // When on the debug iframe, add the connect/disconnect buttons to the header.
  // The need to be on the parent page because the MQTT connection is on the parent. 
  if (url == 'pages/debug.html') {
    document.getElementById('connectButton').classList.remove("d-none");
    document.getElementById('disconnectButton').classList.remove("d-none");
  }
  else {
    document.getElementById('connectButton').classList.add("d-none");
    document.getElementById('disconnectButton').classList.add("d-none");      
  }
  console.debug(Date.now().toString() + " setIframeSrc end");
}

function updateLang(language) {
      var currentLanguage = sessionStorage.getItem('currentLanguage');
      if (language != currentLanguage) {
          if (currentLanguage) {
              document.getElementById(currentLanguage).classList.remove("active");
          }
          document.getElementById(language).classList.add("active");
          sessionStorage.setItem('currentLanguage', language);
      }

    lang = language;
    updateTexts();

    message = {};
    message.kind = 'lang';
    message.message = language;
    
    // When running without a webserver, there is a lot of 'strangeness'
    if (window.location.protocol == "file:") {
        targetOrigin = "*";
    }
    else {
        targetOrigin = window.location.origin;
    }      

    if (document.getElementById('child-iframe')) {
      document.getElementById('child-iframe').contentWindow.postMessage(message, targetOrigin);
    }
    else {
      window.self.postMessage(message, targetOrigin);
    }
}

// Handle a year being selected
function setYear(year) {
  // Handle 'year' and 'month' click/selections
    var url = "pages/" + year + ".html";
    setIframeSrc('child-iframe', url, false)
}

function resizeModal() {
  width = Math.max(document.documentElement.clientWidth, window.innerWidth || 0);
  height = Math.max(document.documentElement.clientHeight, window.innerHeight || 0);

  message = {};
  message.kind = 'resize';
  message.message = {};
  message.message.width = width;
  message.message.height = height - document.getElementById('navbar').clientHeight;

  // When running without a webserver, there is a lot of 'strangeness'
  if (window.location.protocol == "file:") {
      targetOrigin = "*";
  }
  else {
      targetOrigin = window.location.origin;
  }      

  iframe = document.getElementById('child-iframe')
  if (iframe) {
    iframe.contentWindow.postMessage(message, targetOrigin);
  }
  else {
    window.self.postMessage(message, targetOrigin);
  }
}

window.addEventListener("load", function (event) {
  var themes = ['light'];
  theme = sessionStorage.getItem('theme');
  if (!theme) {
    if (window.matchMedia('(prefers-color-scheme: dark)').media === 'not all') {
      theme = themes[0];
    }
    else {
      theme = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'
    }
  }
  setTheme(theme);

  window.addEventListener('scroll', function(event){
    iframe = document.getElementById('child-iframe')
    topOffset = iframe.getBoundingClientRect().top + window.scrollY;
    currentScroll = document.scrollingElement.scrollTop;


    message = {};
    message.kind = 'scroll';
    message.message = {};
    message.message.topOffset = topOffset;
    message.message.currentScroll = currentScroll;
   
    // When running without a webserver, there is a lot of 'strangeness'
    if (window.location.protocol == "file:") {
        targetOrigin = "*";
    }
    else {
        targetOrigin = window.location.origin;
    }      

    if (iframe) {
      iframe.contentWindow.postMessage(message, targetOrigin);
    }
    else {
      window.self.postMessage(message, targetOrigin);
    }
});




  updateTexts();

  if (sessionStorage.getItem('currentPage') === null) {
      sessionStorage.setItem('currentPage', '');

      setIframeSrc('child-iframe', 'pages/.html', false);
  }
  else
  {
    if (sessionStorage.getItem('addQueryString') == 'true') {
      addQueryString = true;
    }
    else {
      addQueryString = false;
    }
      setIframeSrc('child-iframe', sessionStorage.getItem('currentPage'), addQueryString);  
  }

    MQTTConnect();
  
  // Get the actual navbar width and then reset the auto sizing of its width
  navContainer = document.getElementById('nav-container');
  fullNavBarWidth = navContainer.offsetWidth;
  navContainer.classList.remove('w-auto');

  manageNavbar();
  document.body.style.viewport = "visible";
});

addEventListener("resize", (event) => {
  manageNavbar();
  width = Math.max(document.documentElement.clientWidth, window.innerWidth || 0);
  // width/100 is like the css variable vw
  fontSize = width/100 * 1.5;
  // Max is 18px and min is 10px
  document.getElementsByTagName("html")[0].style.fontSize = Math.min(18, Math.max(10, fontSize)) + "px";

  resizeModal();
});

window.addEventListener("beforeunload", function (event) {
  if(sessionStorage.getItem("MQTTConnected")){
    MQTTDisconnect();
  }
});

window.addEventListener('message', 
                        function(e) {
                          // message that was passed from iframe page
                          var kind = e.data.kind;
                          if (kind == undefined) {
                            return;
                          }
                          var message = e.data.message;

                          if (kind == 'resize') {
                              var iframe = document.querySelector("#child-iframe");
                              iframe.style.height = message.height + 'px';
                              //iframe.style.width = message.width + 'px';
                          }
                          if (kind == 'loaded') {
                            document.querySelector("#child-iframe").style.visibility = 'visible';
                            resizeModal();
                          }
                          
                        }, 
                        false);       

    
'''
