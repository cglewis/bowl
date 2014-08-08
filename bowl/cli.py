"""
This module is the commandline interface of bowl.

Created on 14 March 2014
@author: Charlie Lewis
"""

import argparse
from bowl.cli_opts import add
from bowl.cli_opts import connect
from bowl.cli_opts import delete
from bowl.cli_opts import disconnect
from bowl.cli_opts import hosts
from bowl.cli_opts import image_import
from bowl.cli_opts import images
from bowl.cli_opts import info
from bowl.cli_opts import kill
from bowl.cli_opts import link
from bowl.cli_opts import list
from bowl.cli_opts import login
from bowl.cli_opts import logout
from bowl.cli_opts import logs
from bowl.cli_opts import new
from bowl.cli_opts import remove
from bowl.cli_opts import repositories
from bowl.cli_opts import services
from bowl.cli_opts import snapshot
from bowl.cli_opts import snapshots
from bowl.cli_opts import start
from bowl.cli_opts import stop
from bowl.cli_opts import unlink
from bowl.cli_opts import update
from bowl.cli_opts import version

class cli(object):
    """
    This class is responsible for all commandline operations.
    """
    def parse_args(self):
        default_metadata_path = "~/.bowl"

        parser = argparse.ArgumentParser()

        subparsers = parser.add_subparsers(title='bowl commands')

        # add
        parse_add = subparsers.add_parser('add',
                                           help='add a service')
        parse_add.add_argument('OS',
                                help='specify operating system for service')
        parse_add.add_argument('VERSION',
                                help='specify version of operating system')
        parse_add.add_argument('TYPE',
                                help='specify type of service (database, environment, service)')
        parse_add.add_argument('NAME',
                                help='specify name of service')
        parse_add.add_argument('JSON',
                                help='JSON object or path to JSON object that contains associated metadata')
        parse_add.add_argument('PATH',
                                help='path that contains the Dockerfile')
        parse_add.add_argument('--metadata_path', '-m',
                               default=default_metadata_path,
                               help='metadata path, default '+default_metadata_path)
        # !! TODO use default, and restructure if/else in add
        parse_add.add_argument('--repository', '-r',
                                help='specify repository to add service to, use localhost by default')
        parse_add.set_defaults(func=add.add.main)

        # connect
        parse_connect = subparsers.add_parser('connect',
                                              help='connect to a docker host')
        parse_connect.add_argument('DOCKER_HOST',
                                   help='specify docker host to connect to')
        parse_connect.add_argument('--metadata_path', '-m',
                                   default=default_metadata_path,
                                   help='metadata path, default '+default_metadata_path)
        parse_connect.set_defaults(func=connect.connect.main)

        # delete
        parse_delete = subparsers.add_parser('delete',
                                             help='delete an image')
        parse_delete.add_argument('IMAGE_NAME',
                                  help='specify name of image to delete')
        parse_delete.add_argument('--metadata_path', '-m',
                                  default=default_metadata_path,
                                  help='metadata path, default '+default_metadata_path)
        parse_delete.set_defaults(func=delete.delete.main)

        # disconnect
        parse_disconnect = subparsers.add_parser('disconnect',
                                                 help='disconnect from a docker host')
        parse_disconnect.add_argument('DOCKER_HOST',
                                      help='specify docker host to disconnect from')
        parse_disconnect.add_argument('--metadata_path', '-m',
                                      default=default_metadata_path,
                                      help='metadata path, default '+default_metadata_path)
        parse_disconnect.set_defaults(func=disconnect.disconnect.main)

        # hosts
        parse_hosts = subparsers.add_parser('hosts',
                                            help='list hosts that are registered')
        parse_hosts.add_argument('--metadata_path', '-m',
                                 default=default_metadata_path,
                                 help='metadata path, default '+default_metadata_path)
        parse_hosts.add_argument('-z',
                                 action='store_true',
                                 help='do not print any output')
        parse_hosts.set_defaults(func=hosts.hosts.main)

        # images
        parse_images = subparsers.add_parser('images',
                                             help='list images')
        parse_images.add_argument('--metadata_path', '-m',
                                  default=default_metadata_path,
                                  help='metadata path, default '+default_metadata_path)
        parse_images.add_argument('-z',
                                  action='store_true',
                                  help='do not print any output')
        parse_images.set_defaults(func=images.images.main)

        # import
        parse_import = subparsers.add_parser('import',
                                             help='import an image')
        parse_import.add_argument('IMAGE_NAME',
                                  help='specify name of image to import')
        parse_import.add_argument('DOCKER_HOST',
                                  help='specify Docker host of image to import')
        parse_import.add_argument('-d', '--description',
                                  help='description of image to import')
        parse_import.add_argument('--metadata_path', '-m',
                                  default=default_metadata_path,
                                  help='metadata path, default '+default_metadata_path)
        parse_import.add_argument('-u', '--uuid',
                                  help='uuid of image to import')
        # use non-standard naming scheme to not conflict with python's import
        parse_import.set_defaults(func=image_import.image_import.main)

        # info
        parse_info = subparsers.add_parser('info',
                                           help='display system-wide information')
        parse_info.add_argument('-z',
                                action='store_true',
                                help='do not print any output')
        parse_info.set_defaults(func=info.info.main)

        # kill
        parse_kill = subparsers.add_parser('kill',
                                           help='kill running container')
        parse_kill.add_argument('CONTAINER',
                                help='specify container to kill')
        parse_kill.set_defaults(func=kill.kill.main)

        # link
        parse_link = subparsers.add_parser('link',
                                           help='link to a service repository host')
        parse_link.add_argument('SERVICE_HOST',
                                help='specify service repository host to connect to')
        parse_link.add_argument('--metadata_path', '-m',
                                default=default_metadata_path,
                                help='metadata path, default '+default_metadata_path)
        parse_link.add_argument('-z',
                                action='store_true',
                                help='do not print any output')
        parse_link.set_defaults(func=link.link.main)

        # list
        parse_list = subparsers.add_parser('list',
                                           help='list containers running')
        parse_list.add_argument('--metadata_path', '-m',
                                default=default_metadata_path,
                                help='metadata path, default '+default_metadata_path)
        parse_list.add_argument('-z',
                                action='store_true',
                                help='do not print any output')
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

        # logout
        parse_logout = subparsers.add_parser('logout',
                                             help='logout')
        parse_logout.set_defaults(func=logout.logout.main)

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
        parse_new.add_argument('--metadata_path', '-m',
                               default=default_metadata_path,
                               help='metadata path, default '+default_metadata_path)
        parse_new.add_argument('--no_curses', '-n',
                               action='store_true',
                               help='do not use curses')
        parse_new.add_argument('--service', '-s',
                               action='append',
                               help='add a service to the container, can be used more than once, only used with no_curses')
        parse_new.add_argument('--image', '-i',
                               help='specify an image, only used with no_curses')
        parse_new.add_argument('--host',
                               action='append',
                               help='add a host to run the container one, can be used more than once, only used with no_curses')
        parse_new.add_argument('--command', '-c',
                               action='store_true',
                               help='override command at runtime of container, only used with no_curses')
        parse_new.add_argument('--entrypoint', '-e',
                               action='store_true',
                               help='override entrypoint at runtime of container, only used with no_curses')
        parse_new.add_argument('--volume', '-v',
                               action='store_true',
                               help='add volumes at runtime of container, only used with no_curses')
        parse_new.add_argument('--port', '-p',
                               action='store_true',
                               help='set ports at runtime of container, only used with no_curses')
        parse_new.add_argument('--link', '-l',
                               action='store_true',
                               help='add links to containers at runtime of container, only used with no_curses')
        parse_new.add_argument('--name',
                               action='store_true',
                               help='set ports at runtime of container, only used with no_curses')
        parse_new.add_argument('--unique', '-u',
                               action='store_true',
                               help='set different runtime parameters for each container, only used with no_curses')
        parse_new.add_argument('--user',
                               action='store_true',
                               help='add a user at runtime of container, only used with no_curses')
        parse_new.set_defaults(func=new.new.main)

        # remove
        parse_remove = subparsers.add_parser('rm',
                                             help='remove a container')
        parse_remove.add_argument('CONTAINER',
                                  help='specify container to remove')
        parse_remove.add_argument('--metadata_path', '-m',
                                  default=default_metadata_path,
                                  help='metadata path, default '+default_metadata_path)
        parse_remove.set_defaults(func=remove.remove.main)

        # repositories
        parse_repositories = subparsers.add_parser('repositories',
                                                   help='list repositories that are registered')
        parse_repositories.add_argument('-z',
                                    action='store_true',
                                    help='do not print any output')
        parse_repositories.set_defaults(func=repositories.repositories.main)

        # services
        parse_services = subparsers.add_parser('services',
                                               help='list services')
        parse_services.add_argument('-j', '--json',
                                    action='store_true',
                                    help='print complete JSON object for each service')
        parse_services.add_argument('--metadata_path', '-m',
                                    default=default_metadata_path,
                                    help='metadata path, default '+default_metadata_path)
        parse_services.add_argument('-q', '--quiet',
                                    action='store_true',
                                    help='print only the name, will ignore -j if also supplied')
        parse_services.add_argument('-z',
                                    action='store_true',
                                    help='do not print any output')
        parse_services.set_defaults(func=services.services.main)

        # snapshot
        parse_snapshot = subparsers.add_parser('snapshot',
                                               help='snapshot running container')
        parse_snapshot.add_argument('CONTAINER',
                                    help='specify container to snapshot')
        parse_snapshot.add_argument('--metadata_path', '-m',
                                 default=default_metadata_path,
                                 help='metadata path, default '+default_metadata_path)
        parse_snapshot.add_argument('-z',
                                    action='store_true',
                                    help='do not print any output')
        parse_snapshot.set_defaults(func=snapshot.snapshot.main)

        # snapshots
        parse_snapshots = subparsers.add_parser('snapshots',
                                                help='list snapshots')
        parse_snapshots.add_argument('--metadata_path', '-m',
                                 default=default_metadata_path,
                                 help='metadata path, default '+default_metadata_path)
        parse_snapshots.add_argument('-z',
                                    action='store_true',
                                    help='do not print any output')
        parse_snapshots.set_defaults(func=snapshots.snapshots.main)

        # start
        parse_start = subparsers.add_parser('start',
                                            help='start the api server')
        parse_start.add_argument('--metadata_path', '-m',
                                 default=default_metadata_path,
                                 help='metadata path, default '+default_metadata_path)
        parse_start.add_argument('-z',
                                 action='store_true',
                                 help='do not print any output')
        parse_start.set_defaults(func=start.start.main)

        # stop
        parse_stop = subparsers.add_parser('stop',
                                           help='stop the api server')
        parse_stop.add_argument('--metadata_path', '-m',
                                default=default_metadata_path,
                                help='metadata path, default '+default_metadata_path)
        parse_stop.add_argument('-z',
                                action='store_true',
                                help='do not print any output')
        parse_stop.set_defaults(func=stop.stop.main)

        # unlink
        parse_unlink = subparsers.add_parser('unlink',
                                             help='unlink a service repository host')
        parse_unlink.add_argument('SERVICE_HOST',
                                  help='specify service repository host to disconnect from')
        parse_unlink.add_argument('--metadata_path', '-m',
                                  default=default_metadata_path,
                                  help='metadata path, default '+default_metadata_path)
        parse_unlink.set_defaults(func=unlink.unlink.main)

        # update
        parse_update = subparsers.add_parser('update',
                                             help='update service repository hosts')
        parse_update.add_argument('--metadata_path', '-m',
                                  default=default_metadata_path,
                                  help='metadata path, default '+default_metadata_path)
        parse_update.add_argument('-r' '--repository',
                                  help='specify service repository host to get updates from')
        parse_update.add_argument('-z',
                                  action='store_false',
                                  help='do not print any output')
        parse_update.set_defaults(func=update.update.main)

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
