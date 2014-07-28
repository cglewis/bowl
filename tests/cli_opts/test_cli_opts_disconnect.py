"""
This module is the test suite of the disconnect CLI option for bowl.

Created on 27 July 2014
@author: Charlie Lewis
"""

from bowl.cli_opts import disconnect

class TestClass:
    """
    This class is responsible for all tests in the disconnect CLI option.
    """
    def test_cli_opts_disconnect(self):
        a = disconnect.disconnect()
        a.main([])
        assert 1
