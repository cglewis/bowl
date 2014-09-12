"""
This module is the subtract command of bowl.

Created on 1 September 2014
@author: Charlie Lewis
"""
import shutil
import os
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
            # !! TODO
            # remove service
            # check if last item (need to remove comma from previous service if there is one
            # check if not last item '},' as opposed to '}'
            # if result is just '{}' then do following todos, otherwise skip"

            # !! TODO
            # if version services are empty, remove it

            # !! TODO
            # if os versions are empty, remove it
        else:
            print "Service doesn't exist."
            sys.exit(0)
