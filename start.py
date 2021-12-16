import os
import keyboard
import time

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
            os.system("sudo python3 credits.py")



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