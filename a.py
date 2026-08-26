import sys
import time

def run_face_animation(msg,speed):
    def clear_screen():
        sys.stdout.write('\033[H\033[J')
        sys.stdout.flush()
    def open():
        