"""
This module is the test suite of the images CLI option for bowl.

Created on 27 July 2014
@author: Charlie Lewis
"""

from bowl.cli_opts import images

class Object(object):
    pass

class TestClass:
    """
    This class is responsible for all tests in the images CLI option.
    """
    def test_cli_opts_images(self):
        args = Object()
        args.z = True
        a = images.images()
        a.main(args)
        args.z = False
        a.main(args)
        assert 1
