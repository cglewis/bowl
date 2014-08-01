"""
This module is the snapshot command of bowl.

Created on 15 March 2014
@author: Charlie Lewis
"""
import docker
import os

from bowl.cli_opts import list

class Object(object):
    pass

class snapshot(object):
    """
    This class is responsible for the snapshot command of the cli.
    """
    @classmethod
    def main(self, args):
        directory = args.metadata_path
        directory = os.path.expanduser(directory)
        if not os.path.exists(directory):
            os.makedirs(directory)

        list_args = Object()
        list_args.metadata_path = args.metadata_path
        list_args.z = True
        list_a = list.list.main(list_args)

        found = 0
        for container in list_a:
            if args.CONTAINER in container:
                # !! TODO
                print list_a
                found = 1

        if found:
            snapshot_id = []
            try:
                with open(os.path.join(directory, "snapshots"), 'a') as f:
                    # !! TODO
                    f.write("{" +
                            "'title': '"+
                            "}\n")
            except:
                if not args.z:
                    print "unable to snapshot container"
                return False
        else:
            if not args.z:
                print args.CONTAINER, "is not a running container"
            return False
        return True
