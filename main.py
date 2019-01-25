#!/usr/bin/env python3

import curses
import time
import verygen


def menu(scr, choices, title = None):
    scr.nodelay(False)
    selected = 0
    while True:
        scr.clear()
        height, width = scr.getmaxyx()
        if title != None:
            start_l = (height-len(choices)+1)//2
            scr.addstr(start_l-1, (width-len(title))//2, title)
        else:
            start_l = (height-len(choices))//2
        for l in range(len(choices)):
            txt = choices[l]
            start_c = (width-len(txt))//2
            if l == selected:
                scr.addstr(start_l+l, start_c, txt, curses.A_REVERSE)
            else:
                scr.addstr(start_l+l, start_c, txt)
        scr.refresh()
        k = scr.getkey()
        if k=="KEY_DOWN":
            selected += 1
        elif k=="KEY_UP":
            selected -= 1
        elif k=="\n" or k==" ":
            scr.clear()
            scr.nodelay(True)
            return selected
        selected %= len(choices)


def main(scr):
    curses.curs_set(0)
    while True:
        choice = menu(scr, ['play','quit'])
        if choice == 0:
            scr.clear()
            game(scr)
            scr.clear()
        else:
            break

def bar(scr, l, c, width, value):
    scr.addstr(l,c,'#'*int(width*value))

def update(scr, room):
    scr.clear()
    for l, line in enumerate(room.grid):
        for c, tile in enumerate(line):
            if tile.is_a_wall():
                scr.addstr(l, c, "w")
    scr.refresh()

def game(stdscr):
    stdscr.clear()
    stdscr.refresh()
    height, width = stdscr.getmaxyx()
    menu_scr = curses.newwin(height, 10, 0, 0)
    game_scr = curses.newwin(height, width-10, 0, 10)
    game_scr.nodelay(True)
    level = verygen.Level()
    level.generate()
    while True:
        #update menu
        bar(menu_scr, 0, 0, 10, 1)
        menu_scr.refresh()
        update(game_scr, level.main_room)
        k = ''
        while True:
            try:
                k = game_scr.getkey()
            except curses.error:
                break
        time.sleep(0.05)


curses.wrapper(main)
