"""
This module is the test suite of the new CLI option for bowl.

Created on 27 July 2014
@author: Charlie Lewis
"""

from bowl.cli_opts import new

class Object(object):
    pass

class TestClass:
    """
    This class is responsible for all tests in the new CLI option.
    """
    def test_cli_opts_new_build_options(self):
        args = Object()
        args.metadata_path = "new_test"
        a = new.new()
        menu_dict = a.build_options(self, args)
        assert isinstance(menu_dict, dict)
