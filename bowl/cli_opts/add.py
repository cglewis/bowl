"""
This module is the add command of bowl.

Created on 26 May 2014
@author: Charlie Lewis
"""
import ast
import os

from bowl.cli_opts import link

class Object(object):
    pass

class add(object):
    """
    This class is responsible for the add command of the cli.
    """
    @classmethod
    def main(self, args):
        if args.repository:
            # !! TODO connect to api of repository
            print args.repository
            print "TODO"
        else:
            link_args = Object()
            link_args.z = True
            link_args.metadata_path = args.metadata_path
            link_args.SERVICE_HOST = "localhost"
            if link.link.main(link_args):
                directory = os.path.join(args.metadata_path, "services")
                directory = os.path.expanduser(directory)
                if not os.path.exists(directory):
                    os.makedirs(directory)
                directory_os = os.path.join(directory, args.OS)
                if not os.path.exists(directory_os):
                    os.makedirs(directory_os)
                directory_version = os.path.join(directory_os, args.VERSION)
                if not os.path.exists(directory_version):
                    os.makedirs(directory_version)
                directory_type = os.path.join(directory_version, args.TYPE)
                if not os.path.exists(directory_type):
                    os.makedirs(directory_type)
                directory_docker = os.path.join(directory_type, "dockerfiles")
                if not os.path.exists(directory_docker):
                    os.makedirs(directory_docker)
                directory_name = os.path.join(directory_docker, args.NAME)
                if not os.path.exists(directory_name):
                    os.makedirs(directory_name)

                # !! TODO !!!!!
                try:
                    with open(os.path.join(directory, "services"), 'a') as f:
                        f.write("{" +
                                "'title': 'localhost'," +
                                " 'type': 'choice_menu'" +
                                "}\n")
                except:
                    print "unable to add service"
            else:
                print "unable to link localhost as a repository"

        # !! TODO
        # check JSON for path
        # check JSON for "" of key/values
        # check JSON for '' of key/values
        # check JSON for no quoting of key/values
        # check all necessary fields in JSON are there
        # check JSON dependencies like background_cmd only if combine_cmd is true, etc.

        # !! TODO
        # get DOckerfile at path, but also everything in the context of that directory

        # !! TODO
        # add to new container directory (not .default)
        # ask the user if they would like to use .default for default services
        # ask the user if they would like remove .default from their services

        # !! TODO
        # mkdir ~/.bowl/services
        # contains a file that says what all of the service directories are
        #    most likely .default and/or ~/.bowl/services/
        # contains added services, unless specified to be somewhere else

        # !! TODO
        # add service to another repository ...

        # !! TODO
        print args
