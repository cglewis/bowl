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

# !! TODO this needs to be refactored when there are multiple versions
from bowl.containers.ubuntu.precise.databases import databases
from bowl.containers.ubuntu.precise.environment import environment
from bowl.containers.ubuntu.precise.services import services

class new(object):
    """
    This class is responsible for the new command of the cli.
    """
    @staticmethod
    def build_dockerfile(self, dockerfile, uuid_dir):
        # !! TODO use docker host(s) that were selected
        c = docker.Client(base_url='tcp://localhost:4243', version='1.9',
                          timeout=10)

        # try/catch
        with open('/tmp/'+uuid_dir+'/Dockerfile', 'w') as f:
            for line in dockerfile:
                f.write(line+'\n')
        c.build(tag="bowl-"+uuid_dir, quiet=False, path='/tmp/'+uuid_dir,
                nocache=False, rm=False, stream=False)
        #os.remove('/tmp/'+uuid_dir+'/Dockerfile')
        shutil.rmtree('/tmp/'+uuid_dir)
        return c

    @staticmethod
    def run_dockerfile(self, c, image_tag):
        # TODO check if tty and stdin_open (interactive) are needed
        container = c.create_container(image_tag, tty=True, stdin_open=True)
        c.start(container, publish_all_ports=True)

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
        os_num = 0
        for key,os_inst in os_dict.iteritems():
            version_list = inspect.getmembers(os_inst.versions,
                                              predicate=inspect.ismethod)
            version_num = 0
            for version in version_list:
                menu_dict['options'][0]['options'][os_num]['options'].append(getattr(os_inst.versions(), version[0])())

                os_name = key.split("_", 1)
                package = base + os_name[0] + "." + version[0] + "."

                database_dict = {
                 'title': "Databases",
                 'type': "menu",
                 'subtitle': "Please select databases...",
                 'options': []
                }
                db_package = package + "databases"
                db_inst = getattr(__import__(db_package, fromlist=['databases']), 'databases')
                database_list = inspect.getmembers(db_inst.databases, predicate=inspect.ismethod)
                for database in database_list:
                    self.combine_cmd_dict[package+database[0]] = getattr(db_inst.databases(), database[0])()['combine_cmd']
                    database_dict['options'].append(getattr(db_inst.databases(), database[0])())

                environment_dict = {
                 'title': "Environment Tools",
                 'type': "menu",
                 'subtitle': "Please select environment tools...",
                 'options': []
                }
                env_package = package + "environment"
                env_inst = getattr(__import__(env_package, fromlist=['environment']), 'environment')
                environment_list = inspect.getmembers(env_inst.environment, predicate=inspect.ismethod)
                for environ in environment_list:
                    self.combine_cmd_dict[package+environ[0]] = getattr(env_inst.environment(), environ[0])()['combine_cmd']
                    environment_dict['options'].append(getattr(env_inst.environment(), environ[0])())

                service_dict = {
                 'title': "Services",
                 'type': "menu",
                 'subtitle': "Please select services...",
                 'options': []
                }
                serv_package = package + "services"
                serv_inst = getattr(__import__(serv_package, fromlist=['services']), 'services')
                service_list = inspect.getmembers(serv_inst.services, predicate=inspect.ismethod)
                for service in service_list:
                    self.combine_cmd_dict[package+service[0]] = getattr(serv_inst.services(), service[0])()['combine_cmd']
                    service_dict['options'].append(getattr(serv_inst.services(), service[0])())

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

                launch_dict = {
                 'title': "Launch Container",
                 'type': "launch"
                }

                menu_dict['options'][0]['options'][os_num]['options'][version_num]['options'].append(database_dict)
                menu_dict['options'][0]['options'][os_num]['options'][version_num]['options'].append(environment_dict)
                menu_dict['options'][0]['options'][os_num]['options'][version_num]['options'].append(service_dict)
                menu_dict['options'][0]['options'][os_num]['options'][version_num]['options'].append(host_dict)
                menu_dict['options'][0]['options'][os_num]['options'][version_num]['options'].append(launch_dict)
                version_num += 1
            os_num += 1
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
        valid = {"yes":True,   "y":True,  "ye":True,
                 "no":False,     "n":False}
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
        # build dictionary of available container options
        self.combine_cmd_dict = {}
        menu_dict = self.build_options(self)

        self.win = curses.initscr()
        self.win.keypad(1)
        self.build_dict = {}
        self.build_dict['services'] = []
        self.launch = False
        self.user = False

        # init curses stuff
        curses.noecho()
        curses.cbreak()
        curses.start_color()
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

        self.process_menu(self, menu_dict)
        curses.endwin()
        if self.launch:
            self.user = self.query_yes_no(self, "Do you want an account on this container?")
            if self.user:
                username = raw_input("Enter username: ")
                ssh_pubkey = raw_input("Enter path to ssh public key: ")

            # !! TODO use this to build the dockerfile
            # !! TODO if no services were selected, don't create a container
            # !! TODO if contains an ADD line, be sure and copy additional files
            this_dir, this_filename = os.path.split(__file__)
            services = self.build_dict['services']
            dockerfile = []
            num_services = len(services)
            for service in sorted(services):
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
                            elif line.startswith("ADD"):
                                # !! TODO
                                # copy context directory to tmp directory for building
                                dockerfile.append(line.rstrip('\n'))
                            # check for multiple USER commands
                            elif line.startswith("USER"):
                                # !! TODO
                                dockerfile.append(line.rstrip('\n'))
                            # check for multiple ENTRYPOINT commands
                            elif line.startswith("ENTRYPOINT"):
                                # !! TODO
                                # check WORKDIR since CMD and ENTRYPOINT are modified
                                # use the ENTRYPOINT that corresponds with the chosen CMD
                                if num_services == 1:
                                    dockerfile.append(line.rstrip('\n'))
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
                                        dockerfile.append(line.rstrip('\n'))
                                cmd = (line.rstrip('\n')).split(" ", 1)[1:][0]
                            else:
                                dockerfile.append(line.rstrip('\n'))

            uuid_dir = str(uuid.uuid4())
            # !! TODO try/except
            os.mkdir('/tmp/'+uuid_dir)
            if self.user:
                try:
                    # !! TODO try/except
                    with open(ssh_pubkey, 'r') as fi:
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
                    dockerfile.append("RUN apt-get install sudo")
                    dockerfile.append('RUN echo "'+username+
                                      ' ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers')
                    # !! TODO ask if more than one user
                except:
                    print "SSH Key file not found, failed to create user"
            print "\n### GENERATED DOCKERFILE ###"
            for line in dockerfile:
                print line
            print "### END GENERATED DOCKERFILE ###\n"
            c = self.build_dockerfile(self, dockerfile, uuid_dir)
            self.run_dockerfile(self, c, 'bowl-'+uuid_dir)

    @staticmethod
    def display_menu(self, menu, parent):
        if parent is None:
            back = "Exit"
        else:
            back = "Return to %s menu" % parent['title']

        option_size = len(menu['options'])
        position = 0
        key = None
        highlighted = curses.color_pair(1)
        normal = curses.A_NORMAL
        choice = [" "]*(option_size+1)

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
                            self.build_dict['services'].append(menu['options'][position]['command'])
                    else:
                        choice[position] = " "
                        if "command" in menu['options'][position]:
                            # remove from build_dict
                            # TODO check if exists first
                            self.build_dict['services'].remove(menu['options'][position]['command'])
                elif key != ord('\n'):
                    curses.flash()
            except:
                curses.flash()
        return position

    @staticmethod 
    def process_menu(self, menu, parent=None):
        option_size = len(menu['options'])
        exit_menu = False
        while not exit_menu and not self.launch:
            position = self.display_menu(self, menu, parent)
            if position == option_size:
                exit_menu = True
            elif menu['options'][position]['type'] == "menu":
                self.process_menu(self, menu['options'][position], menu)
            elif menu['options'][position]['type'] == "launch":
                self.launch = True
