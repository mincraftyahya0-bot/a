import time


def slowtype(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.09)
    print()


def clear():
    print("\033[H\033[2J", end="", flush=True)


def anim(n):
    for i in range(n):
        clear()
        print("|Ü|", flush=True)
        time.sleep(0.15)

        clear()
        print("|Ö|", flush=True)
        time.sleep(0.15)


anim(100)
