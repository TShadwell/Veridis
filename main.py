from time import sleep
from datetime import datetime
import _thread
import notify
import curses
def Sto24(secs):
	hour=secs//3600
	minute =(secs%3600)//60
	return("%s%s%s%s"%("0"*(2-len(str(hour))),hour,"0"*(2-len(str(minute))), minute))
####ENVIRON###
def tick(Screen, Veridis):
	clock(Screen, Veridis)
	sleep(60-datetime.now().second)
	tick(Screen, Veridis)
def clock(Screen, Veridis):
	#Calculate the size of the upper-right box to see if an art-based clock would work.
	height, width = Screen.getmaxyx()
	now=datetime.now().strftime("%H:%M")
	if (int(width*0.3)-1) <= ((7 * len(now))):
		#Display a text-based clock
		Veridis.Drawables["clock"].text= now
	else:
		lines ={}
		for char in now:
			for n, line in enumerate(Veridis.settings.clockface[char].split("\n")):
				if n in lines:
					lines[n] += line.replace("#", "█")
				else:
					lines[n] = line.replace("#", "█")
		Veridis.Drawables["clock"].text=("\n".join([text.strip(" ").replace("b", " ") for key, text in lines.items() if not len(text.strip(" "))==0]))
	#notify.error(Veridis.Drawables["clock"].text)
	update(Screen, Veridis)
	Screen.refresh()
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
	#Calculate the padding for the clock
	Veridis.Drawables["clock"].padding=(int(((width*0.3)/2)-(len(Veridis.Drawables["clock"].text.split("\n")[0])/2)),1)
	#Draw in the textobjects
	for name, t in Veridis.Drawables.items():
		t.draw(Screen)
	Screen.refresh()
def react(input, Screen, Veridis):
	if (input == 113):
		Veridis.running=False
	elif (input == 410):
		update(Screen, Veridis)
		clock(Screen, Veridis)
	elif (input == 258):
		Veridis.Drawables["timetable"].shift(-1, Screen)
		Veridis.Drawables["timetable"].draw(Screen)
		Screen.refresh()

	elif (input == 259):
		Veridis.Drawables["timetable"].shift(1, Screen)
		Veridis.Drawables["timetable"].draw(Screen)
		Screen.refresh()
	else:
		pass#notify.error(input)
#####MAIN#####
def main(Screen, Veridis):
	curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
	_thread.start_new_thread(tick,(Screen, Veridis))
	#Make the 3 Main frames.
	Veridis.frames["A"] = Veridis.types.frame(70,100,0,0)
	Veridis.frames["B"] = Veridis.types.frame(10,60,70,0)
	Veridis.frames["C"] = Veridis.types.frame(10,40,70,60)
	#Draw in titles
	Veridis.Drawables["now"] = Veridis.types.textobject("Now", 70,0, (1,0))
	Veridis.Drawables["next"] = Veridis.types.textobject("Next", 70,60, (1,0))
	#Clock placeholder
	Veridis.Drawables["clock"] = Veridis.types.textobject("clock", 70,0, (1,1), curses.color_pair(1))
	Veridis.Drawables["timetable"] = Veridis.types.textobject("\n".join([str(x)for x in range(Screen.getmaxyx()[0]-10)]),0,0,(1,1),0, True)
	for period in Veridis.settings.schedule:
		begin, end  = map((lambda t: int(t[:2])*3600+int(t[2:])*60),period["period"].split("-"))
		if int(end-begin) <0:
			#We need two tasks, because this one wraps around to the next day.
			Veridis.day.append((begin, 86400-begin, period["name"]))
			Veridis.day.append((0, end, period["name"]))
		else:
			Veridis.day.append((begin, end-begin, period["name"]))
	Veridis.day=sorted(Veridis.day)
	lst = []
"""
FUNCTION SUMMARY
0:00->day[0][0]
               -> day[1][0]
                           -> day[2][0] etc..
lst=(lst.insert(0,(0,0)) if not(lst[0][0]==0) else lst)#Insert a 'phantom' task at the beginning so the later logic notices the 0->day[1] space, if there is no task starting at 0:00.
[(items[0][0]+items[0][1], items[1][0]) for items in zip(lst, (lst[1:] if (lst[-1][0]+lst[-1][1]==24*3600) else lst.append((24*3600,0))) if not(items[0][0]+items[0][1]>=items[1][0])]
"""
	for i in range(len(Veridis.day)+1): #+1 to account for possible 0:00->task[0]
		n=i-1
		if n==len(Veridis.day)-1:
			break
		elif (n<0) and (not(Veridis.day[i][0]==0)):
			lst.append((0, Veridis.day[i][0]))
		elif (n<0):
			pass
		else:
			start =Veridis.day[n][0]+Veridis.day[n][1]
			lst.append((Veridis.day[n][0]+Veridis.day[n][1], Veridis.day[i][0]))

	notify.error(str(lst)+ "\n|\n" + str(Veridis.day))
	#for slot in Veridis.settings.day:
	#	for prioritytask in [x for x in Veridis.settings.tasks if "Priority" in x]:

	while Veridis.running:
		#Screen.refresh()
		#update(Screen, Veridis)
		react(Screen.getch(), Screen, Veridis)
