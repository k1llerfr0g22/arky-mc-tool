import os
import keyboard
import time
import importlib.util
import sys


os.system("clear")

# THIS IS FROM STACKOVERFLOW AGAIN LOL:

package_needed = "pip"


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# THIS SHIT DOESNT WORKS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!



print("checking depencies")
time.sleep(2)
if package_needed in sys.modules:
    print(f"{package_needed!r} already in sys.modules")
    time.sleep(2)
elif (spec := importlib.util.find_spec(package_needed)) is not None:
    # If you choose to perform the actual import ...
    module = importlib.util.module_from_spec(spec)
    sys.modules[package_needed] = module
    spec.loader.exec_module(module)
    print("all depencies are installed!")
    #print(f"{package_needed!r} has been imported")
    time.sleep(2)

else:
    print(f"can't find the {package_needed!r} module")
    time.sleep(1)
    print("installing" + package_needed)
    os.system("pip install eel")
    time.sleep(1)
    print("installed " + package_needed)


choice = 0

class clrs:          # DEFINE THE COLORS
    BackgroundWhite        = "\033[107m"
    ResetAll = "\033[0m"
    LightGreen   = "\033[92m"
    BOLD = '\033[1m'
    Black        = "\033[30m"

def reset_color():  # DEFINE'S A FUNCTION THAT RESET THE COLOR BY SET THE COLOR TO NONE
    print(clrs.ResetAll + '')

def reset_choice(): # DEFINE'S A FUNCTION THAT RESET THE CHOICE VARIABLE
    choice == 0

reset_choice()

# DEFAULT MENU
"""
        print(clrs.LightGreen + '')
        print("    +++++++++++++++++++++++++++++++++++++++++++")
        print("    +                                         +")
        print("    +               GUI-VARIANT               +")
        print("    +                                         +")
        print("    +                  CLI                    +")
        print("    +                                         +")
        print("    +                  EXIT                   +")
        print("    +                                         +")
        print("    +++++++++++++++++++++++++++++++++++++++++++")
"""
while True:  # MAINLOOP

    reset_color()

    if keyboard.is_pressed('s'): # IF THE S KEY GET PRESSED THE CHOICE VAR
        choice = choice + 1
        time.sleep(0.09)

    if keyboard.is_pressed('w'):
        choice = choice - 1
        time.sleep(0.09)

    if keyboard.is_pressed('q'):
        exit()

    if keyboard.is_pressed('enter'):
        if choice == 2:
            exit()

        if choice == 1:
            os.system("cd data && python3 start_cmd_line_variant.py")

        if choice == 0:
            os.system("cd data/gui_variant && python3 eel_cpp_html_bridge.py")



    if choice == 0: # HIGHLIGHTS "START"
        print(clrs.LightGreen + '')
        print("                         +++++++++++++++++++++++++++++++++++++++++++")
        print("                         +                                         +")
        print("                         +               "  + clrs.BackgroundWhite + clrs.Black + "GUI-VARIANT" + clrs.ResetAll + '' + clrs.LightGreen + '' + "               +")
        print("                         +                                         +")
        print("                         +                  CLI                    +")
        print("                         +                                         +")
        print("                         +                  EXIT                   +")
        print("                         +                                         +")
        print("                         +++++++++++++++++++++++++++++++++++++++++++")


    if choice == 1: # HIGHLIGHTS "CREDITS"
        print(clrs.LightGreen + '')
        print("                         +++++++++++++++++++++++++++++++++++++++++++")
        print("                         +                                         +")
        print("                         +               GUI-VARIANT               +")
        print("                         +                                         +")
        print("                         +                  "  + clrs.BackgroundWhite + clrs.Black + "CLI" + clrs.ResetAll + '' + clrs.LightGreen + '' + "                    +")
        print("                         +                                         +")
        print("                         +                  EXIT                   +")
        print("                         +                                         +")
        print("                         +++++++++++++++++++++++++++++++++++++++++++")

    if choice == 2: # HIGHLIGHTS "EXIT"
        print(clrs.LightGreen + '')
        print("                         +++++++++++++++++++++++++++++++++++++++++++")
        print("                         +                                         +")
        print("                         +               GUI-VARIANT               +")
        print("                         +                                         +")
        print("                         +                  CLI                    +")
        print("                         +                                         +")
        print("                         +                  "  + clrs.BackgroundWhite + clrs.Black + "EXIT" + clrs.ResetAll + '' + clrs.LightGreen + '' + "                   +")
        print("                         +                                         +")
        print("                         +++++++++++++++++++++++++++++++++++++++++++")


    if choice > 2:
        choice = 0;

    if choice < 0:
        choice = 2;



    print(clrs.LightGreen + '')

    time.sleep(0.1)

    os.system("clear")