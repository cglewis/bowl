"""
This module is the test suite of the delete CLI option for bowl.

Created on 27 July 2014
@author: Charlie Lewis
"""

from bowl.cli_opts import delete

class TestClass:
    """
    This class is responsible for all tests in the delete CLI option.
    """
    def test_cli_opts_delete(self):
        a = delete.delete()
        a.main([])
        assert 1
