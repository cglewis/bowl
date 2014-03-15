"""
This module is the version command of punt.

Created on 14 March 2014
@author: Charlie Lewis
"""

import pkg_resources

class version(object):
    """
    This class is responsible for the version command of the cli.
    """
    @classmethod
    def main(self, args):
        print pkg_resources.get_distribution("punt").version
