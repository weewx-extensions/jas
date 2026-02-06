#    Copyright (c) 2025-2026 Rich Bell <bellrichm@gmail.com>
#
#    See the file LICENSE.txt for your full rights.
#

# pylint: disable=wrong-import-order
# pylint: disable=missing-module-docstring, missing-class-docstring, missing-function-docstring
# pylint: disable=invalid-name

import configobj

import unittest
import mock

from user.tests import helpers
import user.jas

class TestConfiguration(unittest.TestCase):
    def test_enable_is_false(self):
        print("start")

        config_dict = {
            'StdReport': {
                'jas': {
                    'enable': False
                }
            }
        }
        config = configobj.ConfigObj(config_dict)

        mock_generator = mock.Mock()
        mock_generator.skin_dict = config

        with self.assertRaises(AttributeError) as error:
            user.jas.JAS(mock_generator)

        self.assertEqual(error.exception.args[0], "'lang' setting is required.")

        print("end")

if __name__ == '__main__':
    helpers.run_tests()
