import eel
import threading
import os

six = "-Xmx6g"

@eel.expose
def hello_world():
	print("hello world")

def python_suicide_quit():
	system("killall python3")


#def start_server_from_js():

ram = input("input_ram: ")

if ram == "2":
	th1 = threading.Thread(target=start_server, args=(2,))

elif ram == "4":
	th1 = threading.Thread(target=start_server, args=(4,))

elif ram == "6":
	th1 = threading.Thread(target=start_server, args=(6,))


def start_server(ram):

	if ram == 6:
		ram =
	os.system("cd /home/k1llerfr0g/code/server/minecraft/aternos && java " + str(six) + " -jar minecraft_server1.17.1.jar")
	print("start_server worked")


def start_html():
	eel.init("html")
	eel.start("home.html", cmdline_args=['--kiosk'])

# (DEFINE) START SERVR JAR WITH THREADS:

start_html = threading.Thread(target=start_html)
th1 = threading.Thread(target=start_server, args=(4,))
th1.start()
start_html.start()
th1.join()
start_html.join()