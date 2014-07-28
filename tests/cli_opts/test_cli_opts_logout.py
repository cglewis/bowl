"""
This module is the test suite of the logout CLI option for bowl.

Created on 27 July 2014
@author: Charlie Lewis
"""

from bowl.cli_opts import logout

class TestClass:
    """
    This class is responsible for all tests in the logout CLI option.
    """
    def test_cli_opts_logout(self):
        a = logout.logout()
        a.main([])
        assert 1
