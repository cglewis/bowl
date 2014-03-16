"""
This module is the new command of punt.

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
        # init curses stuff
        win = curses.initscr()
        win.keypad(1)
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
             ]
            },
           ]
          },
         ]
        }
        self.process_menu(self, win, menu_dict)
        curses.endwin()

    @staticmethod
    def display_menu(self, win, menu, parent):
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
            win.clear()
            win.border(0)
            win.addstr(2,2, menu['title'], curses.A_STANDOUT)
            win.addstr(4,2, menu['subtitle'], curses.A_BOLD)

            for index in range(option_size):
                textstyle = normal
                if position == index:
                    textstyle = highlighted
                if menu['options'][index]['type'] == "choice_menu":
                    win.addstr(index+5, 4, "%d - [%s] %s" % (index+1, choice[index], menu['options'][index]['title']), textstyle)
                else:
                    win.addstr(index+5, 4, "%d - %s" % (index+1, menu['options'][index]['title']), textstyle)
            textstyle = normal
            if position == option_size:
                textstyle = highlighted
            win.addstr(option_size+5, 4, "%d - %s" % (option_size+1, back), textstyle)
            win.refresh()

            key = win.getch()
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
            elif key == 32:
                if choice[position] == " ":
                    choice[position] = "x"
                else:
                    choice[position] = " "
            elif key != ord('\n'):
                curses.flash()
        return position

    @staticmethod
    def process_menu(self, win, menu, parent=None):
        option_size = len(menu['options'])
        exit_menu = False
        while not exit_menu:
            position = self.display_menu(self, win, menu, parent)
            if position == option_size:
                exit_menu = True
            elif menu['options'][position]['type'] == "menu":
                self.process_menu(self, win, menu['options'][position], menu)
