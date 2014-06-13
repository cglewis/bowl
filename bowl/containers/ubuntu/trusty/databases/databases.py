"""
This module is for all databases supported for ubuntu:trusty.

Created on 16 March 2014
@author: Charlie Lewis
"""

class databases(object):
    """
    This class is responsible for all available databases for ubuntu:trusty.
    """
    def elasticsearch(self):
        return {
                'title': "elasticsearch",
                'type': "choice_menu",
                'command': "ubuntu:trusty:databases:elasticsearch",
                'cluster': "yes",
                'combine_cmd': "yes",
                'background_cmd': "TODO",
                'tty': "no",
                'interactive': "no"
               }

    def influxdb(self):
        return {
                'title': "influxdb",
                'type': "choice_menu",
                'command': "ubuntu:trusty:databases:influxdb",
                'cluster': "yes",
                'combine_cmd': "yes",
                'background_cmd': "TODO",
                'tty': "no",
                'interactive': "no"
               }

    def mysql(self):
        return {
                'title': "mysql",
                'type': "choice_menu",
                'command': "ubuntu:trusty:databases:mysql",
                'cluster': "no",
                'combine_cmd': "yes",
                'background_cmd': "TODO",
                'tty': "no",
                'interactive': "no"
               }

    def postgresql(self):
        return {
                'title': "postgresql",
                'type': "choice_menu",
                'command': "ubuntu:trusty:databases:postgresql",
                'cluster': "no",
                'combine_cmd': "yes",
                'background_cmd': "TODO",
                'tty': "no",
                'interactive': "no"
               }

    def redis(self):
        return {
                'title': "redis",
                'type': "choice_menu",
                'command': "ubuntu:trusty:databases:redis",
                'cluster': "yes",
                'combine_cmd': "yes",
                'background_cmd': "TODO",
                'tty': "no",
                'interactive': "no"
               }

    def rethinkdb(self):
        return {
                'title': "rethinkdb",
                'type': "choice_menu",
                'command': "ubuntu:trusty:databases:rethinkdb",
                'cluster': "yes",
                'combine_cmd': "yes",
                'background_cmd': "TODO",
                'tty': "no",
                'interactive': "no"
               }
