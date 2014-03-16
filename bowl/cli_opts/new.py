"""
This module is the new command of bowl.

Created on 15 March 2014
@author: Charlie Lewis
"""

import curses

class new(object):
    """
    This class is responsible for the new command of the cli.
    """
    @classmethod
    def main(self, args):
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
        # !! TODO break this out into different files
        menu_dict = {
         'title': "Build Container",
         'type': "menu",
         'subtitle': "Please select an Operating System...",
         'options': [
          {
           'title': "Ubuntu",
           'type': "menu",
           'subtitle': "Please select a version...",
           'options': [
            {
             'title': "12.04 LTS Precise",
             'type': "menu",
             'subtitle': "Please select services...",
             'options': [
              {
               'title': "Services",
               'type': "menu",
               'subtitle': "Please select services...",
               'options': [
                {
                 'title': "SSH Server",
                 'type': "choice_menu",
                 'command': "ubuntu:precise:sshd"
                },
                {
                 'title': "tmux",
                 'type': "choice_menu",
                 'command': "ubuntu:precise:tmux"
                },
               ]
              },
              {
               'title': "Databases",
               'type': "menu",
               'subtitle': "Please select databases...",
               'options': [
                {
                 'title': "redis",
                 'type': "choice_menu",
                 'command': "ubuntu:precise:redis"
                },
               ]
              },
              {
               'title': "Developer Tools",
               'type': "menu",
               'subtitle': "Please select developers tools...",
               'options': [
                {
                 'title': "python",
                 'type': "choice_menu",
                 'command': "ubuntu:precise:python"
                },
               ]
              },
              {
               'title': "Launch Container",
               'type': "launch"
              },
             ]
            },
           ]
          },
         ]
        }
        self.process_menu(self, menu_dict)
        curses.endwin()
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
