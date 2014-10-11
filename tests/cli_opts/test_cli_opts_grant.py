"""
This module is the test suite of the grant CLI option for bowl.

Created on 11 October 2014
@author: Charlie Lewis
"""

from bowl.cli_opts import grant

class TestClass:
    """
    This class is responsible for all tests in the grant CLI option.
    """
    def test_cli_opts_grant(self):
        a = grant.grant()
        a.main([])
        assert 1
