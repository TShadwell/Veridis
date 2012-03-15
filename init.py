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
			def draw (Self, Screen):
				#[["Time","Event"],[time, event]]
				#Calculate the widths of the rows
				height, width = Screen.getmaxyx()
				
				#Draw the header
				
				#for row in table:
			
		class textobject:
			def __init__(Self, text, percx, percy, padding=(0,0),attrs=0, wrapy=False):
				Self.text= text
				Self.top= percy
				Self.left= percx
				Self.r_top=Self.top/100
				Self.r_left=Self.left/100
				Self.wrapy=wrapy
				Self.padding=padding
				Self.attrs = attrs
			def shift(Self,n, Screen):
				height, width = Screen.getmaxyx()
				dest = Self.i_shift + n
				textlength = len(Self.text.split("\n"))
				outOfBounds= (not((textlength-dest)<(height-2)))
				if ((dest < textlength) and (dest >= 0)):
					Self.i_shift +=n
			i_shift =0
			def draw(Self, Screen):
				height, width = Screen.getmaxyx()
				for n, line in (list(enumerate(Self.text.split("\n")[Self.i_shift:(height+Self.i_shift-2)])) if Self.wrapy else enumerate(Self.text.split("\n"))):
					Screen.addstr(n+int(Self.r_top*height)+Self.padding[1],int(Self.r_left*width)+Self.padding[0],line, Self.attrs)
				#if Self.wrapy:
					#Clear up bits that aren't there anymore.

	def __init__(Self):
		import notify
		import settings
		Self.notify=notify
		Self.settings=settings
	#Day [(secssincemidnight, length, name)]
	day=[]
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
