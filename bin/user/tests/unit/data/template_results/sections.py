#    Copyright (c) 2026 Rich Bell <bellrichm@gmail.com>
#
#    See the file LICENSE.txt for your full rights.
#

# pylint: disable=wrong-import-order
# pylint: disable=missing-module-docstring, missing-class-docstring, missing-function-docstring
# pylint: disable=invalid-name

# pylint: disable=line-too-long
# pylint: disable=too-many-lines

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
