#    Copyright (c) 2025-2026 Rich Bell <bellrichm@gmail.com>
#
#    See the file LICENSE.txt for your full rights.
#

# pylint: disable=wrong-import-order
# pylint: disable=missing-module-docstring, missing-class-docstring, missing-function-docstring
# pylint: disable=invalid-name

import configobj
import time

import unittest
import mock

from user.tests import helpers
import user.jas

class TestConfiguration(unittest.TestCase):
    def test1(self):
        print("start")
        now = int(time.time())

        mock_generator = mock.Mock()

        chart_name = helpers.random_string('chart-1')
        skin_dict = {
            'lang': helpers.random_string(),
            'data_binding': helpers.random_string(),
            'SKIN_ROOT': helpers.random_string(),
            'skin': helpers.random_string(),
            'Extras': {
                'chart_definitions': {
                    chart_name: {
                        'series': {
                            # observations are next
                            helpers.random_string('obs-1'): {}
                        },
                    },
                },
                'minmax': {
                    'observations': {
                        helpers.random_string('obs-2'): {}
                    }
                },
                'thisdate': {
                    'observations': {
                        helpers.random_string('obs-3'): {}
                    }
                },
                'pages': {
                    helpers.random_string('page-1'): {
                        # charts are next
                        chart_name: {},
                    },
                },
            },
        }
        skin_config = configobj.ConfigObj(skin_dict)
        mock_generator.skin_dict = skin_config

        config_dict = {
            'WEEWX_ROOT': helpers.random_string(),
        }
        config = configobj.ConfigObj(config_dict)
        mock_generator.config_dict = config

        with mock.patch('user.jas.time') as mock_time:
            with mock.patch('user.jas.weecfg.get_languages') as mock_get_languages:
                mock_time.time.return_value = now
                mock_get_languages.return_value = None

                user.jas.JAS(mock_generator)

        print("end")

    def test2(self):
        print("start")
        now = int(time.time())

        mock_generator = mock.Mock()

        skin_dict = {
            'lang': helpers.random_string(),
            'data_binding': helpers.random_string(),
            'SKIN_ROOT': helpers.random_string(),
            'skin': helpers.random_string(),
            'Extras': {},
        }
        skin_config = configobj.ConfigObj(skin_dict)
        mock_generator.skin_dict = skin_config

        config_dict = {
            'WEEWX_ROOT': helpers.random_string(),
        }
        config = configobj.ConfigObj(config_dict)
        mock_generator.config_dict = config

        with mock.patch('user.jas.time') as mock_time:
            with mock.patch('user.jas.weecfg.get_languages') as mock_get_languages:
                mock_time.time.return_value = now
                mock_get_languages.return_value = None

                user.jas.JAS(mock_generator)

        print("end")

if __name__ == '__main__':
    helpers.run_tests()
