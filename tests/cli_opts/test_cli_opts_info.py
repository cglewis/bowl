"""
This module is the test suite of the info CLI option for bowl.

Created on 27 July 2014
@author: Charlie Lewis
"""

from bowl.cli_opts import info

class Object(object):
    pass

class TestClass:
    """
    This class is responsible for all tests in the info CLI option.
    """
    def test_cli_opts_info(self):
        args = Object()
        a = info.info()
        args.metadata_path = "test"
        a.main(args)
        assert 1
