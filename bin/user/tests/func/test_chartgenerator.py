#    Copyright (c) 2026 Rich Bell <bellrichm@gmail.com>
#
#    See the file LICENSE.txt for your full rights.
#

# pylint: disable=wrong-import-order
# pylint: disable=missing-module-docstring, missing-class-docstring, missing-function-docstring
# pylint: disable=invalid-name

import unittest

from user.tests import helpers

import configobj

import weewx.manager

import user.jas

config = configobj.ConfigObj('bin/user/tests/func/data/weewx.test.conf', file_error=True)

binding = 'wx_binding'

@unittest.skip("Not ready to  run. Need to figure out how to deal with test data.")
class TestDataGenerator(unittest.TestCase):
    def test_gen_it(self):

        with weewx.manager.DBBinder(config) as db_binder:
            db_manager = db_binder.get_manager(binding)
            ts = db_manager.lastGoodStamp()
            record = db_manager.getRecord(ts)

        generator = user.jas.ChartGenerator(config, config['StdReport']['jas'], ts, True, None, record)

        generator._gen_charts('foo', 'day', 'day', 'day')

        print("done 1")

if __name__ == '__main__':
    helpers.run_tests()
