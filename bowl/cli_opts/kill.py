"""
This module is the kill command of bowl.

Created on 15 March 2014
@author: Charlie Lewis
"""
import docker

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
            c = docker.Client(base_url='tcp://localhost:2375', version='1.9',
                              timeout=10)
            c.kill(args.CONTAINER)
        except:
            print "unable to kill ",args.CONTAINER
