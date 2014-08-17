"""
This module is the test command of bowl.

Created on 11 August 2014
@author: Charlie Lewis
"""
import os

class test(object):
    """
    This class is responsible for the test command of the cli.
    """
    @classmethod
    def main(self, args):
        print args
        if args.f:
            pass
        else:
            # run tests
            cmd = 'py.test -v --cov bowl --cov-report term-missing -x ' + args.path
            out = os.popen(cmd).read()
            print out
            if args.c:
                cmd = 'coveralls --base_dir ' + args.path
                out = os.popen(cmd).read()
                print out
