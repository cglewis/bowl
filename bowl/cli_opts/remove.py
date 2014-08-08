"""
This module is the rm command of bowl.

Created on 26 May 2014
@author: Charlie Lewis
"""
import ast
import docker
import os

class remove(object):
    """
    This class is responsible for the rm command of the cli.
    """
    @classmethod
    def main(self, args):
        # !! TODO make more robust and read from connected hosts
        #         also deal with the possibility of more than one
        #         container having the same name on different hosts
        #         also make it easier to specify the container id
        try:
            directory = args.metadata_path
            directory = os.path.expanduser(directory)
            with open(os.path.join(directory, "containers"), 'r') as f:
                for line in f:
                    container = ast.literal_eval(line.rstrip("\n"))
                    if container['container_id'] == args.CONTAINER:
                        c = docker.Client(base_url='tcp://'+container['host']+':2375', version='1.9',
                                          timeout=10)
                        c.remove_container(args.CONTAINER)
                        print "removed "+container['container_id']+" on "+container['host']
        except:
            return False
        return True
