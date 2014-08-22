"""
This module is the test suite of the logs CLI option for bowl.

Created on 27 July 2014
@author: Charlie Lewis
"""

from bowl.cli_opts import logs

class Object(object):
    pass

class TestClass:
    """
    This class is responsible for all tests in the logs CLI option.
    """
    def test_cli_opts_logs(self):
        args = Object()
        args.CONTAINER = "test"
        args.metadata_path = "test"
        args.z = True
        a = logs.logs()
        a.main(args)
        args.z = False
        a.main(args)
        assert 1
