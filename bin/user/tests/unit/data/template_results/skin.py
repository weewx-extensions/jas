#    Copyright (c) 2026 Rich Bell <bellrichm@gmail.com>
#
#    See the file LICENSE.txt for your full rights.
#

# pylint: disable=wrong-import-order
# pylint: disable=missing-module-docstring, missing-class-docstring, missing-function-docstring
# pylint: disable=invalid-name

# pylint: disable=line-too-long
# pylint: disable=too-many-lines

result_index_min_configuration = \
'''



<!doctype html>
<html lang="foo1" data-bs-theme="light">
   <head>
      <style>
         body iframe {visibility:hidden}
      </style>
      <!-- Required meta tags -->
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      
      <meta name="generator" content="jas foo2">
      <link rel="apple-touch-icon" sizes="180x180" href="icon/apple-touch-icon.png">
      <link rel="icon" type="image/png" sizes="32x32" href="icon/favicon-32x32.png">
      <link rel="icon" type="image/png" sizes="16x16" href="icon/favicon-16x16.png"> 
      <link rel="manifest" href="manifest.json">

      <!-- Bootstrap CSS -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@latest/dist/css/bootstrap.min.css" rel="stylesheet"><link rel="stylesheet" type="text/css" href="jas.css"><link rel="stylesheet" type="text/css" href="user.css">
<script src="https://cdn.jsdelivr.net/npm/paho-mqtt@latest/paho-mqtt.min.js"></script>
      <script src="data/internationalization.js"></script>
      <script src="javascript/index.js"></script>
      <script src="javascript/mqtt.js"></script>


      <!-- Optional JavaScript; choose one of the two! -->

      <!-- Option 1: Bootstrap Bundle with Popper -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@latest/dist/js/bootstrap.bundle.min.js"></script>
      <!-- Option 2: Separate Popper and Bootstrap JS -->
      <!--
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@latest/dist/umd/popper.min.js" ></script><script src="https://cdn.jsdelivr.net/npm/bootstrap@latest/dist/js/bootstrap.min.js"></script>      -->
   </head>      
    
   <body>

      <script src="dataload/index.js"> </script>

      <div class="fixed-top">
         <nav id="navbar" class="navbar navbar-expand">
            <div id="nav-container" class="container-fluid w-auto">
               <a class="navbar-brand" href="#">foo3</a>
               <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
                  <span class="navbar-toggler-icon"></span>
               </button>
               <div class="collapse navbar-collapse" id="navbarCollapse">
                  <ul class="navbar-nav me-auto mb-2 mb-md-0 navbar-nav-scroll">
                  </ul>
                  <div class="form-check form-switch">
                  <input class="form-check-input" type="checkbox" role="switch" id="themeSelection"  data-bs-toggle="collapse" data-bs-target=".navbar-collapse" onchange="updateTheme(this)">
                  </div>
                  <button id="connectButton" class="btn d-none" type="button" text_label="connect_button_label" data-bs-toggle="collapse" data-bs-target=".navbar-collapse" onclick="MQTTConnect()"></button>
                  <button id="disconnectButton" class="btn d-none" type="button" text_label="disconnect_button_label" data-bs-toggle="collapse" data-bs-target=".navbar-collapse" onclick="MQTTDisconnect()"></button>
               </div>
               <button id=refreshButton class="btn" type="button" onclick="refreshData()" text_label="refresh_button_label"></button>
            </div>
         </nav>
      </div>
      <div class="embed-responsive mt-5 pt-5">
         <iframe id="child-iframe" scrolling="no" width="100%"></iframe>
      </div>
   </body>
</html>

  
'''

