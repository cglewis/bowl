"""
This module is the test suite of the repositories CLI option for bowl.

Created on 27 July 2014
@author: Charlie Lewis
"""

from bowl.cli_opts import repositories

class Object(object):
    pass

class TestClass:
    """
    This class is responsible for all tests in the repositories CLI option.
    """
    def test_cli_opts_repositories(self):
        args = Object()
        args.z = True
        a = repositories.repositories()
        a.main(args)
        args.z = False
        a.main(args)
        assert 1
