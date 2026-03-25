#    Copyright (c) 2026 Rich Bell <bellrichm@gmail.com>
#
#    See the file LICENSE.txt for your full rights.
#

# pylint: disable=wrong-import-order
# pylint: disable=missing-module-docstring, missing-class-docstring, missing-function-docstring
# pylint: disable=invalid-name

import unittest
import mock

import Cheetah.Template
import os
import types

from user.tests import helpers

class TestTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        skin_dir = os.path.dirname(__file__) + '/../../../../skins/jas/'
        os.chdir(skin_dir)

    def testXY(self):
        extras = types.SimpleNamespace(
            current = {
                'observations': {
                    'obs1': {
                        'display': False
                    }
                }
            },
        )

        data = {
            'Extras': extras,
        }

        source = \
        '''
source-foo

#from weeutil.weeutil import to_bool, to_list

#set $local_var = 'local'
#set global current_modal_global = False
$current_modal_global

#if $getVar('$Extras.current', False)
  #for observation in $getVar('$Extras.current.observations', {})
      #if 'modal' in to_list($getVar('$Extras.current.observations.' + $observation + '.display', ['page', 'modal']))
          #set global current_modal_global = True
          #break
      #end if
  #end for
#end if

------
$current_modal_global
to_list($getVar('$Extras.current.observations.' + $observation + '.display', ['page', 'modal']))
$getVar('$Extras.current.observations.' + $observation + '.display', ['page', 'modal'])
$getVar('$Extras.current.observations')
$local_var
source-bar
        '''

        template_class = Cheetah.Template.Template.compile(source=source)
        print(f"----\n{Cheetah.Template.Template.generatedModuleCode(template_class)}\n----")

        template_instance = template_class(searchList=[data])
        result = template_instance.respond()

        print(template_instance.getVar('current_modal_global'))
        # print(result)
        print("done")

    def testX(self):
        print("start")

        page_data = types.SimpleNamespace(
            foo4 = {}
            #foo4 = ['a']
        )

        extras = types.SimpleNamespace(
            pages = page_data,
            chart_definitions = 'foo',
            current = {
                'observations': {
                    'obs1': {
                        'display': False
                    }
                }
            },
        )

        mock_logdbg = mock.Mock()
        data = {
            'lang': 'foo1',
            'version': 'foo2',
            'genTime': 'foo3',
            'page': 'foo4',
            'Extras': extras,
            'interval_name_global': 'foo',
            'page_name_global': 'foo',
            'HTML_ROOT': 'foo',
            'filename': 'foo',
            'logdbg': mock_logdbg,
        }

        filename = 'generators/body.inc'

        template_class = Cheetah.Template.Template.compile(file=filename)
        print(f"----\n{Cheetah.Template.Template.generatedModuleCode(template_class)}\n----")

        template_instance = template_class(searchList=[data])
        result = template_instance.respond()
        print(result)

        print("done")

if __name__ == '__main__':
    helpers.run_tests()
