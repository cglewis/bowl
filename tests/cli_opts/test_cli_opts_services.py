"""
This module is the test suite of the services CLI option for bowl.

Created on 27 July 2014
@author: Charlie Lewis
"""

from bowl.cli_opts import services

class Object(object):
    pass

class TestClass:
    """
    This class is responsible for all tests in the services CLI option.
    """
    def test_cli_opts_services(self):
        args = Object()
        args.metadata_path="test"
        args.z = False
        args.quiet = False
        args.json = False
        a = services.services()
        a.main(args)
        args.metadata_path="test2"
        args.z = True
        args.quiet = False
        args.json = False
        a.main(args)
        args.z = False
        args.quiet = True
        args.json = False
        a.main(args)
        args.z = False
        args.quiet = False
        args.json = True
        a.main(args)
        args.z = True
        args.quiet = True
        args.json = False
        a.main(args)
        args.z = True
        args.quiet = False
        args.json = True
        a.main(args)
        args.z = False
        args.quiet = True
        args.json = True
        a.main(args)
        args.z = True
        args.quiet = True
        args.json = True
        a.main(args)
        assert 1
