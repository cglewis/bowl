"""
This module is the info command of bowl.

Created on 14 March 2014
@author: Charlie Lewis
"""
import ast
import os

class info(object):
    """
    This class is responsible for the info command of the cli.
    """
    @classmethod
    def main(self, args):
        containers = 0
        hosts = 0
        images = 0
        repositories = 0
        snapshots = 0
        try:
            directory = args.metadata_path
            directory = os.path.expanduser(directory)
            if os.path.exists(os.path.join(directory, "containers")):
                with open(os.path.join(directory, "containers"), 'r') as f:
                    for line in f:
                        containers += 1
            if os.path.exists(os.path.join(directory, "hosts")):
                with open(os.path.join(directory, "hosts"), 'r') as f:
                    for line in f:
                        hosts += 1
            if os.path.exists(os.path.join(directory, "images")):
                with open(os.path.join(directory, "images"), 'r') as f:
                    for line in f:
                        images += 1
            if os.path.exists(os.path.join(directory, "images")):
                with open(os.path.join(directory, "images"), 'r') as f:
                    for line in f:
                        images += 1
            if os.path.exists(os.path.join(directory, "images")):
                with open(os.path.join(directory, "images"), 'r') as f:
                    for line in f:
                        images += 1
            print "containers: ",containers
            print "hosts: ",hosts
            print "images: ",images
            print "repositories: ",repositories
            print "snapshots: ",snapshots
        except:
            print "unable to get info"
