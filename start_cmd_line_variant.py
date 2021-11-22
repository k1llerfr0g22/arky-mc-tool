import os
import time

print("starting the mc-server-tool in command line variant")
time.sleep(1)
print("compiling code...")
os.system("cd /home/k1llerfr0g/code/c++/projects/tools/mc-server-tool/cmd_line_variant && g++ main.cpp -o main.bin")
print("DONE!")
time.sleep(0.8)
os.system("clear")
print("PRESS ENTER TO START")
input()
os.system("cd /home/k1llerfr0g/code/c++/projects/tools/mc-server-tool/cmd_line_variant && ./main.bin")
