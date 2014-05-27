"""
This module is the rm command of bowl.

Created on 26 May 2014
@author: Charlie Lewis
"""
import docker

class remove(object):
    """
    This class is responsible for the rm command of the cli.
    """
    @classmethod
    def main(self, args):
        # !! TODO make more robust and read from connected hosts
        #         also deal with the possibility of more than one
        #         container having the same name on different hosts
        c = docker.Client(base_url='tcp://localhost:4243', version='1.9',
                          timeout=10)
        c.remove_container(args.CONTAINER)
