"""
This module is the disconnect command of bowl.

Created on 15 March 2014
@author: Charlie Lewis
"""
import ast
import fileinput
import os

class disconnect(object):
    """
    This class is responsible for the disconnect command of the cli.
    """
    @classmethod
    def main(self, args):
        try:
            directory = args.metadata_path
            directory = os.path.expanduser(directory)
            # !! TODO need to do check if specfied host was not there to begin with
            for line in fileinput.input(os.path.join(directory, "hosts"), inplace=True):
                host = ast.literal_eval(line.rstrip('\n'))
                if args.DOCKER_HOST != host['title']:
                    print "%s" % (line),
        except:
            print "unable to remove docker host"
            return False
        return True
