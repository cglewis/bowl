"""
This module is for all tools supported for ubuntu:precise.

Created on 26 June 2014
@author: Charlie Lewis
"""

class tools(object):
    """
    This class is responsible for all available tools for ubuntu:precise.
    """
    def httpie(self):
        return {
                'title': "httpie",
                'type': "choice_menu",
                'command': "ubuntu:precise:tools:httpie",
                'object': "tool",
                'cluster': "no",
                'combine_cmd': "no",
                'tty': "yes",
                'interactive': "no"
               }
