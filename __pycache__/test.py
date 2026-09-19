import time
import random
gameend=False
gamecontinue="y"
while gamecontinue=="y":
    num=random.randint(1,50)
    name=input("enter your name here:")
    print("hello",name," this game is called number guess")
    hearts=5
    for i in range(6):
        print("you have", hearts, "hearts left")
        choice=int(input("enter number here:"))
        if choice<1 or choice>50:
            print("enter numbers between 1 and 50")
        elif choice in [45, 46, 47, 48, 49, 50]:
            print("ice cold")
        elif choice in [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44]:
            print("cold")
        elif choice in [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]:
            print("warm")
        elif choice in [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]:
            print("hot") 
        elif choice in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            print("boling hot")
        else:
            print("correct")
            gameend=True
        if gameend==True:
            gamecontinue=input("continue(y/n)")
            if gamecontinue=="y":
                gameend=False
                break
            else:
                print("thank you for playing")
                break
        hearts=hearts-1