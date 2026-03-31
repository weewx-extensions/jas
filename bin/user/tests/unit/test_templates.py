#    Copyright (c) 2026 Rich Bell <bellrichm@gmail.com>
#
#    See the file LICENSE.txt for your full rights.
#

# pylint: disable=wrong-import-order
# pylint: disable=missing-module-docstring, missing-class-docstring, missing-function-docstring
# pylint: disable=invalid-name

import unittest

import Cheetah.Template
import copy
import os
import types

from user.tests import helpers

from user.tests.unit.data.template_results.body_inc import result_page_has_no_sections, result_page_has_zoom_control, result_page_has_section_debug,\
      result_page_has_file_alert_modal_inc, result_page_layout_is_not_grid, result_page_current_has_modal, result_page_display_aeris_alerts

from user.tests.unit.data.template_results.data_gen import result_data_minimal_configuration, result_display_aeris_observation,\
    result_display_aeris_alert, result_data_thisdate_no_aggregate, result_data_thisdate_has_aggregate, result_data_minmax, result_current_conditions,\
    result_mqtt_configuration, result_data_windrose_configuration

from user.tests.unit.data.template_results.pages_gen import result_pages_minimal_configuration, result_pages_zoom_control_configuration,\
    result_pages_comparison_series, result_pages_multiple_series, result_pages_debug_page

from user.tests.unit.data.template_results.javascript import results_javascript_min_configuration, results_javascript_archive_pages_configuration,\
results_javascript_archive_pages_month_disabled_configuration, results_javascript_landing_page_configuration, results_javascript_mqtt_configuration

from user.tests.unit.data.template_results.data import result_index_year_month_data, result_internationalization

from user.tests.unit.data.template_results.skin import result_index_min_configuration, result_index_build_navigation

def stub_logdbg(_arg1):
    pass

def stub_get_range(_arg1, _arg2, _arg3):
    return (9, 10)

def stub_get_observation_labels(_arg1):
    return {}

def stub_get_text_labels(_arg1):
    return {
        'Language': {}
    }

def stub_get_datetime_formats(_arg1):
    return {
        'forecast_date_format': 'foo01',
        'current_date_time': 'foo02',
        'datepicker_date_format': 'foo03',
        'year_to_year_xaxis_label': 'MM/DD',
        'aggregate_interval_mqtt': {
            'tooltip_x': 'foo05',
            'xaxis_label': 'foo06',
            'label': 'foo07'
        },
        'aggregate_interval_multiyear': {
            'tooltip_x': 'foo08',
            'xaxis_label': 'foo09',
            'label': 'foo10'
        },
        'aggregate_interval_none': {
            'tooltip_x': 'foo11',
            'xaxis_label': 'foo12',
            'label': 'foo013'
        },
        'aggregate_interval_hour': {
            'tooltip_x': 'foo14',
            'xaxis_label': 'foo15',
            'label': 'foo016'
        },
        'aggregate_interval_day': {
            'tooltip_x': 'foo17',
            'xaxis_label': 'foo18',
            'label': 'foo019'
        },
    }

