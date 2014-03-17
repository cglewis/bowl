"""
This module is for all versions supported for ubuntu.

Created on 16 March 2014
@author: Charlie Lewis
"""

class versions(object):
    """
    This class is responsible for all available versions for ubuntu.
    """
    def precise(self):
        return {
                'title': "12.04 LTS Precise",
                'type': "menu",
                'subtitle': "Please select services...",
                'options': []
               }
