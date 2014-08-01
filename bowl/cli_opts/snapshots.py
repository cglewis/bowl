"""
This module is the snapshots command of bowl.

Created on 17 July 2014
@author: Charlie Lewis
"""
import ast
import os

class snapshots(object):
    """
    This class is responsible for the snapshots command of the cli.
    """
    @classmethod
    def main(self, args):
        snapshots = []
        try:
            directory = args.metadata_path
            directory = os.path.expanduser(directory)
            with open(os.path.join(directory, "snapshots"), 'r') as f:
                for line in f:
                    snapshot = ast.literal_eval(line.rstrip("\n"))
                    snapshots.append(snapshot['snapshot_id'])
        except:
            pass
        if not args.z:
            for snapshot in snapshots:
                print snapshot
        return snapshots
