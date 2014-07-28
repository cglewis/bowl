"""
This module is the repositories command of bowl.

Created on 19 July 2014
@author: Charlie Lewis
"""
import ast
import os

class repositories(object):
    """
    This class is responsible for the repositories command of the cli.
    """
    @classmethod
    def main(self, args):
        repositories = []
        try:
            directory = args.metadata_path
            directory = os.path.expanduser(directory)
            with open(os.path.join(directory, "repositories"), 'r') as f:
                for line in f:
                    repository = ast.literal_eval(line.rstrip("\n"))
                    repositories.append(repository['title'])
        except:
            pass
        if not args.z:
            for repository in repositories:
                print repository
        return repositories
