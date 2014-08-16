"""
This module is the test command of bowl.

Created on 11 August 2014
@author: Charlie Lewis
"""
import os
import pytest

class test(object):
    """
    This class is responsible for the test command of the cli.
    """
    @classmethod
    def main(self, args):
        # !! TODO
        print args
        if args.f:
            pass
        else:
            # run tests
            #out = pytest.main(['-v', '--cov', 'bowl', '--cov-report', 'term-missing', '-x', args.path])
            cmd = 'py.test -v --cov bowl --cov-report term-missing -x ' + args.path
            out = os.popen(cmd).read()
            print out
            pass
