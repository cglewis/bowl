"""
This module is the test suite of the CLI for bowl.

Created on 27 July 2014
@author: Charlie Lewis
"""
import pytest
import sys

from bowl import cli

class TestClass:
    """
    This class is responsible for all tests in the CLI.
    """
    def test_cli(self):
        a = cli.cli()
        sys.argv = ["", "-h"]
        with pytest.raises(SystemExit):
            cli.main()
        sys.argv = ["", "new", "-n"]
        cli.main()
