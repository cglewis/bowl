"""
This module is the test suite of the version CLI option for bowl.

Created on 27 July 2014
@author: Charlie Lewis
"""
import pkg_resources

from bowl.cli_opts import version

class TestClass:
    """
    This class is responsible for all tests in the version CLI option.
    """
    def test_cli_opts_version(self):
        version_pkg = pkg_resources.get_distribution("bowl").version
        assert version.version.main([]) == version_pkg
