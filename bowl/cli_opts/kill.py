"""
This module is the kill command of bowl.

Created on 15 March 2014
@author: Charlie Lewis
"""
import ast
import docker
import os

class kill(object):
    """
    This class is responsible for the kill command of the cli.
    """
    @classmethod
    def main(self, args):
        # !! TODO make more robust and read from connected hosts
        #         also deal with the possibility of more than one
        #         container having the same name on different hosts
        try:
            directory = args.metadata_path
            directory = os.path.expanduser(directory)
            with open(os.path.join(directory, "containers"), 'r') as f:
                for line in f:
                    container = ast.literal_eval(line.rstrip("\n"))
                    if container['container_id'] == args.CONTAINER:
                        c = docker.Client(base_url='tcp://'+container['host']+':2375', version='1.12',
                                          timeout=10)
                        c.kill(args.CONTAINER)
                        if not args.z:
                            print "killed "+container['container_id']+" on "+container['host']
        except:
            if not args.z:
                print "unable to kill ",args.CONTAINER
            return False
        return True
