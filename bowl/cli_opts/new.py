"""
This module is the new command of bowl.

Created on 15 March 2014
@author: Charlie Lewis
"""

import curses
import importlib
import inspect
import os
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
    def dockerfiles(self, service):
        # !! TODO
        return []

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
                    service_dict['options'].append(getattr(serv_inst.services(), service[0])())

                launch_dict = {
                 'title': "Launch Container",
                 'type': "launch"
                }

                menu_dict['options'][0]['options'][os_num]['options'][version_num]['options'].append(database_dict)
                menu_dict['options'][0]['options'][os_num]['options'][version_num]['options'].append(environment_dict)
                menu_dict['options'][0]['options'][os_num]['options'][version_num]['options'].append(service_dict)
                menu_dict['options'][0]['options'][os_num]['options'][version_num]['options'].append(launch_dict)
                version_num += 1
            os_num += 1
        return menu_dict

    @classmethod
    def main(self, args):
        # build dictionary of available container options
        menu_dict = self.build_options(self)

        self.win = curses.initscr()
        self.win.keypad(1)
        self.build_dict = {}
        self.build_dict['services'] = []
        self.launch = False

        # init curses stuff
        curses.noecho()
        curses.cbreak()
        curses.start_color()
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

        self.process_menu(self, menu_dict)
        curses.endwin()
        # !! TODO use this to build the dockerfile
        # !! TODO if no services were seleted, don't create a container
        # !! TODO if contains an ADD line, be sure and copy additional files
        this_dir, this_filename = os.path.split(__file__)
        print this_dir
        print this_filename
        print self.build_dict

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
                if menu['options'][index]['type'] == "choice_menu":
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
            if key >= ord('1') and key <= ord(str(option_size+1)):
                position = key - ord('0') - 1
            elif key == 258:
                if position < option_size:
                    position += 1
                else:
                    position = 0
            elif key == 259:
                if position > 0:
                    position += -1
                else:
                    position = option_size
            # !! TODO error check this!!
            elif key == 32 and menu['options'][position]['type'] == "choice_menu":
                if choice[position] == " ":
                    choice[position] = "x"
                    # add to build_dict
                    self.build_dict['services'].append(menu['options'][position]['command'])
                else:
                    choice[position] = " "
                    # remove from build_dict
                    # TODO check if exists first
                    self.build_dict['services'].remove(menu['options'][position]['command'])
            elif key != ord('\n'):
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
