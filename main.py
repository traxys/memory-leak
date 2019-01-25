#!/usr/bin/env python3

import curses
import time
import verygen, player, utils, ai

menu_width = 24

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
            letter = ''
            if tile.is_a_wall():
                letter = 'w'
            elif tile.has_entity():
                if isinstance(tile.entity, player.Player):
                    letter = 'ô'
                else:
                    letter = 'e'
            scr.addstr(l, c, letter)

cut = lambda x: x*(x>0)

def game(stdscr):
    stdscr.clear()
    stdscr.refresh()
    height, width = stdscr.getmaxyx()
    menu_scr = curses.newwin(height, menu_width, 0, 0)
    game_scr = curses.newwin(height, width-menu_width-1, 0, menu_width+1)
    for l in range(height):
        stdscr.addstr(l,menu_width, '|')
    stdscr.refresh()
    game_scr.nodelay(True)
    level = verygen.Level()
    level.generate()
    protagonist = player.Player(level.main_room)
    level.spawn_player(protagonist)
    enemies = [ai.Enemy(protagonist, protagonist.room, x_pos=2, y_pos=3)]
    protagonist.room.spawn_enemy(enemies[0])
    loop_start = time.time()
    while True:
        #update menu
        bar(menu_scr, 0, 0, menu_width, 1)
        update(game_scr, protagonist.room)
        k = ''
        while True:
            try:
                k = game_scr.getkey()
            except curses.error:
                break
        if k == 'A':
            protagonist.move(utils.Direction.Kita)
        if k == 'B':
            protagonist.move(utils.Direction.Minami)
        if k == 'C':
            protagonist.move(utils.Direction.Higashi)
        if k == 'D':
            protagonist.move(utils.Direction.Nishi)
        elif k != '':
            menu_scr.addstr(1,0,k)
        menu_scr.refresh()
        game_scr.refresh()
        time.sleep(cut(0.05+loop_start-time.time()))
        loop_start = time.time()


curses.wrapper(main)
