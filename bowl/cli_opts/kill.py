"""
This module is the kill command of bowl.

Created on 15 March 2014
@author: Charlie Lewis
"""
import ast
import docker
import os

from bowl.cli_opts import hosts
from docker import Client

class Object(object):
    pass

class kill(object):
    """
    This class is responsible for the kill command of the cli.
    """
    @classmethod
    def main(self, args):
        # !! TODO needs to implement login if using that


        # !! TODO make more robust and read from connected hosts
        #         also deal with the possibility of more than one
        #         container having the same name on different hosts
        try:
            directory = args.metadata_path
            directory = os.path.expanduser(directory)

            host_args = Object()
            host_args.metadata_path = args.metadata_path
            host_args.z = True
            host_a = hosts.hosts.main(host_args)

            with open(os.path.join(directory, "containers"), 'r') as f:
                for line in f:
                    container = ast.literal_eval(line.rstrip("\n"))
                    if container['container_id'] == args.CONTAINER:
                        for host in host_a:
                            if container['host'] in host:
                                c = Client(**kwargs_from_env())
                                #c = docker.Client(base_url='tcp://'+host,
                                #                  version='1.12', timeout=10)
                        c.kill(args.CONTAINER)
                        if not args.z:
                            print "killed "+container['container_id']+" on "+container['host']
        except:
            if not args.z:
                print "unable to kill ",args.CONTAINER
            return False
        return True
