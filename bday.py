import time
import sys

def print_slow(text, delay=0.04):
    """Prints text with a typing effect to make it feel like an RPG game."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def start_game():
    print("=" * 60)
    print_slow("WELCOME TO THE ULTIMATE BIRTHDAY QUEST!")
    print("=" * 60)
    time.sleep(1)
    
    print_slow("\nYou wake up and find a locked terminal on your screen.")
    print_slow("A mysterious voice echoes: 'To claim your birthday gift, you must prove your worth!'")
    
    # Customize the recipient's name here
    name = input("\nEnter your name to begin: ").strip()
    
    print_slow(f"\nWelcome, {name}. Let's see if you can unlock your prize...")
    time.sleep(1)
    
    level_one()

def level_one():
    print("\n--- Level 1: The Trivia Lock ---")
    print_slow("[System]: First, a test of memory.")
    
    # CUSTOMIZE: Change this question and answer to something personal or funny!
    answer = input("What is my absolute favorite food in the entire world? ").strip().lower()
    
    if "cookie" in answer or "mango" in answer: # Put your actual answer criteria here
        print_slow("\nCORRECT! The terminal hums as the first lock clicks open.")
        time.sleep(1)
        level_two()
    else:
        print_slow("\nINCORRECT! The terminal buzzes angrily. Try again!")
        level_one()

def level_two():
    print("\n--- Level 2: The Riddle Gate ---")
    print_slow("[System]: You pass the first test. Now for a classic riddle.")
    print_slow("I have keys but open no locks. I have space but no room.")
    print_slow("You can enter, but you can't go outside. What am I?")
    
    riddle_ans = input("Your answer: ").strip().lower()
    
    if "keyboard" in riddle_ans:
        print_slow("\nGENIUS! You managed to solve it. Only one barrier remains...")
        time.sleep(1)
        level_three()
    else:
        print_slow("\nWRONG! The riddle gate remains closed. Think about what you are typing on!")
        level_two()

def level_three():
    print("\n--- Level 3: The Lucky Number ---")
    print_slow("[System]: Final security override required.")
    print_slow("To crack the encryption, guess the exact number I am thinking of between 1 and 10.")
    
    # CUSTOMIZE: Change this to their age or a special date number
    secret_number = "7" 
    
    guess = input("Enter your guess (1-10): ").strip()
    
    if guess == secret_number:
        print_slow("\nACCESS GRANTED! System override successful!!")
        time.sleep(1)
    else:
        print_slow(f"\nAccess Denied! '{guess}' is not the magic number. Try again.")
        level_three()


if __name__ == "__main__":
    start_game()
