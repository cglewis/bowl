"""
This module is the test suite of the test CLI option for bowl.

Created on 11 August 2014
@author: Charlie Lewis
"""

from bowl.cli_opts import test

class TestClass:
    """
    This class is responsible for all tests in the test CLI option.
    """
    def test_cli_opts_test(self):
        # !! TODO make sure this isn't recursive
        a = test.test()
        a.main([])
        assert 1
