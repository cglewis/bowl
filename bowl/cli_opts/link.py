"""
This module is the link command of bowl.

Created on 14 July 2014
@author: Charlie Lewis
"""
import ast
import os

class link(object):
    """
    This class is responsible for the link command of the cli.
    """
    @classmethod
    def main(self, args):
        directory = args.metadata_path
        directory = os.path.expanduser(directory)
        if not os.path.exists(directory):
            os.makedirs(directory)

        path = os.path.join(os.path.expanduser(args.path), 'services')

        # !! TODO name must be unique
        # !! TODO
        #    test connection
        exists = False
        try:
            if os.path.exists(os.path.join(directory, "repositories")):
                with open(os.path.join(directory, "repositories"), 'r') as f:
                    for line in f:
                        repo = ast.literal_eval(line.strip())
                        if repo['title'] == args.SERVICE_HOST and repo['path'] == path:
                            exists = True
            if not exists:
                with open(os.path.join(directory, "repositories"), 'a') as f:
                    f.write("{" +
                            "'title': '"+args.SERVICE_HOST+"'," +
                            " 'type': 'choice_menu'," +
                            " 'name': '"+args.NAME+"'," +
                            " 'path': '"+path+"'" +
                            "}\n")
            else:
                if not args.z:
                    print "repository has already been linked"
        except:
            if not args.z:
                print "unable to link service host"
            return False
        return True
