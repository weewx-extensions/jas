#    Copyright (c) 2026 Rich Bell <bellrichm@gmail.com>
#
#    See the file LICENSE.txt for your full rights.
#

# pylint: disable=wrong-import-order
# pylint: disable=missing-module-docstring, missing-class-docstring, missing-function-docstring
# pylint: disable=invalid-name

import unittest

import Cheetah.Template
import os
import types

from user.tests import helpers

from user.tests.unit.data.template_results.body_inc import result_page_has_no_sections, result_page_has_zoom_control

class TestBodyInc(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        skin_dir = os.path.dirname(__file__) + '/../../../../skins/jas/'
        os.chdir(skin_dir)

    def test_page_has_no_sections(self):
        self.maxDiff = None

        page_name = 'foo1'
        section_data = 'foo2'
        extras = types.SimpleNamespace(
            pages = {
                page_name: {
                    'section': section_data
                }
            },
            chart_definitions = 'bar1',
            current = {
                'observations': {
                    'obs1': {
                        'display': False
                    }
                }
            },
        )

        data = {
            'page': page_name,
            'Extras': extras,
            'page_name_global': 'bar2',
        }

        filename = 'generators/body.inc'

        template_class = Cheetah.Template.Template.compile(file=filename)
        # print(f"----\n{Cheetah.Template.Template.generatedModuleCode(template_class)}\n----")
        template_instance = template_class(searchList=[data])
        result = template_instance.respond()
        self.assertEqual(result, result_page_has_no_sections)

    def test_page_has_zoom_control(self):
        self.maxDiff = None

        page_name = 'foo1'
        section_name = 'foo2'
        extras = types.SimpleNamespace(
            pages = {
                page_name: {
                    'section': section_name,
                    'zoomControl': True
                }
            },
            chart_definitions = 'bar1',
            current = {
                'observations': {
                    'obs1': {
                        'display': False
                    }
                }
            },
        )

        data = {
            'page': page_name,
            'Extras': extras,
            'page_name_global': 'bar2',
        }

        filename = 'generators/body.inc'

        template_class = Cheetah.Template.Template.compile(file=filename)
        # print(f"----\n{Cheetah.Template.Template.generatedModuleCode(template_class)}\n----")
        template_instance = template_class(searchList=[data])
        result = template_instance.respond()
        self.assertEqual(result, result_page_has_zoom_control)

if __name__ == '__main__':
    helpers.run_tests()
