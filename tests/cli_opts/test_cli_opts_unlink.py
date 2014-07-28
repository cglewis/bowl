"""
This module is the test suite of the unlink CLI option for bowl.

Created on 27 July 2014
@author: Charlie Lewis
"""

from bowl.cli_opts import unlink

class TestClass:
    """
    This class is responsible for all tests in the unlink CLI option.
    """
    def test_cli_opts_unlink(self):
        a = unlink.unlink()
        a.main([])
        assert 1
