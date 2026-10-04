#activity1
class a():
    def __init__(self,a):
        self.a=a
    def __lt__(self,other):
        if self.a>other.a:
            return "self.a is bigger"
        else:
            return "other.a is bigger"
    def __eq__ (self,other):
        if self.a==other.a:
            return "equal"
        else:
            return "not equal"


obj_b=a(5)
obj_c=a(3)
#print(obj_b)
#print(obj_c)
print(obj_b < obj_c)
obj_1=a(4)
obj_2=a(4)
#print(obj_1)
#print(obj_2)
print(obj_1 == obj_2)
#activity2
class flashcards():
    def __init__(self,word,meaning):
        self.word=word
        self.meaning=meaning
    def __str__(self):
        return self.word+"("+self.meaning+")"
flash=[]
print("welcome to flashcard")
while True :
    w=input("enter word here :")
    m=input("enter meaning here :")

    flash.append(flashcards(w,m))

    opt=int(input("if you want to make another card,type 0 else,type 1 :"))
    if opt:
        break

print("\n flashcards: \n")
for i in flash:
    print(">",i)
#activity3
import random
class fruitquiz():
    def __init__ (self):
        self.fruits={"apple":"red","banana":"yellow","orange":"orange","mellon":"green"}
    def quiz(self):
        while True:
            fruit,color=random.choice(list(self.fruits.items()))
            print("what is the color of {}".format(fruit))
            inp=input()

            if inp.lower == color:
                print("correct")
            else:
                print("wrong")

            opt=int(input("if you want to play again,type 0 else,type 1 :"))

            if opt:
                break
print("Welcome to fruitquiz")
obj_fq=fruitquiz()
obj_fq.quiz()