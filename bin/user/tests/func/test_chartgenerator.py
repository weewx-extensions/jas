#    Copyright (c) 2026 Rich Bell <bellrichm@gmail.com>
#
#    See the file LICENSE.txt for your full rights.
#

# pylint: disable=wrong-import-order
# pylint: disable=missing-module-docstring, missing-class-docstring, missing-function-docstring
# pylint: disable=invalid-name

import unittest
import mock

from user.tests import helpers

import configobj
import os
import time

import weewx.manager

import user.jas

from  user.tests.func.data.chartgenerator_results import result1, result2, result3, result4

config = configobj.ConfigObj('bin/user/tests/func/data/weewx.test.conf', file_error=True)

# WeeWX moved the location of schemas in 5.2
try:
    import weewx.schemas.wview_extended
except ModuleNotFoundError:
    for _, data_binding in config['DataBindings'].items():
        data_binding['schema'] = 'schemas.wview_extended.schema'

binding = 'wx_binding'

#@unittest.skip("Not ready to  run. Need to figure out how to deal with test data.")
class TestChartGenerator(unittest.TestCase):
    def test_gen_it(self):
        self.maxDiff = None
        now = int(time.time())

        with weewx.manager.DBBinder(config) as db_binder:
            db_manager = db_binder.get_manager(binding)
            ts = db_manager.lastGoodStamp()
            record = db_manager.getRecord(ts)

        with mock.patch('user.jas.time') as mock_time:
            #with mock.patch('user.jas.datetime') as mock_datetime:
            mock_time.time.return_value = now
            # ToDo: This will probably break when on day light savings time....
            os.environ['TZ'] = 'America/New_York'
            time.tzset()

            generator = user.jas.ChartGenerator(config, config['StdReport']['jas'], ts, True, None, record)

            result = generator._gen_charts(helpers.random_string(), 'day', 'day', 'day')
            # print(result)
            self.assertEqual(result, result1.format(now=now))

            print("done 1")

    def test_gen_it2(self):
        self.maxDiff = None
        now = int(time.time())

        with weewx.manager.DBBinder(config) as db_binder:
            db_manager = db_binder.get_manager(binding)
            ts = db_manager.lastGoodStamp()
            record = db_manager.getRecord(ts)

        with mock.patch('user.jas.time') as mock_time:
            #with mock.patch('user.jas.datetime') as mock_datetime:
            mock_time.time.return_value = now
            # ToDo: This will probably break when on day light savings time....
            os.environ['TZ'] = 'America/New_York'
            time.tzset()

            generator = user.jas.ChartGenerator(config, config['StdReport']['jas'], ts, True, None, record)

            result = generator._gen_charts(helpers.random_string(), 'yeartoyear', 'yeartoyear', 'yeartoyear')
            #print(result)
            self.assertEqual(result, result2.format(now=now))

            print("done 1")

    def test_gen_it3(self):
        self.maxDiff = None
        now = int(time.time())

        with weewx.manager.DBBinder(config) as db_binder:
            db_manager = db_binder.get_manager(binding)
            ts = db_manager.lastGoodStamp()
            record = db_manager.getRecord(ts)

        with mock.patch('user.jas.time') as mock_time:
            #with mock.patch('user.jas.datetime') as mock_datetime:
            mock_time.time.return_value = now
            # ToDo: This will probably break when on day light savings time....
            os.environ['TZ'] = 'America/New_York'
            time.tzset()

            generator = user.jas.ChartGenerator(config, config['StdReport']['jas'], ts, True, None, record)

            result = generator._gen_charts(helpers.random_string(), 'multiyear', 'year', 'multiyear')
            # print(result)
            self.assertEqual(result, result3.format(now=now))

            print("done 1")

    def test_gen_it4(self):
        self.maxDiff = None
        now = int(time.time())

        with weewx.manager.DBBinder(config) as db_binder:
            db_manager = db_binder.get_manager(binding)
            ts = db_manager.lastGoodStamp()
            record = db_manager.getRecord(ts)

        with mock.patch('user.jas.time') as mock_time:
            #with mock.patch('user.jas.datetime') as mock_datetime:
            mock_time.time.return_value = now
            # ToDo: This will probably break when on day light savings time....
            os.environ['TZ'] = 'America/New_York'
            time.tzset()

            generator = user.jas.ChartGenerator(config, config['StdReport']['jas'], ts, True, None, record)

            result = generator._gen_charts(helpers.random_string(), 'debug', 'last24hours', 'debug')
            # rint(result)
            self.assertEqual(result, result4.format(now=now))

            print("done 1")

if __name__ == '__main__':
    helpers.run_tests()