class TestBodyInc(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        skin_dir = os.path.dirname(__file__) + '/../../../../skins/jas/'
        os.chdir(skin_dir)

    def test_page_has_no_sections(self):
        self.maxDiff = None

        page_name = 'foo1'
        section_data = 'foo2'
        extras = types.SimpleNamespace(
            pages = {
                page_name: {
                    'section': section_data
                }
            },
            chart_definitions = 'bar1',
            current = {
                'observations': {
                    'obs1': {
                        'display': False
                    }
                }
            },
        )

        data = {
            'page': page_name,
            'Extras': extras,
            'page_name_global': 'bar2',
        }

        filename = 'generators/body.inc'

        template_class = Cheetah.Template.Template.compile(file=filename)
        # print(f"----\n{Cheetah.Template.Template.generatedModuleCode(template_class)}\n----")
        template_instance = template_class(searchList=[data])
        result = template_instance.respond()
        self.assertEqual(result, result_page_has_no_sections)

    def test_page_has_zoom_control(self):
        self.maxDiff = None

        page_name = 'foo1'
        section_name = 'foo2'
        extras = types.SimpleNamespace(
            pages = {
                page_name: {
                    'section': section_name,
                    'zoomControl': True
                }
            },
            chart_definitions = 'bar1',
            current = {
                'observations': {
                    'obs1': {
                        'display': False
                    }
                }
            },
        )

        data = {
            'page': page_name,
            'Extras': extras,
            'page_name_global': 'bar2',
        }

        filename = 'generators/body.inc'

        template_class = Cheetah.Template.Template.compile(file=filename)
        # print(f"----\n{Cheetah.Template.Template.generatedModuleCode(template_class)}\n----")
        template_instance = template_class(searchList=[data])
        result = template_instance.respond()
        self.assertEqual(result, result_page_has_zoom_control)

    def test_page_has_section_debug(self):
        self.maxDiff = None

        page_name = 'foo1'
        section_name = 'debug'
        extras = types.SimpleNamespace(
            pages = {
                page_name: {
                    section_name: {}
                }
            },
            chart_definitions = 'bar1',
            current = {
                'observations': {
                    'obs1': {
                        'display': False
                    }
                }
            },
        )

        data = {
            'page': page_name,
            'Extras': extras,
            'page_name_global': 'bar2',
        }

        filename = 'generators/body.inc'

        template_class = Cheetah.Template.Template.compile(file=filename)
        # print(f"----\n{Cheetah.Template.Template.generatedModuleCode(template_class)}\n----")
        template_instance = template_class(searchList=[data])
        result = template_instance.respond()
        self.assertEqual(result, result_page_has_section_debug)


    def test_page_has_file_alert_model_inc(self):
        self.maxDiff = None

        page_name = 'foo1'
        section_name = 'debug'
        extras = types.SimpleNamespace(
            pages = {
                page_name: {
                    section_name: {
                        'filename': 'sections/alert_modal.inc'
                    }
                }
            },
            chart_definitions = 'bar1',
            current = {
                'observations': {
                    'obs1': {
                        'display': False
                    }
                }
            },
        )

        data = {
            'page': page_name,
            'Extras': extras,
            'page_name_global': 'bar2',
        }

        filename = 'generators/body.inc'

        template_class = Cheetah.Template.Template.compile(file=filename)
        # print(f"----\n{Cheetah.Template.Template.generatedModuleCode(template_class)}\n----")
        template_instance = template_class(searchList=[data])
        result = template_instance.respond()
        self.assertEqual(result, result_page_has_file_alert_modal_inc)

    def test_page_layout_is_not_grid(self):
        self.maxDiff = None

        page_name = 'foo1'
        extras = types.SimpleNamespace(
            pages = {
                page_name: {
                    'debug': {
                        'layout': 'not grid'
                    }
                }
            },
            chart_definitions = 'bar1',
            current = {
                'observations': {
                    'obs1': {
                        'display': False
                    }
                }
            },
        )

        data = {
            'page': page_name,
            'Extras': extras,
            'page_name_global': 'bar2',
        }

        filename = 'generators/body.inc'

        template_class = Cheetah.Template.Template.compile(file=filename)
        # print(f"----\n{Cheetah.Template.Template.generatedModuleCode(template_class)}\n----")
        template_instance = template_class(searchList=[data])
        result = template_instance.respond()

        self.assertEqual(result, result_page_layout_is_not_grid)

    def test_page_has_current_modal(self):
        self.maxDiff = None

        page_name = 'foo1'
        section_data = 'foo2'
        extras = types.SimpleNamespace(
            pages = {
                page_name: {
                    'section': section_data
                }
            },
            chart_definitions = 'bar1',
            current = {
                'observations': {
                    'obs1': {
                        'display': 'modal'
                    }
                }
            },
        )

        data = {
            'page': page_name,
            'Extras': extras,
            'page_name_global': 'bar2',
        }

        filename = 'generators/body.inc'

        template_class = Cheetah.Template.Template.compile(file=filename)
        # print(f"----\n{Cheetah.Template.Template.generatedModuleCode(template_class)}\n----")
        template_instance = template_class(searchList=[data])
        result = template_instance.respond()

        self.assertEqual(result, result_page_current_has_modal)

    def test_page_display_aeris_alerts(self):
        self.maxDiff = None

        page_name = 'foo1'
        section_data = 'foo2'
        extras = types.SimpleNamespace(
            display_aeris_alert = True,
            pages = {
                page_name: {
                    'section': section_data
                }
            },
            chart_definitions = 'bar1',
            current = {
                'observations': {
                    'obs1': {
                        'display': 'modal'
                    }
                }
            },
        )

        data = {
            'page': page_name,
            'Extras': extras,
            'page_name_global': 'bar2',
        }

        filename = 'generators/body.inc'

        template_class = Cheetah.Template.Template.compile(file=filename)
        # print(f"----\n{Cheetah.Template.Template.generatedModuleCode(template_class)}\n----")
        template_instance = template_class(searchList=[data])
        result = template_instance.respond()

        self.assertEqual(result, result_page_display_aeris_alerts)

class TestDataGen(unittest.TestCase):
    page = 'foo8'
    page_definition_name_global = page
    observation = 'obs1'
    extras = types.SimpleNamespace(
        page_definition = {
            page: {
                'aggregate_interval': ['bar1']
            }
        },
        pages = {
            page: {}
        },
        chart_definitions = {
            'windRose': {
                'series': {
                    'series-1': {},
                    'series-2': {},
                }
            }
        },
        current = {
            'observations': {}
        },
        thisdate = {
            'observations': {
                observation: {
                    'unit': 'default'
                }
            }
        },
        minmax = {
            'observations': {
                observation: {}
            }
        },
    )

    label = types.SimpleNamespace()
    setattr(label, observation, 'obs-label')

    data = {
        'data_binding': 'foo1',
        'page_definition_name_global': page_definition_name_global,
        'version': 'foo3',
        'genTime': 'foo4',
        'aggregate_types': ['foo5'],
        'interval_long_name_global': 'foo6',
        'observations': {
            observation: {
                'aggregate_types': {
                    'data_binding': {
                        'unit_name': ['foo7']
                    }
                },
            }
        },
        'unit': {
            'label': label
        },
        'page': page,
        'HTML_ROOT': 'foo8',
        'filename': 'foo9',
        'logdbg': stub_logdbg,
    }


    @classmethod
    def setUpClass(cls):
        skin_dir = os.path.dirname(__file__) + '/../../../../skins/jas/'
        os.chdir(skin_dir)

    def test_miminal_configuration(self):
        self.maxDiff = None

        extras = copy.deepcopy(TestDataGen.extras)

        data = copy.deepcopy(TestDataGen.data)

        data['Extras'] = extras

        filename = 'generators/data.gen'

        template_class = Cheetah.Template.Template.compile(file=filename)
        # print(f"----\n{Cheetah.Template.Template.generatedModuleCode(template_class)}\n----")
        template_instance = template_class(searchList=[data])
        result = template_instance.respond()
        # print(f"----\n{result}\n----")
        self.assertEqual(result, result_data_minimal_configuration)

    def test_display_aeris_alerts(self):
        self.maxDiff = None

        extras = copy.deepcopy(TestDataGen.extras)
        extras.display_aeris_alert = True
        extras.pages[TestDataGen.page]['current'] = {}

        data = copy.deepcopy(TestDataGen.data)

        data['Extras'] = extras

        filename = 'generators/data.gen'

        template_class = Cheetah.Template.Template.compile(file=filename)
        # print(f"----\n{Cheetah.Template.Template.generatedModuleCode(template_class)}\n----")
        template_instance = template_class(searchList=[data])
        result = template_instance.respond()
        #print(f"----\n{result}\n----")
        self.assertEqual(result, result_display_aeris_observation)

    def test_display_aeries_alert(self):
        self.maxDiff = None

        extras = copy.deepcopy(TestDataGen.extras)
        extras.display_aeris_alert = True
        extras.pages[TestDataGen.page]['current'] = {}

        data = copy.deepcopy(TestDataGen.data)

        data['Extras'] = extras

        filename = 'generators/data.gen'

        template_class = Cheetah.Template.Template.compile(file=filename)
        # print(f"----\n{Cheetah.Template.Template.generatedModuleCode(template_class)}\n----")
        template_instance = template_class(searchList=[data])
        result = template_instance.respond()
        #print(f"----\n{result}\n----")
        self.assertEqual(result, result_display_aeris_alert)

    def test_thisdate_no_aggregate(self):
        self.maxDiff = None

        extras = copy.deepcopy(TestDataGen.extras)
        extras.pages[TestDataGen.page]['thisdate'] = {}

        data = copy.deepcopy(TestDataGen.data)

        data['Extras'] = extras

        filename = 'generators/data.gen'

        template_class = Cheetah.Template.Template.compile(file=filename)
        # print(f"----\n{Cheetah.Template.Template.generatedModuleCode(template_class)}\n----")
        template_instance = template_class(searchList=[data])
        result = template_instance.respond()
        # print(f"----\n{result}\n----")
        self.assertEqual(result, result_data_thisdate_no_aggregate)

    def test_thisdate_has_aggregate(self):
        self.maxDiff = None

        extras = copy.deepcopy(TestDataGen.extras)
        extras.pages[TestDataGen.page]['thisdate'] = {}
        extras.thisdate['observations'][TestDataGen.observation]['type'] = 'type-1'

        data = copy.deepcopy(TestDataGen.data)

        data['Extras'] = extras

        filename = 'generators/data.gen'

        template_class = Cheetah.Template.Template.compile(file=filename)
        # print(f"----\n{Cheetah.Template.Template.generatedModuleCode(template_class)}\n----")
        template_instance = template_class(searchList=[data])
        result = template_instance.respond()
        # print(f"----\n{result}\n----")
        self.assertEqual(result, result_data_thisdate_has_aggregate)

    def test_minmax(self):
        self.maxDiff = None

        extras = copy.deepcopy(TestDataGen.extras)
        extras.pages[TestDataGen.page]['minmax'] = {}

        data = copy.deepcopy(TestDataGen.data)

        data['Extras'] = extras

        filename = 'generators/data.gen'

        template_class = Cheetah.Template.Template.compile(file=filename)
        # print(f"----\n{Cheetah.Template.Template.generatedModuleCode(template_class)}\n----")
        template_instance = template_class(searchList=[data])
        result = template_instance.respond()
        # print(f"----\n{result}\n----")
        self.assertEqual(result, result_data_minmax)

    def test_current_conditions(self):
        self.maxDiff = None

        extras = copy.deepcopy(TestDataGen.extras)
        extras.pages[TestDataGen.page]['current'] = {}
        extras.current['observation'] = TestDataGen.observation
        extras.current['observations'] = {
            TestDataGen.observation: {}
        }

        data = copy.deepcopy(TestDataGen.data)

        data['Extras'] = extras

        filename = 'generators/data.gen'

        template_class = Cheetah.Template.Template.compile(file=filename)
        # print(f"----\n{Cheetah.Template.Template.generatedModuleCode(template_class)}\n----")
        template_instance = template_class(searchList=[data])
        result = template_instance.respond()
        # print(f"----\n{result}\n----")
        self.assertEqual(result, result_current_conditions)

    def test_mqtt_configuration(self):
        self.maxDiff = None

        extras = copy.deepcopy(TestDataGen.extras)
        extras.mqtt = {
            'topics': {
                'topic-1': {
                    'fields': {
                        'field-1': {
                            'name': 'name-1'
                        }
                    }
                }
            }
        }

        data = copy.deepcopy(TestDataGen.data)

        data['Extras'] = extras

        filename = 'generators/data.gen'

        template_class = Cheetah.Template.Template.compile(file=filename)
        # print(f"----\n{Cheetah.Template.Template.generatedModuleCode(template_class)}\n----")
        template_instance = template_class(searchList=[data])
        result = template_instance.respond()
        # print(f"----\n{result}\n----")
        self.assertEqual(result, result_mqtt_configuration)

    def test_windrose_configuration(self):
        self.maxDiff = None

        extras = copy.deepcopy(TestDataGen.extras)
        extras.pages[TestDataGen.page]['windRose'] = {
            'series': {
                'series-1': {},
                'series-2': {},
            },
        }

        data = copy.deepcopy(TestDataGen.data)

        data['Extras'] = extras

        filename = 'generators/data.gen'

        template_class = Cheetah.Template.Template.compile(file=filename)
        # print(f"----\n{Cheetah.Template.Template.generatedModuleCode(template_class)}\n----")
        template_instance = template_class(searchList=[data])
        result = template_instance.respond()
        # print(f"----\n{result}\n----")
        self.assertEqual(result, result_data_windrose_configuration)

class TestPageGen(unittest.TestCase):
    page = 'page-1'

    extras = {
        'pages': {
            page: {}
        },
        'chart_definitions': {},
        'page_definition': {
            page: {}
        }
    }

    data = {
        'lang': 'foo1',
        'version': 'foo2',
        'genTime': 'foo3',
        'page': page,
        'interval_name_global': 'foo4',
        'page_name_global': 'foo5',
        'HTML_ROOT': 'foo6',
        'filename': 'foo7',
        'Extras': extras,
        'logdbg': stub_logdbg,
        'data_binding': 'foo8',
        'getRange': stub_get_range,
    }

    @classmethod
    def setUpClass(cls):
        skin_dir = os.path.dirname(__file__) + '/../../../../skins/jas/'
        os.chdir(skin_dir)

    def test_miminal_configuration(self):
        self.maxDiff = None

        data = copy.deepcopy(TestPageGen.data)

        filename = 'generators/pages.gen'

        template_class = Cheetah.Template.Template.compile(file=filename)
        # print(f"----\n{Cheetah.Template.Template.generatedModuleCode(template_class)}\n----")
        template_instance = template_class(searchList=[data])
        result = template_instance.respond()
        # print(f"----\n{result}\n----")
        self.assertEqual(result, result_pages_minimal_configuration)

    def test_zoom_control_configuration(self):
        self.maxDiff = None

        extras = copy.deepcopy(TestPageGen.extras)
        extras['pages'][TestPageGen.page] = {
            'zoomControl': 'bar1'
        }

        data = copy.deepcopy(TestPageGen.data)
        data['Extras'] = extras

        filename = 'generators/pages.gen'

        template_class = Cheetah.Template.Template.compile(file=filename)
        # print(f"----\n{Cheetah.Template.Template.generatedModuleCode(template_class)}\n----")
        template_instance = template_class(searchList=[data])
        result = template_instance.respond()
        # print(f"----\n{result}\n----")
        self.assertEqual(result, result_pages_zoom_control_configuration)

    def test_comparison_series_configuration(self):
        self.maxDiff = None

        extras = copy.deepcopy(TestPageGen.extras)
        extras['page_definition'] = {
            TestPageGen.page: {
                'series_type': 'comparison'
            }
        }

        data = copy.deepcopy(TestPageGen.data)
        data['Extras'] = extras

        filename = 'generators/pages.gen'

        template_class = Cheetah.Template.Template.compile(file=filename)
        # print(f"----\n{Cheetah.Template.Template.generatedModuleCode(template_class)}\n----")
        template_instance = template_class(searchList=[data])
        result = template_instance.respond()
        # print(f"----\n{result}\n----")
        self.assertEqual(result, result_pages_comparison_series)

    def test_comparison_multiple_configuration(self):
        self.maxDiff = None

        extras = copy.deepcopy(TestPageGen.extras)
        extras['page_definition'] = {
            TestPageGen.page: {
                'series_type': 'multiple'
            }
        }

        data = copy.deepcopy(TestPageGen.data)
        data['Extras'] = extras

        filename = 'generators/pages.gen'

        template_class = Cheetah.Template.Template.compile(file=filename)
        # print(f"----\n{Cheetah.Template.Template.generatedModuleCode(template_class)}\n----")
        template_instance = template_class(searchList=[data])
        result = template_instance.respond()
        # print(f"----\n{result}\n----")
        self.assertEqual(result, result_pages_multiple_series)

    def test_debug_page(self):
        self.maxDiff = None

        data = copy.deepcopy(TestPageGen.data)
        data['page_name_global'] = 'debug'

        filename = 'generators/pages.gen'

        template_class = Cheetah.Template.Template.compile(file=filename)
        # print(f"----\n{Cheetah.Template.Template.generatedModuleCode(template_class)}\n----")
        template_instance = template_class(searchList=[data])
        result = template_instance.respond()
        # print(f"----\n{result}\n----")
        self.assertEqual(result, result_pages_debug_page)

class TestJavascript(unittest.TestCase):
    extras = {
        'mqtt': {
            'host': 'foo3',
            'port': 'foo4',
            'timeout': 'foo5',
            'keepAliveInterval': 'foo6',
            'cleanSession': 'foo7',
            'useSSL': 'foo8',
            'reconnect': 'foo9',
        },
        'pages': {},
    }

    data = {
        'weewx_version': 'foo10',
        'version': 'foo11',
        'HTML_ROOT': 'foo12',
        'filename': 'foo13',
        'logdbg': stub_logdbg
    }

    @classmethod
    def setUpClass(cls):
        skin_dir = os.path.dirname(__file__) + '/../../../../skins/jas/'
        os.chdir(skin_dir)

    def test_miminal_configuration(self):
        self.maxDiff = None

        extras = copy.deepcopy(TestJavascript.extras)

        data = copy.deepcopy(TestJavascript.data)
        data['Extras'] = extras

        filename = 'javascript/index.js.tmpl'

        template_class = Cheetah.Template.Template.compile(file=filename)
        # print(f"----\n{Cheetah.Template.Template.generatedModuleCode(template_class)}\n----")
        template_instance = template_class(searchList=[data])
        result = template_instance.respond()
        # print(f"----\n{result}\n----")
        self.assertEqual(result, results_javascript_min_configuration)

    def test_archive_pages_configuration(self):
        self.maxDiff = None

        extras = copy.deepcopy(TestJavascript.extras)
        extras['pages'] = {
            'archive-month': {
                'enable': True,
            },
            'archive-year': {
                'enable': True,
            },
        }

        data = copy.deepcopy(TestJavascript.data)
        data['Extras'] = extras

        filename = 'javascript/index.js.tmpl'

        template_class = Cheetah.Template.Template.compile(file=filename)
        # print(f"----\n{Cheetah.Template.Template.generatedModuleCode(template_class)}\n----")
        template_instance = template_class(searchList=[data])
        result = template_instance.respond()
        # print(f"----\n{result}\n----")
        self.assertEqual(result, results_javascript_archive_pages_configuration)

    def test_archive_pages_month_disabled_configuration(self):
        self.maxDiff = None

        extras = copy.deepcopy(TestJavascript.extras)
        extras['pages'] = {
            'archive-month': {
                'enable': False,
            },
            'archive-year': {
                'enable': True,
            },
        }

        data = copy.deepcopy(TestJavascript.data)
        data['Extras'] = extras

        filename = 'javascript/index.js.tmpl'

        template_class = Cheetah.Template.Template.compile(file=filename)
        # print(f"----\n{Cheetah.Template.Template.generatedModuleCode(template_class)}\n----")
        template_instance = template_class(searchList=[data])
        result = template_instance.respond()
        # print(f"----\n{result}\n----")
        self.assertEqual(result, results_javascript_archive_pages_month_disabled_configuration)

    def test_landing_page_configuration(self):
        self.maxDiff = None

        page = 'page-1'
        extras = copy.deepcopy(TestJavascript.extras)
        extras['pages'][page] = {
            'query_string_on': 'page'
        }
        extras['landing_page'] = 'page-1'

        data = copy.deepcopy(TestJavascript.data)
        data['Extras'] = extras

        filename = 'javascript/index.js.tmpl'

        template_class = Cheetah.Template.Template.compile(file=filename)
        # print(f"----\n{Cheetah.Template.Template.generatedModuleCode(template_class)}\n----")
        template_instance = template_class(searchList=[data])
        result = template_instance.respond()
        # print(f"----\n{result}\n----")
        self.assertEqual(result, results_javascript_landing_page_configuration)

    def test_mqtt_configuration(self):
        self.maxDiff = None

        extras = copy.deepcopy(TestJavascript.extras)
        extras['mqtt']['enable'] = True

        data = copy.deepcopy(TestJavascript.data)
        data['Extras'] = extras

        filename = 'javascript/index.js.tmpl'

        template_class = Cheetah.Template.Template.compile(file=filename)
        # print(f"----\n{Cheetah.Template.Template.generatedModuleCode(template_class)}\n----")
        template_instance = template_class(searchList=[data])
        result = template_instance.respond()
        # print(f"----\n{result}\n----")
        self.assertEqual(result, results_javascript_mqtt_configuration)

class TestData(unittest.TestCase):
    extras = {
    }

    data = {
    }

    @classmethod
    def setUpClass(cls):
        skin_dir = os.path.dirname(__file__) + '/../../../../skins/jas/'
        os.chdir(skin_dir)

    def test_index_year_month(self):
        self.maxDiff = None

        extras = copy.deepcopy(TestJavascript.extras)

        data = copy.deepcopy(TestJavascript.data)
        data['Extras'] = extras
        data['SummaryByYear'] = ['1999', '2000']
        data['SummaryByMonth'] = ['1999-06', '1999-07', '1999-11', '1999-12']

        filename = 'data/index.js.tmpl'

        template_class = Cheetah.Template.Template.compile(file=filename)
        # print(f"----\n{Cheetah.Template.Template.generatedModuleCode(template_class)}\n----")
        template_instance = template_class(searchList=[data])
        result = template_instance.respond()
        # print(f"----\n{result}\n----")
        self.assertEqual(result, result_index_year_month_data)

    def test_internationalization(self):
        self.maxDiff = None

        extras = copy.deepcopy(TestJavascript.extras)

        data = copy.deepcopy(TestJavascript.data)
        data['Extras'] = extras
        data['lang'] = 'lang-1'
        data['languages'] = {
            'lang-1': {},
            'lang-2': {},
        }
        data['observationLabels'] = stub_get_observation_labels
        data['textLabels'] = stub_get_text_labels
        data['dateTimeFormats'] = stub_get_datetime_formats

        filename = 'data/internationalization.js.tmpl'

        template_class = Cheetah.Template.Template.compile(file=filename)
        # print(f"----\n{Cheetah.Template.Template.generatedModuleCode(template_class)}\n----")
        template_instance = template_class(searchList=[data])
        result = template_instance.respond()
        # print(f"----\n{result}\n----")
        self.assertEqual(result, result_internationalization)

class TestSkin(unittest.TestCase):
    extras = {
        'pages': {}
    }

    data = {
        'lang': 'foo1',
        'version': 'foo2',
        'station': {
            'location': 'foo3'
        },
        'HTML_ROOT': 'foo4',
        'filename': 'foo5',
        'logdbg': stub_logdbg
    }

    @classmethod
    def setUpClass(cls):
        skin_dir = os.path.dirname(__file__) + '/../../../../skins/jas/'
        os.chdir(skin_dir)

    def test_index_min_configuration(self):
        self.maxDiff = None

        extras = copy.deepcopy(TestSkin.extras)

        data = copy.deepcopy(TestSkin.data)
        data['Extras'] = extras

        filename = 'index.html.tmpl'

        template_class = Cheetah.Template.Template.compile(file=filename)
        # print(f"----\n{Cheetah.Template.Template.generatedModuleCode(template_class)}\n----")
        template_instance = template_class(searchList=[data])
        result = template_instance.respond()
        # print(f"----\n{result}\n----")
        self.assertEqual(result, result_index_min_configuration)

    def test_index_build_navigation(self):
        self.maxDiff = None

        extras = copy.deepcopy(TestSkin.extras)
        extras['pages'] = {
            'page-01': {},
            'page-02': {
                'navbar': 'secondary',
            },
            'page-03': {
                'query_string_on': 'page'
            },
            # ToDo: Is switching between primary and secondary navbar location 'legal'?
            'page-04': {
                'navbar': 'secondary',
            },
            'page-05': {
                'enable': False,
            }
        }

        data = copy.deepcopy(TestSkin.data)
        data['Extras'] = extras

        filename = 'index.html.tmpl'

        template_class = Cheetah.Template.Template.compile(file=filename)
        # print(f"----\n{Cheetah.Template.Template.generatedModuleCode(template_class)}\n----")
        template_instance = template_class(searchList=[data])
        result = template_instance.respond()
        # print(f"----\n{result}\n----")
        self.assertEqual(result, result_index_build_navigation)

if __name__ == '__main__':
    helpers.run_tests()
