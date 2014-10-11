"""
This module is the test suite of the revoke CLI option for bowl.

Created on 11 October 2014
@author: Charlie Lewis
"""

from bowl.cli_opts import revoke

class TestClass:
    """
    This class is responsible for all tests in the revoke CLI option.
    """
    def test_cli_opts_revoke(self):
        a = revoke.revoke()
        a.main([])
        assert 1
