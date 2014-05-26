"""
This module is the connect command of bowl.

Created on 15 March 2014
@author: Charlie Lewis
"""

import os

class connect(object):
    """
    This class is responsible for the connect command of the cli.
    """
    @classmethod
    def main(self, args):
        directory = "~/.bowl"
        directory = os.path.expanduser(directory)
        if not os.path.exists(directory):
            os.makedirs(directory)
        # !! TODO
        #    test connection
        #    allow different port
        try:
            with open(os.path.join(directory, "hosts"), 'a') as f:
                f.write("{" +
                        " 'title': '"+args.DOCKER_HOST+"'," +
                        " 'type': 'choice_menu'" +
                        "}\n")
        except:
            print "unable to add docker host"
