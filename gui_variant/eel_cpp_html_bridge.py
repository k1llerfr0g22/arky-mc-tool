import eel
import threading

@eel.expose
def hello_world():
	print("hello world")

def python_suicide_quit():
	system("killall python3")


def start_server_from_java():
	

def start_server():
	# I have to add parameters in this func that define the ram
	print("start_server worked")


# (DEFINE) START SERVR JAR WITH THREADS:

th1 = threading.Thread(target=threadFunc)
th1.start()


eel.init("html")
eel.start("home.html", cmdline_args=['--kiosk'])