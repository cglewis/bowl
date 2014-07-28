"""
This module is the hosts command of bowl.

Created on 14 March 2014
@author: Charlie Lewis
"""
import ast
import os

class hosts(object):
    """
    This class is responsible for the hosts command of the cli.
    """
    @classmethod
    def main(self, args):
        hosts = []
        try:
            directory = args.metadata_path
            directory = os.path.expanduser(directory)
            with open(os.path.join(directory, "hosts"), 'r') as f:
                for line in f:
                    host = ast.literal_eval(line.rstrip("\n"))
                    hosts.append(host['title'])
        except:
            pass
        if not args.z:
            for host in hosts:
                print host
        return hosts
