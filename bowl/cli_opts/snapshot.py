"""
This module is the snapshot command of bowl.

Created on 15 March 2014
@author: Charlie Lewis
"""
from bowl.cli_opts import list

class Object(object):
    pass

class snapshot(object):
    """
    This class is responsible for the snapshot command of the cli.
    """
    @classmethod
    def main(self, args):
        list_args = Object()
        list_args.metadata_path = args.metadata_path
        list_args.z = True

        list_a = list.list.main(list_args)
        if args.CONTAINER in list_a:
            # !! TODO
            print list_a
        else:
            print args.CONTAINER, "is not a running container"
