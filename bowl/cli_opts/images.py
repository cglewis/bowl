"""
This module is the images command of bowl.

Created on 22 June 2014
@author: Charlie Lewis
"""
import ast
import os

class images(object):
    """
    This class is responsible for the images command of the cli.
    """
    @classmethod
    def main(self, args):
        images = []
        try:
            directory = args.metadata_path
            directory = os.path.expanduser(directory)
            with open(os.path.join(directory, "images"), 'r') as f:
                for line in f:
                    image = ast.literal_eval(line.rstrip("\n"))
                    images.append(image['title'])
        except:
            pass
        if not args.z:
            for image in images:
                print image
        return images
