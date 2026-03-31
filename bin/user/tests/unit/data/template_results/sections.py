#    Copyright (c) 2026 Rich Bell <bellrichm@gmail.com>
#
#    See the file LICENSE.txt for your full rights.
#

# pylint: disable=wrong-import-order
# pylint: disable=missing-module-docstring, missing-class-docstring, missing-function-docstring
# pylint: disable=invalid-name

# pylint: disable=line-too-long
# pylint: disable=too-many-lines

result_chart_minimal_configuration = \
'''

                                
                                
                              
             
<div class="grid-cols01">
    <div class="card">
    <div class="card-body text-center">
               <h5 class="card-title" text_label="section-01_title" data-bs-toggle="modal" data-bs-target="#chartModal" role="button" data-bs-chart="section-01global-page-01" data-bs-title="section-01_title">
        </h5>
        <div id="section-01global-page-01"></div>
    </div>
    </div>   
</div>   '''

result_chart_configuration = \
'''

                                
                                
             
<div class="grid-cols01">
    <div class="card">
    <div class="card-body text-center">
               <h5 class="card-title"  data-bs-chart="section-01global-page-01" data-bs-title="title-01">            title-01
        </h5>
        <div id="section-01global-page-01"></div>
    </div>
    </div>   
</div>   '''

result_current_minimal_configuration = \
'''

<div class="grid-cols01">
    <div class="card">
        <div class="card-body text-center">
                <table class="table">
                  <tbody>
                </tbody>
            </table>
            <div id="updateDateDiv"></div>
        </div>
    </div>
</div>'''

result_current_configuration = \
'''
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
                <h5 class="text-center w-100" id="currentModalTitle"></h5>
                <div id='currentObservationModal' class="text-center">
                </div>
                <div id='currentAQIModal' class="text-center">
                </div>
                <div id='currentAlertModal' class="text-center">
                </div>
                <table class="table">
                    <tbody>
                             <tr class="row mx0"> 
                                <th scope="row" class="col" obs_label="obs-02"></th>
                                <td id="obs-02_value_modal" class="col"></td>
                            
                            
                                <th scope="row" class="col" obs_label="obs-03"></th>
                                <td id="obs-03_value_modal" class="col"></td>
                             </tr> 
                    </tbody>
                </table>
                <div id="updateModalDate" class="text-center"></div>
          
            </div>
            <div class="modal-footer" id="currentModalFooter"></div>
        </div>
    </div>
</div>'''

result_current_modal_minimal_configuration = \
'''
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
                    </tbody>
                </table>
                <div id="updateModalDate" class="text-center"></div>
          
            </div>
            <div class="modal-footer" id="currentModalFooter"></div>
        </div>
    </div>
</div>'''

result_current_modal_configuration = \
'''
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
                <h5 class="text-center w-100" id="currentModalTitle"></h5>
                <div id='currentObservationModal' class="text-center">
                </div>
                <div id='currentAQIModal' class="text-center">
                </div>
                <div id='currentAlertModal' class="text-center">
                </div>
                <table class="table">
                    <tbody>
                             <tr class="row mx0"> 
                                <th scope="row" class="col" obs_label="obs-02"></th>
                                <td id="obs-02_value_modal" class="col"></td>
                            
                            
                                <th scope="row" class="col" obs_label="obs-03"></th>
                                <td id="obs-03_value_modal" class="col"></td>
                             </tr> 
                    </tbody>
                </table>
                <div id="updateModalDate" class="text-center"></div>
          
            </div>
            <div class="modal-footer" id="currentModalFooter"></div>
        </div>
    </div>
</div>'''

result_minmax_configuration = \
'''
<div class="grid-cols01">
    <div class="card">
        <div class="card-body text-center">
                <h5 class="card-title"  text_label="minmax_title"></h5>
                </h5>        
                <table class="table">
                  <tbody>
                        <tr class="row mx0">
                            <th class="col" scope="row" obs_label="obs-01"></th>
                            <td id="obs-01_minmax_min" class="col">
                            </td>
                            <td id="obs-01_minmax_max" class="col">
                            </td>
                        </tr>
                        <tr class="row mx0">
                            <th class="col" scope="row" obs_label="obs-02"></th>
                            <td id="obs-02_minmax_min" class="col">
                            </td>
                            <td id="obs-02_minmax_max" class="col">
                            </td>
                        </tr>
                </tbody>
            </table>
        </div>
    </div>
</div>'''

result_thisdate_configuration = \
'''
<div class="grid-cols01">
    <div class="card">
        <div class="card-body text-center">
                <h5 class="card-title"  text_label="thisdate_title"></h5>
                </h5>     
                <input type="text" id="thisdatetimerange-input" style="text-align:center">   
                <table class="table">
                  <tbody>
                        <tr  class="row mx0">
                        <th class="col" scope="row" obs_label="obs-01"></th>
                            <td id="obs-01_thisdate_foo1" class="col">
                            </td>
                            <td class="col"></td>
                        </tr>    
                        <tr  class="row mx0">
                        <th class="col" scope="row" obs_label="obs-02"></th>
                            <td id="obs-02_thisdate_min" class="col">
                            </td>               
                            <td id="obs-02_thisdate_max" class="col">
                            </td>                                                          
                        </tr>    
                </tbody>
                </table>     
        </div>
    </div>
</div>
'''