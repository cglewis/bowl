"""
This module is the link command of bowl.

Created on 14 July 2014
@author: Charlie Lewis
"""
import os

class link(object):
    """
    This class is responsible for the link command of the cli.
    """
    @classmethod
    def main(self, args):
        directory = "~/.bowl"
        directory = os.path.expanduser(directory)
        if not os.path.exists(directory):
            os.makedirs(directory)
        # !! TODO
        #    test connection
        try:
            with open(os.path.join(directory, "repositories"), 'a') as f:
                f.write("{" +
                        "'title': '"+args.SERVICE_HOST+"'," +
                        " 'type': 'choice_menu'" +
                        "}\n")
        except:
            print "unable to add service host"
            return False
        return True
