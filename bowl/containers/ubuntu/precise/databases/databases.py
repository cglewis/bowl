"""
This module is for all databases supported for ubuntu:precise.

Created on 16 March 2014
@author: Charlie Lewis
"""

class databases(object):
    """
    This class is responsible for all available databases for ubuntu:precise.
    """
    def redis(self):
        return {
                'title': "redis",
                'type': "choice_menu",
                'command': "ubuntu:precise:redis"
               }
