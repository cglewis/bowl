"""
This module is the test suite of the new CLI option for bowl.

Created on 27 July 2014
@author: Charlie Lewis
"""
import pytest

from bowl.cli_opts import new
from requests import exceptions

class Object(object):
    pass

class TestClass:
    """
    This class is responsible for all tests in the new CLI option.
    """
    def test_cli_opts_new_build_options(self):
        args = Object()
        args.metadata_path = "new_test"
        a = new.new()
        menu_dict = a.build_options(self, args)
        assert isinstance(menu_dict, dict)

        args.no_curses = True
        args.toggle_default = False
        args.host = []
        args.host.append("test")

        args.service = []
        args.service.append("os:version:type:service")
        args.image = False

        args.command = False
        args.entrypoint = False
        args.volume = False
        args.volume_from = False
        args.port = False
        args.link = False
        args.name = False
        args.unique = False
        args.user = False

        a.main(args)

        #args.command = True
        #args.entrypoint = True
        #args.volume = True
        #args.port = True
        #args.link = True
        #args.name = True
        #args.unique = True
        #args.user = True

        #a.main(args)

        #args.service = False
        #args.image = True

        #a.main(args)
