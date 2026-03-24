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

class TestCheetahTemplate(unittest.TestCase):
    def test(self):
        station = types.SimpleNamespace(
            station_url = 'foo.foo'
        )

        data = {
            'station': station,
        }

        skin_dir = os.path.dirname(__file__) + '/../../../../skins/jas/'

        filename = skin_dir + 'manifest.json.tmpl'

        template = Cheetah.Template.Template(file=filename, searchList=[data])
        str(template)
        #result = str(template)

        print("done")

    def test2(self):
        station = types.SimpleNamespace(
            location = 'foo.foo'
        )

        extras = types.SimpleNamespace(
            pages = 'foo',
        )

        data = {
            'lang': 'foo',
            'version': 'foo',
            'station': station,
            'Extras': extras,
            'HTML_ROOT': 'foo',
            'filename': 'foo',
            'logdbg': mock.Mock(),
        }

        skin_dir = os.path.dirname(__file__) + '/../../../../skins/jas/'

        filename = skin_dir + 'index.html.tmpl'

        template = Cheetah.Template.Template(file=filename, searchList=[data])
        str(template)
        # result = str(template)

        print("done")

    def testX(self):
        page_data = types.SimpleNamespace(
            foo4 = {}
            #foo4 = ['a']
        )

        extras = types.SimpleNamespace(
            pages = page_data,
            chart_definitions = 'foo',
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

        skin_dir = os.path.dirname(__file__) + '/../../../../skins/jas/'
        # ToDo: wrap in a context?
        # ToDO: Do once in class setup
        os.chdir(skin_dir)

        filename = 'generators/pages.gen'
        filename = 'generators/body.inc'

        template_class = Cheetah.Template.Template.compile(file=filename)
        print(f"----\n{Cheetah.Template.Template.generatedModuleCode(template_class)}\n----")

        template_instance = template_class(searchList=[data])
        result = str(template_instance)

        print(result)

        print("done")

if __name__ == '__main__':
    helpers.run_tests()
