"""
This module is the test suite of the list CLI option for bowl.

Created on 27 July 2014
@author: Charlie Lewis
"""

from bowl.cli_opts import list

class Object(object):
    pass

class TestClass:
    """
    This class is responsible for all tests in the list CLI option.
    """
    def test_cli_opts_list(self):
        args = Object()
        args.metadata_path = "test"
        args.z = True
        a = list.list()
        a.main(args)
        args.z = False
        a.main(args)
        assert 1
