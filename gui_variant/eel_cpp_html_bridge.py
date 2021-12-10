#!/usr/bin/python
import eel
import threading
import os
import time

#### VARS:      ####
# VARS FOR RAM AMOUNT ARG 	
two = "-Xmx2g"
four = "-Xmx4g"
six = "-Xmx6g"
start_server_bool = True


# START MSG:
print("starting.")


#### FUNCTIONS: ####
@eel.expose
def python_suicide_quit():
	system("killall python3")

def hello_world():
	print("hello_world")


#def start_server_from_js(): (idk why this is here but maybe ill need this reminder later...)

"""def start_server():
	global ram
	if ram == 6:
		os.system("cd /home/k1llerfr0g/code/server/minecraft/aternos && java " + str(six) + " -jar minecraft_server1.17.1.jar")
		print("start_server worked")

	if ram == 4:
		os.system("cd /home/k1llerfr0g/code/server/minecraft/aternos && java " + str(four) + " -jar minecraft_server1.17.1.jar")
		print("start_server worked")

	if ram == 2:
		os.system("cd /home/k1llerfr0g/code/server/minecraft/aternos && java " + str(two) + " -jar minecraft_server1.17.1.jar")
		print("start_server worked")"""

def loading(loading_step):
	if loading_step == 1:
		print("   loading " + "|" + u'\u2588' +  u'\u2593' + u'\u2592' + u'\u2591');





def start_server_2g():
	print("called python sts2func")
	os.system("cd /home/k1llerfr0g/code/server/minecraft/aternos && java " + str(two) + " -jar minecraft_server1.17.1.jar")

def start_server_4g():
	os.system("cd /home/k1llerfr0g/code/server/minecraft/aternos && java " + str(four) + " -jar minecraft_server1.17.1.jar")

def start_server_6g():
	os.system("cd /home/k1llerfr0g/code/server/minecraft/aternos && java " + str(six) + " -jar minecraft_server1.17.1.jar")

def sts2g_thread():
	os.system("firefox")
	#sts2g = threading.Thread(target=start_server_2g)
	#sts2g.start()
	#sts2g.join()

def sts4g_thread():
	sts4g = threading.Thread(target=start_server_4g).start()


def sts6g_thread():
	sts2g = threading.Thread(target=start_server_6g).start()


def start_html():
	eel.init("html")
	eel.start("home.html", cmdline_args=['--kiosk'])

# TEST THE LOADING FUNC
#while True:
#	loading(1)
#	loading(2)


#### THREADS:   ####
start_html = threading.Thread(target=start_html)


start_html.start()


start_html.join()








