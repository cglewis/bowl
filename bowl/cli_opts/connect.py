"""
This module is the connect command of bowl.

Created on 15 March 2014
@author: Charlie Lewis
"""

import ast
import os
import sys

class connect(object):
    """
    This class is responsible for the connect command of the cli.
    """
    @classmethod
    def main(self, args):
        # !! TODO needs to implement login if using that


        directory = args.metadata_path
        directory = os.path.expanduser(directory)
        if not os.path.exists(directory):
            os.makedirs(directory)
        # !! TODO
        #    test connection
        exists = False
        try:
            if os.path.exists(os.path.join(directory, "hosts")):
                with open(os.path.join(directory, "hosts"), 'r') as f:
                    for line in f:
                        repo = ast.literal_eval(line.strip())
                        if repo['title'] == args.DOCKER_HOST:
                            exists = True
            if not exists:
                with open(os.path.join(directory, "hosts"), 'a') as f:
                    host_dict = {}
                    host_dict['title'] = args.DOCKER_HOST
                    host_dict['port'] = args.port
                    host_dict['type'] = 'choice_menu'
                    f.write(str(host_dict)+"\n")
            else:
                print "host has already been connected"
        except:
            print sys.exc_info()
            print "unable to add docker host"
            return False
        return True
