#    Copyright (c) 2026 Rich Bell <bellrichm@gmail.com>
#
#    See the file LICENSE.txt for your full rights.
#

# pylint: disable=wrong-import-order
# pylint: disable=missing-module-docstring, missing-class-docstring, missing-function-docstring
# pylint: disable=invalid-name

# pylint: disable=line-too-long
# pylint: disable=too-many-lines

result_pages_minimal_configuration = \
'''


<!doctype html>
<html lang="foo1" data-bs-theme="light">
   <head>
      <!-- Required meta tags -->
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">

      <meta name="generator" content="jas foo2 foo3">
      

      <!-- Bootstrap CSS -->
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@latest/dist/css/bootstrap.min.css" rel="stylesheet">
      <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@latest/font/bootstrap-icons.min.css" rel="stylesheet">
      <link rel="stylesheet" type="text/css" href="../jas.css">
      <link rel="stylesheet" type="text/css" href="../user.css">

      <script src="https://cdn.jsdelivr.net/npm/echarts@latest/dist/echarts.min.js"></script>      <script src="https://cdn.jsdelivr.net/npm/moment@latest/moment.min.js"></script>
      <script src="../data/internationalization.js"></script>
      <script src="../data/foo4.js"></script>

      <script src="../javascript/foo5.js"></script>


      <!-- Optional JavaScript; choose one of the two! -->
      <!-- Option 1: Bootstrap Bundle with Popper -->
      <script src="https://cdn.jsdelivr.net/npm/bootstrap@latest/dist/js/bootstrap.bundle.min.js">      </script>

      <!-- Option 2: Separate Popper and Bootstrap JS -->
      <!--
      <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@latest/dist/umd/popper.min.js" ></script>
      <script src="https://cdn.jsdelivr.net/npm/bootstrap@latest/dist/js/bootstrap.min.js"></script>
      -->

   </head>
    <body onresize="refreshSizes()" onload="refreshSizes()">
      <div style="display: none;">
        <iframe id="data-iframe"></iframe>
      </div>



    <div class="container">


    </div>
      <script src="../charts/foo5.js"></script>
    
    <!-- Modal -->
<div class="modal" id="chartModal" tabindex="-1" role="dialog" aria-labelledby="chartModalTitle" aria-hidden="true">
  <div class="modal-dialog modal-xl" role="document">
    <div class="modal-content">
      <div class="modal-header" id="chartModalHeader">
        <h5 class="modal-title" id="chartModalTitle">Modal title</h5>
        <button type="button" class="close" data-bs-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body" id="chartModalBody">
        ...
      </div>
      <div class="modal-footer" id="chartModalFooter"></div>
    </div>
  </div>
</div>


    </body> 

  
'''

result_pages_zoom_control_configuration = \
'''


<!doctype html>
<html lang="foo1" data-bs-theme="light">
   <head>
      <!-- Required meta tags -->
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">

      <meta name="generator" content="jas foo2 foo3">
      
      <link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/gh/alumuko/vanilla-datetimerange-picker@latest/dist/vanilla-datetimerange-picker.css">
      <script src="https://cdn.jsdelivr.net/gh/alumuko/vanilla-datetimerange-picker@latest/dist/vanilla-datetimerange-picker.js"></script>

      <!-- Bootstrap CSS -->
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@latest/dist/css/bootstrap.min.css" rel="stylesheet">
      <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@latest/font/bootstrap-icons.min.css" rel="stylesheet">
      <link rel="stylesheet" type="text/css" href="../jas.css">
      <link rel="stylesheet" type="text/css" href="../user.css">

      <script src="https://cdn.jsdelivr.net/npm/echarts@latest/dist/echarts.min.js"></script>      <script src="https://cdn.jsdelivr.net/npm/moment@latest/moment.min.js"></script>
      <script src="../data/internationalization.js"></script>
      <script src="../data/foo4.js"></script>

      <script src="../javascript/foo5.js"></script>


      <!-- Optional JavaScript; choose one of the two! -->
      <!-- Option 1: Bootstrap Bundle with Popper -->
      <script src="https://cdn.jsdelivr.net/npm/bootstrap@latest/dist/js/bootstrap.bundle.min.js">      </script>

      <!-- Option 2: Separate Popper and Bootstrap JS -->
      <!--
      <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@latest/dist/umd/popper.min.js" ></script>
      <script src="https://cdn.jsdelivr.net/npm/bootstrap@latest/dist/js/bootstrap.min.js"></script>
      -->

   </head>
    <body onresize="refreshSizes()" onload="refreshSizes()">
      <div style="display: none;">
        <iframe id="data-iframe"></iframe>
      </div>



    <div class="container">
<div class="row mb-4 justify-content-center">
    <div class="col text-center">
        <a text_label="zoomControl_label"></a>
        <input type="text" id="zoomdatetimerange-input" style="text-align:center">   
        <button id="resetRange" text_label="resetRange_label" onclick="resetRange()"></button>
    </div>
</div>


    </div>
      <script src="../charts/foo5.js"></script>
    
    <!-- Modal -->
<div class="modal" id="chartModal" tabindex="-1" role="dialog" aria-labelledby="chartModalTitle" aria-hidden="true">
  <div class="modal-dialog modal-xl" role="document">
    <div class="modal-content">
      <div class="modal-header" id="chartModalHeader">
        <h5 class="modal-title" id="chartModalTitle">Modal title</h5>
        <button type="button" class="close" data-bs-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body" id="chartModalBody">
        ...
      </div>
      <div class="modal-footer" id="chartModalFooter"></div>
    </div>
  </div>
</div>


    </body> 

  
'''

