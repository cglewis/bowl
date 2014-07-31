"""
This module is the test suite of the snapshot CLI option for bowl.

Created on 27 July 2014
@author: Charlie Lewis
"""

from bowl.cli_opts import snapshot

class Object(object):
    pass

class TestClass:
    """
    This class is responsible for all tests in the snapshot CLI option.
    """
    def test_cli_opts_snapshot(self):
        args = Object()
        args.metadata_path = "test"
        args.CONTAINER = "foo"
        args.z = True
        a = snapshot.snapshot()
        a.main(args)
        args.z = False
        a.main(args)
        assert 1
