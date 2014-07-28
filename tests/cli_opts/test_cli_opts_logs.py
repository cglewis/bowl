"""
This module is the test suite of the logs CLI option for bowl.

Created on 27 July 2014
@author: Charlie Lewis
"""

from bowl.cli_opts import logs

class TestClass:
    """
    This class is responsible for all tests in the logs CLI option.
    """
    def test_cli_opts_logs(self):
        a = logs.logs()
        a.main([])
        assert 1
