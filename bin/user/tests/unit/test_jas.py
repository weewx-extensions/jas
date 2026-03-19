#    Copyright (c) 2025-2026 Rich Bell <bellrichm@gmail.com>
#
#    See the file LICENSE.txt for your full rights.
#

# pylint: disable=wrong-import-order
# pylint: disable=missing-module-docstring, missing-class-docstring, missing-function-docstring
# pylint: disable=invalid-name

import configobj
import datetime
import os
import time

import unittest
import mock

from user.tests import helpers
import user.jas
from user.tests.unit.data.test_results import result1

from weewx import __version__ as weewx_version


class TestExtensions(unittest.TestCase):
    report_name = helpers.random_string()
    page_name = helpers.random_string()
    skin_dict = {
        'lang': helpers.random_string('lang-1'),
        'data_binding': helpers.random_string(),
        'SKIN_ROOT': helpers.random_string(),
        'REPORT_NAME': report_name,
        'skin': report_name,
        'Extras': {
            'page_definition': {},
            'pages': {
                page_name: {},
            },
        },
    }

    config_dict = {
        'WEEWX_ROOT': helpers.random_string(),
        'StdReport': {
            'Defaults': {},
            report_name: {},
        },
    }

    def merge_language(self, _language, _config_dict, _report_name, lang_dict):
        lang_data = {
            'Labels': {
                'Generic': {
                }
            },
            'Texts': {},
        }

        if self.expected_date_formats:
            lang_data['Texts'] = {
                'forecast_date_format': self.expected_date_formats['forecast_date_format'],
                'current_date_time': self.expected_date_formats['current_date_time'],
                'datepicker_date_format': self.expected_date_formats['datepicker_date_format'],
                'year_to_year_xaxis_label': self.expected_date_formats['year_to_year_xaxis_label'],
                'aggregate_interval_mqtt': {
                    'tooltip_x': self.expected_date_formats['aggregate_interval_mqtt']['tooltip_x'],
                    'xaxis_label': self.expected_date_formats['aggregate_interval_mqtt']['xaxis_label'],
                    'label': self.expected_date_formats['aggregate_interval_mqtt']['label'],
                },
                'aggregate_interval_multiyear': {
                    'tooltip_x': self.expected_date_formats['aggregate_interval_mqtt']['tooltip_x'],
                    'xaxis_label': self.expected_date_formats['aggregate_interval_mqtt']['xaxis_label'],
                    'label': self.expected_date_formats['aggregate_interval_mqtt']['label'],
                },
                'aggregate_interval_none': {
                    'tooltip_x': self.expected_date_formats['aggregate_interval_mqtt']['tooltip_x'],
                    'xaxis_label': self.expected_date_formats['aggregate_interval_mqtt']['xaxis_label'],
                    'label': self.expected_date_formats['aggregate_interval_mqtt']['label'],
                },
                'aggregate_interval_hour': {
                    'tooltip_x': self.expected_date_formats['aggregate_interval_mqtt']['tooltip_x'],
                    'xaxis_label': self.expected_date_formats['aggregate_interval_mqtt']['xaxis_label'],
                    'label': self.expected_date_formats['aggregate_interval_mqtt']['label'],
                },
                'aggregate_interval_day': {
                    'tooltip_x': self.expected_date_formats['aggregate_interval_mqtt']['tooltip_x'],
                    'xaxis_label': self.expected_date_formats['aggregate_interval_mqtt']['xaxis_label'],
                    'label': self.expected_date_formats['aggregate_interval_mqtt']['label'],
                },
            }

        lang_dict.merge(configobj.ConfigObj(lang_data))

    def test_get_extension_list(self):
        now = int(time.time())

        mock_generator = mock.Mock()
        mock_generator.skin_dict = configobj.ConfigObj(TestExtensions.skin_dict)
        mock_generator.config_dict = configobj.ConfigObj(TestExtensions.config_dict)

        with mock.patch('user.jas.time') as mock_time:
            with mock.patch('user.jas.weecfg.get_languages') as mock_get_languages:
                mock_time.time.return_value = now
                mock_get_languages.return_value = None

                SUT = user.jas.JAS(mock_generator)

                extension_list = SUT.get_extension_list(None, None)

                expected_extension_list = {
                    'aggregate_types': SUT.aggregate_types,
                    'dateTimeFormats': SUT.get_datetime_formats,
                    'data_binding': SUT.data_binding,
                    'genJs': SUT.gen_js,
                    'genJasOptions': SUT._gen_jas_options,
                    'genTime': SUT.gen_time,
                    'getRange': SUT._get_range,
                    'getUnitLabel': SUT._get_unit_label,
                    'languages': SUT.languages,
                    'logdbg': user.jas.logdbg,
                    'loginf': user.jas.loginf,
                    'logerr': user.jas.logerr,
                    'observations': SUT.observations,
                    'observationLabels': SUT._get_observation_labels,
                    'textLabels': SUT._get_text_labels,
                    'version': user.jas.VERSION,
                    'weewx_version': weewx_version,
                }

        self.assertEqual(extension_list[0], expected_extension_list)

    def test_extension_dateTimeFormats(self):
        now = int(time.time())

        language = TestExtensions.skin_dict['lang']

        mock_generator = mock.Mock()
        mock_generator.skin_dict = configobj.ConfigObj(TestExtensions.skin_dict)
        mock_generator.config_dict = configobj.ConfigObj(TestExtensions.config_dict)

        self.expected_date_formats = {
            'forecast_date_format': helpers.random_string('forecast_date_format'),
            'current_date_time': helpers.random_string('current_date_time'),
            'datepicker_date_format': helpers.random_string('datepicker_date_format'),
            'year_to_year_xaxis_label': helpers.random_string('year_to_year_xaxis_label'),
            'aggregate_interval_mqtt': {
                'tooltip_x': helpers.random_string('tooltip_x'),
                'xaxis_label': helpers.random_string('xaxis_label'),
                'label': helpers.random_string('label'),
            },
            'aggregate_interval_multiyear': {
                'tooltip_x': helpers.random_string('tooltip_x'),
                'xaxis_label': helpers.random_string('xaxis_label'),
                'label': helpers.random_string('label'),
            },
            'aggregate_interval_none': {
                'tooltip_x': helpers.random_string('tooltip_x'),
                'xaxis_label': helpers.random_string('xaxis_label'),
                'label': helpers.random_string('label'),
            },
            'aggregate_interval_hour': {
                'tooltip_x': helpers.random_string('tooltip_x'),
                'xaxis_label': helpers.random_string('xaxis_label'),
                'label': helpers.random_string('label'),
            },
            'aggregate_interval_day': {
                'tooltip_x': helpers.random_string('tooltip_x'),
                'xaxis_label': helpers.random_string('xaxis_label'),
                'label': helpers.random_string('label'),
            },
        }

        with mock.patch('user.jas.time') as mock_time:
            with mock.patch('user.jas.weecfg.get_languages') as mock_get_languages:
                with mock.patch('user.jas.merge_lang') as mock_merge_lang:
                    mock_time.time.return_value = now
                    mock_get_languages.return_value = [language]

                    mock_merge_lang.side_effect = self.merge_language

                    SUT = user.jas.JAS(mock_generator)
                    extension_list = SUT.get_extension_list(None, None)[0]

                    date_time_formats = extension_list['dateTimeFormats'](language)

                    self.assertEqual(date_time_formats, self.expected_date_formats)

    def test_extension_genJs(self):
        self.maxDiff = None

        now = int(time.time())

        mock_generator = mock.Mock()
        mock_generator.skin_dict = configobj.ConfigObj(TestExtensions.skin_dict)
        mock_generator.config_dict = configobj.ConfigObj(TestExtensions.config_dict)

        with mock.patch('user.jas.time') as mock_time:
            with mock.patch('user.jas.weecfg.get_languages') as mock_get_languages:
                os.environ['TZ'] = 'America/New_York'
                time.tzset()

                now = int(time.time())
                utc_offset = (datetime.datetime.fromtimestamp(now) -
                            datetime.datetime.utcfromtimestamp(now)).total_seconds()/60

                mock_time.time.return_value = now
                mock_get_languages.return_value = None

                SUT = user.jas.JAS(mock_generator)
                extension_list = SUT.get_extension_list(None, None)[0]

                js = extension_list['genJs'](helpers.random_string(), TestExtensions.page_name, None, None, None, None)
                self.assertEqual(js, result1.format(utc_offset=utc_offset, page_name=TestExtensions.page_name))

    def testX(self):
        print("start")
        self.maxDiff = None

        now = int(time.time())

        mock_generator = mock.Mock()
        mock_generator.skin_dict = configobj.ConfigObj(TestExtensions.skin_dict)
        mock_generator.config_dict = configobj.ConfigObj(TestExtensions.config_dict)

        with mock.patch('user.jas.time') as mock_time:
            with mock.patch('user.jas.weecfg.get_languages') as mock_get_languages:
                os.environ['TZ'] = 'America/New_York'
                time.tzset()

                now = int(time.time())
                utc_offset = (datetime.datetime.fromtimestamp(now) -
                            datetime.datetime.utcfromtimestamp(now)).total_seconds()/60

                mock_time.time.return_value = now
                mock_get_languages.return_value = None

                SUT = user.jas.JAS(mock_generator)
                extension_list = SUT.get_extension_list(None, None)[0]


        print("end")

if __name__ == '__main__':
    helpers.run_tests()
