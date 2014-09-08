"""
This module is the test suite of the add CLI option for bowl.

Created on 27 July 2014
@author: Charlie Lewis
"""
import os
import shutil

from bowl.cli_opts import add

class Object(object):
    pass

class TestClass:
    """
    This class is responsible for all tests in the add CLI option.
    """
    def test_cli_opts_add(self):
        if os.path.exists("test"):
            shutil.rmtree("test")
        os.makedirs("test")
        open('test/Dockerfile', 'a').close()
        args = Object()
        args.repository = "test"
        args.metadata_path = "test"
        args.OS = "OS"
        args.VERSION = "VERSION"
        args.TYPE = "TYPE"
        args.NAME = "NAME"
        args.JSON = '{"cluster":"yes","combine_cmd":"yes","background_cmd":"bar","tty":"no","interactive":"no"}'
        args.PATH = "test"
        a = add.add()
        a.main(args)
        args.repository = ""
        a.main(args)
        assert 1