result_index_build_navigation = \
'''



<!doctype html>
<html lang="foo1" data-bs-theme="light">
   <head>
      <style>
         body iframe {visibility:hidden}
      </style>
      <!-- Required meta tags -->
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      
      <meta name="generator" content="jas foo2">
      <link rel="apple-touch-icon" sizes="180x180" href="icon/apple-touch-icon.png">
      <link rel="icon" type="image/png" sizes="32x32" href="icon/favicon-32x32.png">
      <link rel="icon" type="image/png" sizes="16x16" href="icon/favicon-16x16.png"> 
      <link rel="manifest" href="manifest.json">

      <!-- Bootstrap CSS -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@latest/dist/css/bootstrap.min.css" rel="stylesheet"><link rel="stylesheet" type="text/css" href="jas.css"><link rel="stylesheet" type="text/css" href="user.css">
<script src="https://cdn.jsdelivr.net/npm/paho-mqtt@latest/paho-mqtt.min.js"></script>
      <script src="data/internationalization.js"></script>
      <script src="javascript/index.js"></script>
      <script src="javascript/mqtt.js"></script>


      <!-- Optional JavaScript; choose one of the two! -->

      <!-- Option 1: Bootstrap Bundle with Popper -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@latest/dist/js/bootstrap.bundle.min.js"></script>
      <!-- Option 2: Separate Popper and Bootstrap JS -->
      <!--
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@latest/dist/umd/popper.min.js" ></script><script src="https://cdn.jsdelivr.net/npm/bootstrap@latest/dist/js/bootstrap.min.js"></script>      -->
   </head>      
    
   <body>

      <script src="dataload/index.js"> </script>

      <div class="fixed-top">
         <nav id="navbar" class="navbar navbar-expand">
            <div id="nav-container" class="container-fluid w-auto">
               <a class="navbar-brand" href="#">foo3</a>
               <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
                  <span class="navbar-toggler-icon"></span>
               </button>
               <div class="collapse navbar-collapse" id="navbarCollapse">
                  <ul class="navbar-nav me-auto mb-2 mb-md-0 navbar-nav-scroll">
                             <li class="nav-item">
                                <a id= "pages/page-01.html" class="nav-link text-nowrap" role="button" onclick="setIframeSrc('child-iframe', 'pages/page-01.html', false)" data-bs-toggle="collapse" data-bs-target=".navbar-collapse" text_label="page-01_navbarText"></a>
                             </li>
                                <li class="nav-item dropdown">
                                   <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false" text_label="more_dropdown_label">
                                   </a>
                                   <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                             <a id= "pages/page-02.html" class="dropdown-item nav-link text-nowrap" role="button" onclick="setIframeSrc('child-iframe', 'pages/page-02.html', false)" data-bs-toggle="collapse" data-bs-target=".navbar-collapse" text_label="page-02_navbarText"></a>
                                   </ul>
                                </li>                        
                             <li class="nav-item">
                                <a id= "pages/page-03.html" class="nav-link text-nowrap" role="button" onclick="setIframeSrc('child-iframe', 'pages/page-03.html', true)" data-bs-toggle="collapse" data-bs-target=".navbar-collapse" text_label="page-03_navbarText"></a>
                             </li>
                                <li class="nav-item dropdown">
                                   <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false" text_label="more_dropdown_label">
                                   </a>
                                   <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                             <a id= "pages/page-04.html" class="dropdown-item nav-link text-nowrap" role="button" onclick="setIframeSrc('child-iframe', 'pages/page-04.html', false)" data-bs-toggle="collapse" data-bs-target=".navbar-collapse" text_label="page-04_navbarText"></a>
                              </ul>
                           </li>                        
                  </ul>
                  <div class="form-check form-switch">
                  <input class="form-check-input" type="checkbox" role="switch" id="themeSelection"  data-bs-toggle="collapse" data-bs-target=".navbar-collapse" onchange="updateTheme(this)">
                  </div>
                  <button id="connectButton" class="btn d-none" type="button" text_label="connect_button_label" data-bs-toggle="collapse" data-bs-target=".navbar-collapse" onclick="MQTTConnect()"></button>
                  <button id="disconnectButton" class="btn d-none" type="button" text_label="disconnect_button_label" data-bs-toggle="collapse" data-bs-target=".navbar-collapse" onclick="MQTTDisconnect()"></button>
               </div>
               <button id=refreshButton class="btn" type="button" onclick="refreshData()" text_label="refresh_button_label"></button>
            </div>
         </nav>
      </div>
      <div class="embed-responsive mt-5 pt-5">
         <iframe id="child-iframe" scrolling="no" width="100%"></iframe>
      </div>
   </body>
</html>

  
'''

result_index_build_navigation_month = \
'''



<!doctype html>
<html lang="foo1" data-bs-theme="light">
   <head>
      <style>
         body iframe {visibility:hidden}
      </style>
      <!-- Required meta tags -->
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      
      <meta name="generator" content="jas foo2">
      <link rel="apple-touch-icon" sizes="180x180" href="icon/apple-touch-icon.png">
      <link rel="icon" type="image/png" sizes="32x32" href="icon/favicon-32x32.png">
      <link rel="icon" type="image/png" sizes="16x16" href="icon/favicon-16x16.png"> 
      <link rel="manifest" href="manifest.json">

      <!-- Bootstrap CSS -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@latest/dist/css/bootstrap.min.css" rel="stylesheet"><link rel="stylesheet" type="text/css" href="jas.css"><link rel="stylesheet" type="text/css" href="user.css">
<script src="https://cdn.jsdelivr.net/npm/paho-mqtt@latest/paho-mqtt.min.js"></script>
      <script src="data/internationalization.js"></script>
      <script src="javascript/index.js"></script>
      <script src="javascript/mqtt.js"></script>


      <!-- Optional JavaScript; choose one of the two! -->

      <!-- Option 1: Bootstrap Bundle with Popper -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@latest/dist/js/bootstrap.bundle.min.js"></script>
      <!-- Option 2: Separate Popper and Bootstrap JS -->
      <!--
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@latest/dist/umd/popper.min.js" ></script><script src="https://cdn.jsdelivr.net/npm/bootstrap@latest/dist/js/bootstrap.min.js"></script>      -->
   </head>      
    
   <body>

      <script src="dataload/index.js"> </script>

      <div class="fixed-top">
         <nav id="navbar" class="navbar navbar-expand">
            <div id="nav-container" class="container-fluid w-auto">
               <a class="navbar-brand" href="#">foo3</a>
               <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
                  <span class="navbar-toggler-icon"></span>
               </button>
               <div class="collapse navbar-collapse" id="navbarCollapse">
                  <ul class="navbar-nav me-auto mb-2 mb-md-0 navbar-nav-scroll">
                              <li class="nav-item dropdown">
                              <div class="dropdown">
                                 <a class="nav-link dropdown-toggle" href="#" role="button" id="dropdownYearMonth" role="button" data-bs-toggle="dropdown" aria-expanded="false" text_label="yearMonth_dropdown_label">
                                 </a>
                                 <ul class="dropdown-menu pre-scrollable" aria-labelledby="dropdownYearMonth" id="dropdownYearMonthMenu">
                                 </ul>
                              </div>
                              </li>
                  </ul>
                  <div class="form-check form-switch">
                  <input class="form-check-input" type="checkbox" role="switch" id="themeSelection"  data-bs-toggle="collapse" data-bs-target=".navbar-collapse" onchange="updateTheme(this)">
                  </div>
                  <button id="connectButton" class="btn d-none" type="button" text_label="connect_button_label" data-bs-toggle="collapse" data-bs-target=".navbar-collapse" onclick="MQTTConnect()"></button>
                  <button id="disconnectButton" class="btn d-none" type="button" text_label="disconnect_button_label" data-bs-toggle="collapse" data-bs-target=".navbar-collapse" onclick="MQTTDisconnect()"></button>
               </div>
               <button id=refreshButton class="btn" type="button" onclick="refreshData()" text_label="refresh_button_label"></button>
            </div>
         </nav>
      </div>
      <div class="embed-responsive mt-5 pt-5">
         <iframe id="child-iframe" scrolling="no" width="100%"></iframe>
      </div>
   </body>
</html>

  
'''


