"""
This module is the test suite of the stop CLI option for bowl.

Created on 27 July 2014
@author: Charlie Lewis
"""

from bowl.cli_opts import stop

class Object(object):
    pass

class TestClass:
    """
    This class is responsible for all tests in the stop CLI option.
    """
    def test_cli_opts_stop(self):
        args = Object()
        args.metadata_path="test"
        args.z = True
        a = stop.stop()
        a.main(args)
        args.z = False
        a.main(args)
        assert 1
