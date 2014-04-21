"""
This module is for all services supported for ubuntu:precise.

Created on 16 March 2014
@author: Charlie Lewis
"""

class services(object):
    """
    This class is responsible for all available services for ubuntu:precise.
    """
    def rsyslog(self):
        return {
                'title': "rsyslog",
                'type': "choice_menu",
                'command': "ubuntu:precise:services:rsyslog",
                'combine_cmd': "yes",
                'tty': "no",
                'interactive': "no"
               }

    def sshd(self):
        return {
                'title': "SSH Server",
                'type': "choice_menu",
                'command': "ubuntu:precise:services:sshd",
                'combine_cmd': "yes",
                'tty': "no",
                'interactive': "no"
               }

    def tmux(self):
        return {
                'title': "tmux",
                'type': "choice_menu",
                'command': "ubuntu:precise:services:tmux",
                'combine_cmd': "no",
                'tty': "yes",
                'interactive': "yes"
               }
