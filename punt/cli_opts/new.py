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
                                               'type': "command",
                                               'command': "ubuntu:precise"
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
        prev_pos = None
        key = None
        highlighted = curses.color_pair(1)
        normal = curses.A_NORMAL

        while key != ord('\n'):
            if position != prev_pos:
                prev_pos = position
                win.clear()
                win.border(0)
                win.addstr(2,2, menu['title'], curses.A_STANDOUT)
                win.addstr(4,2, menu['subtitle'], curses.A_BOLD)

                for index in range(option_size):
                    textstyle = normal
                    if position == index:
                        textstyle = highlighted
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
            elif key != ord('\n'):
                curses.flash()
        return position

    @staticmethod
    def process_menu(self, win, menu, parent=None):
        option_size = len(menu['options'])
        exit_menu = False
        while not exit_menu:
            getin = self.display_menu(self, win, menu, parent)
            if getin == option_size:
                exit_menu = True
            elif menu['options'][getin]['type'] == "menu":
                self.process_menu(self, win, menu['options'][getin], menu)
