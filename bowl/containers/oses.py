"""
This module is for all operating systems supported for bowl.

Created on 16 March 2014
@author: Charlie Lewis
"""

class oses(object):
    """
    This class is responsible for all available operating systems for bowl.
    """
    def ubuntu(self):
        return {
                'title': "Ubuntu",
                'type': "menu",
                'subtitle': "Please select a version...",
                'options': []
               }
