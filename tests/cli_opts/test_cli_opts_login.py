"""
This module is the test suite of the login CLI option for bowl.

Created on 27 July 2014
@author: Charlie Lewis
"""

from bowl.cli_opts import login

class TestClass:
    """
    This class is responsible for all tests in the login CLI option.
    """
    def test_cli_opts_login(self):
        a = login.login()
        a.main([])
        assert 1
