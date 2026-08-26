import sys
import time
import os
dur= 1000
msg="Hi, Im your coding helper"
def clear_screen():
       os.system('cls' if os.name == 'nt' else 'clear')
def open():
        clear_screen()
        print(r" /(Ö)\ \n ",msg)
        time.sleep(dur)
def close():
        clear_screen()
        print(r" /(Ü)\ \n ",msg)
open()