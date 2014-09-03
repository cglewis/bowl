"""
This module is the test suite of the subtract CLI option for bowl.

Created on 1 September 2014
@author: Charlie Lewis
"""

from bowl.cli_opts import subtract

class TestClass:
    """
    This class is responsible for all tests in the subtract CLI option.
    """
    def test_cli_opts_subtract(self):
        a = subtract.subtract()
        a.main([])
        assert 1
