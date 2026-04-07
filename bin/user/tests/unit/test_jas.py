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
import random
import time

import unittest
import mock

from user.tests import helpers
import user.jas
from user.tests.unit.data.test_results import result1, result2

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.expected_date_formats = None
        self.expected_observation_labels = None
        self.expected_text_labels = None

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

        if self.expected_observation_labels:
            lang_data['Labels'] = {
                'Generic': self.expected_observation_labels
            }

        if self.expected_text_labels:
            lang_data['Texts'] = self.expected_text_labels

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
                    'genJasOptions': SUT.gen_jas_options,
                    'genTime': SUT.gen_time,
                    'getRange': SUT.get_range,
                    'getUnitLabel': SUT._get_unit_label,
                    'languages': SUT.languages,
                    'logdbg': user.jas.logdbg,
                    'loginf': user.jas.loginf,
                    'logerr': user.jas.logerr,
                    'observations': SUT.observations,
                    'observationLabels': SUT.get_observation_labels,
                    'textLabels': SUT.get_text_labels,
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
        today = datetime.datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
        year = str(today.year)
        month = str(today.month)

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
                self.assertEqual(js, result1.format(utc_offset=utc_offset, page_name=TestExtensions.page_name, year=year, month=month))

    def test_extension_genJasOptions(self):
        self.maxDiff = None

        now = int(time.time())

        mock_generator = mock.Mock()
        mock_generator.skin_dict = configobj.ConfigObj(TestExtensions.skin_dict)
        mock_generator.config_dict = configobj.ConfigObj(TestExtensions.config_dict)

        with mock.patch('user.jas.time') as mock_time:
            with mock.patch('user.jas.weecfg.get_languages') as mock_get_languages:

                mock_time.time.return_value = now
                mock_get_languages.return_value = None

                SUT = user.jas.JAS(mock_generator)
                extension_list = SUT.get_extension_list(None, None)[0]

                jas_options = extension_list['genJasOptions'](helpers.random_string(), TestExtensions.page_name)
                self.assertEqual(jas_options, result2.format(now=now))

    def test_extension_getRange(self):
        self.maxDiff = None

        now = int(time.time())
        first_timestamp = random.randint(0,0)
        last_timestamp = now
        first_year = int(datetime.datetime.fromtimestamp(first_timestamp).strftime('%Y'))
        last_year = int(datetime.datetime.fromtimestamp(last_timestamp).strftime('%Y')) + 1

        mock_generator = mock.Mock()
        mock_generator.skin_dict = configobj.ConfigObj(TestExtensions.skin_dict)
        mock_generator.config_dict = configobj.ConfigObj(TestExtensions.config_dict)

        mock_dbm = mock.Mock()
        mock_dbm.firstGoodStamp.return_value = first_timestamp
        mock_dbm.lastGoodStamp.return_value = last_timestamp
        mock_generator.db_binder.get_manager.return_value = mock_dbm

        with mock.patch('user.jas.time') as mock_time:
            with mock.patch('user.jas.weecfg.get_languages') as mock_get_languages:

                mock_time.time.return_value = now
                mock_get_languages.return_value = None

                SUT = user.jas.JAS(mock_generator)
                extension_list = SUT.get_extension_list(None, None)[0]

                result = extension_list['getRange'] = SUT.get_range(None, None, None)
                self.assertEqual(result, (first_year, last_year))

    def test_extension_observationLabels(self):
        self.maxDiff = None

        now = int(time.time())

        language = TestExtensions.skin_dict['lang']

        mock_generator = mock.Mock()
        mock_generator.skin_dict = configobj.ConfigObj(TestExtensions.skin_dict)
        mock_generator.config_dict = configobj.ConfigObj(TestExtensions.config_dict)

        self.expected_observation_labels = {}
        for _ in range(1, random.randint(1, 10)):
            self.expected_observation_labels[helpers.random_string()] = helpers.random_string()

        with mock.patch('user.jas.time') as mock_time:
            with mock.patch('user.jas.weecfg.get_languages') as mock_get_languages:
                with mock.patch('user.jas.merge_lang') as mock_merge_lang:

                    mock_time.time.return_value = now
                    mock_get_languages.return_value = [language]

                    mock_merge_lang.side_effect = self.merge_language

                    SUT = user.jas.JAS(mock_generator)
                    extension_list = SUT.get_extension_list(None, None)[0]

                    observation_labels = extension_list['observationLabels'](language)

                    self.assertEqual(observation_labels, self.expected_observation_labels)

    def test_extension_textLabels(self):
        self.maxDiff = None

        now = int(time.time())

        language = TestExtensions.skin_dict['lang']

        mock_generator = mock.Mock()
        mock_generator.skin_dict = configobj.ConfigObj(TestExtensions.skin_dict)
        mock_generator.config_dict = configobj.ConfigObj(TestExtensions.config_dict)

        self.expected_text_labels = {}
        for _ in range(1, random.randint(1, 10)):
            self.expected_text_labels[helpers.random_string()] = helpers.random_string()

        with mock.patch('user.jas.time') as mock_time:
            with mock.patch('user.jas.weecfg.get_languages') as mock_get_languages:
                with mock.patch('user.jas.merge_lang') as mock_merge_lang:

                    mock_time.time.return_value = now
                    mock_get_languages.return_value = [language]

                    mock_merge_lang.side_effect = self.merge_language

                    SUT = user.jas.JAS(mock_generator)
                    extension_list = SUT.get_extension_list(None, None)[0]

                    text_labels = extension_list['textLabels'](language)

                    self.assertEqual(text_labels, self.expected_text_labels)

if __name__ == '__main__':
    helpers.run_tests()
