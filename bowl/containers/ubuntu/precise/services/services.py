"""
This module is for all services supported for ubuntu:precise.

Created on 16 March 2014
@author: Charlie Lewis
"""

class services(object):
    """
    This class is responsible for all available services for ubuntu:precise.
    """
    def sshd(self):
        return {
                'title': "SSH Server",
                'type': "choice_menu",
                'command': "ubuntu:precise:sshd"
               }

    def tmux(self):
        return {
                'title': "tmux",
                'type': "choice_menu",
                'command': "ubuntu:precise:tmux"
               }
