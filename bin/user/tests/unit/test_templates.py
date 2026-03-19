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

        print(result)
        print("done")

if __name__ == '__main__':
    helpers.run_tests()
