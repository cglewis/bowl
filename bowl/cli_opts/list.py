"""
This module is the list command of bowl.

Created on 14 March 2014
@author: Charlie Lewis
"""
import ast
import docker
import os

from bowl.cli_opts import hosts

class Object(object):
    pass

class list(object):
    """
    This class is responsible for the list command of the cli.
    """
    @classmethod
    def main(self, args):
        containers = []
        try:
            directory = args.metadata_path
            directory = os.path.expanduser(directory)
            with open(os.path.join(directory, "containers"), 'r') as f:
                for line in f:
                    container = ast.literal_eval(line.rstrip("\n"))
                    containers.append(container['container_id']+","+container['host'])
        except:
            pass
        host_args = Object()
        host_args.metadata_path = args.metadata_path
        host_args.z = True
        host_a = hosts.hosts.main(host_args)

        host_c = []
        for host in host_a:
            c = docker.Client(base_url='tcp://'+host+':2375', version='1.9',
                              timeout=2)
            host_c.append(c.containers())

        compare_containers = []
        try:
            for container in host_c[0]:
                compare_containers.append(container['Names'][0][1:])
        except:
            if not args.z:
                print "no hosts found"
            return ""

        running_containers = []
        for item in containers:
            container_id = item.split(',')[0]
            if container_id in compare_containers:
                running_containers.append(item)

        if not args.z:
            for container in running_containers:
                print container
        return running_containers
