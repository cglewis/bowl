"""
This module is the test suite of the connect CLI option for bowl.

Created on 27 July 2014
@author: Charlie Lewis
"""

from bowl.cli_opts import connect

class Object(object):
    pass

class TestClass:
    """
    This class is responsible for all tests in the connect CLI option.
    """
    def test_cli_opts_connect(self):
        args = Object()
        args.metadata_path="test"
        a = connect.connect()
        a.main(args)
        assert 1
