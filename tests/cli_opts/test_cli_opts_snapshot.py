"""
This module is the test suite of the snapshot CLI option for bowl.

Created on 27 July 2014
@author: Charlie Lewis
"""

from bowl.cli_opts import snapshot

class TestClass:
    """
    This class is responsible for all tests in the snapshot CLI option.
    """
    def test_cli_opts_snapshot(self):
        a = snapshot.snapshot()
        a.main([])
        assert 1
