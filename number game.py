import time
import random
gameend=False
gamecontinue="y"
while gamecontinue=="y":
    num=random.randint(1,100)
    name=input("enter your name here:")
    print("hello",name," this game is called number guess")
    for i in range(5):
        choice=int(input("enter number here:"))
        if choice<1 or choice>100:
            print("enter numbers between 1 and 100")
        elif choice>num:
            print("too high")
        elif choice<num:
            print("too low")
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