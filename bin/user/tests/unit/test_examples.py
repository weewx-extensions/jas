#    Copyright (c) 2026 Rich Bell <bellrichm@gmail.com>
#
#    See the file LICENSE.txt for your full rights.
#

# pylint: disable=wrong-import-order
# pylint: disable=missing-module-docstring, missing-class-docstring, missing-function-docstring
# pylint: disable=invalid-name

import unittest
import mock

import configobj
import time

from user.tests import helpers

import user.jas

class TestTemplate(unittest.TestCase):
    def test_template(self):
        pass

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

    def testX(self):
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

from Cheetah.Template import Template

class TestCheetahTemplate(unittest.TestCase):
    def test_hello_world(self):
        # 1. Define the template
        template_def = """
<html>
<head><title>$title</title></head>
<body>
$contents
</body>
</html>
        """

        # 2. Define the data (namespace)
        data = {
            'title': 'Hello World Example',
            'contents': 'Hello World!'
        }

        # 3. Instantiate the template and render
        # Passing data via searchList
        t = Template(template_def, searchList=[data])
        actual_output = str(t).strip() # Convert to string and strip whitespace for clean comparison

        # 4. Define the expected output
        expected_output = """
<html>
<head><title>Hello World Example</title></head>
<body>
Hello World!
</body>
</html>
        """.strip()

        # 5. Assert the actual output matches the expected output
        self.assertEqual(actual_output, expected_output, "Template output did not match expected output")

    def test_dynamic_data(self):
        # Test with different data to ensure flexibility
        template_def = "User: $name, ID: $id"
        data = {'name': 'Jane Doe', 'id': 123}
        t = Template(template_def, searchList=[data])
        actual_output = str(t).strip()
        expected_output = "User: Jane Doe, ID: 123"

        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    helpers.run_tests()
