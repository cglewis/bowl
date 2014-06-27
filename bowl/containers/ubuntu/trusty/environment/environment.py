"""
This module is for all environment tools supported for ubuntu:trusty.

Created on 16 March 2014
@author: Charlie Lewis
"""

class environment(object):
    """
    This class is responsible for all available environment tools for
    ubuntu:trusty.
    """
    def golang(self):
        return {
                'title': "golang",
                'type': "choice_menu",
                'command': "ubuntu:trusty:environment:golang",
                'object': "environment",
                'combine_cmd': "no",
                'tty': "yes",
                'interactive': "yes"
               }

    def python(self):
        return {
                'title': "python",
                'type': "choice_menu",
                'command': "ubuntu:trusty:environment:python",
                'object': "environment",
                'combine_cmd': "no",
                'tty': "yes",
                'interactive': "yes"
               }

    def tmux(self):
        return {
                'title': "tmux",
                'type': "choice_menu",
                'command': "ubuntu:trusty:environment:tmux",
                'object': "environment",
                'combine_cmd': "no",
                'tty': "yes",
                'interactive': "yes"
               }
