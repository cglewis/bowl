"""
This module is the test suite of the subtract CLI option for bowl.

Created on 1 September 2014
@author: Charlie Lewis
"""

from bowl.cli_opts import subtract

class Object(object):
    pass

class TestClass:
    """
    This class is responsible for all tests in the subtract CLI option.
    """
    def test_cli_opts_subtract(self):
        args = Object()
        args.metadata_path = "test"
        args.OS = "OS"
        args.VERSION = "VERSION"
        args.TYPE = "TYPE"
        args.NAME = "NAME"
        a = subtract.subtract()
        a.main(args)
        args.metadata_path = ""
        a.main(args)
        assert 1
