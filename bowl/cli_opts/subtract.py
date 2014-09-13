"""
This module is the subtract command of bowl.

Created on 1 September 2014
@author: Charlie Lewis
"""
import fileinput
import os
import shutil
import sys

class subtract(object):
    """
    This class is responsible for the subtract command of the cli.
    """
    @classmethod
    def main(self, args):
        if os.path.exists(os.path.join(args.metadata_path,
                                       args.OS,
                                       args.VERSION,
                                       args.TYPE,
                                       'dockerfiles',
                                       args.NAME)):
            # remove dockerfiles
            shutil.rmtree(os.path.join(args.metadata_path,
                                       args.OS,
                                       args.VERSION,
                                       args.TYPE,
                                       'dockerfiles',
                                       args.NAME))
            # remove service
            found = 0
            for line in fileinput.input(os.path.join(args.metadata_path, args.OS, args.VERSION, args.TYPE, args.TYPE), inplace=True):
                if args.NAME in line:
                    found = 1
                elif found == 1:
                    if line == " }\n" or line == " },\n":
                        found = 0
                else:
                    print "%s" (line),

            # !! TODO
            # if result is just '{}' then do following todos, otherwise skip"

            # !! TODO
            # if version services are empty, remove it and dockerfiles dir

            # !! TODO
            # if os versions are empty, remove it
        else:
            print "Service doesn't exist."
            sys.exit(0)
