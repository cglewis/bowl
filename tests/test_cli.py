"""
This module is the test suite of the CLI for bowl.

Created on 27 July 2014
@author: Charlie Lewis
"""
import pytest
import sys

from docker import client
from requests import exceptions

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
        sys.argv = ["", "new", "-n", "--host", "test", "-s", "os:version:type:service", "-l"]
        with pytest.raises(exceptions.ConnectionError):
            cli.main()
        sys.argv = ["", "test"]
        cli.main()
        #sys.argv = ["", "new", "-n", "--host", "127.0.0.1", "-s", "os:version:type:service", "-l"]
        #with pytest.raises(client.APIError):
        #    cli.main()
