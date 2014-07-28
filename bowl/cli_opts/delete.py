"""
This module is the delete command of bowl.

Created on 22 June 2014
@author: Charlie Lewis
"""
import ast
import fileinput
import os

class delete(object):
    """
    This class is responsible for the delete command of the cli.
    """
    @classmethod
    def main(self, args):
        try:
            directory = args.metadata_path
            directory = os.path.expanduser(directory)
            # !! TODO need to do check if specfied image was not there to begin with
            for line in fileinput.input(os.path.join(directory, "images"), inplace=True):
                image = ast.literal_eval(line.rstrip('\n'))
                if args.IMAGE_NAME != image['title']:
                    print "%s" % (line),
        except:
            print "unable to delete image"
            return False
        return True

