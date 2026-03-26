#    Copyright (c) 2026 Rich Bell <bellrichm@gmail.com>
#
#    See the file LICENSE.txt for your full rights.
#

# pylint: disable=wrong-import-order
# pylint: disable=missing-module-docstring, missing-class-docstring, missing-function-docstring
# pylint: disable=invalid-name

# pylint: disable=line-too-long
# pylint: disable=too-many-lines

result_page_has_no_sections = \
'''


    <div class="container">


    </div>
      <script src="../charts/bar2.js"></script>
    
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


'''

result_page_has_zoom_control = \
'''


    <div class="container">
<div class="row mb-4 justify-content-center">
    <div class="col text-center">
        <a text_label="zoomControl_label"></a>
        <input type="text" id="zoomdatetimerange-input" style="text-align:center">   
        <button id="resetRange" text_label="resetRange_label" onclick="resetRange()"></button>
    </div>
</div>


    </div>
      <script src="../charts/bar2.js"></script>
    
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


'''

result_page_has_section_debug = \
'''


    <div class="container">

            <div class="row graphrow align-content-start">

<button id="connectButton" class="btn d-none" type="button" text_label="connect_button_label" onclick="MQTTConnect()"></button>
<button id="disconnectButton" class="btn d-none" type="button" text_label="disconnect_button_label" onclick="MQTTDisconnect()"></button>

<div class="col-sm-10 mb-4">
  <button type="button" class="btn" onclick="copyLog()">Copy Log</button>
  <button type="button" class="btn" onclick="clearLog()">Clear Log</button>
</div>

<div class="col-sm-10 mb-4">
  <div class="text-wrap" id="logDisplay"
    style="overflow-y:scroll; height:300px">
  </div>
</div>

<script>
  if (window.self === window.top) {
    document.getElementById('connectButton').classList.remove("d-none");
    document.getElementById('disconnectButton').classList.remove("d-none");
  }
</script> 
      </div>
    </div>
      <script src="../charts/bar2.js"></script>
    
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


'''

result_page_has_file_alert_modal_inc = \
'''


    <div class="container">

            <div class="row graphrow align-content-start">

<div class="modal" id="alertModal" tabindex="-1" role="dialog" aria-labelledby="alertModalTitle" aria-hidden="true">
    <div class="modal-dialog modal-xl" role="document">
        <div class="modal-content">
            <div class="modal-header" id="alertModalHeader">
                <h5 class="modal-title"></h5>
                <button type="button" class="close" data-bs-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                </button>
            </div>
            <div class="modal-body" id="alertModalBody">
                <div id="alertDetailModal" class="text-center"></div>
            </div>
            <div class="modal-footer" id="alertModalFooter"></div>
        </div>
    </div>
</div>
      </div>
    </div>
      <script src="../charts/bar2.js"></script>
    
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


'''

result_page_layout_is_not_grid = \
'''


    <div class="container">


<button id="connectButton" class="btn d-none" type="button" text_label="connect_button_label" onclick="MQTTConnect()"></button>
<button id="disconnectButton" class="btn d-none" type="button" text_label="disconnect_button_label" onclick="MQTTDisconnect()"></button>

<div class="col-sm-10 mb-4">
  <button type="button" class="btn" onclick="copyLog()">Copy Log</button>
  <button type="button" class="btn" onclick="clearLog()">Clear Log</button>
</div>

<div class="col-sm-10 mb-4">
  <div class="text-wrap" id="logDisplay"
    style="overflow-y:scroll; height:300px">
  </div>
</div>

<script>
  if (window.self === window.top) {
    document.getElementById('connectButton').classList.remove("d-none");
    document.getElementById('disconnectButton').classList.remove("d-none");
  }
</script>           </div>

    </div>
      <script src="../charts/bar2.js"></script>
    
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


'''

result_page_current_has_modal = \
'''


    <div class="container">


    </div>
      <script src="../charts/bar2.js"></script>
    
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


<div class="modal" id="currentModal" tabindex="-1" role="dialog" aria-labelledby="currentModalTitle" aria-hidden="true">
    <div class="modal-dialog modal-xl" role="document">
        <div class="modal-content">
            <div class="modal-header" id="currentModalHeader">
                <h5 class="modal-title"></h5>
                <button type="button" class="close" data-bs-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                </button>
            </div>
            <div class="modal-body" id="currentModalBody">
                <table class="table">
                    <tbody>
                             <tr class="row mx0"> 
                                <th scope="row" class="col" obs_label="obs1"></th>
                                <td id="obs1_value_modal" class="col"></td>
                            
                    </tbody>
                </table>
                <div id="updateModalDate" class="text-center"></div>
          
            </div>
            <div class="modal-footer" id="currentModalFooter"></div>
        </div>
    </div>
</div>
'''

result_page_display_aeris_alerts = \
'''


    <div class="container">


    </div>
      <script src="../charts/bar2.js"></script>
    
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


<div class="modal" id="currentModal" tabindex="-1" role="dialog" aria-labelledby="currentModalTitle" aria-hidden="true">
    <div class="modal-dialog modal-xl" role="document">
        <div class="modal-content">
            <div class="modal-header" id="currentModalHeader">
                <h5 class="modal-title"></h5>
                <button type="button" class="close" data-bs-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                </button>
            </div>
            <div class="modal-body" id="currentModalBody">
                <div id='currentAlertModal' class="text-center">
                </div>
                <table class="table">
                    <tbody>
                             <tr class="row mx0"> 
                                <th scope="row" class="col" obs_label="obs1"></th>
                                <td id="obs1_value_modal" class="col"></td>
                            
                    </tbody>
                </table>
                <div id="updateModalDate" class="text-center"></div>
          
            </div>
            <div class="modal-footer" id="currentModalFooter"></div>
        </div>
    </div>
</div>

<div class="modal" id="alertModal" tabindex="-1" role="dialog" aria-labelledby="alertModalTitle" aria-hidden="true">
    <div class="modal-dialog modal-xl" role="document">
        <div class="modal-content">
            <div class="modal-header" id="alertModalHeader">
                <h5 class="modal-title"></h5>
                <button type="button" class="close" data-bs-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                </button>
            </div>
            <div class="modal-body" id="alertModalBody">
                <div id="alertDetailModal" class="text-center"></div>
            </div>
            <div class="modal-footer" id="alertModalFooter"></div>
        </div>
    </div>
</div>'''
