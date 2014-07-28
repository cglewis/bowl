"""
This module is the test suite of the remove CLI option for bowl.

Created on 27 July 2014
@author: Charlie Lewis
"""
import pytest

from docker import client
from bowl.cli_opts import remove

class Object(object):
    pass

class TestClass:
    """
    This class is responsible for all tests in the remove CLI option.
    """
    def test_cli_opts_remove(self):
        args = Object()
        args.CONTAINER="test"
        a = remove.remove()
        with pytest.raises(client.APIError):
            a.main(args)
        assert 1
