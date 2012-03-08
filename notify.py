from os import system
Queue =[]
def error(text):
	system("zenity --error --text='%s' --title='Error' &" % (text))