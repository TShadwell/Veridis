print("Veridis init.")
import curses
from math import floor
class Veridis:
	class types:
		class frame:
			def __init__(Self, percwidth, percheight, percleft, perctop):
				Self.width=percwidth
				Self.height=percheight
				Self.left=percleft
				Self.top=perctop
				Self.r_width=Self.width/100
				Self.r_height=Self.height/100
		class table:
			def __init__(Self, table, percx, percy,coloura, colourb, padding=(0,0), wrap=1):
				Self.table=table
				Self.x=percx
				Self.y=percy
				Self.padding=padding
				Self.wrap=wrap
			
		class textobject:
			def __init__(Self, text, percx, percy, padding=(0,0),attrs=0, wrap=-1):
				Self.text= text
				Self.top= percy
				Self.left= percx
				Self.r_top=Self.top/100
				Self.r_left=Self.left/100
				Self.wrap=wrap
				Self.padding=padding
				Self.attrs = attrs
			def draw(Self, Screen):
				height, width = Screen.getmaxyx()
				for n, line in enumerate(Self.text.split("\n")):
					Screen.addstr(n+int(Self.r_top*height)+Self.padding[1],int(Self.r_left*width)+Self.padding[0],line, Self.attrs)
	def __init__(Self):
		import notify
		import settings
		Self.notify=notify
		Self.settings=settings
	running = True
	frames={}
	Drawables={}
#####INIT#####
def init(Screen):
	from main import main
	curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
	curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
	curses.curs_set(0)
	veridis = Veridis()
	veridis.settings.tasks = veridis.settings.readsettings("data/tasks", veridis)
	veridis.settings.schedule = veridis.settings.readsettings("data/schedule", veridis)
	main(Screen, veridis)
#################
curses.wrapper(init)
