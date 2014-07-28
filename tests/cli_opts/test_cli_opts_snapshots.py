"""
This module is the test suite of the snapshots CLI option for bowl.

Created on 27 July 2014
@author: Charlie Lewis
"""

from bowl.cli_opts import snapshots

class TestClass:
    """
    This class is responsible for all tests in the snapshots CLI option.
    """
    def test_cli_opts_snapshots(self):
        a = snapshots.snapshots()
        a.main([])
        assert 1
