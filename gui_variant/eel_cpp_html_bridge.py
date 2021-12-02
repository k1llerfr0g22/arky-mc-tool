import eel
import threading
import os

#### VARS:      ####
# VARS FOR RAM AMOUNT ARG 	
two = "-Xmx2g"
four = "-Xmx4g"
six = "-Xmx6g"
start_server_bool = True


#### FUNCTIONS: ####
@eel.expose

def hello_world():
	print("hello world")

def python_suicide_quit():
	system("killall python3")


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


def start_html():
	eel.init("html")
	eel.start("home.html", cmdline_args=['--kiosk'])

# DEFINE THREADS:

start_html =  threading.Thread(target=start_server)


# ACTUAL RUNNING SCRIPT (OR IDK HOW TO CALL IT LOL)


start_html.start()
start_html.join()








