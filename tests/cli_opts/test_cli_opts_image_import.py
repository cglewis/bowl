"""
This module is the test suite of the image_import CLI option for bowl.

Created on 27 July 2014
@author: Charlie Lewis
"""

from bowl.cli_opts import image_import

class Object(object):
    pass

class TestClass:
    """
    This class is responsible for all tests in the image_import CLI option.
    """
    def test_cli_opts_image_import(self):
        args = Object()
        args.metadata_path="test"
        args.uuid = None
        args.description = ""
        a = image_import.image_import()
        a.main(args)
        assert 1
