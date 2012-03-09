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
				r_width=Self.width/100
				r_height=Self.height/100
	def __init__(Self):
		import notify
		import settings
		Self.notify=notify
		Self.settings=settings
	running = True
	frames = {}
#####INIT#####
def init(Screen):
	from main import main
	curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
	curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
	curses.curs_set(0)
	veridis = Veridis()
	main(Screen, veridis)
#################
curses.wrapper(init)