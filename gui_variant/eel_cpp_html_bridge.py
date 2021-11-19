import eel

@eel.expose
def hello_world():
	print("hello world")

def python_suicide_quit():
	system("killall python3")



eel.init("html")
eel.start("index.html", cmdline_args=['--kiosk'])