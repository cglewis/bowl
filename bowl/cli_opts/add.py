"""
This module is the add command of bowl.

Created on 26 May 2014
@author: Charlie Lewis
"""
import ast
import fileinput
import json
import os
import sys

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
                directory_databases = os.path.join(directory_version, "databases")
                if not os.path.exists(directory_databases):
                    os.makedirs(directory_databases)
                directory_docker = os.path.join(directory_databases, "dockerfiles")
                if not os.path.exists(directory_docker):
                    os.makedirs(directory_docker)
                directory_environment = os.path.join(directory_version, "environment")
                if not os.path.exists(directory_environment):
                    os.makedirs(directory_environment)
                directory_docker = os.path.join(directory_environment, "dockerfiles")
                if not os.path.exists(directory_docker):
                    os.makedirs(directory_docker)
                directory_services = os.path.join(directory_version, "services")
                if not os.path.exists(directory_services):
                    os.makedirs(directory_services)
                directory_docker = os.path.join(directory_services, "dockerfiles")
                if not os.path.exists(directory_docker):
                    os.makedirs(directory_docker)
                directory_tools = os.path.join(directory_version, "tools")
                if not os.path.exists(directory_tools):
                    os.makedirs(directory_tools)
                directory_docker = os.path.join(directory_tools, "dockerfiles")
                if not os.path.exists(directory_docker):
                    os.makedirs(directory_docker)
                directory_name = os.path.join(directory_docker, args.NAME)
                if not os.path.exists(directory_name):
                    os.makedirs(directory_name)

                try:
                    if os.path.exists(os.path.join(directory, "oses")):
                        os_name = "\""+args.OS+"\":"
                        if not os_name in open(os.path.join(directory, "oses")).read():
                            num_lines = sum(1 for line in open(os.path.join(directory, "oses")))
                            for line_number, line in enumerate(fileinput.input(os.path.join(directory, "oses"), inplace=1)):
                                try:
                                    if line_number == num_lines-2:
                                        sys.stdout.write(line.rstrip('\n')+",\n")
                                    elif line_number == num_lines-1:
                                        sys.stdout.write("\n")
                                    else:
                                        sys.stdout.write(line)
                                except:
                                    print "Malformed oses file, not enough lines"
                            with open(os.path.join(directory, "oses"), 'a') as f:
                                f.write(" \""+args.OS+"\":\n" +
                                        " {\n" +
                                        "  \"title\": \""+args.OS.capitalize()+"\",\n" +
                                        "  \"type\": \"menu\",\n" +
                                        "  \"subtitle\": \"Please select a version...\",\n" +
                                        "  \"object\": \"os\",\n" +
                                        "  \"options\": []\n" +
                                        " }\n" +
                                        "}")
                    else:
                        with open(os.path.join(directory, "oses"), 'a') as f:
                            f.write("{\n" +
                                    " \""+args.OS+"\":\n" +
                                    " {\n" +
                                    "  \"title\": \""+args.OS.capitalize()+"\",\n" +
                                    "  \"type\": \"menu\",\n" +
                                    "  \"subtitle\": \"Please select a version...\",\n" +
                                    "  \"object\": \"os\",\n" +
                                    "  \"options\": []\n" +
                                    " }\n" +
                                    "}")
                except:
                    print "unable to add operating systems"
                try:
                    directory = os.path.join(directory, args.OS)
                    if os.path.exists(os.path.join(directory, "versions")):
                        version_name = "\""+args.VERSION+"\":"
                        if not version_name in open(os.path.join(directory, "versions")).read():
                            num_lines = sum(1 for line in open(os.path.join(directory, "versions")))
                            for line_number, line in enumerate(fileinput.input(os.path.join(directory, "versions"), inplace=1)):
                                try:
                                    if line_number == num_lines-2:
                                        sys.stdout.write(line.rstrip('\n')+",\n")
                                    elif line_number == num_lines-1:
                                        sys.stdout.write("\n")
                                    else:
                                        sys.stdout.write(line)
                                except:
                                    print "Malformed version file, not enough lines"
                            with open(os.path.join(directory, "versions"), 'a') as f:
                                f.write(" \""+args.VERSION+"\":\n" +
                                        " {\n" +
                                        "  \"title\": \""+args.VERSION.capitalize()+"\",\n" +
                                        "  \"type\": \"menu\",\n" +
                                        "  \"subtitle\": \"Please select services...\",\n" +
                                        "  \"object\": \"version\",\n" +
                                        "  \"options\": []\n" +
                                        " }\n" +
                                        "}")
                    else:
                        with open(os.path.join(directory, "versions"), 'a') as f:
                            f.write("{\n" +
                                    " \""+args.VERSION+"\":\n" +
                                    " {\n" +
                                    "  \"title\": \""+args.VERSION.capitalize()+"\",\n" +
                                    "  \"type\": \"menu\",\n" +
                                    "  \"subtitle\": \"Please select services...\",\n" +
                                    "  \"object\": \"version\",\n" +
                                    "  \"options\": []\n" +
                                    " }\n" +
                                    "}")
                except:
                    print "unable to add versions"
                # !! TODO !!!!!
                if args.TYPE == 'databases':
                    try:
                        if os.path.exists(os.path.join(directory_databases, "databases")):
                            db_name = "\""+args.NAME+"\":"
                            if not db_name in open(os.path.join(directory_databases, "databases")).read():
                                num_lines = sum(1 for line in open(os.path.join(directory_databases, "databases")))
                                for line_number, line in enumerate(fileinput.input(os.path.join(directory_databases, "databases"), inplace=1)):
                                    try:
                                        if line_number == num_lines-2:
                                            sys.stdout.write(line.rstrip('\n')+",\n")
                                        elif line_number == num_lines-1:
                                            sys.stdout.write("\n")
                                        else:
                                            sys.stdout.write(line)
                                    except:
                                        print "Malformed databases file, not enough lines"
                                with open(os.path.join(directory_databases, "databases"), 'a') as f:
                                    # !! TODO edd in args.JSON
                                    f.write(" \""+args.NAME+"\":\n" +
                                            " {\n" +
                                            "  \"title\": \""+args.NAME+"\",\n" +
                                            "  \"type\": \"choice_menu\",\n" +
                                            "  \"command\": \""+args.OS+":"+args.VERSION+":"+args.TYPE+":"+args.NAME+"\",\n" +
                                            "  \"object\": \"database\",\n" +
                                            " }\n" +
                                            "}")
                        else:
                            with open(os.path.join(directory_databases, "databases"), 'a') as f:
                                # !! TODO edd in args.JSON
                                f.write("{\n" +
                                        " \""+args.NAME+"\":\n" +
                                        " {\n" +
                                        "  \"title\": \""+args.NAME+"\",\n" +
                                        "  \"type\": \"choice_menu\",\n" +
                                        "  \"command\": \""+args.OS+":"+args.VERSION+":"+args.TYPE+":"+args.NAME+"\",\n" +
                                        "  \"object\": \"database\",\n" +
                                        " }\n" +
                                        "}")
                    except:
                        print "unable to add databases"
                else:
                    try:
                        if not os.path.exists(os.path.join(directory_databases, "databases")):
                            with open(os.path.join(directory_databases, "databases"), 'w') as f:
                                f.write("{\n}")
                    except:
                        pass
                # !! TODO !!!!!
                if args.TYPE == 'environment':
                    try:
                        if os.path.exists(os.path.join(directory_environment, "environment")):
                            env_name = "\""+args.NAME+"\":"
                            if not env_name in open(os.path.join(directory_environment, "environment")).read():
                                num_lines = sum(1 for line in open(os.path.join(directory_environemnt, "environemnt")))
                                for line_number, line in enumerate(fileinput.input(os.path.join(directory_environment, "environment"), inplace=1)):
                                    try:
                                        if line_number == num_lines-2:
                                            sys.stdout.write(line.rstrip('\n')+",\n")
                                        elif line_number == num_lines-1:
                                            sys.stdout.write("\n")
                                        else:
                                            sys.stdout.write(line)
                                    except:
                                        print "Malformed environment file, not enough lines"
                                with open(os.path.join(directory_environment, "environment"), 'a') as f:
                                    # !! TODO edd in args.JSON
                                    f.write(" \""+args.NAME+"\":\n" +
                                            " {\n" +
                                            "  \"title\": \""+args.NAME+"\",\n" +
                                            "  \"type\": \"choice_menu\",\n" +
                                            "  \"command\": \""+args.OS+":"+args.VERSION+":"+args.TYPE+":"+args.NAME+"\",\n" +
                                            "  \"object\": \"environment\",\n" +
                                            " }\n" +
                                            "}")
                        else:
                            with open(os.path.join(directory_environment, "environment"), 'a') as f:
                                # !! TODO edd in args.JSON
                                f.write("{\n" +
                                        " \""+args.NAME+"\":\n" +
                                        " {\n" +
                                        "  \"title\": \""+args.NAME+"\",\n" +
                                        "  \"type\": \"choice_menu\",\n" +
                                        "  \"command\": \""+args.OS+":"+args.VERSION+":"+args.TYPE+":"+args.NAME+"\",\n" +
                                        "  \"object\": \"environment\",\n" +
                                        " }\n" +
                                        "}")
                    except:
                        print "unable to add environment"
                else:
                    try:
                        if not os.path.exists(os.path.join(directory_environment, "environment")):
                            with open(os.path.join(directory_environment, "environment"), 'w') as f:
                                f.write("{\n}")
                    except:
                        pass
                # !! TODO !!!!!
                if args.TYPE == 'services':
                    try:
                        if os.path.exists(os.path.join(directory_services, "services")):
                            service_name = "\""+args.NAME+"\":"
                            if not service_name in open(os.path.join(directory_services, "services")).read():
                                num_lines = sum(1 for line in open(os.path.join(directory_services, "services")))
                                for line_number, line in enumerate(fileinput.input(os.path.join(directory_services, "services"), inplace=1)):
                                    try:
                                        if line_number == num_lines-2:
                                            sys.stdout.write(line.rstrip('\n')+",\n")
                                        elif line_number == num_lines-1:
                                            sys.stdout.write("\n")
                                        else:
                                            sys.stdout.write(line)
                                    except:
                                        print "Malformed services file, not enough lines"
                                with open(os.path.join(directory_services, "services"), 'a') as f:
                                    # !! TODO edd in args.JSON
                                    f.write(" \""+args.NAME+"\":\n" +
                                            " {\n" +
                                            "  \"title\": \""+args.NAME+"\",\n" +
                                            "  \"type\": \"choice_menu\",\n" +
                                            "  \"command\": \""+args.OS+":"+args.VERSION+":"+args.TYPE+":"+args.NAME+"\",\n" +
                                            "  \"object\": \"services\",\n" +
                                            " }\n" +
                                            "}")
                        else:
                            with open(os.path.join(directory_services, "services"), 'a') as f:
                                # !! TODO edd in args.JSON
                                f.write("{\n" +
                                        " \""+args.NAME+"\":\n" +
                                        " {\n" +
                                        "  \"title\": \""+args.NAME+"\",\n" +
                                        "  \"type\": \"choice_menu\",\n" +
                                        "  \"command\": \""+args.OS+":"+args.VERSION+":"+args.TYPE+":"+args.NAME+"\",\n" +
                                        "  \"object\": \"services\",\n" +
                                        " }\n" +
                                        "}")
                    except:
                        print "unable to add services"
                else:
                    try:
                        if not os.path.exists(os.path.join(directory_services, "services")):
                            with open(os.path.join(directory_services, "services"), 'w') as f:
                                f.write("{\n}")
                    except:
                        pass
                # !! TODO !!!!!
                if args.TYPE == 'tools':
                    try:
                        if os.path.exists(os.path.join(directory_tools, "tools")):
                            tool_name = "\""+args.NAME+"\":"
                            if not tool_name in open(os.path.join(directory_tools, "tools")).read():
                                num_lines = sum(1 for line in open(os.path.join(directory_tools, "tools")))
                                for line_number, line in enumerate(fileinput.input(os.path.join(directory_tools, "tools"), inplace=1)):
                                    try:
                                        if line_number == num_lines-2:
                                            sys.stdout.write(line.rstrip('\n')+",\n")
                                        elif line_number == num_lines-1:
                                            sys.stdout.write("\n")
                                        else:
                                            sys.stdout.write(line)
                                    except:
                                        print "Malformed tools file, not enough lines"
                                with open(os.path.join(directory_tools, "tools"), 'a') as f:
                                    # !! TODO edd in args.JSON
                                    f.write(" \""+args.NAME+"\":\n" +
                                            " {\n" +
                                            "  \"title\": \""+args.NAME+"\",\n" +
                                            "  \"type\": \"choice_menu\",\n" +
                                            "  \"command\": \""+args.OS+":"+args.VERSION+":"+args.TYPE+":"+args.NAME+"\",\n" +
                                            "  \"object\": \"tools\",\n" +
                                            " }\n" +
                                            "}")
                        else:
                            with open(os.path.join(directory_tools, "tools"), 'a') as f:
                                # !! TODO edd in args.JSON
                                f.write("{\n" +
                                        " \""+args.NAME+"\":\n" +
                                        " {\n" +
                                        "  \"title\": \""+args.NAME+"\",\n" +
                                        "  \"type\": \"choice_menu\",\n" +
                                        "  \"command\": \""+args.OS+":"+args.VERSION+":"+args.TYPE+":"+args.NAME+"\",\n" +
                                        "  \"object\": \"tools\",\n" +
                                        " }\n" +
                                        "}")
                    except:
                        print "unable to add tools"
                else:
                    try:
                        if not os.path.exists(os.path.join(directory_tools, "tools")):
                            with open(os.path.join(directory_tools, "tools"), 'w') as f:
                                f.write("{\n}")
                    except:
                        pass
            else:
                print "unable to link localhost as a repository"

        # !! TODO
        # check JSON for path
        # check JSON for "" of key/values
        # check JSON for '' of key/values
        # check JSON for no quoting of key/values
        # check all necessary fields in JSON are there
        #       cluster
        #       combine_cmd
        #       background_cmd
        #       tty
        #       interactive
        # check JSON dependencies like background_cmd only if combine_cmd is true, etc.

        # !! TODO
        # get DOckerfile at path, but also everything in the context of that directory

        # !! TODO
        # add to new container directory (not .default)
        # ask the user if they would like to use .default for default services
        # ask the user if they would like remove .default from their services

        # !! TODO
        #DONE# mkdir ~/.bowl/services
        # contains a file that says what all of the service directories are
        #    most likely .default and/or ~/.bowl/services/
        # contains added services, unless specified to be somewhere else

        # !! TODO
        # add service to another repository ...

        # !! TODO
        print args
