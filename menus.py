import curses,time

def menu(scr, choices, title = None):
	scr.nodelay(False)
	selected = 0
	while True:
		scr.clear()
		height, width = scr.getmaxyx()
		if title != None:
			start_l = (height-len(choices)+1)/2
			scr.addstr(start_l-1, (width-len(title))/2, title)
		else:
			start_l = (height-len(choices))/2
		for l in xrange(len(choices)):
			txt = choices[l]
			start_c = (width-len(txt))/2
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
            pass
            #scr.clear()
            #scr.addstr(0,0,"there is no game you fucker !")
            #scr.refresh()
            #k = scr.getkey()
            #scr.clear()
        else:
            break


curses.wrapper(main)