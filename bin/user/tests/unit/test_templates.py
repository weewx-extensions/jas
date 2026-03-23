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
        result = str(template)

        print("done")

    def testX(self):
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
        result = str(template)

        print("done")

    def testXY(self):
        page_data = types.SimpleNamespace(
            foo4 = {}
            #foo4 = ['a']
        )

        extras = types.SimpleNamespace(
            pages = page_data,
            chart_definitions = 'foo',
        )

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
            'logdbg': mock.Mock(),
        }

        skin_dir = os.path.dirname(__file__) + '/../../../../skins/jas/'
        # ToDo: wrap in a context?
        os.chdir(skin_dir)

        filename = 'generators/pages.gen'
        filename = 'generators/body.inc'

        #template = Cheetah.Template.Template(file=filename, searchList=[data])
        #template_source = Cheetah.Template.Template.compile(file=filename, returnAClass=False)
        template_class = Cheetah.Template.Template.compile(file=filename)
        class_source = Cheetah.Template.Template.generatedClassCode(template_class)
        module_source = Cheetah.Template.Template.generatedModuleCode(template_class)
        print('----')
        print(module_source)
        print('----')
        template_instance = template_class(searchList=[data])

        result = str(template_instance)

        print(result)

        print('{lang} {version} {Extras} {logdbg}'.format(**data))

        print("done")

if __name__ == '__main__':
    helpers.run_tests()