result_pages_comparison_series = \
'''


<!doctype html>
<html lang="foo1" data-bs-theme="light">
   <head>
      <!-- Required meta tags -->
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">

      <meta name="generator" content="jas foo2 foo3">
      

      <!-- Bootstrap CSS -->
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@latest/dist/css/bootstrap.min.css" rel="stylesheet">
      <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@latest/font/bootstrap-icons.min.css" rel="stylesheet">
      <link rel="stylesheet" type="text/css" href="../jas.css">
      <link rel="stylesheet" type="text/css" href="../user.css">

      <script src="https://cdn.jsdelivr.net/npm/echarts@latest/dist/echarts.min.js"></script>      <script src="https://cdn.jsdelivr.net/npm/moment@latest/moment.min.js"></script>
      <script src="../data/internationalization.js"></script>
      <script src="../data/foo4.js"></script>
                <script src="../data/year9.js"></script>
      <script src="../data/yeartoyear.js"></script>

      <script src="../javascript/foo5.js"></script>


      <!-- Optional JavaScript; choose one of the two! -->
      <!-- Option 1: Bootstrap Bundle with Popper -->
      <script src="https://cdn.jsdelivr.net/npm/bootstrap@latest/dist/js/bootstrap.bundle.min.js">      </script>

      <!-- Option 2: Separate Popper and Bootstrap JS -->
      <!--
      <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@latest/dist/umd/popper.min.js" ></script>
      <script src="https://cdn.jsdelivr.net/npm/bootstrap@latest/dist/js/bootstrap.min.js"></script>
      -->

   </head>
    <body onresize="refreshSizes()" onload="refreshSizes()">
      <div style="display: none;">
        <iframe id="data-iframe"></iframe>
      </div>



    <div class="container">


    </div>
      <script src="../charts/foo5.js"></script>
    
    <!-- Modal -->
<div class="modal" id="chartModal" tabindex="-1" role="dialog" aria-labelledby="chartModalTitle" aria-hidden="true">
  <div class="modal-dialog modal-xl" role="document">
    <div class="modal-content">
      <div class="modal-header" id="chartModalHeader">
        <h5 class="modal-title" id="chartModalTitle">Modal title</h5>
        <button type="button" class="close" data-bs-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body" id="chartModalBody">
        ...
      </div>
      <div class="modal-footer" id="chartModalFooter"></div>
    </div>
  </div>
</div>


    </body> 

  
'''


