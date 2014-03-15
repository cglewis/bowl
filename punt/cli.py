"""
This module is the commandline interface of punt.

Created on 14 March 2014
@author: Charlie Lewis
"""

import argparse
import redis
import socket
import sys
from punt.cli_opts import hosts
from punt.cli_opts import info
from punt.cli_opts import list
from punt.cli_opts import login
from punt.cli_opts import logs
from punt.cli_opts import new
from punt.cli_opts import version

class cli(object):
    """
    This class is responsible for all commandline operations.
    """
    def parse_args(self):
        parser = argparse.ArgumentParser()

        subparsers = parser.add_subparsers(title='punt commands')

        # hosts
        parse_hosts = subparsers.add_parser('hosts',
                                            help='list hosts that are registered')
        parse_hosts.set_defaults(func=hosts.hosts.main)

        # info
        parse_info = subparsers.add_parser('info',
                                           help='display system-wide information')
        parse_info.set_defaults(func=info.info.main)

        # list
        parse_list = subparsers.add_parser('list',
                                           help='list containers running')
        parse_list.set_defaults(func=list.list.main)

        # login
        parse_login = subparsers.add_parser('login',
                                            help='login with credentials')
        parse_login.add_argument('-e', '--email',
                                 help='email address')
        parse_login.add_argument('-u', '--username',
                                 help='username')
        parse_login.add_argument('PASSWORD',
                                 help='password')
        parse_login.set_defaults(func=login.login.main)

        # logs
        parse_logs = subparsers.add_parser('logs',
                                           help='server logs')
        parse_logs.add_argument('HOST',
                                default="localhost",
                                help='specify host to get logs from')
        parse_logs.set_defaults(func=logs.logs.main)

        # new
        parse_new = subparsers.add_parser('new',
                                           help='new container')
        parse_new.set_defaults(func=new.new.main)

        # version
        parse_version = subparsers.add_parser('version',
                                           help='show version')
        parse_version.set_defaults(func=version.version.main)

        args = parser.parse_args()
        if args.func:
            args.func(args)

def main():
    cli().parse_args()

if __name__ == "__main__": # pragma: no cover
    main()
