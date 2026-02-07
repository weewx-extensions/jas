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
import time

import weewx.manager
import weeutil.weeutil

import user.jas

from  user.tests.func.data.datagenerator_results import result1, result2

config = configobj.ConfigObj('bin/user/tests/func/data/weewx.test.conf', file_error=True)

binding = 'wx_binding'

@unittest.skip("Not ready to  run. Need to figure out how to deal with test data.")
class TestDataGenerator(unittest.TestCase):
    def test_gen_it(self):
        self.maxDiff = None
        now = int(time.time())

        with mock.patch('user.jas.time') as mock_time:
            mock_time.time.return_value = now

            with weewx.manager.DBBinder(config) as db_binder:
                db_manager = db_binder.get_manager(binding)
                ts = db_manager.lastGoodStamp()
                record = db_manager.getRecord(ts)

            generator = user.jas.DataGenerator(config, config['StdReport']['jas'], ts, True, None, record)

            time_span = weeutil.weeutil.TimeSpan(ts, record['dateTime'])

            result = generator._gen_it(time_span, 'foo', 'day', 'day', None)
            # print(result)
            self.assertEqual(result, result1.format(now=now))

            result = generator._gen_data_load(time_span, 'foo', 'day', 'active', 'day', 'day_')
           #  print(result)
            self.assertEqual(result, result2.format(now=now))

            print("done 1")

if __name__ == '__main__':
    helpers.run_tests()
