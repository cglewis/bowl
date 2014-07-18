"""
This module is for all operating systems supported for bowl.

Created on 16 March 2014
@author: Charlie Lewis
"""

class oses(object):
    """
    This class is responsible for all available operating systems for bowl.
    """
    #def main(self, default):
        # if default, default services are wanted, use .default
        # also add in ~/.bowl/services
        # also add in ~/.bowl/repositories
    def ubuntu(self):
        return {
                'title': "Ubuntu",
                'type': "menu",
                'subtitle': "Please select a version...",
                'object': "os",
                'options': []
               }
