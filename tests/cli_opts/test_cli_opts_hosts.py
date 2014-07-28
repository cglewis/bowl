"""
This module is the test suite of the hosts CLI option for bowl.

Created on 27 July 2014
@author: Charlie Lewis
"""

from bowl.cli_opts import hosts

class Object(object):
    pass

class TestClass:
    """
    This class is responsible for all tests in the hosts CLI option.
    """
    def test_cli_opts_hosts(self):
        args = Object()
        args.z = True
        a = hosts.hosts()
        a.main(args)
        args.z = False
        a.main(args)
        assert 1
