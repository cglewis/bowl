"""
This module is for all environment tools supported for ubuntu:precise.

Created on 16 March 2014
@author: Charlie Lewis
"""

class environment(object):
    """
    This class is responsible for all available environment tools for
    ubuntu:precise.
    """
    def python(self):
        return {
                'title': "python",
                'type': "choice_menu",
                'command': "ubuntu:precise:python"
               }
