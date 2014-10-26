"""
This module is the logs command of bowl.

Created on 14 March 2014
@author: Charlie Lewis
"""
import docker
import os

from bowl.cli_opts import hosts
from bowl.cli_opts import list

class Object(object):
    pass

class logs(object):
    """
    This class is responsible for the logs command of the cli.
    """
    @classmethod
    def main(self, args):
        # !! TODO needs to implement login if using that


        directory = args.metadata_path
        directory = os.path.expanduser(directory)
        if not os.path.exists(directory):
            os.makedirs(directory)

        list_args = Object()
        list_args.metadata_path = args.metadata_path
        list_args.z = True
        list_a = list.list.main(list_args)

        host_args = Object()
        host_args.metadata_path = args.metadata_path
        host_args.z = True
        host_a = hosts.hosts.main(host_args)

        for container in list_a:
            if args.CONTAINER in container:
                 host = container.split(",")[1]
                 cont = container.split(",")[0]
                 try:
                     for h in host_a:
                         if host in h:
                             c = docker.Client(base_url='tcp://'+h,
                                               version='1.12',
                                               timeout=2)
                     output = c.logs(cont)
                     if not args.z:
                         print output
                     return output
                 except:
                     if not args.z:
                         print "unable to get logs for container "+cont
                     return False
