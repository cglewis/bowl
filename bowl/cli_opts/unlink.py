"""
This module is the unlink command of bowl.

Created on 14 July 2014
@author: Charlie Lewis
"""
import ast
import fileinput
import os

class unlink(object):
    """
    This class is responsible for the unlink command of the cli.
    """
    @classmethod
    def main(self, args):
        try:
            directory = args.metadata_path
            directory = os.path.expanduser(directory)
            # !! TODO need to do check if specfied repository was not there to begin with
            for line in fileinput.input(os.path.join(directory, "repositories"), inplace=True):
                host = ast.literal_eval(line.rstrip('\n'))
                if args.NAME != host['name'] and directory != host['path']:
                    print "%s" % (line),
        except:
            # !! TODO don't print as it will replace what's in repositories
            #print "unable to remove service repository"
            return False
        return True