result_index_build_navigation_year = \
'''



<!doctype html>
<html lang="foo1" data-bs-theme="light">
   <head>
      <style>
         body iframe {visibility:hidden}
      </style>
      <!-- Required meta tags -->
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      
      <meta name="generator" content="jas foo2">
      <link rel="apple-touch-icon" sizes="180x180" href="icon/apple-touch-icon.png">
      <link rel="icon" type="image/png" sizes="32x32" href="icon/favicon-32x32.png">
      <link rel="icon" type="image/png" sizes="16x16" href="icon/favicon-16x16.png"> 
      <link rel="manifest" href="manifest.json">

      <!-- Bootstrap CSS -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@latest/dist/css/bootstrap.min.css" rel="stylesheet"><link rel="stylesheet" type="text/css" href="jas.css"><link rel="stylesheet" type="text/css" href="user.css">
<script src="https://cdn.jsdelivr.net/npm/paho-mqtt@latest/paho-mqtt.min.js"></script>
      <script src="data/internationalization.js"></script>
      <script src="javascript/index.js"></script>
      <script src="javascript/mqtt.js"></script>


      <!-- Optional JavaScript; choose one of the two! -->

      <!-- Option 1: Bootstrap Bundle with Popper -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@latest/dist/js/bootstrap.bundle.min.js"></script>
      <!-- Option 2: Separate Popper and Bootstrap JS -->
      <!--
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@latest/dist/umd/popper.min.js" ></script><script src="https://cdn.jsdelivr.net/npm/bootstrap@latest/dist/js/bootstrap.min.js"></script>      -->
   </head>      
    
   <body>

      <script src="dataload/index.js"> </script>

      <div class="fixed-top">
         <nav id="navbar" class="navbar navbar-expand">
            <div id="nav-container" class="container-fluid w-auto">
               <a class="navbar-brand" href="#">foo3</a>
               <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
                  <span class="navbar-toggler-icon"></span>
               </button>
               <div class="collapse navbar-collapse" id="navbarCollapse">
                  <ul class="navbar-nav me-auto mb-2 mb-md-0 navbar-nav-scroll">
                              <li class="nav-item dropdown">
                              <a class="nav-link dropdown-toggle" href="#" id="dropdownYear" role="button" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false" text_label="year_dropdown_label">
                              </a>
                              <div class="dropdown-menu" aria-labelledby="dropdownYear" id="dropdownYearMenu">
                              </li>
                  </ul>
                  <div class="form-check form-switch">
                  <input class="form-check-input" type="checkbox" role="switch" id="themeSelection"  data-bs-toggle="collapse" data-bs-target=".navbar-collapse" onchange="updateTheme(this)">
                  </div>
                  <button id="connectButton" class="btn d-none" type="button" text_label="connect_button_label" data-bs-toggle="collapse" data-bs-target=".navbar-collapse" onclick="MQTTConnect()"></button>
                  <button id="disconnectButton" class="btn d-none" type="button" text_label="disconnect_button_label" data-bs-toggle="collapse" data-bs-target=".navbar-collapse" onclick="MQTTDisconnect()"></button>
               </div>
               <button id=refreshButton class="btn" type="button" onclick="refreshData()" text_label="refresh_button_label"></button>
            </div>
         </nav>
      </div>
      <div class="embed-responsive mt-5 pt-5">
         <iframe id="child-iframe" scrolling="no" width="100%"></iframe>
      </div>
   </body>
</html>

  
'''
