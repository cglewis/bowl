"""
This module is the new command of bowl.

Created on 15 March 2014
@author: Charlie Lewis
"""

import ast
import curses
import docker
import importlib
import inspect
import os
import shutil
import sys
import uuid
from bowl.containers import oses

class new(object):
    """
    This class is responsible for the new command of the cli.
    """
    @staticmethod
    def build_dockerfile(self, dockerfile, uuid_dir):
        # try/catch
        with open('/tmp/'+uuid_dir+'/Dockerfile', 'w') as f:
            for line in dockerfile:
                f.write(line+'\n')

        image_tag = 'bowl-'+uuid_dir

        for index, host in enumerate(self.hosts):
            # !! TODO try/except - verify that hosts specified can be reached
            c = docker.Client(base_url='tcp://'+host['title']+':2375', version='1.9',
                              timeout=2)

            # !! TODO check that the build actually created an image before trying to create the container
            c.build(tag="bowl-"+uuid_dir, quiet=False, path='/tmp/'+uuid_dir,
                    nocache=False, rm=False, stream=False)

            # TODO check if tty and stdin_open (interactive) are needed
            if len(self.names) != 0:
                if self.unique:
                    container = c.create_container(image_tag, tty=True, stdin_open=True, name=self.names[index], hostname=self.names[index])
                else:
                    container = c.create_container(image_tag, tty=True, stdin_open=True, name=self.names[0], hostname=self.names[0])
            else:
                container = c.create_container(image_tag, tty=True, stdin_open=True)
            c.start(container, publish_all_ports=True)

        shutil.rmtree('/tmp/'+uuid_dir)
        return

    @staticmethod
    def build_options(self):
        menu_dict = {
         'title': "Build your bowl",
         'type': "menu",
         'subtitle': "Please select a choice...",
         'options': [
          {
           'title': "Build Container",
           'type': "menu",
           'subtitle': "Please select an Operating System...",
           'options': []
          },
          {
           'title': "Choose Image",
           'type': "menu",
           'subtitle': "Please select an Image...",
           'options': []
          }
         ]
        }
        os_dict = {}
        base = "bowl.containers."
        os_list = inspect.getmembers(oses.oses, predicate=inspect.ismethod)
        for item in os_list:
            package = base + item[0]
            os_dict[item[0]+'_versions'] = getattr(__import__(package,
                                                              fromlist=['versions']),
                                                              'versions')
            menu_dict['options'][0]['options'].append(getattr(oses.oses(), item[0])())

        try:
            directory = "~/.bowl"
            directory = os.path.expanduser(directory)
            with open(os.path.join(directory, "images"), 'r') as f:
                for line in f:
                    menu_dict['options'][1]['options'].append(ast.literal_eval(line.rstrip('\n')))
        except:
            pass

        launch_dict = {
          'title': "Launch Container",
          'type': "launch"
        }
        launch_image_dict = {
          'title': "Launch Image(s)",
          'type': "launch"
        }

        os_num = 0
        for key,os_inst in os_dict.iteritems():
            version_list = inspect.getmembers(os_inst.versions,
                                              predicate=inspect.ismethod)
            version_num = 0
            for version in version_list:
                menu_dict['options'][0]['options'][os_num]['options'].append(getattr(os_inst.versions(), version[0])())

                database_dict = {
                  'title': "Databases",
                  'type': "menu",
                  'subtitle': "Please select databases...",
                  'options': []
                }
                os_name = key.split("_", 1)
                package = base + os_name[0] + "." + version[0] + "."

                db_package = package + "databases"
                importlib.import_module(db_package)
                db_inst = getattr(__import__(db_package, fromlist=['databases']), 'databases')
                database_list = inspect.getmembers(db_inst.databases, predicate=inspect.ismethod)
                for database in database_list:
                    self.combine_cmd_dict[package+database[0]] = getattr(db_inst.databases(), database[0])()['combine_cmd']
                    if self.combine_cmd_dict[package+database[0]] == "yes":
                        self.background_cmd_dict[package+database[0]] = getattr(db_inst.databases(), database[0])()['background_cmd']
                    database_dict['options'].append(getattr(db_inst.databases(), database[0])())

                environment_dict = {
                  'title': "Environment Tools",
                  'type': "menu",
                  'subtitle': "Please select environment tools...",
                  'options': []
                }
                env_package = package + "environment"
                importlib.import_module(env_package)
                env_inst = getattr(__import__(env_package, fromlist=['environment']), 'environment')
                environment_list = inspect.getmembers(env_inst.environment, predicate=inspect.ismethod)
                for environ in environment_list:
                    self.combine_cmd_dict[package+environ[0]] = getattr(env_inst.environment(), environ[0])()['combine_cmd']
                    if self.combine_cmd_dict[package+environ[0]] == "yes":
                        self.background_cmd_dict[package+environ[0]] = getattr(env_inst.environment(), environ[0])()['background_cmd']
                    environment_dict['options'].append(getattr(env_inst.environment(), environ[0])())

                service_dict = {
                  'title': "Services",
                  'type': "menu",
                  'subtitle': "Please select services...",
                  'options': []
                }
                serv_package = package + "services"
                importlib.import_module(serv_package)
                serv_inst = getattr(__import__(serv_package, fromlist=['services']), 'services')
                service_list = inspect.getmembers(serv_inst.services, predicate=inspect.ismethod)
                for service in service_list:
                    self.combine_cmd_dict[package+service[0]] = getattr(serv_inst.services(), service[0])()['combine_cmd']
                    if self.combine_cmd_dict[package+service[0]] == "yes":
                        self.background_cmd_dict[package+service[0]] = getattr(serv_inst.services(), service[0])()['background_cmd']
                    service_dict['options'].append(getattr(serv_inst.services(), service[0])())

                tool_dict = {
                  'title': "Tools",
                  'type': "menu",
                  'subtitle': "Please select tools...",
                  'options': []
                }
                tool_package = package + "tools"
                importlib.import_module(tool_package)
                tool_inst = getattr(__import__(tool_package, fromlist=['tools']), 'tools')
                tool_list = inspect.getmembers(tool_inst.tools, predicate=inspect.ismethod)
                for tool in tool_list:
                    self.combine_cmd_dict[package+tool[0]] = getattr(tool_inst.tools(), tool[0])()['combine_cmd']
                    if self.combine_cmd_dict[package+tool[0]] == "yes":
                        self.background_cmd_dict[package+tool[0]] = getattr(tool_inst.tools(), tool[0])()['background_cmd']
                    tool_dict['options'].append(getattr(tool_inst.tools(), tool[0])())

                host_dict = {
                  'title': "Docker Hosts",
                  'type': "menu",
                  'subtitle': "Please select which hosts are available to use for containers...",
                  'options': []
                }
                try:
                    directory = "~/.bowl"
                    directory = os.path.expanduser(directory)
                    with open(os.path.join(directory, "hosts"), 'r') as f:
                        for line in f:
                            host_dict['options'].append(ast.literal_eval(line.rstrip('\n')))
                except:
                    pass

                menu_dict['options'][0]['options'][os_num]['options'][version_num]['options'].append(database_dict)
                menu_dict['options'][0]['options'][os_num]['options'][version_num]['options'].append(environment_dict)
                menu_dict['options'][0]['options'][os_num]['options'][version_num]['options'].append(service_dict)
                menu_dict['options'][0]['options'][os_num]['options'][version_num]['options'].append(tool_dict)
                menu_dict['options'][0]['options'][os_num]['options'][version_num]['options'].append(host_dict)
                menu_dict['options'][0]['options'][os_num]['options'][version_num]['options'].append(launch_dict)
                version_num += 1
            os_num += 1

        menu_dict['options'][1]['options'].append(launch_image_dict)
        return menu_dict

    @staticmethod
    def query_yes_no(self, question, default="no"):
        """Ask a yes/no question via raw_input() and return their answer.

        "question" is a string that is presented to the user.
        "default" is the presumed answer if the user just hits <Enter>.
            It must be "no" (the default), "yes" or None (meaning
            an answer is required of the user).

        The "answer" return value is one of "yes" or "no".
        """
        valid = {"yes":True, "y":True, "ye":True,
                 "no":False, "n":False}
        if default == None:
            prompt = " [y/n] "
        elif default == "yes":
            prompt = " [Y/n] "
        elif default == "no":
            prompt = " [y/N] "
        else:
            raise ValueError("invalid default answer: '%s'" % default)

        while True:
            sys.stdout.write(question + prompt)
            choice = raw_input().lower()
            if default is not None and choice == '':
                return valid[default]
            elif choice in valid:
                return valid[choice]
            else:
                sys.stdout.write("Please respond with 'yes' or 'no' "\
                                 "(or 'y' or 'n').\n")

    @classmethod
    def main(self, args):
        # !! TODO this should be in __init__
        # build dictionary of available container options
        self.combine_cmd_dict = {}
        self.background_cmd_dict = {}
        menu_dict = self.build_options(self)

        self.win = curses.initscr()
        self.win.keypad(1)
        self.build_dict = {}
        self.build_dict['services'] = []
        self.hosts = []
        self.launch = False
        self.exit = False
        self.image = False
        self.default = True
        self.user = False
        self.name = False
        self.names = []
        self.unique = False
        self.cmd = False
        self.entrypoint = False
        self.port = False
        self.link = False
        self.volume = False

        # init curses stuff
        curses.noecho()
        curses.cbreak()
        curses.start_color()
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

        self.menus_dict = {}
        # !! TODO cleanup
        build_dict = self.build_dict
        build_dict = self.process_menu(self, menu_dict, build_dict)
        self.build_dict = build_dict
        curses.endwin()

        if self.launch:
            self.default = self.query_yes_no(self, "Use default runtime settings?", default="yes")


        # !! TODO fix this!!!
        if not self.default:
            # init curses stuff
            curses.noecho()
            curses.cbreak()
            curses.start_color()
            curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

            # !! TODO only have the option for asking about different parameters if more than one host was selected
            #         if so, loop through the questions for each container/host
            # !! TODO loop through X number of volumes they would like to add
            # !! TODO loop through X number of ports in the dockerfile they would like to modify
            # !! TODO loop through X number of containers they would like to link to
            # !! TODO loop through X number of accounts they would like to add to teh container
            # !! TODO if image a user can't be added
            #                  also introspection of ports/volumes might be hard
            options_dict = {
             'title': "Runtime options",
             'type': "menu",
             'subtitle': "Please select the runtime options you would like to change...",
             'options': [
              {
               'title': "Do you want to override the CMD of the container?",
               'type': "choice_menu",
               'options': [
                {
                 'config':'cmd'
                }
               ]
              },
              {
               'title': "Do you want to override the ENTRYPOINT of the container?",
               'type': "choice_menu",
               'options': [
                {
                 'config':'entrypoint'
                }
               ]
              },
              {
               'title': "Do you want to attach a volume to this container?",
               'type': "choice_menu",
               'options': [
                {
                 'config':'volume'
                }
               ]
              },
              {
               'title': "Do you want to specify how a port should be exposed?",
               'type': "choice_menu",
               'options': [
                {
                 'config':'port'
                }
               ]
              },
              {
               'title': "Do you want to link this container to another container?",
               'type': "choice_menu",
               'options': [
                {
                 'config':'link'
                }
               ]
              },
              {
               'title': "Do you want to name this container?",
               'type': "choice_menu",
               'options': [
                {
                 'config':'name'
                }
               ]
              },
              {
               'title': "Do you want an account on this container?",
               'type': "choice_menu",
               'options': [
                {
                 'config':'user'
                }
               ]
              }
             ]
            }

            if len(self.hosts) > 1:
                options_dict['options'].append(
                 {
                  'title': "Should the containers use different parameters?",
                  'type': "choice_menu",
                  'options': [
                   {
                    'config':'unique'
                   }
                  ]
                 })

            # !! TODO cleanup
            self.config_dict = {}
            self.config_dict['services'] = []
            config_dict = self.config_dict
            config_dict = self.options_menu(self, options_dict, config_dict)
            self.config_dict = config_dict
            curses.endwin()

        if self.name:
            if self.unique:
                for host in self.hosts:
                    # !! TODO try/except - verify that hosts specified can be reached
                    c = docker.Client(base_url='tcp://'+host['title']+':2375', version='1.9',
                                      timeout=2)
                    name = raw_input("Enter container name for container running on "+host['title']+":")
                    self.names.append(name)
            else:
                # !! TODO validate
                name = raw_input("Enter container name: ")
                self.names.append(name)
            print self.names
        if self.link:
            # !! TODO only list containers for each host of which the container is going to be spun up on
            #         can't link to a container that is not running on the same docker host
            containers = []

            if self.unique:
                for host in self.hosts:
                    # !! TODO try/except - verify that hosts specified can be reached
                    c = docker.Client(base_url='tcp://'+host['title']+':2375', version='1.9',
                                      timeout=2)
                    containers = c.containers()
                    if len(containers) == 0:
                        print "There are no running containers on the host "+host['title']+" to link to."
                        junk = raw_input("Press enter to continue...")
                    else:
                        # init curses stuff
                        curses.noecho()
                        curses.cbreak()
                        curses.start_color()
                        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

                        options_dict = {
                         'title': "Containers to Link",
                         'type': "menu",
                         'subtitle': "Please select the containers you would like to link on host "+host['title']+"...",
                         'options': [
                         ]
                        }
                        for container in containers:
                            container_name = ""
                            names = container['Names']
                            for n in names:
                                container_name += n[1:] + " - "
                            container_id = container['Id']
                            container_name += container_id
                            options_dict['options'].append(
                                 {
                                  'title': '"'+container_name+'"',
                                  'type': "choice_menu",
                                  'options': [
                                   {
                                    'link':'"'+container_id+'"'
                                   }
                                  ]
                                 }
                                )

                        # !! TODO cleanup
                        self.config_dict = {}
                        self.config_dict['services'] = []
                        config_dict = self.config_dict
                        config_dict = self.options_menu(self, options_dict, config_dict)
                        self.config_dict = config_dict
                        curses.endwin()
            else:
                for host in self.hosts:
                    # !! TODO try/except - verify that hosts specified can be reached
                    c = docker.Client(base_url='tcp://'+host['title']+':2375', version='1.9',
                                      timeout=2)
                    containers.append(c.containers())
                    print containers


                if len(containers) == 0:
                    print "There are no running containers on the host to link to."
                    junk = raw_input("Press enter to continue...")
                else:
                    # !! TODO remove containers that are not on all hosts

                    # init curses stuff
                    curses.noecho()
                    curses.cbreak()
                    curses.start_color()
                    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

                    options_dict = {
                     'title': "Containers to Link",
                     'type': "menu",
                     'subtitle': "Please select the containers you would like to link...",
                     'options': [
                     ]
                    }
                    for host in containers:
                        for container in host:
                            container_name = ""
                            names = container['Names']
                            for n in names:
                                container_name += n[1:] + " - "
                            container_id = container['Id']
                            container_name += container_id
                            options_dict['options'].append(
                                 {
                                  'title': '"'+container_name+'"',
                                  'type': "choice_menu",
                                  'options': [
                                   {
                                    'link':'"'+container_id+'"'
                                   }
                                  ]
                                 }
                                )

                    # !! TODO cleanup
                    self.config_dict = {}
                    self.config_dict['services'] = []
                    config_dict = self.config_dict
                    config_dict = self.options_menu(self, options_dict, config_dict)
                    self.config_dict = config_dict
                    curses.endwin()

            print self.link
        if self.port:
            # !! TODO present available exposed ports, and allow each to be assigned specifically
            print self.port
        if self.volume:
            # !! TODO allow n number of runtime volumes (check if needs to be in dockerfile?)
            volumes = []
            no = True
            while no:
                volume = raw_input("Enter a volume (path:path): ")
                # !! TODO validate input
                volumes.append(volume)
                no = self.query_yes_no(self, "Would you like to add another volume?", default="no")
            print self.volume
            print volumes
        if self.entrypoint:
            # !! TODO allow entrypoint to be overridden
            entrypoint = raw_input("Enter new runtime ENTRYPOINT: ")
            print entrypoint
        if self.cmd:
            # !! TODO allow cmd to be overridden
            cmd = raw_input("Enter new runtime CMD: ")
            print cmd

        # !! TODO move out questions
        if self.image:
            for index, image_info in enumerate(self.build_dict['services']):
                image_tag, image_host = image_info.split(",", 1)
                # !! TODO try/except - verify that hosts specified can be reached
                c = docker.Client(base_url='tcp://'+image_host+':2375', version='1.9',
                                  timeout=2)

                cmd = raw_input("Enter command you wish to use for "+image_tag+": ")
                # TODO check if tty and stdin_open (interactive) are needed
                if len(self.names) != 0:
                    if self.unique:
                        container = c.create_container(image_tag, command=cmd, tty=True, stdin_open=True, name=self.names[index], hostname=self.names[index])
                    else:
                        container = c.create_container(image_tag, command=cmd, tty=True, stdin_open=True, name=self.names[0], hostname=self.names[0])
                else:
                    container = c.create_container(image_tag, command=cmd, tty=True, stdin_open=True)
                c.start(container, publish_all_ports=True)

        if self.launch and not self.image:
            if self.user:
                username = raw_input("Enter username: ")
                ssh_pubkey = raw_input("Enter path to ssh public key: ")

            # !! TODO use this to build the dockerfile
            # !! TODO if no services were selected, don't create a container
            # !! TODO if contains an ADD line, be sure and copy additional files
            this_dir, this_filename = os.path.split(__file__)
            services = self.build_dict['services']
            print "The following services have been selected and will be packaged up into a container: "
            # !! TODO parse this out by os/version/type/service
            print services
            dockerfile = []
            num_services = len(services)
            envs = {}
            workdirs = {}
            entrypoints = {}
            cmds = {}
            for service in sorted(services):
                envs[service] = []
                workdirs[service] = []
                entrypoints[service] = []
                cmds[service] = []

                entrypoint = "/bin/sh -c"
                cmd = ""
                # !! error check that the array is this size
                service_name = service.split(':', 3)
                os_flavor = "/".join(service_name[0:3])
                path = os.path.join(os.path.dirname(this_dir),
                                    "containers/"+os_flavor+"/dockerfiles/"+service_name[3]+"/Dockerfile")
                with open(path, 'r') as f:
                    for line in f:
                        # remove duplicate lines
                        if line.rstrip('\n'	) not in dockerfile:
                            # combine EXPOSE commands
                            if line.startswith("EXPOSE"):
                                if any(cmd.startswith("EXPOSE") for cmd in dockerfile):
                                    line = ' '.join(line.rstrip('\n').split(' ', 1)[1:])
                                    # !! TODO make sure this is what the command starts with
                                    # !! TODO display a warning to the user if there is overlapping ports
                                    matching = [s for s in dockerfile if "EXPOSE" in s]
                                    matching.append(line)
                                    dockerfile.remove(matching[0])
                                    dockerfile.append(' '.join(matching))
                                else:
                                    dockerfile.append(line.rstrip('\n'))
                            elif line.startswith("ADD") or line.startswith("COPY"):
                                # !! TODO
                                # copy context directory to tmp directory for building
                                dockerfile.append(line.rstrip('\n'))
                            # check for multiple USER commands
                            elif line.startswith("USER"):
                                # !! TODO
                                if num_services == 1:
                                    dockerfile.append(line.rstrip('\n'))
                                else:
                                    if self.combine_cmd_dict["bowl.containers." +
                                                             service_name[0] +
                                                             "." +
                                                             service_name[1] +
                                                             "." +
                                                             service_name[3]] == "yes":
                                        envs[service].append(line.rstrip('\n'))
                                    # !! TODO
                                    dockerfile.append(line.rstrip('\n'))
                            elif line.startswith("ENV"):
                                # !! TODO
                                if num_services == 1:
                                    dockerfile.append(line.rstrip('\n'))
                                else:
                                    if self.combine_cmd_dict["bowl.containers." +
                                                             service_name[0] +
                                                             "." +
                                                             service_name[1] +
                                                             "." +
                                                             service_name[3]] == "yes":
                                        envs[service].append(line.rstrip('\n'))
                                    # !! TODO
                                    dockerfile.append(line.rstrip('\n'))
                            # check for multiple WORKDIR commands
                            elif line.startswith("WORKDIR"):
                                # !! TODO
                                if num_services == 1:
                                    dockerfile.append(line.rstrip('\n'))
                                else:
                                    if self.combine_cmd_dict["bowl.containers." +
                                                             service_name[0] +
                                                             "." +
                                                             service_name[1] +
                                                             "." +
                                                             service_name[3]] == "yes":
                                        workdirs[service].append(line.rstrip('\n'))
                                    # !! TODO
                                    dockerfile.append(line.rstrip('\n'))
                            # check for multiple ENTRYPOINT commands
                            elif line.startswith("ENTRYPOINT"):
                                # !! TODO
                                # check WORKDIR since CMD and ENTRYPOINT are modified
                                # use the ENTRYPOINT that corresponds with the chosen CMD
                                if num_services == 1:
                                    dockerfile.append(line.rstrip('\n'))
                                else:
                                    if self.combine_cmd_dict["bowl.containers." +
                                                             service_name[0] +
                                                             "." +
                                                             service_name[1] +
                                                             "." +
                                                             service_name[3]] == "yes":
                                        entrypoints[service].append(line.rstrip('\n'))
                                entrypoint = (line.rstrip('\n')).split(" ", 1)[1:][0]
                            # check for multiple CMD commands
                            elif line.startswith("CMD"):
                                # !! TODO
                                # check WORKDIR since CMD and ENTRYPOINT are modified
                                if num_services == 1:
                                    dockerfile.append(line.rstrip('\n'))
                                else:
                                    if self.combine_cmd_dict["bowl.containers." +
                                                             service_name[0] +
                                                             "." +
                                                             service_name[1] +
                                                             "." +
                                                             service_name[3]] == "yes":
                                        # !! TODO only append if there is only one
                                        # if more than one, use supervisord or something
                                        # if none of them are combine_cmds then use /bin/bash
                                        cmds[service].append(self.background_cmd_dict["bowl.containers." +
                                                             service_name[0] +
                                                             "." +
                                                             service_name[1] +
                                                             "." +
                                                             service_name[3]])
                                        #cmds[service].append(line.rstrip('\n'))
                                        #dockerfile.append(line.rstrip('\n'))
                                cmd = (line.rstrip('\n')).split(" ", 1)[1:][0]
                            else:
                                dockerfile.append(line.rstrip('\n'))

            uuid_dir = str(uuid.uuid4())
            # !! TODO try/except
            os.mkdir('/tmp/'+uuid_dir)

            # if more than one service with combine_cmd, use supervisord
            if len(cmds) > 1:
                print "\nFound more than one service that runs a command, installing supervisord..."
                dockerfile.append("RUN apt-get install -y supervisor")
                print cmds
                # !! TODO

            if self.user:
                try:
                    # !! TODO try/except
                    with open(os.path.expanduser(ssh_pubkey), 'r') as fi:
                        with open("/tmp/"+uuid_dir+"/authorized_keys", 'w') as fo:
                            for line in fi:
                                fo.write(line)
                    dockerfile.append("RUN useradd "+username)
                    dockerfile.append("RUN mkdir -p /home/"+username+
                                      "/.ssh; chown "+username+
                                      " /home/"+username+
                                      "/.ssh; chmod 700 /home/"+username+"/.ssh")
                    dockerfile.append("ADD authorized_keys /home/"+username+"/.ssh/authorized_keys")
                    # !! TODO ask if user needs sudo
                    dockerfile.append("RUN apt-get install -y sudo")
                    dockerfile.append('RUN echo "'+username+
                                      ' ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers')
                    # !! TODO ask if more than one user
                except:
                    print "SSH Key file not found, failed to create user"
            if "CMD" not in dockerfile:
                dockerfile.append("CMD /bin/bash")
            print "\n### GENERATED DOCKERFILE ###"
            for line in dockerfile:
                print line
            print "### END GENERATED DOCKERFILE ###\n"
            self.build_dockerfile(self, dockerfile, uuid_dir)

    @staticmethod
    def display_menu(self, menu, parent, build_dict):
        option_size = len(menu['options'])
        hash_menu = hash(str(menu))
        choice = []
        if hash_menu in self.menus_dict:
            choice = self.menus_dict[hash_menu]
        else:
            choice = [" "]*(option_size+1)
            self.menus_dict[hash_menu] = choice

        if parent is None:
            back = "Exit"
        else:
            back = "Return to %s menu" % parent['title']

        position = 0
        key = None
        highlighted = curses.color_pair(1)
        normal = curses.A_NORMAL
        while key != ord('\n'):
            self.win.clear()
            self.win.border(0)
            self.win.addstr(2,2, menu['title'], curses.A_STANDOUT)
            self.win.addstr(4,2, menu['subtitle'], curses.A_BOLD)

            for index in range(option_size):
                textstyle = normal
                if position == index:
                    textstyle = highlighted
                if menu['options'][index]['title'] == "Docker Hosts":
                    self.win.addstr(index+6, 4, "%d - %s" % (index+1, menu['options'][index]['title']), textstyle)
                elif menu['options'][index]['type'] == "choice_menu":
                    self.win.addstr(index+5, 4, "%d - [%s] %s" % (index+1, choice[index], menu['options'][index]['title']), textstyle)
                elif menu['options'][index]['type'] == "launch":
                    self.win.addstr(index+6, 4, "%d - %s" % (index+1, menu['options'][index]['title']), textstyle)
                else:
                    self.win.addstr(index+5, 4, "%d - %s" % (index+1, menu['options'][index]['title']), textstyle)
            textstyle = normal
            if position == option_size:
                textstyle = highlighted
            if back != "Exit":
                if "object" in parent and parent['object'] == "os":
                    if len(build_dict['services']) > 0:
                        back = "Exit"
                else:
                    back = "Return to %s menu" % parent['title']

            self.win.addstr(option_size+6, 4, "%d - %s" % (option_size+1, back), textstyle)
            self.win.refresh()

            key = self.win.getch()
            try:
                if key >= ord('1') and key <= ord(str(option_size+1)):
                    position = key - ord('0') - 1
                elif key == 258:
                    if position < option_size:
                        position += 1
                    else:
                        position = 0
                elif key == 259:
                    if position > 0:
                        position -= 1
                    else:
                        position = option_size
                # !! TODO error check this!!
                elif key == 32 and menu['options'][position]['type'] == "choice_menu":
                    if choice[position] == " ":
                        choice[position] = "x"
                        if "command" in menu['options'][position]:
                            # add to build_dict
                            build_dict['services'].append(menu['options'][position]['command'])
                        else:
                            # add to docker hosts
                            if self.default:
                                self.hosts.append(menu['options'][position])
                            else:
                                if "options" in menu['options'][position]:
                                    if "config" in menu['options'][position]['options'][0]:
                                        if "unique" == menu['options'][position]['options'][0]['config']:
                                            self.unique = True
                                        if "cmd" == menu['options'][position]['options'][0]['config']:
                                            self.cmd = True
                                        if "entrypoint" == menu['options'][position]['options'][0]['config']:
                                            self.entrypoint = True
                                        if "volume" == menu['options'][position]['options'][0]['config']:
                                            self.volume = True
                                        if "port" == menu['options'][position]['options'][0]['config']:
                                            self.port = True
                                        if "link" == menu['options'][position]['options'][0]['config']:
                                            self.link = True
                                        if "name" == menu['options'][position]['options'][0]['config']:
                                            self.name = True
                                        if "user" == menu['options'][position]['options'][0]['config']:
                                            self.user = True
                    else:
                        choice[position] = " "
                        if "command" in menu['options'][position]:
                            # remove from build_dict
                            # TODO check if exists first
                            build_dict['services'].remove(menu['options'][position]['command'])
                        else:
                            # remove from docker hosts
                            if self.default:
                                self.hosts.remove(menu['options'][position])
                            else:
                                if "options" in menu['options'][position]:
                                    if "config" in menu['options'][position]['options'][0]:
                                        if "unique" == menu['options'][position]['options'][0]['config']:
                                            self.unique = False
                                        if "cmd" == menu['options'][position]['options'][0]['config']:
                                            self.cmd = False
                                        if "entrypoint" == menu['options'][position]['options'][0]['config']:
                                            self.entrypoint = False
                                        if "volume" == menu['options'][position]['options'][0]['config']:
                                            self.volume = False
                                        if "port" == menu['options'][position]['options'][0]['config']:
                                            self.port = False
                                        if "link" == menu['options'][position]['options'][0]['config']:
                                            self.link = False
                                        if "name" == menu['options'][position]['options'][0]['config']:
                                            self.name = False
                                        if "user" == menu['options'][position]['options'][0]['config']:
                                            self.user = False
                elif key != ord('\n'):
                    curses.flash()
            except:
                curses.flash()
            self.menus_dict[hash_menu] = choice
        return position, back, build_dict

    @staticmethod 
    def options_menu(self, menu, config_dict, parent=None):
        option_size = len(menu['options'])
        exit_menu = False
        while not exit_menu:
            position, back, config_dict = self.display_menu(self, menu, parent, config_dict)
            if position == option_size:
                exit_menu = True
        return config_dict

    @staticmethod 
    def process_menu(self, menu, build_dict, parent=None):
        option_size = len(menu['options'])
        exit_menu = False
        while not exit_menu and not self.launch and not self.exit:
            position, back, build_dict = self.display_menu(self, menu, parent, build_dict)
            if position == option_size:
                exit_menu = True
                if back == "Exit":
                    self.exit = True
            elif menu['options'][position]['type'] == "menu":
                build_dict = self.process_menu(self, menu['options'][position], build_dict, menu)
            elif menu['options'][position]['type'] == "launch":
                if position == 1:
                    self.image = True
                self.launch = True
        return build_dict
