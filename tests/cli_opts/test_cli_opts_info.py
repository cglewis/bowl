"""
This module is the test suite of the info CLI option for bowl.

Created on 27 July 2014
@author: Charlie Lewis
"""

from bowl.cli_opts import info

class TestClass:
    """
    This class is responsible for all tests in the info CLI option.
    """
    def test_cli_opts_info(self):
        a = info.info()
        a.main([])
        assert 1
