from time import sleep
from datetime import datetime
import _thread
import notify
import curses
####ENVIRON###
def tick(Screen, Veridis):
	update(Screen, Veridis)
	sleep(60-datetime.now().second)
	tick(Screen, Veridis)
def update(Screen, Veridis):
	#Redraw frames
	Screen.clear()
	height, width = Screen.getmaxyx()
	vert=[]
	horiz=[]
	for name, frame in Veridis.frames.items():
		if not frame.top == 0:
			if not frame.top in horiz: horiz.append(frame.top)
		if not frame.left == 0:
			if not frame.left in horiz: vert.append(frame.left)
	for x in vert:
		Screen.vline(0,int(width*(x/100)),curses.ACS_VLINE,int(height))
	for y in horiz:
		Screen.hline(int(height*(y/100)),int(width*(min(vert)/100)),curses.ACS_HLINE,int(width-(width*(min(vert)/100))))
	Screen.border()
	for y in horiz:
		#Draw in the pipes
		Screen.addch(int(height*(y/100)),int(width*(min(vert)/100)), curses.ACS_LTEE)
		Screen.addch(int(height*(y/100)),width-1, curses.ACS_RTEE)
	for x in vert:
		#Draw in the pipes
		Screen.addch(0,int(width*(x/100)), curses.ACS_BSSS)
		Screen.addch(height-1,int(width*(x/100)), curses.ACS_BTEE)
	Screen.refresh()
def react(input, Screen, Veridis):
	if (input == 113):
		Veridis.running=False
	elif (input == 410):
		update(Screen, Veridis)
#####MAIN#####
def main(Screen, Veridis):
	_thread.start_new_thread(tick,(Screen, Veridis))
	#Make the 3 Main frames.
	Veridis.frames["A"] = Veridis.types.frame(70,100,0,0)
	Veridis.frames["B"] = Veridis.types.frame(10,60,70,0)
	Veridis.frames["C"] = Veridis.types.frame(10,40,70,60)
	while Veridis.running:
		Screen.refresh()
		update(Screen, Veridis)
		react(Screen.getch(), Screen, Veridis)