result_pages_multiple_series = \
'''


<!doctype html>
<html lang="foo1" data-bs-theme="light">
   <head>
      <!-- Required meta tags -->
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">

      <meta name="generator" content="jas foo2 foo3">
      

      <!-- Bootstrap CSS -->
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@latest/dist/css/bootstrap.min.css" rel="stylesheet">
      <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@latest/font/bootstrap-icons.min.css" rel="stylesheet">
      <link rel="stylesheet" type="text/css" href="../jas.css">
      <link rel="stylesheet" type="text/css" href="../user.css">

      <script src="https://cdn.jsdelivr.net/npm/echarts@latest/dist/echarts.min.js"></script>      <script src="https://cdn.jsdelivr.net/npm/moment@latest/moment.min.js"></script>
      <script src="../data/internationalization.js"></script>
      <script src="../data/foo4.js"></script>
                <script src="../data/year9.js"></script>
      <script src="../data/multiyear.js"></script>

      <script src="../javascript/foo5.js"></script>


      <!-- Optional JavaScript; choose one of the two! -->
      <!-- Option 1: Bootstrap Bundle with Popper -->
      <script src="https://cdn.jsdelivr.net/npm/bootstrap@latest/dist/js/bootstrap.bundle.min.js">      </script>

      <!-- Option 2: Separate Popper and Bootstrap JS -->
      <!--
      <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@latest/dist/umd/popper.min.js" ></script>
      <script src="https://cdn.jsdelivr.net/npm/bootstrap@latest/dist/js/bootstrap.min.js"></script>
      -->

   </head>
    <body onresize="refreshSizes()" onload="refreshSizes()">
      <div style="display: none;">
        <iframe id="data-iframe"></iframe>
      </div>



    <div class="container">


    </div>
      <script src="../charts/foo5.js"></script>
    
    <!-- Modal -->
<div class="modal" id="chartModal" tabindex="-1" role="dialog" aria-labelledby="chartModalTitle" aria-hidden="true">
  <div class="modal-dialog modal-xl" role="document">
    <div class="modal-content">
      <div class="modal-header" id="chartModalHeader">
        <h5 class="modal-title" id="chartModalTitle">Modal title</h5>
        <button type="button" class="close" data-bs-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body" id="chartModalBody">
        ...
      </div>
      <div class="modal-footer" id="chartModalFooter"></div>
    </div>
  </div>
</div>


    </body> 

  
'''
result_pages_debug_page = \
'''


<!doctype html>
<html lang="foo1" data-bs-theme="light">
   <head>
      <!-- Required meta tags -->
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">

      <meta name="generator" content="jas foo2 foo3">
      

      <!-- Bootstrap CSS -->
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@latest/dist/css/bootstrap.min.css" rel="stylesheet">
      <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@latest/font/bootstrap-icons.min.css" rel="stylesheet">
      <link rel="stylesheet" type="text/css" href="../jas.css">
      <link rel="stylesheet" type="text/css" href="../user.css">

      <script src="https://cdn.jsdelivr.net/npm/echarts@latest/dist/echarts.min.js"></script>      <script src="https://cdn.jsdelivr.net/npm/moment@latest/moment.min.js"></script>
      <script src="../data/internationalization.js"></script>
      <script src="../data/foo4.js"></script>

      <script src="../javascript/debug.js"></script>

      <script src="https://cdn.jsdelivr.net/npm/paho-mqtt@latest/paho-mqtt.min.js"></script>      <script src="../javascript/mqtt.js"></script>

      <!-- Optional JavaScript; choose one of the two! -->
      <!-- Option 1: Bootstrap Bundle with Popper -->
      <script src="https://cdn.jsdelivr.net/npm/bootstrap@latest/dist/js/bootstrap.bundle.min.js">      </script>

      <!-- Option 2: Separate Popper and Bootstrap JS -->
      <!--
      <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@latest/dist/umd/popper.min.js" ></script>
      <script src="https://cdn.jsdelivr.net/npm/bootstrap@latest/dist/js/bootstrap.min.js"></script>
      -->

   </head>
    <body onresize="refreshSizes()" onload="refreshSizes()">
      <div style="display: none;">
        <iframe id="data-iframe"></iframe>
      </div>



    <div class="container">


    </div>
      <script src="../charts/debug.js"></script>
    
    <!-- Modal -->
<div class="modal" id="chartModal" tabindex="-1" role="dialog" aria-labelledby="chartModalTitle" aria-hidden="true">
  <div class="modal-dialog modal-xl" role="document">
    <div class="modal-content">
      <div class="modal-header" id="chartModalHeader">
        <h5 class="modal-title" id="chartModalTitle">Modal title</h5>
        <button type="button" class="close" data-bs-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body" id="chartModalBody">
        ...
      </div>
      <div class="modal-footer" id="chartModalFooter"></div>
    </div>
  </div>
</div>


    </body> 

  
'''
